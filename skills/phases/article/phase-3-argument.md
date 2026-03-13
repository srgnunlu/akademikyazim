---
title: "Phase 3 — Single Argument Architecture"
title_tr: "Aşama 3 — Tek Argüman Mimarisi"
node_type: phase
phase_number: 3
document_type: article
phase_gate_in: "phase-2-reading.md"
phase_gate_out: "phase-4-writing.md"
description: "Design the single central argument that runs through the entire article. Map every source to a section, identify counter-arguments, and ensure the logical flow is complete before writing begins."
description_tr: "Makalenin tamamına yayılan tek merkezi argümanı tasarla. Her kaynağı bir bölüme eşle, karşı-argümanları belirle ve yazma başlamadan önce mantıksal akışın tam olduğundan emin ol."
tags: [phase, article, argument, architecture, structure]
outputs:
  - "argument_map.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 3 — Single Argument Architecture / Tek Argüman Mimarisi

## Purpose / Amaç

A journal article is not a collection of topics — it is a single argument, developed systematically from claim to evidence to conclusion. This phase builds the skeleton of that argument before a single section is written. Structural problems discovered here cost one hour to fix. Structural problems discovered in Phase 4 cost days.

Bir dergi makalesi konu koleksiyonu değildir — iddiadan kanıta sonuca sistematik olarak geliştirilen tek bir argümandır. Bu aşama, tek bir bölüm yazılmadan önce o argümanın iskeletini inşa eder. Burada keşfedilen yapısal sorunları düzeltmek bir saat alır. Aşama 4'te keşfedilen yapısal sorunlar günler alır.

---

## Step 1 — Restate the Central Claim / Merkezi İddiayı Yeniden İfade Et

Return to `claim_statement.md`. After reading (Phase 2), has the claim changed? If yes, update it now — not after writing.

`claim_statement.md` dosyasına dön. Okuma sonrası (Aşama 2) iddia değişti mi? Evet ise şimdi güncelle — yazmadan sonra değil.

The claim must remain singular. If you find yourself stating two independent claims, you either have two articles or you have one claim and one implication. Decide which.

İddia tekil kalmalı. Birbirinden bağımsız iki iddia ifade ettiğini fark edersen, ya iki makalenin var ya da bir iddia ve bir çıkarımın var. Hangisi olduğuna karar ver.

---

## Step 2 — Map the Argument Structure / Argüman Yapısını Haritalandır

A standard journal article argument runs:

Standart bir dergi makalesi argümanı şu şekilde ilerler:

**Introduction** — Establishes the gap, states the claim, previews the structure.
What do readers need to know to understand why the claim matters? What is promised in this article?

**Giriş** — Boşluğu kurar, iddiayı belirtir, yapıyı önizler.
Okuyucuların iddiasının neden önemli olduğunu anlamak için ne bilmesi gerekiyor? Bu makalede ne vaat ediliyor?

**Methods / Framework** — How is the claim tested, demonstrated, or developed?
What evidence or analytical framework supports the claim? Why is this method appropriate?

**Yöntemler / Çerçeve** — İddia nasıl test ediliyor, gösteriliyor veya geliştiriliyor?
İddiayı hangi kanıt veya analitik çerçeve destekliyor? Bu yöntem neden uygun?

**Results / Evidence** — What did the analysis produce?
Present findings without interpretation. If qualitative: present the argument's evidence. If quantitative: present data.

**Sonuçlar / Kanıt** — Analiz ne ürettim?
Bulguları yorumsuz sun. Nitel ise: argümanın kanıtını sun. Nicel ise: verileri sun.

**Discussion** — What do the results mean for the claim?
Do the results confirm, complicate, or require qualification of the claim? Address counter-arguments here.

**Tartışma** — Sonuçlar iddia için ne anlama geliyor?
Sonuçlar iddiayı doğruluyor mu, karmaşıklaştırıyor mu, yoksa nitelendirme mi gerektiriyor? Karşı-argümanları burada ele al.

**Conclusion** — What has been established? What comes next?
Restate the claim in light of evidence. Identify limitations. Identify future directions.

**Sonuç** — Ne ortaya konuldu? Sırada ne var?
Kanıt ışığında iddiayı yeniden ifade et. Sınırlılıkları belirle. Gelecek yönleri belirle.

---

## Step 3 — Assign Every AKTİF Source to a Section / Her AKTİF Kaynağı Bir Bölüme Ata

Open `OKUMA_RAPORU.md`. For every ⭐ AKTİF source, confirm which section it serves.

`OKUMA_RAPORU.md` dosyasını aç. Her ⭐ AKTİF kaynak için hangi bölüme hizmet ettiğini onayla.

Sources not assigned to any section: remove from AKTİF, downgrade to OKUNDU. If you cannot assign a source, it means either the source is not actually needed, or the argument map is incomplete.

Hiçbir bölüme atanmayan sources: AKTİF'ten çıkar, OKUNDU'ya düşür. Bir kaynağı atayamazsan, ya kaynak gerçekten gerekli değil, ya da argüman haritası eksik.

---

## Step 4 — Identify Counter-Arguments / Karşı-Argümanları Belirle

Every strong contribution claim has at least one credible objection. List them now.

Her güçlü katkı iddiasının en az bir güvenilir itirazı vardır. Onları şimdi listele.

For each counter-argument:
- State it precisely (not as a strawman)
- Identify which source(s) make or imply this objection
- Decide: will this be addressed in Discussion, or in a footnote?
- Write one sentence that pre-empts or responds to it

Her karşı-argüman için:
- Tam olarak ifade et (saman adam olarak değil)
- Hangi kaynak(lar)ın bu itirazı yaptığını veya ima ettiğini belirle
- Karar ver: Tartışmada mı ele alınacak, yoksa dipnotta mı?
- Onu önleyen veya yanıtlayan bir cümle yaz

---

## Step 5 — Check for Logical Completeness / Mantıksal Bütünlüğü Kontrol Et

Before proceeding to writing, check:

Yazıya geçmeden önce kontrol et:

- Does the Introduction gap directly motivate the Methods/Framework chosen?
- Do the Results/Evidence directly address the Methods/Framework?
- Does the Discussion interpret the Results relative to the original claim (not relative to something else)?
- Does the Conclusion restate the claim as now established — not as merely suggested?

- Giriş boşluğu seçilen Yöntemler/Çerçeveyi doğrudan motive ediyor mu?
- Sonuçlar/Kanıt doğrudan Yöntemler/Çerçeveyi ele alıyor mu?
- Tartışma, Sonuçları orijinal iddiaya göre mi yorumluyor (başka bir şeye göre değil)?
- Sonuç bölümü, iddiayı artık kurulmuş olarak mı yeniden ifade ediyor — yalnızca önerilmiş olarak değil?

If any answer is no, revise the argument map now.

Herhangi bir cevap hayırsa, argüman haritasını şimdi revize et.

---

## Output / Çıktı

Create `argument_map.md` containing:
1. Final contribution claim (updated if necessary)
2. Section-by-section argument outline with 2-3 sentences per section describing content
3. Source-to-section assignment table
4. Counter-argument list with planned responses
5. Logical completeness check (each of the four checks above, marked yes/no with notes)

`argument_map.md` oluştur:
1. Son katkı iddiası (gerekirse güncellenmiş)
2. Bölüm başına 2-3 cümle içerik açıklaması ile bölüm bölüm argüman taslağı
3. Kaynak-bölüm atama tablosu
4. Planlı yanıtlarla karşı-argüman listesi
5. Mantıksal bütünlük kontrolü (yukarıdaki dört kontrolün her biri, notlarla evet/hayır işaretli)

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Contribution claim confirmed or updated.
- [ ] Argument map covers all six sections.
- [ ] Every AKTİF source is assigned to exactly one section.
- [ ] At least one counter-argument is identified and addressed.
- [ ] All four logical completeness checks pass.
- [ ] `argument_map.md` is written and saved.

- [ ] Katkı iddiası onaylanmış veya güncellenmiş.
- [ ] Argüman haritası tüm altı bölümü kapsıyor.
- [ ] Her AKTİF kaynak tam olarak bir bölüme atanmış.
- [ ] En az bir karşı-argüman belirlenmiş ve ele alınmış.
- [ ] Dört mantıksal bütünlük kontrolünün tümü geçilmiş.
- [ ] `argument_map.md` yazılmış ve kaydedilmiş.

Do not proceed to Phase 4 until the argument map is logically complete.

Argüman haritası mantıksal olarak tamamlanmadan Aşama 4'e geçme.
