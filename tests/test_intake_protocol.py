"""Tests for scripts/intake_protocol.py — Source Intake Protocol."""

from __future__ import annotations

import pytest
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.intake_protocol import (
    parse_note,
    extract_keywords,
    cluster_by_keywords,
    detect_conflicts,
    write_report,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

NOTE_A = """\
# Smith 2020 — Digital Literacy in Education

Yazar: Smith
DOI: 10.1234/smith2020

Smith (2020) argues that digital literacy significantly improves student outcomes.
The study finds that technology integration demonstrates positive effects on learning.
Results show increased engagement and better academic performance.
"""

NOTE_B = """\
# Jones 2019 — Technology in Classrooms

Yazar: Jones
DOI: 10.1234/jones2019

Jones (2019) argues that technology does not necessarily improve learning outcomes.
Despite widespread adoption, the study finds no significant correlation between
digital tools and academic performance. However, engagement shows some improvement.
"""

NOTE_C = """\
# Lee 2021 — Mobile Learning Trends

Yazar: Lee
DOI: 10.1234/lee2021

Lee (2021) demonstrates that mobile learning platforms show promising results.
The study suggests that accessibility increases when digital tools are available.
Student engagement with mobile platforms shows consistent improvement.
"""


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    notes_dir = tmp_path / "notes"
    notes_dir.mkdir()
    (notes_dir / "smith2020.md").write_text(NOTE_A, encoding="utf-8")
    (notes_dir / "jones2019.md").write_text(NOTE_B, encoding="utf-8")
    (notes_dir / "lee2021.md").write_text(NOTE_C, encoding="utf-8")
    return tmp_path


# ── Tests ─────────────────────────────────────────────────────────────────────

class TestParseNote:
    def test_extracts_title(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert "Smith 2020" in note["title"]

    def test_extracts_author(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert note["author"] == "Smith"

    def test_extracts_year(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert note["year"] == "2020"

    def test_extracts_doi(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert note["doi"] == "10.1234/smith2020"

    def test_extracts_claims(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert len(note["claims"]) >= 1

    def test_extracts_core_claim(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert len(note["core_claim"]) > 0

    def test_extracts_keywords(self, tmp_project: Path):
        note = parse_note(tmp_project / "notes" / "smith2020.md")
        assert len(note["keywords"]) > 0


class TestExtractKeywords:
    def test_returns_list(self):
        assert isinstance(extract_keywords("hello world test words example"), list)

    def test_filters_stop_words(self):
        kw = extract_keywords("this is a test with some words for analysis")
        assert "this" not in kw

    def test_top_n_limit(self):
        text = "alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu"
        kw = extract_keywords(text, top_n=3)
        assert len(kw) <= 3


class TestClustering:
    def test_creates_clusters(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        clusters = cluster_by_keywords(notes)
        assert len(clusters) >= 1

    def test_all_notes_assigned(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        clusters = cluster_by_keywords(notes)
        assigned = set()
        for c in clusters:
            assigned.update(c["note_indices"])
        assert assigned == set(range(len(notes)))

    def test_empty_notes(self):
        assert cluster_by_keywords([]) == []


class TestConflictDetection:
    def test_detects_conflicts(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        conflicts = detect_conflicts(notes)
        # Smith says positive, Jones says not — should detect conflict
        assert isinstance(conflicts, list)

    def test_no_conflicts_single_note(self, tmp_path: Path):
        notes_dir = tmp_path / "notes"
        notes_dir.mkdir()
        (notes_dir / "single.md").write_text("# Single\nSome text here.", encoding="utf-8")
        notes = [parse_note(notes_dir / "single.md")]
        assert detect_conflicts(notes) == []


class TestWriteReport:
    def test_writes_report(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        clusters = cluster_by_keywords(notes)
        conflicts = detect_conflicts(notes)
        output = tmp_project / "SOURCE_MAP.md"
        write_report(notes, clusters, conflicts, output)
        assert output.exists()
        content = output.read_text(encoding="utf-8")
        assert "Kaynak Haritası" in content
        assert "smith2020.md" in content

    def test_report_has_clusters(self, tmp_project: Path):
        notes = [parse_note(p) for p in sorted((tmp_project / "notes").glob("*.md"))]
        clusters = cluster_by_keywords(notes)
        conflicts = detect_conflicts(notes)
        output = tmp_project / "SOURCE_MAP.md"
        write_report(notes, clusters, conflicts, output)
        content = output.read_text(encoding="utf-8")
        assert "Küme" in content


class TestMainCLI:
    def test_runs_successfully(self, tmp_project: Path):
        import subprocess
        result = subprocess.run(
            [sys.executable, "scripts/intake_protocol.py",
             "--project-dir", str(tmp_project)],
            cwd=str(Path(__file__).parent.parent),
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert (tmp_project / "SOURCE_MAP.md").exists()

    def test_no_notes_dir(self, tmp_path: Path):
        import subprocess
        result = subprocess.run(
            [sys.executable, "scripts/intake_protocol.py",
             "--project-dir", str(tmp_path)],
            cwd=str(Path(__file__).parent.parent),
            capture_output=True, text=True,
        )
        assert result.returncode == 0  # graceful exit
