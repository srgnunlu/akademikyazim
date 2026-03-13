---
title: "Writing Environment Profile — Sword-Inspired Onboarding"
title_tr: "Yazım Ortamı Profili — Sword Temelli Onboarding"
node_type: technique
description: "Sword (2017): productive academics design personal writing environments — no universal best time/place. Onboarding adds writing environment questions to personalize session reminders and goal suggestions."
description_tr: "Sword (2017): üretken akademisyenler kişisel yazım ortamları tasarlar — evrensel en iyi zaman/yer yoktur. Onboarding'e yazım ortamı soruları ekle, oturum hatırlatıcılarını ve hedef önerilerini kişiselleştir."
tags: [technique, writing-environment, sword, onboarding, personalization, session-start]
links_to:
  - skills/techniques/writing-scheduler.md
  - skills/core/session-continuity.md
  - skills/techniques/implementation-intention.md
language: bilingual
version: "1.0"
---

# Yazım Ortamı Profili / Writing Environment Profile

## Araştırma Temeli / Research Basis

**Sword (2017) — *Air & Light & Time & Space*:**
Stanford'da 1200+ akademisyenle yapılan araştırma: üretken akademik yazarların ortak özelliği tek bir "doğru" ortam değil — *kendi ortamlarını kasıtlı olarak tasarlamalarıdır*.

**Bulgular:**
- En üretken zaman ve yer kişiden kişiye çok farklı
- Kendi ortam tercihlerinin farkında olmak, sürdürülebilir alışkanlık kurmayı kolaylaştırır
- "İlham gelinceye kadar bekle" = verimsizlik tuzağı

---

## Onboarding Soruları / Onboarding Questions

İlk oturumda **bir kez** sor (STATUS.md'ye kaydet):

```
Yazım ortamını tanıyalım:

1. En iyi ne zaman yazıyorsunuz?
   A) Sabah erken (07:00-10:00)
   B) Sabah geç / öğlen (10:00-13:00)
   C) Öğleden sonra (13:00-17:00)
   D) Akşam (17:00-21:00)
   E) Gece geç (21:00+)

2. Nerede yazıyorsunuz?
   A) Ev — sessiz oda
   B) Ev — ortak alan
   C) Ofis / kütüphane
   D) Kafe
   E) Değişiyor

3. Tercih ettiğiniz oturum süresi?
   A) 15-30 dakika (kısa, sık)
   B) 45-60 dakika (standart)
   C) 90 dakika (uzun blok)
   D) 120+ dakika (nadir maraton değil, blok)

4. Müzik / arka plan ses?
   A) Sessizlik
   B) Enstrümental / ambient
   C) Gürültülü ortam (kafe gürültüsü)
   D) Fark etmez
```

---

## Yazım Ortamı Profili / Profile Output

```yaml
writing_env:
  best_time: morning_early    # morning_early | morning_late | afternoon | evening | night
  best_place: home_quiet      # home_quiet | home_shared | office | cafe | anywhere
  preferred_duration: 60      # 15 | 30 | 45 | 60 | 90 | 120
  background: silence         # silence | instrumental | ambient | cafe | doesnt_matter
  ritual: "kahve, telefon kapalı, 5 dk okuma"  # opsiyonel, kullanıcı ekler
  setup_time_min: 5           # ortam hazırlığı için gereken süre tahmini
```

---

## Kişiselleştirilmiş Öneriler / Personalized Suggestions

Profil tamamlandıktan sonra oturum başında:

**Sabahçı, ev, 60 dk:**
```
Sabah yazım saatini yaklaşıyor.
Bugünkü blok: 09:00-10:00
Ortam: ev, sessiz

Kahveni al, telefonu kapat — 5 dakikaya başlayabilirsin.
```

**Geç gece, kafe, 90 dk:**
```
Akşam yazım saatin.
90 dakikalık blok için hazır mısın?

Yer seçimin kafe ise: kulaklık + gürültü iptal — çalışma ortamı kurulu.
```

---

## Profil Güncelleme

Mevsime veya yaşam koşullarına göre değişebilir. Güncelleme komutu:
```
/ortam-güncelle
```

Veya STATUS.md'deki `writing_env` alanını elle düzenle.

---

## Ritual Tasarımı / Ritual Design

Sword'un önemli bir bulgusu: üretken akademisyenler çoğunlukla küçük başlangıç ritüeli geliştirir.

```
Başlangıç ritüeliniz var mı?
(Örnek: "Masayı topla, kahve koy, 3 dakika önceki notu oku, yaz")

Bu ritüeli tanımlayın — TezAtlas oturum başında hatırlatır.
```

Kısa ritüel → beyin "yazmaya geçiş" sinyali alır → daha az irade gücü gerekir.
