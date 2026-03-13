---
title: "Phase 0 — Review Protocol"
title_tr: "Aşama 0 — İnceleme Protokolü"
node_type: phase
phase_number: 0
document_type: lit-review
phase_gate_in: null
phase_gate_out: "phase-1-search.md"
description: "Define the research question, scope, databases, and search strings before any searching begins. The protocol must be specific enough that a second researcher could replicate the entire search independently."
description_tr: "Herhangi bir arama başlamadan önce araştırma sorusunu, kapsamı, veritabanlarını ve arama dizelerini tanımlayın. Protokol, ikinci bir araştırmacının aramayı bağımsız olarak kopyalayabileceği kadar ayrıntılı olmalıdır."
tags: [phase, lit-review, protocol, PRISMA, research-question]
outputs:
  - "review_protocol.md"
  - "PRISMA_flow_initialized.md"
links_to:
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Phase 0 — Review Protocol
# Aşama 0 — İnceleme Protokolü

## Gate Rule / Geçiş Kuralı

**EN:** Do not execute any database searches until this protocol is approved and locked. Changes after searching begins invalidate reproducibility.

**TR:** Bu protokol onaylanıp kilitlenmeden hiçbir veritabanı araması yapmayın. Aramalar başladıktan sonra yapılan değişiklikler tekrarlanabilirliği geçersiz kılar.

---

## 1. Research Question / Araştırma Sorusu

**EN:** State the primary research question in one sentence. If secondary questions exist, list them below the primary. Use PICO (Population, Intervention, Comparison, Outcome) or SPIDER (Sample, Phenomenon of Interest, Design, Evaluation, Research type) where applicable.

**TR:** Birincil araştırma sorusunu tek cümlede ifade edin. İkincil sorular varsa birincil sorunun altında listeleyin. Uygulanabilir durumlarda PICO veya SPIDER çerçevesini kullanın.

```
Primary question / Birincil soru:
[Write here / Buraya yazın]

PICO/SPIDER breakdown / Döküm:
P/S:
I/PI:
C/D:
O/E:
  /R:
```

---

## 2. Inclusion & Exclusion Criteria / Dahil Etme ve Dışlama Kriterleri

**EN:** Define criteria before searching. Every criterion must be testable — a second reviewer must reach the same decision given the same record.

**TR:** Arama başlamadan kriterleri tanımlayın. Her kriter sınanabilir olmalıdır — ikinci bir gözlemci aynı kayıt verildiğinde aynı karara ulaşabilmelidir.

| Criterion / Kriter | Include / Dahil Et | Exclude / Dışla |
|--------------------|-------------------|-----------------|
| Publication years / Yayın yılları | | |
| Languages / Diller | | |
| Study types / Çalışma türleri | | |
| Population / Popülasyon | | |
| Geographic scope / Coğrafi kapsam | | |
| Quality threshold / Kalite eşiği | | |

---

## 3. Database List / Veritabanı Listesi

**EN:** List every database to be searched. For each, note access level and any platform-specific syntax differences.

**TR:** Aranacak her veritabanını listeleyin. Her biri için erişim düzeyini ve platforma özgü sözdizimi farklarını not edin.

- [ ] Scopus
- [ ] Web of Science (WoS)
- [ ] PubMed / MEDLINE
- [ ] PsycINFO
- [ ] ERIC (education)
- [ ] IEEE Xplore (engineering/CS)
- [ ] Other / Diğer: ___________

---

## 4. Boolean Search Strings / Boolean Arama Dizeleri

**EN:** Write a complete, executable search string for each database. Record field codes (e.g., TITLE-ABS-KEY in Scopus vs TS= in WoS). Do not start searches until all strings are written and reviewed.

**TR:** Her veritabanı için eksiksiz, çalıştırılabilir bir arama dizesi yazın. Alan kodlarını kaydedin (örn. Scopus'ta TITLE-ABS-KEY, WoS'ta TS=). Tüm dizeler yazılıp gözden geçirilene kadar aramaları başlatmayın.

```
Scopus:
TITLE-ABS-KEY([terms here])

WoS:
TS=([terms here])

PubMed:
([MeSH terms]) AND ([free text])
```

---

## 5. PRISMA Flow — Initial Template / PRISMA Akışı — Başlangıç Şablonu

**EN:** Initialize the PRISMA diagram with placeholders. Numbers are filled in during Phases 1–2.

**TR:** PRISMA diyagramını yer tutucularla başlatın. Sayılar Aşama 1–2'de doldurulur.

```
Records identified / Tanımlanan kayıtlar: N = ___
After deduplication / Tekilleştirme sonrası: N = ___
Screened (title/abstract) / Taranmış (başlık/özet): N = ___
Excluded / Dışlanan: N = ___
Full-text assessed / Tam metin değerlendirilen: N = ___
Full-text excluded (with reasons) / Dışlanan (gerekçeli): N = ___
Included in review / İncelemeye dahil edilen: N = ___
```

---

## Registration / Kayıt (Optional but Recommended)

**PROSPERO Registration** (for systematic reviews of health/social care topics):
- Register at: https://www.crd.york.ac.uk/prospero/
- Register BEFORE starting the search (pre-registration = transparency)
- Include your PROSPERO ID in the final manuscript

**Review Type Selection:**
- Standard systematic review → use PRISMA checklist
- Scoping review → use PRISMA-ScR checklist (Tricco et al. 2018)
- Meta-analysis (quantitative synthesis) → additional phases needed: effect size extraction, heterogeneity testing (I², forest plot)
- Umbrella review (review of reviews) → special inclusion criteria apply

Note: If meta-analysis is planned, add Phase 3b: Statistical Synthesis between Data Extraction and Synthesis.

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] Research question is answerable within scope / Araştırma sorusu kapsam içinde yanıtlanabilir
- [ ] All criteria are independently testable / Tüm kriterler bağımsız olarak sınanabilir
- [ ] All databases listed with access confirmed / Tüm veritabanları listelendi, erişim doğrulandı
- [ ] Search strings written for every database / Her veritabanı için arama dizesi yazıldı
- [ ] PRISMA template initialized / PRISMA şablonu başlatıldı
- [ ] A second researcher could replicate without asking questions / İkinci araştırmacı soru sormadan kopyalayabilir

**Gate out:** → phase-1-search.md
