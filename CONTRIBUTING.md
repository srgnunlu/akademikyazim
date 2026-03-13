# Contributing to TezAtlas

TezAtlas is built as a graph of markdown skill nodes. Contributing does not require deep technical knowledge — only familiarity with how academic workflows work in your field.

## Quick Start

```bash
git clone https://github.com/tialkan/TezAtlas.git
cd TezAtlas
pip install pyyaml pre-commit
pre-commit install
```

---

## Node Types

Every `.md` file in `skills/` must declare a `node_type` in its YAML frontmatter.

| node_type | Where | Description |
|-----------|-------|-------------|
| `core` | `skills/core/` | Workflow-wide rules and principles (Iron Rules, session structure, modes) |
| `phase` | `skills/phases/<type>/` | A numbered step in a document workflow (Phase 0, Phase 1, …) |
| `phase-fork` | `skills/phases/<type>/` | An optional branching path from a phase (e.g. methodology fork). Does NOT get included in phase chain tests. |
| `technique` | `skills/techniques/` | A reusable academic skill (snowball sampling, citation formatting, etc.) |
| `template` | `skills/templates/` | A fill-in template loaded into session context (notes, outlines, etc.) |
| `tooling` | `skills/tooling/` | Documentation for external tools (LaTeX, Docker, statistics software) |
| `foundation` | `skills/disciplines/` | Discipline-specific rules (law, medicine, STEM, humanities) |
| `moc` | `skills/moc/` | Map-of-Content index nodes |

---

## Frontmatter Schema

Every node must have valid frontmatter. The pre-commit hook (`scripts/check_frontmatter.py`) validates this automatically.

```yaml
---
title: "Human-readable title"
title_tr: "Türkçe başlık"          # optional but encouraged
node_type: technique                # see table above
description: "One sentence describing what this node does"
description_tr: "Türkçe açıklama" # optional
tags: [reading, saturation, methodology]
links_to:                           # paths relative to repo root
  - skills/techniques/snowball-sampling.md
  - skills/templates/tpl-notes.md
language: bilingual                 # bilingual | en | tr
version: "1.0"
---
```

**Additional fields for `phase` nodes:**

```yaml
node_type: phase
phase_number: 3
document_type: thesis               # thesis | article | conference | lit-review | ...
gate_in: "phase-2-contribution-claim.md"
gate_out: "phase-4-outline.md"
```

**`phase-fork` nodes** do NOT need `gate_in` / `gate_out` or `phase_number` — they are optional branches, not part of the linear chain.

---

## Validation

Before committing, run:

```bash
# Validate a single node
python3 scripts/check_frontmatter.py skills/techniques/your-node.md

# Validate all nodes (what pre-commit runs)
python3 scripts/check_frontmatter.py skills/

# Run the full test suite
python3 -m pytest tests/ -v
```

The pre-commit hook runs automatically on every `git commit`. Fix all errors before submitting a PR.

---

## Adding a New Technique Node

1. Create `skills/techniques/your-technique.md`
2. Fill in frontmatter (title, description, tags, links_to, language, version)
3. Write ~80 lines of focused content — bilingual (EN + TR) preferred
4. Run `python3 scripts/check_frontmatter.py skills/techniques/your-technique.md`
5. Add to relevant `skills/moc/MOC-*.md`
6. Submit PR

---

## Adding a New Phase Fork

Phase forks are optional methodological branches (e.g. "quantitative vs qualitative" within Phase 3).

```yaml
---
title: "Your Fork Title"
node_type: phase-fork               # NOT phase — this excludes it from chain tests
description: "When this fork activates and what it does"
tags: [methodology, quantitative]
language: bilingual
version: "1.0"
---
```

Place the file in `skills/phases/<doctype>/phase-N-something-fork.md`.

---

## Adding a Discipline Module

Discipline modules live in `skills/disciplines/`. Use `node_type: foundation`.

Required sections:
- **Citation Formats**: primary citation styles for the discipline
- **Key Databases**: where to find sources
- **Methodological Conventions**: what counts as valid evidence
- **Language-Specific Notes**: TR/DE/FR equivalents where relevant
- **Iron Rule Adaptations**: any discipline-specific applications of the 9 rules

---

## Adding a Plugin

For larger contributions (multiple nodes for a niche field), use the plugin system:

1. Create a directory with:
   - `tezatlas-plugin.json` manifest
   - Your node `.md` files
   - `README.md` (recommended)
   - `LICENSE` file
2. Validate: `python3 scripts/validate_plugin.py path/to/plugin/`
3. Install locally: `python3 scripts/install_plugin.py path/to/plugin/`
4. Submit as a PR or publish to TezAtlas Exchange (CC BY 4.0 recommended)

See `skills/core/plugin-system.md` for the manifest schema.

---

## The One Hard Constraint

**No contribution may instruct TezAtlas to generate unsourced content, skip a phase gate, or fabricate a citation.**

All 9 Iron Rules must be respected by every node. A PR that introduces a mechanism for bypassing any Iron Rule will not be merged — regardless of how well-written the node is.

---

## Commit Style

```
feat: add technique node for grounded theory analysis
fix: correct phase_number in conference phase-3
docs: update RESEARCH_BACKING.md with Pintrich citation
```

---

## Where Contributions Are Most Needed

- Discipline modules: Engineering sub-disciplines, Economics, Education
- Language support: Arabic, Chinese, Portuguese, Italian, Japanese
- Technique nodes: meta-analysis, discourse analysis, computational methods
- Template nodes: policy brief, working paper, systematic review protocol
- Community plugins: field-specific skill packs

Questions? Open an issue or start a Discussion on GitHub.
