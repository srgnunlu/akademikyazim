"""Context window management for agent conversations.

Handles chunking, prioritization, and summarization of long documents
to fit within LLM context windows.

Usage:
    from agents.context import ContextManager
    ctx = ContextManager(max_tokens=8000)
    ctx.add("source_notes", notes_text, priority=1)
    ctx.add("arguments", args_text, priority=2)
    messages = ctx.build_messages(system_prompt, user_prompt)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class ContextBlock:
    """A block of context with priority and metadata."""

    key: str
    content: str
    priority: int = 5  # 1 = highest priority, 10 = lowest
    max_chars: int = 0  # 0 = no limit
    truncatable: bool = True

    @property
    def char_count(self) -> int:
        return len(self.content)

    @property
    def estimated_tokens(self) -> int:
        # Rough estimate: 1 token ≈ 4 chars for English, ~3 for Turkish
        return self.char_count // 3


class ContextManager:
    """Manages context window allocation for LLM conversations."""

    def __init__(self, max_tokens: int = 16000):
        self.max_tokens = max_tokens
        self._blocks: list[ContextBlock] = []

    def add(
        self,
        key: str,
        content: str,
        priority: int = 5,
        max_chars: int = 0,
        truncatable: bool = True,
    ) -> None:
        """Add a context block."""
        self._blocks.append(ContextBlock(
            key=key,
            content=content,
            priority=priority,
            max_chars=max_chars,
            truncatable=truncatable,
        ))

    def build_context(self) -> str:
        """Build the context string, fitting within token budget."""
        # Sort by priority (lower = higher priority)
        sorted_blocks = sorted(self._blocks, key=lambda b: b.priority)

        # Estimate budget per block
        total_estimated = sum(b.estimated_tokens for b in sorted_blocks)
        budget_chars = self.max_tokens * 3  # rough token-to-char conversion

        parts = []
        used_chars = 0

        for block in sorted_blocks:
            remaining = budget_chars - used_chars
            if remaining <= 0:
                break

            content = block.content

            # Apply max_chars limit
            if block.max_chars and len(content) > block.max_chars:
                content = _smart_truncate(content, block.max_chars)

            # Truncate to fit remaining budget
            if block.truncatable and len(content) > remaining:
                content = _smart_truncate(content, int(remaining))

            if content:
                parts.append(f"### {block.key}\n{content}")
                used_chars += len(content)

        return "\n\n".join(parts)

    def build_messages(
        self,
        system_prompt: str,
        user_prompt: str,
    ) -> list[dict]:
        """Build a messages list with context injected."""
        context = self.build_context()

        # Reserve tokens for system prompt and user prompt
        system_tokens = len(system_prompt) // 3
        user_tokens = len(user_prompt) // 3
        overhead = system_tokens + user_tokens + 500  # margin

        # Rebuild context with adjusted budget
        old_max = self.max_tokens
        self.max_tokens = max(1000, self.max_tokens - overhead)
        context = self.build_context()
        self.max_tokens = old_max

        messages = [{"role": "system", "content": system_prompt}]

        if context:
            messages.append({
                "role": "user",
                "content": f"## Context\n\n{context}\n\n---\n\n## Task\n\n{user_prompt}",
            })
        else:
            messages.append({"role": "user", "content": user_prompt})

        return messages

    def clear(self) -> None:
        self._blocks.clear()


def _smart_truncate(text: str, max_chars: int) -> str:
    """Truncate text at a natural boundary (paragraph or sentence)."""
    if len(text) <= max_chars:
        return text

    # Try to truncate at paragraph boundary
    truncated = text[:max_chars]
    last_para = truncated.rfind("\n\n")
    if last_para > max_chars * 0.5:
        return truncated[:last_para] + "\n\n[... truncated]"

    # Try sentence boundary
    last_sentence = max(truncated.rfind(". "), truncated.rfind(".\n"))
    if last_sentence > max_chars * 0.5:
        return truncated[:last_sentence + 1] + " [... truncated]"

    # Hard truncate
    return truncated + "... [truncated]"


def chunk_academic_text(text: str, chunk_size: int = 4000) -> list[str]:
    """Split academic text into chunks at section boundaries."""
    # Split by section headers
    sections = re.split(r"\n(?=#{1,3}\s)", text)

    chunks = []
    current_chunk = ""

    for section in sections:
        if len(current_chunk) + len(section) > chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = section
        else:
            current_chunk += "\n" + section

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def summarize_for_context(text: str, max_chars: int = 2000) -> str:
    """Extract the most important parts of a text for context injection."""
    if len(text) <= max_chars:
        return text

    lines = text.splitlines()
    important = []
    total = 0

    for line in lines:
        # Prioritize: headers, bullet points, claims, citations
        is_important = (
            line.startswith("#")
            or line.startswith("- ")
            or line.startswith("* ")
            or bool(re.search(r"\(\d{4}\)", line))  # year citation
            or bool(re.search(r"\b(finds?|shows?|argues?|concludes?)\b", line, re.I))
        )
        if is_important:
            important.append(line)
            total += len(line)
            if total >= max_chars:
                break

    if not important:
        return text[:max_chars] + "... [truncated]"

    return "\n".join(important)
