---
title: "Saturation Check — When to Stop Reading"
title_tr: "Doygunluk Kontrolü — Okumayı Ne Zaman Durduracaksın"
node_type: technique
description: "Algorithm for detecting reading saturation in Phase 3. Run every 5 sources. Compares new-argument counts between last two batches — when new argument count approaches zero, saturation is reached."
description_tr: "Faz 3'te okuma doygunluğunu tespit etme algoritması. Her 5 kaynakta bir çalıştır. Son iki grubun yeni argüman sayılarını karşılaştırır — yeni argüman sayısı sıfıra yaklaştığında doygunluk var."
tags: [saturation-check, doygunluk, reading-loop, stopping-criterion, phase-3]
links_to:
  - skills/phases/thesis/phase-3-reading.md
  - skills/phases/thesis/phase-4-structure.md
used_by:
  - skills/phases/thesis/phase-3-reading.md
  - skills/techniques/snowball-sampling.md
language: bilingual
version: "2.0"
---

# Doygunluk Kontrolü / Saturation Check

## Algoritma

Her 5 kaynak okunduktan sonra `OKUMA_RAPORU.md` güncelle ve değerlendir:

```
OKUMA_RAPORU.md:
  Toplam okunan kaynak: [X]
  Son 5 kaynakta yeni argüman: [Y]
  Önceki 5 kaynakta yeni argüman: [Z]

  Y < Z  → Azalma trendi → doygunluğa yaklaşılıyor
  Y ≈ 0  → Doygunluk → Faz 4'e geçilebilir
  Y ≥ Z  → Hâlâ yeni şeyler öğreniliyor → okumaya devam
```

## Doygunluk Kriterleri

"Yeni argüman" sayılır — eğer son 5 kaynakta:
- Yeni teorik çerçeve çıkmadıysa
- Yeni metodolojik yaklaşım görülmediyse
- Tezin temel argümanını değiştiren bir bulgu yoksa
- Kartopu ile keşfedilen yeni sources artık filtrelerden geçmiyorsa

→ Doygunluk sinyali

## Faz 4'e Geçiş Kararı

Doygunluk teyit edildikten sonra `OKUMA_RAPORU.md`'ye kaydet:
```markdown
## Doygunluk Tespiti
Tarih: [tarih]
Toplam okunan: [X] kaynak
Kararın gerekçesi: [neden doygunluk sinyali]
Faz 4'e geçiş: ONAYLANDI
```

Ardından [[phase-4-structure]]'a geç.
