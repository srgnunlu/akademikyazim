---
title: "TezAtlas Exchange — Community Ecosystem"
title_tr: "TezAtlas Değişim Platformu — Topluluk Ekosistemi"
node_type: core
description: "Community marketplace for discipline-specific workflow packs, phase templates, prompt libraries, custom skill nodes. CC-licensed templates. AI-assisted curation. Direct import into core system. Network effect."
description_tr: "Disipline özgü iş akışı paketleri, faz şablonları, prompt kütüphaneleri, özel skill düğümleri için topluluk pazaryeri. CC lisanslı şablonlar. AI destekli kürasyon. Çekirdek sisteme doğrudan import. Ağ etkisi."
tags: [core, exchange, community, marketplace, plugin, discipline-packs, network-effect]
links_to:
  - skills/core/plugin-system.md
  - skills/core/web-version-roadmap.md
language: bilingual
version: "1.0"
---

# TezAtlas Değişim Platformu / TezAtlas Exchange

## Vizyon / Vision

TezAtlas'ı tek bir çekirdek sistemden, araştırmacı topluluğunun katkı yaptığı bir **iş akışı ekosistemine** dönüştürmek.

**Temel fikir:** Bir klinisyen sistematik derleme için optimize edilmiş bir TezAtlas paketi oluşturdu → onu paylaşıyor → başka klinisyenler indiriyor → paket iyileştiriliyor. Çekirdek ekibin kapasitesinin ötesinde kapsam genişlemesi.

---

## Paket Türleri / Package Types

### 1. Disiplin Paketleri (Discipline Packs)
Alana özgü iş akışları:
- `clinical-systematic-review/` — PRISMA, Cochrane standartları
- `turkish-law-thesis/` — YÖK + UYAP uyumlu hukuk tezi
- `stem-reproducibility/` — Docker + Jupyter + preregistration

### 2. Faz Şablonları (Phase Templates)
Standart faz şablonlarının disipline özel versiyonları:
- `phase-3-reading-humanities.md` — beşeri bilimler okuma protokolü
- `phase-4-outline-social.md` — sosyal bilim yapı şablonu

### 3. Prompt Kütüphaneleri (Prompt Libraries)
Alanına özel soru paketleri:
- `devils-advocate-law.md` — hukuk tezi için Şeytan'ın Avukatı soruları
- `methodology-checker-clinical.md` — klinik araştırma metodoloji kontrol

### 4. Skill Düğümleri (Custom Nodes)
Topluluk katkılı ek node'lar:
- `skills/community/[kullanıcı-adı]/[node-adı].md`

---

## Yaşam Döngüsü / Lifecycle

```
Araştırmacı
    │
    ├─ Paket oluşturur
    │   └─ tezatlas-plugin.json manifest yazar
    │   └─ skills/ ve templates/ ekler
    │   └─ GitHub repo'ya push eder
    │
    ├─ Exchange'e gönderir
    │   └─ Otomatik doğrulama (frontmatter, bağlantılar)
    │   └─ AI kalite taraması (Iron Rule uyumu)
    │   └─ Topluluk incelemesi (opsiyonel)
    │
    └─ Yayınlanır
        └─ CC BY 4.0 lisansıyla
        └─ Sürüm yönetimi (semantic versioning)
        └─ Bağımlılık takibi
```

---

## Kurulum Modeli / Installation Model

**Basit yol (git clone):**
```bash
git clone https://github.com/tezatlas-exchange/clinical-systematic-review \
  skills/community/clinical-systematic-review
```

**Gelecekteki CLI (planlı):**
```bash
tezatlas install clinical-systematic-review
tezatlas install @username/custom-pack
tezatlas list-installed
tezatlas update --all
```

---

## Kalite Güvencesi / Quality Assurance

Exchange'de yayınlanan her paket için:

```
Otomatik:
□ Frontmatter şema doğrulaması
□ links_to referansları geçerli mi?
□ Iron Rule 1 uyumu (kaynak olmadan iddia var mı?)
□ Dil tutarlılığı

Topluluk:
□ Disiplin uzmanı incelemesi (opsiyonel rozetler)
□ Kullanıcı puanlaması ve yorumlar
□ Hata bildirimleri
```

---

## Lisanslama / Licensing

- Tüm Exchange paketleri **Creative Commons BY 4.0** (minimum)
- Ticari kullanıma izin verilir — atıf zorunlu
- Katkı yapanın GitHub kullanıcı adı paket adında kalır
- TezAtlas çekirdek ekibi paketleri değiştirmez — fork ederek dallanma

---

## Uygulama Yol Haritası / Implementation Roadmap

| Faz | Ne? | Ne Zaman? |
|-----|-----|-----------|
| Faz 1 | GitHub-based manuel paketler + README protokolü | Şimdi |
| Faz 2 | tezatlas-plugin.json standardı + doğrulama script | tezatlas.com Faz 2 ile |
| Faz 3 | Exchange web arayüzü + arama | tezatlas.com Faz 3 ile |
| Faz 4 | CLI install komutu + bağımlılık yönetimi | tezatlas.com Faz 4 ile |

**Şu an:** `skills/community/` klasörünü oluşturarak topluluk paketleri manuel olarak eklenebilir.
