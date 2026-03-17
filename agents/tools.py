"""Agent tool registry — exposes existing scripts/APIs as callable tools.

Agents use LLM function-calling to invoke these tools. Each tool is defined
with a name, description, parameter schema (OpenAI function-calling format),
and an execute function.

Usage:
    from agents.tools import ToolRegistry
    registry = ToolRegistry(project_dir)
    result = await registry.execute("search_papers", {"query": "..."})
    tool_defs = registry.get_tool_definitions()  # for LLM function-calling
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

logger = logging.getLogger(__name__)

_ROOT = Path(__file__).resolve().parent.parent


@dataclass
class ToolDef:
    """A tool definition for LLM function-calling."""

    name: str
    description: str
    parameters: dict  # JSON Schema
    execute: Callable[..., Any]

    def to_openai_schema(self) -> dict:
        """Convert to OpenAI function-calling format."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }

    def to_anthropic_schema(self) -> dict:
        """Convert to Anthropic tool_use format."""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.parameters,
        }


def _run_script(script_name: str, args: dict, project_dir: Path) -> dict:
    """Run a TezAtlas script as a subprocess and return parsed output."""
    script_path = _ROOT / "scripts" / script_name
    if not script_path.exists():
        return {"error": f"Script not found: {script_name}"}

    cmd = [sys.executable, str(script_path)]

    # Add project dir
    if "--project-dir" not in str(args):
        cmd.extend(["--project-dir", str(project_dir)])

    # Convert args dict to CLI flags
    for key, value in args.items():
        flag = f"--{key.replace('_', '-')}"
        if isinstance(value, bool):
            if value:
                cmd.append(flag)
        elif isinstance(value, list):
            for v in value:
                cmd.extend([flag, str(v)])
        else:
            cmd.extend([flag, str(value)])

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=120, cwd=str(_ROOT)
        )
        output = result.stdout.strip()
        if result.returncode != 0:
            return {
                "error": f"Script exited with code {result.returncode}",
                "stderr": result.stderr.strip()[:500],
                "stdout": output[:500],
            }
        # Try parsing as JSON
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            return {"output": output[:2000]}
    except subprocess.TimeoutExpired:
        return {"error": "Script timed out after 120s"}
    except Exception as exc:
        return {"error": str(exc)}


class ToolRegistry:
    """Registry of tools available to agents via function-calling."""

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self._tools: dict[str, ToolDef] = {}
        self._register_builtin_tools()

    def register(self, tool: ToolDef) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> ToolDef | None:
        return self._tools.get(name)

    def list_tools(self) -> list[str]:
        return list(self._tools.keys())

    def get_tool_definitions(self, format: str = "openai") -> list[dict]:
        """Get all tool definitions in the specified format."""
        if format == "anthropic":
            return [t.to_anthropic_schema() for t in self._tools.values()]
        return [t.to_openai_schema() for t in self._tools.values()]

    async def execute(self, name: str, arguments: dict) -> Any:
        """Execute a tool by name with given arguments."""
        tool = self._tools.get(name)
        if not tool:
            return {"error": f"Unknown tool: {name}"}
        try:
            result = tool.execute(**arguments)
            return result
        except Exception as exc:
            logger.error("Tool '%s' failed: %s", name, exc)
            return {"error": str(exc)}

    def _register_builtin_tools(self) -> None:
        """Register all built-in TezAtlas tools."""
        pd = self.project_dir

        # ── Academic Search ──────────────────────────────────────
        self.register(ToolDef(
            name="search_papers",
            description="Search for academic papers across Semantic Scholar, OpenAlex, and CrossRef. Returns ranked results with DOI, citation count, and PDF links.",
            parameters={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query for academic papers"},
                    "limit": {"type": "integer", "description": "Max results to return", "default": 10},
                },
                "required": ["query"],
            },
            execute=lambda **kw: _run_script("find_source.py", {**kw, "format": "json"}, pd),
        ))

        # ── Source Intake ────────────────────────────────────────
        self.register(ToolDef(
            name="run_intake",
            description="Cluster all sources in sources/ folder, extract core claims, flag contradictions. Produces SOURCE_MAP.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("intake_protocol.py", kw, pd),
        ))

        # ── Contradiction Scanner ────────────────────────────────
        self.register(ToolDef(
            name="run_contradiction_scan",
            description="Scan across all source notes for contradictions. Produces CONTRADICTIONS.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("contradiction_scan.py", kw, pd),
        ))

        # ── Gap Scanner ──────────────────────────────────────────
        self.register(ToolDef(
            name="run_gap_scan",
            description="Identify research gaps and unanswered questions from source notes. Produces GAPS.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("gap_scanner.py", kw, pd),
        ))

        # ── Citation Chain ───────────────────────────────────────
        self.register(ToolDef(
            name="run_citation_chain",
            description="Trace intellectual lineage: who started, challenged, developed ideas. Produces CITATION_CHAIN.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("citation_chain.py", kw, pd),
        ))

        # ── Snowball Sampling ────────────────────────────────────
        self.register(ToolDef(
            name="run_snowball",
            description="Extract DOIs from source notes and PDFs for snowball sampling. Produces SNOWBALL_CANDIDATES.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("snowball.py", kw, pd),
        ))

        # ── Saturation Check ────────────────────────────────────
        self.register(ToolDef(
            name="check_saturation",
            description="Check argument coverage across sources and determine if reading saturation is reached.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("saturation_map.py", kw, pd),
        ))

        # ── Style Lint ───────────────────────────────────────────
        self.register(ToolDef(
            name="style_lint",
            description="Check academic writing quality: passive voice, hedging, over-claiming, readability.",
            parameters={
                "type": "object",
                "properties": {
                    "file": {"type": "string", "description": "Path to draft file to lint"},
                },
                "required": ["file"],
            },
            execute=lambda **kw: _run_script(
                "../tools/style_linter.py", kw, pd
            ),
        ))

        # ── Phase Gate Check ─────────────────────────────────────
        self.register(ToolDef(
            name="check_phase_gate",
            description="Check if conditions for advancing to the next phase are met.",
            parameters={
                "type": "object",
                "properties": {
                    "current_phase": {"type": "integer", "description": "Current phase number"},
                    "target_phase": {"type": "integer", "description": "Target phase number"},
                },
                "required": ["current_phase", "target_phase"],
            },
            execute=lambda **kw: _run_script("phase_gate_check.py", kw, pd),
        ))

        # ── Synthesize ──────────────────────────────────────────
        self.register(ToolDef(
            name="run_synthesize",
            description="Multi-source synthesis by argument across all source notes. Produces SYNTHESIS.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("synthesize.py", kw, pd),
        ))

        # ── Knowledge Map ───────────────────────────────────────
        self.register(ToolDef(
            name="run_knowledge_map",
            description="Map field structure: pillars, contentions, and boundaries. Produces KNOWLEDGE_MAP.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("knowledge_map.py", kw, pd),
        ))

        # ── RQ Drift Check ──────────────────────────────────────
        self.register(ToolDef(
            name="check_rq_drift",
            description="Detect research question drift by comparing current draft against original RQ.",
            parameters={
                "type": "object",
                "properties": {
                    "file": {"type": "string", "description": "Path to draft file to check"},
                },
                "required": ["file"],
            },
            execute=lambda **kw: _run_script("rq_drift.py", kw, pd),
        ))

        # ── Reading Tracker ─────────────────────────────────────
        self.register(ToolDef(
            name="reading_status",
            description="Get current reading progress: sources read vs total, coverage by argument.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("reading_tracker.py", {**kw, "action": "status"}, pd),
        ))

        # ── Assumption Killer ───────────────────────────────────
        self.register(ToolDef(
            name="run_assumptions",
            description="Find untested assumptions across source notes with risk analysis. Produces ASSUMPTIONS.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("assumption_killer.py", kw, pd),
        ))

        # ── So What Test ────────────────────────────────────────
        self.register(ToolDef(
            name="run_so_what",
            description="Run the 'So What?' significance test: generate 3 essential statements. Produces SO_WHAT.md.",
            parameters={
                "type": "object",
                "properties": {},
            },
            execute=lambda **kw: _run_script("so_what_test.py", kw, pd),
        ))
