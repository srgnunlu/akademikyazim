---
title: "Plugin / Extension System"
title_tr: "Eklenti / Uzantı Sistemi"
node_type: core
description: "Formalize the skills/ modular structure: tezatlas-plugin.json manifest, validator script, install command, namespace isolation. Enables community contributions without core maintainer bottleneck."
description_tr: "skills/ modüler yapısını resmileştir: tezatlas-plugin.json manifest, doğrulayıcı script, kurulum komutu, isim alanı izolasyonu. Çekirdek bakımcı darboğazı olmaksızın topluluk katkısına olanak tanır."
tags: [core, plugin-system, extension, manifest, validator, community, namespace]
links_to:
  - skills/core/tezatlas-exchange.md
  - scripts/check_frontmatter.py
language: bilingual
version: "1.0"
---

# Eklenti / Uzantı Sistemi / Plugin System

## Mevcut Durum / Current State

`skills/` klasörü modülerdir — her `.md` dosyası bağımsız bir node. Ancak üçüncü taraf katkılar için formal bir API yoktur. Bu belge eklenti sistemini tanımlar.

---

## tezatlas-plugin.json Manifestosu

Her eklenti paketinin kökünde bulunmalı:

```json
{
  "name": "clinical-systematic-review",
  "version": "1.2.0",
  "description": "Systematic review workflow for clinical researchers (Cochrane/PRISMA)",
  "author": "github-username",
  "license": "CC-BY-4.0",
  "tezatlas_version": ">=1.0.0",
  "namespace": "clinical",
  "nodes": [
    "skills/community/clinical/phase-2-prisma.md",
    "skills/community/clinical/phase-3-cochrane-reading.md",
    "skills/community/clinical/templates/tpl-prisma-flow.md"
  ],
  "dependencies": [],
  "conflicts": [],
  "tags": ["clinical", "systematic-review", "prisma", "cochrane"],
  "repository": "https://github.com/username/tezatlas-clinical-sr"
}
```

---

## Namespace İzolasyonu / Namespace Isolation

Çakışmaları önlemek için:

```
Çekirdek nodes:     skills/core/*, skills/phases/*, skills/techniques/*
Topluluk nodes:     skills/community/[namespace]/[node].md
Kullanıcı nodes:    skills/local/[node].md  (gitignore'da tutulabilir)
```

**Kurallar:**
- Topluluk node'ları çekirdek node'ları override edemez
- `links_to` referansları tam yol kullanmalı
- Namespace = tezatlas-plugin.json'daki `namespace` alanı

---

## Doğrulama Scripti / Validator Script

`scripts/validate_plugin.py`:

```bash
python3 scripts/validate_plugin.py path/to/plugin/

# Çıktı:
✅ Manifest geçerli (tezatlas-plugin.json)
✅ Tüm node dosyaları mevcut (3/3)
✅ Frontmatter şema uyumlu
✅ links_to referansları çözümlendi
⚠️  WARNING: 'skills/techniques/ocr.md' referansı → mevcut değil
✅ Namespace çakışması yok ('clinical' temiz)
✅ Iron Rule 1 uyumu taraması temiz

Özet: 1 uyarı, 0 hata
Plugin kuruluma hazır (uyarıları gözden geçirin)
```

---

## Kurulum / Installation

### Manuel (şu an desteklenen):

```bash
# Klonla
git clone https://github.com/username/tezatlas-clinical-sr \
  skills/community/clinical-systematic-review

# Doğrula
python3 scripts/validate_plugin.py skills/community/clinical-systematic-review/

# Kullan (Claude Code'da)
# Plugin otomatik tanınır — skills/ klasöründe zaten
```

### CLI (gelecekte planlanan):

```bash
tezatlas install clinical-systematic-review
tezatlas install @username/custom-pack --version 1.2.0
tezatlas list-installed
tezatlas remove clinical-systematic-review
tezatlas update --all
```

---

## Eklenti Geliştirme Rehberi / Plugin Development Guide

### Minimum gereksinimler:

1. **tezatlas-plugin.json** — manifest dosyası
2. **skills/community/[namespace]/** — node dosyaları (frontmatter zorunlu)
3. **README.md** — kurulum ve kullanım
4. **LICENSE** — CC BY 4.0 önerilir

### Frontmatter zorunlu alanları (topluluk node'ları):

```yaml
---
title: "..."
title_tr: "..."  # Türkçe başlık opsiyonel ama önerilir
node_type: technique  # veya core / tooling / template / phase-fork
description: "..."
tags: [community, namespace-adı, ...]
language: bilingual  # veya tr / en
version: "1.0"
---
```

### Test etme:

```bash
python3 scripts/validate_plugin.py .
python3 -m pytest tests/ -q  # Çekirdek testler hâlâ geçmeli
```

---

## Güvenlik Modeli / Security Model

- Plugin'ler yalnızca `.md` dosyaları ve `tezatlas-plugin.json` içerebilir
- Python veya shell script içeren plugin'ler kabul edilmez (Exchange kuralı)
- Claude Code zaten sandbox — plugin'ler kod çalıştıramaz
- Güven modeli: kullanıcı kaynak kodu görebilir (markdown), kör kurulum yok
