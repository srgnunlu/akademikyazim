---
title: "Docker / Devcontainer Support"
title_tr: "Docker / Devcontainer Desteği"
node_type: tooling
description: "Single-command reproducible environment. .devcontainer/devcontainer.json for VS Code / GitHub Codespaces. Dockerfile: Python 3.12, PyMuPDF, Tesseract with tur+eng, figlet banner, pre-commit hooks."
description_tr: "Tek komutla tekrarlanabilir ortam. VS Code / GitHub Codespaces için .devcontainer/devcontainer.json. Dockerfile: Python 3.12, PyMuPDF, Türkçe+İngilizce Tesseract, figlet banner, pre-commit hooks."
tags: [tooling, docker, devcontainer, codespaces, reproducibility, windows, onboarding]
links_to:
  - skills/core/data-privacy.md
language: bilingual
version: "1.0"
---

# Docker / Devcontainer Desteği

## Neden? / Why?

TezAtlas şu bağımlılıkları gerektirir:
- Python 3.11+
- PyMuPDF (PDF metin katmanı)
- Tesseract + Türkçe dil paketi (taranmış PDF OCR)
- Pre-commit hooks

Windows veya üniversite yönetimli makinelerde bu kurulum sorunlu olabilir. Docker her şeyi tek seferlik çözer.

---

## VS Code Dev Container (Önerilen)

**Ön koşul:** Docker Desktop + VS Code Remote-Containers eklentisi

```bash
# 1. Repoyu klonla
git clone https://github.com/YOUR_USERNAME/TezAtlas.git
cd TezAtlas

# 2. VS Code'da aç
code .

# 3. VS Code: "Reopen in Container" (sağ altta bildirim çıkar)
# Veya: Ctrl+Shift+P → "Dev Containers: Reopen in Container"

# Ortam otomatik kurulur (~3-5 dakika, ilk kez)
```

**İçinde neler var:**
- Python 3.12 + tüm bağımlılıklar
- Tesseract tur+eng
- Pre-commit hooks kurulu
- VS Code Markdown, Python, YAML eklentileri

---

## GitHub Codespaces

```bash
# GitHub'da: Code → Codespaces → Create codespace on main
# Otomatik .devcontainer/devcontainer.json kullanır
# Tarayıcıda tam geliştirme ortamı
```

Codespaces ücretsiz tier: 60 saat/ay (120 çekirdek-saat)

---

## Docker CLI (Sadece Docker)

```bash
# Image oluştur
docker build -t tezatlas .

# Mevcut dizini bağlayarak çalıştır
docker run -it --rm \
  -v "$(pwd):/workspace" \
  -e GEMINI_API_KEY="..." \
  tezatlas

# OCR çalıştır
docker run --rm \
  -v "$(pwd):/workspace" \
  tezatlas \
  python3 ocr_pipeline.py sources/ --batch --lang tur+eng

# Agents çalıştır
docker run --rm \
  -v "$(pwd):/workspace" \
  -e GEMINI_API_KEY="..." \
  tezatlas \
  python3 agents/run.py --list-providers
```

---

## Windows Özel Notlar

Windows'ta PowerShell ile `$(pwd)` çalışmaz — şunu kullan:
```powershell
docker run -it --rm -v "${PWD}:/workspace" tezatlas
```

Veya WSL2 + Ubuntu tercih et — Unix benzeri ortam.

---

## Dockerfile İçeriği Özeti

```
Python 3.12-slim-bookworm (Debian tabanlı)
├── tesseract-ocr + tur + eng dil paketleri
├── poppler-utils (PDF araçları)
├── git
├── figlet (banner için)
├── PyMuPDF, pytesseract, pyyaml, python-dotenv
├── openai, anthropic, mcp
└── pre-commit
```

---

## Gizlilik Notu

`.env` dosyası container'a kopyalanmaz — `-e VAR=value` veya `--env-file` kullan.

Dockerfile'da API key olmadığından emin ol:
```bash
# Image güvenlik taraması (opsiyonel)
docker run --rm aquasec/trivy image tezatlas
```
