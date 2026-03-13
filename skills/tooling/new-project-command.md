---
title: "Template Scaffolding Command — /tezatlas new"
title_tr: "Şablon İskele Komutu — /tezatlas new"
node_type: tooling
description: "One-command project bootstrap: creates STATUS.md, READING_REPORT.md, ARGUMENTS.md, sources/, notes/, discipline-specific templates. Fast-path for experienced users who already know their parameters."
description_tr: "Tek komutla proje başlatma: STATUS.md, READING_REPORT.md, ARGUMENTS.md, sources/, notes/, disipline özgü şablonlar oluşturur. Parametrelerini bilen deneyimli kullanıcılar için hızlı yol."
tags: [tooling, scaffolding, new-project, bootstrap, cli, fast-path]
links_to:
  - skills/core/session-continuity.md
  - scripts/new_project.py
language: bilingual
version: "1.0"
---

# Şablon İskele Komutu / Template Scaffolding Command

## Hızlı Başlangıç / Quick Start

```bash
# Makale (Türkçe, Hukuk)
python3 scripts/new_project.py \
  --type article \
  --lang tr \
  --field law \
  --title "Yapay Zeka ve Hukuki Sorumluluk"

# Ampirik tez (Ekonomi)
python3 scripts/new_project.py \
  --type thesis \
  --lang both \
  --field economics \
  --empirical \
  --title "CBDC ve Para Politikası" \
  --output ~/tezlerim/cbdc

# Konferans bildirisi (İngilizce, CS)
python3 scripts/new_project.py \
  --type conference \
  --lang en \
  --field computer-science \
  --title "Federated Learning Privacy"
```

---

## Oluşturulan Dosyalar / Created Files

| Dosya | Her zaman | Ampirik (`--empirical`) |
|-------|-----------|------------------------|
| `STATUS.md` | ✅ | ✅ |
| `READING_REPORT.md` | ✅ | ✅ |
| `ARGUMENTS.md` | ✅ | ✅ |
| `sources/` | ✅ | ✅ |
| `notes/` | ✅ | ✅ |
| `cikti/` | ✅ | ✅ |
| `.gitignore` | ✅ (yoksa) | ✅ (yoksa) |
| `METODOLOJI.md` | ❌ | ✅ |

---

## Desteklenen Türler / Supported Types

```
thesis           → Doktora / Yüksek Lisans Tezi
article          → Dergi Makalesi
conference       → Konferans Bildirisi
lit-review       → Literatür Derlemesi
report           → Araştırma Raporu
book-chapter     → Kitap Bölümü
grant-proposal   → Hibe Başvurusu
research-proposal→ Araştırma Önerisi
```

---

## Conversational Onboarding ile Farkı / vs. Conversational Onboarding

| Özellik | Conversational (`/tezatlas`) | Fast-path (`new_project.py`) |
|---------|------------------------------|-------------------------------|
| Hedef | Yeni kullanıcılar | Deneyimli kullanıcılar |
| Süreç | 5 soru, adım adım | Tek komut |
| Kişiselleştirme | Yüksek | Standart şablonlar |
| Bağlam kurulumu | Tam | Temel |

**Öneri:** İlk proje → conversational. Sonraki projeler → fast-path.

---

## Tam Argüman Listesi / Full Arguments

```
--type      Belge türü (zorunlu)
--lang      tr / en / both (varsayılan: tr)
--field     Akademik alan (varsayılan: other)
--title     Çalışma başlığı (varsayılan: [Başlık Belirlenmedi])
--empirical METODOLOJI.md oluştur
--output    Dizin yolu (varsayılan: .)

Yardım:
python3 scripts/new_project.py --help
```
