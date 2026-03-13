---
title: "Research Career Graph — Longitudinal Tracking"
title_tr: "Araştırma Kariyer Grafiği — Uzun Vadeli Takip"
node_type: core
description: "Track researcher activity across projects and years: methodologies used, publication trajectory, skill gaps, recurring themes, writing quality evolution. AI offers increasingly personalized guidance based on career history."
description_tr: "Araştırmacı aktivitesini projeler ve yıllar boyunca takip et: kullanılan metodolojiler, yayın yörüngesi, beceri boşlukları, tekrarlayan temalar, yazım kalitesi gelişimi. AI kariyer geçmişine dayalı giderek kişiselleşen rehberlik sunar."
tags: [core, career-graph, longitudinal, tracking, personalization, skill-gap, publication-trajectory]
links_to:
  - skills/core/session-continuity.md
  - skills/core/attrition-prevention.md
  - skills/techniques/publication-strategist.md
language: bilingual
version: "1.0"
---

# Araştırma Kariyer Grafiği / Research Career Graph

## Vizyon / Vision

TezAtlas'ı tek projeden çok bir araçtan **kariyer boyu araştırma ortağına** dönüştüren özellik. Her tamamlanan proje, araştırmacı profili için veri üretir — ve bu veri bir sonraki projede daha iyi rehberlik sağlar.

---

## Kariyer Grafiği Veri Yapısı / Career Graph Data Structure

`CAREER_PROFILE.md` (proje kök dizininin üstünde, araştırmacı genelinde):

```yaml
researcher_profile:
  name: "[ARAŞTIRMACI ADI]"
  field: "Ekonomi / Kamu Yönetimi"
  created: "2024-09-01"
  last_updated: "2026-02-27"

completed_projects:
  - id: "proj_001"
    type: thesis
    title: "CBDC ve Para Politikası"
    started: "2024-09-01"
    completed: "2026-06-01"
    methodology: ["nicel", "regresyon", "panel-veri"]
    sources_used: 42
    writing_days: 187
    publication: null

  - id: "proj_002"
    type: article
    title: "Dijital Para Birimi Tasarımı"
    started: "2026-07-01"
    completed: null
    methodology: ["teorik", "karşılaştırmalı"]
    sources_used: 18
    writing_days: 34
    publication:
      venue: "Journal of Monetary Economics"
      status: "under_review"

skills:
  methodologies:
    quantitative: used      # used | advanced | never
    qualitative: never
    mixed_methods: never
    systematic_review: never
    case_study: used
  citation_styles:
    apa7: advanced
    chicago: never
    bluebook: never
  software:
    spss: used
    r: never
    python: advanced
    nvivo: never

recurring_themes:
  - "merkez bankası bağımsızlığı"
  - "dijital para politikası"
  - "finansal teknoloji düzenlemesi"

writing_trajectory:
  avg_words_per_session: 412
  longest_streak: 21
  style_score_trend: [62, 68, 71, 75]  # proje bazlı
```

---

## Kariyer Grafiği Önerileri / Career-Based Recommendations

Profil doldukça TezAtlas kişiselleştirir:

```
Kariyer Profili Analizi:

Metodoloji: 2 nicel proje — nitel deneyim yok.
"Dijital Para Tasarımı" projeniz için nitel
boyut eklemek ister misiniz?
→ Uzman görüşmesi veya politika belgesi analizi
  mevcut nicel bulgularınızı tamamlayabilir.

Tema: Merkez bankası bağımsızlığı 3 projede tekrar ediyor.
Bu, güçlü bir araştırma kimliği gösteriyor.
Sistematik derleme için olgun bir alan.
```

---

## Beceri Boşluğu Tespiti / Skill Gap Detection

```
Metodoloji Repertuarınız:
✅ Nicel / regresyon / panel veri
✅ Karşılaştırmalı analiz
❌ Sistematik derleme / meta-analiz (hiç yapılmadı)
❌ Nitel (hiç yapılmadı)
❌ SEM / yapısal eşitlik modellemesi

Bir dahaki proje için öğrenme fırsatı:
Sistematik derleme → mevcut birikimle doğal adım.
```

---

## Yayın Yörüngesi / Publication Trajectory

```
Yayın Haritası:
2024: —
2025: 1 konferans bildirisi (CBDC konferansı)
2026: 1 makale (gönderimde) + 1 tez
2027 Hedef: ?

Mevcut hıza göre: yılda 1-2 çıktı.
Doçentlik başvurusu için hedef:
→ Alanınızda beklenen minimum: [Source: YÖK kriterleri — doğrula]
```

---

## Uygulama Notu / Implementation Note

Bu özellik **faz 1 (mevcut)**: `CAREER_PROFILE.md` manuel tutulur, araştırmacı günceller.

**Faz 2 (gelecek)**: Tamamlanan projelerden otomatik veri çekimi.
**Faz 3 (gelecek)**: Çok cihaz senkronizasyonu / tezatlas.com entegrasyonu.

Şu an için: her proje tamamlandığında `CAREER_PROFILE.md`'yi güncelle.

```bash
# Proje tamamlandığında çalıştır:
python3 scripts/export_career_data.py --project-dir . --output ~/CAREER_PROFILE.md
```

*(Bu script gelecekteki bir geliştirme olarak planlanmaktadır)*
