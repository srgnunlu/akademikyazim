"""Methodology Checker Agent — validates methodological consistency."""

from __future__ import annotations

import json
from pathlib import Path

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
        return _parse_json(raw)


def _parse_json(text: str) -> dict:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        lines = [l for l in lines if not l.strip().startswith("```")]
        cleaned = "\n".join(lines)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw_response": text, "_parse_error": True}
