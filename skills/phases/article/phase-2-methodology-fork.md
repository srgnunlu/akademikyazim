---
title: "Phase 2 — Methodology Fork (Article)"
title_tr: "Aşama 2 — Metodoloji Çatalı (Makale)"
node_type: phase-fork
phase_number: 2
document_type: article
phase_gate_in: "phase-2-reading.md"
phase_gate_out: "phase-3-argument.md"
description: "Methodology fork for empirical articles: quantitative (2-Q), qualitative (2-Ql), or mixed-methods (2-M) sub-phase. Triggered after reading phase if research design involves primary data collection. Non-empirical (theoretical/literature-based) articles skip this phase."
description_tr: "Ampirik makaleler için metodoloji çatalı: nicel (2-Q), nitel (2-Ql) veya karma yöntem (2-M) alt fazı. Araştırma tasarımı birincil veri toplamayı içeriyorsa okuma fazının ardından tetiklenir. Ampirik olmayan (teorik/literatür tabanlı) makaleler bu fazı atlar."
tags: [phase, article, methodology, empirical, quantitative, qualitative, mixed-methods, fork]
outputs:
  - "METODOLOJI.md (research design document)"
  - "data_collection_plan.md (if applicable)"
links_to:
  - skills/core/iron-rules.md
  - skills/core/anti-hallucination.md
  - skills/core/agent-orchestration.md
language: bilingual
version: "1.0"
---

# Aşama 2 — Metodoloji Çatalı / Methodology Fork (Article)

## Çatal Kararı / Fork Decision

Bu faz yalnızca **ampirik makaleler** için geçerlidir. Önce şunu sor:

```
Makaleniz birincil veri toplamayı (anket, deney, görüşme, gözlem,
veri seti analizi) içeriyor mu?

A) Evet, nicel veri / Yes, quantitative data  → Aşama 2-Q
B) Evet, nitel veri  / Yes, qualitative data  → Aşama 2-Ql
C) Evet, karma yöntem / Yes, mixed methods    → Aşama 2-M
D) Hayır, teorik/literatür tabanlı            → Metodoloji çatalı atla → Aşama 3
```

---

## Aşama 2-Q — Nicel Yol / Quantitative Path

### Araştırma Tasarımı

```markdown
# METODOLOJI.md

## Araştırma Tasarımı
- Tasarım türü: [deneysel / yarı-deneysel / korelasyonel / kesitsel / boylamsal]
- Hipotezler: [H0 ve H1 veya araştırma soruları]

## Örneklem
- Hedef popülasyon: [...]
- Örnekleme yöntemi: [olasılıklı / amaçlı / kolaylık]
- Tahmini n: [...]
- Güç analizi: [G*Power sonucu: d=[...], α=[...], güç=[...]]

## Veri Toplama
- Araç: [anket / test / ölçek / mevcut veri tabanı]
- Ölçek kaynağı: [kaynak + güvenilirlik/geçerlik bilgisi]

## Analiz Planı
- Temel analiz: [t-testi / ANOVA / regresyon / SEM / ...]
- Yazılım: [SPSS / R / Python (statsmodels)]
- Raporlama standardı: [APA 7 istatistik formatı]
```

**Methodology Checker tetikle:**
```bash
python3 agents/run.py methodology_checker \
  --input METODOLOJI.md \
  --research-question "..." \
  --field [alan] \
  --document-type article
```

### Geçiş Kapısı (2-Q → 3)

- [ ] Araştırma sorusu ≤ 3 test edilebilir hipoteze indirgendi
- [ ] Örneklem büyüklüğü güç analizi ile hesaplandı ve kaynaklı
- [ ] Kullanılacak ölçekler/araçlar belirlendi ve `/sources/` klasöründe
- [ ] Etik onay gereksinimi değerlendirildi (IRB / etik kurul)
- [ ] Methodology Checker skoru ≥ 60

---

## Aşama 2-Ql — Nitel Yol / Qualitative Path

### Araştırma Tasarımı

```markdown
# METODOLOJI.md

## Araştırma Tasarımı
- Yaklaşım: [fenomenoloji / grounded theory / etnografi / içerik analizi / söylem analizi / vaka çalışması]
- Ontoloji / Epistemoloji: [yorumsamacı / eleştirel / yapılandırmacı / ...]

## Katılımcılar
- Örnekleme stratejisi: [amaçlı / kartopu / teorik örnekleme]
- Dahil etme / dışlama kriterleri: [...]
- Tahmini katılımcı sayısı: [8-15 görüşme / doygunluğa kadar]

## Veri Toplama
- Yöntem: [yarı yapılandırılmış görüşme / odak grup / gözlem / belge analizi]
- Araç: [görüşme protokolü — ek olarak verilecek]

## Analiz
- Analiz yöntemi: [tematik analiz / IPA / grounded theory kodlama]
- Yazılım: [NVivo / ATLAS.ti / Manuel]
- Güvenilirlik: [üye kontrolü / araştırmacı yansıtması / çift kodlama]
```

### Geçiş Kapısı (2-Ql → 3)

- [ ] Metodolojik yaklaşım araştırma sorusuyla tutarlı (epistemolojik hizalama)
- [ ] Veri toplama protokolü taslağı hazır
- [ ] Etik onay / aydınlatılmış onam planı var
- [ ] Güvenilirlik stratejisi belirlendi

---

## Aşama 2-M — Karma Yöntem / Mixed Methods Path

```markdown
# METODOLOJI.md

## Karma Yöntem Tasarımı
- Desen: [açıklayıcı sıralı (QUAN → qual) / keşifsel sıralı (qual → QUAN) / eş zamanlı üçgenleme]
- Nicel ağırlığı: [QUAN/qual veya eşit]
- Entegrasyon noktası: [veri toplama / analiz / yorum]

## Sıralı ise:
- Faz 1: [nicel bileşen — bkz. 2-Q formatı]
- Faz 2: [nitel bileşen — bkz. 2-Ql formatı]
- Entegrasyon: [nicel bulgular nitel soruları nasıl şekillendiriyor?]
```

### Geçiş Kapısı (2-M → 3)

- [ ] Her iki bileşen için 2-Q ve 2-Ql kapı kriterlerini ayrı ayrı karşıla
- [ ] Entegrasyon noktası tasarımda açık
- [ ] Zaman çizelgesi gerçekçi (karma yöntem serisi daha uzun sürer)

---

## Anti-Halüsinasyon Notu (Methodology)

Metodoloji bölümünde AI önerisi içeren her madde Iron Rule M'e tabidir:

- İstatistiksel güç analizi → G*Power veya belirli bir çalışma atfıyla
- Örneklem büyüklüğü önerileri → kaynaklı norm gerektirir
- Güvenilirlik katsayısı eşikleri → APA / alan spesifik rehber atfı
- Raporlama standartları → CONSORT, STROBE, COREQ vb. doğrudan atıf

Kaynak gösterilemeyen metodoloji tavsiyesi: `[Source: Unverified]` etiketi.
