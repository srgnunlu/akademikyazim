---
title: "Statistical Analysis Tools Node"
title_tr: "İstatistiksel Analiz Araçları Düğümü"
node_type: tooling
description: "R vs Python (statsmodels, scipy) for academic stats, APA style statistical reporting format (t(df) = X, p = .XX, d = .XX), power analysis (G*Power), effect size reporting conventions."
description_tr: "Akademik istatistik için R ve Python (statsmodels, scipy) karşılaştırması, APA istatistik raporlama formatı (t(df) = X, p = .XX, d = .XX), güç analizi (G*Power), etki büyüklüğü raporlama konvansiyonları."
tags: [tooling, statistics, r, python, apa, power-analysis, effect-size, reporting]
links_to:
  - skills/phases/article/phase-2-methodology-fork.md
  - skills/core/iron-rules.md
  - skills/core/anti-hallucination.md
language: bilingual
version: "1.0"
---

# İstatistiksel Analiz Araçları / Statistical Analysis Tools

## R mi Python mi? / R or Python?

| Kriter | R | Python |
|--------|---|--------|
| **Akademik istatistik** | ✅ Standart (psych, lavaan, lme4) | ✅ statsmodels, scipy, pingouin |
| **Veri manipülasyonu** | tidyverse (güçlü) | pandas (daha geniş ekosistem) |
| **Makine öğrenmesi** | caret / tidymodels | sklearn (üstün) |
| **Görselleştirme** | ggplot2 (akademik standart) | matplotlib, seaborn |
| **Raporlama** | R Markdown / Quarto | Jupyter, Quarto |
| **SEM / CFA** | lavaan ✅ | semopy (gelişmekte) |
| **Çok değişkenli** | MANOVA, HLM: doğal | scipy, pingouin ile mümkün |
| **Psikoloji/Tıp** | Tercih edilen | |
| **Ekonometri** | quantreg, plm | statsmodels (güçlü) |

**Karar kuralı:** Alan standardına bak. Psikoloji → R. Ekonometri → Python veya Stata. CS → Python. İkisi de kabul edilir; tutarlı ol.

---

## APA 7 İstatistik Raporlama Formatı

### t-testi
```
t(df) = değer, p = .XX, d = .XX, 95% CI [alt, üst]

Örnek: t(48) = 3.24, p = .002, d = 0.91, 95% CI [0.38, 1.44]
```

### ANOVA
```
F(df_between, df_within) = değer, p = .XX, η² = .XX

Örnek: F(2, 87) = 8.42, p < .001, η² = .16
```

### Korelasyon
```
r(df) = .XX, p = .XX, 95% CI [alt, üst]

Örnek: r(98) = .43, p < .001, 95% CI [.26, .58]
```

### Regresyon
```
β = .XX, SE = .XX, t(df) = XX, p = .XX

Model: R² = .XX, F(df1, df2) = XX, p = .XX
```

### Ki-kare
```
χ²(df, N = XX) = değer, p = .XX, φ = .XX (veya Cramér's V)
```

**APA kuralları:**
- p değerleri: tam değer yaz (p = .043), p < .001 kullan (p = .000 değil)
- Küçük sayılar: 0 olmadan başla (.43, .001 — 0.43 değil)
- df parantez içinde, italik

---

## Etki Büyüklüğü / Effect Size

| Test | Etki büyüklüğü | Küçük | Orta | Büyük |
|------|----------------|-------|------|-------|
| t-testi | Cohen's d | .20 | .50 | .80 |
| ANOVA | η² veya ω² | .01 | .06 | .14 |
| Korelasyon | r | .10 | .30 | .50 |
| Ki-kare | Cramér's V | .10 | .30 | .50 |
| Regresyon | f² | .02 | .15 | .35 |

**Kaynak:** Cohen (1988) — *Statistical Power Analysis for the Behavioral Sciences*.

---

## Güç Analizi / Power Analysis

**G*Power** (ücretsiz, GUI): [gpower.hhu.de](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower)

Standart giriş parametreleri:
- α = .05 (Tip I hata)
- Güç (1-β) = .80 (Tip II hata önleme)
- Beklenen etki büyüklüğü → alandan tahmin et veya pilot çalışma

**Python ile G*Power muadili:**
```python
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()
n = analysis.solve_power(effect_size=0.5, alpha=0.05, power=0.80)
print(f"Gerekli n (her grup): {n:.0f}")
```

---

## Raporlama Standartları / Reporting Standards

| Alan | Standart | Kaynak |
|------|----------|--------|
| Psikoloji | APA 7 + JARS | APA Publication Manual |
| Tıp / Klinik | CONSORT, STROBE | equator-network.org |
| Nitel | COREQ, SRQR | equator-network.org |
| Sistematik Derleme | PRISMA 2020 | prisma-statement.org |
| SEM/CFA | MacCallum kriterleri | MacCallum et al. (1996) |

---

## TezAtlas Entegrasyonu

Faz 2-Q metodoloji belgesine şu alanları ekle:
```yaml
analysis:
  software: "R 4.3.2 / Python 3.11"
  packages: ["lavaan", "tidyverse"]
  reporting_standard: "APA 7"
  power_analysis: "G*Power 3.1.9.7, d=0.50, α=.05, power=.80, n=128"
  effect_size_type: "Cohen's d"
```
