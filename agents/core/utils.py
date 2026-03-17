"""Shared utilities for agent core modules."""

from __future__ import annotations

import json


def parse_json_response(text: str) -> dict:
    """Best-effort JSON parse, stripping markdown fences if present."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        lines = cleaned.split("\n")
        lines = [line for line in lines if not line.strip().startswith("```")]
        cleaned = "\n".join(lines)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {"raw_response": text, "_parse_error": True}
