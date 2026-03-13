"""
tests/test_session.py — TezAtlas core session orchestration tests

Tests for:
- TezAtlasSession.load() — STATUS.md parsing
- TezAtlasSession.save() — STATUS.md write-back
- TezAtlasSession.end_session() — streak, wellbeing, DASHBOARD.md
- TezAtlasSession.advance_phase() — phase gate integration
- PhaseGate.check() — gate condition evaluation
- generate_dashboard_content() — DASHBOARD.md generation
"""

from __future__ import annotations

import textwrap
from datetime import date, timedelta
from pathlib import Path

import pytest

from core.session import TezAtlasSession, PHASE_NAMES
from core.phase_gate import PhaseGate
from core.dashboard import generate_dashboard_content


# ── Fixtures ──────────────────────────────────────────────────────────────────

STATUS_MINIMAL = textwrap.dedent("""\
    # STATUS.md — TezAtlas Project State

    ```yaml
    document_type: thesis
    current_phase: 0
    language: en
    research_field: economics
    ```
""")

STATUS_PHASE2 = textwrap.dedent("""\
    # STATUS.md — TezAtlas Project State

    ```yaml
    document_type: thesis
    current_phase: 2
    language: en
    research_field: economics
    sources:
      total_collected: 5
      read: 2
      deferred: 0
      saturation_reached: false
    writing_schedule:
      current_streak: 3
      longest_streak: 5
      total_sessions: 10
      last_session_date: "{today}"
    wellbeing:
      days_inactive: 0
      attrition_risk: low
    next_actions:
      - Read three more sources
      - Add arguments to ARGUMENTS.md
    blockers: []
    gates: {{}}
    ```
""").format(today=date.today().isoformat())

STATUS_WITH_GATES = textwrap.dedent("""\
    # STATUS.md — TezAtlas Project State

    ```yaml
    document_type: thesis
    current_phase: 3
    language: en
    research_field: economics
    sources:
      total_collected: 10
      read: 9
      deferred: 0
      saturation_reached: true
    writing_schedule:
      current_streak: 0
      longest_streak: 5
      total_sessions: 20
      last_session_date: null
    wellbeing:
      days_inactive: 0
      attrition_risk: low
    gates:
      advisor_checkpoint_phase4:
        confirmed: true
    ```
""")


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    """Empty project dir with STATUS.md."""
    (tmp_path / "STATUS.md").write_text(STATUS_MINIMAL, encoding="utf-8")
    (tmp_path / "sources").mkdir()
    return tmp_path


@pytest.fixture
def tmp_project_phase2(tmp_path: Path) -> Path:
    (tmp_path / "STATUS.md").write_text(STATUS_PHASE2, encoding="utf-8")
    (tmp_path / "sources").mkdir()
    return tmp_path


@pytest.fixture
def tmp_project_phase3_gated(tmp_path: Path) -> Path:
    (tmp_path / "STATUS.md").write_text(STATUS_WITH_GATES, encoding="utf-8")
    (tmp_path / "sources").mkdir()
    # Create 10 dummy PDFs
    for i in range(10):
        (tmp_path / "sources" / f"paper{i}.pdf").write_bytes(b"%PDF dummy")
    # ARGUMENTS.md with 5 rows
    argumanlar = "# ARGUMENTS\n\n| İddia | Kaynak |\n|-------|--------|\n"
    for i in range(5):
        argumanlar += f"| Argüman {i+1} | Source {i+1} |\n"
    (tmp_path / "ARGUMENTS.md").write_text(argumanlar, encoding="utf-8")
    (tmp_path / "SAVUNMA_ZIRHI.md").write_text("# Defense armor\n", encoding="utf-8")
    return tmp_path


# ── TezAtlasSession.load() ────────────────────────────────────────────────────

class TestSessionLoad:
    def test_load_minimal(self, tmp_project: Path) -> None:
        sess = TezAtlasSession(tmp_project)
        state = sess.load()
        assert state["document_type"] == "thesis"
        assert state["current_phase"] == 0

    def test_load_derived_phase_name(self, tmp_project: Path) -> None:
        sess = TezAtlasSession(tmp_project)
        state = sess.load()
        # Phase 0 for thesis → should be a non-empty string
        assert isinstance(state["_phase_name"], str)
        assert len(state["_phase_name"]) > 0

    def test_load_source_count(self, tmp_project: Path) -> None:
        # Add PDFs
        (tmp_project / "sources" / "a.pdf").write_bytes(b"%PDF")
        (tmp_project / "sources" / "b.pdf").write_bytes(b"%PDF")
        sess = TezAtlasSession(tmp_project)
        state = sess.load()
        assert state["_source_count"] == 2

    def test_load_no_sources_dir(self, tmp_path: Path) -> None:
        (tmp_path / "STATUS.md").write_text(STATUS_MINIMAL, encoding="utf-8")
        # No sources/ dir
        sess = TezAtlasSession(tmp_path)
        state = sess.load()
        assert state["_source_count"] == 0

    def test_load_argumanlar_count(self, tmp_project: Path) -> None:
        argumanlar = "# ARGUMENTS\n\n| İddia | Kaynak |\n|-------|--------|\n| A1 | S1 |\n| A2 | S2 |\n"
        (tmp_project / "ARGUMENTS.md").write_text(argumanlar, encoding="utf-8")
        sess = TezAtlasSession(tmp_project)
        state = sess.load()
        assert state["_argumanlar_count"] == 2

    def test_load_savunma_zirhi_flag(self, tmp_project: Path) -> None:
        sess = TezAtlasSession(tmp_project)
        state = sess.load()
        assert state["_savunma_zirhi_exists"] is False

        (tmp_project / "SAVUNMA_ZIRHI.md").write_text("content", encoding="utf-8")
        state2 = sess.load()
        assert state2["_savunma_zirhi_exists"] is True

    def test_load_attrition_risk_low(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        state = sess.load()
        # Last session was today → 0 days inactive → low
        assert state["_attrition_risk"] == "low"

    def test_load_attrition_risk_high(self, tmp_path: Path) -> None:
        old_date = (date.today() - timedelta(days=20)).isoformat()
        status = STATUS_MINIMAL.replace(
            "current_phase: 0",
            f"current_phase: 0\nwriting_schedule:\n  last_session_date: {old_date}\n  current_streak: 5\n  longest_streak: 5\n  total_sessions: 1",
        )
        (tmp_path / "STATUS.md").write_text(status, encoding="utf-8")
        (tmp_path / "sources").mkdir()
        sess = TezAtlasSession(tmp_path)
        state = sess.load()
        assert state["_attrition_risk"] == "high"
        assert state["_days_inactive"] >= 20


# ── TezAtlasSession.save() ───────────────────────────────────────────────────

class TestSessionSave:
    def test_save_updates_field(self, tmp_project: Path) -> None:
        sess = TezAtlasSession(tmp_project)
        sess.save({"current_phase": 1})
        state = sess.load()
        assert state["current_phase"] == 1

    def test_save_preserves_other_fields(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        sess.save({"current_phase": 3})
        state = sess.load()
        assert state["document_type"] == "thesis"
        assert state["current_phase"] == 3

    def test_save_roundtrip(self, tmp_project: Path) -> None:
        sess = TezAtlasSession(tmp_project)
        sess.save({"next_actions": ["Do X", "Do Y"], "blockers": ["Issue Z"]})
        state = sess.load()
        assert "Do X" in (state.get("next_actions") or [])
        assert "Issue Z" in (state.get("blockers") or [])


# ── TezAtlasSession.end_session() ────────────────────────────────────────────

class TestEndSession:
    def test_end_session_creates_dashboard(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        sess.end_session(summary="Read 2 sources", sources_read_delta=2)
        assert (tmp_project_phase2 / "DASHBOARD.md").exists()

    def test_end_session_increments_sources(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        initial_state = sess.load()
        initial_read = int((initial_state.get("sources") or {}).get("read", 0))
        sess.end_session(summary="reading", sources_read_delta=3)
        new_state = sess.load()
        assert int((new_state.get("sources") or {}).get("read", 0)) == initial_read + 3

    def test_end_session_increments_total_sessions(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        initial = sess.load()
        initial_total = int((initial.get("writing_schedule") or {}).get("total_sessions", 0))
        sess.end_session(summary="done")
        new_state = sess.load()
        assert int((new_state.get("writing_schedule") or {}).get("total_sessions", 0)) == initial_total + 1

    def test_end_session_updates_next_actions(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        sess.end_session(summary="x", next_actions=["Action A", "Action B"])
        state = sess.load()
        assert "Action A" in (state.get("next_actions") or [])


# ── PhaseGate.check() ────────────────────────────────────────────────────────

class TestPhaseGate:
    def test_gate_0_to_1_passes(self, tmp_project: Path) -> None:
        gate = PhaseGate(tmp_project, "thesis")
        result = gate.check(0, 1)
        assert result["passed"] is True

    def test_gate_0_to_1_fails_no_sources_dir(self, tmp_path: Path) -> None:
        (tmp_path / "STATUS.md").write_text(STATUS_MINIMAL, encoding="utf-8")
        # No sources/ dir
        gate = PhaseGate(tmp_path, "thesis")
        result = gate.check(0, 1)
        assert result["passed"] is False
        labels = [fc["label"] for fc in result["failed_checks"]]
        assert any("sources" in lbl.lower() for lbl in labels)

    def test_gate_1_to_2_requires_pdf(self, tmp_project: Path) -> None:
        gate = PhaseGate(tmp_project, "thesis")
        result = gate.check(1, 2)
        assert result["passed"] is False  # no PDFs

        (tmp_project / "sources" / "paper.pdf").write_bytes(b"%PDF")
        result2 = gate.check(1, 2)
        assert result2["passed"] is True

    def test_gate_2_to_3_requires_3_pdfs_and_argumanlar(self, tmp_project: Path) -> None:
        gate = PhaseGate(tmp_project, "thesis")
        result = gate.check(2, 3)
        assert result["passed"] is False

    def test_gate_3_to_4_thesis_all_conditions(self, tmp_project_phase3_gated: Path) -> None:
        gate = PhaseGate(tmp_project_phase3_gated, "thesis")
        state = TezAtlasSession(tmp_project_phase3_gated).load()
        result = gate.check(3, 4, state)
        assert result["passed"] is True, result["failed_checks"]

    def test_gate_4_to_5_thesis_advisor(self, tmp_project_phase3_gated: Path) -> None:
        gate = PhaseGate(tmp_project_phase3_gated, "thesis")
        state = TezAtlasSession(tmp_project_phase3_gated).load()
        result = gate.check(4, 5, state)
        # advisor_checkpoint_phase4 is confirmed in STATUS_WITH_GATES
        assert result["passed"] is True

    def test_gate_5_to_6_thesis_no_deferred_passes(self, tmp_project: Path) -> None:
        # No READING_REPORT.md → no deferred entries → gate passes (Iron Rule 9)
        gate = PhaseGate(tmp_project, "thesis")
        result = gate.check(5, 6)
        assert result["passed"] is True

    def test_gate_5_to_6_thesis_with_deferred_blocked(self, tmp_project: Path) -> None:
        # READING_REPORT.md with a deferred entry but no manual confirmation
        report = (
            "# READING_REPORT.md\n\n"
            "| # | Yazar | Yıl | Başlık | Durum | Alaka | Notlar |\n"
            "|---|-------|-----|--------|-------|-------|--------|\n"
            "| 1 | Smith | 2020 | A Paper | 🔴 Ertelendi | | paper.pdf |\n"
        )
        (tmp_project / "READING_REPORT.md").write_text(report, encoding="utf-8")
        gate = PhaseGate(tmp_project, "thesis")
        result = gate.check(5, 6)
        assert result["passed"] is False
        labels = [fc["label"] for fc in result["failed_checks"]]
        assert any("Iron Rule 9" in lbl for lbl in labels)

    def test_gate_5_to_6_thesis_with_deferred_confirmed_passes(
        self, tmp_project: Path
    ) -> None:
        # Deferred entries exist but gates.deferred_pool_reviewed.confirmed = true
        report = (
            "# READING_REPORT.md\n\n"
            "| # | Yazar | Yıl | Başlık | Durum | Alaka | Notlar |\n"
            "|---|-------|-----|--------|-------|-------|--------|\n"
            "| 1 | Smith | 2020 | A Paper | 🔴 Ertelendi | | paper.pdf |\n"
        )
        (tmp_project / "READING_REPORT.md").write_text(report, encoding="utf-8")
        status_with_confirm = textwrap.dedent("""\
            # STATUS.md

            ```yaml
            document_type: thesis
            current_phase: 5
            language: en
            research_field: economics
            gates:
              deferred_pool_reviewed:
                confirmed: true
            ```
        """)
        (tmp_project / "STATUS.md").write_text(status_with_confirm, encoding="utf-8")
        gate = PhaseGate(tmp_project, "thesis")
        state = TezAtlasSession(tmp_project).load()
        result = gate.check(5, 6, state)
        assert result["passed"] is True

    def test_gate_article_4_to_5_deferred_blocked(self, tmp_project: Path) -> None:
        # Article type: (4,5) should also enforce Iron Rule 9
        report = (
            "# READING_REPORT.md\n\n"
            "| # | Yazar | Yıl | Başlık | Durum | Alaka | Notlar |\n"
            "|---|-------|-----|--------|-------|-------|--------|\n"
            "| 1 | Jones | 2021 | B Paper | 🔴 Ertelendi | | b.pdf |\n"
        )
        (tmp_project / "READING_REPORT.md").write_text(report, encoding="utf-8")
        # Add 5 PDFs to pass the pdf count gate
        for i in range(5):
            (tmp_project / "sources" / f"art{i}.pdf").write_bytes(b"%PDF")
        gate = PhaseGate(tmp_project, "article")
        result = gate.check(4, 5)
        assert result["passed"] is False
        labels = [fc["label"] for fc in result["failed_checks"]]
        assert any("Iron Rule 9" in lbl for lbl in labels)

    def test_gate_result_structure(self, tmp_project: Path) -> None:
        gate = PhaseGate(tmp_project, "thesis")
        result = gate.check(0, 1)
        assert "passed" in result
        assert "passed_checks" in result
        assert "failed_checks" in result
        assert "message" in result
        assert "from_phase" in result
        assert "to_phase" in result

    def test_check_all_remaining(self, tmp_project: Path) -> None:
        gate = PhaseGate(tmp_project, "thesis")
        results = gate.check_all_remaining(0)
        assert isinstance(results, list)
        assert len(results) > 0
        for r in results:
            assert "passed" in r


# ── generate_dashboard_content() ─────────────────────────────────────────────

class TestDashboard:
    def test_dashboard_contains_phase_info(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        state = sess.load()
        content = generate_dashboard_content(state, tmp_project_phase2)
        assert "DASHBOARD" in content
        assert "Phase" in content or "Faz" in content

    def test_dashboard_contains_streak(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        state = sess.load()
        content = generate_dashboard_content(state, tmp_project_phase2)
        assert "Streak" in content or "streak" in content.lower()

    def test_dashboard_contains_progress_bar(self, tmp_project_phase2: Path) -> None:
        sess = TezAtlasSession(tmp_project_phase2)
        state = sess.load()
        content = generate_dashboard_content(state, tmp_project_phase2)
        # ASCII bars use these chars
        assert "█" in content or "░" in content

    def test_dashboard_no_exception_with_empty_state(self, tmp_path: Path) -> None:
        (tmp_path / "STATUS.md").write_text(STATUS_MINIMAL, encoding="utf-8")
        (tmp_path / "sources").mkdir()
        sess = TezAtlasSession(tmp_path)
        state = sess.load()
        # Should not raise
        content = generate_dashboard_content(state, tmp_path)
        assert isinstance(content, str)
        assert len(content) > 100

    def test_dashboard_high_attrition_warning(self, tmp_path: Path) -> None:
        old_date = (date.today() - timedelta(days=20)).isoformat()
        status = STATUS_MINIMAL.replace(
            "current_phase: 0",
            f"current_phase: 0\nwriting_schedule:\n  last_session_date: {old_date}\n  current_streak: 0\n  longest_streak: 0\n  total_sessions: 1\nwellbeing:\n  days_inactive: 20\n  attrition_risk: high",
        )
        (tmp_path / "STATUS.md").write_text(status, encoding="utf-8")
        (tmp_path / "sources").mkdir()
        sess = TezAtlasSession(tmp_path)
        state = sess.load()
        content = generate_dashboard_content(state, tmp_path)
        assert "attrition" in content.lower() or "risk" in content.lower()


# ── PHASE_NAMES coverage ──────────────────────────────────────────────────────

class TestPhaseNames:
    def test_all_doc_types_have_phase_names(self) -> None:
        expected = [
            "thesis", "article", "conference", "lit-review",
            "report", "book-chapter", "grant-proposal", "research-proposal",
        ]
        for dt in expected:
            assert dt in PHASE_NAMES, f"Missing PHASE_NAMES entry for '{dt}'"
            assert len(PHASE_NAMES[dt]) > 0

    def test_phase_names_are_strings(self) -> None:
        for doc_type, phases in PHASE_NAMES.items():
            for phase_num, name in phases.items():
                assert isinstance(name, str), f"{doc_type}[{phase_num}] is not a string"
                assert len(name) > 0
