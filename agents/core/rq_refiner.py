"""Research Question Refiner Agent — transforms vague ideas into research questions.

Takes a raw idea/topic from the user and produces 3 alternative research
questions with scope analysis, feasibility assessment, and originality check.
"""

from __future__ import annotations

import json
from pathlib import Path

from agents.core.utils import parse_json_response
from agents.memory import AgentMemory
from agents.providers.base import LLMProvider

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "rq_refiner.md"


class RQRefinerAgent:
    """Refines a vague research idea into structured research questions."""

    def __init__(self, provider: LLMProvider, model: str | None = None):
        self.provider = provider
        self.model = model
        self.system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")

    async def run(
        self,
        idea: str,
        field: str = "",
        document_type: str = "article",
        language: str = "tr",
        existing_literature: str = "",
        memory: AgentMemory | None = None,
    ) -> dict:
        """Refine a research idea into 3 research question alternatives.

        Args:
            idea: The raw research idea or topic from the user.
            field: Academic field (e.g., economics, law, medicine).
            document_type: Target document type (article, thesis, etc.).
            language: Output language (tr/en/both).
            existing_literature: Optional context from prior literature search.
            memory: Optional shared memory for context.

        Returns:
            {
                "original_idea": str,
                "research_questions": [
                    {
                        "id": "RQ1",
                        "question": str,
                        "type": "descriptive|explanatory|exploratory",
                        "scope": str,
                        "feasibility": "high|medium|low",
                        "originality_assessment": str,
                        "suggested_methodology": str,
                        "key_variables": [str],
                    },
                    ...  # 3 alternatives
                ],
                "recommendation": str,  # which RQ is strongest and why
                "scope_warnings": [str],
            }
        """
        # Build context from memory if available
        context = ""
        if memory:
            entries = memory.search(idea, top_k=3)
            if entries:
                context = "\n".join(
                    f"- [{e.agent}] {e.key}: {json.dumps(e.value, ensure_ascii=False, default=str)[:300]}"
                    for e in entries
                )

        user_payload = json.dumps({
            "idea": idea,
            "field": field,
            "document_type": document_type,
            "language": language,
            "existing_literature_context": existing_literature or context,
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model, temperature=0.4)
        result = parse_json_response(raw)

        # Store in memory
        if memory and not result.get("_parse_error"):
            memory.store(
                "research_questions",
                result,
                agent="rq_refiner",
                persist=True,
            )

        return result
