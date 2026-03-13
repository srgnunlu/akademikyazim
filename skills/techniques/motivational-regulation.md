---
title: "Motivational Regulation Prompts — Pintrich Module"
title_tr: "Motivasyonel Düzenleme Promtları — Pintrich Modülü"
node_type: technique
description: "Pintrich (2000): doctoral writing requires sustained intrinsic motivation across years. At each phase gate: store personal 'why'. Show back during low-motivation periods. Connects task to personal value."
description_tr: "Pintrich (2000): doktora yazımı yıllar içinde sürdürülen içsel motivasyon gerektirir. Her faz kapısında: kişisel 'neden'i sakla. Düşük motivasyon dönemlerinde göster. Görevi kişisel değerle bağla."
tags: [technique, motivational-regulation, pintrich, intrinsic-motivation, phase-gate, wellbeing, srl]
links_to:
  - skills/core/attrition-prevention.md
  - skills/core/session-continuity.md
  - skills/techniques/writing-scheduler.md
language: bilingual
version: "1.0"
---

# Motivasyonel Düzenleme Promtları / Motivational Regulation Prompts

## Araştırma Temeli / Research Basis

**Pintrich (2000) — Self-Regulated Learning:**
Doktora yazım sürecinde motivasyon kaybı, yetenek veya zeka eksikliğinden değil — *görev değeri* bağlantısının kopmasından kaynaklanır.

**Temel kavramlar:**
- **İçsel motivasyon:** Araştırmanın kendisi için ilgi duyma
- **Görev değeri:** "Bu araştırma neden önemli?"
- **Öz-yeterlilik:** "Bunu yapabilir miyim?"
- **Kontrolün yüklendiği yer:** Başarı/başarısızlık kişisel çabaya mı, dışsal faktörlere mi atfediliyor?

---

## Faz Kapısı Motivasyon Kaydı / Phase Gate Motivation Record

Her önemli faz geçişinde **bir kez** sor ve `STATUS.md`'ye kaydet:

```
Faz [X]'i tamamladın.

Bir cümleyle: Bu araştırma sana göre neden önemli?
(Akademik değil, kişisel — içten bir yanıt)

"Bu araştırma önemli çünkü: [...]"
```

Kayıt formatı (`STATUS.md`):
```yaml
motivation:
  why_statement: "CBDC'lerin küçük ülkelerdeki etkileri anlaşılırsa,
    para politikasının demokratikleşmesine katkıda bulunabilirim."
  recorded_at: "2026-02-01"
  phase: 3
```

---

## Düşük Motivasyon Tetikleyicisi / Low Motivation Trigger

Tetikleme koşulları (attrition-prevention ile koordineli):
- 14+ günlük hareketsizlik
- 3+ ardışık kaçırılan hedef
- Kullanıcı "motivasyon" veya "sıkıştım" gibi ifadeler kullandığında

```
[N] gündür görüşmemiştik.

Bir süre önce şunu yazmıştın:
"Bu araştırma önemli çünkü: [why_statement]"

Bu hâlâ geçerli mi?
A) Evet — o zaman nereden devam ediyoruz?
B) Değişti — konuşalım
C) Bilmiyorum — bu da tamam
```

---

## Görev Değeri Bağlantısı / Task-Value Connection

Sıkıcı veya mekanik görevlerde (referans listesi, tablo formatı, veri temizleme):

```
Bu bölüm araştırmanın en heyecanlı kısmı değil.

Ama şunu hatırlatayım: [why_statement]

Bu küçük adım o büyük soruya hizmet ediyor.
15 dakika için başla.
```

---

## Öz-Yeterlilik Desteği / Self-Efficacy Support

Akademik öz-yeterlilik somut kanıtlarla güçlenir:

```
Bu ay:
✅ [N] kaynak okudun
✅ [N] paragraf yazdın
✅ Faz [X]'i tamamladın

"Yapamam" hissettiren şey ne?
A) Bu spesifik görev çok belirsiz
B) Yorgunluk / motivasyon düşüklüğü
C) Dış engel (zaman, kaynak, danışman)
```

---

## Dil Kuralları

**Kullanılmaz:**
- "Motivasyonunu kaybetmemelisin"
- Gerçekçi olmayan pozitiflik ("Sen yapabilirsin!")
- Akademik başarıyı kişilik özelliğine bağlama

**Kullanılır:**
- Araştırmacının kendi sözleriyle hatırlatma
- Kontrol edilebilir nedenlere atıf (strateji, plan)
- Somut ilerlemeyi göster

---

## STATUS.md Alanları

```yaml
motivation:
  why_statement: "[araştırmacının kendi ifadesi]"
  recorded_at: "YYYY-MM-DD"
  phase: 3
  last_shown: "YYYY-MM-DD"
  resonance: high   # high | medium | low — araştırmacı günceller
```
