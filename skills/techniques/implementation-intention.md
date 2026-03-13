---
title: "Implementation Intention Builder — Pre-Session"
title_tr: "Uygulama Niyeti Oluşturucu — Oturum Öncesi"
node_type: technique
description: "Gollwitzer & Sheeran (2006): If-Then planning reduces procrastination 2-3x vs general intentions. TezAtlas session start: complete the If-Then sentence for today's writing commitment."
description_tr: "Gollwitzer & Sheeran (2006): Eğer-O Zaman planlaması ertelemeyi genel niyetlere kıyasla 2-3 kat azaltır. TezAtlas oturum başında: bugünkü yazım taahhüdü için Eğer-O Zaman cümlesini tamamla."
tags: [technique, implementation-intention, gollwitzer, procrastination, session-start, pre-session, srl]
links_to:
  - skills/techniques/writing-scheduler.md
  - skills/core/session-continuity.md
  - skills/core/attrition-prevention.md
language: bilingual
version: "1.0"
---

# Uygulama Niyeti Oluşturucu / Implementation Intention Builder

## Araştırma Temeli / Research Basis

**Gollwitzer & Sheeran (2006) — Meta-analiz (94 çalışma):**

| Niyet Türü | Etkililik |
|-----------|-----------|
| Genel niyet ("Yarın yazacağım") | Düşük — koşullar belirsiz |
| Uygulama niyeti ("Eğer saat 09:00 olursa, o zaman X dosyasını açıp Y paragrafını yazacağım") | 2-3 kat daha etkili |

**Mekanizma:** "Eğer-O Zaman" formatı, niyet ile durumsal tetikleyici arasında otomatik bir bağlantı kurar. Bilinçli motivasyon gerektirmez.

---

## Oturum Başında / Session Start Protocol

Her oturum başında, yazmaya geçmeden önce:

```
Bugünkü yazım taahhüdünü tamamla:

"Eğer saat [SAAT] olursa ve ben [YER]'deysem,
o zaman [DOSYA]'yı açacağım ve
[SPESİFİK GÖREV]'i [SÜRE] dakika boyunca yazacağım."

Örnek:
"Eğer saat 09:00 olursa ve ben masamdaysam,
o zaman BOLUM_3.md'yi açacağım ve
3.2 alt bölümünün giriş paragrafını 45 dakika boyunca yazacağım."
```

---

## Spesifiklik Kontrolü / Specificity Check

Taahhüt alındığında spesifiklik değerlendir:

| Eleman | Belirsiz ❌ | Spesifik ✅ |
|--------|-----------|------------|
| Zaman | "Sabah" | "09:00" |
| Yer | "Evde" | "Çalışma odam, masam" |
| Dosya | "Tez" | "BOLUM_3.md" |
| Görev | "Yazmak" | "3.2 giriş paragrafı" |
| Süre | "Biraz" | "45 dakika" |

Belirsiz bir eleman tespit edilirse:
```
Taahhüdünde [zaman/yer/görev] biraz genel kalmış.

Daha spesifik yapabilir misin?
"[belirsiz kısım]" yerine daha kesin bir şey?
```

---

## Engel Öncesi Planlama / If-Then for Obstacles

**Gelişmiş versiyon:** Yaygın engelleri önceden planla.

```
Olası bir engel için plan yapalım:

"Eğer [oturum saatinde dikkatim dağılırsa / yorgun hissedersem /
internet çekim olursa], o zaman [ne yapacaksın]?"

Örnek:
"Eğer telefon dikkatimi dağıtırsa,
o zaman telefonu çantama koyacağım ve
alarm kuracağım."
```

---

## Kaydedilen Taahhütler / Saved Commitments

`STATUS.md`'ye oturum başında kaydedilir, oturum sonunda değerlendirilir:

```yaml
session_commitment:
  if_time: "09:00"
  if_place: "home-desk"
  then_file: "BOLUM_3.md"
  then_task: "3.2 giriş paragrafı"
  then_duration: 45
  committed_at: "2026-02-27"
  completed: true
  reflection: "Planlandığı gibi gitti — dikkat dağılmadı"
```

---

## Tamamlanma Değerlendirmesi / Completion Review

Oturum sonunda:
```
Taahhüdünü değerlendir:

"Eğer saat 09:00 olursa → [X dosyası, Y görevi, Z dakika]"

A) Tamamlandı ✅
B) Kısmen tamamlandı — ne engelledi?
C) Tamamlanamadı — ne oldu?
```

**B veya C seçilirse:** Engeli tanımla, bir sonraki için If-Then planını güncelle. Suçlama yok — öğrenme fırsatı.

---

## Düşük Motivasyon Özel Versiyonu

Attrition risk yüksek dönemde, düşük hedef:
```
Bugün küçük bir taahhüt yapalım:

"Eğer saat [X] olursa,
o zaman [dosyayı açacağım] — en az 10 dakika."

10 dakika. Başlamak bitirmenin yarısı.
```
