"""Tests for new CLI scripts — so_what, knowledge_map, assumption_killer, citation_chain."""

from __future__ import annotations

import subprocess
import sys
import pytest
from pathlib import Path

_ROOT = Path(__file__).parent.parent

NOTE_A = """\
# Smith 2020 — Digital Literacy

Yazar: Smith
DOI: 10.1234/smith2020

Smith (2020) argues that digital literacy is widely accepted as beneficial.
The consensus is that technology integration demonstrates positive effects.
This has real-world impact on educational policy and practice.
The assumption is that all students have equal access to technology.
Mobile learning platforms are assumed to be universally available.
Smith references Jones (2019) and Lee (2021) in the discussion.
Further research is needed on rural implementations.
"""

NOTE_B = """\
# Jones 2019 — Critical Review

Yazar: Jones
DOI: 10.1234/jones2019

Jones (2019) challenges the assumption that technology improves outcomes.
It remains unclear whether digital tools genuinely enhance learning.
The impact on policy remains debatable and contested.
This assumption has been taken for granted by many researchers.
Jones pioneered the critical examination of educational technology claims.
Some questions remain: Does technology really improve critical thinking?
"""

ARGUMENTS = """\
| # | İddia | Kaynak | Zıt Görüş |
|---|-------|--------|-----------|
| 1 | Digital literacy improves student outcomes | Smith 2020 | Jones 2019 |
| 2 | Technology access is universally available | — | — |
| 3 | Mobile learning transforms rural education | Lee 2021 | — |
"""


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    notes = tmp_path / "notes"
    notes.mkdir()
    (notes / "smith2020.md").write_text(NOTE_A, encoding="utf-8")
    (notes / "jones2019.md").write_text(NOTE_B, encoding="utf-8")
    (tmp_path / "ARGUMENTS.md").write_text(ARGUMENTS, encoding="utf-8")
    return tmp_path


def _run_script(name: str, project_dir: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, f"scripts/{name}", "--project-dir", str(project_dir)],
        cwd=str(_ROOT),
        capture_output=True, text=True,
    )


class TestSoWhatTest:
    def test_runs_successfully(self, tmp_project: Path):
        result = _run_script("so_what_test.py", tmp_project)
        assert result.returncode == 0

    def test_creates_output(self, tmp_project: Path):
        _run_script("so_what_test.py", tmp_project)
        assert (tmp_project / "SO_WHAT.md").exists()

    def test_output_has_3_sections(self, tmp_project: Path):
        _run_script("so_what_test.py", tmp_project)
        content = (tmp_project / "SO_WHAT.md").read_text(encoding="utf-8")
        assert "Kanıtladığı" in content or "Proven" in content
        assert "Bilmediğimizin" in content or "Unknowns" in content
        assert "Gerçek Dünya" in content or "Real-World" in content

    def test_no_notes_graceful(self, tmp_path: Path):
        result = _run_script("so_what_test.py", tmp_path)
        assert result.returncode == 0


class TestKnowledgeMap:
    def test_runs_successfully(self, tmp_project: Path):
        result = _run_script("knowledge_map.py", tmp_project)
        assert result.returncode == 0

    def test_creates_output(self, tmp_project: Path):
        _run_script("knowledge_map.py", tmp_project)
        assert (tmp_project / "KNOWLEDGE_MAP.md").exists()

    def test_output_has_tree(self, tmp_project: Path):
        _run_script("knowledge_map.py", tmp_project)
        content = (tmp_project / "KNOWLEDGE_MAP.md").read_text(encoding="utf-8")
        assert "Destek Sütunları" in content or "Support Pillars" in content

    def test_no_notes_graceful(self, tmp_path: Path):
        result = _run_script("knowledge_map.py", tmp_path)
        assert result.returncode == 0


class TestAssumptionKiller:
    def test_runs_successfully(self, tmp_project: Path):
        result = _run_script("assumption_killer.py", tmp_project)
        assert result.returncode == 0

    def test_creates_output(self, tmp_project: Path):
        _run_script("assumption_killer.py", tmp_project)
        assert (tmp_project / "ASSUMPTIONS.md").exists()

    def test_output_has_assumptions(self, tmp_project: Path):
        _run_script("assumption_killer.py", tmp_project)
        content = (tmp_project / "ASSUMPTIONS.md").read_text(encoding="utf-8")
        assert "Varsayım" in content

    def test_no_notes_graceful(self, tmp_path: Path):
        result = _run_script("assumption_killer.py", tmp_path)
        assert result.returncode == 0


class TestCitationChain:
    def test_runs_successfully(self, tmp_project: Path):
        result = _run_script("citation_chain.py", tmp_project)
        assert result.returncode == 0

    def test_creates_output(self, tmp_project: Path):
        _run_script("citation_chain.py", tmp_project)
        assert (tmp_project / "CITATION_CHAIN.md").exists()

    def test_output_has_concepts(self, tmp_project: Path):
        _run_script("citation_chain.py", tmp_project)
        content = (tmp_project / "CITATION_CHAIN.md").read_text(encoding="utf-8")
        assert "Kavram" in content or "Atıf Zinciri" in content

    def test_specific_concept(self, tmp_project: Path):
        result = subprocess.run(
            [sys.executable, "scripts/citation_chain.py",
             "--project-dir", str(tmp_project),
             "--concept", "digital"],
            cwd=str(_ROOT),
            capture_output=True, text=True,
        )
        assert result.returncode == 0

    def test_no_notes_graceful(self, tmp_path: Path):
        result = _run_script("citation_chain.py", tmp_path)
        assert result.returncode == 0
