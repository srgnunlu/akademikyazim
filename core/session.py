"""
core/session.py — TezAtlas Oturum Yöneticisi / Session Manager

STATUS.md okur/yazar, oturum durumunu takip eder, DASHBOARD.md üretir.

Kullanım:
    from core.session import TezAtlasSession
    session = TezAtlasSession()
    state = session.load()
    session.end_session(summary="...", sources_read_delta=2)
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

# ── Faz adları ──────────────────────────────────────────────────────────────

PHASE_NAMES: dict[str, dict[int, str]] = {
    "thesis": {
        0: "Kimlik / Identity",
        1: "Konu / Topic",
        2: "Katkı İddiası / Contribution Claim",
        3: "Okuma / Systematic Reading",
        4: "Yapı / Outline",
        5: "Yazım / First Draft",
        6: "Revizyon / Revision",
        7: "Finalizasyon / Submission",
    },
    "article": {
        0: "Kimlik / Identity",
        1: "Kaynak / Sources",
        2: "İskelet / Scaffold",
        3: "Okuma / Reading",
        4: "Taslak / Draft",
        5: "İç İnceleme / Internal Review",
        6: "Hakem Döngüsü / Peer Review",
    },
    "conference": {
        0: "Özet / Abstract",
        1: "Kaynak / Sources",
        2: "İskelet / Scaffold",
        3: "Okuma / Reading",
        4: "Taslak / Draft",
        5: "Sunum / Presentation",
    },
    "lit-review": {
        0: "Protokol / Protocol",
        1: "Veritabanı / Database Search",
        2: "Eleme / Screening",
        3: "Veri Çıkarma / Data Extraction",
        4: "Sentez / Synthesis",
        5: "Taslak / Draft",
    },
    "report": {
        0: "Yönetici Özeti / Executive Summary",
        1: "Kaynak / Sources",
        2: "Çerçeve / Framework",
        3: "Analiz / Analysis",
        4: "Taslak / Draft",
    },
    "book-chapter": {
        0: "Cilt Uyumu / Volume Alignment",
        1: "Kaynak / Sources",
        2: "İskelet / Scaffold",
        3: "Okuma / Reading",
        4: "Taslak / Draft",
    },
    "grant-proposal": {
        0: "Fon Analizi / Funder Analysis",
        1: "Kanıt Tabanı / Evidence Base",
        2: "Anlatı / Narrative Draft",
        3: "Bütçe / Budget",
        4: "Uyumluluk / Compliance",
        5: "Başvuru / Submission",
    },
    "research-proposal": {
        0: "Problem / Problem Statement",
        1: "Literatür / Lit. Scoping",
        2: "Metodoloji / Methodology",
        3: "Komite / Committee Draft",
        4: "Final Başvurusu / Final Submission",
    },
    "poster": {
        0: "Ana İddia / Core Claim",
        1: "Görsel Hiyerarşi / Visual Hierarchy",
    },
    "technical-report": {
        0: "Hipotez / Hypothesis",
        1: "Metodoloji / Methodology",
    },
}

# Attrition risk thresholds (days inactive)
ATTRITION_DAYS = {"medium": 7, "high": 14}


# ── STATUS.md parser ─────────────────────────────────────────────────────────

def _extract_yaml_blocks(content: str) -> dict[str, Any]:
    """Tüm ```yaml...``` bloklarını çıkar ve birleştirilmiş dict döndür."""
    pattern = re.compile(r"```yaml\n(.*?)```", re.DOTALL)
    merged: dict[str, Any] = {}
    for match in pattern.finditer(content):
        try:
            data = yaml.safe_load(match.group(1)) or {}
            if isinstance(data, dict):
                merged.update(data)
        except yaml.YAMLError:
            pass
    return merged


def _count_argumanlar(project_dir: Path) -> int:
    """ARGUMENTS.md'deki aktif argüman sayısını döndür."""
    path = project_dir / "ARGUMENTS.md"
    if not path.exists():
        return 0
    lines = path.read_text(encoding="utf-8").splitlines()
    # İçerik satırlarını say: `| N | ...` formatında, başlık ve ayraç hariç
    count = 0
    for line in lines:
        stripped = line.strip()
        if (
            stripped.startswith("|")
            and not stripped.startswith("| #")
            and "---" not in stripped
            and "İddia" not in stripped  # başlık satırı
        ):
            # Boş satırları atla
            cols = [c.strip() for c in stripped.strip("|").split("|")]
            if len(cols) >= 2 and cols[1]:  # ikinci sütun (İddia) dolu
                count += 1
    return count


# ── TezAtlasSession ──────────────────────────────────────────────────────────

class TezAtlasSession:
    """
    TezAtlas proje oturumunu yönetir.

    STATUS.md'yi okur/yazar; faz durumu, kaynak sayıları,
    yazım istatistikleri ve attrition risk sinyallerini takip eder.
    """

    def __init__(self, project_dir: Path | None = None) -> None:
        self.project_dir = project_dir or Path.cwd()
        self.status_path = self.project_dir / "STATUS.md"
        self._state: dict[str, Any] = {}

    # ── Load ─────────────────────────────────────────────────────────────────

    def load(self) -> dict[str, Any]:
        """
        STATUS.md'yi okur ve state dict döndürür.
        Dosya yoksa boş dict döner (yeni proje).
        """
        if not self.status_path.exists():
            return {}

        content = self.status_path.read_text(encoding="utf-8")
        self._state = _extract_yaml_blocks(content)

        # Türetilmiş alanlar
        self._state["_status_exists"] = True
        self._state["_project_dir"] = str(self.project_dir)
        self._state["_source_count"] = self._count_sources()
        self._state["_argumanlar_count"] = _count_argumanlar(self.project_dir)
        self._state["_days_inactive"] = self._days_since_last_session()
        self._state["_attrition_risk"] = self._compute_attrition_risk()
        self._state["_phase_name"] = self._current_phase_name()
        self._state["_savunma_zirhi_exists"] = (
            self.project_dir / "SAVUNMA_ZIRHI.md"
        ).exists()

        return self._state

    def is_new_project(self) -> bool:
        return not self.status_path.exists()

    # ── Save ─────────────────────────────────────────────────────────────────

    def save(self, updates: dict[str, Any]) -> None:
        """STATUS.md'yi günceller. Dosya yoksa oluşturur."""
        self._state.update(updates)
        self._state["last_updated"] = date.today().isoformat()
        self._write_status_md()

    def _write_status_md(self) -> None:
        """Mevcut state'ten STATUS.md üretir ve yazar."""
        s = self._state
        today = date.today().isoformat()
        doc_type = s.get("document_type", "thesis")
        current_phase = int(s.get("current_phase", 0))
        phase_names = PHASE_NAMES.get(doc_type, {})

        # Faz tablosu
        rows = []
        for phase_num, phase_name in sorted(phase_names.items()):
            if phase_num < current_phase:
                status = "✅ Tamamlandı"
                completed_at = s.get(f"phase_{phase_num}_completed", today)
            elif phase_num == current_phase:
                status = "⏳ Devam ediyor"
                completed_at = "—"
            else:
                status = "⏸ Bekliyor"
                completed_at = "—"
            rows.append(
                f"| {phase_num} | {phase_name} | {status} | {completed_at} |"
            )
        phase_table = "\n".join(rows)

        # Kaynaklar
        src = s.get("sources", {}) or {}
        total = src.get("total_collected", self._count_sources())
        read = src.get("read", 0)
        active = src.get("active", 0)
        deferred = src.get("deferred", 0)
        saturation = str(src.get("saturation_reached", False)).lower()

        # Yazım takibi
        ws = s.get("writing_schedule", {}) or {}
        streak = ws.get("current_streak", 0)
        longest = ws.get("longest_streak", 0)
        last_sess = ws.get("last_session_date") or "null"
        total_sess = ws.get("total_sessions", 0)

        # Wellbeing
        wb = s.get("wellbeing", {}) or {}
        days_inactive = wb.get("days_inactive", 0)
        attrition = wb.get("attrition_risk", "low")
        last_advisor = wb.get("last_advisor_checkpoint") or "null"
        goals_missed = wb.get("goals_missed_consecutive", 0)

        # Motivasyon
        mot = s.get("motivation", {}) or {}
        why = mot.get("why_statement") or "null"
        rec_at = mot.get("recorded_at") or "null"

        # Sonraki adımlar / Engeller — hem YAML hem markdown olarak yaz
        next_actions = s.get("next_actions") or []
        blockers = s.get("blockers") or []
        workflow_yaml = yaml.dump(
            {"next_actions": next_actions, "blockers": blockers},
            allow_unicode=True,
            default_flow_style=False,
        ).strip()

        if next_actions:
            actions_str = "\n".join(f"- {a}" for a in next_actions[:3])
        else:
            actions_str = "- [ ] *Sonraki adımı belirle / Define next action*"

        blockers_str = (
            "\n".join(f"- 🔴 {b}" for b in blockers)
            if blockers
            else "<!-- Aktif engel yok / No active blockers -->"
        )

        # Kapı tamamlamaları
        gates = s.get("gates") or {}
        gates_yaml = yaml.dump(gates, allow_unicode=True, default_flow_style=False).strip()

        content = f"""# STATUS.md — TezAtlas Proje Durumu

## Proje Kimliği

```yaml
title: "{s.get('title', '[Başlık Belirlenmedi]')}"
document_type: {doc_type}
field: {s.get('field', 'other')}
language: {s.get('language', 'Türkçe')}
created: "{s.get('created', today)}"
last_updated: "{today}"
current_phase: {current_phase}
```

## Faz İlerlemesi

| Faz | Ad | Durum | Tamamlanma |
|-----|----|-------|------------|
{phase_table}

## Kaynak Havuzu

```yaml
sources:
  total_collected: {total}
  read: {read}
  active: {active}
  deferred: {deferred}
  saturation_reached: {saturation}
```

## Yazım Takibi

```yaml
writing_schedule:
  current_streak: {streak}
  longest_streak: {longest}
  last_session_date: {last_sess}
  total_sessions: {total_sess}

wellbeing:
  last_session_date: "{today}"
  days_inactive: {days_inactive}
  goals_missed_consecutive: {goals_missed}
  last_advisor_checkpoint: {last_advisor}
  attrition_risk: {attrition}

motivation:
  why_statement: {why}
  recorded_at: {rec_at}
```

## Faz Kapıları / Phase Gates

```yaml
{gates_yaml}
```

## İş Akışı / Workflow State

```yaml
{workflow_yaml}
```

## Sonraki Adımlar / Next Actions

{actions_str}

## Aktif Engeller / Active Blockers

{blockers_str}

## Notlar

<!-- Danışman geri bildirimleri, kararlar, önemli notlar -->
"""
        self.status_path.write_text(content, encoding="utf-8")

    # ── Faz yönetimi ─────────────────────────────────────────────────────────

    def advance_phase(self, force: bool = False) -> dict[str, Any]:
        """
        Sonraki faza geçer. Gate kontrolü yapar.
        force=True ise gate başarısız olsa bile geçer (bypass kaydedilir).
        """
        from core.phase_gate import PhaseGate

        doc_type = self._state.get("document_type", "thesis")
        current = int(self._state.get("current_phase", 0))
        next_ph = current + 1

        gate = PhaseGate(self.project_dir, doc_type)
        result = gate.check(current, next_ph)

        if not result["passed"] and not force:
            return {"advanced": False, "gate_result": result}

        today = date.today().isoformat()
        gates = self._state.get("gates") or {}
        gates[f"{current}_to_{next_ph}"] = {
            "passed": True,
            "forced": not result["passed"],
            "date": today,
        }
        self.save({
            "current_phase": next_ph,
            f"phase_{current}_completed": today,
            "gates": gates,
        })
        return {"advanced": True, "from_phase": current, "to_phase": next_ph}

    def confirm_gate(self, gate_key: str) -> None:
        """Belirli bir gate koşulunu manuel olarak onaylar (örn. advisor_checkpoint)."""
        gates = self._state.get("gates") or {}
        gates[gate_key] = {"confirmed": True, "date": date.today().isoformat()}
        self.save({"gates": gates})

    # ── Session end ───────────────────────────────────────────────────────────

    def end_session(
        self,
        summary: str = "",
        sources_read_delta: int = 0,
        words_written: int = 0,
        next_actions: list[str] | None = None,
        blockers: list[str] | None = None,
        goals_met: bool = True,
    ) -> dict[str, Any]:
        """
        Oturumu kapatır: STATUS.md günceller, DASHBOARD.md üretir.
        Session summary dict döndürür.
        """
        from core.dashboard import generate_dashboard_content

        today = date.today().isoformat()
        s = self._state

        # Kaynakları güncelle
        src = s.get("sources") or {}
        if sources_read_delta > 0:
            src["read"] = src.get("read", 0) + sources_read_delta
        src["total_collected"] = max(
            src.get("total_collected", 0), self._count_sources()
        )
        s["sources"] = src

        # Yazım istatistikleri
        ws = s.get("writing_schedule") or {}
        last_sess = ws.get("last_session_date")
        if last_sess:
            try:
                from datetime import date as _date
                delta = (_date.today() - _date.fromisoformat(str(last_sess))).days
                ws["current_streak"] = (
                    ws.get("current_streak", 0) + 1 if delta <= 1 else 1
                )
            except (ValueError, TypeError):
                ws["current_streak"] = 1
        else:
            ws["current_streak"] = 1
        ws["longest_streak"] = max(ws.get("longest_streak", 0), ws["current_streak"])
        ws["last_session_date"] = today
        ws["total_sessions"] = ws.get("total_sessions", 0) + 1
        s["writing_schedule"] = ws

        # Wellbeing
        wb = s.get("wellbeing") or {}
        wb["last_session_date"] = today
        wb["days_inactive"] = 0
        wb["goals_missed_consecutive"] = (
            0 if goals_met else wb.get("goals_missed_consecutive", 0) + 1
        )
        wb["attrition_risk"] = "low"
        s["wellbeing"] = wb

        if next_actions is not None:
            s["next_actions"] = next_actions
        if blockers is not None:
            s["blockers"] = blockers

        self.save({})

        # DASHBOARD.md
        dashboard_path = self.project_dir / "DASHBOARD.md"
        dashboard_path.write_text(
            generate_dashboard_content(s, self.project_dir),
            encoding="utf-8",
        )

        return {
            "status": "session_closed",
            "date": today,
            "phase": s.get("current_phase", 0),
            "phase_name": self._current_phase_name(),
            "streak": ws["current_streak"],
            "total_sessions": ws["total_sessions"],
            "summary": summary,
        }

    # ── Yardımcı metodlar ─────────────────────────────────────────────────────

    def _count_sources(self) -> int:
        sources_dir = self.project_dir / "sources"
        if not sources_dir.is_dir():
            return 0
        return len(list(sources_dir.glob("*.pdf")))

    def _days_since_last_session(self) -> int:
        # Check wellbeing first, fall back to writing_schedule
        wb = self._state.get("wellbeing") or {}
        ws = self._state.get("writing_schedule") or {}
        last = wb.get("last_session_date") or ws.get("last_session_date")
        if not last:
            return 0
        try:
            from datetime import date as _date
            return (_date.today() - _date.fromisoformat(str(last))).days
        except (ValueError, TypeError):
            return 0

    def _compute_attrition_risk(self) -> str:
        days = self._state.get("_days_inactive", 0)
        if days >= ATTRITION_DAYS["high"]:
            return "high"
        if days >= ATTRITION_DAYS["medium"]:
            return "medium"
        return "low"

    def _current_phase_name(self) -> str:
        doc_type = self._state.get("document_type", "thesis")
        phase = int(self._state.get("current_phase", 0))
        return PHASE_NAMES.get(doc_type, {}).get(phase, f"Phase {phase}")
