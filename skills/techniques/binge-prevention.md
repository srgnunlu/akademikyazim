---
title: "Binge-Writing Prevention System"
title_tr: "Maraton Yazım Önleme Sistemi"
node_type: technique
description: "Boice (1990): binge writing = lower output, higher anxiety, reinforced avoidance. TezAtlas warning if user attempts very long single session (>4 hours). Celebrate streak over marathon."
description_tr: "Boice (1990): maraton yazım = düşük çıktı, yüksek kaygı, kaçınmayı pekiştirme. Çok uzun tek oturum (>4 saat) girişiminde TezAtlas uyarır. Maratonu değil sürekliliği kutla."
tags: [technique, binge-prevention, boice, writing-scheduler, wellbeing, session-length]
links_to:
  - skills/techniques/writing-scheduler.md
  - skills/core/attrition-prevention.md
  - skills/core/user-modes.md
language: bilingual
version: "1.0"
---

# Maraton Yazım Önleme Sistemi / Binge-Writing Prevention

## Araştırma Temeli / Research Basis

**Boice (1990) — *Professors as Writers*:**

| Yazım Stili | Çıktı | Kaygı | Uzun Vadeli Etki |
|-------------|-------|-------|-----------------|
| Günlük düzenli (30-90 dk) | ✅ Yüksek | ✅ Düşük | Alışkanlık kurar |
| Maraton (4+ saat, seyrek) | ⚠️ Düşük (baştaki coşku yanıltır) | ⚠️ Yüksek | Kaçınmayı pekiştirir |

**Temel bulgu:** Maraton yazım seansları kısa vadede üretken *hissettirse* de, bittikten sonra gelen yorgunluk ve tükenmişlik bir sonraki oturumu erteleme olasılığını artırır.

---

## Tetikleyiciler / Triggers

### 1. Oturum Başında Uzun Plan Algılandığında

Kullanıcı 4+ saat tek oturum planladığında:

```
⚠️ Maraton Yazım Planı Algılandı

Planlanan süre: [X] saat

Boice'un (1990) bulgusu: 4+ saatlik tek oturumlar çıktı
kalitesini ve sürdürülebilirliği düşürür.

Öneri: Bu oturumu böl.
A) [2 saat şimdi] + [2 saat yarın veya öğleden sonra]
B) [90 dk + 30 dk mola + 90 dk] — bugün
C) Devam et (seçimim bu)

Tercih?
```

### 2. Aktif Oturum 3 Saati Geçtiğinde

```
⏱️ 3 saattir yazıyorsun.

Mola vermeyi düşün: 10-15 dakikalık bir ara, hem beyin
hem de gözler için önemli.

Devam etmek istersen: C seç — engel değilim.
Ama yarın için bir şey ayır: bugün her şeyi bitirmeye çalışmak
genellikle işe yaramaz.
```

---

## Streak Kutlaması / Streak Celebration

Maraton yerine, sürekliliği kutla:

```
🔥 5 gün üst üste yazdın!

Bu, tek bir 8 saatlik seansla aynı toplam süre — ama çok
daha sürdürülebilir.

Boice haklıydı.
```

| Streak | Kutlama Mesajı |
|--------|----------------|
| 3 gün | "Ritim kuruluyor — bu en zor kısımdı." |
| 7 gün | "1 hafta! Bu çalışma şekli işe yarıyor." |
| 14 gün | "2 hafta — bu artık bir alışkanlık." |
| 30 gün | "30 gün. Boice haklıydı." |
| Kayıp | "Dün yazamadın — tamam. Bugün nereden devam?" |

---

## Dil ve Ton Kuralları

**Kullanılmaz:**
- "Yeterince çalışmıyorsun"
- "Bu kadar kısa oturumla bitiremezsin"
- Suçlama veya zaman baskısı

**Kullanılır:**
- Seçenek sun, zorlamaz
- Bilimsel bulgulara dayandır (Boice'un adını ver)
- Streak'i somut başarı olarak çerçevele

---

## STATUS.md Entegrasyonu

```yaml
writing_schedule:
  current_streak: 5
  last_session_date: "2026-02-27"
  session_duration_min: 75
  binge_warning_threshold: 240  # dakika
  binge_warnings_received: 0
```
