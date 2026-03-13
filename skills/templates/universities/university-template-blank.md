---
title: "University Template — Blank / Boş Şablon"
title_tr: "Üniversite Şablonu — Boş"
node_type: template
description: "Blank university formatting template for institutions not yet in the TezAtlas database. Load this when the student's university is not listed, then populate from the university's official thesis writing guide."
description_tr: "TezAtlas veritabanında henüz bulunmayan kurumlar için boş üniversite format şablonu. Öğrencinin üniversitesi listede yoksa bunu yükle, ardından üniversitenin resmi tez yazım kılavuzundan doldur."
tags: [template, university, formatting, blank, custom]
links_to:
  - skills/moc/MOC-universities.md
language: bilingual
version: "1.0"
---

# University Template — Blank / Boş Üniversite Şablonu

Bu şablon desteklenmeyen üniversiteler için başlangıç noktasıdır. Üniversitenin resmi tez yazım kılavuzunu temin et ve aşağıdaki alanları doldur.

## Format Ayarları / Format Settings

Üniversitenin kılavuzundan aşağıdaki bilgileri topla ve `templates/universities/` altına yeni bir YAML dosyası oluştur:

| Alan | Değer | Kaynak |
|------|-------|--------|
| Kenar boşlukları (margin) | — | Kılavuz §... |
| Yazı tipi (font) | — | Kılavuz §... |
| Yazı boyutu (font size) | — | Kılavuz §... |
| Satır aralığı (line spacing) | — | Kılavuz §... |
| Paragraf girintisi | — | Kılavuz §... |
| Başlık formatları | — | Kılavuz §... |
| Dipnot boyutu | — | Kılavuz §... |
| Kaynakça stili | — | Kılavuz §... |
| İntihal aracı | — | Kılavuz §... |

## Ön Matter Sayfa Sırası / Front Matter Page Order

1. Kapak sayfası
2. İmza sayfası
3. Özet (TR)
4. Abstract (EN)
5. İçindekiler
6. Şekil listesi (varsa)
7. Tablo listesi (varsa)
8. Kısaltmalar (varsa)

Üniversiteye özgü sıralama için resmi kılavuzu kontrol et.

## Sonraki Adım / Next Step

Bilgileri topladıktan sonra `templates/universities/<universite-kisa-adi>.yaml` dosyası oluştur ve [[MOC-universities]] listesine ekle.
