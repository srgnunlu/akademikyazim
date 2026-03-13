---
title: "Phase 2 — Focused Reading"
title_tr: "Aşama 2 — Odaklı Okuma"
node_type: phase
phase_number: 2
document_type: article
phase_gate_in: "phase-1-literature.md"
phase_gate_out: "phase-3-argument.md"
description: "Read the candidate sources using a three-level triage system. Every source must directly serve the contribution claim. Maximum 40 active sources."
description_tr: "Aday sourcesı üç seviyeli triyaj sistemiyle oku. Her kaynak doğrudan katkı iddiasına hizmet etmeli. Maksimum 40 aktif kaynak."
tags: [phase, article, reading, triage, notes]
outputs:
  - "OKUMA_RAPORU.md"
  - "notlar/ (one note file per active source)"
links_to:
  - skills/core/iron-rules.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 2 — Focused Reading / Odaklı Okuma

## Purpose / Amaç

This phase converts the literature list from Phase 1 into actionable reading notes. Articles are not theses — you cannot read everything deeply. The triage system lets you invest reading time where the contribution claim demands it, and skip or skim where it does not.

Bu aşama, Aşama 1'deki literatür listesini kullanılabilir okuma notlarına dönüştürür. Makaleler tez değildir — her şeyi derinlemesine okuyamazsın. Triyaj sistemi, okuma zamanını katkı iddiasının gerektirdiği yere yatırmanı ve gerektirmediği yerde atlamanı ya da yüzeysel okumanı sağlar.

---

## The Three-Level Triage System / Üç Seviyeli Triyaj Sistemi

Every source from `lit_position.md` receives one of three labels:

`lit_position.md` dosyasındaki her kaynak üç etiketten birini alır:

**⭐ AKTİF** — Read fully, take detailed notes, assign to a section of the argument map.
These sources will be cited and engaged with in the article text. Maximum 40 sources receive this label. Justification required if more than 30 are AKTİF.

**⭐ AKTİF** — Tamamen oku, ayrıntılı not al, argüman haritasının bir bölümüne ata.
Bu sources makale metninde atıf alacak ve tartışılacak. Maksimum 40 kaynak bu etiketi alır. 30'dan fazla AKTİF varsa gerekçe gerekli.

**✅ OKUNDU** — Read abstract, introduction, conclusion. Sufficient for background acknowledgment.
These sources appear in the reference list but receive minimal in-text engagement. No detailed notes required — one sentence summary only.

**✅ OKUNDU** — Özet, giriş, sonuç okundu. Arka plan kabulü için yeterli.
Bu sources referans listesinde görünür ama metinde minimal etkileşim alır. Ayrıntılı not gerekmez — yalnızca bir cümle özet.

**⏭️ ATLANDI** — Skimmed or not read. Excluded from reference list.
Record why it was skipped. Common reasons: out of scope, superseded by a more recent work, methodologically incompatible.

**⏭️ ATLANDI** — Göz gezdirildi veya okunmadı. Referans listesinden çıkarıldı.
Neden atlandığını kaydet. Yaygın nedenler: kapsam dışı, daha yeni bir çalışmayla geçersizleşti, metodolojik olarak uyumsuz.

---

## Scope Rule for AKTİF Sources / AKTİF Kaynaklar İçin Kapsam Kuralı

Before assigning ⭐ AKTİF, ask: does this source do at least one of the following?

⭐ AKTİF atamadan önce sor: bu kaynak aşağıdakilerden en az birini yapıyor mu?

1. Directly supports or challenges the contribution claim
2. Provides a method or framework the article adopts or critiques
3. Represents a key prior finding the article advances beyond
4. Offers a counter-argument that must be addressed in Discussion

1. Katkı iddiasını doğrudan destekliyor veya zorluyor
2. Makalenin benimsediği veya eleştirdiği bir yöntem veya çerçeve sunuyor
3. Makalenin ötesine geçtiği temel önceki bulguyu temsil ediyor
4. Tartışma bölümünde ele alınması gereken bir karşı-argüman sunuyor

If the answer to all four is no, the source is ✅ OKUNDU at most.

Dördüne de cevap hayırsa, kaynak en fazla ✅ OKUNDU'dur.

---

## Note Format for AKTİF Sources / AKTİF Kaynaklar İçin Not Formatı

Create one file per AKTİF source in the `notlar/` folder. Filename: `[AuthorYear]-[keyword].md`

Her AKTİF kaynak için `notlar/` klasöründe bir dosya oluştur. Dosya adı: `[YazarYıl]-[anahtar-kelime].md`

Each note file contains:
- Full citation
- Core argument of the paper (2-3 sentences)
- Key finding or claim (direct quote or close paraphrase with page number)
- How it relates to your contribution claim (1-2 sentences)
- Which section of the article it will be used in (Introduction / Methods / Discussion / Conclusion)
- Any counter-arguments or limitations to note

Her not dosyası içerir:
- Tam atıf
- Makalenin temel argümanı (2-3 cümle)
- Temel bulgu veya iddia (sayfa numarasıyla doğrudan alıntı veya yakın parafraz)
- Katkı iddiandıra nasıl ilişkili (1-2 cümle)
- Makalenin hangi bölümünde kullanılacak (Giriş / Yöntemler / Tartışma / Sonuç)
- Dikkat edilmesi gereken karşı-argümanlar veya sınırlılıklar

---

## Iron Rules Apply / Demir Kurallar Geçerli

See `skills/core/iron-rules.md`. Summary of non-negotiable rules for this phase:

`skills/core/iron-rules.md` dosyasına bak. Bu aşama için pazarlık edilemez kuralların özeti:

- Do not cite what you have not read. ✅ OKUNDU sources may be cited only for the claim confirmed in abstract/conclusion. AKTİF sources only: cite specific pages.
- Do not paraphrase a paraphrase. Go to the original source.
- If a source is unavailable, mark it ATLANDI. Do not cite from secondary summaries.

- Okumadığın şeyi atıf yapma. ✅ OKUNDU sources yalnızca özet/sonuçta doğrulanan iddia için atıf alabilir. Yalnızca AKTİF sources: belirli sayfalara atıf yap.
- Bir parafrazı parafraz yapma. Orijinal kaynağa git.
- Bir kaynak mevcut değilse, ATLANDI olarak işaretle. İkincil özetlerden atıf yapma.

---

## Output / Çıktı

**OKUMA_RAPORU.md** — A status table of all sources:

| Source | Label | Section Assigned | Note File |
|---|---|---|---|
| Author, Year | ⭐ AKTİF | Discussion | notlar/AuthorYear-keyword.md |
| Author, Year | ✅ OKUNDU | Background | — |
| Author, Year | ⏭️ ATLANDI | — | reason: out of scope |

**notlar/** — One `.md` file per AKTİF source.

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] Every source from Phase 1 has a triage label.
- [ ] No more than 40 sources are labeled AKTİF.
- [ ] Every AKTİF source has a note file in `notlar/`.
- [ ] Every AKTİF source is assigned to a section.
- [ ] `OKUMA_RAPORU.md` is complete with all sources listed.
- [ ] Iron Rules have been applied — no unread citations.

- [ ] Aşama 1'deki her kaynak bir triyaj etiketine sahip.
- [ ] 40'tan fazla kaynak AKTİF etiketli değil.
- [ ] Her AKTİF kaynak için `notlar/` klasöründe bir not dosyası var.
- [ ] Her AKTİF kaynak bir bölüme atanmış.
- [ ] `OKUMA_RAPORU.md` tüm sources listelenerek tamamlanmış.
- [ ] Demir Kurallar uygulanmış — okunmamış atıf yok.

Do not proceed to Phase 3 until every AKTİF source has a note file and a section assignment.

Her AKTİF kaynak için bir not dosyası ve bölüm ataması olmadan Aşama 3'e geçme.
