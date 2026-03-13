#!/usr/bin/env python3
"""
scripts/phase_gate_check.py — TezAtlas Phase Gate Validator

Checks whether all conditions for a phase transition are met.
Prints a human-readable gate report and exits with:
  0 → all gates passed
  1 → one or more gates failed
  2 → usage/config error

Usage:
    python3 scripts/phase_gate_check.py --from 2 --to 3
    python3 scripts/phase_gate_check.py --from 3 --to 4 --project-dir /path/to/project
    python3 scripts/phase_gate_check.py --all-remaining --from 2   # show all future gates
    python3 scripts/phase_gate_check.py --confirm advisor_checkpoint_phase4

Options:
    --from N           Source phase (required unless --confirm)
    --to N             Target phase (required unless --all-remaining or --confirm)
    --all-remaining    Show gate status for all phases from --from onward
    --confirm KEY      Mark a gate condition as manually confirmed in STATUS.md
    --force            Advance phase even if gates fail (skips checks, use with care)
    --advance          If all gates pass, advance to the target phase
    --project-dir PATH Project root (default: current dir)
    --json             Output raw JSON instead of formatted report
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

from core.phase_gate import PhaseGate
from core.session import TezAtlasSession


def _format_result(result: dict) -> str:
    lines = []
    icon = "✅" if result["passed"] else "🚫"
    lines.append(f"{icon} **{result['message']}**")
    lines.append("")

    if result.get("passed_checks"):
        lines.append("**Passed:**")
        for label in result["passed_checks"]:
            lines.append(f"  ✓ {label}")

    if result.get("failed_checks"):
        lines.append("")
        lines.append("**Failed:**")
        for fc in result["failed_checks"]:
            lines.append(f"  ✗ {fc['label']}")
            lines.append(f"    → {fc['hint']}")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="TezAtlas phase gate checker")
    parser.add_argument("--project-dir", type=Path, default=Path("."))
    parser.add_argument("--from", type=int, dest="from_phase", metavar="N")
    parser.add_argument("--to", type=int, dest="to_phase", metavar="N")
    parser.add_argument("--all-remaining", action="store_true")
    parser.add_argument("--confirm", type=str, metavar="KEY",
                        help="Mark a gate key as confirmed in STATUS.md")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--advance", action="store_true")
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    status_path = project_dir / "STATUS.md"

    if not status_path.exists():
        print("STATUS.md not found.", file=sys.stderr)
        sys.exit(2)

    sess = TezAtlasSession(project_dir)
    state = sess.load()
    doc_type = state.get("document_type", "thesis")
    gate = PhaseGate(project_dir, doc_type)

    # ── --confirm mode ───────────────────────────────────────────────────────
    if args.confirm:
        sess.confirm_gate(args.confirm)
        print(f"✅ Gate '{args.confirm}' confirmed in STATUS.md")
        sys.exit(0)

    # ── --all-remaining mode ─────────────────────────────────────────────────
    if args.all_remaining:
        from_phase = args.from_phase if args.from_phase is not None else int(state.get("current_phase", 0))
        results = gate.check_all_remaining(from_phase, state)
        if args.as_json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            for r in results:
                print(_format_result(r))
                print()
        all_passed = all(r["passed"] for r in results)
        sys.exit(0 if all_passed else 1)

    # ── Single gate check ────────────────────────────────────────────────────
    if args.from_phase is None or args.to_phase is None:
        parser.error("--from and --to are required (or use --all-remaining / --confirm)")

    result = gate.check(args.from_phase, args.to_phase, state)

    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(_format_result(result))

    # ── --advance: optionally advance the phase ──────────────────────────────
    if args.advance:
        if result["passed"] or args.force:
            advance_result = sess.advance_phase(force=args.force)
            if advance_result.get("advanced"):
                print(f"\n🚀 Phase advanced: {advance_result['from_phase']} → {advance_result['to_phase']}")
            else:
                print(f"\n{advance_result.get('message', 'Could not advance phase.')}")
        else:
            print("\n⛔ Phase NOT advanced — fix the failed gates first.")
            sys.exit(1)

    sys.exit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
