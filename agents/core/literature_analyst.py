"""Literature Analyst Agent — analyzes and synthesizes found sources.

Goes beyond source_hunter by evaluating quality, clustering by theme,
detecting gaps and contradictions, and producing structured analysis outputs.
"""

from __future__ import annotations

import json
from pathlib import Path

from agents.core.utils import parse_json_response
from agents.memory import AgentMemory
from agents.providers.base import ChatResponse, LLMProvider
from agents.tools import ToolRegistry

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "literature_analyst.md"


class LiteratureAnalystAgent:
    """Analyzes literature sources for quality, themes, gaps, and contradictions."""

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
        research_question: str,
        field: str = "",
        source_notes: list[dict] | None = None,
        memory: AgentMemory | None = None,
    ) -> dict:
        """Analyze literature sources and produce structured analysis.

        Args:
            research_question: The research question driving the analysis.
            field: Academic field.
            source_notes: List of source note dicts (from notes/ folder).
            memory: Shared agent memory.

        Returns:
            {
                "source_count": int,
                "quality_assessment": [
                    {"source": str, "quality_score": float, "strengths": [str], "weaknesses": [str]},
                ],
                "theme_clusters": [
                    {"theme": str, "sources": [str], "summary": str},
                ],
                "gaps": [str],
                "contradictions": [
                    {"claim_a": str, "source_a": str, "claim_b": str, "source_b": str},
                ],
                "saturation_estimate": float,
                "recommendations": [str],
            }
        """
        # Gather source notes from project if not provided
        if not source_notes and memory:
            notes_data = memory.retrieve_value("source_notes", [])
            if notes_data:
                source_notes = notes_data

        # Run existing analysis tools if available
        tool_results = {}
        if self.tools:
            tool_results = await self._run_analysis_tools()

        user_payload = json.dumps({
            "research_question": research_question,
            "field": field,
            "source_notes": source_notes or [],
            "tool_analysis": tool_results,
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.3)
        result = parse_json_response(raw)

        if memory and not result.get("_parse_error"):
            memory.store(
                "literature_analysis",
                result,
                agent="literature_analyst",
                persist=True,
            )

        return result

    async def _run_analysis_tools(self) -> dict:
        """Run existing TezAtlas analysis scripts via tool registry."""
        results = {}
        tool_names = ["run_intake", "run_contradiction_scan", "run_gap_scan"]
        for name in tool_names:
            if self.tools and self.tools.get(name):
                try:
                    result = await self.tools.execute(name, {})
                    results[name] = result
                except Exception:
                    pass
        return results

    async def assess_source_quality(
        self,
        source_metadata: dict,
        memory: AgentMemory | None = None,
    ) -> dict:
        """Assess the quality of a single source.

        Args:
            source_metadata: Dict with title, authors, year, venue, citation_count, etc.

        Returns:
            {"quality_score": float, "tier": "A|B|C", "reasons": [str]}
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": json.dumps({
                "task": "assess_source_quality",
                "source": source_metadata,
            }, ensure_ascii=False)},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.2)
        return parse_json_response(raw)
