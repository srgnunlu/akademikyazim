"""
core/dashboard.py — TezAtlas DASHBOARD.md Üreticisi

Hull (1932) hedef-gradient hipotezine dayanan ASCII progress bar'lar.
Faz ilerleme yüzdesi, kaynak doygunluğu, yazım istatistikleri, streak takibi.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from core.session import PHASE_NAMES


def _bar(value: float, width: int = 20) -> str:
    """0-1 arasında value için ASCII progress bar üretir."""
    value = max(0.0, min(1.0, value))
    filled = round(value * width)
    empty = width - filled
    return "█" * filled + "░" * empty


def _pct(value: float) -> str:
    return f"{round(value * 100):3d}%"


def generate_dashboard_content(state: dict[str, Any], project_dir: Path) -> str:
    """
    DASHBOARD.md içeriğini üretir.

    state: TezAtlasSession.load() çıktısı
    project_dir: proje kök dizini
    """
    today = date.today().isoformat()
    doc_type = state.get("document_type", "thesis")
    current_phase = int(state.get("current_phase", 0))
    phase_names = PHASE_NAMES.get(doc_type, {})
    total_phases = len(phase_names)

    # Faz ilerleme %
    phase_pct = current_phase / total_phases if total_phases > 0 else 0.0
    phase_name = phase_names.get(current_phase, f"Phase {current_phase}")
    next_phase = phase_names.get(current_phase + 1, "—")

    # Kaynak verileri
    src = state.get("sources") or {}
    total_sources = int(src.get("total_collected", 0))
    read_sources = int(src.get("read", 0))
    deferred = int(src.get("deferred", 0))
    saturation = src.get("saturation_reached", False)
    src_pct = read_sources / total_sources if total_sources > 0 else 0.0

    # Yazım istatistikleri
    ws = state.get("writing_schedule") or {}
    streak = int(ws.get("current_streak", 0))
    longest_streak = int(ws.get("longest_streak", 0))
    total_sessions = int(ws.get("total_sessions", 0))

    # Wellbeing
    wb = state.get("wellbeing") or {}
    days_inactive = int(wb.get("days_inactive", 0))
    attrition_risk = wb.get("attrition_risk", "low")
    risk_icon = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(attrition_risk, "🟢")

    # Argümanlar
    arg_count = int(state.get("_argumanlar_count", 0))

    # Kelime sayısı / yazım istatistikleri
    writing_stats = state.get("writing_stats") or {}
    total_words = int(writing_stats.get("total_words", 0))
    target_words = int(writing_stats.get("target_words", 0))
    pdf_pages = int(writing_stats.get("pdf_pages", 0))
    last_compile = writing_stats.get("last_compile", "—")
    word_pct = total_words / target_words if target_words > 0 else 0.0

    # Sonraki adımlar
    next_actions = state.get("next_actions") or []
    blockers = state.get("blockers") or []

    # Saturation durumu
    sat_label = "✅ Doygunluğa ulaşıldı" if saturation else f"{read_sources}/{total_sources} okundu"
    sat_pct_val = 1.0 if saturation else src_pct

    # Attrition uyarısı
    attrition_warn = ""
    if attrition_risk == "high":
        attrition_warn = "\n> ⚠️ **Yüksek attrition riski!** 14+ gündür oturum yok. /tezatlas ile devam et.\n"
    elif attrition_risk == "medium":
        attrition_warn = "\n> 💛 **Dikkat:** 7+ gündür oturum yok. Küçük bir adım at.\n"

    # Engel uyarısı
    blocker_section = ""
    if blockers:
        blocker_lines = "\n".join(f"- 🔴 {b}" for b in blockers)
        blocker_section = f"\n## 🚧 Aktif Engeller\n\n{blocker_lines}\n"

    # Sonraki adımlar
    action_section = ""
    if next_actions:
        action_lines = "\n".join(f"- [ ] {a}" for a in next_actions[:3])
        action_section = f"\n## 📋 Sonraki Adımlar\n\n{action_lines}\n"

    # ARGUMENTS durumu
    arg_icon = "✅" if arg_count >= 5 else ("⚠️" if arg_count >= 3 else "❌")
    arg_label = f"{arg_count} argüman" if arg_count > 0 else "Henüz argüman yok"

    # Savunma zırhı
    savunma_path = project_dir / "SAVUNMA_ZIRHI.md"
    savunma_icon = "✅" if savunma_path.exists() else "❌"

    dashboard = f"""# DASHBOARD.md — TezAtlas İlerleme Panosu

*Güncellendi: {today}*
{attrition_warn}
---

## 📊 Faz İlerlemesi

```
{doc_type.upper()} → Faz {current_phase}: {phase_name}

Faz     {_bar(phase_pct)} {_pct(phase_pct)}  ({current_phase}/{total_phases} faz)
```

**Aktif faz:** {phase_name}
**Sonraki faz:** {next_phase}

---

## 📚 Okuma & Doygunluk

```
Kaynaklar {_bar(sat_pct_val)} {_pct(sat_pct_val)}  {sat_label}
```

| Alan | Değer |
|------|-------|
| Toplam kaynak | {total_sources} |
| Okunan | {read_sources} |
| Ertelenmiş (ERKEN) | {deferred} |
| Doygunluk | {"✅ Evet" if saturation else "⏳ Henüz değil"} |

---

## ✍️ Yazım & Kelime Sayısı

```
Streak  {"█" * min(streak, 20)}{"░" * max(0, 20 - streak)}  {streak} gün
{f"Kelime  {_bar(word_pct)} {_pct(word_pct)}  ({total_words:,} / {target_words:,})" if target_words > 0 else "Kelime  (hedef henüz belirlenmedi)"}
```

| Alan | Değer |
|------|-------|
| Aktif streak | {streak} gün |
| En uzun streak | {longest_streak} gün |
| Toplam oturum | {total_sessions} |
| Son oturumdan | {days_inactive} gün |
| Attrition riski | {risk_icon} {attrition_risk.upper()} |
| Toplam kelime | {f"{total_words:,}" if total_words > 0 else "—"} |
| Hedef kelime | {f"{target_words:,}" if target_words > 0 else "—"} |
| PDF sayfaları | {pdf_pages if pdf_pages > 0 else "—"} |
| Son derleme | {last_compile} |

---

## 🗺️ Argümanlar & Savunma

| Kontrol | Durum |
|---------|-------|
| Argüman girişleri | {arg_icon} {arg_label} |
| SAVUNMA_ZIRHI.md | {savunma_icon} {"Mevcut" if savunma_path.exists() else "Eksik (Iron Rule 8)"} |
{action_section}{blocker_section}
---

## 🔮 Sıradaki Kilometre Taşı

"""
    # Sıradaki kilometre taşı
    milestones = {
        0: "Phase 1'e geç: İlk kaynakları sources/ klasörüne ekle",
        1: "Phase 2'ye geç: En az 3 kaynak + ARGUMENTS.md başlat",
        2: "Phase 3'e geç: En az 3 argüman + 3 kaynak ekle",
        3: "Phase 4'e geç: %80 kaynak oku + SAVUNMA_ZIRHI.md oluştur",
        4: "Phase 5'e geç: Danışman outline onayı al",
        5: "Phase 6'ya geç: İlk taslağı tamamla",
        6: "Phase 7'ye geç: Revizyon döngüsünü tamamla",
        7: "🎉 Finalizasyon fazında — son kontrolleri yap ve teslim et",
    }
    dashboard += milestones.get(current_phase, "Sonraki adımı belirle") + "\n"

    return dashboard
