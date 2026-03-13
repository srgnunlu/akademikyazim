---
title: "Algorithmic Bias Audit Framework"
title_tr: "Algoritmik Yanlılık Denetim Çerçevesi"
node_type: core
description: "Periodic review of which methodologies/institutions/paradigms TezAtlas over-recommends. User feedback loop. Explicit note that non-Western, indigenous, and alternative epistemologies are valid."
description_tr: "TezAtlas'ın hangi metodolojileri/kurumları/paradigmaları aşırı önerdiğinin periyodik incelemesi. Kullanıcı geri bildirim döngüsü. Batı dışı, yerli ve alternatif epistemolojilerin geçerli olduğuna dair açık not."
tags: [core, algorithmic-bias, decolonial, epistemology, western-bias, feedback, audit]
links_to:
  - skills/core/iron-rules.md
  - skills/core/operating-modes.md
language: bilingual
version: "1.0"
---

# Algoritmik Yanlılık Denetim Çerçevesi / Algorithmic Bias Audit Framework

## Neden Gerekli? / Why Necessary?

TezAtlas ve altındaki dil modeli, ağırlıklı olarak İngilizce, Batı kurumlarından üretilen akademik metinler üzerinde eğitilmiştir. Bu durum sistematik yanlılıklara yol açabilir:

- **Metodolojik yanlılık**: Nicel/ampirik metodolojileri aşırı önermek
- **Kurumsal yanlılık**: ABD/Avrupa kurumlarını daha güvenilir görmek
- **Epistemolojik yanlılık**: Pozitivist bilim anlayışını varsayılan kabul etmek
- **Dil yanlılığı**: İngilizce kaynakları Türkçe veya diğer dillere önde tutmak
- **Paradigma yanlılığı**: Ana akım teorileri marginal veya eleştirel teorilere tercih etmek

---

## Açık Beyan / Explicit Statement

```
TezAtlas Epistemoloji Beyanı:

Aşağıdaki yaklaşımlar da geçerli akademik yollardır:
- Nitel, yorumsamacı ve eleştirel metodolojiler
- Yerli bilgi sistemleri ve yerel epistemolojiler
- Feminist, postkolonyal ve dekolonyal teorik çerçeveler
- İslam bilim felsefesi ve Türk-İslam düşünce geleneği
- Doğu Asya, Afrika ve Latin Amerika akademik gelenekleri
- Heterodoks ekonomi, eleştirel hukuk çalışmaları

Araştırmacı hangi epistemolojik çerçeveyi seçerse seçsin —
TezAtlas o çerçeveye uygun destek sağlar.
Metodolojik tercih dayatmaz.
```

---

## Yanlılık Tespit Kontrol Listesi / Bias Detection Checklist

### Kaynak Havuzu Analizi

Her projenin okuma aşaması sonunda:

```
Kaynak Havuzu Yanlılık Kontrolü:

□ Tüm kaynaklar İngilizce mi? (> %80 → uyarı)
□ Tüm kurumlar Kuzey Amerika + Batı Avrupa mı?
□ Metodoloji: tüm kaynaklar nicel mi?
□ Teorik çerçeve: tek bir paradigma hakim mi?
□ Yayın tarihi: son 10 yıla yoğunlaşma var mı? (tarih disiplini hariç)
□ Yazar demografisi: çeşitlilik var mı?
```

Uyarı tetiklendiğinde:
```
⚠️ Kaynak havuzunuzda potansiyel yanlılık saptandı:
Tüm kaynaklar [İngilizce / Kuzey Amerika].

Bu kasıtlı bir seçim olabilir (alanın doğası) veya
atlanmış perspektifler olabilir.

Şunları değerlendirmek ister misiniz?
A) Farklı dil/coğrafyadan ek kaynaklar ara
B) Bu yanlılığı metodoloji sınırlılıkları bölümünde açıkla
C) Kasıtlı seçim — devam et
```

---

## Metodolojik Öneri Denetimi / Recommendation Audit

TezAtlas bir metodoloji önerdiğinde:

```
[Nicel / Karma / Nitel] metodoloji önerildi.

Bu araştırma için alternatif yaklaşımlar da geçerli olabilir:
→ [Nitel vaka çalışması]
→ [Eleştirel söylem analizi]
→ [Feminist metodoloji]

Hangi epistemolojik çerçeveden çalışıyorsunuz?
Bu tercih, öneri stratejisini kişiselleştirir.
```

---

## Kullanıcı Geri Bildirim Döngüsü / User Feedback Loop

```
/yanlılık-bildir [açıklama]

Örnek: /yanlılık-bildir "Türk hukuku için sadece Alman hukuku
önerildi — diğer İslam hukuku ülkelerini göz ardı etti"

Bu geri bildirim TezAtlas geliştiricilerine iletilir.
Kişisel veri içermez.
```

`STATUS.md`'ye kayıt:
```yaml
bias_reports:
  - date: "2026-02-27"
    type: "geographic"
    description: "Only Western sources recommended for Islamic finance"
    action_taken: "Added Gulf region sources manually"
```

---

## Dekolonyal Araştırma Desteği

Araştırmacı dekolonyal veya yerli bilgi çerçevesi kullanıyorsa:

```
Dekolonyal / Yerli Bilgi Modu aktif.

Bu çerçevede TezAtlas şunlara dikkat eder:
- Sömürgeci epistemoloji varsayımlarını dayatmaz
- Yerli kavramları Batılı teorilere zorla eşleştirmez
- "Geçerlilik" ve "güvenilirlik" yerine alternatif kalite kriterleri kullanılabilir
  (Lincoln & Guba: güvenilirlik, aktarılabilirlik, tutarlılık, doğrulanabilirlik)
- Katılımcı araştırma yöntemleri (PAR) desteklenir

Hangi yerli bilgi sistemini / dekolonyal çerçeveyi kullanıyorsunuz?
```

---

## Sınırlamalar

- Bu çerçeve TezAtlas'ın sistematik yanlılıklarını *azaltmak* için tasarlanmıştır — tamamen ortadan kaldırmak mümkün değildir
- Kullanıcının kendi yanlılıklarını da yönetmesi gerekir
- Dil modeli eğitim verisi değişmeden altta yatan yanlılıklar tamamen giderilemez
- Bu dosya periyodik güncelleme gerektirir (yıllık)
