#!/usr/bin/env python3
"""TezAtlas Multi-Agent CLI — run agents from the command line.

Usage:
    python agents/run.py source_hunter --research-question "..." --field economics
    python agents/run.py methodology_checker --input methodology.md --research-question "..."
    python agents/run.py citation_verifier --claim "..." --source sources/file.pdf
    python agents/run.py --list-providers
    python agents/run.py --test-providers
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from pathlib import Path

# Ensure project root is on sys.path so `agents` package resolves
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from agents.config import AgentConfig
from agents.core.source_hunter import SourceHunterAgent
from agents.core.methodology_checker import MethodologyCheckerAgent
from agents.core.citation_verifier import CitationVerifierAgent


def _print_json(data: dict) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False))


# ── List providers ──────────────────────────────────────────────

def cmd_list_providers(config: AgentConfig) -> None:
    print("=== Configured Providers ===\n")
    for p in config.list_providers():
        key_status = "SET" if p["api_key_set"] else "NOT SET"
        print(f"  {p['name']}")
        print(f"    Type:    {p['type']}")
        print(f"    Base:    {p['base_url']}")
        print(f"    Model:   {p['default_model']}")
        print(f"    Key env: {p['api_key_env']} ({key_status})")
        print()

    print("=== Agent Assignments ===\n")
    for a in config.list_agents():
        model = a["model"] or "(provider default)"
        print(f"  {a['name']}  →  {a['provider']} / {model}")
        print(f"    {a['description']}")
        print()


# ── Test providers ──────────────────────────────────────────────

async def _test_providers(config: AgentConfig) -> None:
    print("=== Provider Health Check ===\n")
    for info in config.list_providers():
        name = info["name"]
        if not info["api_key_set"] and info["api_key_env"].lower() != "none":
            print(f"  {name}: SKIPPED (no API key)")
            continue
        try:
            provider = config.get_provider(name)
            result = await provider.health_check()
            status = result["status"].upper()
            detail = result.get("detail", "")
            print(f"  {name}: {status} — {detail}")
        except Exception as exc:
            print(f"  {name}: ERROR — {exc}")
    print()


def cmd_test_providers(config: AgentConfig) -> None:
    asyncio.run(_test_providers(config))


# ── Source Hunter ───────────────────────────────────────────────

async def _run_source_hunter(config: AgentConfig, args: argparse.Namespace) -> None:
    provider, model = config.get_agent_provider("source_hunter")
    agent = SourceHunterAgent(provider, model)

    existing = []
    if args.existing_sources:
        src_dir = Path(args.existing_sources)
        if src_dir.is_dir():
            existing = [f.stem for f in src_dir.iterdir() if f.suffix == ".pdf"]

    result = await agent.run(
        research_question=args.research_question,
        field=args.field or "",
        existing_sources=existing,
        language_preference=args.language or "both",
    )
    _print_json(result)


# ── Methodology Checker ────────────────────────────────────────

async def _run_methodology_checker(config: AgentConfig, args: argparse.Namespace) -> None:
    provider, model = config.get_agent_provider("methodology_checker")
    agent = MethodologyCheckerAgent(provider, model)

    input_path = Path(args.input)
    if input_path.exists():
        methodology_text = input_path.read_text(encoding="utf-8")
    else:
        methodology_text = args.input  # treat as inline text

    result = await agent.run(
        methodology_text=methodology_text,
        research_question=args.research_question or "",
        field=args.field or "",
        document_type=args.document_type or "thesis",
    )
    _print_json(result)


# ── Citation Verifier ──────────────────────────────────────────

async def _run_citation_verifier(config: AgentConfig, args: argparse.Namespace) -> None:
    provider, model = config.get_agent_provider("citation_verifier")
    agent = CitationVerifierAgent(provider, model)

    result = await agent.run(
        claim=args.claim,
        source_path=args.source,
    )
    _print_json(result)


# ── Argument parser ────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agents/run.py",
        description="TezAtlas Multi-Agent CLI",
    )
    parser.add_argument(
        "--list-providers", action="store_true",
        help="Show all configured providers and agent assignments",
    )
    parser.add_argument(
        "--test-providers", action="store_true",
        help="Health-check all configured providers",
    )
    parser.add_argument(
        "--config", type=str, default=None,
        help="Path to agents.yaml (default: project root)",
    )

    sub = parser.add_subparsers(dest="agent")

    # source_hunter
    sh = sub.add_parser("source_hunter", help="Run Source Hunter Agent")
    sh.add_argument("--research-question", required=True)
    sh.add_argument("--field", default="")
    sh.add_argument("--existing-sources", default=None,
                    help="Path to sources/ directory")
    sh.add_argument("--language", default="both",
                    choices=["tr", "en", "both"])

    # methodology_checker
    mc = sub.add_parser("methodology_checker", help="Run Methodology Checker Agent")
    mc.add_argument("--input", required=True,
                    help="Path to methodology text file, or inline text")
    mc.add_argument("--research-question", default="")
    mc.add_argument("--field", default="")
    mc.add_argument("--document-type", default="thesis",
                    choices=["thesis", "article", "report"])

    # citation_verifier
    cv = sub.add_parser("citation_verifier", help="Run Citation Verifier Agent")
    cv.add_argument("--claim", required=True)
    cv.add_argument("--source", required=True,
                    help="Path to source PDF file")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config_path = Path(args.config) if args.config else None
    config = AgentConfig(config_path) if config_path else AgentConfig()

    if args.list_providers:
        cmd_list_providers(config)
        return

    if args.test_providers:
        cmd_test_providers(config)
        return

    if args.agent == "source_hunter":
        asyncio.run(_run_source_hunter(config, args))
    elif args.agent == "methodology_checker":
        asyncio.run(_run_methodology_checker(config, args))
    elif args.agent == "citation_verifier":
        asyncio.run(_run_citation_verifier(config, args))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
