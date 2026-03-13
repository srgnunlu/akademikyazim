---
title: "Şablon — COMPARATIVE_ANALYSIS.md"
title_en: "Template — COMPARATIVE_ANALYSIS.md"
node_type: template
description: "Output template for the Deep Comparative Analysis technique. Generated at Phase 3→4 transition."
description_tr: "Derin Karşılaştırmalı Analiz tekniğinin çıktı şablonu. Faz 3→4 geçişinde oluşturulur."
tags: [template, comparative-analysis, synthesis, phase-3, phase-4]
links_to:
  - skills/techniques/comparative-analysis.md
language: bilingual
version: "1.0"
---

# Şablon: COMPARATIVE_ANALYSIS.md

Aşağıdaki şablonu proje kök dizininde `COMPARATIVE_ANALYSIS.md` olarak oluştur.

---

```markdown
# Karşılaştırmalı Kaynak Analizi / Comparative Source Analysis

**Proje:** [PROJE ADI]
**Araştırma Sorusu:** [STATUS.md'den]
**Analiz tarihi:** [TARİH]
**Analiz edilen kaynak sayısı:** [N]

---

## 1. Analiz Edilen Kaynaklar

| # | Kısa kod | Yazar(lar) | Yıl | Tür | Not dosyası |
|---|----------|-----------|-----|-----|-------------|
| K1 | [KOD] | [AD] | [YIL] | [makale/rapor/kitap] | notlar/xxx_notlar.md |
| K2 | | | | | |

---

## 2. Tema Matrisi

| Tema | K1 | K2 | K3 | K4 | K5 | Toplam |
|------|----|----|----|----|-----|--------|
| [Tema 1] | ● | ● | ○ | ● | ● | 4/5 |
| [Tema 2] | | | | | | |
| [Tema 3] | | | | | | |

`●` = güçlü vurgu | `○` = sınırlı/dolaylı | boş = yok

---

## 3. Çelişkiler ve Tartışmalı Noktalar

### Çelişki #1: [KONU]

**[Kısa kod 1]** ([Yazar, Yıl, s.X]):
> "[Alıntı veya parafraz]"

**[Kısa kod 2]** ([Yazar, Yıl, s.X]):
> "[Zıt görüş]"

**Fark kaynağı:** [metodoloji / veri seti / tanım farklılığı]
**Tezde ele alış:** [kullanıcı kararı — sonuçta doldur]

---

## 4. Metodoloji Deseni

| Yöntem | Kaynak sayısı | Kaynaklar |
|--------|--------------|-----------|
| [Yöntem 1] | N/[toplam] | K1, K3 |
| [Yöntem 2] | | |

**Alan metodoloji notu:** [Alanda baskın yöntem nedir? Tezin yöntemi buna nasıl konumlanıyor?]

---

## 5. Kanıt Güç Matrisi

| İddia | Güçlü (3+) | Orta (2) | Zayıf (1) | Boşluk (0) |
|-------|-----------|---------|---------|-----------|
| [İddia 1] | ●●● | | | |
| [İddia 2] | | ●● | | |
| [İddia 3] | | | ● | |
| [İddia 4] | | | | ✗ |

---

## 6. Okuma Boşlukları ve Öneriler

| # | Boşluk | Neden önemli | Arama önerisi |
|---|--------|-------------|---------------|
| 1 | [Konu] | [Tez için önemi] | [Kaynak türü / veri tabanı] |
| 2 | | | |

**Deferred pool için eklenecekler:** [varsa]

---

## 7. Faz 4 Yapısına Bağlantı

Bu analiz şu taslak bölümlerini besler:

| Bölüm | Destekleyen kaynaklar | Çelişki var mı? |
|-------|----------------------|-----------------|
| [Bölüm başlığı] | K1, K3, K5 | Hayır |
| [Bölüm başlığı] | K2, K4 | Evet (bkz. Çelişki #1) |

---

*Bu belge [[comparative-analysis]] tekniği ile oluşturulmuştur.*
*Kaynaklar: [kaynak kısa kodları]*
```
