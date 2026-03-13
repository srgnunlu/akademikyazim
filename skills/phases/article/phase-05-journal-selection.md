---
title: "Phase 0.5 — Journal Selection"
title_tr: "Faz 0.5 — Dergi Seçimi"
node_type: phase
phase_number: 0.5
document_type: article
phase_gate_in: "phase-0-claim.md"
phase_gate_out: "phase-1-literature.md"
description: "A dedicated phase to evaluate target journals based on impact factor, scope fit, audience, open access policy, and acceptance rate before writing begins."
description_tr: "Yazmaya başlamadan önce hedef dergileri etki faktörü, kapsam uyumu, hedef kitle, açık erişim politikası ve kabul oranına göre değerlendirmeye ayrılmış faz."
tags: [phase, article, journal-selection, publication-strategy]
outputs:
  - "journal_target.md"
links_to:
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Phase 0.5 — Journal Selection / Faz 0.5 — Dergi Seçimi

## Purpose / Amaç

**EN:** Wrong journal selection wastes 6-12 months of revision cycles. This phase forces a strategic evaluation of publication venues before literature reading and writing begins, ensuring the manuscript is tailored to the correct audience and format from day one.

**TR:** Yanlış dergi seçimi 6-12 aylık revizyon döngülerinin israf edilmesine neden olur. Bu faz, literatür okuma ve yazma işlemlerine başlamadan önce yayın mecralarının stratejik bir değerlendirmesini zorunlu kılarak, makalenin ilk günden itibaren doğru kitleye ve formata göre uyarlanmasını sağlar.

---

## Steps / Adımlar

**1. Identify 3 Candidate Journals / 3 Aday Dergi Belirleyin**
- Start with the journals you cite most often in your claim statement.
- Ask senior colleagues for recommendations.
- Consider indexing requirements (e.g., SCI, SSCI, AHCI, TR Dizin).

**2. Evaluate Scope Fit / Kapsam Uyumunu Değerlendirin**
- Read the "Aims & Scope" section of each candidate carefully.
- Search each journal's recent issues for your specific keywords. If they haven't published anything similar in 3 years, it's a high-risk submission.

**3. Analyze Metrics and Logistics / Metrikleri ve Lojistiği Analiz Edin**
- **Time to first decision:** Crucial if you have graduation/promotion deadlines.
- **Acceptance rate:** Be realistic about your contribution's magnitude.
- **Open Access (OA) policy & APC (Article Processing Charge):** Do you have funding to pay for it?

**4. Final Selection / Nihai Seçim**

For each of the 3 candidate journals, present an evaluation matrix before asking the user to rank them:

```
Dergi Adı: [Journal Name]
> ✅ [Kapsam uyumu, etki faktörü, erişim avantajı]
> ⚠️ [Kabul oranı riski, APC yükü, bekleme süresi]
> ⭐ Kapsam uyumu: ★★★★☆ | Kabul şansı: ★★★☆☆ | Hız: ★★☆☆☆ | Prestij: ★★★★★
> Tavsiye: [Bu dergiye göndermek için en uygun koşul nedir?]
```

Üç adayın matrisi yan yana gösterildikten sonra kullanıcıdan A/B/C sıralaması iste.
Rank them as Target A (Primary), Target B (Backup 1), and Target C (Backup 2).

---

## Output Template / Çıktı Şablonu

### journal_target.md
```markdown
# Target Journal Strategy

## Target A: [Journal Name]
- Publisher / Index:
- Impact Factor / Quartile:
- Time to First Decision (avg):
- Word Count Limit:
- Reference Style:
- Rationale for Fit: "This is the primary target because..."

## Target B: [Journal Name]
[Details]

## Target C: [Journal Name]
[Details]
```

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] 3 candidate journals identified and evaluated.
- [ ] Primary target (Target A) selected based on realistic scope and timeline match.
- [ ] `journal_target.md` created and committed.
