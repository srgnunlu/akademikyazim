---
title: "Knowledge Gap Visualizer"
title_tr: "Bilgi Boşluğu Görselleştiricisi"
node_type: technique
description: "After reading saturation: visual map of which RQs/argument nodes have strong evidence, which are thin, which have only one source. Forces researcher to see gaps before writing. Generates prioritized reading queue for gaps."
description_tr: "Okuma doygunluğu sonrası: hangi araştırma sorularının/argüman düğümlerinin güçlü kanıta sahip olduğunu, hangilerin zayıf olduğunu, hangilerinin tek kaynağa dayandığını görsel olarak haritalandır. Araştırmacıyı yazımdan önce boşlukları görmeye zorla."
tags: [technique, knowledge-gap, reading-saturation, evidence-map, argument-map, phase-3, phase-4]
links_to:
  - skills/core/cognitive-augmentation.md
  - skills/techniques/comparative-analysis.md
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Bilgi Boşluğu Görselleştiricisi / Knowledge Gap Visualizer

## Ne Zaman? / When?

**Faz 3 (Okuma) → Faz 4 (Yapı/Outline) geçişinde** — okuma doygunluğuna ulaşıldıktan sonra.

Aktivasyon: `/boşluk-haritası` veya faz 3 çıkış kapısında otomatik.

**Önkoşul:** CAW (Cognitive Augmentation Workspace) aktif ve `ARGUMENTS.md` güncel.

---

## Kanıt Gücü Matrisi / Evidence Strength Matrix

Her argüman düğümü (araştırma sorusu veya alt iddia) için:

```
Bilgi Boşluğu Haritası
══════════════════════════════════════════════════════════════
Araştırma Sorusu / Argüman    Kaynak Sayısı  Kanıt Gücü  Durum
══════════════════════════════════════════════════════════════
RQ1: CBDC benimseme hızı      8 kaynak       ●●●         ✅ Güçlü
RQ2: Para pol. aktarımı       5 kaynak       ●●○         🟡 Orta
RQ3: Gizlilik trade-off       1 kaynak       ●○○         🔴 Zayıf
RQ4: Kurumsal çerçeve         0 kaynak       ○○○         ❌ BOŞ
Alt: Gelişmekte olan ülkeler  3 kaynak       ●●○         🟡 Orta
Alt: Merkez bankası bağımsızlığı 2 kaynak   ●○○         🔴 Zayıf
══════════════════════════════════════════════════════════════

Özet:
✅ Güçlü (3+ kaynak, çoklu metodoloji): 1/6
🟡 Orta (2-4 kaynak, homojen): 2/6
🔴 Zayıf (tek kaynak): 2/6
❌ Boş (kaynak yok): 1/6
```

---

## Görsel Harita / Visual Map (ASCII)

```
Ana Araştırma Sorusu
        │
   ┌────┴────┐
   │         │
RQ1 ●●●   RQ2 ●●○
   │         │
   │    ┌────┴────┐
   │    │         │
   │  Alt●●○   RQ3 ●○○ ⚠️
   │
RQ4 ○○○ ← BOŞ — Önce bu

Kanıt gücü: ●●● Güçlü  ●●○ Orta  ●○○ Zayıf  ○○○ Boş
```

---

## Boşluk Öncelik Sıralaması / Gap Priority Queue

Harita tamamlandıktan sonra okuma önceliği:

```
Yazımdan Önce Doldurul ması Gereken Boşluklar:

1. 🔴 ZORUNLU — RQ4: Kurumsal çerçeve (0 kaynak)
   Argümanın çekirdeği — bu boşlukla yazım başlamamalı
   Öneri: Kaynak Avcısı ile ara: `source_hunter --query "CBDC institutional framework"`

2. 🔴 ÖNERİLEN — RQ3: Gizlilik trade-off (tek kaynak)
   Tek kaynağa dayalı iddia hakemlik sürecinde reddedilme riski taşır
   Mevcut kaynak: [ECB 2021] → Ek kaynak: [arXiv'de ara]

3. 🟡 İSTEĞE BAĞLI — MB Bağımsızlığı (2 kaynak)
   Alt argüman — yetersiz ama kritik değil
   Öneri: Mevcut 2 kaynağı derinle oku, gerekirse 1 kaynak ekle
```

---

## Boşluk Kararı / Gap Decision

Her boşluk için araştırmacı karar verir:

```
RQ3 için gizlilik trade-off boşluğu:

A) Kaynak Avcısı ile ek kaynak ara (önerilen)
B) Bu iddiayı kapsam dışına al (gerekçe ile)
C) "[KAYNAK GEREKLİ]" etiketi ile devam et, sonra tamamla
D) İddiayı daha dar kapsama çek (mevcut kanıtla savunulabilir hale getir)
```

---

## ARGUMENTS.md ile Entegrasyon

Knowledge Gap Visualizer, `ARGUMENTS.md`'den verileri okur ve günceller:

```markdown
## Kanıt Boşluğu Kararları
| RQ/Argüman | Karar | Gerekçe |
|------------|-------|---------|
| RQ4 Kurumsal çerçeve | Kaynak ara | Çekirdek argüman |
| RQ3 Gizlilik | Kapsam daralt | [Tanım değiştirildi] |
```

---

## Sınırlamalar

- Görselleştirme notlara dayanır — notlar alınmadıysa işlevsiz
- "Güçlü kanıt" = birden fazla metodoloji + birden fazla kaynak; sayı değil kalite
- Tek güçlü kaynak, birden fazla zayıf kaynaktan üstündür
- Harita bir kontrol noktasıdır; son yazım kararı araştırmacıya aittir
