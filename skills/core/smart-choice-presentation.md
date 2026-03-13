---
title: "Smart Choice Presentation — Akademik Karar Matrisi"
title_tr: "Akıllı Seçenek Sunumu — Akademik Karar Matrisi"
node_type: core
priority: high
description: "Whenever the user faces a substantive academic choice during the writing phases, present each option with pros, cons, and a star-rated evaluation matrix. Applies to methodology, structure, argument strategy, journal selection, and other consequential decisions."
description_tr: "Kullanıcı yazım aşamalarında önemli bir akademik seçimle karşılaştığında, her seçeneği avantaj, dezavantaj ve yıldızlı değerlendirme matrisiyle sun. Metodoloji, yapı, argüman stratejisi, dergi seçimi ve diğer kritik kararlara uygulanır."
tags: [core, ux, decision-support, writing-phase, methodology, structure, journal-selection]
links_to:
  - skills/techniques/drafting-alternatives.md
  - skills/phases/thesis/phase-3-reading.md
  - skills/phases/thesis/phase-4-structure.md
  - skills/phases/article/phase-05-journal-selection.md
language: bilingual
version: "1.0"
---

# Akıllı Seçenek Sunumu / Smart Choice Presentation

## Ne zaman kullanılır? / When to apply?

Yazım aşamalarında ilerlerken kullanıcı **sonuçları geri alınamaz veya zahmetli olan** bir seçimle karşılaştığında bu formatı uygula.

Tetikleyici durumlar:

| Karar Noktası | Nerede | Seçenekler |
|---|---|---|
| Metodoloji seçimi | Phase 3 (Okuma → Metodoloji Dallanması) | Teorik / Nicel / Nitel / Karma |
| Yapı seçimi | Phase 4 (Yapı Tasarımı) | Hukuk / STEM / Sosyal Bil. / Tıp |
| Dergi seçimi | Article Phase 0.5 | 3 aday dergi karşılaştırması |
| Argüman stratejisi | Phase 6 Yazım (drafting-alternatives.md) | A/B/C/D taslak alternatifleri |
| Atıf sistemi seçimi | Phase 5 Protokol | APA / Chicago / Vancouver / vd. |
| Bölüm yazım sırası | Phase 6 Yazım | Teorik → Ampirik vs. Giriş önce |
| Veri analiz yöntemi | Phase 3-E3 | Betimsel / Çıkarımsal / Tematik |

---

## Sunum Formatı / Presentation Format

Her seçenek için şu bloğu kullan:

```
**[Seçenek Adı]**
> ✅ [Avantaj 1 | Avantaj 2 | Avantaj 3]
> ⚠️ [Dezavantaj veya risk 1 | Dezavantaj 2]
> ⭐ [Kriter 1]: ★★★★☆ | [Kriter 2]: ★★★☆☆ | [Kriter 3]: ★★★★★
> 💡 *Uygunsa:* [Bu seçenek hangi koşulda en mantıklı tercih?]
```

Yıldız formatı: `★★★★★` (5 tam) ile `★☆☆☆☆` (1 tam, 4 boş) arasında.
Kriterler seçime göre değişir — her karar noktasına uygun kriterler seç.

---

## Değerlendirme Sonrası / After Evaluation

1. Tüm seçenekler gösterildikten sonra kullanıcıdan seçim iste.
2. Kullanıcı seçtikten sonra, seçimin **sonuçlarını** kısa özetle: "Bu seçimle birlikte X adımı aktif oldu, Y adımı devre dışı kaldı."
3. Seçim STATUS.md'ye kaydedilir.
4. Kullanıcı daha sonra fikrini değiştirirse, değişikliğin maliyetini (geri gitme gerekliyse hangi adımlar) açıkça belirt.

---

## Paragraf Alternatiflerindeki Fark / Distinction from Drafting Alternatives

`drafting-alternatives.md` aynı formatı paragraf düzeyinde uygular (A/B/C/D metin alternatifleri + Savunma/Akıcılık/Özgünlük/Bağlam puanlaması). Bu dosya (smart-choice-presentation.md) ise paragrafın üstünde — metodoloji, yapı ve strateji gibi **makro düzey** kararlara uygulanır.

İkisi birbirini tamamlar; iç içe geçmez.
