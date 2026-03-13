---
title: "Şablon — YÖK Kapak ve Ön Sayfalar"
title_en: "Template — YÖK Cover and Front Pages"
node_type: template
description: "YÖK uyumlu kapak sayfası, jüri onay sayfası, etik beyan ve özet şablonları. Üniversite kılavuzu ile doğrula."
description_en: "YÖK-compliant cover page, jury approval, ethics declaration, and abstract templates. Verify against your university guide."
tags: [template, yok, cover, formatting, turkish-universities]
links_to:
  - skills/disciplines/yok-compliance.md
language: bilingual
version: "1.0"
---

# YÖK Ön Sayfa Şablonları

Aşağıdaki şablonları kopyala, köşeli parantez içindeki alanları doldur, üniversitenin özel kılavuzuyla karşılaştır.

---

## 1. İÇ KAPAK SAYFASI

```
[ÜNİVERSİTE ADI]
[ENSTİTÜ ADI]
[ANABİLİM DALI]


[TEZ BAŞLIĞI]
(Büyük Harf, Koyu, Ortalı)


[TÜR] TEZİ
(YÜKSEK LİSANS / DOKTORA)


Hazırlayan
[ÖĞRENCİNİN ADI SOYADI]
[ÖĞRENCİ NO]


Danışman
[UNVAN AD SOYAD]
[ÜNİVERSİTE/BÖLÜM]


[ŞEHİR], [YIL]
```

---

## 2. JÜRİ ONAY SAYFASI

```
[ÜNİVERSİTE ADI]
[ENSTİTÜ ADI]

[TEZ BAŞLIĞI]

[ÖĞRENCİNİN ADI SOYADI] tarafından hazırlanan bu tez,
[TARİH] tarihinde aşağıdaki jüri üyeleri tarafından
[YÜKSEK LİSANS / DOKTORA] tezi olarak kabul edilmiştir.


JÜRİ ÜYELERİ

Danışman : [UNVAN AD SOYAD]        İmza: ___________
           [Üniversite, Bölüm]

Üye       : [UNVAN AD SOYAD]        İmza: ___________
           [Üniversite, Bölüm]

Üye       : [UNVAN AD SOYAD]        İmza: ___________
           [Üniversite, Bölüm]

[Doktora için ek 2 üye:]
Üye       : [UNVAN AD SOYAD]        İmza: ___________
Üye       : [UNVAN AD SOYAD]        İmza: ___________


Enstitü Müdürü
[UNVAN AD SOYAD]                    İmza: ___________
```

---

## 3. ETİK BEYAN SAYFASI (YÖK 2020+ Zorunlu)

```
ETİK BEYAN

Bu tezin hazırlanmasında bilimsel etiğe ve akademik kurallara özenle
uyulduğunu, tez içindeki bütün bilgilerin etik davranış ve akademik
kurallara uygun olarak elde edilerek sunulduğunu, ayrıca tez yazım
kurallarına uygun olarak hazırlanan bu çalışmada başkalarının
eserlerinden yararlanılması durumunda bilimsel kurallara uygun olarak
atıf yapıldığını bildiririm.

                                    [İMZA]
                          [AD SOYAD]
                          [TARİH]


[Varsa: Bu tez [ETİK KURUL ADI] tarafından [KARAR NO] sayılı ve
[TARİH] tarihli kararı ile etik açıdan uygun bulunmuştur.]
```

---

## 4. TÜRKÇE ÖZET (150–350 Kelime)

```
ÖZET

[TEZ BAŞLIĞI]

[AD SOYAD]
[TÜR] Tezi, [ANABİLİM DALI]
Danışman: [UNVAN AD SOYAD]
[YIL], [TOPLAM SAYFA] sayfa

─────────────────────────────────────────────────────────────────

[Araştırmanın amacı. 1-2 cümle.]

[Yöntem. Tasarım, örneklem/veri, analiz tekniği. 2-3 cümle.]

[Ana bulgular. En önemli 3-5 bulgu. 3-4 cümle.]

[Sonuç ve katkı. Alana özgü önemi, sınırlılıklar, gelecek
araştırma önerileri. 2-3 cümle.]

─────────────────────────────────────────────────────────────────
Anahtar Kelimeler: [kelime1], [kelime2], [kelime3], [kelime4], [kelime5]
```

**Özet yazım kuralları:**
- İlk satır girinti YOK
- Tüm paragraflar arasında boşluk YOK (tek blok)
- Kısaltmalar açılımıyla birlikte
- Atıf YOK — özet bağımsız bir metin
- Tablo/şekil referansı YOK

---

## 5. İNGİLİZCE ABSTRACT (150–350 Kelime)

```
ABSTRACT

[TEZ BAŞLIĞI İNGİLİZCE]

[AD SOYAD]
[TÜR in English] Thesis, [DEPARTMENT in English]
Supervisor: [TITLE NAME SURNAME]
[YEAR], [TOTAL PAGES] pages

─────────────────────────────────────────────────────────────────

[Purpose of the study. 1-2 sentences.]

[Methods. Design, sample/data, analysis technique. 2-3 sentences.]

[Main findings. 3-5 most important findings. 3-4 sentences.]

[Conclusion and contribution. Significance, limitations, future
research. 2-3 sentences.]

─────────────────────────────────────────────────────────────────
Keywords: [keyword1], [keyword2], [keyword3], [keyword4], [keyword5]
```

---

## Üniversite Özel Kontroller

Yukarıdaki şablonu kullanmadan önce kontrol et:

| Üniversite | Özel Gereksinim |
|------------|-----------------|
| ODTÜ | Kapak sayfasında üniversite logosu zorunlu; METU English kapak da eklenir |
| İTÜ | Kapak rengi tür'e göre (bkz. `yok-compliance.md`); logo sol üst |
| Boğaziçi | Tez İngilizce ise kapak İngilizce; Türkçe özet ayrı eklenir |
| Hacettepe | Etik kurul kararı fotokopisi ekler bölümüne |
| Ankara | Sol kenar 4 cm; jüri imza satırı daha geniş |

Üniversite kılavuzu bulunamazsa: danışmanından son 2 yılda kabul edilmiş bir tezi referans olarak iste.
