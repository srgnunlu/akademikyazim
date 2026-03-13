---
title: "Template — tezprotokol.md (Phase 5 Output)"
title_tr: "Şablon — tezprotokol.md (Faz 5 Çıktısı)"
node_type: template
priority: critical
produces_file: tezprotokol.md
associated_phase: 5
description: "Project constitution file generated at Phase 5 by merging all Phase 0-4 outputs. This is the single most-read file across all sessions — every session starts by reading it."
description_tr: "Faz 5'te Faz 0-4 çıktıları birleştirilerek üretilen proje anayasası dosyası. Tüm oturumlarda en çok okunan dosya — her oturum bu dosyayı okuyarak başlar."
tags: [template, phase-5, project-constitution, session-start, always-read]
links_to:
  - skills/phases/thesis/phase-5-protocol.md
  - skills/core/context-management.md
  - skills/moc/MOC-citations.md
used_by:
  - skills/phases/thesis/phase-5-protocol.md
  - skills/core/context-management.md
  - skills/techniques/session-structure.md
language: bilingual
version: "2.0"
---

# Şablon: tezprotokol.md

Bu dosya Faz 5'te otomatik üretilir. Faz 0-4'teki tüm bilgiler birleştirilir. **Her oturumda ilk okunan dosyadır.**

This file is auto-generated in Phase 5 by merging all Phase 0-4 outputs. **It is read at the start of every session.**

---

```markdown
# Tez Protokolü

> Oluşturma tarihi: [tarih]
> Son güncelleme: [tarih]
> TezAtlas versiyon: 2.0

---

## 1. Proje Kimliği
*(Faz 0'dan — proje_kimlik.md)*

- **Öğrenci:** [ad soyad]
- **Üniversite / Enstitü / ABD:** [X / X / X]
- **Program:** [YL / DR]
- **Danışman:** [unvan + ad soyad]
- **Tez dili:** [X]
- **Disiplin:** [X]
- **Atıf sistemi:** [X]
- **Teslim tarihi:** [X / belirsiz]

---

## 2. Tez Başlığı ve Araştırma Soruları
*(Faz 1'den — konu_kesfi.md)*

**Başlık:** [onaylanmış tez başlığı]

**Araştırma soruları:**
1. [RQ1]
2. [RQ2]
3. [RQ3]
*(YL için 3-5, DR için 5-7)*

**Anahtar kavramlar:** [kavram1], [kavram2], [kavram3] ...

---

## 3. Tez Yapısı
*(Faz 4'ten — yapi_taslagi.md)*

```
Bölüm 1: [başlık]
  1.1 [alt bölüm]
  1.2 [alt bölüm]
Bölüm 2: [başlık]
  ...
Sonuç
Kaynakça
```

Dosya haritası:
```
chapter_1_intro.md     → [X] kelime hedefi
chapter_2_[konu].md    → [X] kelime hedefi
...
```

---

## 4. Kaynak Politikası
*(Evrensel + projeye özel — skills/core/source-policy.md)*

- Yazımda (Faz 6) yalnızca /sources/ klasöründeki PDF'ler
- Web: yalnızca Faz 1-2'de keşif için
- [Projeye özel istisnalar varsa buraya ekle]

---

## 5. Atıf Sistemi Formatları
*(Faz 0'dan + MOC-citations'dan)*

**Seçilen sistem:** [Chicago / APA 7 / Harvard / IEEE / OSCOLA / Vancouver]

Temel format örnekleri:
- Kitap dipnotu: [örnek]
- Makale dipnotu: [örnek]
- İkinci atıfta: [a.g.e. / Ibid. örneği]
- Kaynakça formatı: [örnek]

*(Tam rehber: templates/citations/[sistem].md)*

---

## 6. Yazım Standartları
*(Üniversite formatı + akademik dil)*

- **Kenar boşlukları:** [sol/sağ/üst/alt]
- **Yazı tipi:** [X, punto]
- **Satır aralığı:** [X]
- **Dipnot boyutu:** [X punto]
- **Sayfa numarası:** [konum]
- **Dil tutarlılığı:** [TR: ş/ç/ğ/ı/ö/ü | EN: American / British]

---

## 7. Bölüm Uzunluk Hedefleri
*(Faz 4'ten)*

| Bölüm | Hedef Kelime |
|-------|:---:|
| Giriş | [X] |
| Bölüm 1 | [X] |
| Bölüm 2 | [X] |
| Sonuç | [X] |
| **Toplam** | **[X]** |

---

## 8. Teorik Çerçeve Özeti
*(Faz 3 okumalarından)*

[2-4 paragraf: tezin teorik/kavramsal temeli, kullanılan temel sources, metodoloji özeti]

---

## 9. Kritik Uyarılar
*(Danışmandan veya önceki oturumlardan birikmiş — DERSLER.md'den)*

- [Uyarı 1]
- [Uyarı 2]
*(Başlangıçta boş, Faz 5 sonrasında DERSLER.md'den güncellenir)*

---

## 10. Oturum Planı

Her oturum başında oku:
1. Bu dosya (tezprotokol.md)
2. MEMORY.md
3. DERSLER.md
4. TERMINOLOJI.md
5. İlgili _notlar.md

Her oturum sonunda güncelle:
1. MEMORY.md (sayısal)
2. DURUM_OZETI.md (narrative)
3. DERSLER.md (varsa yeni ders)
4. TERMINOLOJI.md (varsa yeni terim)
5. git commit (ZORUNLU)
```
