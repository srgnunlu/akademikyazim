---
title: "Multilingual Source Management"
title_tr: "Çok Dilli Kaynak Yönetimi"
node_type: core
description: "Turkish thesis writers commonly use English, German, and French sources. Original-language quote preservation alongside translations, bilingual citation format, language tag per source, automatic language detection via OCR pipeline metadata."
description_tr: "Türk tez yazarları genellikle İngilizce, Almanca ve Fransızca kaynaklar kullanır. Orijinal dilde alıntıyı çeviriyle birlikte koru, iki dilli atıf formatı, her kaynak için dil etiketi, OCR pipeline ile otomatik dil tespiti."
tags: [core, multilingual, translation, citation, turkish, german, french, ocr, quote-preservation]
links_to:
  - skills/core/iron-rules.md
  - skills/core/anti-hallucination.md
  - skills/disciplines/yok-compliance.md
language: bilingual
version: "1.0"
---

# Çok Dilli Kaynak Yönetimi / Multilingual Source Management

## Neden Önemli? / Why It Matters

Türk akademisyenler tez ve makalelerinde sıkça İngilizce, Almanca, Fransızca kaynak kullanır. Bu durum üç yaygın hataya yol açar:

1. **Yanlış çeviri**: Kaynak metnin anlamı çeviride kaybolur veya değişir
2. **Özgün metin atlanır**: Yalnızca çeviri verilir, hakemler/jüri özgün dili görmek ister
3. **Atıf formatı**: Bazı Türk üniversiteleri kaynak başlığının hem özgün hem çevrilmiş halini ister

---

## Alıntı Koruma Protokolü / Quote Preservation Protocol

Yabancı dilde alıntı için standart format:

```markdown
## Özgün Alıntı Formatı

[YAZAR, YIL, s. X]:
> "[Özgün dilde tam alıntı]"
> [Türkçe çeviri] (Çeviren: araştırmacı / AI destekli)

Örnek:
[Habermas, 1984, s. 285]:
> "Communicative action is oriented to reaching understanding."
> "İletişimsel eylem, anlaşmaya yönelik bir eylemdir." (Çeviri: araştırmacı)
```

**Kural:** Çeviri AI destekli ise `[AI destekli çeviri — araştırmacı onaylı]` etiketi.

---

## Dil Etiketi / Language Tag

`KAYNAK_ENVANTERI.md` ve `READING_REPORT.md`'de her kaynağa dil etiketi:

```markdown
| Kaynak | Dil | Orijinal Başlık | Çevrilmiş Başlık |
|--------|-----|----------------|-----------------|
| Weber_1922 | de | Wirtschaft und Gesellschaft | Economy and Society |
| Derrida_1967 | fr | De la grammatologie | Of Grammatology |
| BIS_2023 | en | CBDC Report | CBDC Raporu (TR: kullanılmaz) |
```

---

## Bilingual Atıf Formatı / Bilingual Citation Format

Bazı Türk üniversiteleri (özellikle sosyal bilimler) yabancı dil kaynak başlığının Türkçe çevirisini ister:

```
Weber, M. (1922). Wirtschaft und Gesellschaft [Economy and Society].
  Mohr Siebeck.

Derrida, J. (1967). De la grammatologie [Gramatoloji Üzerine].
  Les Éditions de Minuit.
```

**YÖK uyumlu format için** bkz. `skills/disciplines/yok-compliance.md`

---

## Dil Tespiti / Language Detection

OCR pipeline metadata'sından otomatik dil tespiti:

```bash
# OCR pipeline dil tespiti
python3 ocr_pipeline.py sources/ --detect-language --lang tur+eng+deu+fra
```

Tespit sonucu `KAYNAK_ENVANTERI.md`'de `lang` alanına yazılır.

**Manuel override:** Eğer tespit yanlışsa:
```bash
python3 ocr_pipeline.py sources/weber_1922.pdf --force-lang deu
```

---

## Çeviri Güvence Protokolü / Translation Assurance Protocol

Çeviri yapılırken Iron Rule 1 geçerliliğini korur:

```
Çeviri önerisi:
"[Özgün metin]"
→ "[Çeviri önerisi]"

Onaylamadan önce kontrol et:
□ Anlam özgün metinle örtüşüyor mu?
□ Teknik terimler doğru çevrildi mi?
□ Çeviride kaynak gösteriminde "[Çev.]" notu var mı?

Onay: araştırmacıya ait — AI çeviriyi önerir, araştırmacı onaylar.
```

---

## Almanca/Fransızca Özel Durumlar

**Almanca umlaut sorunları:** Ä Ö Ü → OCR bazen yanlış okur. OCR sonrası kontrol:
```bash
grep -P "[ÄÖÜäöüß]" notes/*.md  # Almanca karakterleri kontrol et
```

**Fransızca aksan işaretleri:** é è ê ë à â ù û î ï → aynı durum.

**Latin kökenli dil kaynakları (İspanyolca, İtalyanca, Portekizce):** Türk akademisyenler bu dillerde kaynak kullandığında aynı protokol — Türkçe + İngilizce ara çeviri önerilebilir.

---

## STATUS.md Entegrasyonu

```yaml
sources:
  languages:
    en: 18
    tr: 4
    de: 3
    fr: 2
  bilingual_citations_required: true  # üniversite gereksinimi
  translation_policy: researcher_approved  # researcher_approved | ai_draft_only
```
