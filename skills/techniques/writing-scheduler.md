---
title: "Daily Writing Scheduler — Silvia/Boice Module"
title_tr: "Günlük Yazım Zamanlayıcı — Silvia/Boice Modülü"
node_type: technique
description: "Research-backed daily writing session protocol: scheduled blocks (Silvia 2007), streak tracking (Boice 1990), micro-goal commitment, post-session reflection. Populates DASHBOARD.md streak section."
description_tr: "Araştırma destekli günlük yazım oturum protokolü: planlı bloklar (Silvia 2007), süreklilik takibi (Boice 1990), mikro-hedef taahhüdü, oturum sonrası yansıma. DASHBOARD.md streak bölümünü besler."
tags: [technique, writing-scheduler, silvia, boice, srl, streak, daily-writing, ux]
links_to:
  - skills/templates/tpl-dashboard.md
  - skills/core/session-continuity.md
  - skills/core/user-modes.md
language: bilingual
version: "1.0"
---

# Günlük Yazım Zamanlayıcı / Daily Writing Scheduler

## Araştırma Temeli / Research Basis

**Silvia (2007) — "How to Write a Lot":** Yazımı "eğer zamanım olursa yazarım" değil, takvim randevusu gibi planla. Günlük 30-90 dk düzenli yazım, haftalık maratonu geçer.

**Boice (1990) — "Professors as Writers":** Günlük küçük oturumlar > aralıklı binge writing. Binge: daha düşük çıktı, daha yüksek kaygı, kaçınmayı pekiştirir. Süreklilik (streak) ölçümü, çıktı miktarından daha güçlü motivasyon kaynağıdır.

---

## Oturum Başı — Mikro-Hedef Taahhüdü / Session Start Micro-Goal

Her yazım oturumunda ilk adım:

```
Bugün ne yazacaksınız? (Bir cümleyle tamamla)

"Bugün [BÖLÜM ADI]'nın [ALT BÖLÜM] paragraflarını yazacağım."

Süre: [30 / 60 / 90] dakika
Kelime hedefi: [200 / 400 / 600] kelime  (opsiyonel)
```

**Hedef belirleme kuralı:** Spesifik + ulaşılabilir. "Tez yazmak" değil — "2.1 alt bölümünün giriş paragrafını yazmak".

---

## Yazım Ortamı Profili / Writing Environment Profile

Onboarding'de bir kez sor (STATUS.md'ye kaydet):

```yaml
writing_env:
  best_time: morning      # morning | afternoon | evening | night
  best_place: home        # home | office | cafe | anywhere
  preferred_duration: 60  # 30 | 60 | 90 | 120+ dakika
  session_reminder: true  # false = hatırlatıcılar kapalı
```

Bu profil TezAtlas'ın oturum başında gösterdiği banner'ı kişiselleştirir.

---

## Streak Takibi / Streak Tracking

`DASHBOARD.md`'deki streak bölümü her oturum sonunda güncellenir:

```
Yazım Streak (Son 14 Gün)
Mo Tu We Th Fr Sa Su  Mo Tu We Th Fr Sa Su
 ●  ●  ●  ○  ●  ○  ○   ●  ●  ●  ●  ●  ○  ○
Mevcut streak: 5 gün  |  En uzun streak: 9 gün
```

**Streak kuralı:**
- Bir oturum ≥ 15 dakika aktif yazım = o gün streak için sayılır
- Hafta sonu boşlukları ceza değil — "rest days" olarak işaretle
- Hedef: konsistans, maraton değil

**Kutlama mesajları:**

| Streak | Mesaj |
|--------|-------|
| 3 gün | "3 günlük streak — ritim kuruluyor" |
| 7 gün | "1 hafta kesintisiz! Bu çalışma şekli işe yarıyor." |
| 14 gün | "2 haftalık streak — bu artık bir alışkanlık." |
| 30 gün | "30 gün! Boice haklıydı." |

**Uyarı:** Streak kaybedildiğinde ceza yok. Şu mesaj gösterilir:
> "Dün yazamadın — tamam. Bugün nereden devam ediyoruz?"

---

## Oturum Sonu — 2 Soruluk Yansıma / Post-Session Reflection

Her oturum bitiminde:

```
1. Bugün ne iyi gitti?
2. Bir dahaki sefere ne değiştirirdin?
```

Cevaplar `DASHBOARD.md`'nin "Son oturum notu" alanına kaydedilir. AI bu cevapları okuyarak bir sonraki oturumda kişiselleştirilmiş başlangıç notu sunar.

---

## Uzun Oturum Uyarısı / Long Session Warning

4 saatten uzun tek oturum planlandığında:

```
⚠️ Uzun oturum planı algılandı.
Boice'un bulgusu: 4+ saat binge writing çıktı kalitesini ve
sürdürülebilirliği düşürür.

Öneri: Bu oturumu 2 ayrı oturuma böl.
Seçenek A: [2 saat şimdi] + [2 saat yarın]
Seçenek B: [90 dk + 30 dk mola + 90 dk]

Devam etmek ister misiniz?
```

---

## DASHBOARD.md Entegrasyonu

Writing scheduler aşağıdaki DASHBOARD.md alanlarını günceller:

```markdown
## Yazım Takvimine Uyum
Son 7 günde planlı oturum: [N]/7
Ortalama oturum süresi: [X] dk
Toplam bu hafta: [X] kelime

## Streak
[Streak görsel — bkz. tpl-dashboard.md]
Mevcut: [N] gün | En uzun: [N] gün

## Son Oturum
[TARİH] — [X] dk — [X] kelime — [mikro-hedef tamamlandı mı?]
Notlar: [yansıma cevabı]
```

---

## STATUS.md Scheduler Alanları

```yaml
writing_schedule:
  preferred_days: [Mon, Tue, Wed, Thu, Fri]
  preferred_time: "09:00"
  session_duration_min: 60
  current_streak: 5
  longest_streak: 9
  last_session_date: "2026-02-27"
  total_sessions: 34
```
