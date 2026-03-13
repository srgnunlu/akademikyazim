---
title: "/status — Quick Status Command"
title_tr: "/status — Hızlı Durum Komutu"
node_type: core
description: "Read-only 5-line status summary. Reads STATUS.md + READING_REPORT.md + MEMORY.md and outputs a compact summary: current phase, completion %, unread sources, next action, days since last session. No state changes."
description_tr: "Salt okunur 5 satırlık durum özeti. STATUS.md + READING_REPORT.md + MEMORY.md okur ve kompakt özet üretir. Durum değişikliği yapmaz."
tags: [core, status, slash-command, read-only]
links_to:
  - skills/core/session-continuity.md
  - skills/templates/tpl-dashboard.md
language: bilingual
version: "1.0"
---

# /status — Quick Status Command

## What It Does / Ne Yapar

**EN:** `/status` is a read-only command. It reads existing project files and outputs a 5-line compact summary without initializing a session, loading phase files, or making any changes.

**TR:** `/status` salt okunur bir komuttur. Mevcut proje dosyalarını okur ve hiçbir değişiklik yapmadan kompakt özet üretir.

---

## Output Format / Çıktı Formatı

```
📍 Phase: [Phase Name + Number] ([X]% complete)
📚 Sources: [N read] / [N total] — Saturation: [YES/NO/PARTIAL]
⏭  Next: [Specific next action from STATUS.md]
📅 Last session: [DATE] ([N days ago])
⚠️  Blockers: [N] | Open questions: [N]
```

**Example / Örnek:**
```
📍 Phase: Phase 6 — Writing (42% complete)
📚 Sources: 34 read / 51 total — Saturation: PARTIAL
⏭  Next: Write section 3.2 (argument: state capacity theory)
📅 Last session: 2026-02-25 (2 days ago)
⚠️  Blockers: 1 | Open questions: 2
```

---

## How to Invoke / Nasıl Çağrılır

```
/status
```

No arguments. No options. Always read-only.

---

## Data Sources (Priority Order) / Veri Kaynakları

1. **STATUS.md** — phase, completion %, next action, blockers, open questions, last updated
2. **MEMORY.md** — total word count, completed sections
3. **READING_REPORT.md** — source counts (total, read, saturation)
4. **DASHBOARD.md** — if exists, pull session streak

If STATUS.md does not exist:
```
⚠️  No STATUS.md found. Run /tezatlas to initialize or resume a project.
```

If READING_REPORT.md does not exist:
```
📚 Sources: unknown (READING_REPORT.md not found)
```

---

## What /status Does NOT Do

- Does NOT initialize a session
- Does NOT load phase skill nodes
- Does NOT update any files
- Does NOT start the SRL session ritual
- Does NOT trigger agent calls
- Does NOT open a new project

For full session initialization: run `/tezatlas`
For full dashboard: read `DASHBOARD.md`

---

## Implementation (Claude Code Behavior)

When `/status` is invoked:

```
1. Read STATUS.md (if exists)
2. Read MEMORY.md (if exists)
3. Read READING_REPORT.md (if exists)
4. Compute days_since_last_session
5. Extract: phase, completion %, next_action, blocker_count, question_count
6. Format and output 5-line summary
7. STOP — do not proceed to session initialization
```

If user wants to continue after `/status`:
- Ask: "Do you want to continue this session? I can resume from [next action]."
