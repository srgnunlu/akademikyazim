---
title: "Phase 4 — Proposal Writing"
title_tr: "Faz 4 — Teklif Yazımı"
node_type: phase
phase_number: 4
document_type: grant-proposal
phase_gate_in: "phase-3-budget.md"
phase_gate_out: "phase-5-review-submit.md"
description: "Write the proposal sections in the correct order, with Iron Rule source verification at each step. Every section must be self-contained and scannable."
description_tr: "Teklif bölümlerini doğru sırayla yaz; her adımda Demir Kural kaynak doğrulaması uygula. Her bölüm bağımsız ve taranabilir olmalıdır."
tags: [phase, grant-proposal, writing, structure, abstract]
outputs:
  - "proposal_draft.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/core/source-policy.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/natural-voice.md
  - skills/core/guided-writing-mode.md
language: bilingual
version: "1.0"
---

# Phase 4 — Proposal Writing
# Faz 4 — Teklif Yazımı

## Gate Rule / Geçiş Kuralı

**EN:** Do NOT proceed to Phase 5 until every section is written, every claim has a cited source (Iron Rule 1), and the total length is within ±10% of the page limit. Do NOT write the abstract until all other sections are complete.

**TR:** Her bölüm yazılana, her iddia kaynak içerene (Demir Kural 1) ve toplam uzunluk sayfa limitinin ±%10'u içinde olana kadar Faz 5'e geçme. Diğer tüm bölümler tamamlanana kadar özet yazma.

---

## Guided Writing Mode / Rehberli Yazım Modu

Bu fazda `skills/core/guided-writing-mode.md` protokolü aktiftir:
- Her bölüm/paragraf için A/B seçenekleri üretilir
- Her seçenek kaynak kanıtlarıyla desteklenir (📚)
- Akademik Yazım Notu yapıyı ve normu açıklar (📖)
- Kullanıcı seçer, birleştirir veya yeniden yönlendirir
- Demir Kural 1: Kaynak olmadan yazım YOK

In this phase, the `skills/core/guided-writing-mode.md` protocol is active:
- A/B draft options are generated for each section/paragraph
- Each option is backed by source evidence (📚)
- Academic Writing Note explains structure and norms (📖)
- User selects, merges, or redirects
- Iron Rule 1: No writing without source

---

## Writing Order / Yazım Sırası

Write sections in this order — NOT the order they appear in the final document:

```
1. Methodology     (you know this best — start here)
2. Impact          (flows from methodology outcomes)
3. Innovation      (articulate once you've written the "what")
4. Problem Statement + Literature (frame around your approach)
5. Budget Narrative (describe resources you already planned)
6. Abstract        (LAST — summarizes what you've written)
```

**TR:** Bölümleri bu sırayla yaz — nihai belgede göründükleri sırayla değil. Özeti en son yaz.

---

## Steps / Adımlar

**1. Draft Each Section / Her Bölümü Taslak Olarak Yaz**
- Write a complete draft without self-editing — get ideas down
- Use active voice: "We will analyze" not "Analysis will be conducted"
- Use direct language: no hedging unless scientifically required ("may" vs. "will")
- TR: Öz-eleştiri yapmadan tam taslak yaz. Aktif ses kullan. Dolaylı dilden kaçın.

**2. Source Verification After Each Section / Her Bölüm Sonrası Kaynak Doğrulaması**
Apply Iron Rule 1 section by section:
- Highlight every factual or interpretive claim
- Confirm each has a citation in /sources/
- Remove or rewrite any claim that cannot be sourced
- TR: Her bölümden sonra Demir Kural 1'i uygula. Kaynaksız kalan her iddiayı kaldır veya yeniden yaz.

**3. Alignment Check Against Funder Criteria / Fon Kaynağı Kriterleriyle Uyum Kontrolü**
Return to Phase 0 funder_profile.md:
- For each evaluation criterion: does your text explicitly address it?
- Weight your word count roughly proportional to criteria weights
  (if "impact" = 30% of score, it should get roughly 30% of your writing attention)
- TR: Faz 0'daki değerlendirme kriterlerine geri dön. Her kriter için metinde açık bir yanıt var mı?

**4. Page Limit Discipline / Sayfa Limiti Disiplini**
- If limit is 15 pages: target 14.5 pages
- NEVER exceed the limit (automatic disqualification at most funders)
- NEVER fall short by more than 10% (signals insufficient effort)
- Cut ruthlessly: if a sentence doesn't advance the argument, delete it
- TR: Limitin altında %10'dan fazla kalma, üstüne çıkma. Argümanı ilerletmeyen her cümleyi sil.

**5. Reviewer Readability / Hakem Okunabilirliği**
The reviewer is busy, reviewing many proposals, possibly not your exact specialist:
- Use clear section headers
- Use bold to mark key claims (innovation, impact, feasibility)
- Every section should be understandable without reading prior sections
- First sentence of each paragraph = the paragraph's main claim
- TR: Hakem meşgul ve muhtemelen tam uzmanlık alanında değil. Net başlıklar, kalın kilit iddialar, her bölüm bağımsız okunabilir olmalı.

---

## Section-by-Section Checklist / Bölüm Bölüm Kontrol Listesi

```
[ ] Problem Statement: evidence-based, cited, ≤ 1 page
[ ] Literature / State of the Art: gap clearly identified, cited
[ ] Innovation Claim: one explicit sentence
[ ] Methodology: detailed enough for specialist review, WPs visible
[ ] Work Plan / Gantt: all deliverables present, all milestones dated
[ ] Impact: scientific + societal + funder-specific
[ ] Team / CV section: track record supports feasibility claim
[ ] Budget Narrative: consistent with Phase 3 budget_table.md
[ ] Abstract: written last, ≤ 250 words (or call limit), covers all sections
```

---

## AI Hakem İncelemesi / AI Reviewer Gate

Yazım fazı tamamlandığında, sonraki faza geçmeden önce `/ai-review` komutu çalıştırılmalıdır.
Bkz: `skills/core/reviewer-mode.md`

Before advancing to the next phase, run `/ai-review` to trigger AI Peer Review.
See: `skills/core/reviewer-mode.md`

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] All sections drafted in writing order, then reordered for submission
- [ ] Iron Rule 1 check passed (all claims sourced)
- [ ] Alignment check: every funder criterion explicitly addressed
- [ ] Total length within ±10% of page limit
- [ ] Abstract written last and reviewed for accuracy
- [ ] proposal_draft.md saved and version-controlled
