---
title: "Anti-Hallucination Protocol for Methodology Advice"
title_tr: "Metodoloji Tavsiyeleri İçin Anti-Halüsinasyon Protokolü"
node_type: core
description: "Iron Rule variant: no methodology advice without a traceable source. Applies to statistical test selection, IRB requirements, reporting standards, sample size calculations, and all methodological guidance given by AI."
description_tr: "Demir Kural türevi: izlenebilir kaynak olmadan metodoloji tavsiyesi verilmez. İstatistiksel test seçimi, IRB gereksinimleri, raporlama standartları, örneklem büyüklüğü hesaplamaları ve AI tarafından verilen tüm metodolojik rehberlik için geçerlidir."
tags: [core, anti-hallucination, methodology, iron-rules, source-verification]
links_to:
  - skills/core/iron-rules.md
  - skills/core/quality-control.md
  - skills/core/agent-orchestration.md
language: bilingual
version: "1.0"
---

# Anti-Hallucination Protocol — Methodology Advice
# Anti-Halüsinasyon Protokolü — Metodoloji Tavsiyeleri

## The Rule / Kural

**EN:** Every piece of methodology advice given by TezAtlas (or by any AI agent in the system) must cite a specific, verifiable source — not LLM memory. This is Iron Rule 1's methodology equivalent.

> **Iron Rule M: No methodology advice without a traceable source.**

**TR:** TezAtlas (veya sistemdeki herhangi bir AI agent'ı) tarafından verilen her metodoloji tavsiyesi, LLM belleğine değil belirli, doğrulanabilir bir kaynağa dayanmalıdır.

> **Demir Kural M: İzlenebilir kaynak olmadan metodoloji tavsiyesi verilmez.**

---

## Why This Rule Exists / Bu Kural Neden Var

**EN:** Methodology advice is high-stakes. Wrong statistical test choices, missed IRB requirements, or non-compliant reporting invalidate research at publication or ethics review. LLMs can generate plausible-sounding but incorrect methodology advice with high confidence. The source requirement forces the system to ground advice in verified standards rather than probabilistic text generation.

**TR:** Metodoloji tavsiyeleri yüksek risklidir. Yanlış istatistiksel test seçimleri, kaçırılan IRB gereksinimleri veya uyumsuz raporlama; yayın veya etik incelemede araştırmayı geçersiz kılar. LLM'ler yüksek güvenle kulağa makul gelen ama yanlış metodoloji tavsiyeleri üretebilir. Kaynak zorunluluğu, sistemi olasılıksal metin üretimi yerine doğrulanmış standartlara dayandırmaya zorlar.

---

## High-Risk Zones / Yüksek Riskli Alanlar

These are the areas where AI methodology hallucination is most dangerous:

| Zone | Examples | Required Source Type |
|------|----------|---------------------|
| Statistical tests | "Use ANOVA because..." | Textbook / stats methodology paper |
| Sample size / power | "n=30 is sufficient" | Power analysis formula + study |
| IRB / Ethics requirements | "You need consent forms if..." | Institutional guidelines / regulatory document |
| Reporting standards | "CONSORT requires item X" | Reporting guideline document (CONSORT, STROBE, PRISMA, etc.) |
| Qualitative methods | "Saturation is reached when..." | Methodological literature (e.g., Guest et al., 2006) |
| Effect sizes | "Cohen's d=0.5 is medium" | Cohen (1988) or equivalent |
| Validity/reliability | "Cronbach alpha > 0.7 means..." | Methodological textbook |

---

## Compliance Rules / Uyum Kuralları

**Rule M-1: Cite the Standard, Not Memory**

When TezAtlas gives methodology advice, it must explicitly state:
- Which source/standard the advice derives from
- Whether that standard is available in `/sources/` or is a well-known external reference

```
CORRECT: "CONSORT 2010 requires items 6a and 11a for your RCT description.
          (Source: Schulz et al., 2010 — CONSORT 2010 Statement)"

WRONG:   "You need to report randomization details because that's standard practice."
```

**Rule M-2: Hallucination Risk Score**

All methodology advice carries a risk tag:
- `[Source: /sources/file.pdf, p.X]` — confirmed in local source
- `[Source: External standard — CONSORT/APA/etc.]` — well-known verifiable standard
- `[Source: Unverified — treat as suggestion only]` — LLM memory only, not a definitive source

**Rule M-3: No Fake Statistics**

TezAtlas must NEVER generate fake statistics, effect sizes, p-values, or sample size calculations. If a user asks for a specific number (e.g., "what should my sample size be?"), TezAtlas must:
1. Name the appropriate formula/tool (G*Power, power analysis formula)
2. Ask for the parameters needed (effect size, alpha, power, test type)
3. Walk through the calculation with the formula — not invent a number

**Rule M-4: Methodology Agent Must Cite Sources**

When the Methodology Checker Agent (`agents/core/methodology_checker.py`) flags issues, its system prompt requires sourced recommendations. If the agent's output contains unsourced recommendations, Claude Code must flag them as `[Source: Unverified]` before presenting to the user.

---

## Enforcement Points / Uygulama Noktaları

| Phase | Trigger | Check |
|-------|---------|-------|
| Phase 3/5 (Thesis) | AI gives methodology recommendation | Rule M-1: cite source |
| Phase 3 (Article) | AI suggests statistical approach | Rule M-1 + M-3 |
| Phase 2-3 (Grant) | AI advises on methodology section | Rule M-1 |
| Any phase | AI mentions reporting standards | Rule M-2: external standard citation |
| Agent output | Methodology Checker flagging issues | Rule M-4: sourced recommendations only |
| Quality control | Pre-finalization check | Scan all AI methodology statements |

---

## What TezAtlas Does When It Lacks a Source / Kaynak Yoksa

```
User asks: "What statistical test should I use?"

Response pattern:
1. Identify the question type (comparison? correlation? prediction?)
2. Name the decision framework (flowchart, Field 2013, or equivalent)
3. Walk through the decision with the user — questions, not declarations
4. If a specific test is recommended: cite a textbook or paper
5. If unsure: "I'm not certain which test applies here without a source.
   Recommend consulting [Field, 2013] or a statistician."
```

**TR:** Kaynak yoksa TezAtlas kesin öneride bulunmaz; karar çerçevesini paylaşır, soruları yönlendirir ve kaynak için referans gösterir.

---

## Integration with Quality Control / Kalite Kontrolüyle Entegrasyon

Before any phase gate involving methodology, run this check:

```
[ ] All AI methodology advice in this phase has a cited source
[ ] No specific statistics invented without formula or data
[ ] Reporting standard requirements cited to actual standards
[ ] Methodology Checker agent outputs tagged with source status
[ ] Any [Source: Unverified] items flagged to user for independent verification
```
