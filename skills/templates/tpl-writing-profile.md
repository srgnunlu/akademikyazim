---
title: "Template — Writing Style Profile"
title_tr: "Şablon — Yazım Stili Profili"
node_type: template
description: "Template for YAZIM_PROFILI.md — the user's personal writing fingerprint. Created during onboarding or first writing session."
description_tr: "YAZIM_PROFILI.md şablonu — kullanıcının kişisel yazım parmak izi. Onboarding veya ilk yazım oturumunda oluşturulur."
tags: [template, writing-profile, style, natural-voice]
links_to:
  - skills/techniques/natural-voice.md
used_by:
  - skills/core/onboarding.md
  - skills/techniques/natural-voice.md
language: bilingual
version: "1.0"
---

# YAZIM_PROFILI.md Şablonu / Writing Style Profile Template

Bu dosya iki şekilde doldurulabilir:

**Yöntem A (önerilen):** Kullanıcı daha önce yazdığı 2-3 sayfa akademik metin paylaşır. AI metni analiz ederek profili otomatik doldurur, kullanıcı onaylar/düzeltir.

**Yöntem B:** Kullanıcı aşağıdaki soruları yanıtlar.

---

## Oluşturulacak Dosya: `YAZIM_PROFILI.md`

```markdown
# Yazım Stili Profili
Son güncelleme: [tarih]
Oluşturma yöntemi: [örnek analiz / soru-cevap / karma]

## Cümle Tercihleri
- Ortalama cümle uzunluğu: [X] kelime
- Uzunluk varyasyonu: [düşük / orta / yüksek]
- Kısa vurgu cümleleri (≤10 kelime) kullanır mı: [evet / hayır]
- Çok uzun cümleler (30+ kelime) kullanır mı: [evet / hayır]

## Noktalama
- Noktalı virgül (;): [sık / nadir / hiç]
- Tire arası açıklama (— ... —): [sık / nadir / hiç]
- Parantez içi açıklama: [sık / nadir / hiç]
- İki nokta (:) ile açıklama/liste: [sık / nadir / hiç]
- Üç nokta (...): [sık / nadir / hiç]

## Paragraf Yapısı
- Tercih edilen uzunluk: [kısa 3-5 cümle / orta 5-8 / uzun 8+]
- Madde listesi tercihi: [sık / nadir / hiç]
- Paragraf geçiş stili: [geçiş cümlesiyle / içerikle doğal / bağlaçla]

## Üslup
- Edilgen/etken: [ağırlıklı edilgen / dengeli / ağırlıklı etken]
- Hedging yoğunluğu: [çekingen / dengeli / kararlı]
- Doğrudan alıntı sıklığı: [sık / nadir]
- Retorik soru kullanır mı: [evet / hayır]
- Birinci çoğul kişi (biz/we): [evet / hayır]

## Kaçınılanlar
<!-- Kullanıcının "ben bunu yapmam" dediği şeyler -->
- [örnek: "Tire arası cümle yazmıyorum"]
- [örnek: "Noktalı virgül kullanmıyorum, yeni cümle başlarım"]
- [örnek: "Madde listesi yerine uzun paragraflar tercih ederim"]

## Tercih Edilen Kalıplar
<!-- Kullanıcının sıklıkla kullandığı geçiş/yapı kalıpları -->
- [örnek: "Bu noktada..."]
- [örnek: "Nitekim..."]
- [örnek: Cümleleri genellikle bağlaçsız, ayrı cümle olarak kurar]

## Notlar
<!-- Profilin özel durumları, ek açıklamalar -->
```

---

## Yöntem A: Örnek Metin Analizi Protokolü

Kullanıcıdan metin alındığında AI şu metrikleri çıkarır:

1. **Cümle uzunluk dağılımı** — min, max, ortalama, standart sapma
2. **Noktalama sayımı** — noktalı virgül, tire, parantez, iki nokta sıklığı
3. **Paragraf uzunlukları** — ortalama cümle sayısı per paragraf
4. **Geçiş analizi** — paragraflar nasıl bağlanıyor?
5. **Edilgen/etken oranı**
6. **Kelime tekrar oranı** — aynı kök kelimenin paragraf içi tekrar sıklığı
7. **Yapısal çeşitlilik** — SVO dışı cümle oranı

Sonuç kullanıcıya sunulur: "Analizime göre profiliniz şöyle. Düzeltmek istediğiniz bir şey var mı?"

---

## Yöntem B: Soru-Cevap Protokolü

Onboarding veya ilk yazım oturumunda AI şu soruları sorar:

1. "Cümleleriniz genellikle uzun mu, kısa mı, yoksa karışık mı?"
2. "Noktalı virgül kullanır mısınız, yoksa genellikle yeni cümleye mi başlarsınız?"
3. "Tire arası açıklamalar (— böyle — ) kullanır mısınız?"
4. "Paragraflarınız genellikle kaç cümle? Kısa mı, uzun mu?"
5. "Madde listesi mi tercih edersiniz, düzyazı içinde anlatmayı mı?"
6. "Yazarken hiç kullanmadığınız, size ait olmayan yapılar var mı?"
7. "Sık kullandığınız geçiş kalıpları var mı? (ör. 'nitekim', 'bu noktada')"

Yanıtlar profil dosyasına dönüştürülür.

---

## Profil Güncelleme Tetikleyicileri

- Kullanıcı bir alternatifi seçerken sürekli belirli bir stili tercih ediyorsa → "Profilinizde X güncellemesi yapalım mı?"
- Kullanıcı açıkça stil değişikliği belirtiyorsa → profil güncellenir
- `DERSLER.md`'ye stil dersi eklendiyse → profil kontrol edilir
- Her 10 yazım oturumunda → profil gözden geçirme önerilir
