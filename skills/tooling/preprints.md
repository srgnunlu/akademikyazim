---
title: "Preprint Strategy Node"
title_tr: "Önbaskı Strateji Düğümü"
node_type: tooling
description: "When to post a preprint (before/after submission), which server (arXiv, SSRN, bioRxiv, EarthArXiv, SSOAR), embargo policies, journal double-submission rules, DOI and version management."
description_tr: "Önbaskı ne zaman yayınlanır (gönderim öncesi/sonrası), hangi sunucu (arXiv, SSRN, bioRxiv, EarthArXiv, SSOAR), ambargo politikaları, dergi çift gönderim kuralları, DOI ve sürüm yönetimi."
tags: [tooling, preprint, arxiv, ssrn, open-access, doi, version-management]
links_to:
  - skills/techniques/publication-strategist.md
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Önbaskı Strateji Düğümü / Preprint Strategy Node

## Önbaskı Nedir? / What is a Preprint?

Önbaskı (preprint), hakemli yayın sürecinden **önce** açık erişimle yayınlanan çalışma versiyonudur. Peer review olmaksızın yayınlanır; ancak günümüzde birçok dergi, hakemli yayından önce önbaskı yayınlanmasına izin vermektedir.

---

## Ne Zaman Yayınlanır? / When to Post?

| Strateji | Durum | Öneri |
|----------|-------|-------|
| **Gönderim öncesi** | Hız kritik (tartışmayı başlatmak), fikirsel öncelik önemli | arXiv, SSRN — uygun |
| **Gönderim sırasında** | Çoğu dergi kabul eder | Dergi politikasını kontrol et |
| **Kabul sonrası** | Ambargolu dergiler | Accepted manuscript versiyonunu kullan |
| **Yayın sonrası** | Kapalı erişim dergi | Sherpa/RoMEO ile izin kontrol et |

**Önce kontrol:** [Sherpa/RoMEO](https://www.sherpa.ac.uk/romeo/) — derginin önbaskı politikası.

---

## Sunucu Seçimi / Server Selection

| Sunucu | Disiplinler | Özellikler |
|--------|-------------|------------|
| **arXiv** | Fizik, Mat, CS, Ekonomi, q-bio | Kalıcı arXiv ID, moderasyon var, çok hızlı |
| **SSRN** | Hukuk, Ekonomi, İşletme, Sosyal | Geniş kapsam, Elsevier platformu |
| **bioRxiv / medRxiv** | Biyoloji, Tıp, Sağlık | Cold Spring Harbor, ORCID entegrasyonu |
| **EarthArXiv** | Yer ve Uzay Bilimleri | OSF altyapısı |
| **SocArXiv** | Sosyal Bilimler | OSF altyapısı, açık peer review |
| **SSOAR** | Sosyal Bilimler (Almanca ağırlıklı) | GESIS, Türk çalışmaları için uygun |
| **OSF Preprints** | Genel | Disiplin agnostik, proje deposu ile entegre |
| **PsyArXiv** | Psikoloji, Davranış | Preregistration ile birlikte kullan |

---

## Derginin Politikasını Kontrol / Journal Policy Check

**Yasak politikalar (nadir ama var):**
- Nature dergilerinin bir kısmı: gönderim öncesi önbaskı = ön yayın sayılır → RED
- Bazı tıp dergileri: medRxiv hariç önbaskı kabul etmez

**Kontrol adımları:**
1. Dergi web sitesinde "Preprint policy" ara
2. Sherpa/RoMEO'dan dergiyi sorgula
3. Şüpheli durumlarda editöre e-posta ile sor

---

## DOI ve Sürüm Yönetimi / DOI and Version Management

```
Sürüm 1 → önbaskı DOI: 10.48550/arXiv.XXXX.XXXXX
Sürüm 2 → revize edildi (hakem geribildirimi sonrası)
Sürüm 3 → accepted manuscript

Her sürüm: aynı DOI, farklı timestamp
```

**Temel kural:** Önbaskı DOI ≠ yayın DOI. İkisini de atıf listesine ekle.

**Sürüm notları:** Her versiyona kısa bir "Changes from v1" notu ekle.

---

## TezAtlas Entegrasyonu

- Önbaskı yayınlanınca `STATUS.md`'ye `preprint_doi` alanı ekle
- `KAYNAK_ENVANTERI.md`'de önbaskı versiyonlarını `preprint` olarak etiketle
- Önbaskı alıntılarken: `[Yazar(lar), Yıl, preprint — hakemli değil]` notu ekle

---

## Türkiye'ye Özel Notlar

- **YÖK**: Önbaskı tez jüri sürecinde kaynak olarak kabul edilebilir, ancak "[Preprint]" etiketi zorunlu
- **TÜBİTAK**: 1001/1003 projelerinde önbaskı yayın sayılır (2023 sonrası güncelleme)
- Türkçe önbaskı için: **SSOAR** veya **OSF Preprints** önerilir (DergiPark önbaskı kabul etmez)
