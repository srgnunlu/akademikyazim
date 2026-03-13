---
title: "Guided Writing Mode — AI Drafts, You Guide"
title_tr: "Rehberli Yazım Modu — AI Yazar, Siz Yönlendirirsiniz"
node_type: foundation
priority: critical
description: "TezAtlas'ın birincil yazım protokolü. AI her bölüm için A/B seçenekleri, kaynak kanıtı, güçlü/zayıf analizi ve akademik yazım notu sunar. Kullanıcı seçer, yönlendirir, sahiplenir."
tags: [guided-writing, draft-generator, a-b-options, academic-note, always-active]
links_to:
  - skills/core/iron-rules.md
  - skills/techniques/drafting-alternatives.md
  - skills/core/reviewer-mode.md
language: bilingual
version: "1.0"
---

# Rehberli Yazım Modu / Guided Writing Mode

Bu mod, TezAtlas'ın **birincil yazım protokolüdür**.

AI bir taslak yazar. Siz seçer, yönlendirir ve sahiplenirsiniz.

---

## Temel Çıktı Formatı / Core Output Format

Her bölüm veya paragraf yazımında AI şu sabit formatı kullanır:

```
## [Bölüm / Paragraf Adı]

### Seçenek A — ★★★★☆
[Tam taslak metin — kaynaklara dayalı, atıflı]

📚 Kullanılan kaynaklar:
  - kaynak_a.pdf s.45: "doğrudan alıntı veya parafraz"
  - kaynak_b.pdf s.12: parafraz açıklaması

✅ Güçlü: [argüman sırası, kaynak desteği, akıcılık]
⚠️ Zayıf: [karşı görüş eksikliği, geniş iddia, hedging sorunu]

---
### Seçenek B — ★★★☆☆
[Alternatif taslak metin — farklı yapı veya ton]

📚 Kullanılan kaynaklar:
  - kaynak_c.pdf s.8: ...

✅ Güçlü: ...
⚠️ Zayıf: ...

---
### 📖 Akademik Yazım Notu
[Neden bu yapı? Bu bölüm türünde (Giriş / Literatür / Yöntem / Sonuç) akademik norm ne?
Hangi kaynaktan ne öğrendik? Bu paragraf tezin hangi argümanına hizmet ediyor?]

→ Seçiminiz? A / B / Birleştir / Yeniden yaz
```

---

## Seçenek Stratejileri / Option Strategies

AI seçenekler üretirken şu varyasyon stratejilerini kullanır:

| Seçenek | Strateji |
|---------|---------|
| A | Doğrudan, ampirik odaklı (veri-önce) — en güçlü kaynak desteği |
| B | Teorik, anlatı odaklı — literatür boşluğu üzerinden kurulan çerçeve |
| C | Temkinli, hedged — karşı argümanları açıkça ele alan |
| D | (varsa) Sentezci, cesur — birden fazla kaynağı entegre eden |

Seçenekler **toplam puana göre azalan sırada** sunulur.

---

## Yıldız Puanlama / Star Rating

Her seçenek 4 kriter üzerinden değerlendirilir:

| Kriter | Açıklama |
|--------|---------|
| **Savunma** | Kaynak desteği ne kadar güçlü? (Iron Rule 1) |
| **Akıcılık** | Önceki paragraftan geçiş ne kadar pürüzsüz? |
| **Özgünlük** | Kullanıcının katkısı ne kadar belirgin? |
| **Bağlam** | Argüman izleyiciyle uyum ve tekrar önleme |

Kaynak desteği olmayan seçenek **Savunma = 0** alır ve `[KAYNAK BEKLENİYOR]` etiketiyle işaretlenir.

---

## Akademik Yazım Notu / Academic Writing Note

Her seçenek setinin sonunda şunlar açıklanır:

1. **Bölüm normları**: Bu bölüm türünde (Giriş / Literatür / Yöntem / Tartışma / Sonuç) akademik yazımın beklentileri neler?
2. **Kaynak öğrenimi**: Bu paragrafta kullanılan kaynaklardan çıkarılan temel fikir nedir?
3. **Argüman hizmeti**: Bu paragraf tezin hangi üst argümanına hizmet ediyor?
4. **Ton rehberi**: Hangi durumlarda hedging gerekir, hangi durumlarda güçlü iddia yapılabilir?

Bu not yazım becerisi gelişimini destekler — sadece taslak üretimi değil.

---

## Seçim Sonrası Akış / Post-Selection Flow

Kullanıcı bir seçenek seçtiğinde:

1. AI seçimin **dezavantajını** özellikle ele alır
2. O dezavantajı gidermek için **B.1 / B.2 / B.3 alt seçenekleri** sunar
3. Kullanıcı nihai seçimi yapar
4. AI **Paragraf Bağlam Kartını (PBK)** ve **Argüman İzleyiciyi** günceller
5. Bir sonraki paragrafın alternatifleri bu güncel bağlamla üretilir

---

## Iron Rule Kontrolü / Iron Rule Check

- Her seçenek **Iron Rule 1 ve 4'e** uymalıdır
- Kaynak olmadan hiçbir seçenek üretilmez
- Kaynak bulunamazsa: yazım DURUR → `[KAYNAK BEKLENİYOR]` etiketi → başka paragraftan devam

---

## Doğal Ses Filtresi / Natural Voice Filter

Her seçenek sunulmadan önce:

1. **Kara liste taraması**: AI tipik kelimeler (`delve`, `crucial`, `comprehensive` vb.) çıkarılır
2. **Burstiness kontrolü**: Cümle uzunluğu en az 3 bant (kısa / orta / uzun) içermeli
3. **Yazım profili eşleşmesi**: `YAZIM_PROFILI.md` varsa, kullanıcının ses tercihleriyle karşılaştır

---

## Bölüm Türü Uyarlaması / Section Type Adaptation

`detect_section_type()` (core/literature_intel.py) bölüm türünü otomatik algılar
ve Akademik Yazım Notu'nu buna göre uyarlar:

| Bölüm | Özel norm |
|-------|-----------|
| Giriş | Problemi kur, katkı iddiasını netleştir, yapıyı özetle |
| Literatür | Karşılaştırmalı analiz, boşluk tespiti, sentez |
| Yöntem | Meşruiyet gerekçesi, alternatif yönteme cevap |
| Bulgular | Nesnel aktarım, yorum yasak |
| Tartışma | Kaynakla karşılaştır, sınırlılıkları açık söyle |
| Sonuç | Katkıyı tekrar ifade et, gelecek çalışma öner |

---

## Hakem Kapısı Entegrasyonu / Reviewer Gate Integration

Faz geçişlerinde Guided Writing Mode çıktıları **AI Hakem İncelemesi**ne tabi tutulur:

```
╔══════════════════════════════╗
║  AI Hakem İncelemesi         ║
║  Faz 3 → Faz 4 Geçişi        ║
╠══════════════════════════════╣
║  ✅ Kaynak doygunluğu: OK    ║
║  ⚠️  Argüman 3 → kaynak yok  ║
║  ❌ Karşı argüman eksik      ║
╚══════════════════════════════╝
→ 2 sorunu çöz, sonra geç
```

Detay: `skills/core/reviewer-mode.md`

---

## Kısayol Referansı / Quick Reference

Guided Writing Mode şu dosyalarla entegre çalışır:

- `skills/techniques/drafting-alternatives.md` — tam A/B/C/D matrisi ve puanlama
- `skills/techniques/paragraph-coherence.md` — PBK ve Argüman İzleyici
- `skills/techniques/natural-voice.md` — kara liste + burstiness
- `skills/core/reviewer-mode.md` — faz kapısı hakem protokolü
- `skills/core/smart-choice-presentation.md` — makro kararlar için yıldız matrisi
