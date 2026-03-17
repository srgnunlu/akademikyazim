"""Tests for agents/tools.py and provider tool-calling support."""

from __future__ import annotations

from pathlib import Path

import pytest

from agents.providers.base import ChatResponse, ToolCall
from agents.tools import ToolDef, ToolRegistry


@pytest.fixture
def temp_project(tmp_path):
    # Create minimal project structure
    (tmp_path / "sources").mkdir()
    (tmp_path / "notes").mkdir()
    return tmp_path


class TestToolDef:
    def test_openai_schema(self):
        tool = ToolDef(
            name="test_tool",
            description="A test tool",
            parameters={
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
            execute=lambda **kw: {"result": "ok"},
        )
        schema = tool.to_openai_schema()
        assert schema["type"] == "function"
        assert schema["function"]["name"] == "test_tool"
        assert schema["function"]["description"] == "A test tool"
        assert "query" in schema["function"]["parameters"]["properties"]

    def test_anthropic_schema(self):
        tool = ToolDef(
            name="test_tool",
            description="A test tool",
            parameters={"type": "object", "properties": {}},
            execute=lambda **kw: {},
        )
        schema = tool.to_anthropic_schema()
        assert schema["name"] == "test_tool"
        assert "input_schema" in schema


class TestToolRegistry:
    def test_register_and_get(self, temp_project):
        registry = ToolRegistry(temp_project)
        custom_tool = ToolDef(
            name="custom",
            description="Custom tool",
            parameters={"type": "object", "properties": {}},
            execute=lambda **kw: {"ok": True},
        )
        registry.register(custom_tool)
        assert registry.get("custom") is not None
        assert registry.get("nonexistent") is None

    def test_builtin_tools_registered(self, temp_project):
        registry = ToolRegistry(temp_project)
        tools = registry.list_tools()
        # Should have the built-in tools
        assert "search_papers" in tools
        assert "run_intake" in tools
        assert "run_gap_scan" in tools
        assert "run_contradiction_scan" in tools
        assert "check_phase_gate" in tools

    def test_get_tool_definitions_openai(self, temp_project):
        registry = ToolRegistry(temp_project)
        defs = registry.get_tool_definitions(format="openai")
        assert len(defs) > 0
        assert all(d["type"] == "function" for d in defs)

    def test_get_tool_definitions_anthropic(self, temp_project):
        registry = ToolRegistry(temp_project)
        defs = registry.get_tool_definitions(format="anthropic")
        assert len(defs) > 0
        assert all("name" in d and "input_schema" in d for d in defs)

    @pytest.mark.asyncio
    async def test_execute_unknown_tool(self, temp_project):
        registry = ToolRegistry(temp_project)
        result = await registry.execute("nonexistent", {})
        assert "error" in result


class TestChatResponse:
    def test_basic(self):
        resp = ChatResponse(text="hello")
        assert resp.text == "hello"
        assert not resp.has_tool_calls
        assert resp.finish_reason == "stop"

    def test_with_tool_calls(self):
        resp = ChatResponse(
            text="",
            tool_calls=[
                ToolCall(id="tc_1", name="search_papers", arguments={"query": "test"}),
            ],
        )
        assert resp.has_tool_calls
        assert len(resp.tool_calls) == 1
        assert resp.tool_calls[0].name == "search_papers"
        assert resp.tool_calls[0].arguments == {"query": "test"}


class TestToolCall:
    def test_fields(self):
        tc = ToolCall(id="tc_1", name="test", arguments={"a": 1})
        assert tc.id == "tc_1"
        assert tc.name == "test"
        assert tc.arguments == {"a": 1}
