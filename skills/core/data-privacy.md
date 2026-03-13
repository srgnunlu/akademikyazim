---
title: "Data Privacy Architecture — Local-First Research Data Policy"
title_tr: "Veri Gizliliği Mimarisi — Yerel-Öncelikli Araştırma Verisi Politikası"
node_type: core
description: "All pre-publication research data stays local. Defines sensitive data categories, .gitignore rules, GDPR/KVKK checklist, safe sharing, session log policy, data ownership, and breach protocol."
description_tr: "Yayın öncesi tüm araştırma verileri yerel kalır. Hassas veri kategorileri, .gitignore kuralları, GDPR/KVKK kontrol listesi, güvenli paylaşım, oturum günlüğü politikası, veri sahipliği ve ihlal protokolü."
tags: [core, privacy, gdpr, kvkk, local-first, gitignore, always-active]
links_to:
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Veri Gizliliği Mimarisi / Data Privacy Architecture

**HER ZAMAN AKTİF — disiplin veya belge türünden bağımsız.**
**ALWAYS ACTIVE — applies regardless of discipline or document type.**

---

## 1. Yerel-Öncelik İlkesi / Local-First Principle

Yayın öncesi araştırma verileri, araştırmacı **her veri seti için açık opt-in kararı vermeden** hiçbir bulut hizmetine gönderilmez.

Research data is **never transmitted to any cloud service** without explicit, per-dataset opt-in.

Bu anlama gelir / This means:
- Ham veri dosyaları → yerel makine veya kurumun onaylı şifreli sürücüsü
- TezAtlas proje klasörleri veri içeriyorsa → GitHub, Dropbox, OneDrive ile **varsayılan olarak senkronize edilmez**
- Overleaf bulut sayılır → IRB protokolü izin vermedikçe katılımcı alıntılarını veya yayımlanmamış bulguları oraya yapıştırma

---

## 2. Hassas Araştırma Verisi Kategorileri / Sensitive Data Categories

| Kategori | Örnekler |
|----------|----------|
| Katılımcı transkriptleri | Görüşme kayıtları, verbatim transkriptler, odak grup notları |
| Anket yanıtları | Ham Qualtrics/Google Forms verileri, tanımlayıcı içeren çıktılar |
| Klinik / sağlık verisi | Hasta kayıtları, tanı verileri, ilaç geçmişi |
| Yayımlanmamış elyazmaları | Taslak bölümler, gönderilmemiş makaleler |
| Kurumsal veriler | Gizli belgeler, mali kayıtlar, İK verileri |
| Kişisel yazışmalar | Kaynak olarak kullanılan e-posta, mektup, DM |
| Biyometrik / davranışsal veri | Göz izleme, EEG, fizyolojik ölçümler |
| Konum verisi | Katılımcıyı tanımlayabilecek konum bilgisi |
| Hukuki dosyalar | Müvekkil yazışmaları, mühürlü mahkeme belgeleri |
| IRB kısıtlı materyaller | Etik onayında açıkça kısıtlanan her veri |

**Şüphe durumunda: hassas varsay.**

---

## 3. .gitignore Kuralları / .gitignore Rules

Projenin `.gitignore` dosyasına ekle:

```gitignore
# ============================================================
# TezAtlas Data Privacy Block — KALDIR MA
# ============================================================

# Ham veri dizinleri / Raw data directories
data/
raw_data/
transcripts/
participants/
interviews/
survey_responses/
clinical/
fieldnotes/

# Nicel veri dosyaları / Quantitative data files
*.csv
*.xlsx
*.xls
*.sav          # SPSS
*.dta          # Stata
*.rdata        # R workspace
*.rds          # R object
*.mat          # MATLAB
*.feather
*.parquet

# Nitel analiz dosyaları / Qualitative analysis files
*.qda          # MAXQDA
*.nvp          # NVivo project
*.atlas        # ATLAS.ti

# Ses / görüntü kayıtları / Audio-video recordings
*.mp3
*.mp4
*.wav
*.m4a
*.mov

# Tanımlayıcı içerebilecek çıktılar
*_raw.*
*_identifiable.*
*_participants.*
# ============================================================
```

---

## 4. GDPR / KVKK Uyum Kontrol Listesi

**Veri toplamadan önce:**
- [ ] Etik kurul / IRB onayı alındı ve belgelendi
- [ ] Aydınlatılmış onam formu: ne toplanıyor, nerede saklanıyor, ne kadar süre, kim erişiyor
- [ ] Veri minimizasyonu: yalnızca araştırma sorusu için gerekli veriler
- [ ] KVKK için: açık rıza beyanı yazılı alındı

**Veri toplarken:**
- [ ] Tüm dosyalarda katılımcı adı yerine ID kullanılıyor
- [ ] ID–isim anahtar tablosu ayrı, şifreli, erişim kısıtlı
- [ ] Hassas veriler AI araçlarına, bulut belgelere veya e-postaya yapıştırılmıyor

**Veri toplandıktan sonra:**
- [ ] Saklama süresi belirlendi (tipik: yayın sonrası 5–10 yıl)
- [ ] Anonimleştirme protokolü belgelendi
- [ ] Yayın öncesi paylaşım: anonimleştirilmiş ve ikinci araştırmacı tarafından gözden geçirildi

---

## 5. Güvenli Paylaşım / Safe Sharing

**Kabul edilebilir:**
- Anonimleştirilmiş toplu istatistikler (hücre boyutu < 5 olmayan)
- IRB onaylı anonimleştirilmiş alıntılar
- Erişim kontrollü kurumsal havuzlar (OSF embargo, TÜBİTAK veri deposu)
- Ortak araştırmacılarla şifreli kanal (Signal, kurumsal SecureShare)

**IRB değişikliği olmadan kabul edilemez:**
- Ham transkriptlerin orijinal etik onayında yer almayan kişilerle paylaşımı
- Tam veri seti yüklemesi (GitHub, OSF public, Zenodo) — eğer onam kapsamadıysa
- Ticari AI aracıyla işleme — etik kurulu tarafından incelenmemişse

---

## 6. Oturum Günlüğü Politikası / Session Log Policy

Claude Code oturumları araştırma bağlamı içerir. Pratik kural:

> "Bu metin bir git commit'inde görünse kurumuma karşı rahat olur muyum?" → Hayırsa yapıştırma — tanımla.

- Tam katılımcı transkriptlerini bağlama yapıştırma → yalnızca anonimleştirilmiş alıntılar
- `.claude/` dizini → cloud backup'a senkronize etmeden önce içeriği gözden geçir
- Kurumsal makinede çalışıyorsan → IT politikasının oturum günlüklerini kapsayıp kapsamadığını kontrol et

---

## 7. Veri Sahipliği Beyanı / Data Ownership Statement

**Araştırmacı, TezAtlas oturumunda üretilen TÜM içeriğin sahibidir.**

TezAtlas yalnızca iş akışı iskeleti, yapısal öneriler ve yazım yönergeleri üretir. Araştırma verisi, argümanlar, yorumlar veya sonuçlar üzerinde hiçbir hak iddia etmez.

Anthropic'in veri işleme politikası için: `https://www.anthropic.com/legal/privacy`

Kurumun AI araçlarının araştırmada kullanımı için veri işleme anlaşması (DPA) gerektiriyorsa — hassas verilerle TezAtlas projesine başlamadan önce bu anlaşmayı al.

---

## 8. İhlal Protokolü / Breach Protocol

Hassas veri yanlışlıkla git'e commit edildiyse:

**Adım 1:** Push etme. Edildiyse diğer makinelere pull'lanmasını durdur.

**Adım 2:** BFG Repo Cleaner (önerilen):
```bash
bfg --delete-files sensitive_file.csv
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

**Adım 3:** Danışmanı derhal bildir. Depo herhangi bir süre public erişime açıktıysa IRB/etik kurulu bildir. AB/TR kişisel verisi ifşa edildiyse GDPR/KVKK bildirim yükümlülüğünü değerlendir (72 saatlik pencere).

**Adım 4:** Dosya desenini `.gitignore`'a ekle. Pre-commit hook'un bunu yakalaması için kontrol et.
