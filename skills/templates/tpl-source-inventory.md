---
title: "Template — KAYNAK_ENVANTERI.md (Phase 2 Output)"
title_tr: "Şablon — KAYNAK_ENVANTERI.md (Faz 2 Çıktısı)"
node_type: template
produces_file: KAYNAK_ENVANTERI.md
associated_phase: 2
description: "Source inventory file created at end of Phase 2 and updated throughout Phases 3 and 6. Tracks all downloaded PDFs by category with diversity metrics."
description_tr: "Faz 2 sonunda oluşturulan ve Faz 3 ile 6 boyunca güncellenen kaynak envanter dosyası. Çeşitlilik metrikleriyle kategoriye göre indirilen tüm PDF'leri izler."
tags: [template, phase-2, source-inventory, diversity-metrics]
links_to:
  - skills/phases/thesis/phase-2-sources.md
  - skills/phases/thesis/phase-3-reading.md
used_by:
  - skills/phases/thesis/phase-2-sources.md
  - skills/phases/thesis/phase-3-reading.md
language: bilingual
version: "2.1"
---

# Şablon: KAYNAK_ENVANTERI.md

```markdown
# Kaynak Envanteri

> Son güncelleme: [tarih]
> Toplam kaynak: [X]
> Konum: /sources/

## Kategori 1: [Kategori Adı]
**Tez bağlantısı:** [hangi bölüm/araştırma sorusuyla ilgili]
- `Yazar_Yıl_Kısa_Başlık.pdf` — [kısa açıklama]
- `Yazar_Yıl_Kısa_Başlık.pdf` — [kısa açıklama]

## Kategori 2: [Kategori Adı]
...

## Çeşitlilik Metrikleri
- Dil dağılımı: TR %X / EN %X / Diğer %X
- Tarih dağılımı: Klasik (pre-2000) %X / 2000-2020 %X / 2020+ %X
- Tür dağılımı: Kitap %X / Makale %X / Rapor %X / Tez %X
- Yazar yoğunluğu: En çok atıf: [Yazar X] ([N]), [Yazar Y] ([N])

## Bekleyen İndirmeler
- [ ] `Yazar_Yıl_Başlık.pdf` — [link]
- [ ] `Yazar_Yıl_Başlık.pdf` — [link]

## Dosya Adı Normalizasyon Kayıtları
- `Eski_Dosya_Adi.pdf` → `Yeni_Dosya_Adi.pdf`
- `Eski_Dosya_Adi_2.pdf` → `Yeni_Dosya_Adi_2.pdf`
```
