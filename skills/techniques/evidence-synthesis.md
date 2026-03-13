---
title: "Evidence Synthesis Engine — Elicit/Consensus Equivalent"
title_tr: "Kanıt Sentezi Motoru — Elicit/Consensus Muadili"
node_type: technique
description: "Extract claim-evidence pairs from reading notes, cluster by research question, generate synthesis matrix (author × finding × method × conclusion), flag consensus vs. disagreement, output feeds Phase 4 outline. Source-anchored: every synthesis point traces to a local PDF."
description_tr: "Okuma notlarından iddia-kanıt çiftleri çıkar, araştırma sorusuna göre kümelendir, sentez matrisi oluştur (yazar × bulgu × yöntem × sonuç), konsensüs vs. anlaşmazlık işaretle, çıktı Faz 4 taslağını besler. Kaynak bağlantılı: her sentez noktası yerel PDF'e izlenir."
tags: [technique, evidence-synthesis, elicit, consensus, synthesis-matrix, phase-4, source-anchored]
links_to:
  - skills/core/cognitive-augmentation.md
  - skills/core/anti-hallucination.md
  - skills/techniques/comparative-analysis.md
language: bilingual
version: "1.0"
---

# Kanıt Sentezi Motoru / Evidence Synthesis Engine

## Elicit / Consensus'dan Farkı / Difference from Elicit/Consensus

| Özellik | Elicit / Consensus | TezAtlas ESE |
|---------|-------------------|--------------|
| Kaynak | Web aramadan, LLM belleğinden | Sadece `/sources/` yerel PDF'leri |
| Doğrulama | Zayıf — halüsinasyon riski | Iron Rule 1: kaynak gösterilemeyen = `[Source: Unverified]` |
| Kapsam | Geniş, otomatik | Araştırmacının okuduklarıyla sınırlı |
| Şeffaflık | "Elicit diyor ki" | "Auer et al. (2022), s. 14 diyor ki" |

---

## Adım 1 — İddia-Kanıt Çiftleri / Claim-Evidence Pairs

Okuma notlarından (CAW ile koordineli) otomatik çıkarım:

```
notes/ klasörü tarandı — 12 not dosyası bulundu.

İddia-Kanıt Çiftleri (HAM):
┌─────────────────────────────────────────────────────────────┐
│ İddia                  │ Kaynak           │ s.  │ Güç │ RQ │
├─────────────────────────────────────────────────────────────┤
│ CBDC benimseme ↑ → MB  │ Auer et al.2022  │ 14  │ ●●● │ RQ1│
│ para arzı kontrolü ↑   │                  │     │     │    │
├─────────────────────────────────────────────────────────────┤
│ CBDC gizlilik riski    │ ECB 2021         │ 8   │ ●●○ │ RQ3│
│ yüksek                 │                  │     │     │    │
├─────────────────────────────────────────────────────────────┤
│ Para pol. aktarımı     │ BIS 2023         │ 22  │ ●●● │ RQ2│
│ güçlenir               │                  │     │     │    │
└─────────────────────────────────────────────────────────────┘
```

---

## Adım 2 — Sentez Matrisi / Synthesis Matrix

Araştırma sorusuna göre kümelendirilmiş:

```
Sentez Matrisi: RQ2 — Para Politikası Aktarımı

Yazar (Yıl)     │ Bulgu           │ Yöntem   │ Sonuç      │ Çelişki?
────────────────┼─────────────────┼──────────┼────────────┼─────────
BIS (2023)      │ Aktarım güçlenir│ Simülasyon│ CBDC+      │ Hayır
Auer et al.2022 │ Enflasyon riski │ Ampirik  │ Karışık    │ EVET ⚠️
Niepelt (2020)  │ Dezintermedias. │ Model    │ MB bağımsız│ Hayır
Kumhof & Noone  │ Politika etkili │ DSGE     │ CBDC+      │ Hayır
(2021)          │                 │          │            │
────────────────┼─────────────────┼──────────┼────────────┼─────────
Konsensüs: Para politikası aktarımı güçlenir (3/4)
Anlaşmazlık: Enflasyon etkisi — metodoloji farkı var (simülasyon vs. ampirik)
```

---

## Adım 3 — Konsensüs ve Anlaşmazlık Tespiti

```
📊 Konsensüs Alanları (RQ2):
✅ Para politikası aktarımının güçleneceği: 3/4 kaynak hemfikir
✅ Merkez bankası rolünün değişeceği: 4/4 kaynak hemfikir

⚠️ Anlaşmazlık Alanları:
→ Enflasyon etkisi: BIS (nötr) vs. Auer et al. (artış riski)
  Metodoloji farkı: simülasyon vs. ampirik — bu farkı tezde açıkla

❌ Kanıt Boşlukları:
→ Gelişmekte olan ülkelere özel etki: kanıt yok
→ Uzun vadeli (10+ yıl) etkiler: spekülatif
```

---

## Adım 4 — Faz 4 Taslak Çıktısı / Phase 4 Outline Feed

```
Bölüm Önerileri (Sentez Bazlı):

3.1 Para Politikası Aktarım Mekanizması
   [Konsensüs: 3 kaynak — güçlü temel]
   → BIS (2023), Niepelt (2020), Kumhof & Noone (2021)

3.2 Enflasyon Etkisi: Metodolojik Anlaşmazlık
   [Tartışmalı — metodoloji farkını açıkla]
   → Auer et al. (2022) vs. BIS (2023) — bu çelişkiyi tezin pozisyonu olarak kullan

3.3 Gelişmekte Olan Ülkeler: Kanıt Boşluğu
   [Boşluk — araştırma katkısı fırsatı]
   → Mevcut literatürün sınırlılığını belirt → kendi katkın burada
```

---

## Anti-Halüsinasyon Güvencesi

Her sentez noktası izlenebilir:

```
Konsensüs iddiası: "Para politikası aktarımı güçlenir"

Kaynak izleme:
→ BIS (2023), s. 22: "[tam alıntı]" ✅ notes/BIS_2023.md'de
→ Niepelt (2020), s. 8: "[tam alıntı]" ✅ notes/Niepelt_2020.md'de
→ Kumhof (2021), s. 15: "[tam alıntı]" ✅ notes/Kumhof_2021.md'de

Sentez: kaynaklı ✅ — Iron Rule 1 ihlali yok
```

Kaynak izlenemeyen sentez → `[Source: Unverified — notları kontrol et]`
