"""Argument Builder Agent — constructs theoretical framework from sources.

Reads source notes and literature analysis to build argument hierarchy,
map support/counter-evidence, and generate outline structure.
"""

from __future__ import annotations

import json
from pathlib import Path

from agents.core.utils import parse_json_response
from agents.memory import AgentMemory
from agents.providers.base import LLMProvider

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "argument_builder.md"


class ArgumentBuilderAgent:
    """Builds theoretical framework and argument structure from literature."""

    def __init__(self, provider: LLMProvider, model: str | None = None):
        self.provider = provider
        self.model = model
        self.system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")

    async def run(
        self,
        research_question: str,
        literature_analysis: dict | None = None,
        source_notes: list[dict] | None = None,
        field: str = "",
        document_type: str = "article",
        language: str = "tr",
        memory: AgentMemory | None = None,
    ) -> dict:
        """Build argument structure from sources.

        Args:
            research_question: The refined research question.
            literature_analysis: Output from LiteratureAnalystAgent.
            source_notes: List of source note dicts.
            field: Academic field.
            document_type: Target document type.
            language: Output language.
            memory: Shared agent memory.

        Returns:
            {
                "theoretical_framework": {
                    "name": str,
                    "description": str,
                    "key_concepts": [str],
                },
                "arguments": [
                    {
                        "id": int,
                        "claim": str,
                        "type": "main|supporting|counter",
                        "evidence": [{"source": str, "quote": str, "page": str}],
                        "counter_evidence": [{"source": str, "quote": str}],
                        "strength": "strong|moderate|weak",
                        "parent_id": int | null,
                    },
                ],
                "argument_hierarchy": str,  # ASCII tree of argument structure
                "defense_armor": [
                    {
                        "argument_id": int,
                        "strongest_support": str,
                        "strongest_counter": str,
                        "rebuttal_strategy": str,
                    },
                ],
                "outline": {
                    "sections": [
                        {"title": str, "argument_ids": [int], "word_target": int},
                    ],
                },
                "warnings": [str],
            }
        """
        # Gather context from memory
        if memory:
            if not literature_analysis:
                literature_analysis = memory.retrieve_value("literature_analysis", {})
            if not source_notes:
                source_notes = memory.retrieve_value("source_notes", [])
            rq_data = memory.retrieve_value("research_questions", {})
            if rq_data and not research_question:
                # Use the recommended RQ
                rqs = rq_data.get("research_questions", [])
                if rqs:
                    research_question = rqs[0].get("question", research_question)

        user_payload = json.dumps({
            "research_question": research_question,
            "field": field,
            "document_type": document_type,
            "language": language,
            "literature_analysis": literature_analysis or {},
            "source_notes_summary": _summarize_notes(source_notes or []),
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.3)
        result = parse_json_response(raw)

        if memory and not result.get("_parse_error"):
            memory.store(
                "argument_structure",
                result,
                agent="argument_builder",
                persist=True,
            )

        return result

    async def generate_outline(
        self,
        arguments: list[dict],
        document_type: str = "article",
        language: str = "tr",
    ) -> dict:
        """Generate a detailed outline from the argument structure.

        Returns:
            {"sections": [{"title": str, "subsections": [...], "argument_ids": [int]}]}
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": json.dumps({
                "task": "generate_outline",
                "arguments": arguments,
                "document_type": document_type,
                "language": language,
            }, ensure_ascii=False)},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.3)
        return parse_json_response(raw)


def _summarize_notes(notes: list[dict], max_per_note: int = 500) -> list[dict]:
    """Summarize source notes to fit within context limits."""
    summaries = []
    for note in notes[:30]:  # Cap at 30 sources
        summary = {
            "title": note.get("title", ""),
            "file": note.get("file", ""),
            "claims": note.get("claims", [])[:5],
            "keywords": note.get("keywords", [])[:8],
        }
        # Truncate content
        content = note.get("content", "")
        if len(content) > max_per_note:
            content = content[:max_per_note] + "..."
        summary["content_preview"] = content
        summaries.append(summary)
    return summaries
