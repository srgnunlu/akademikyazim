---
title: "Phase 3 — Data Extraction"
title_tr: "Aşama 3 — Veri Çıkarma"
node_type: phase
phase_number: 3
document_type: lit-review
phase_gate_in: "phase-2-screening.md"
phase_gate_out: "phase-4-synthesis.md"
description: "Standardized extraction of key data from each included study using a consistent form. Includes quality assessment with a tool appropriate to the review type. Produces the extraction table that feeds directly into synthesis."
description_tr: "Tutarlı bir form kullanarak dahil edilen her çalışmadan temel verilerin standartlaştırılmış olarak çıkarılması. İnceleme türüne uygun bir araçla kalite değerlendirmesini içerir. Doğrudan senteze aktarılan çıkarma tablosunu üretir."
tags: [phase, lit-review, extraction, quality-assessment, CASP, RoB2, GRADE]
outputs:
  - "extraction_table.md"
links_to:
  - skills/core/iron-rules.md
  - skills/phases/lit-review/phase-2-screening.md
language: bilingual
version: "1.0"
---

# Phase 3 — Data Extraction
# Aşama 3 — Veri Çıkarma

## Gate Rule / Geçiş Kuralı

**EN:** Extract only from the included set finalized in Phase 2. Do not add or remove studies here. If a previously excluded study seems relevant, return to Phase 2, document the change, and update PRISMA counts.

**TR:** Yalnızca Aşama 2'de kesinleştirilen dahil edilen setten çıkarın. Burada çalışma eklemeyin veya çıkarmayın. Daha önce dışlanan bir çalışma ilgili görünüyorsa Aşama 2'ye dönün, değişikliği belgeleyin ve PRISMA sayılarını güncelleyin.

---

## 1. Extraction Form / Çıkarma Formu

**EN:** Complete one form per included study. Consistency is critical — use the same level of detail for every study regardless of how well it aligns with your thesis.

**TR:** Dahil edilen her çalışma için bir form doldurun. Tutarlılık kritiktir — her çalışma için, sizin tezinizle ne kadar uyumlu olduğundan bağımsız olarak aynı ayrıntı düzeyini kullanın.

```markdown
### Study ID: ___
**Authors / Yazarlar:**
**Year / Yıl:**
**Title / Başlık:**
**Journal/Source / Dergi/Kaynak:**
**DOI:**

**Study Design / Çalışma Tasarımı:**
(RCT, cohort, cross-sectional, qualitative, mixed-methods, etc.)

**Sample / Örneklem:**
- Size / Büyüklük: N = ___
- Population / Popülasyon:
- Recruitment / İşe Alım:

**Intervention or Phenomenon / Müdahale veya Olgu:**

**Comparison (if applicable) / Karşılaştırma (varsa):**

**Outcome Measures / Sonuç Ölçümleri:**

**Key Findings / Temel Bulgular:**

**Limitations Reported by Authors / Yazarların Bildirdiği Sınırlılıklar:**

**Quality Score / Kalite Puanı:** ___ / ___ (tool: ___)

**Notes / Notlar:**
```

---

## 2. Quality Assessment / Kalite Değerlendirmesi

**EN:** Select the quality assessment tool appropriate to your review type. Apply it consistently to every included study. Record total score and domain-level scores where applicable.

**TR:** İnceleme türünüze uygun kalite değerlendirme aracını seçin. Dahil edilen her çalışmaya tutarlı biçimde uygulayın. Toplam puanı ve uygun durumlarda alan düzeyindeki puanları kaydedin.

**Tool selection guide / Araç seçim kılavuzu:**

| Review type / İnceleme türü | Tool / Araç |
|----------------------------|-------------|
| Systematic review of RCTs / RKD'lerin sistematik derlemesi | RoB2 (Cochrane) |
| Observational studies / Gözlemsel çalışmalar | ROBINS-I |
| Qualitative studies / Nitel çalışmalar | CASP Qualitative |
| Diagnostic accuracy / Tanısal doğruluk | QUADAS-2 |
| Mixed / Karma | Appropriate per study design |
| Overall evidence body / Genel kanıt bütünü | GRADE |

---

## 3. Extraction Table Assembly / Çıkarma Tablosu Derleme

**EN:** After extracting all studies, compile into a single table sorted by year (oldest first). This is extraction_table.md and is the primary input to Phase 4.

**TR:** Tüm çalışmaları çıkardıktan sonra yıla göre sıralanmış (eskiden yeniye) tek bir tabloda derleyin. Bu extraction_table.md'dir ve Aşama 4'ün birincil girdisidir.

```markdown
## Extraction Table / Çıkarma Tablosu

| ID | Authors | Year | Design | N | Key Finding | Quality |
|----|---------|------|--------|---|-------------|---------|
| S01 | | | | | | |
| S02 | | | | | | |
```

---

## 4. Cross-Study Notes / Çalışmalar Arası Notlar

**EN:** As you extract, note patterns that will be relevant in Phase 4:
- Studies that measure the same outcome differently
- Studies with directly contradictory findings
- Studies with unusually high or low quality scores
- Methodological gaps (designs that are missing from the literature)

**TR:** Çıkarırken Aşama 4'te ilgili olacak örüntüleri not edin:
- Aynı sonucu farklı biçimde ölçen çalışmalar
- Doğrudan çelişkili bulgulara sahip çalışmalar
- Olağandışı yüksek veya düşük kalite puanlarına sahip çalışmalar
- Metodolojik boşluklar (literatürde eksik olan tasarımlar)

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] Every included study has a completed extraction form / Dahil edilen her çalışmanın tamamlanmış çıkarma formu var
- [ ] Quality assessment tool selected and applied consistently / Kalite değerlendirme aracı seçildi ve tutarlı biçimde uygulandı
- [ ] extraction_table.md compiled and sorted / extraction_table.md derlendi ve sıralandı
- [ ] Cross-study patterns noted / Çalışmalar arası örüntüler not edildi
- [ ] No studies added or removed relative to Phase 2 output / Aşama 2 çıktısına göre çalışma eklenmedi veya çıkarılmadı

**Gate in:** phase-2-screening.md
**Gate out:** → phase-4-synthesis.md
