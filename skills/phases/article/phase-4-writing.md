---
title: "Phase 4 — Section Writing"
title_tr: "Aşama 4 — Bölüm Yazımı"
node_type: phase
phase_number: 4
document_type: article
phase_gate_in: "phase-3-argument.md"
phase_gate_out: "phase-5-revision.md"
description: "Write each section of the article in the order that minimizes structural risk. Track word count against the journal limit. Every claim in the draft must have a source."
description_tr: "Yapısal riski minimize eden sırayla makalenin her bölümünü yaz. Kelime sayısını dergi limitine karşı takip et. Taslaktaki her iddianın kaynağı olmalı."
tags: [phase, article, writing, drafting, word-count]
outputs:
  - "draft/methods.md"
  - "draft/results.md"
  - "draft/discussion.md"
  - "draft/introduction.md"
  - "draft/abstract.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/core/source-policy.md
  - skills/techniques/drafting-alternatives.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/natural-voice.md
  - skills/core/guided-writing-mode.md
language: bilingual
version: "1.0"
---

# Phase 4 — Section Writing / Bölüm Yazımı

## Purpose / Amaç

Writing order in journal articles is counter-intuitive: the Introduction is written last, not first. This order exists because you cannot honestly introduce what you have not yet demonstrated. Writing the evidence sections first prevents the common failure of promising more than the evidence delivers.

Dergi makalelerinde yazım sırası sezgiye aykırıdır: Giriş en son yazılır, ilk olarak değil. Bu sıra, henüz kanıtlamadığın şeyi dürüstçe tanıtamayacağın için vardır. Kanıt bölümlerini önce yazmak, kanıtın sunduğundan fazlasını vaat etme yaygın başarısızlığını önler.

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

**1. Methods / Framework** → **2. Results / Evidence** → **3. Discussion** → **4. Introduction** → **5. Abstract**

This is not optional. Follow this order.

Bu isteğe bağlı değil. Bu sırayı takip et.

---

## Section 1: Methods / Framework / Yöntemler / Çerçeve

Write: what did you do, and why is this the right way to investigate the claim?

Yaz: ne yaptın ve bu, iddiayı araştırmanın doğru yolu neden?

Guidelines:
- Be precise enough that a reader could replicate or critically evaluate the approach
- Cite the methodological sources assigned to this section in `argument_map.md`
- Do not include results here — only the approach
- If theoretical/analytical: describe the framework and justify its selection

Kılavuzlar:
- Bir okuyucunun yaklaşımı kopyalayabileceği veya eleştirel olarak değerlendirebileceği kadar kesin ol
- `argument_map.md` dosyasında bu bölüme atanan metodolojik sourcesı atıf yap
- Buraya sonuç dahil etme — yalnızca yaklaşım
- Teorik/analitik ise: çerçeveyi tanımla ve seçimini gerekçelendir

After drafting: verify that every procedural or methodological claim has a source or an explicit statement that this is your novel contribution.

Taslak oluşturduktan sonra: her prosedürel veya metodolojik iddianın bir kaynağı ya da bunun senin özgün katkın olduğuna dair açık bir ifade içerdiğini doğrula.

---

## Section 2: Results / Evidence / Sonuçlar / Kanıt

Write: what did the analysis produce?

Yaz: analiz ne ürettim?

Guidelines:
- Present findings without interpretation — that comes in Discussion
- For quantitative work: report statistics, tables, figures
- For qualitative/analytical work: present the evidence as structured arguments
- Every figure and table must have a caption that stands alone
- Every numerical claim must cite its source or state it is your data
- **Drafting Rule:** Apply `drafting-alternatives.md` for major paragraphs. Offer the user A/B/C options and a scoring matrix before finalizing the text.

Kılavuzlar:
- Bulguları yorumsuz sun — bu Tartışmada geliyor
- Nicel çalışma için: istatistikleri, tabloları, şekilleri raporla
- Nitel/analitik çalışma için: kanıtı yapılandırılmış argümanlar olarak sun
- Her şekil ve tablonun bağımsız duran bir başlığı olmalı
- Her sayısal iddia kaynağını atıf yapmalı ya da bunun senin verin olduğunu belirtmeli
- **Taslak Kuralı:** Önemli paragraflar için `drafting-alternatives.md` kuralını uygula. Metni sonlandırmadan önce kullanıcıya A/B/C seçenekleri ve bir puanlama matrisi sun.

After drafting: check — does this section deliver what the Methods section set up?

Taslak oluşturduktan sonra: kontrol et — bu bölüm, Yöntemler bölümünün kurduğunu teslim ediyor mu?

---

## Section 3: Discussion / Tartışma

Write: what do the results mean for the contribution claim?

Yaz: sonuçlar katkı iddiası için ne anlama geliyor?

Guidelines:
- Open Discussion by restating the central claim and immediately connecting it to the results
- Address every counter-argument identified in `argument_map.md`
- Compare your findings to the landmark works from Phase 1 — how do your results advance, confirm, or complicate theirs?
- Acknowledge limitations directly and specifically (not vaguely: "future research is needed")
- Do not introduce new evidence or new sources not in `OKUMA_RAPORU.md`

Kılavuzlar:
- Tartışmayı merkezi iddiayı yeniden ifade ederek ve hemen sonuçlara bağlayarak aç
- `argument_map.md` dosyasında belirtilen her karşı-argümanı ele al
- Bulgularını Aşama 1'deki temel çalışmalarla karşılaştır — sonuçlarındır onların çalışmasını nasıl ilerletiyor, onaylıyor veya karmaşıklaştırıyor?
- Sınırlılıkları doğrudan ve spesifik olarak kabul et (belirsiz değil: "gelecekteki araştırmaya ihtiyaç var")
- `OKUMA_RAPORU.md` dosyasında olmayan yeni kanıt veya yeni sources tanıtma

After drafting: verify that Discussion does not claim more than the Results established.

Taslak oluşturduktan sonra: Tartışmanın Sonuçların ortaya koyduğundan fazlasını iddia etmediğini doğrula.

---

## Section 4: Introduction / Giriş

Write the Introduction only after Methods, Results, and Discussion are drafted.

Giriş'i yalnızca Yöntemler, Sonuçlar ve Tartışma taslaklandıktan sonra yaz.

Guidelines:
- Open with the problem or gap (not with a broad claim about the field)
- Cite the landmark works to establish the conversation you are entering
- State the contribution claim explicitly (do not make readers guess)
- Preview the structure: "This article first... then... finally..."
- Introduction length: typically 10-15% of total article word count

Kılavuzlar:
- Problem veya boşlukla aç (alan hakkında geniş bir iddiayla değil)
- Girdiğin konuşmayı kurmak için temel çalışmaları atıf yap
- Katkı iddiasını açıkça belirt (okuyucuların tahmin etmesini sağlama)
- Yapıyı önizle: "Bu makale önce... sonra... son olarak..."
- Giriş uzunluğu: tipik olarak toplam makale kelime sayısının %10-15'i

After drafting: check that every promise in the Introduction is delivered in the article.

Taslak oluşturduktan sonra: Girişte verilen her vaadin makalede yerine getirildiğini kontrol et.

---

## Section 5: Abstract / Özet

Write the Abstract last. The Abstract is a miniature version of the complete article.

Özeti en son yaz. Özet, tamamlanmış makalenin minyatür versiyonudur.

Four-sentence abstract framework (adapt to journal requirements):

Dört cümlelik özet çerçevesi (dergi gereksinimlerine adapte et):

1. Problem/gap sentence: "Research on X has not addressed Y."
2. Method sentence: "This article [does / analyzes / examines] Z using [approach]."
3. Result sentence: "The analysis shows / finds / demonstrates [specific finding]."
4. Implication sentence: "These findings suggest / establish / contribute [implication]."

Check: can a specialist in the field understand the contribution from the Abstract alone, without reading the article?

Kontrol: Alandaki bir uzman, makaleyi okumadan yalnızca Özetten katkıyı anlayabilir mi?

---

## Word Count Tracking / Kelime Sayısı Takibi

Record target word count from journal guidelines. Track after each section draft.

Dergi kılavuzlarından hedef kelime sayısını kaydet. Her bölüm taslağından sonra takip et.

| Section | Target Words | Drafted Words | Status |
|---|---|---|---|
| Methods | [N] | — | pending |
| Results | [N] | — | pending |
| Discussion | [N] | — | pending |
| Introduction | [N] | — | pending |
| Abstract | [max N] | — | pending |
| References | — | — | pending |
| **Total** | **[journal limit]** | — | — |

If over the journal limit after first draft: cut in Discussion and Introduction first. Methods and Results cuts are higher risk.

İlk taslaktan sonra dergi limitinin üzerindeyse: önce Tartışma ve Girişte kes. Yöntemler ve Sonuçlar kesintileri daha yüksek risk taşır.

---

## AI Hakem İncelemesi / AI Reviewer Gate

Yazım fazı tamamlandığında, sonraki faza geçmeden önce `/ai-review` komutu çalıştırılmalıdır.
Bkz: `skills/core/reviewer-mode.md`

Before advancing to the next phase, run `/ai-review` to trigger AI Peer Review.
See: `skills/core/reviewer-mode.md`

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] All five sections drafted in the correct order.
- [ ] Every claim in the draft has a source or is marked as the author's original contribution.
- [ ] Word count is within the journal limit (or a plan exists to reach it).
- [ ] Discussion does not exceed what Results established.
- [ ] Introduction promises are delivered in the body.
- [ ] Abstract stands alone as a complete summary.

- [ ] Tüm beş bölüm doğru sırayla taslaklandırılmış.
- [ ] Taslaktaki her iddianın kaynağı var veya yazarın özgün katkısı olarak işaretlenmiş.
- [ ] Kelime sayısı dergi limiti dahilinde (veya ulaşmak için bir plan var).
- [ ] Tartışma, Sonuçların ortaya koyduğunu aşmıyor.
- [ ] Giriş vaatleri gövdede yerine getirilmiş.
- [ ] Özet eksiksiz bir özet olarak bağımsız duruyor.

Do not proceed to Phase 5 until all five sections are drafted and word count is in range.

Tüm beş bölüm taslaklandırılmadan ve kelime sayısı aralıkta olmadan Aşama 5'e geçme.
