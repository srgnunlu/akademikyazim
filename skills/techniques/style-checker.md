---
title: "Academic Writing Style Checker"
title_tr: "Akademik Yazım Stili Denetleyicisi"
node_type: technique
description: "Passive voice detector, over-hedging detector, over-claiming detector, discipline-appropriate register checker. Runs as Phase 6/7 quality gate, not during drafting."
description_tr: "Pasif çatı tespiti, aşırı çekince tespiti, aşırı iddia tespiti, alana uygun tarz denetimi. Faz 6/7 kalite kapısı olarak çalışır, taslak yazımı sırasında değil."
tags: [technique, style-checker, passive-voice, hedging, quality-gate, phase-6, phase-7]
links_to:
  - skills/core/iron-rules.md
  - skills/core/anti-hallucination.md
  - skills/techniques/copilot-writing.md
language: bilingual
version: "1.0"
---

# Akademik Yazım Stili Denetleyicisi / Academic Writing Style Checker

## Ne Zaman Çalışır? / When Does It Run?

**Faz 6 (Yazım) → Faz 7 (Finalizasyon) geçiş kapısında** — taslak yazılırken değil, yazım tamamlanınca.

Aktivasyon: `/stil-kontrol [dosya]` veya faz geçiş kapısında otomatik.

---

## 4 Denetim Boyutu / 4 Audit Dimensions

### 1. Pasif Çatı Yoğunluğu / Passive Voice Density

**Hedef:** Bölüm başına ≤ %25 pasif çatı (fen bilimleri yöntem bölümü hariç: %40'a kadar kabul edilebilir)

```
Kontrol edilen örüntüler:
- "it was found that" → "the study found"
- "has been shown" → "X showed"
- "is considered to be" → "researchers consider"
- Türkçe: "-ldı/-ldi" yoğunluğu, özellikle argümantasyon bölümlerinde
```

**Üst eşik:** Metodoloji bölümü dışında, 10 cümlede 4'ten fazla pasif yapı → uyarı.

---

### 2. Aşırı Çekince / Over-Hedging

Akademik yazımda çekince (hedging) gereklidir — ancak aşırısı argümanı zayıflatır.

**Tek çekinceli (normal):**
> "The findings suggest that..."

**Çok katmanlı çekince (sorunlu):**
> "The findings might perhaps possibly suggest that it could be the case that..."

```
Kırmızı bayrak örüntüleri:
- 3+ zincir çekince: might + perhaps + possibly + could
- "it seems as if it might be"
- Türkçe: "olabilir gibi görünmektedir" — 3 çekince katmanı
```

---

### 3. Aşırı İddia / Over-Claiming

Özellikle sonuç bölümlerinde.

```
Kırmızı bayrak ifadeler:
- "definitively proves" → "provides evidence for"
- "clearly demonstrates" → "suggests" veya "indicates"
- "without doubt" → genellikle kaldır
- "the first study ever" → kaynağını doğrula
- "revolutionary", "groundbreaking" → editörler bu tür ifadelerden hoşlanmaz
- Türkçe: "kesinlikle kanıtlamaktadır" → "kanıt sunmaktadır"
```

---

### 4. Alana Uygun Tarz / Discipline Register

| Disiplin | Beklenen Tarz | Yaygın Hatalar |
|----------|---------------|----------------|
| Fen/Müh. | Nesnel, pasif ağırlıklı, kısa cümle | 1. şahıs kullanmak |
| Sosyal Bil. | 1. çoğul şahıs kabul edilir, yorumlayıcı | Aşırı teknik jargon |
| Hukuk | Kesin, normatif, birincil kaynak ağırlıklı | Belirsiz atıf |
| Beşeri Bil. | 1. şahıs kabul edilir, argümantatif | Pasif aşırılığı |
| Tıp/Sağlık | CONSORT/STROBE terminolojisi | Klinik dil karıştırma |

---

## Denetim Raporu Formatı / Audit Report Format

```
Stil Denetim Raporu — [DOSYA ADI]
══════════════════════════════════
Tarih: [TARİH] | Kelime sayısı: [N]

┌─────────────────────────────────────────────┐
│ Pasif çatı oranı:  %18  ✅ (hedef: ≤%25)   │
│ Çekince yoğunluğu: 7/1000 kelime ✅         │
│ Aşırı iddia:       2 örüntü ⚠️              │
│ Tarz tutarlılığı:  Genel ✅                  │
└─────────────────────────────────────────────┘

Aşırı İddia Tespitleri:
─────────────────────
→ Satır 142: "definitively proves" — öneri: "provides evidence for"
→ Satır 267: "without any doubt" — öneri: kaldır veya "strongly suggests"

Çekince Zinciri Tespitleri:
─────────────────────────
(Temiz — sorun yok)
```

---

## Sınırlamalar

- Bağlam körü: "clearly demonstrates" bazen haklı olabilir (çok güçlü kanıt)
- Pasif çatı: yöntem bölümünde yüksek oranlar normaldir
- Bu araç yazımı engellemez — yalnızca geçiş kapısında rapor verir
- Nihai karar her zaman araştırmacıya aittir
