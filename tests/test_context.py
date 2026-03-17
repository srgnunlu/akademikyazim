"""Tests for agents/context.py — context window management."""

from __future__ import annotations

import pytest

from agents.context import ContextManager, chunk_academic_text, summarize_for_context


class TestContextManager:
    def test_basic_build(self):
        ctx = ContextManager(max_tokens=5000)
        ctx.add("notes", "Some source notes", priority=1)
        ctx.add("arguments", "Some arguments", priority=2)

        result = ctx.build_context()
        assert "notes" in result
        assert "arguments" in result

    def test_priority_ordering(self):
        ctx = ContextManager(max_tokens=5000)
        ctx.add("low_priority", "LOW", priority=10)
        ctx.add("high_priority", "HIGH", priority=1)

        result = ctx.build_context()
        # High priority should come first
        high_pos = result.index("HIGH")
        low_pos = result.index("LOW")
        assert high_pos < low_pos

    def test_truncation_under_budget(self):
        ctx = ContextManager(max_tokens=100)  # Very small budget
        ctx.add("big_block", "x" * 5000, priority=1, truncatable=True)

        result = ctx.build_context()
        assert len(result) < 5000
        assert "truncated" in result.lower()

    def test_build_messages(self):
        ctx = ContextManager(max_tokens=5000)
        ctx.add("data", "test data", priority=1)

        messages = ctx.build_messages("You are a bot.", "Do something.")
        assert len(messages) == 2
        assert messages[0]["role"] == "system"
        assert messages[0]["content"] == "You are a bot."
        assert "test data" in messages[1]["content"]
        assert "Do something" in messages[1]["content"]

    def test_empty_context(self):
        ctx = ContextManager(max_tokens=5000)
        messages = ctx.build_messages("system", "user prompt")
        assert len(messages) == 2
        assert messages[1]["content"] == "user prompt"

    def test_clear(self):
        ctx = ContextManager()
        ctx.add("a", "b")
        ctx.clear()
        assert ctx.build_context() == ""


class TestChunkAcademicText:
    def test_basic_chunking(self):
        text = "## Section 1\nContent 1\n\n## Section 2\nContent 2\n\n## Section 3\nContent 3"
        chunks = chunk_academic_text(text, chunk_size=50)
        assert len(chunks) >= 2

    def test_single_chunk(self):
        text = "Short text"
        chunks = chunk_academic_text(text, chunk_size=1000)
        assert len(chunks) == 1
        assert chunks[0].strip() == "Short text"


class TestSummarizeForContext:
    def test_short_text_unchanged(self):
        text = "Short text"
        assert summarize_for_context(text, max_chars=100) == text

    def test_extracts_important_lines(self):
        text = """# Header
Regular line
- Bullet point
Another line
Smith (2020) argues that X
Regular line again
The study finds that Y"""
        result = summarize_for_context(text, max_chars=200)
        assert "Header" in result
        assert "Bullet point" in result
        assert "Smith (2020)" in result
