---
title: "Session Continuity — STATUS.md & /resume"
title_tr: "Oturum Sürekliliği — STATUS.md ve /resume"
node_type: core
description: "For projects spanning weeks or months: auto-generate STATUS.md at session end summarizing current phase, next 3 actions, open questions, and blockers. The /resume command reads STATUS.md and reconstructs context at session start. Addresses the context loss problem for long thesis projects."
description_tr: "Haftalarca veya aylarca süren projeler için: oturum sonunda otomatik STATUS.md üret. /resume komutu STATUS.md'yi okuyarak bağlamı yeniden kurar."
tags: [core, session-continuity, status, resume, context-recovery]
links_to:
  - skills/core/context-management.md
  - skills/techniques/session-structure.md
  - skills/templates/tpl-status.md
  - skills/templates/tpl-dashboard.md
language: bilingual
version: "1.0"
---

# Session Continuity — STATUS.md & /resume
# Oturum Sürekliliği — STATUS.md ve /resume

## Overview / Genel Bakış

**EN:** Long academic projects (thesis: 6-24 months, dissertation: 2-5 years) span many Claude sessions. Context is lost between sessions. STATUS.md is the persistent bridge: a structured snapshot written at every session end and read at every session start.

**TR:** Uzun akademik projeler birçok Claude oturumuna yayılır. STATUS.md kalıcı köprüdür: her oturum sonunda yazılır, her oturum başında okunur.

---

## STATUS.md — Structure / Yapı

STATUS.md is generated automatically at session end. It is the single source of truth for session recovery.

```markdown
# STATUS.md — [Project Name]
Last updated: [YYYY-MM-DD HH:MM]
Session count: [N]

## 1. Project Snapshot / Proje Anlık Görüntüsü
- Document type: [thesis / article / grant / etc.]
- Phase: [current phase name + number]
- Phase completion: [X%]
- Days active: [total days since project start]
- Sessions completed: [N]

## 2. Current Position / Mevcut Konum
- Working on: [exact section/subsection being written]
- Last completed unit: [section/paragraph title + file]
- Next unit to start: [exact next task]
- Writing position: [chapter X, section Y, paragraph Z]

## 3. Next 3 Actions / Sonraki 3 Eylem
1. [IMMEDIATE] [Specific action — file, task, decision]
2. [THIS SESSION] [Specific action]
3. [NEXT SESSION] [Specific action]

## 4. Open Questions / Açık Sorular
- [Question 1 that needs resolution before proceeding]
- [Question 2]
(Delete when resolved)

## 5. Blockers / Engelleyiciler
- [Blocker 1: missing source / advisor feedback needed / etc.]
(Delete when resolved)

## 6. Source Status / Kaynak Durumu
- Total sources: [N]
- Read: [N]
- Saturation reached: [YES / NO / PARTIAL]
- Deferred pool: [N sources pending]

## 7. Phase Gate Status / Faz Kapısı Durumu
- Current gate: [gate criteria]
- Gate conditions met: [checklist — X of Y complete]
- Blocked on: [specific condition]

## 8. Writing Context (PBK) / Yazım Bağlamı
- Last paragraph: [main claim summary]
- Terms used: [list]
- Open point: [unresolved thread]
- Next paragraph task: [transition direction]
- Argument tracker: [X/Y subclaims complete]

## 9. Session Notes / Oturum Notları
[Free text — anything important that doesn't fit above]
```

---

## /resume Command — Protocol

When user runs `/tezatlas` and STATUS.md exists:

```
1. Read STATUS.md immediately
2. Check last_updated date:
   - < 7 days: full context reconstruction
   - 7-30 days: reconstruction + "It's been X days — verify nothing changed"
   - > 30 days: reconstruction + deep context check + offer phase review
3. Present recovery banner:

╔══════════════════════════════════════════════════════╗
║  RESUMING PROJECT: [Project Name]                    ║
║  Last session: [DATE] ([N days ago])                 ║
║  Phase: [PHASE NAME + NUMBER]                        ║
║  Next action: [ACTION FROM STATUS.md]                ║
║  Open questions: [N] | Blockers: [N]                 ║
╚══════════════════════════════════════════════════════╝

Do you want to:
A) Continue from where I left off [recommended]
B) Review STATUS.md before continuing
C) Start a different task

```

4. Load context: phase file + relevant technique files + STATUS.md content
5. If PBK section exists: reconstruct paragraph context card
6. Resume from "Next 3 Actions" item 1
```

---

## Session End — STATUS.md Generation

Add to every session end ritual (see `session-structure.md`):

```
After DURUM_OZETI.md + MEMORY.md updates:

1. Generate/update STATUS.md with current state
2. Update: last_updated, session_count, current_position
3. Clear resolved blockers and answered questions
4. Write Next 3 Actions based on current phase progress
5. Compute phase_completion % from phase checklist items
6. Generate DASHBOARD.md (see tpl-dashboard.md)
7. git commit: includes STATUS.md + DASHBOARD.md
```

---

## Days-Since-Last-Session Logic

At every session start, compute:

```python
days_inactive = (today - last_updated_date).days

if days_inactive == 0:
    # Same day — no recovery banner needed
elif days_inactive <= 3:
    # Short break — brief "Welcome back, continuing from..."
elif days_inactive <= 14:
    # Standard recovery — full STATUS.md banner
elif days_inactive <= 60:
    # Extended break — recovery + "Check if anything changed (advisor feedback? new sources?)"
else:
    # Long hiatus — recovery + phase review offer + wellbeing check-in
    # (Proposal #44: Risk Signal Detection)
```

**TR:** Aktif olmama süresine göre farklı kurtarma seviyeleri uygulanır.

---

## Integration Points / Entegrasyon Noktaları

- **Session start:** `session-structure.md` → read STATUS.md first
- **Session end:** `session-structure.md` → write STATUS.md + DASHBOARD.md
- **Phase gate:** Update STATUS.md "Phase Gate Status" when gate criteria change
- **Blocker added:** Update STATUS.md "Blockers" immediately
- **Advisor checkpoint:** Update STATUS.md "Open Questions" with advisor feedback
