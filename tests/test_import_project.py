"""Tests for scripts/import_project.py — Mid-Project Import Tool."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.import_project import (
    scan_directory,
    detect_phase,
    setup_project,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def empty_dir(tmp_path: Path) -> Path:
    return tmp_path


@pytest.fixture
def phase2_dir(tmp_path: Path) -> Path:
    """Directory with PDFs but no notes — Phase 2."""
    sources = tmp_path / "sources"
    sources.mkdir()
    for i in range(5):
        (sources / f"paper_{i}.pdf").write_bytes(b"%PDF-fake")
    return tmp_path


@pytest.fixture
def phase3_dir(tmp_path: Path) -> Path:
    """Directory with PDFs and notes — Phase 3."""
    sources = tmp_path / "sources"
    sources.mkdir()
    for i in range(5):
        (sources / f"paper_{i}.pdf").write_bytes(b"%PDF-fake")

    notes = tmp_path / "notes"
    notes.mkdir()
    for i in range(4):
        (notes / f"note_{i}.md").write_text(
            f"# Note {i}\n\nThis is a reading note about paper {i}. "
            "The study demonstrates significant findings about the topic. "
            "Results show that the methodology is valid and reliable.\n",
            encoding="utf-8",
        )
    return tmp_path


@pytest.fixture
def phase5_dir(tmp_path: Path) -> Path:
    """Directory with drafts — Phase 5."""
    sources = tmp_path / "sources"
    sources.mkdir()
    for i in range(3):
        (sources / f"paper_{i}.pdf").write_bytes(b"%PDF-fake")

    notes = tmp_path / "notes"
    notes.mkdir()
    for i in range(3):
        (notes / f"note_{i}.md").write_text(
            f"# Note {i}\n\nReading note content here with enough words.\n",
            encoding="utf-8",
        )

    # Draft files
    (tmp_path / "introduction.md").write_text(
        "# Introduction\n\n" + "This is a substantial draft introduction with many words. " * 300,
        encoding="utf-8",
    )
    (tmp_path / "literature_review.md").write_text(
        "# Literature Review\n\n" + "The literature shows various important findings and results. " * 200,
        encoding="utf-8",
    )
    return tmp_path


@pytest.fixture
def phase6_dir(tmp_path: Path) -> Path:
    """Directory with many drafts — Phase 6."""
    sources = tmp_path / "sources"
    sources.mkdir()
    for i in range(10):
        (sources / f"paper_{i}.pdf").write_bytes(b"%PDF-fake")

    for name in ["introduction", "literature_review", "methodology", "discussion"]:
        (tmp_path / f"{name}.md").write_text(
            f"# {name.title()}\n\n" + f"Draft content for {name} section. " * 500,
            encoding="utf-8",
        )
    return tmp_path


# ── Scan Tests ────────────────────────────────────────────────────────────────

class TestScanDirectory:
    def test_empty_dir(self, empty_dir: Path):
        scan = scan_directory(empty_dir)
        assert len(scan["pdfs"]) == 0
        assert len(scan["notes"]) == 0
        assert len(scan["drafts"]) == 0

    def test_finds_pdfs(self, phase2_dir: Path):
        scan = scan_directory(phase2_dir)
        assert len(scan["pdfs"]) == 5

    def test_finds_notes(self, phase3_dir: Path):
        scan = scan_directory(phase3_dir)
        assert len(scan["notes"]) >= 3

    def test_finds_drafts(self, phase5_dir: Path):
        scan = scan_directory(phase5_dir)
        assert len(scan["drafts"]) >= 1
        assert scan["total_word_count"] > 1000

    def test_finds_bib_files(self, tmp_path: Path):
        (tmp_path / "refs.bib").write_text("@article{test, title={Test}}")
        scan = scan_directory(tmp_path)
        assert len(scan["bib_files"]) == 1

    def test_skips_system_files(self, tmp_path: Path):
        (tmp_path / "STATUS.md").write_text("# Status")
        (tmp_path / "README.md").write_text("# Readme")
        (tmp_path / "ARGUMENTS.md").write_text("# Args")
        scan = scan_directory(tmp_path)
        assert len(scan["notes"]) == 0
        assert len(scan["drafts"]) == 0


# ── Phase Detection Tests ────────────────────────────────────────────────────

class TestDetectPhase:
    def test_empty_is_phase0(self, empty_dir: Path):
        scan = scan_directory(empty_dir)
        phase, _, _ = detect_phase(scan)
        assert phase == 0

    def test_pdfs_only_is_phase2(self, phase2_dir: Path):
        scan = scan_directory(phase2_dir)
        phase, _, _ = detect_phase(scan)
        assert phase == 2

    def test_pdfs_and_notes_is_phase3(self, phase3_dir: Path):
        scan = scan_directory(phase3_dir)
        phase, _, _ = detect_phase(scan)
        assert phase == 3

    def test_drafts_is_phase5(self, phase5_dir: Path):
        scan = scan_directory(phase5_dir)
        phase, _, _ = detect_phase(scan)
        assert phase == 5

    def test_many_drafts_is_phase6(self, phase6_dir: Path):
        scan = scan_directory(phase6_dir)
        phase, _, _ = detect_phase(scan)
        assert phase == 6

    def test_returns_reasons(self, phase3_dir: Path):
        scan = scan_directory(phase3_dir)
        _, _, reasons = detect_phase(scan)
        assert len(reasons) >= 1


# ── Setup Tests ──────────────────────────────────────────────────────────────

class TestSetupProject:
    def test_creates_status(self, phase3_dir: Path):
        scan = scan_directory(phase3_dir)
        setup_project(phase3_dir, scan, 3, "thesis", "tr", "law", "Test")
        assert (phase3_dir / "STATUS.md").exists()
        content = (phase3_dir / "STATUS.md").read_text()
        assert "current_phase: 3" in content
        assert "imported: true" in content

    def test_creates_core_files(self, empty_dir: Path):
        scan = scan_directory(empty_dir)
        result = setup_project(empty_dir, scan, 0, "article", "en", "cs", "Test")
        assert (empty_dir / "STATUS.md").exists()
        assert (empty_dir / "READING_REPORT.md").exists()
        assert (empty_dir / "ARGUMENTS.md").exists()
        assert len(result["created"]) == 3

    def test_skips_existing_files(self, tmp_path: Path):
        (tmp_path / "STATUS.md").write_text("existing")
        scan = scan_directory(tmp_path)
        result = setup_project(tmp_path, scan, 0, "thesis", "tr", "law", "Test")
        assert "STATUS.md (already exists)" in result["skipped"]
        # Shouldn't overwrite
        assert (tmp_path / "STATUS.md").read_text() == "existing"

    def test_moves_scattered_pdfs(self, tmp_path: Path):
        (tmp_path / "paper.pdf").write_bytes(b"%PDF-fake")
        scan = scan_directory(tmp_path)
        result = setup_project(tmp_path, scan, 1, "article", "en", "cs", "Test")
        # PDF should be moved to sources/
        assert (tmp_path / "sources" / "paper.pdf").exists()
        assert len(result["moved"]) >= 1

    def test_creates_directories(self, empty_dir: Path):
        scan = scan_directory(empty_dir)
        setup_project(empty_dir, scan, 0, "thesis", "tr", "law", "Test")
        assert (empty_dir / "sources").is_dir()
        assert (empty_dir / "notes").is_dir()


# ── CLI Tests ────────────────────────────────────────────────────────────────

class TestCLI:
    def test_scan_only(self, phase3_dir: Path):
        result = subprocess.run(
            [sys.executable, "scripts/import_project.py",
             "--dir", str(phase3_dir),
             "--type", "thesis", "--lang", "tr", "--field", "law",
             "--scan-only", "--json"],
            cwd=str(Path(__file__).parent.parent),
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert data["phase"] == 3

    def test_full_import(self, phase2_dir: Path):
        result = subprocess.run(
            [sys.executable, "scripts/import_project.py",
             "--dir", str(phase2_dir),
             "--type", "article", "--lang", "en", "--field", "computer-science",
             "--title", "Test Paper"],
            cwd=str(Path(__file__).parent.parent),
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert (phase2_dir / "STATUS.md").exists()

    def test_phase_override(self, phase2_dir: Path):
        result = subprocess.run(
            [sys.executable, "scripts/import_project.py",
             "--dir", str(phase2_dir),
             "--type", "thesis", "--lang", "tr", "--field", "law",
             "--phase-override", "4", "--json"],
            cwd=str(Path(__file__).parent.parent),
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert data["phase"] == 4
        content = (phase2_dir / "STATUS.md").read_text()
        assert "current_phase: 4" in content
