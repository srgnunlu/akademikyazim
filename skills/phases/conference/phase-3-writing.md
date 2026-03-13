---
title: "Phase 3 — Writing Against Abstract Commitments"
title_tr: "Aşama 3 — Özet Taahhütlerine Karşı Yazım"
node_type: phase
phase_number: 3
document_type: conference
phase_gate_in: "phase-2-reading.md"
phase_gate_out: "phase-4-finalization.md"
description: "Write the full paper. Every section must deliver exactly what the submitted abstract promised. The conference template governs structure. Reverse-engineer the writing plan from the submission deadline."
description_tr: "Tam bildiriyi yaz. Her bölüm, gönderilen özetin vaat ettiği tam olarak neyse onu teslim etmelidir. Konferans şablonu yapıyı belirler. Yazım planını gönderim son tarihinden geriye doğru mühendislik et."
tags: [phase, conference, writing, deadline, structure]
outputs:
  - "draft/paper_draft.md (or .tex)"
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

# Phase 3 — Writing Against Abstract Commitments / Özet Taahhütlerine Karşı Yazım

## Purpose / Amaç

The submitted abstract is a binding commitment to the program committee and reviewers. Every section of the full paper must deliver what the abstract promised — no more (scope creep), no less (under-delivery). This phase structures the writing process around that commitment and against the submission deadline.

Gönderilen özet, program komitesi ve hakemlere karşı bağlayıcı bir taahhüttür. Tam bildirinin her bölümü, özetin vaat ettiğini teslim etmelidir — fazlasını değil (kapsam kayması), eksiğini değil (eksik teslimat). Bu aşama, yazım sürecini o taahhüt etrafında ve gönderim son tarihine karşı yapılandırır.

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

## Step 1 — Build the Reverse-Deadline Writing Plan / Geriye Doğru Son Tarih Yazım Planını Oluştur

From the submission deadline, work backwards:

Gönderim son tarihinden geriye doğru çalış:

| Day | Task |
|---|---|
| Deadline - 0 | Submission |
| Deadline - 1 | Final proofreading and formatting check |
| Deadline - 2 | Phase 4 finalization (format, anonymize, page limit) |
| Deadline - 3 | Complete draft; all sections written |
| Deadline - 4 | Discussion + Conclusion drafted |
| Deadline - 5 | Introduction + Related Work drafted |
| Deadline - 6 | Methods + Results/Evidence drafted |
| Deadline - 7 | Writing plan confirmed; Phase 3 begins |

Adjust based on paper length and available working time. The plan is written before writing begins.

Bildiri uzunluğuna ve mevcut çalışma süresine göre ayarla. Plan, yazım başlamadan önce yazılır.

---

## Step 2 — Map the Abstract to Sections / Özeti Bölümlere Eşle

Open `abstract_v1.md`. Identify where each of the four abstract elements will be delivered in the paper:

`abstract_v1.md` dosyasını aç. Dört özet öğesinin her birinin bildiride nerede teslim edileceğini belirle:

| Abstract Element | Paper Section | Specific Content Committed |
|---|---|---|
| Problem | Introduction | [exact problem statement from abstract] |
| Approach | Methods | [exact method or framework committed] |
| Contribution | Discussion / Conclusion | [exact contribution claim committed] |
| Result | Results / Evaluation | [exact result or expected result committed] |

If the result was labeled "expected" in the abstract, the paper must either (a) deliver actual results, or (b) explicitly address the status of the result and why the paper is still a contribution.

Sonuç özette "beklenen" olarak etiketlendiyse, bildiri ya (a) gerçek sonuçlar teslim etmeli, ya da (b) sonucun durumunu ve bildirinin neden hâlâ katkı olduğunu açıkça ele almalıdır.

---

## Step 3 — Follow the Conference Template Exactly / Konferans Şablonunu Tam Olarak Takip Et

Conference papers follow the template of the organizing body. Do not invent section headings.

Konferans bildirileri, düzenleyici kuruluşun şablonunu takip eder. Bölüm başlıkları icat etme.

Retrieve the conference template (LaTeX, Word, or Overleaf) now and write directly into it. Do not write in a plain text file and migrate later — formatting errors are harder to fix at the last moment.

Konferans şablonunu (LaTeX, Word veya Overleaf) şimdi al ve doğrudan içine yaz. Düz metin dosyasına yazıp sonra taşıma — biçimlendirme hataları son anda düzeltmek daha zordur.

Typical conference paper sections:

Tipik konferans bildirisi bölümleri:

1. **Abstract** (already written — paste from `abstract_v1.md`)
2. **Introduction** — Problem, gap, contribution claim, paper structure
3. **Related Work** — Use the topic/gap table from `lit_position.md`
4. **Methods / System / Framework** — Deliver the approach committed in the abstract
5. **Evaluation / Results** — Deliver the result committed in the abstract
6. **Discussion** — Interpret results relative to the contribution claim; address limitations
7. **Conclusion** — Restate contribution; future work (brief)
8. **References**

---

## Step 4 — Writing Each Section / Her Bölümü Yazma

**Related Work** — Write first. This is direct conversion of the `lit_position.md` table into prose. Paragraph per topic row. Keep it short: typically 0.5-1 page.

**İlgili Çalışmalar** — Önce yaz. Bu, `lit_position.md` tablosunu düzyazıya doğrudan dönüştürmedir. Konu satırı başına bir paragraf. Kısa tut: tipik olarak 0.5-1 sayfa.

**Methods / Framework** — Write second. Precise enough for replication or evaluation. No padding. Every methodological claim cites its source or is stated as your contribution.

**Yöntemler / Çerçeve** — İkinci yaz. Kopyalama veya değerlendirme için yeterince kesin. Dolgu yok. Her metodolojik iddia kaynağını atıf yaptırır veya senin katkın olarak belirtilir.

**Results / Evaluation** — Write third. Deliver what the abstract committed. Tables, figures, and metrics must be presented cleanly. No interpretation here — save that for Discussion.

**Sonuçlar / Değerlendirme** — Üçüncü yaz. Özetin taahhüt ettiğini teslim et. Tablolar, şekiller ve metrikler temiz sunulmalıdır. Burada yorum yok — bunu Tartışma için sakla.

**Discussion** — Write fourth. Interpret results relative to the contribution claim. Address at least one limitation. Compare to the most relevant related work.

**Tartışma** — Dördüncü yaz. Sonuçları katkı iddiasına göre yorumla. En az bir sınırlılığı ele al. En ilgili ilgili çalışmalarla karşılaştır.

**Introduction** — Write fifth. State the problem, the gap, the contribution claim (explicitly, not implicitly), and the paper structure ("Section 2 reviews... Section 3 presents...").

**Giriş** — Beşinci yaz. Problemi, boşluğu, katkı iddiasını (açıkça, örtük değil) ve bildiri yapısını belirt ("Bölüm 2 inceler... Bölüm 3 sunar...").

**Conclusion** — Write last. Restate the contribution. Identify 1-2 specific future directions. Do not introduce new claims.

**Sonuç** — En son yaz. Katkıyı yeniden ifade et. 1-2 spesifik gelecek yön belirle. Yeni iddialar tanıtma.

---

## Scope Discipline / Kapsam Disiplini

Every paragraph written must serve one of these purposes:
- Delivering what the abstract promised
- Providing necessary context for the reader to evaluate the contribution
- Addressing a limitation or counter-argument

Her yazılan paragraf şu amaçlardan birine hizmet etmelidir:
- Özetin vaat ettiğini teslim etmek
- Okuyucunun katkıyı değerlendirmesi için gerekli bağlamı sağlamak
- Bir sınırlılığı veya karşı-argümanı ele almak

If a paragraph does not serve one of these purposes, delete it. Conference page limits enforce discipline that journal pages do not.

Bir paragraf bu amaçlardan birine hizmet etmiyorsa, sil. Konferans sayfa limitleri, dergi sayfalarının uygulamadığı disiplini dayatır.

---

## AI Hakem İncelemesi / AI Reviewer Gate

Yazım fazı tamamlandığında, sonraki faza geçmeden önce `/ai-review` komutu çalıştırılmalıdır.
Bkz: `skills/core/reviewer-mode.md`

Before advancing to the next phase, run `/ai-review` to trigger AI Peer Review.
See: `skills/core/reviewer-mode.md`

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Writing plan (reverse-deadline) created before writing began.
- [ ] All sections written in the correct order.
- [ ] Every section delivers what `abstract_v1.md` committed.
- [ ] Abstract element-to-section mapping table is satisfied.
- [ ] Every claim in the draft has a source or is stated as the author's contribution.
- [ ] Draft is written directly in the conference template (LaTeX/Word).
- [ ] Word/page count is estimated and within range.

- [ ] Geriye-doğru-son tarih yazım planı yazıma başlamadan önce oluşturulmuş.
- [ ] Tüm bölümler doğru sırayla yazılmış.
- [ ] Her bölüm `abstract_v1.md` dosyasının taahhüt ettiğini teslim ediyor.
- [ ] Özet öğesi-bölüm eşleme tablosu tatmin edilmiş.
- [ ] Taslaktaki her iddianın kaynağı var veya yazarın katkısı olarak belirtilmiş.
- [ ] Taslak doğrudan konferans şablonuna (LaTeX/Word) yazılmış.
- [ ] Kelime/sayfa sayısı tahmin edilmiş ve aralıkta.

Do not proceed to Phase 4 until the draft is complete and within the page limit range.

Taslak tamamlanmadan ve sayfa limiti aralığında olmadan Aşama 4'e geçme.
