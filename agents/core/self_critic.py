"""Self-Critic Agent — multi-layer review and iterative improvement.

Reviews drafts across 4 dimensions:
1. Argument consistency
2. Source verification (via citation_verifier)
3. Style quality (via style_linter)
4. Literature alignment

Returns structured feedback for the draft_writer to iterate on.
"""

from __future__ import annotations

import json
from pathlib import Path

from agents.core.utils import parse_json_response
from agents.memory import AgentMemory
from agents.providers.base import LLMProvider
from agents.tools import ToolRegistry

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "self_critic.md"


class SelfCriticAgent:
    """Reviews and critiques drafts with multi-layer analysis."""

    def __init__(
        self,
        provider: LLMProvider,
        model: str | None = None,
        tool_registry: ToolRegistry | None = None,
    ):
        self.provider = provider
        self.model = model
        self.tools = tool_registry
        self.system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")

    async def run(
        self,
        draft_text: str,
        section_type: str = "",
        research_question: str = "",
        arguments: list[dict] | None = None,
        source_notes: list[dict] | None = None,
        memory: AgentMemory | None = None,
    ) -> dict:
        """Review a draft section and produce structured feedback.

        Args:
            draft_text: The draft text to review.
            section_type: Section type (intro, literature, method, etc.).
            research_question: The research question.
            arguments: Expected arguments for this section.
            source_notes: Available source notes for verification.
            memory: Shared agent memory.

        Returns:
            {
                "overall_score": float,  # 0-10
                "pass": bool,  # True if score >= 7
                "layers": {
                    "argument_consistency": {
                        "score": float,
                        "issues": [{"location": str, "issue": str, "suggestion": str}],
                    },
                    "source_verification": {
                        "score": float,
                        "unsupported_claims": [str],
                        "missing_citations": [str],
                    },
                    "style_quality": {
                        "score": float,
                        "issues": [{"type": str, "location": str, "suggestion": str}],
                    },
                    "literature_alignment": {
                        "score": float,
                        "gaps": [str],
                        "unused_relevant_sources": [str],
                    },
                },
                "revision_instructions": str,
                "priority_fixes": [str],
            }
        """
        # Gather context from memory
        if memory:
            if not arguments:
                arg_data = memory.retrieve_value("argument_structure", {})
                arguments = arg_data.get("arguments", []) if arg_data else []
            if not research_question:
                rq_data = memory.retrieve_value("research_questions", {})
                rqs = rq_data.get("research_questions", []) if rq_data else []
                if rqs:
                    research_question = rqs[0].get("question", "")

        # Run style linter if available
        style_report = {}
        if self.tools and self.tools.get("style_lint"):
            try:
                style_report = await self.tools.execute(
                    "style_lint", {"file": "_inline_", "text": draft_text}
                )
            except Exception:
                pass

        user_payload = json.dumps({
            "draft_text": draft_text,
            "section_type": section_type,
            "research_question": research_question,
            "arguments": arguments or [],
            "source_notes_summary": [
                {"title": n.get("title", ""), "claims": n.get("claims", [])[:3]}
                for n in (source_notes or [])[:15]
            ],
            "style_report": style_report,
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.2)
        result = parse_json_response(raw)

        if memory and not result.get("_parse_error"):
            memory.store(
                f"review_{section_type}",
                result,
                agent="self_critic",
                metadata={"section_type": section_type},
            )

        return result

    async def review_full_document(
        self,
        sections: list[dict],
        research_question: str = "",
        memory: AgentMemory | None = None,
    ) -> dict:
        """Review the complete document for coherence and consistency.

        Args:
            sections: List of {"title": str, "type": str, "content": str}.
            research_question: The research question.

        Returns:
            {
                "overall_score": float,
                "coherence_score": float,
                "section_scores": [{"section": str, "score": float}],
                "cross_section_issues": [str],
                "rq_alignment": float,
                "revision_priorities": [str],
            }
        """
        combined = "\n\n".join(
            f"## {s.get('title', s.get('type', 'Section'))}\n{s.get('content', '')[:2000]}"
            for s in sections
        )

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": json.dumps({
                "task": "full_document_review",
                "document": combined,
                "research_question": research_question,
                "section_count": len(sections),
            }, ensure_ascii=False)},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.2)
        result = parse_json_response(raw)

        if memory and not result.get("_parse_error"):
            memory.store(
                "full_document_review",
                result,
                agent="self_critic",
                persist=True,
            )

        return result
