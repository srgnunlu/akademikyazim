---
title: "Phase 0 — Hypothesis & Objective"
title_tr: "Faz 0 — Hipotez ve Amaç"
node_type: phase
phase_number: 0
document_type: technical-report
phase_gate_in: null
phase_gate_out: "phase-1-methods.md"
description: "Define the specific, measurable, and falsifiable hypothesis or engineering objective of the technical report."
description_tr: "Teknik raporun spesifik, ölçülebilir ve yanlışlanabilir hipotezini veya mühendislik hedefini tanımlayın."
tags: [phase, technical-report, hypothesis, objective, stem]
outputs:
  - "experiment_brief.md"
links_to:
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Phase 0 — Hypothesis & Objective / Faz 0 — Hipotez ve Amaç

## Purpose / Amaç

**EN:** A technical or lab report is strictly focused on empirical validation or engineering verification. This phase explicitly states the hypothesis being tested or the technical parameter being measured before detailing how it was done.

**TR:** Teknik veya laboratuvar raporu, kesinlikle ampirik doğrulamaya veya mühendislik doğrulamasına odaklanır. Bu faz, nasıl yapıldığını detaylandırmadan önce test edilen hipotezi veya ölçülen teknik parametreyi açıkça belirtir.

---

## Steps / Adımlar

**1. State the Hypothesis / Objective / Hipotezi veya Amacı Belirtin**
- **Science:** "We hypothesize that [X] causes [Y] because..."
- **Engineering:** "The objective is to verify if system [X] meets specification [Y] under conditions [Z]."

**2. Identify the Key Variables / Temel Değişkenleri Belirleyin**
- Independent Variables (what you changed/controlled)
- Dependent Variables (what you measured)
- Control Variables (what you kept constant)

**3. Define the Success/Failure Criteria / Başarı/Başarısızlık Kriterlerini Tanımlayın**
- What exact threshold of measurement confirms or refutes the hypothesis? (e.g., p < 0.05, latency < 10ms, yield > 95%).

---

## Output Template / Çıktı Şablonu

### experiment_brief.md
```markdown
# Experiment / Project Brief

**Hypothesis / Objective:** [...]

**Variables:**
- Independent: [...]
- Dependent: [...]
- Controls: [...]

**Success/Validation Criteria:** [...]
```

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Hypothesis is falsifiable and clear.
- [ ] Variables are correctly categorized.
- [ ] Success criteria are quantified.
- [ ] `experiment_brief.md` is saved.
