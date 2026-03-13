---
title: "TezAtlas Orchestrator Interface"
title_tr: "TezAtlas Orkestratör Arayüzü"
node_type: core
description: "Defines the abstract orchestrator contract that TezAtlas requires. Claude Code is one implementation; any session-based AI assistant with tool use and file access can serve as orchestrator."
description_tr: "TezAtlas'ın gerektirdiği soyut orkestratör sözleşmesini tanımlar. Claude Code bir implementasyondur; araç kullanımı ve dosya erişimine sahip herhangi bir oturum tabanlı YZ asistanı orkestratör olarak çalışabilir."
tags: [architecture, orchestrator, abstraction, portability]
links_to:
  - skills/core/agent-orchestration.md
  - skills/core/session-continuity.md
  - agents/README.md
language: bilingual
version: "1.0"
---

# TezAtlas Orchestrator Interface / Orkestratör Arayüzü

## What Is the Orchestrator? / Orkestratör Nedir?

TezAtlas separates two concerns:

1. **The workflow engine** — phase gates, Iron Rules, skill nodes, session state. This is TezAtlas itself and is implementation-agnostic.
2. **The orchestrator** — the AI assistant that runs the workflow engine within a session, reads and writes files, calls external tools, and maintains conversational state.

Claude Code is the **reference implementation** of the orchestrator. But TezAtlas is designed so that any AI assistant meeting the interface requirements below can run the framework.

---

## Orchestrator Requirements / Orkestratör Gereksinimleri

A compliant TezAtlas orchestrator MUST be able to:

### 1. File System Access
- Read `.md` files from `skills/`, `templates/`, `notes/`
- Write `STATUS.md`, `READING_REPORT.md`, `DASHBOARD.md`, `ARGUMENTS.md`
- Append to session logs

### 2. Tool Use / Shell Execution
- Run `python3 scripts/find_source.py` (Iron Rule 3)
- Run `python3 ocr_pipeline.py` (PDF text extraction)
- Run `python3 agents/run.py` (multi-agent calls)
- Run `git commit` (Iron Rule 6)

### 3. Selective Context Loading
- Load skill nodes on demand — NOT all 130 nodes at once
- Release nodes when a phase exits
- Maintain session state between tool calls

### 4. Session Continuity
- Read `STATUS.md` at session start
- Write `STATUS.md` at session end
- Present recovery banner when resuming interrupted work

### 5. Phase Gate Enforcement
- Block phase transitions without required gate conditions
- Request supervisor/advisor checkpoint documents at mandated gates

---

## Claude Code as Orchestrator / Claude Code Orkestratör Olarak

Claude Code satisfies all five requirements:

| Requirement | Claude Code Mechanism |
|-------------|----------------------|
| File system | `Read`, `Write`, `Edit` tools |
| Tool use | `Bash` tool (subprocess execution) |
| Selective loading | Context window management; only referenced nodes are read |
| Session continuity | `STATUS.md` + `/tezatlas` recovery banner |
| Phase gate enforcement | CLAUDE.md Iron Rules + phase node gate fields |

**Claude Code-specific dependencies to isolate:**
- `/tezatlas` slash command → skill invocation system
- `CLAUDE.md` → auto-loaded context
- Claude Code's context window limits → node loading strategy

---

## Alternative Orchestrator Implementations

Any AI assistant with tool use capability can serve as orchestrator. Mapping of requirements to other systems:

| Requirement | Cursor | GitHub Copilot Chat | Custom API Agent |
|-------------|--------|---------------------|-----------------|
| File system | ✅ native | ✅ via workspace | ✅ file tools |
| Tool use | ✅ run commands | ⚠️ limited | ✅ function calling |
| Selective loading | ✅ context | ⚠️ manual | ✅ programmatic |
| Session continuity | ✅ via STATUS.md | ✅ via STATUS.md | ✅ via STATUS.md |
| Phase gate enforcement | ⚠️ prompt-based | ⚠️ prompt-based | ✅ if coded |

For non-Claude-Code orchestrators, the `STATUS.md` file is the critical portability layer — it encodes all session state in a format that any orchestrator can read and write.

---

## Portability Layer: STATUS.md

`STATUS.md` is the single artifact that makes TezAtlas orchestrator-agnostic:

```markdown
## TezAtlas Session State
phase: 3
document_type: thesis
language: tr
field: economics
next_actions:
  - Read Smith_2023.pdf
  - Complete saturation gate checklist
  - Commit session notes
blockers: []
pbk:  # Paragraph Context Card (last paragraph written)
  claim: "..."
  open_points: [...]
```

Any orchestrator that can read and write this file can resume a TezAtlas session, regardless of which orchestrator started it.

---

## What Iron Rules Require From the Orchestrator

Some Iron Rules impose direct requirements on the orchestrator implementation:

| Rule | Orchestrator Requirement |
|------|--------------------------|
| Rule 1 (no writing without source) | Must verify `sources/` directory before generation |
| Rule 3 (AI downloads first) | Must be able to execute `scripts/find_source.py` |
| Rule 6 (mandatory git commit) | Must have `git` execution capability |
| Rule 7 (no progress without action) | Must write to `STATUS.md` when blockers are detected |

An orchestrator that cannot satisfy Rule 3 or Rule 6 MUST document this limitation explicitly and prompt the user to perform the action manually.

---

## Multi-Agent Delegation / Çok-Ajanlı Yetkilendirme

The orchestrator is responsible for delegating to specialized agents when appropriate:

```
Orchestrator (Claude Code)
├── Source Hunter Agent    (via agents/run.py, any LLM provider)
├── Methodology Checker    (via agents/run.py, any LLM provider)
├── Citation Verifier      (via agents/run.py, any LLM provider)
└── find_source.py         (academic APIs, no LLM required)
```

The orchestrator is NOT responsible for the agents' LLM provider choice — that is configured in `agents.yaml`. This separation means the orchestrator (e.g. Claude Code) and the agents can use different LLMs.

---

## Version / Sürüm

Orchestrator interface version: **1.0**

Breaking changes to this interface will be versioned and documented in `CHANGELOG.md`.
