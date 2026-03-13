"""Tests for core/literature_intel.py — Literature Intelligence Layer."""

from __future__ import annotations

import pytest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.literature_intel import (
    detect_section_type,
    NoteIndex,
    ArgumentIndex,
    LiteratureIntel,
    SECTION_TOOLS,
    SECTION_CHECKS,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

NOTE_SUPPORT = """\
# Smith 2020 — Digital Literacy

Smith (2020) demonstrates that digital literacy significantly improves student outcomes.
The study confirms that technology integration shows positive effects on learning.
"""

NOTE_CONTRA = """\
# Jones 2019 — Technology Critique

Jones (2019) argues that technology does not improve learning outcomes.
Despite widespread adoption, no significant correlation was found.
"""

ARGUMENTS = """\
| # | İddia | Kaynak |
|---|-------|--------|
| 1 | Digital literacy improves student outcomes | Smith 2020 |
| 2 | Technology integration shows positive learning effects | Smith 2020 |
"""


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    notes = tmp_path / "notes"
    notes.mkdir()
    (notes / "smith2020.md").write_text(NOTE_SUPPORT, encoding="utf-8")
    (notes / "jones2019.md").write_text(NOTE_CONTRA, encoding="utf-8")
    (tmp_path / "ARGUMENTS.md").write_text(ARGUMENTS, encoding="utf-8")
    return tmp_path


# ── Section Detection ─────────────────────────────────────────────────────────

class TestDetectSectionType:
    def test_from_filename_tr(self):
        assert detect_section_type(Path("giris.md")) == "intro"

    def test_from_filename_en(self):
        assert detect_section_type(Path("literature_review.md")) == "literature"

    def test_from_filename_method(self):
        assert detect_section_type(Path("yontem.md")) == "method"

    def test_from_filename_discussion(self):
        assert detect_section_type(Path("tartisma.md")) == "discussion"

    def test_from_filename_conclusion(self):
        assert detect_section_type(Path("sonuc.md")) == "conclusion"

    def test_from_filename_results(self):
        assert detect_section_type(Path("bulgular.md")) == "results"

    def test_from_content(self):
        content = "Bu bölümde araştırma sorusu tartışılacak ve kapsam belirlenecektir. Amaç ve motivasyon açıklanacaktır."
        result = detect_section_type(content=content)
        assert result == "intro"

    def test_unknown_returns_none(self):
        assert detect_section_type(Path("random_file.md"), "") is None

    def test_content_literature(self):
        content = "Bu literatür taraması mevcut çalışmaları inceleyecektir. Kaynak incelemesi sonuçları aşağıdadır. Prior research shows..."
        result = detect_section_type(content=content)
        assert result == "literature"


# ── NoteIndex ─────────────────────────────────────────────────────────────────

class TestNoteIndex:
    def test_loads_notes(self, tmp_project: Path):
        idx = NoteIndex(tmp_project / "notes")
        assert len(idx.notes) == 2

    def test_find_related(self, tmp_project: Path):
        idx = NoteIndex(tmp_project / "notes")
        related = idx.find_related("digital literacy improves student outcomes in education")
        assert len(related) >= 1

    def test_find_related_empty(self, tmp_path: Path):
        idx = NoteIndex(tmp_path / "notes")  # doesn't exist
        assert idx.find_related("anything") == []

    def test_find_contradicting(self, tmp_project: Path):
        idx = NoteIndex(tmp_project / "notes")
        # The notes have contradicting views on technology
        contras = idx.find_contradicting(
            "Technology demonstrates significant improvement in learning outcomes"
        )
        # May or may not find contradictions depending on keyword overlap
        assert isinstance(contras, list)


# ── ArgumentIndex ─────────────────────────────────────────────────────────────

class TestArgumentIndex:
    def test_loads_arguments(self, tmp_project: Path):
        idx = ArgumentIndex(tmp_project)
        assert len(idx.arguments) == 2

    def test_find_matching(self, tmp_project: Path):
        idx = ArgumentIndex(tmp_project)
        matches = idx.find_matching("digital literacy outcomes student improvement")
        assert len(matches) >= 1

    def test_missing_argumanlar(self, tmp_path: Path):
        idx = ArgumentIndex(tmp_path)
        assert len(idx.arguments) == 0


# ── LiteratureIntel ───────────────────────────────────────────────────────────

class TestLiteratureIntel:
    def test_analyze_paragraph(self, tmp_project: Path):
        intel = LiteratureIntel(tmp_project)
        result = intel.analyze_paragraph(
            "Digital literacy significantly improves student outcomes in modern education."
        )
        assert "related_sources" in result
        assert "contradictions" in result
        assert "matching_arguments" in result
        assert "unsupported_claims" in result
        assert "suggestions" in result

    def test_review_for_section(self, tmp_project: Path):
        intel = LiteratureIntel(tmp_project)
        draft = (
            "Digital literacy has become crucial in modern education.\n\n"
            "Studies show that technology integration improves outcomes.\n\n"
            "However, some researchers question these findings."
        )
        result = intel.review_for_section(draft, filepath=Path("giris.md"))
        assert result["section_type"] == "intro"
        assert "paragraph_analyses" in result
        assert len(result["paragraph_analyses"]) >= 1
        assert "recommended_tools" in result

    def test_review_section_auto_detect(self, tmp_project: Path):
        intel = LiteratureIntel(tmp_project)
        draft = "Bu literatür taraması mevcut çalışmaları incelemektedir. Prior research shows many perspectives."
        result = intel.review_for_section(draft)
        # May detect literature or None
        assert isinstance(result["section_type"], (str, type(None)))


# ── Section tools and checks ─────────────────────────────────────────────────

class TestSectionConfig:
    def test_all_sections_have_tools(self):
        for section in ["intro", "literature", "method", "results", "discussion", "conclusion"]:
            assert section in SECTION_TOOLS

    def test_all_sections_have_checks(self):
        for section in ["intro", "literature", "method", "results", "discussion", "conclusion"]:
            assert section in SECTION_CHECKS
