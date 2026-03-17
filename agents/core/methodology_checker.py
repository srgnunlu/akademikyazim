"""Methodology Checker Agent — validates methodological consistency."""

from __future__ import annotations

import json
from pathlib import Path

from agents.core.utils import parse_json_response
from agents.providers.base import LLMProvider

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "methodology_checker.md"


class MethodologyCheckerAgent:
    """Validates research methodology for consistency and soundness."""

    def __init__(self, provider: LLMProvider, model: str | None = None):
        self.provider = provider
        self.model = model
        self.system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")

    async def run(
        self,
        methodology_text: str,
        research_question: str = "",
        field: str = "",
        document_type: str = "thesis",
    ) -> dict:
        """Run methodology validation.

        Returns parsed JSON with assessment, or raw text on parse failure.
        """
        user_payload = json.dumps({
            "research_question": research_question,
            "field": field,
            "methodology_text": methodology_text,
            "document_type": document_type,
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model)
        return parse_json_response(raw)
