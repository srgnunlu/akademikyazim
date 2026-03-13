---
title: "Template — DASHBOARD.md (Progress Dashboard)"
title_tr: "Şablon — DASHBOARD.md (İlerleme Panosu)"
node_type: template
description: "Auto-generated progress dashboard written at session end. Visual format with phase progress bar, source saturation, session streak, and next milestone. Motivated by goal-gradient hypothesis (Hull, 1932): effort increases as goal approaches."
description_tr: "Oturum sonunda otomatik oluşturulan ilerleme panosu. Hedef-gradyan hipotezine göre (Hull, 1932): hedefe yaklaştıkça çaba artar."
tags: [template, dashboard, progress, visualization, motivation]
links_to:
  - skills/core/session-continuity.md
  - skills/core/status-command.md
language: bilingual
version: "1.0"
---

# DASHBOARD.md Template

Copy this template to your project root as `DASHBOARD.md`.
Auto-updated at every session end by TezAtlas.

---

```markdown
# DASHBOARD — [Project Name]
Last updated: [YYYY-MM-DD] | Session [N]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## PHASE PROGRESS / FAZ İLERLEMESİ

Phase [N]/[TOTAL]: [Phase Name]
[████████░░░░░░░░░░░░] [X]%

Phase history:
  ✅ Phase 0 — [Name]
  ✅ Phase 1 — [Name]
  ✅ Phase 2 — [Name]
  🔄 Phase [N] — [Name] (current)
  ○  Phase [N+1] — [Name]
  ○  Phase [N+2] — [Name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SOURCES / KAYNAKLAR

[████████████████░░░░] [N] / [TOTAL] read ([X]%)
Saturation: [YES ✅ / PARTIAL ⚠️ / NO ❌]
Deferred pool: [N] sources pending

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## WRITING / YAZIM

Total words: [N]
Sections complete: [N] / [TOTAL]
[████████░░░░░░░░░░░░] [X]%

Section status:
  ✅ [Section 1 name] — [N words]
  ✅ [Section 2 name] — [N words]
  🔄 [Section N name] — [N words] (in progress)
  ○  [Section N+1 name]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## SESSION ACTIVITY / OTURUM AKTİVİTESİ

Days active: [N]
Total sessions: [N]
Last 7 days: [X X X X X X X] (■ = active day)
Current streak: [N days]
Longest streak: [N days]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## NEXT MILESTONE / SONRAKİ MİLESTONE

🎯 [Milestone name — e.g., "Advisor Checkpoint (Phase 4 gate)"]
   Remaining: [what needs to happen before milestone]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## BLOCKERS & OPEN QUESTIONS / ENGELLEYİCİLER

Blockers: [N]
  ⚠️ [Blocker description]

Open questions: [N]
  ❓ [Question description]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Progress Bar Generator / İlerleme Çubuğu Üreticisi

Formula for progress bars (20-character width):
```
filled = round(percentage / 5)  # 20 blocks total
bar = "█" * filled + "░" * (20 - filled)
output = f"[{bar}] {percentage}%"
```

Example outputs:
```
0%:   [░░░░░░░░░░░░░░░░░░░░] 0%
25%:  [█████░░░░░░░░░░░░░░░] 25%
50%:  [██████████░░░░░░░░░░] 50%
75%:  [███████████████░░░░░] 75%
100%: [████████████████████] 100%
```

---

## Session Streak Visualization

Last 7 days as blocks (rightmost = today):
```
■ = active session   □ = no session

Example — active 5 of 7 days:
[□ ■ ■ ■ □ ■ ■]
```

---

## Auto-Update Protocol

At session end, update DASHBOARD.md:
1. Phase progress: count completed checklist items / total
2. Source stats: from READING_REPORT.md
3. Writing stats: from MEMORY.md (word count, sections)
4. Session activity: add today's date if session was active
5. Next milestone: from STATUS.md Phase Gate Status
6. Blockers/questions: from STATUS.md

DASHBOARD.md is display-only — it never drives logic. STATUS.md drives logic.
