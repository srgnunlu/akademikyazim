"""Tests for scripts/gap_scanner.py — Research Gap Scanner."""

from __future__ import annotations

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.gap_scanner import (
    parse_note,
    parse_argumanlar,
    analyze_gaps,
    write_report,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

NOTE_WITH_GAPS = """\
# Review of Digital Education

This area remains under-researched in developing countries.
Further research is needed on long-term effects of digital tools.
The study finds that mobile learning shows promising results.
Limited evidence exists for effectiveness in rural settings.
What is the optimal frequency of technology integration?
"""

NOTE_WITHOUT_GAPS = """\
# Comprehensive Study

The study demonstrates that this approach works effectively.
Results confirm previous findings about engagement improvement.
"""

ARGUMENTS = """\
| # | İddia | Kaynak | Zıt Görüş |
|---|-------|--------|-----------|
| 1 | Digital literacy improves student outcomes significantly | Smith 2020 | Jones 2019 |
| 2 | Rural education benefits from mobile technology adoption | Lee 2021 | — |
| 3 | Blockchain revolutionizes academic integrity mechanisms | — | — |
"""


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    notes_dir = tmp_path / "notes"
    notes_dir.mkdir()
    (notes_dir / "review.md").write_text(NOTE_WITH_GAPS, encoding="utf-8")
    (notes_dir / "study.md").write_text(NOTE_WITHOUT_GAPS, encoding="utf-8")
    (tmp_path / "ARGUMENTS.md").write_text(ARGUMENTS, encoding="utf-8")
    return tmp_path


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestParseNote:
    def test_extracts_gap_sentences(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "review.md")
        assert len(note["gap_sentences"]) >= 1

    def test_extracts_questions(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "review.md")
        assert len(note["questions"]) >= 1

    def test_no_gaps_clean_note(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "study.md")
        assert len(note["gap_sentences"]) == 0


class TestParseArgumanlar:
    def test_parses_arguments(self, tmp_project: Path):
        args = parse_argumanlar(tmp_project / "ARGUMENTS.md")
        assert len(args) == 3

    def test_missing_file(self, tmp_path: Path):
        assert parse_argumanlar(tmp_path / "nonexistent.md") == []


class TestAnalyzeGaps:
    def test_finds_explicit_gaps(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        args = parse_argumanlar(tmp_project / "ARGUMENTS.md")
        result = analyze_gaps(notes, args)
        assert len(result["explicit_gaps"]) >= 1

    def test_finds_open_questions(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        args = parse_argumanlar(tmp_project / "ARGUMENTS.md")
        result = analyze_gaps(notes, args)
        assert len(result["open_questions"]) >= 1

    def test_finds_argument_gaps(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        args = parse_argumanlar(tmp_project / "ARGUMENTS.md")
        result = analyze_gaps(notes, args)
        # Argument 3 about blockchain should be a gap
        assert len(result["argument_gaps"]) >= 1


class TestWriteReport:
    def test_writes_report(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        args = parse_argumanlar(tmp_project / "ARGUMENTS.md")
        result = analyze_gaps(notes, args)
        output = tmp_project / "GAPS.md"
        write_report(result, notes, args, output)
        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert "Araştırma Boşlukları" in content


class TestMainCLI:
    def test_runs_successfully(self, tmp_project: Path):
        import subprocess
        result = subprocess.run(
            [sys.executable, "scripts/gap_scanner.py",
             "--project-dir", str(tmp_project)],
            cwd=str(Path(__file__).parent.parent),
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert (tmp_project / "GAPS.md").exists()
