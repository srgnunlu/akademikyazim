---
title: "Phase 2 — Methodology & Work Plan"
title_tr: "Faz 2 — Metodoloji ve Çalışma Planı"
node_type: phase
phase_number: 2
document_type: grant-proposal
phase_gate_in: "phase-1-research-case.md"
phase_gate_out: "phase-3-budget.md"
description: "Design the research methodology, structure work packages with deliverables, assess risks, and plan ethical compliance. Funders scrutinize this section most."
description_tr: "Araştırma metodolojisini tasarla, çıktılarla birlikte çalışma paketlerini yapılandır, riskleri değerlendir ve etik uyumu planla. Fon kaynakları bu bölümü en çok inceler."
tags: [phase, grant-proposal, methodology, work-plan, risk, ethics]
outputs:
  - "methodology.md"
  - "gantt_chart.md"
  - "risk_register.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 2 — Methodology & Work Plan
# Faz 2 — Metodoloji ve Çalışma Planı

## Gate Rule / Geçiş Kuralı

**EN:** Do NOT proceed to Phase 3 until every work package has at least one measurable deliverable with a completion date. Vague deliverables ("draft report") are insufficient — specify what the deliverable demonstrates.

**TR:** Her çalışma paketinin tamamlanma tarihiyle birlikte en az bir ölçülebilir çıktısı olana kadar Faz 3'e geçme. Belirsiz çıktılar ("taslak rapor") yetersizdir — çıktının neyi kanıtladığını belirt.

---

## Steps / Adımlar

**1. Research Design / Araştırma Tasarımı**
- State the overarching research design explicitly (experimental, observational, computational, mixed-methods, etc.)
- Justify the design choice: why is this design appropriate for your research questions?
- Describe methods at the level of detail a specialist reviewer can evaluate
- TR: Genel araştırma tasarımını açıkça ifade et. Tasarım seçimini gerekçelendir. Yöntemleri uzman bir hakimin değerleyebileceği düzeyde açıkla.

**2. Work Packages / Çalışma Paketleri**
Structure as: WP0 (management), WP1, WP2, ... WPn (dissemination)
For each WP:
```
WP[N]: [Title]
Lead: [PI / Co-PI / Postdoc name]
Duration: Month [X] – Month [Y]
Objectives: [1-3 objectives]
Tasks:
  T[N].1 [Task name] — [Description]
  T[N].2 ...
Deliverables:
  D[N].1 [Month X]: [Specific deliverable] — [What it demonstrates]
Milestones:
  M[N].1 [Month X]: [Go/no-go decision or review point]
```
- TR: Her WP için hedefler, görevler, teslim edilecekler ve kilometre taşları tanımla.

**3. Risk Analysis / Risk Analizi**
For each significant risk:
```
Risk: [Description]
Probability: High / Medium / Low
Impact: High / Medium / Low
Contingency: [Specific alternative approach]
```
Common risks to address: data access failure, key personnel departure, technical method failure, ethical approval delay
- TR: Her önemli risk için olasılık, etki ve alternatif yaklaşım tanımla.

**4. Resources / Kaynaklar**
- Personnel: list each role, FTE percentage, and duration
- Equipment: list major items (links to Phase 3 budget justification)
- Computational/data resources: servers, datasets, licenses
- TR: Personel, ekipman ve hesaplama/veri kaynaklarını listele. Faz 3 bütçe gerekçesine bağlan.

**5. Ethical Considerations / Etik Hususlar**
- IRB/ethics board approval: required? Status?
- Data management plan (DMP): storage, access, retention, deletion
- Open access policy: journal, dataset, code (many funders mandate this)
- Gender dimension: does your methodology account for sex/gender variables? (EU funders require this)
- TR: Etik kurul onayı, veri yönetim planı, açık erişim politikası ve cinsiyet boyutunu ele al.

---

## Gantt Chart Template / Gantt Şeması Şablonu

```
WP / Task          | M1 | M2 | M3 | ... | M24 |
-------------------|----|----|----| ... |-----|
WP1: [Title]       | ## | ## |    |     |     |
  T1.1             | ## | ## |    |     |     |
  T1.2             |    | ## | ## |     |     |
WP2: [Title]       |    |    | ## |     |     |
...
D = Deliverable ◆  |    |  ◆ |    |     |  ◆  |
M = Milestone ●    |  ● |    |    |     |  ●  |
```

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Research design justified (not just described)
- [ ] All WPs defined with objectives, tasks, deliverables, milestones
- [ ] Every deliverable is measurable and dated
- [ ] Gantt chart covers full project duration
- [ ] Risk register has at least 4 risks with contingencies
- [ ] Ethical compliance section complete (IRB status, DMP, open access)
- [ ] Resources section matches what will appear in the budget (Phase 3)
