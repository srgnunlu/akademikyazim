---
title: "Phase 1 — Literature Positioning"
title_tr: "Aşama 1 — Literatür Konumlandırması"
node_type: phase
phase_number: 1
document_type: article
phase_gate_in: "phase-0-claim.md"
phase_gate_out: "phase-2-reading.md"
description: "Find 30-60 directly relevant sources, identify the most cited works in this niche, and produce a structured map of what has been done and what has not."
description_tr: "30-60 doğrudan ilgili kaynak bul, bu nişte en çok atıf alan çalışmaları belirle ve neyin yapıldığı ile yapılmadığının yapısal haritasını çıkar."
tags: [phase, article, literature, positioning, gap-analysis]
outputs:
  - "lit_position.md (table: topic → key papers → gap)"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/core/source-policy.md
language: bilingual
version: "1.0"
---

# Phase 1 — Literature Positioning / Literatür Konumlandırması

## Purpose / Amaç

Articles do not require exhaustive literature coverage — they require focused, authoritative coverage of the specific niche. This phase builds a precise map of the field around your contribution claim. Every source added must pass the relevance test: does it directly inform, support, or challenge the claim from Phase 0?

Makaleler kapsamlı literatür taraması gerektirmez — spesifik niş üzerinde odaklanmış, yetkili bir kapsam gerektirir. Bu aşama, katkı iddiandın etrafında kesin bir alan haritası oluşturur. Eklenen her kaynak alaka testini geçmeli: Aşama 0'daki iddiayı doğrudan destekliyor, bilgilendiriyor veya zorluyor mu?

---

## Step 1 — Define Search Scope / Arama Kapsamını Belirle

From `claim_statement.md`, extract 5-10 key terms and phrases. These drive your search.

`claim_statement.md` dosyasından 5-10 anahtar terim ve ifade çıkar. Bunlar aramanı yönlendiriyor.

Search databases: Web of Science, Scopus, Google Scholar, domain-specific databases (ACM DL, PubMed, IEEE Xplore, etc.). Use at least two databases.

Veritabanlarını tara: Web of Science, Scopus, Google Scholar, alana özgü veritabanları. En az iki veritabanı kullan.

---

## Step 2 — Collect 30-60 Candidate Sources / 30-60 Aday Kaynak Topla

Target range is 30-60. Fewer than 30 suggests under-coverage; more than 60 suggests scope creep — your claim may be too broad.

Hedef aralık 30-60. 30'dan az yetersiz kapsam; 60'tan fazla kapsam kayması anlamına gelir — iddiandan çok geniş olabilir.

For each source, record immediately:
- Full citation (do not defer this)
- One sentence: what does this paper do?
- One word: how does it relate to your claim? (supports / challenges / background / method)

Her kaynak için hemen kaydet:
- Tam atıf (bunu erteleme)
- Bir cümle: bu makale ne yapıyor?
- Bir kelime: iddiannla nasıl ilişkili? (destekler / zorlar / arka plan / yöntem)

---

## Step 3 — Identify the 3-5 Most Cited Works / En Çok Atıf Alan 3-5 Çalışmayı Belirle

These are the works that define the conversation you are entering. Every reader of your target journal knows them. You must cite them and position your work relative to them.

Bunlar girdiğin konuşmayı tanımlayan çalışmalardır. Hedef derginin her okuyucusu onları bilir. Onları mutlaka atıf yapmalı ve çalışmandı bunlara göre konumlandırmalısın.

For each of the 3-5 landmark works:
- Why is it central to this niche?
- What does your article do that this work does not?
- Is your claim compatible with it, or does it contradict it?

3-5 temel çalışmanın her biri için:
- Neden bu niş için merkezi?
- Makalenin bu çalışmanın yapmadığı nesi var?
- İddiandır bununla uyumlu mu, yoksa çelişiyor mu?

---

## Step 4 — Map What Has Been Done and What Has Not / Yapılanları ve Yapılmayanları Haritalandır

Create a structured table — this becomes the core of `lit_position.md`.

Yapılandırılmış bir tablo oluştur — bu `lit_position.md` dosyasının özü olur.

| Topic / Sub-claim | Key Papers | What They Cover | What They Leave Open |
|---|---|---|---|
| [topic 1] | [Author, Year; Author, Year] | [what is covered] | [the gap] |
| [topic 2] | ... | ... | ... |

The "What They Leave Open" column must connect directly to your contribution claim. If a row's gap does not connect to your claim, that row belongs in background — not in the positioning table.

"Ne Bıraktıkları Açık" sütunu doğrudan katkı iddiandıra bağlanmalı. Bir satırın boşluğu iddiandıra bağlanmıyorsa, o satır arka plana aittir — konumlandırma tablosuna değil.

---

## Step 5 — Document the Gap with Evidence / Boşluğu Kanıtla Belgele

Summarize in 1-2 paragraphs: here is what the literature does, and here is what it does not do. The gap is not assumed — it is demonstrated by the absence of specific papers.

1-2 paragrafta özetle: literatür şunu yapıyor, şunu yapmıyor. Boşluk varsayılmaz — belirli makalelerin yokluğuyla gösterilir.

If you searched thoroughly and found papers that already make your claim, return to Phase 0 and revise the claim.

Kapsamlı arama yapıp iddiandı zaten yapan makaleler bulduysan, Aşama 0'a dön ve iddiayı revize et.

---

## Output / Çıktı

Create `lit_position.md` containing:
1. Search terms and databases used
2. The structured topic → key papers → gap table
3. Landmark works summary (3-5 entries)
4. Gap summary paragraph (evidence-based, not assumed)
5. Full reference list (30-60 entries, properly formatted for target journal)

`lit_position.md` oluştur:
1. Kullanılan arama terimleri ve veritabanları
2. Yapılandırılmış konu → temel makaleler → boşluk tablosu
3. Temel çalışmalar özeti (3-5 giriş)
4. Boşluk özet paragrafı (kanıta dayalı, varsayımsal değil)
5. Tam referans listesi (30-60 giriş, hedef dergi formatında)

---

## Completion Criteria / Tamamlanma Kriterleri

- [ ] 30-60 sources collected with full citations.
- [ ] 3-5 landmark works identified and analyzed.
- [ ] Structured topic/gap table completed.
- [ ] Gap is documented with evidence (not assumed).
- [ ] Every source in the list connects to the contribution claim.
- [ ] `lit_position.md` is written and saved.

- [ ] Tam atıflarla 30-60 kaynak toplanmış.
- [ ] 3-5 temel çalışma belirlenmiş ve analiz edilmiş.
- [ ] Yapılandırılmış konu/boşluk tablosu tamamlanmış.
- [ ] Boşluk kanıtla belgelenmiş (varsayılmamış).
- [ ] Listedeki her kaynak katkı iddiasıyla bağlantılı.
- [ ] `lit_position.md` yazılmış ve kaydedilmiş.

Do not proceed to Phase 2 until the gap is documented — not assumed.

Boşluk belgelenmeden — varsayılmadan — Aşama 2'ye geçme.
