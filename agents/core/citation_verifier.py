"""Citation Verifier Agent — cross-checks citations against source PDFs."""

from __future__ import annotations

import json
import logging
from pathlib import Path

import pymupdf  # PyMuPDF

from agents.core.utils import parse_json_response
from agents.providers.base import LLMProvider

logger = logging.getLogger(__name__)

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
        return parse_json_response(raw)


def _extract_pdf_text(pdf_path: str, max_chars: int = 50_000) -> str:
    """Extract text from PDF using PyMuPDF. Truncates to max_chars."""
    try:
        doc = pymupdf.open(pdf_path)
    except (FileNotFoundError, RuntimeError, PermissionError) as exc:
        logger.error("Cannot open PDF %s: %s", pdf_path, exc)
        raise

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
