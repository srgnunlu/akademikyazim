"""Draft Writer Agent — generates source-anchored section drafts.

Writes academic text section by section, ensuring every claim is backed
by a source. Produces A/B/C alternatives for user selection.

CRITICAL: Never generates core thesis, original arguments, data interpretation,
or conclusions. These are always presented as options for the user to choose.
"""

from __future__ import annotations

import json
from pathlib import Path

from agents.core.utils import parse_json_response
from agents.memory import AgentMemory
from agents.providers.base import LLMProvider

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "draft_writer.md"


class DraftWriterAgent:
    """Generates source-anchored draft sections with A/B/C alternatives."""

    def __init__(self, provider: LLMProvider, model: str | None = None):
        self.provider = provider
        self.model = model
        self.system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")

    async def run(
        self,
        section_title: str,
        section_type: str,
        outline: dict | None = None,
        arguments: list[dict] | None = None,
        source_notes: list[dict] | None = None,
        research_question: str = "",
        field: str = "",
        language: str = "tr",
        revision_feedback: str = "",
        memory: AgentMemory | None = None,
    ) -> dict:
        """Write a draft for a single section.

        Args:
            section_title: Title of the section to write.
            section_type: Type (intro, literature, method, results, discussion, conclusion).
            outline: Section outline with subsections and argument IDs.
            arguments: Relevant arguments for this section.
            source_notes: Source notes relevant to this section.
            research_question: The research question.
            field: Academic field.
            language: Output language (tr/en).
            revision_feedback: Feedback from self-critic for revision.
            memory: Shared agent memory.

        Returns:
            {
                "section_title": str,
                "section_type": str,
                "drafts": [
                    {
                        "id": "A",
                        "content": str,  # Full section text
                        "word_count": int,
                        "citations_used": [str],
                        "approach": str,  # Brief description of writing approach
                    },
                    {
                        "id": "B",
                        "content": str,
                        "word_count": int,
                        "citations_used": [str],
                        "approach": str,
                    },
                ],
                "writing_notes": str,
                "unsupported_claims": [str],
                "suggested_additions": [str],
            }
        """
        # Gather context from memory
        if memory:
            if not arguments:
                arg_data = memory.retrieve_value("argument_structure", {})
                arguments = arg_data.get("arguments", [])
            if not research_question:
                rq_data = memory.retrieve_value("research_questions", {})
                rqs = rq_data.get("research_questions", []) if rq_data else []
                if rqs:
                    research_question = rqs[0].get("question", "")
            if not source_notes:
                source_notes = memory.retrieve_value("source_notes", [])

        user_payload = json.dumps({
            "section_title": section_title,
            "section_type": section_type,
            "outline": outline or {},
            "arguments": arguments or [],
            "source_notes": _compress_notes(source_notes or []),
            "research_question": research_question,
            "field": field,
            "language": language,
            "revision_feedback": revision_feedback,
            "is_revision": bool(revision_feedback),
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.4)
        result = parse_json_response(raw)

        if memory and not result.get("_parse_error"):
            memory.store(
                f"draft_{section_type}",
                result,
                agent="draft_writer",
                metadata={"section_title": section_title, "section_type": section_type},
            )

        return result

    async def revise(
        self,
        draft: str,
        feedback: str,
        section_type: str,
        source_notes: list[dict] | None = None,
        memory: AgentMemory | None = None,
    ) -> dict:
        """Revise a draft based on self-critic feedback.

        Returns same structure as run() but with revised content.
        """
        return await self.run(
            section_title="(revision)",
            section_type=section_type,
            source_notes=source_notes,
            revision_feedback=feedback,
            memory=memory,
        )


def _compress_notes(notes: list[dict], max_total: int = 15000) -> list[dict]:
    """Compress notes to fit within context window."""
    compressed = []
    total_chars = 0
    for note in notes[:25]:
        entry = {
            "title": note.get("title", ""),
            "file": note.get("file", ""),
            "doi": note.get("doi", ""),
            "claims": note.get("claims", [])[:3],
            "keywords": note.get("keywords", [])[:5],
        }
        content = note.get("content", "")
        remaining = max_total - total_chars
        if remaining <= 0:
            break
        if len(content) > 400:
            content = content[:400] + "..."
        entry["excerpt"] = content
        total_chars += len(content)
        compressed.append(entry)
    return compressed
