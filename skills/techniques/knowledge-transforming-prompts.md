---
title: "Knowledge-Transforming Prompts (Bereiter & Scardamalia)"
title_tr: "Bilgi Dönüştürücü Promtlar (Bereiter & Scardamalia)"
node_type: technique
description: "Before each paragraph/section in Phase 6: pushes writers from knowledge-telling (novice: dump what I know) to knowledge-transforming (expert: writing changes my thinking). Based on Bereiter & Scardamalia (1987)."
description_tr: "Faz 6'da her paragraf/bölümden önce: yazarları bilgi anlatımından (acemi: bildiklerini döktür) bilgi dönüştürmeye (uzman: yazım düşüncemi değiştirir) iter. Bereiter & Scardamalia (1987) temelli."
tags: [technique, knowledge-transforming, bereiter, scardamalia, phase-6, writing-quality, metacognition]
links_to:
  - skills/techniques/copilot-writing.md
  - skills/core/cognitive-augmentation.md
  - skills/techniques/style-checker.md
language: bilingual
version: "1.0"
---

# Bilgi Dönüştürücü Promtlar / Knowledge-Transforming Prompts

## Araştırma Temeli / Research Basis

**Bereiter & Scardamalia (1987) — *The Psychology of Written Composition*:**

İki temel yazma modu:

| Mod | Kim? | Süreç |
|-----|------|-------|
| **Bilgi Anlatımı** (Knowledge-Telling) | Acemi yazar | "Ne biliyorum?" → yaz |
| **Bilgi Dönüştürme** (Knowledge-Transforming) | Uzman yazar | "Bu argüman okuyucumun düşüncesini nasıl değiştiriyor?" → yaz → düşün → yeniden yaz |

**Temel öngörü:** Uzman yazarlar, yazmayı *bilgiyi dışa aktarma* aracı değil *düşünce geliştirme* aracı olarak kullanır. TezAtlas bu geçişi tetikler.

---

## Aktivasyon Noktaları / Activation Points

Her Faz 6 paragraf/bölümü başlamadan önce — özellikle:
- Yeni bir argüman bölümü açılırken
- Sonuç bölümü yazılmadan önce
- Uzun bir metodoloji bölümü başlamadan önce
- Yazar "ne yazacağımı bilmiyorum" dediğinde

---

## Bilgi Dönüştürücü Soru Paketi / KT Question Set

### Bölüm Başı (1 dakika)

```
Bu bölümü yazmadan önce:

1. Bu argüman okuyucumun düşüncesini nasıl değiştirmeli?
   "Bu bölümü okuduktan sonra okuyucu şunu düşünmeli: [...]"

2. Bu bölüm tezimin/makalemimin ana argümanına nasıl katkıda bulunuyor?
   "Bu olmadan araştırma şu nedenle eksik kalır: [...]"

3. Bu bölümü yazarken benim için ne belirsiz?
   "Hâlâ yanıtlamak istediğim soru: [...]"
```

### Paragraf Başı (30 saniye)

```
Bu paragraf:
A) Bir iddiayı kanıtlarıyla destekliyor mu?
B) Bir karşı argümanı ele alıyor mu?
C) İki fikri birleştiriyor mu?

→ Seçtiğin fonksiyon ne? Bunu açık et, sonra yaz.
```

### Bölüm Sonu (2 dakika)

```
Yazdıktan sonra:

1. Bu bölümü yazmak sana ne öğretti?
   (Başlamadan bildiğinden farklı bir şey var mı?)

2. En zayıf nokta nerede?
   "Bir hakem şunu sorgulayabilir: [...]"

3. Bir sonraki bölüm bu bölümün neresinden devam etmeli?
```

---

## Bilgi Anlatımı Sinyalleri / Knowledge-Telling Signals

Bu örüntüler bilgi anlatımına işaret eder — dönüştürme sorusu tetikle:

```
⚠️ "Bu konuda şunlar bilinmektedir..."
⚠️ Kaynak listesi → özet → başka kaynak (argüman yok)
⚠️ Her paragraf aynı yapıda: [yazar] şunu buldu / şunu söyledi
⚠️ "Sonuç olarak" → önceki paragrafların tekrarı
```

---

## Uygulama Modu / Application Mode

**Thought Partner modunda** (varsayılan): AI bu soruları sorar, yanıtları araştırmacı üretir.

**Draft Generator modunda**: AI soruları sormaz, taslağı üretir — ancak taslağın ardından Knowledge-Transforming sorularını review için sunar.

---

## Örnek Diyalog / Example Dialogue

```
Araştırmacı: "3.2 bölümünü yazmak istiyorum — CBDC'nin enflasyon etkisi."

TezAtlas (KT Protokolü):
"Yazmadan önce 1 soru:
Bu bölümü okuduktan sonra okuyucun şunu düşünmesini istiyorsun:
[Bunu tamamla, sonra başlayalım]"

Araştırmacı: "CBDC'nin enflasyon etkisinin belirsiz olduğunu ve bağlama
göre değiştiğini — özellikle kurumsal yapıya göre."

TezAtlas: "O zaman bölümün çekirdeği 'koşullu etki' argümanı.
Hangi koşullar bu etkiyi belirliyor? En güçlü kanıtın nerede?"
```

---

## Sınırlamalar

- KT sorular her paragraf için değil, önemli geçişlerde — akışı kesme
- Araştırmacı yanıt vermek istemezse atla: `/kt-atla`
- Zaman baskısı altında (Deadline Mode aktifse) kısa versiyon: yalnızca "Bu argüman ne işe yarıyor?"
