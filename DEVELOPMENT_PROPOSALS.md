# TezAtlas — Development Proposals

**Last updated:** 2026-02-22
**Framework version:** 1.0
**Contributing:** Add new proposals at the end with the next number.

---

## How to Read This File

| Field | Values |
|---|---|
| Status | `Proposed` / `In Progress` / `Done` |
| Priority | `Critical` / `High` / `Medium` / `Low` |
| Category | `phase` / `core` / `ocr` / `architecture` / `discipline` / `tooling` / `ux` |

---

## Phase Completions (Applied from Gemini feedback 2026-02-22)

### 1. Thesis — Empirical Research Fork (Methodology Fork)
**Status:** Done
**Priority:** Critical
**Category:** phase
Added quantitative / qualitative / mixed-methods sub-phases (3-E1, 3-E2, 3-E3) to thesis Phase 3. Phase 4 gate requires `analysis_results.md` if empirical path chosen.

### 2. Article — Peer Review Revision Cycle (Phase 6)
**Status:** Done
**Priority:** Critical
**Category:** phase
New phase: editorial decision triage, point-by-point reviewer response format, revision version tracking (git), resubmission checklist, strategic journal-switching protocol.

### 3. Conference — Presentation Preparation (Phase 5)
**Status:** Done
**Priority:** High
**Category:** phase
New phase: slide structure (time-slot driven), talk notes, Q&A prep (anticipated questions), rehearsal protocol, post-conference repository upload.

### 4. Literature Review — PROSPERO + PRISMA-ScR
**Status:** Done
**Priority:** High
**Category:** phase
Added PROSPERO pre-registration guidance, review type matrix (systematic/scoping/meta-analysis/umbrella), Phase 3b placeholder for statistical synthesis if meta-analysis planned.

### 5. Iron Rule 5 — Advisor Adaptation by Document Type
**Status:** Done
**Priority:** High
**Category:** core
"Advisor" now maps to: faculty advisor (thesis), co-author/colleague (article), colleague reviewer (conference), independent screener (lit-review), client/stakeholder (report), volume editor (book chapter).

---

## Phase Gaps (Identified, Not Yet Applied)

### 6. Article — Journal Selection Phase (Phase 0.5)
**Status:** Done
**Priority:** High
**Category:** phase
Before writing begins, add a journal targeting phase: impact factor, scope fit, audience, open access policy, typical review time, acceptance rate. Output: `journal_target.md`. Rationale: wrong journal selection wastes 6-12 months of revision cycles.

### 7. Thesis — Defense Preparation Phase (Phase 8)
**Status:** Done
**Priority:** High
**Category:** phase
Separate defense prep from finalization: mock defense, committee-specific Q&A prep, defense slides, known committee preferences, post-defense revision tracking.

### 8. Research Report — Dissemination Phase (Phase 5)
**Status:** Done
**Priority:** Medium
**Category:** phase
After writing: communication plan (who gets the report, in what format), executive briefing (1-page), press release, stakeholder presentation, open-access hosting.

### 9. Book Chapter — Editor Feedback & Final Submission (Phase 5)
**Status:** Done
**Priority:** Medium
**Category:** phase
Dedicated phase for editor feedback round, final alignment with volume argument, publisher format compliance, bio + contributor notes.

### 10. All Types — Empirical Path for Article/Conference
**Status:** Done
**Priority:** High
**Category:** phase
Apply the methodology fork (quantitative/qualitative/mixed) to article Phase 2 and conference Phase 1. Currently only implemented for thesis.

---

## New Document Types

### 11. Grant Proposal / Funding Application
**Status:** Done
**Priority:** High
**Category:** phase
New document type: grant proposals (NSF, ERC, TÜBİTAK, Wellcome, DFG). Phases: funder analysis → problem statement → methodology → budget → impact statement → submission. Iron Rule adaptation: funders have strict word limits — concision is a constraint, not a preference.

### 12. Research Proposal / Dissertation Prospectus
**Status:** Done
**Priority:** High
**Category:** phase
Pre-thesis document type: the proposal that needs advisor/committee approval before thesis work begins. Shorter than thesis, persuasive framing. 5 phases: problem, literature, methodology, expected contribution, timeline.

### 13. Poster / Extended Abstract
**Status:** Done
**Priority:** Medium
**Category:** phase
Conference posters and extended abstracts (1-4 pages) as a distinct type. Key constraint: extreme compression — every word earns its place. Phases: claim → visual hierarchy design → content compression → print/display prep.

### 14. Technical / Lab Report
**Status:** Done
**Priority:** Medium
**Category:** phase
Structured empirical report (STEM): hypothesis, methods, results, discussion, conclusion. Differs from research report in being more formulaic and reproducibility-focused.

---

## Architecture: The Methodological Oracle

### 15. Methodological Oracle (MO) — Core Feature
**Status:** Done
**Priority:** Critical
**Category:** architecture
An ontology-driven methodology advisor that: (a) suggests appropriate methods for the research question, (b) warns about common biases (p-hacking, selection bias, confounding), (c) recommends sample size calculations, (d) flags ethical issues proactively, (e) integrates with code (Python/R) for reproducibility. This is the single biggest differentiator from all other AI research tools.

### 16. Cognitive Augmentation Workspace (CAW)
**Status:** Done
**Priority:** High
**Category:** architecture
As the user reads and writes, auto-extract key claims, evidence, and counter-arguments into a semantic concept map + argumentation graph. Gap detector: which arguments lack evidence? Contradiction detector: source A says X, source B says ¬X. Devil's Advocate agent: challenges assumptions before writing phase. This lives in Phase 3-4 transition.

### 17. Feedback Integration & Response Engine (FIRE)
**Status:** Done
**Priority:** High
**Category:** architecture
Universal feedback ingestor: parse reviewer comments (PDF), supervisor track-changes (docx), email feedback, OCR of handwritten notes. Semantic categorization: major/minor, methodology/writing/structure. Auto-draft point-by-point response document. Link each response to the specific manuscript change. Solves the #2 most painful academic workflow problem.

### 18. Dynamic Publication Strategist (DPS)
**Status:** Done
**Priority:** Medium
**Category:** architecture
Journal/conference recommendation engine: content → venue matching based on topic, methodology, contribution type. Know the submission requirements (page format, reference style, anonymization rules) per target venue. Auto-reformat references and structure for target journal. Generate cover letter template.

### 19. Proactive Methodological Guardian
**Status:** Done
**Priority:** Critical
**Category:** architecture
Always-on monitoring: detects methodological flaws in real-time (not just at phase gates), suggests candidate sources for unsourced claims (proactive Iron Rule 1 enforcement), personalized to researcher's field and typical mistakes. This is NOT a reactive checker — it intervenes before the error becomes a draft. The key differentiator from all competitors (Elicit, Consensus, Perplexity, Zotero — none of them do this).

### 20. Reproducibility & Data Provenance Layer
**Status:** Done
**Priority:** High
**Category:** architecture
Document every methodological decision: software versions, random seeds, data cleaning steps, exclusion rationale. Generate a methods appendix automatically. Output: replication package ready for journal submission. FAIR principles built in (Findable, Accessible, Interoperable, Reusable).

---

## Discipline-Specific Modules

### 21. Law / Legal Research Module
**Status:** Done
**Priority:** High
**Category:** discipline
Legal citation styles: Bluebook (US), OSCOLA (UK), AGLC (Australia). Primary source handling: cases, statutes, regulations, legislative history. Argumentation structure for persuasive legal writing vs. academic legal analysis. Turkish law: UYAP-compatible citation format, Yargıtay/Danıştay/AYM citation conventions.

### 22. Medicine / Health Sciences Module
**Status:** Done
**Priority:** High
**Category:** discipline
IRB/ethics board application template, clinical trial registration (ClinicalTrials.gov), reporting guidelines (CONSORT for RCTs, STROBE for observational, PRISMA for reviews, SPIRIT for protocols), risk of bias tools (Cochrane RoB 2.0, GRADE). HIPAA/GDPR compliance for patient data.

### 23. STEM / Engineering / CS Module
**Status:** Done
**Priority:** High
**Category:** discipline
LaTeX workflow node (Overleaf, local compile, BibTeX/biber). GitHub/GitLab integration for code repositories linked to paper. Computational reproducibility: environment capture (conda env, Docker, requirements.txt), MLflow/W&B experiment tracking, benchmark comparison format. IEEE/ACM citation styles.

### 24. Social Sciences Module
**Status:** Done
**Priority:** Medium
**Category:** discipline
APA 7 citation deep support. Qualitative methods: interview protocol design, transcription standards, Atlas.ti/NVivo compatible codebook format, member-checking documentation. Survey design: Likert scale conventions, validity/reliability reporting. Mixed methods integration protocol.

### 25. Humanities Module
**Status:** Done
**Priority:** Medium
**Category:** discipline
Chicago 17 (author-date and notes-bibliography variants). Primary source handling: archival documents, manuscripts, historical texts. Discourse analysis, close reading, hermeneutics documentation. MLA 9 for literary studies.

---

## Tooling & Integrations

### 26. Citation Format Node
**Status:** Done
**Priority:** High
**Category:** tooling
A dedicated `skills/tooling/citation-formats.md` node covering: APA 7, Chicago 17, MLA 9, Vancouver, IEEE, Bluebook, OSCOLA. Per-document-type defaults. Common mistakes per format. How to switch formats without losing data. BibTeX/RIS export guidance.

### 27. LaTeX Workflow Node
**Status:** Done
**Priority:** High
**Category:** tooling
`skills/tooling/latex-workflow.md`: Overleaf vs local setup, BibTeX vs biber, key packages for academic writing (biblatex, hyperref, amsmath, algorithm2e), figure handling, submission to arXiv.

### 28. Preprint Strategy Node
**Status:** Done
**Priority:** Medium
**Category:** tooling
`skills/tooling/preprints.md`: When to post a preprint (before/after submission), which server (arXiv, SSRN, bioRxiv, EarthArXiv, SSOAR), embargo policies, journal double-submission rules, DOI and version management.

### 29. Zotero / Reference Manager Integration
**Status:** Done
**Priority:** Medium
**Category:** tooling
`skills/tooling/reference-managers.md`: Export BibTeX/RIS from TezAtlas reading report format, Zotero connector, Mendeley import, shared library for collaborative projects.

### 30. Statistical Analysis Tools Node
**Status:** Done
**Priority:** Medium
**Category:** tooling
`skills/tooling/statistics.md`: R vs Python (statsmodels, scipy) for academic stats, APA style statistical reporting format (t(df) = X, p = .XX, d = .XX), power analysis (G*Power), effect size reporting conventions.

---

## UX & Workflow

### 31. Iron Rule 1 Adaptation for Deadline Pressure
**Status:** Done
**Priority:** High
**Category:** core
For conference papers on tight deadlines: allow initial drafting from memory/notes, but flag every unsourced claim with [SOURCE NEEDED]. Gate: finalization phase cannot begin if any [SOURCE NEEDED] flags remain. Spirit preserved, deadline reality respected.

### 32. Co-authorship Workflow
**Status:** Done
**Priority:** Medium
**Category:** ux
Multi-author use case: shared `READING_REPORT.md`, conflict resolution for overlapping source notes, authorship contribution log (CRediT taxonomy), review assignment per section.

### 33. Session Continuity Across Long Projects
**Status:** Done
**Priority:** High
**Category:** ux
For projects spanning months: `STATUS.md` auto-generated at session end summarizing current phase, next 3 actions, open questions, and blockers. `/resume` command reads STATUS.md and reconstructs context. Addresses the context loss problem for long thesis projects.

### 34. Academic Writing Style Checker
**Status:** Done
**Priority:** Medium
**Category:** ux
Passive voice detector, over-hedging detector ("it might perhaps possibly..."), over-claiming detector ("this definitively proves..."), discipline-appropriate register checker. Runs as a Phase 6/7 quality gate, not during drafting.

### 35. Knowledge Gap Visualizer
**Status:** Done
**Priority:** Medium
**Category:** ux
After reading saturation: visual map of which RQs/argument nodes have strong evidence, which are thin, which have only one source. Forces researcher to see the gaps before writing. Generates a prioritized reading queue for gaps.

---

## Risk Mitigation (from Gemini analysis)

### 36. Anti-Hallucination Protocol for Methodology Advice
**Status:** Done
**Priority:** Critical
**Category:** core
Methodology advice (statistical tests, IRB requirements, reporting standards) must cite specific, verifiable sources — not rely on LLM memory. Add Iron Rule variant: "No methodology advice without source" parallel to Iron Rule 1.

### 37. Algorithmic Bias Audit Framework
**Status:** Done
**Priority:** Medium
**Category:** core
Periodic review of which methodologies/institutions/paradigms TezAtlas over-recommends. User feedback loop. Explicit note that non-Western, indigenous, and alternative epistemologies are valid.

### 38. Data Privacy Architecture
**Status:** Done
**Priority:** High
**Category:** architecture
All pre-publication data stays local (never sent to cloud unless user explicitly opts in). `.gitignore` by default excludes all data files. GDPR-compliant session logs. Clear data ownership statement: researcher owns all content, TezAtlas generates only the workflow scaffolding.

---

## Research-Backed Features (Evidence Base: 2026-02-22)

*These proposals are grounded in academic research on doctoral education, writing psychology, and SRL theory. See RESEARCH_BACKING.md for full citations.*

### 39. Daily Writing Scheduler — Silvia/Boice Module
**Status:** Done
**Priority:** High
**Category:** ux
Schedule specific daily writing blocks (Silvia 2007: "treat writing time as an appointment"). Recurring session reminder, streak tracker (Boice: daily > binge), weekly consistency summary. Language: celebrate showing up, not just output.

### 40. SRL Session Ritual — Forethought/Performance/Reflection
**Status:** Done
**Priority:** High
**Category:** ux
Based on Zimmerman's SRL cycle (2002). Before session: micro-goal prompt ("Today I will write [X]"). During session: timer + word counter. After session: 2-question reflection ("What worked? What would you change?"). Attribution framing: controllable causes (strategy, planning) not fixed (ability).

### 41. Advisor Checkpoint Template — Supervision Research
**Status:** Done (tpl-advisor-checkpoint.md created)
**Priority:** High
**Category:** core
Structured 7-section template based on Wisker (2005) and Lee (2008) supervision research. Captures: progress, work for review, specific feedback requests, advisor responses, goals, wellbeing check-in, action items. Replaces vague "meet your advisor" instruction.

### 42. Anxiety-Aware Language Design System
**Status:** Done
**Priority:** Critical
**Category:** ux
Writing anxiety affects 41% of graduate students (Daly & Miller 1975). TezAtlas language audit: (a) no shame-based messages ("you're behind"), (b) process goals not outcome goals, (c) scaffold features for blank-page fear (sentence starters, paragraph templates), (d) progress visualization shows gains not deficits, (e) "ugly first draft" mode disables all formatting/editing suggestions during initial drafting.

### 43. Knowledge-Transforming Prompts (Bereiter & Scardamalia Module)
**Status:** Done
**Priority:** Medium
**Category:** ux
Before each paragraph/section in Phase 6: "What does this argument DO for your reader? How does it advance your thesis?" Pushes writers from knowledge-telling (novice: dump what I know) to knowledge-transforming (expert: writing changes my thinking). Based on Bereiter & Scardamalia (1987).

### 44. Risk Signal Detection — Attrition Prevention
**Status:** Done
**Priority:** High
**Category:** architecture
Based on Lovitts (2001): 40-50% PhD attrition linked to isolation, loss of self-efficacy, supervisor breakdown. TezAtlas detects: (a) >2 weeks session inactivity, (b) 3+ consecutive missed goals, (c) no advisor checkpoint in >6 weeks. Gentle check-in ("It looks like you haven't written in a while — is everything okay?"). NOT punitive — opens support conversation.

### 45. Binge-Writing Prevention System
**Status:** Done
**Priority:** Medium
**Category:** ux
Boice (1990): binge writing = lower output, higher anxiety, reinforced avoidance. TezAtlas warning if user attempts very long single session (>4 hours): "Long sessions often reduce quality and increase burnout. Consider splitting into two sessions." Alternatively: celebrate when user writes 5 days in a row (streak > consistency > single marathon).

### 46. Motivational Regulation Prompts — Pintrich Module
**Status:** Done
**Priority:** Medium
**Category:** ux
Pintrich (2000): doctoral writing requires sustained intrinsic motivation across years. At each phase gate: "In one sentence — why does this research matter to you?" Answer is stored and shown back during low-motivation periods. Connects task completion to personal value and broader significance.

### 47. Implementation Intention Builder — Pre-Session
**Status:** Done
**Priority:** Medium
**Category:** ux
Gollwitzer & Sheeran (2006): "If-Then" planning significantly reduces procrastination. TezAtlas session start: "Complete this sentence: If it is [time] on [day], then I will open [file] and write [specific task] for [duration]." Research shows implementation intentions are 2-3x more effective than general intentions ("I'll write tomorrow").

### 48. Writing Environment Profile — Sword-Inspired Onboarding
**Status:** Done
**Priority:** Low
**Category:** ux
Sword (2017): productive academics design personal writing environments — no universal best time/place. TezAtlas onboarding adds: "When do you write best? (Morning/Afternoon/Evening/Night), Where? (Home/Office/Café/Anywhere), Preferred session length? (15min/30min/60min/90min+)". Generates a "Writing Environment Profile" used to personalize session reminders and goal suggestions.

---

## Two Operating Modes (Gemini Analysis 2026-02-22)

*See full analysis in git history. Core decision: TezAtlas defaults to Workflow Assistant; Copilot features available with guardrails.*

### 49. Dual Operating Mode — Workflow Assistant / Research Copilot
**Status:** Done
**Priority:** Critical
**Category:** architecture
TezAtlas operates on a spectrum: **Workflow Assistant** (default — user writes, AI guides and checks) vs **Research Copilot** (AI generates drafts, user reviews and owns). Default is Workflow Assistant for all academic output — aligned with Zimmerman SRL and academic integrity. Copilot mode available with explicit toggle and integrity warning. Key distinction by task: core intellectual work (argument synthesis, drafting) → Workflow Assistant always. Utility tasks (reformatting, grammar, single-paper summary) → Copilot available. Student Mode defaults stricter than Researcher Mode.

### 50. Collaborative Research Workspace
**Status:** Done
**Priority:** High
**Category:** architecture
**Difficulty:** Hard | **Impact:** High
Multi-author and co-PI support: role-based permissions (PI, co-author, reviewer, editor), paragraph-level contribution tracking, AI "Conflict Resolver" (flags when two authors cite same source with different conclusions), shared Research Note Pool with cross-contributor synthesis preserving individual attribution. Critical for co-authored articles, grant proposals, collaborative book chapters.

### 51. Adaptive Output Transformer
**Status:** Done
**Priority:** High
**Category:** architecture
**Difficulty:** Medium | **Impact:** High
Once a core project (thesis/article) is advanced: generate derivative outputs from the same research base. Target: press release, policy brief, blog post, conference abstract, executive summary. AI restructures/reformats for new audience — never fabricates new claims, only transforms. Every AI-transformed section clearly flagged for user review. Constraint: output diversity without intellectual compromise.

### 52. Provenance & Reasoning Layer (AI Transparency)
**Status:** Done
**Priority:** Critical
**Category:** architecture
**Difficulty:** Medium | **Impact:** High
Every AI suggestion carries a reasoning log: "This suggestion is based on [source X, page Y]. My reasoning: [brief explanation]." Hallucination Risk Score (Low/Medium/High) attached to AI outputs based on source availability, claim specificity, model confidence. Directly operationalizes Iron Rule 4 (no fabricated citations) for AI's own outputs. Makes AI intellectual contribution legible, auditable, trustworthy.

### 53. Research Career Graph — Longitudinal Tracking
**Status:** Done
**Priority:** Medium
**Category:** architecture
**Difficulty:** Hard | **Impact:** High
Track researcher activity across projects and years: methodologies used, publication trajectory, skill gaps ("you've never written a systematic review"), recurring themes, writing quality evolution. AI offers increasingly personalized guidance based on career history. Transforms TezAtlas from a project tool into a career-long research partner.

### 54. TezAtlas Exchange — Community Ecosystem
**Status:** Done
**Priority:** Medium
**Category:** architecture
**Difficulty:** Hard | **Impact:** High (long-term)
Community marketplace for discipline-specific workflow packs, phase templates, prompt libraries, custom skill nodes. Researchers/institutions publish validated templates (e.g., "Systematic Review for Clinical Trials", "Humanities Thesis for Turkish Universities") under Creative Commons. AI-assisted curation for quality. Direct import into core system. Network effect: community extends discipline coverage beyond core team's capacity.

### 55. Phase 3 Reading — Copilot vs Assistant Distinction
**Status:** Done
**Priority:** High
**Category:** phase
Workflow Assistant mode: guided annotation prompts, user-written summaries with AI accuracy check, concept mapping with user input, question prompts ("What is the author's primary RQ?"). Copilot mode: automated synthesis across multiple papers, proactive gap identification, "Read & Report" (user assigns docs + question → AI returns structured briefing). Both modes: Iron Rules apply, no unsourced claims.

### 56. Phase 6 Writing — Copilot vs Assistant Distinction
**Status:** Done
**Priority:** High
**Category:** phase
Workflow Assistant: structural scaffolding, paragraph-level feedback (coherence, evidence integration), logical gap detection, citation prompts, voice preservation. Copilot: outline-to-draft generation (marked as AI-generated, all sources cited), argument generation from notes, 3-alternative rephrasing with explanations. Both modes: user must review, own, and substantially engage with all content.

### 57. Student Mode vs Researcher Mode
**Status:** Done
**Priority:** High
**Category:** ux
Student Mode (default for thesis/research-proposal): Copilot features restricted, Workflow Assistant enforced, SRL session ritual mandatory, advisor checkpoints strictly gated. Researcher Mode (default for article/grant/report): Copilot features unlocked, session ritual optional, peer review cycle enabled. User selects at onboarding; can switch with explanation. Rationale: same tool, different learning scaffolding based on career stage.

### 58. Productive Struggle Preservation
**Status:** Done
**Priority:** Medium
**Category:** core
Based on Bjork & Bjork "desirable difficulties" research and Vygotsky's Zone of Proximal Development. TezAtlas should NOT remove all friction — specifically: (a) AI never generates the core research argument, only challenges and questions it; (b) "Struggle detection" (user stuck for >20 min) triggers scaffolding prompts, not AI-generated solutions; (c) Writing quality scores are shown as trajectories (improving) not absolute grades. The goal: build researcher capability, not researcher dependency.

---

## Technical Infrastructure (Added 2026-02-27)

### 59. Dependency Management — requirements.txt / pyproject.toml
**Status:** Done
**Priority:** High
**Category:** tooling
No dependency management exists. OCR pipeline requires `pymupdf`, `pytesseract`, `pillow` but these are only mentioned in README and code comments. Add a `pyproject.toml` (or at minimum `requirements.txt`) so the project installs with a single `pip install -e .` command. Include optional dependency groups: `[ocr]` for Tesseract, `[dev]` for linting/testing.

### 60. CI/CD Pipeline — GitHub Actions
**Status:** Done
**Priority:** High
**Category:** tooling
No CI/CD exists. Add `.github/workflows/` with: (a) Markdown lint for all skill nodes, (b) YAML frontmatter validation (required fields per node type), (c) Wikilink integrity check — detect broken `[[link]]` references across ~100 skill nodes, (d) OCR pipeline unit tests, (e) Spell check for EN/TR content. This prevents silent breakage as the skill graph grows.

### 61. Test Suite
**Status:** Done
**Priority:** High
**Category:** tooling
Zero tests exist. Minimum viable test suite: (a) OCR pipeline functional tests (text-layer PDF, scanned PDF, batch mode), (b) Skill graph integrity — every `phase_gate_out` target file exists, every wikilink resolves, (c) Frontmatter schema validation — required fields present per `node_type`, (d) Phase chain continuity — no broken sequences in any document type path. Framework: `pytest` with fixtures for sample PDFs.

### 62. Pre-commit Hooks
**Status:** Done
**Priority:** Medium
**Category:** tooling
Iron Rule 6 mandates git commit after every session, but no pre-commit hooks enforce quality. Add hooks for: (a) Markdown formatting consistency, (b) Detect accidentally committed PDFs in `sources/` (gitignore bypass), (c) `STATUS.md` staleness check (warn if >7 days old), (d) Frontmatter schema validation on changed skill nodes. Use `pre-commit` framework for portability.

---

## Multi-Agent Architecture (Added 2026-02-27)

### 63. Multi-Agent Orchestration via Claude Code Task Tool
**Status:** Done
**Priority:** High
**Category:** architecture
TezAtlas runs in a single Claude session. Leverage Claude Code's Task tool for parallel sub-agents: (a) **Source Hunter Agent** — background source search/download while user writes, (b) **Methodology Checker Agent** — validates methodological consistency per paragraph, (c) **Citation Verifier Agent** — cross-checks references against actual PDF content in `/sources/`. Keeps single-session simplicity while adding parallelism. No external infrastructure needed.

### 64. MCP Server for Academic APIs
**Status:** Done
**Priority:** High
**Category:** tooling
Build a TezAtlas-specific MCP server providing: (a) Semantic Scholar API — paper search, citation graph, author lookup, (b) OpenAlex API — open access metadata, institution data, (c) CrossRef API — DOI resolution, BibTeX generation, (d) Zotero/Mendeley API — library sync, (e) ORCID API — researcher profile. Replaces manual database access described in `skills/tooling/database-access.md` with live tool calls.

---

## Source Management & Discovery (Added 2026-02-27)

### 65. Automatic BibTeX/RIS Generation from PDFs
**Status:** Done
**Priority:** High
**Category:** tooling
OCR pipeline extracts text but not bibliographic metadata. Add a DOI detection layer: (a) regex scan for DOI patterns in first 2 pages, (b) CrossRef API lookup → structured BibTeX/RIS, (c) fallback: extract title + authors via heuristics → fuzzy match against CrossRef/OpenAlex. Output: auto-generated `.bib` file per source. Eliminates manual citation entry — the #1 time sink in source management.

### 66. Multilingual Source Management
**Status:** Done
**Priority:** Medium
**Category:** core
Turkish thesis writers commonly use English, German, and French sources. Add: (a) original-language quote preservation alongside translations, (b) bilingual citation format (original + translated title per many Turkish university requirements), (c) language tag per source in `READING_REPORT.md`, (d) automatic detection of source language via OCR pipeline metadata. Prevents the common error of untranslated or mistranslated quotations.

---

## User Experience Enhancements (Added 2026-02-27)

### 67. Progress Dashboard — DASHBOARD.md
**Status:** Done
**Priority:** High
**Category:** ux
Auto-generated at session end alongside `STATUS.md`. Visual format:
```
Phase: 3/8 ████████░░░░░░░░ 37%
Sources: 24 read / 31 total
Saturation: 78% (2 more needed)
Days active: 34 | Sessions: 18
Next milestone: Advisor checkpoint (Phase 4 gate)
```
Addresses motivation through visible progress. Based on goal-gradient hypothesis (Hull 1932): effort increases as the goal gets closer.

### 68. `/status` Slash Command
**Status:** Done
**Priority:** High
**Category:** ux
Quick status query without full `/tezatlas` initialization. Reads `STATUS.md` + `READING_REPORT.md` + `MEMORY.md` and outputs a 5-line summary: current phase, completion percentage, unread sources, next action, days since last session. No state changes, no SRL ritual — pure read-only status check.

### 69. Template Scaffolding Command
**Status:** Done
**Priority:** Medium
**Category:** ux
One-command project bootstrap: `/tezatlas new article --lang tr --field law` creates the full file structure: `STATUS.md`, `READING_REPORT.md`, `MEMORY.md`, `sources/`, `notes/`, discipline-specific templates, pre-configured `.gitignore`. Currently onboarding is conversational (5 questions) — this adds a fast-path for experienced users who already know their parameters.

---

## Academic Quality & Integration (Added 2026-02-27)

### 70. Deep Comparative Analysis Mode — Phase 3
**Status:** Done
**Priority:** High
**Category:** phase
Leverage Claude's 200K context window for bulk source analysis in Phase 3: (a) load 5+ source notes simultaneously, (b) cross-source theme extraction, (c) contradiction detection (Source A claims X, Source B claims ¬X — with page references), (d) common methodology pattern identification, (e) evidence strength matrix (which claims have multiple independent sources). Inspired by Gemini Deep Research's multi-document reasoning capability. Output: `COMPARATIVE_ANALYSIS.md`.

### 71. University Format Templates — YÖK Compliance
**Status:** Done
**Priority:** High
**Category:** discipline
`MOC-universities.md` exists but has no content. Populate with: (a) YÖK tez yazım kılavuzu format rules (margins, fonts, spacing, page numbering), (b) university-specific templates (İstanbul, Ankara, ODTÜ, Boğaziçi, Hacettepe — top 5 first), (c) cover page, jury approval page, ethics declaration page generators, (d) Turkish abstract (özet) + English abstract formatting rules. Critical for Turkish users — format rejection is a common submission failure.

### 72. Academic Writing Style Linter — Real-time
**Status:** Done
**Priority:** Medium
**Category:** ux
Upgrade proposal #34 (style checker at phase gate) to real-time inline feedback during Phase 6 writing: (a) passive voice density, (b) hedge word frequency ("perhaps", "might", "possibly"), (c) overclaiming detection ("definitively proves", "clearly demonstrates"), (d) sentence length variance, (e) discipline-appropriate register. Inspired by Writefull/Trinka but integrated into TezAtlas workflow without external dependency.

---

## Distribution & Community (Added 2026-02-27)

### 73. Docker / Devcontainer Support
**Status:** Done
**Priority:** Medium
**Category:** tooling
Single-command reproducible environment. `.devcontainer/devcontainer.json` for VS Code / GitHub Codespaces. Dockerfile: Python 3.11+, PyMuPDF, Tesseract with `tur+eng` language packs, figlet + lolcat for banner, Claude Code CLI. Eliminates "works on my machine" onboarding friction, especially for users on Windows or university-managed machines.

### 74. tezatlas.com — BYOK Web Version Roadmap
**Status:** Done
**Priority:** Medium
**Category:** architecture
README mentions tezatlas.com but no implementation exists. Phased roadmap: Phase 1 — static documentation site (Astro/Next.js, skill graph visualization, interactive demo). Phase 2 — BYOK (Bring Your Own Key) Claude API integration, session persistence via localStorage or Supabase. Phase 3 — collaborative features, institutional licensing. Phase 4 — TezAtlas Exchange marketplace (see proposal #54).

### 75. Plugin / Extension System
**Status:** Done
**Priority:** Medium
**Category:** architecture
`skills/` folder is modular but has no formal plugin API. Formalize: (a) standard frontmatter schema with required/optional fields per `node_type`, (b) `tezatlas-plugin.json` manifest for third-party skill packs, (c) validator script (`python validate_plugin.py <path>`), (d) install command (`tezatlas install <plugin-name>` or simple git clone into `skills/community/`), (e) namespace isolation to prevent conflicts with core nodes. Enables community contributions without core maintainer bottleneck.

---

## Competitive Gap Closures (Added 2026-02-27)

### 76. Citation Graph Discovery — ResearchRabbit Equivalent
**Status:** Done
**Priority:** High
**Category:** tooling
ResearchRabbit and Connected Papers offer visual citation graph exploration — TezAtlas has no equivalent. Add: (a) given a seed paper DOI, fetch citing/cited papers via Semantic Scholar API, (b) score relevance to current research questions, (c) add high-relevance papers to deferred source pool, (d) integrate with snowball sampling protocol (`skills/techniques/snowball-sampling.md`). Automates the most time-consuming part of literature discovery.

### 77. Evidence Synthesis Engine — Elicit/Consensus Equivalent
**Status:** Done
**Priority:** Medium
**Category:** architecture
Elicit and Consensus offer automated evidence synthesis across papers. TezAtlas equivalent: (a) extract claim-evidence pairs from reading notes, (b) cluster by research question, (c) generate synthesis matrix (author × finding × method × conclusion), (d) flag consensus vs. disagreement areas, (e) output feeds directly into Phase 4 outline. Differentiator: TezAtlas version is source-anchored (Iron Rule 1) — every synthesis point traces to a local PDF, not LLM memory.
