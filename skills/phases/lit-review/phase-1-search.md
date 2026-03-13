---
title: "Phase 1 — Systematic Search"
title_tr: "Aşama 1 — Sistematik Arama"
node_type: phase
phase_number: 1
document_type: lit-review
phase_gate_in: "phase-0-protocol.md"
phase_gate_out: "phase-2-screening.md"
description: "Execute the searches defined in the protocol, record exact query strings and hit counts for each database, deduplicate results, and export to a reference manager. Every search action must be logged for reproducibility."
description_tr: "Protokolde tanımlanan aramaları yürütün, her veritabanı için tam sorgu dizelerini ve isabet sayılarını kaydedin, sonuçları tekilleştirin ve referans yöneticisine aktarın. Her arama eylemi tekrarlanabilirlik için günlüğe kaydedilmelidir."
tags: [phase, lit-review, search, deduplication, reproducibility]
outputs:
  - "search_log.md"
  - "deduplicated_results.csv"
links_to:
  - skills/core/iron-rules.md
  - skills/core/agent-orchestration.md
  - skills/phases/lit-review/phase-0-protocol.md
language: bilingual
version: "1.0"
---

# Phase 1 — Systematic Search
# Aşama 1 — Sistematik Arama

## Gate Rule / Geçiş Kuralı

**EN:** Phase 0 protocol must be locked before executing any searches. Do not modify inclusion/exclusion criteria after searches begin.

**TR:** Herhangi bir arama yürütmeden önce Aşama 0 protokolü kilitlenmiş olmalıdır. Aramalar başladıktan sonra dahil etme/dışlama kriterlerini değiştirmeyin.

---

## 1. Pre-Search Checklist / Arama Öncesi Kontrol Listesi

**EN:** Confirm before running any query:

**TR:** Herhangi bir sorgu çalıştırmadan önce doğrulayın:

- [ ] Protocol (Phase 0) is locked and dated / Protokol kilitli ve tarihli
- [ ] Access to all listed databases confirmed / Tüm veritabanlarına erişim doğrulandı
- [ ] Search strings copied exactly from protocol / Arama dizeleri protokolden olduğu gibi kopyalandı
- [ ] Reference manager ready to receive exports / Referans yöneticisi dışa aktarımları almaya hazır

---

## 2. Executing Searches / Aramaları Yürütme

**EN:** Run each database search exactly as specified in the protocol. For each search, record immediately:
- Database name and platform URL
- Exact query string used (copy-paste, no paraphrase)
- Date and time of search
- Total hit count before any filters
- Hit count after date/language filters
- Export format used (RIS, CSV, BibTeX)

**TR:** Her veritabanı aramasını protokolde belirtildiği gibi tam olarak çalıştırın. Her arama için hemen kaydedin:
- Veritabanı adı ve platform URL'si
- Kullanılan tam sorgu dizesi (kopyala-yapıştır, parafraz yok)
- Arama tarihi ve saati
- Herhangi bir filtre uygulanmadan önce toplam isabet sayısı
- Tarih/dil filtreleri sonrası isabet sayısı
- Kullanılan dışa aktarma biçimi (RIS, CSV, BibTeX)

---

## 3. Search Log Template / Arama Günlüğü Şablonu

**EN:** One row per database. This becomes search_log.md.

**TR:** Veritabanı başına bir satır. Bu, search_log.md olur.

```markdown
## Search Log / Arama Günlüğü

| Database | Query String | Date | Raw Hits | Filtered Hits | Export Format |
|----------|-------------|------|----------|---------------|---------------|
| Scopus | TITLE-ABS-KEY(...) | YYYY-MM-DD | N | N | RIS |
| WoS | TS=(...) | YYYY-MM-DD | N | N | RIS |
| PubMed | (...) | YYYY-MM-DD | N | N | CSV |
```

---

## 4. Deduplication / Tekilleştirme

**EN:** After collecting all exports, deduplicate across databases. Duplicates arise when the same article is indexed in multiple databases. Use your reference manager's built-in deduplication tool first, then manually check borderline cases (same authors, similar titles, slight date differences).

**TR:** Tüm dışa aktarmaları topladıktan sonra veritabanları arasında tekilleştirin. Aynı makale birden fazla veritabanında dizinlendiğinde kopyalar ortaya çıkar. Önce referans yöneticinizin yerleşik tekilleştirme aracını kullanın, ardından sınır vakaları manuel olarak kontrol edin.

**Deduplication record / Tekilleştirme kaydı:**

```
Total records before deduplication / Tekilleştirme öncesi toplam: N = ___
Duplicates removed / Kaldırılan kopyalar: N = ___
Records after deduplication / Tekilleştirme sonrası kayıtlar: N = ___
```

---

## 5. Export to Reference Manager / Referans Yöneticisine Aktarma

**EN:** Export the deduplicated set as a CSV or RIS file compatible with Zotero, Mendeley, or your chosen tool. Ensure the following fields are present for every record:
- Authors, Title, Year, Journal/Source, Abstract, DOI/URL, Database of origin

**TR:** Tekilleştirilmiş seti Zotero, Mendeley veya seçtiğiniz araçla uyumlu CSV veya RIS dosyası olarak dışa aktarın. Her kayıt için şu alanların mevcut olduğundan emin olun:
- Yazarlar, Başlık, Yıl, Dergi/Kaynak, Özet, DOI/URL, Kaynak veritabanı

---

## 6. Outputs / Çıktılar

**EN:** This phase produces two files that feed directly into Phase 2.

**TR:** Bu aşama doğrudan Aşama 2'ye aktarılan iki dosya üretir.

- **search_log.md** — query strings, dates, hit counts for all databases
- **deduplicated_results.csv** — clean record set ready for screening

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] All databases from protocol searched / Protokoldeki tüm veritabanları arandı
- [ ] Each search logged with date, query, and hit count / Her arama tarih, sorgu ve isabet sayısıyla günlüğe kaydedildi
- [ ] Deduplication completed and count recorded / Tekilleştirme tamamlandı ve sayı kaydedildi
- [ ] deduplicated_results.csv exported and accessible / deduplicated_results.csv dışa aktarıldı ve erişilebilir
- [ ] PRISMA numbers updated (identified, after deduplication) / PRISMA sayıları güncellendi

**Gate in:** phase-0-protocol.md
**Gate out:** → phase-2-screening.md
