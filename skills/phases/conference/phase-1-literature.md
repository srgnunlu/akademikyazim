---
title: "Phase 1 — Focused Literature"
title_tr: "Aşama 1 — Odaklı Literatür"
node_type: phase
phase_number: 1
document_type: conference
phase_gate_in: "phase-0-abstract.md"
phase_gate_out: "phase-2-reading.md"
description: "Build a focused literature list of 15-30 sources directly relevant to the abstract's contribution. Conference papers cite less than journals — this is correct, not a shortcut."
description_tr: "Özetin katkısıyla doğrudan ilgili 15-30 kaynaktan oluşan odaklı bir literatür listesi oluştur. Konferans bildirileri dergilerden daha az atıf yapar — bu doğrudur, kısayol değil."
tags: [phase, conference, literature, focused, positioning]
outputs:
  - "lit_position.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 1 — Focused Literature / Odaklı Literatür

## Purpose / Amaç

Conference papers have strict page limits. A 6-page paper cannot carry 60 references and still have room for content. The literature scope for a conference paper is deliberately narrower than a journal article — this is not a weakness, it reflects the format. The goal is precision: cite exactly what you need to position the contribution and no more.

Konferans bildirilerinin katı sayfa limitleri vardır. 6 sayfalık bir bildiri 60 referans taşıyıp hâlâ içerik için yer bulamaz. Konferans bildirisi için literatür kapsamı, bir dergi makalesinden kasıtlı olarak daha dardır — bu bir zayıflık değil, formatı yansıtır. Amaç kesinliktir: katkıyı konumlandırmak için tam olarak neye ihtiyacın varsa onu atıf yap, fazlasını değil.

---

## Step 1 — Define the Citation Budget / Atıf Bütçesini Belirle

Check the conference page limit and typical reference density for that venue:

Konferans sayfa limitini ve o mekan için tipik referans yoğunluğunu kontrol et:

- 4-page papers: typically 10-20 references
- 6-page papers: typically 15-25 references
- 8-page papers: typically 20-35 references
- 10-page papers: typically 25-40 references

Set your target: "This paper will have approximately N references." This is your citation budget.

Hedefinizi belirle: "Bu bildirinin yaklaşık N referansı olacak." Bu senin atıf bütçendir.

---

## Step 2 — Priority Criteria / Öncelik Kriterleri

With a limited citation budget, every reference must earn its place. Apply this priority order:

Sınırlı bir atıf bütçesiyle, her referans yerini kazanmalı. Bu öncelik sırasını uygula:

**Priority 1 — Most recent, from this venue or closely related venues**
If you are submitting to ACM CHI, recent CHI papers on your topic signal that your work belongs there. If you are submitting to an IEEE conference, IEEE publications in the niche carry weight with reviewers.

**Öncelik 1 — En güncel, bu mekandan veya yakından ilgili mekanlardan**
ACM CHI'ye gönderiyorsan, konuna ilişkin güncel CHI makaleleri, çalışmanın oraya ait olduğuna işaret eder.

**Priority 2 — Most cited in this specific subfield (last 5 years)**
These are the papers reviewers will expect to see. If you do not cite them, reviewers will notice. Search Google Scholar, Semantic Scholar, or the specific venue's proceedings for citation counts.

**Öncelik 2 — Bu spesifik alt-alanda en çok atıf alan (son 5 yıl)**
Bunlar, hakemlerin görmeyi beklediği makalelerdir. Onları atıf yapmasan, hakemler fark eder.

**Priority 3 — Directly supports or challenges the abstract's contribution claim**
Any paper that makes the same claim (must be engaged with), contradicts your result (must be addressed), or provides the method you use (must be cited).

**Öncelik 3 — Özetin katkı iddiasını doğrudan destekleyen veya zorlayan**
Aynı iddiayı yapan herhangi bir makale (etkileşime girilmeli), sonucuna çelişen (ele alınmalı) veya kullandığın yöntemi sağlayan (atıf yapılmalı).

---

## Step 3 — Search Strategy / Arama Stratejisi

Search efficiently — conference paper timelines are compressed.

Verimli ara — konferans bildirisi zaman çizelgeleri sıkıştırılmıştır.

Start with the target conference's own proceedings (ACM DL, IEEE Xplore, or the conference website's past proceedings). Search for your 3-5 key terms. This quickly surfaces what the community has already done and what it expects to see cited.

Hedef konferansın kendi bildiri kitabıyla (ACM DL, IEEE Xplore veya konferans web sitesinin geçmiş bildiri kitapları) başla. 3-5 anahtar terimin için ara. Bu, topluluğun zaten ne yaptığını ve neyin atıf yapılmasını beklediğini hızla ortaya çıkarır.

Then search Google Scholar for the most cited recent work on your topic. Stop when you reach 30 candidates — do not exceed 30 at this stage.

Ardından Google Scholar'da konunuzla ilgili en çok atıf alan güncel çalışmayı ara. 30 adaya ulaştığında dur — bu aşamada 30'u aşma.

---

## Step 4 — Winnow to 15-30 / 15-30'a İndir

Apply the priority criteria from Step 2 to each candidate. Keep only those that:
- Have appeared in the target venue or a closely related venue recently (Priority 1), OR
- Are the most cited in the subfield (Priority 2), OR
- Directly serve the abstract's contribution claim (Priority 3)

Her adaya Adım 2'deki öncelik kriterlerini uygula. Yalnızca şunları tut:
- Son zamanlarda hedef mekanda veya yakından ilgili bir mekanda yayınlanmış (Öncelik 1), VEYA
- Alt-alanda en çok atıf alan (Öncelik 2), VEYA
- Özetin katkı iddiasına doğrudan hizmet eden (Öncelik 3)

If a source passes none of the three priorities, it does not belong in a conference paper's reference list. Remove it.

Bir kaynak üç önceliğin hiçbirini geçmiyorsa, konferans bildirisi referans listesine ait değildir. Kaldır.

---

## Step 5 — Build the Literature Position Table / Literatür Konum Tablosunu Oluştur

Create a brief structured table for `lit_position.md`:

`lit_position.md` için kısa bir yapılandırılmış tablo oluştur:

| Topic | Key Papers | What They Cover | Gap / Your Advance |
|---|---|---|---|
| [topic] | [Author Year] | [what is covered] | [what your paper does that they do not] |

This table should have 3-6 rows — one per sub-topic of the abstract. Keep it short. This table becomes the basis of the Related Work section.

Bu tablo 3-6 satır içermeli — özetin her alt konusu için bir tane. Kısa tut. Bu tablo, İlgili Çalışmalar bölümünün temelini oluşturur.

---

## Output / Çıktı

**lit_position.md** containing:
1. Citation budget (target number of references)
2. Search terms and venues searched
3. Topic/gap table (3-6 rows)
4. Final list of 15-30 sources with full citations, formatted for the target conference

**lit_position.md** içeren:
1. Atıf bütçesi (hedef referans sayısı)
2. Aranan arama terimleri ve mekanlar
3. Konu/boşluk tablosu (3-6 satır)
4. Hedef konferans için biçimlendirilmiş tam atıflarla 15-30 kaynak listesi

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Citation budget defined based on page limit.
- [ ] Sources are capped at 30 maximum, with a target of 15-25.
- [ ] Every source passes at least one of the three priority criteria.
- [ ] Topic/gap table completed with 3-6 rows.
- [ ] All citations formatted correctly for the target conference.
- [ ] `lit_position.md` written and saved.

- [ ] Sayfa limitine göre atıf bütçesi tanımlanmış.
- [ ] Kaynaklar maksimum 30 ile sınırlandırılmış, 15-25 hedefleniyor.
- [ ] Her kaynak üç öncelik kriterinden en az birini geçiyor.
- [ ] Konu/boşluk tablosu 3-6 satırla tamamlanmış.
- [ ] Tüm atıflar hedef konferans için doğru biçimlendirilmiş.
- [ ] `lit_position.md` yazılmış ve kaydedilmiş.

Do not proceed to Phase 2 until the source list is within the citation budget.

Kaynak listesi atıf bütçesi dahilinde olmadan Aşama 2'ye geçme.
