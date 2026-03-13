---
title: "Phase 1b — Methodology Fork (Conference)"
title_tr: "Aşama 1b — Metodoloji Çatalı (Konferans)"
node_type: phase-fork
phase_number: 1
document_type: conference
phase_gate_in: "phase-1-literature.md"
phase_gate_out: "phase-2-reading.md"
description: "Methodology fork for empirical conference papers: quantitative (1b-Q), qualitative (1b-Ql), or mixed-methods (1b-M) sub-phase. Triggered after focused literature if research design involves primary data collection. Non-empirical papers skip this phase. Conference constraint: compress methodology to 200-400 words."
description_tr: "Ampirik konferans bildirileri için metodoloji çatalı: nicel (1b-Q), nitel (1b-Ql) veya karma yöntem (1b-M) alt fazı. Odaklı literatür fazının ardından araştırma tasarımı birincil veri toplamayı içeriyorsa tetiklenir. Ampirik olmayan bildiriler bu fazı atlar. Konferans kısıtlaması: metodolojiyi 200-400 kelimeye sıkıştır."
tags: [phase, conference, methodology, empirical, quantitative, qualitative, mixed-methods, fork]
outputs:
  - "METODOLOJI.md (compressed — conference version)"
links_to:
  - skills/core/iron-rules.md
  - skills/core/anti-hallucination.md
  - skills/phases/article/phase-2-methodology-fork.md
language: bilingual
version: "1.0"
---

# Aşama 1b — Metodoloji Çatalı / Methodology Fork (Conference)

## Konferans Kısıtlaması / Conference Constraint

Konferans bildirilerinde metodoloji bölümü genellikle **200-400 kelime** ile sınırlıdır. Bu fazın amacı:
1. Doğru metodolojik yolu belirlemek
2. Kısıtlı alanda en önemli tasarım kararlarını öne çıkarmak
3. Hakemler için yeterli güvenilirliği sağlamak

> **Not:** Makale versiyonu için tam metodoloji detayları → `skills/phases/article/phase-2-methodology-fork.md`

---

## Çatal Kararı / Fork Decision

Bu faz yalnızca **ampirik bildiriler** için geçerlidir:

```
Bildiriniz birincil veri toplamayı içeriyor mu?

A) Evet, nicel veri / Yes, quantitative data  → Aşama 1b-Q
B) Evet, nitel veri  / Yes, qualitative data  → Aşama 1b-Ql
C) Evet, karma yöntem / Yes, mixed methods    → Aşama 1b-M
D) Hayır, teorik/kavramsal/literatür          → Metodoloji çatalı atla → Aşama 2
```

---

## Aşama 1b-Q — Nicel Yol / Quantitative Path

### Konferans Metodoloji Özeti

```markdown
# METODOLOJI.md (Conference — Quantitative)

## Tasarım (1-2 cümle)
[Tasarım türü: deneysel / yarı-deneysel / korelasyonel / kesitsel]
[Temel hipotez veya araştırma sorusu]

## Örneklem (2-3 cümle)
- N = [sayı] | Yöntem: [olasılıklı / kolaylık / tabakalı]
- Güç analizi: [G*Power — d=[...], α=.05, güç=.80]
- Veri kaynağı: [anket / mevcut veri tabanı / deney]

## Analiz (1-2 cümle)
[Ana analiz: t-testi / ANOVA / regresyon / SEM]
[Yazılım: SPSS / R / Python]

## Sınırlılıklar (1 cümle — önemli ise)
[En kritik sınırlılık — hakemler sorar]
```

### Geçiş Kapısı (1b-Q → 2)

- [ ] Örneklem büyüklüğü güç analizi ile desteklendi
- [ ] Analiz yöntemi araştırma sorusuyla eşleşiyor
- [ ] Metodoloji bölümü ≤ 400 kelime
- [ ] Etik onay durumu belirtildi (gerekiyorsa)

---

## Aşama 1b-Ql — Nitel Yol / Qualitative Path

### Konferans Metodoloji Özeti

```markdown
# METODOLOJI.md (Conference — Qualitative)

## Yaklaşım (1-2 cümle)
[Fenomenoloji / grounded theory / içerik analizi / vaka çalışması]
[Epistemolojik konum — kısaca]

## Katılımcılar (2-3 cümle)
- N = [sayı] | Örnekleme: [amaçlı / kartopu]
- Dahil etme kriteri: [...]
- Veri toplama: [yarı yapılandırılmış görüşme / odak grup / belgeler]

## Analiz (1-2 cümle)
[Tematik analiz / IPA / içerik analizi]
[Güvenilirlik: üye kontrolü / çift kodlama]

## Sınırlılıklar (1 cümle)
[Genellenebilirlik sınırı — hakemler mutlaka sorar]
```

### Geçiş Kapısı (1b-Ql → 2)

- [ ] Metodolojik yaklaşım araştırma sorusuyla tutarlı
- [ ] Örnekleme stratejisi ve sayısı gerekçelendirildi
- [ ] Güvenilirlik stratejisi belirtildi
- [ ] Metodoloji bölümü ≤ 400 kelime

---

## Aşama 1b-M — Karma Yöntem / Mixed Methods Path

Konferans bildirilerinde karma yöntem nadirdir (sayfa kısıtı). Hakemler çoğunlukla ikisinden birini tercih eder.

```markdown
# METODOLOJI.md (Conference — Mixed Methods)

## Desen (1 cümle)
[Açıklayıcı sıralı / Keşifsel sıralı / Eş zamanlı]
[Nicel bileşen ağırlığı: QUAN-qual]

## Bileşenler (3-4 cümle toplam)
Nicel: [N, tasarım, analiz — bkz. 1b-Q formatı, sadeleştirilmiş]
Nitel: [N, yaklaşım — bkz. 1b-Ql formatı, sadeleştirilmiş]
Entegrasyon: [hangi aşamada, nasıl]
```

**Konferans uyarısı:** Karma yöntem için sayfa sınırı genellikle yetersizdir. Her iki bileşeni yüzeysel sunmak yerine, birini öne çıkarmayı değerlendirin.

### Geçiş Kapısı (1b-M → 2)

- [ ] Her iki bileşen kısaca ama yeterince açıklandı
- [ ] Entegrasyon noktası gösterildi
- [ ] Toplam metodoloji ≤ 400 kelime — **sıkı kısıt**

---

## Anti-Halüsinasyon Notu

Konferans metodoloji özetlerinde de Iron Rule M geçerlidir:

- Örneklem büyüklükleri → güç analizi kaynağı
- Güvenilirlik eşikleri → standart kaynak atfı (APA / alan rehberi)
- Raporlama standartları → CONSORT, COREQ, SRQR kısaltmaları bile atıf gerektirir

Kaynak gösterilemeyen metodoloji tavsiyesi: `[Source: Unverified]` etiketi.
