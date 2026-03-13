---
title: "Phase 1 — Methodology & Reproducibility"
title_tr: "Faz 1 — Metodoloji ve Tekrarlanabilirlik"
node_type: phase
phase_number: 1
document_type: technical-report
phase_gate_in: "phase-0-hypothesis.md"
phase_gate_out: "phase-2-results.md"
description: "Document the experimental setup, materials, software environments, and procedures with enough detail that an independent researcher can exactly reproduce the results."
description_tr: "Deneysel kurulumu, malzemeleri, yazılım ortamlarını ve prosedürleri, bağımsız bir araştırmacının sonuçları tam olarak tekrarlayabileceği yeterli ayrıntıyla belgeleyin."
tags: [phase, technical-report, methodology, reproducibility, materials]
outputs:
  - "methods_section.md"
links_to:
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Phase 1 — Methodology & Reproducibility / Faz 1 — Metodoloji ve Tekrarlanabilirlik

## Purpose / Amaç

**EN:** The core of a technical report is reproducibility. If another engineer or scientist cannot read your methods and perfectly replicate your setup, the report is invalid.

**TR:** Teknik bir raporun özü tekrarlanabilirliktir. Başka bir mühendis veya bilim insanı yöntemlerinizi okuyup kurulumunuzu mükemmel bir şekilde kopyalayamazsa, rapor geçersizdir.

---

## Steps / Adımlar

**1. Hardware / Materials / Donanım / Malzemeler**
- List all physical components, instruments, and materials used.
- Include exact model numbers, manufacturers, and calibration status where relevant.

**2. Software & Environment / Yazılım ve Ortam**
- For computational work, list OS, language version (e.g., Python 3.10), library versions (e.g., pandas 2.0.1, PyTorch 2.1), and random seeds.
- Mention Docker containers, conda environments, or GitHub repositories if applicable.

**3. Procedure / Prosedür**
- Write the step-by-step process used to collect data.
- Detail data cleaning steps: how were outliers handled? Were any data points excluded, and why?

---

## Output Template / Çıktı Şablonu

### methods_section.md
```markdown
# Methods and Materials

## Experimental Setup / Equipment
- [Item 1, Model X, Manufacturer]
- [Item 2, Purity %, Supplier]

## Computational Environment
- OS: [...]
- Core Libraries: [...]
- Random Seed: [...]

## Procedure
1. [...]
2. [...]
3. [...]

## Data Processing
[Explanation of how raw data was filtered and cleaned]
```

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] All hardware and software versions are strictly documented.
- [ ] The data cleaning protocol is explicitly stated.
- [ ] `methods_section.md` is complete and clear.
