"""Citation Verifier Agent — cross-checks citations against source PDFs."""

from __future__ import annotations

import json
from pathlib import Path

import pymupdf  # PyMuPDF

from agents.providers.base import LLMProvider

_PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "citation_verifier.md"


class CitationVerifierAgent:
    """Cross-checks claims against source document content."""

    def __init__(self, provider: LLMProvider, model: str | None = None):
        self.provider = provider
        self.model = model
        self.system_prompt = _PROMPT_PATH.read_text(encoding="utf-8")

    async def run(
        self,
        claim: str,
        source_path: str,
        source_metadata: dict | None = None,
    ) -> dict:
        """Verify a claim against a source document.

        Args:
            claim: The claim text including in-text citation.
            source_path: Path to the source PDF file.
            source_metadata: Optional dict with title, authors, year.

        Returns:
            Parsed JSON verification result.
        """
        source_text = _extract_pdf_text(source_path)
        if source_metadata is None:
            source_metadata = {"filename": Path(source_path).name}

        user_payload = json.dumps({
            "claim": claim,
            "source_content": source_text,
            "source_metadata": source_metadata,
        }, ensure_ascii=False)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_payload},
        ]

        raw = await self.provider.chat(messages, model=self.model)
        return _parse_json(raw)


def _extract_pdf_text(pdf_path: str, max_chars: int = 50_000) -> str:
    """Extract text from PDF using PyMuPDF. Truncates to max_chars."""
    doc = pymupdf.open(pdf_path)
    pages = []
    total = 0
    for page in doc:
        text = page.get_text()
        pages.append(f"--- Page {page.number + 1} ---\n{text}")
        total += len(text)
        if total >= max_chars:
            break
    doc.close()
    combined = "\n".join(pages)
    return combined[:max_chars]


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
