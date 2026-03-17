---
title: "TezAtlas — Skill Graph Index"
node_type: index
---

# TezAtlas Skill Graph

Root entry point. Follow links to the relevant cluster.

## Slash Commands

### Core
- `/tezatlas` — Start or resume a session
- `/import` — Import existing academic work (mid-project entry)
- `/status` — Read-only project status check
- `/review-draft <file>` — 4-layer draft review: argument integrity, source anchoring, style, literature alignment
- `/ai-review` — Trigger AI Peer Review at any time (phase gate, section, argument, or saturation)

### Literature Intelligence
- `/intake` — Source map: cluster sources, extract core claims, flag contradictions → SOURCE_MAP.md
- `/contradictions` — Enhanced cross-source contradiction scanner → CONTRADICTIONS.md
- `/citation-chain` — Intellectual lineage: who started → challenged → developed → consensus → CITATION_CHAIN.md
- `/gaps` — Research gap scanner: unanswered questions, coverage gaps → GAPS.md
- `/method-audit` — Methodology audit across sources + user's own method
- `/assumptions` — Untested assumption finder with risk analysis → ASSUMPTIONS.md
- `/knowledge-map` — Field structure: pillars + contentions + boundaries → KNOWLEDGE_MAP.md
- `/so-what` — "So What?" test: 3 essential statements → SO_WHAT.md
- `/synthesize` — Multi-source synthesis by argument → SYNTHESIS.md

### Output & Submission
- `/latex` — Convert Markdown drafts to LaTeX (.tex)
- `/compile-pdf` — Compile LaTeX to PDF via latexmk (with word count)
- `/submission-check` — Pre-submission checklist (word count, citations, structure, blind review)

### Other
- `/devil-advocate` — Challenge your claim/argument from 4 angles before writing
- `/citation-check "<claim>" <source.pdf>` — Verify a specific claim against a source (Iron Rule 4)
- `/generate-citations` — Extract DOIs from PDFs → CrossRef/OpenAlex → BibTeX/RIS
- `/career-profile` — Research career dashboard + skill gap analysis
- `/install-plugin <path>` — Validate and install a community plugin

## AI Intelligence Scripts
- `scripts/snowball.py` — Extract DOIs from notes/PDFs → SNOWBALL_CANDIDATES.md (Iron Rule 2)
- `scripts/contradiction_scan.py` — Cross-source contradiction detection → CONTRADICTIONS.md
- `scripts/saturation_map.py` — Argument coverage mapping → SATURATION.md
- `scripts/rq_drift.py` — Research question drift detection → DRIFT_REPORT.md
- `scripts/synthesize.py` — Multi-source synthesis scaffold → SYNTHESIS.md

## Core
- [[core/what-is-tezatlas]] — What is TezAtlas
- [[core/onboarding]] — Start here (document type + language selection)
- [[core/iron-rules]] — 9 immutable constraints (always active)
- [[core/source-policy]] — Web vs local source rules by phase
- [[core/academic-integrity]] — AI policy + advisor checkpoints
- [[core/research-ethics]] — IRB, KVKK, publication ethics, data integrity
- [[core/reviewer-mode]] — Independent researcher checkpoint protocol (Iron Rule 5 alternative)
- [[core/working-principles]] — 8 operational principles
- [[core/context-management]] — Session memory system
- [[core/quality-control]] — Per-section and document-wide checklists
- [[core/error-recovery]] — Recovery protocols

## Phases by Document Type
- [Thesis phases](phases/thesis/) — Doctoral / Master's Thesis (8 phases)
- [Article phases](phases/article/) — Journal Article (6 phases)
- [Conference phases](phases/conference/) — Conference Paper (5 phases)
- [Lit-review phases](phases/lit-review/) — Literature / Systematic Review (6 phases)
- [Report phases](phases/report/) — Research Report (5 phases)
- [Book-chapter phases](phases/book-chapter/) — Book Chapter (5 phases)
- [Grant-proposal phases](phases/grant-proposal/) — Grant Proposal (6 phases)
- [Research-proposal phases](phases/research-proposal/) — Research Proposal / Prospectus (5 phases)
- [Poster phases](phases/poster/) — Poster / Extended Abstract (2 phases)
- [Technical-report phases](phases/technical-report/) — Technical / Lab Report (2 phases)

## Architecture (AI Core)
- [[architecture/methodological-oracle]] — Methodology interrogation and bias check
- [[architecture/proactive-methodological-guardian]] — Real-time drafting guardrails
- [[architecture/feedback-integration-engine]] — FIRE: Universal feedback ingestor
- [[architecture/ai-provenance-layer]] — Invisible source-tracking for AI drafts
- [[architecture/reproducibility-layer]] — Code and data provenance tracking
- [[architecture/collaborative-workspace]] — Multi-author conflict resolution & CRediT
- [[architecture/adaptive-output]] — Derivative outputs (press release, brief) without fabrication
- [[architecture/autonomous-telemetry]] — Privacy-safe UX feedback & struggle detection

## Techniques
- [[techniques/contribution-claim]] — Originality & gap verification (Phase 0 gate, all doc types)
- [[techniques/snowball-sampling]] — Source discovery loop
- [[techniques/saturation-check]] — When to stop reading
- [[techniques/critical-reading]] — Evaluating sources
- [[techniques/argument-mapping]] — Structure from reading
- [[techniques/argument-evaluation]] — Logical quality check
- [[techniques/pdf-reading]] — Pre-check and handling
- [[techniques/source-hunting]] — Finding and downloading
- [[techniques/session-structure]] — Start and end rituals
- [[techniques/literature-synthesis]] — Synthesizing multiple sources into arguments
- [[techniques/feedback-integration]] — Managing revisions and reviewer responses
- [[techniques/journal-selection]] — Selecting the right publication venue
- [[techniques/citation-formatting]] — APA / MLA / Chicago / Bluebook / Vancouver
- [[techniques/pre-submission-review]] — Peer review simulation before submission
- [[techniques/academic-writing-quality]] — Hedging, signposting, argument flow, register
- [[techniques/turkish-academic-writing]] — TR-specific conventions, YÖK/TR Dizin standards
- [[techniques/drafting-alternatives]] — A/B/C/D drafting generation & scored evaluation matrix

## Templates
- [[templates/tpl-notes]] — Reading notes (_notlar.md equivalent)
- [[templates/tpl-reading-report]] — Progress dashboard
- [[templates/tpl-source-inventory]] — Source list
- [[templates/tpl-outline]] — Structure outline
- [[templates/tpl-project-identity]] — Phase 0 output
- [[templates/tpl-thesis-protocol]] — Phase 5 output (thesis)
- [[templates/tpl-source-map]] — Phase 4 output
- [[templates/tpl-terminology]] — Glossary
- [[templates/tpl-status-summary]] — Session-end update
- [[templates/tpl-lessons]] — Self-improvement log
- [[templates/tpl-topic-discovery]] — Phase 1 output

## Discipline Modules
- [[disciplines/law]] — Law / Legal Studies (TR + comparative, citation, methodology)
- [[disciplines/medicine]] — Medicine & Health Sciences (EQUATOR, IRB, Vancouver)
- [[disciplines/stem]] — STEM & Engineering (LaTeX, IEEE, Reproducibility)
- [[disciplines/social-sciences]] — Social Sciences (APA 7, Qualitative, Survey Design)
- [[disciplines/humanities]] — Humanities (Chicago 17/MLA 9, Archival, Close Reading)
- [[disciplines/egitim]] — Eğitim Bilimleri (Education)
- [[disciplines/isletme]] — İşletme (Business Administration)

## Tooling & UX
- [[tooling/annas-archive]] — Source download
- [[tooling/database-access]] — Institutional databases
- [[tooling/git-workflow]] — Version control
- [[tooling/citation-formats]] — APA / Chicago / MLA / IEEE / Bluebook rules
- [[tooling/reference-managers]] — Zotero / Mendeley / BibTeX integration
- [[ux/srl-session-ritual]] — Pre/post session goals and reflection (Boice Protocol)
- [[ux/anxiety-aware-language]] — Anti-perfectionism and motivation protocols

## Navigation (MOC)
- [[moc/MOC-core]] — Core cluster map
- [[moc/MOC-phases]] — Phases cluster map
- [[moc/MOC-citations]] — Citations cluster map
- [[moc/MOC-disciplines]] — Disciplines map
- [[moc/MOC-universities]] — Universities map
- [[moc/MOC-architecture]] — Architecture & AI Features map
