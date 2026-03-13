---
title: "Template — _notlar.md (Phase 3 / 6 Reading Notes)"
title_tr: "Şablon — _notlar.md (Faz 3 / 6 Okuma Notları)"
node_type: template
produces_file: _notlar.md
associated_phase: 3
description: "Standardized reading notes file. One file per section or source group. Each note entry includes target section and research question fields to directly connect reading to writing."
description_tr: "Standart okuma notları dosyası. Bölüm veya kaynak grubu başına bir dosya. Sayfa numaralı doğrudan alıntı adayları, parafraz argümanları, kartopu keşfedilen referanslar ve yazım planı içerir."
tags: [template, phase-3, phase-6, reading-notes, writing-plan, snowball]
links_to:
  - skills/phases/thesis/phase-3-reading.md
  - skills/phases/thesis/phase-6-writing.md
  - skills/techniques/snowball-sampling.md
  - skills/techniques/critical-reading.md
used_by:
  - skills/phases/thesis/phase-3-reading.md
  - skills/phases/thesis/phase-6-writing.md
  - skills/techniques/pdf-reading.md
language: bilingual
version: "2.4"
---

# Şablon: _notlar.md

Bu dosya kök dizinde değil, `notlar/` klasörü altında oluşturulmalıdır.
Örnek: `notlar/BIS_2020_CBDC_Foundational_Principles_Core_Features_notlar.md`

Tamamlanma kriteri zorunludur. Bir dosya "✅ TAMAMLANDI" olmadan önce:
- En az 2 doğrudan alıntı adayı (sayfa numaralı)
- En az 3 parafraz argümanı (sayfa numaralı)
- En az 1 kartopu keşfi kaydı
- Eleştirel değerlendirme alanlarının tamamı
- Yazım planı 5 adımın tamamı

```markdown
# Kaynak Notları: [Alt Bölüm Adı]

> Hazırlanma tarihi: [tarih]
> Okunan PDF sayısı: [X]
> Toplam not sayısı: [X]

## Tamamlanma Kontrol Listesi
- [ ] En az 2 doğrudan alıntı adayı var
- [ ] En az 3 parafraz argümanı var
- [ ] En az 1 kartopu keşfi kaydı var
- [ ] Eleştirel değerlendirme alanları tam dolu
- [ ] Yazım planındaki 5 adım dolu

## Kaynak 1: [Yazar, Kısa Başlık, Yıl]
**PDF:** [dosya_adi.pdf]
**Kalite:** [hakemli makale / kitap / rapor / çalışma kağıdı]
**Hedef bölüm:** [X.Y — hangi alt bölümde kullanılacak]
**Araştırma sorusu:** [RQ1 / RQ2 / RQ3 — hangi soruyu yanıtlıyor]

### Doğrudan alıntı adayları (sayfa numaralı)
<!-- ATİF TÜRÜ: BİRİNCİL = bu kaynağın kendi ifadesi
               İKİNCİL  = kaynak başka birinden aktarıyor → tam arama zinciri otomatik başlar
               İKİNCİL durumunda bu satır, zincir tamamlanıp birincil PDF elde edilince BİRİNCİL'e dönüşür.
               Zincir sonuç vermezse bu alıntı satırı silinir, argüman başka kaynakla kurulur. -->
- s.46: "Exact quote here..." — Hedef: [X.Y] — RQ: [RQ1] — ATİF: BİRİNCİL
- s.112: "Another quote..." — Hedef: [X.Y] — RQ: [RQ2] — ATİF: İKİNCİL → birincil: [Yazar Yıl] → ARANACAK

### Parafraz için ana argümanlar (sayfa numaralı)
- s.23-25: [argüman açıklaması — orijinal sözcükleri değil]
- s.78: [argüman açıklaması]

### Keşfedilen yeni referanslar (KARTOPU)
- s.45: Knapp (1905) Staatliche Theorie des Geldes → /sources/'da [VAR/YOK]
- s.67: Menger (1892) → /sources/'da [VAR/YOK] → [İNDİRİLECEK]

### Eleştirel Değerlendirme
- Bu kaynakla: [ ] Hemfikirim [ ] Kısmen hemfikirim [ ] Değilim
- Gerekçe: [Neden? — 1-2 cümle]
- Metodolojik güç: [Ne iyi yapılmış?]
- Metodolojik zayıflık / önyargı: [Nerede yetersiz veya taraflı?]
- Tezimde nasıl konumlandıracağım: [ ] Destek [ ] Karşı argüman [ ] Arka plan [ ] Çürütülecek

### Diğer sourcesla bağlantılar
- Bu kaynak s.45 argümanı ↔ Şu kaynak s.12: [bağlantı açıklaması]

---

## Kaynak 2: [Yazar, Kısa Başlık, Yıl]
[aynı yapı — Eleştirel Değerlendirme dahil]

---

## Yazım Planı
Bu notlara dayanarak alt bölümün paragraf sırası:
1. Giriş paragrafı: [hangi sourcesdan, hangi sayfalardan]
2. Ana argüman 1: [kaynak, sayfa]
3. Ana argüman 2: [kaynak, sayfa]
4. Sentez/yorum paragrafı: [hangi sources birleştirilecek]
5. Geçiş paragrafı: [sonraki bölüme bağlantı]
```

---

## ✅ OKUNDU Kısaltılmış Şablon

Bu şablon ⭐ AKTİF değil, ✅ OKUNDU seviyesindeki sources için kullanılır.
Tamamlanma kriteri: Anahtar cümle + 1 alıntı + 1 parafraz + eleştiri notu.

```markdown
# Kaynak Notları (OKUNDU): [Yazar, Kısa Başlık, Yıl]

> Hazırlanma tarihi: [tarih]
> Seviye: ✅ OKUNDU
> Kanıt türü: [HUKUK / VERİ / TEORİ / MODEL / ELEŞTİRİ]
> İlgili RQ: [RQ1 / RQ2 / ...]

## Anahtar Cümle (ZORUNLU — Gemini uyarısı)
"Bu kaynağı okudum çünkü [X]. Doğrudan atıf gitmiyor çünkü [Y]."
<!-- Örnek: "Bu kaynağı okudum çünkü KVKK genel çerçevesini anlamak gerekiyordu.
     Doğrudan atıf gitmiyor çünkü KVKK_2024_Bankacilik kaynağı DTL'ye özgün boşlukları
     daha güçlü işliyor." -->

## Doğrudan alıntı adayı (1 adet)
- s.XX: "..." — Bağlam: [neden önemli]

## Parafraz argümanı (1 adet)
- s.XX-XX: [argüman özeti]

## Eleştiri notu
- Güçlü yön: [kısa]
- Zayıf yön / önyargı: [kısa]
- Tezdeki konumu: [ ] Arka plan [ ] Karşı argüman [ ] Metodolojik bağlam

## Terfi Notu
<!-- Faz 6 başında bu not okunur. Eğer yazılan bölümde bu kaynağa ihtiyaç doğarsa
     AKTİF'e terfi et ve tam şablonu doldur. -->
- Terfi koşulu: [hangi durumda AKTİF'e çıkar?]
```
