---
title: "Phase 2 — PRISMA Screening"
title_tr: "Aşama 2 — PRISMA Taraması"
node_type: phase
phase_number: 2
document_type: lit-review
phase_gate_in: "phase-1-search.md"
phase_gate_out: "phase-3-extraction.md"
description: "Two-stage screening: title/abstract screening followed by full-text review of passing records. Every exclusion at Stage 2 must be documented with a reason. PRISMA flow diagram is updated with counts at each decision point."
description_tr: "İki aşamalı tarama: başlık/özet taraması, ardından geçen kayıtların tam metin incelemesi. Aşama 2'deki her dışlama gerekçeyle belgelenmelidir. PRISMA akış diyagramı her karar noktasındaki sayılarla güncellenir."
tags: [phase, lit-review, screening, PRISMA, inclusion, exclusion]
outputs:
  - "screening_decisions.md"
  - "PRISMA_diagram.md"
links_to:
  - skills/core/iron-rules.md
  - skills/phases/lit-review/phase-1-search.md
language: bilingual
version: "1.0"
---

# Phase 2 — PRISMA Screening
# Aşama 2 — PRISMA Taraması

## Gate Rule / Geçiş Kuralı

**EN:** Screening criteria are fixed from Phase 0. Do not invent new exclusion reasons mid-screening. If a new pattern appears, document it and apply it consistently from that point forward, noting the change.

**TR:** Tarama kriterleri Aşama 0'dan sabittir. Tarama ortasında yeni dışlama gerekçeleri icat etmeyin. Yeni bir örüntü ortaya çıkarsa, bunu belgeleyin ve bu noktadan itibaren tutarlı biçimde uygulayın, değişikliği not edin.

---

## 1. Stage 1 — Title & Abstract Screening / Aşama 1 — Başlık ve Özet Taraması

**EN:** Screen every record in deduplicated_results.csv against the inclusion/exclusion criteria using only the title and abstract. Apply a liberal inclusion threshold at this stage — when in doubt, include. The goal is to avoid false negatives; false positives are caught in Stage 2.

**TR:** deduplicated_results.csv'deki her kaydı yalnızca başlık ve özeti kullanarak dahil etme/dışlama kriterlerine göre tarayın. Bu aşamada liberal bir dahil etme eşiği uygulayın — şüphe durumunda dahil edin. Amaç yanlış negatifleri önlemektir; yanlış pozitifler Aşama 2'de yakalanır.

**Decision rule / Karar kuralı:**
- INCLUDE / DAHİL ET — clearly meets criteria or unclear
- EXCLUDE / DIŞLA — clearly does not meet criteria (state which criterion)

```
Stage 1 result / Aşama 1 sonucu:
Records screened / Taranan kayıtlar: N = ___
Excluded at Stage 1 / Aşama 1'de dışlanan: N = ___
Proceeding to full-text / Tam metne geçen: N = ___
```

---

## 2. Stage 2 — Full-Text Screening / Aşama 2 — Tam Metin Taraması

**EN:** Obtain the full text of every record that passed Stage 1. Screen each against all inclusion/exclusion criteria. For every excluded record, record the specific exclusion reason. Multiple reasons are possible; record the primary reason.

**TR:** Aşama 1'i geçen her kaydın tam metnini edinin. Her birini tüm dahil etme/dışlama kriterlerine göre tarayın. Dışlanan her kayıt için belirli dışlama gerekçesini kaydedin. Birden fazla gerekçe mümkündür; birincil gerekçeyi kaydedin.

**Standard exclusion reason codes / Standart dışlama gerekçe kodları:**
- `WRONG_POP` — wrong population/sample
- `WRONG_INT` — wrong intervention/phenomenon
- `WRONG_OUT` — wrong outcome/measure
- `WRONG_DESIGN` — study design not eligible
- `WRONG_DATE` — outside date range
- `WRONG_LANG` — language not eligible
- `NO_FULL_TEXT` — full text not retrievable
- `DUPLICATE` — duplicate identified at full-text stage
- `LOW_QUALITY` — below quality threshold

---

## 3. Screening Decisions Log / Tarama Kararları Günlüğü

**EN:** Record every Stage 2 decision. This becomes screening_decisions.md.

**TR:** Her Aşama 2 kararını kaydedin. Bu, screening_decisions.md olur.

```markdown
## Stage 2 Screening Decisions

| ID | Authors | Year | Title | Decision | Exclusion Reason |
|----|---------|------|-------|----------|-----------------|
| 001 | | | | INCLUDE | — |
| 002 | | | | EXCLUDE | WRONG_DESIGN |
```

```
Stage 2 result / Aşama 2 sonucu:
Full texts assessed / Değerlendirilen tam metinler: N = ___
Excluded (with reasons) / Dışlanan (gerekçeli): N = ___
Included in review / İncelemeye dahil edilen: N = ___
```

---

## 4. PRISMA Diagram — Updated / PRISMA Diyagramı — Güncellenmiş

**EN:** Fill in all counts from Phases 1 and 2. This becomes PRISMA_diagram.md.

**TR:** Aşama 1 ve 2'deki tüm sayıları doldurun. Bu, PRISMA_diagram.md olur.

```
Identification / Tanımlama:
  Records from databases / Veritabanlarından kayıtlar: N = ___
  Duplicates removed / Kaldırılan kopyalar: N = ___

Screening / Tarama:
  Records screened / Taranan kayıtlar: N = ___
  Records excluded (title/abstract) / Dışlanan (başlık/özet): N = ___

Eligibility / Uygunluk:
  Full texts assessed / Değerlendirilen tam metinler: N = ___
  Full texts excluded / Dışlanan tam metinler: N = ___
    WRONG_DESIGN: N = ___
    WRONG_POP: N = ___
    [other reasons / diğer gerekçeler]: N = ___

Included / Dahil edilen:
  Studies included in review / İncelemeye dahil edilen çalışmalar: N = ___
```

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] All records screened at Stage 1 / Tüm kayıtlar Aşama 1'de tarandı
- [ ] All Stage 1 passes retrieved as full text / Aşama 1'i geçenlerin tamamı tam metin olarak alındı
- [ ] Every Stage 2 exclusion has a documented reason / Her Aşama 2 dışlamasının belgelenmiş gerekçesi var
- [ ] screening_decisions.md completed / screening_decisions.md tamamlandı
- [ ] PRISMA_diagram.md updated with final counts / PRISMA_diagram.md nihai sayılarla güncellendi

**Gate in:** phase-1-search.md
**Gate out:** → phase-3-extraction.md
