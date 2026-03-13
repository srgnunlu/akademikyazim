---
title: "Paragraph Coherence — Intra-Section Context Continuity"
title_tr: "Paragraf Tutarlılığı — Bölüm İçi Bağlam Sürekliliği"
node_type: technique
priority: high
description: "Real-time paragraph-to-paragraph context tracking during writing. Maintains argument state, prevents repetition, and ensures each new paragraph builds on the previous one. Fires during Phase 6 (thesis) and Phase 4 (article) writing."
description_tr: "Yazım sırasında gerçek zamanlı paragraftan paragrafa bağlam takibi. Argüman durumunu korur, tekrarı önler ve her yeni paragrafın öncekinin üzerine inşa edilmesini sağlar. Faz 6 (tez) ve Faz 4 (makale) yazımında tetiklenir."
tags: [technique, writing, coherence, context, continuity, repetition-avoidance, paragraph-flow, always-active-during-writing]
links_to:
  - skills/techniques/drafting-alternatives.md
  - skills/techniques/academic-writing-quality.md
  - skills/techniques/session-structure.md
  - skills/core/quality-control.md
  - skills/core/context-management.md
used_by:
  - skills/phases/thesis/phase-6-writing.md
  - skills/phases/article/phase-4-writing.md
  - skills/phases/conference/phase-3-writing.md
  - skills/phases/lit-review/phase-5-writing.md
  - skills/phases/report/phase-4-writing.md
  - skills/phases/book-chapter/phase-4-writing.md
  - skills/phases/grant-proposal/phase-4-writing.md
language: bilingual
version: "1.0"
---

# Paragraf Tutarlılığı / Paragraph Coherence

## Problem

Drafting Alternatives matrisi paragrafı izole birim olarak ele alır.
Önceki paragrafta ne söylendiği, hangi terimlerin kullanıldığı, hangi argümanın tamamlandığı bilinmeden yeni alternatifler üretilir.

Sonuç: tekrar, bağlam kopukluğu, argüman boşluğu, terim monotonluğu.

---

## Kural 1: Paragraf Bağlam Kartı (PBK)

Her paragraf seçiminden SONRA, bir sonraki paragrafa geçmeden ÖNCE aşağıdaki bağlam kartı güncellenir.

```
╔══════════════════════════════════════════════════════╗
║  PARAGRAF BAĞLAM KARTI (PBK)                         ║
╠══════════════════════════════════════════════════════╣
║  Bölüm: [X.Y alt bölüm adı]                         ║
║  Paragraf: [#N — yazılan paragraf sırası]            ║
║  Ana iddia: [tek cümle — bu paragraf ne söyledi?]    ║
║  Kullanılan terimler: [virgülle ayrılmış]            ║
║  Sunulan kanıt: [kaynak + sayfa]                     ║
║  Açık kalan nokta: [sonraki paragrafta ele alınmalı] ║
║  Geçiş yönü: [bir sonraki paragraf neye bağlanmalı]  ║
╚══════════════════════════════════════════════════════╝
```

**PBK dosyaya yazılmaz.** Oturum içi bağlam olarak bellekte tutulur. Oturum sonunda PBK durumu `DURUM_OZETI.md`'ye eklenir ("Son yazılan paragraf: [özet], sonraki paragraf: [geçiş yönü]").

---

## Kural 2: Sonraki Paragraf Üretiminde Zorunlu Girdi

Drafting Alternatives çalışırken, önceki PBK bilgisi **her alternatifin üretim prompt'una dahil edilir**:

```
AI dahili prompt yapısı:
─────────────────────────────────
Önceki paragraf: [PBK'dan ana iddia]
Kullanılan terimler: [PBK'dan — bunları TEKRARLAMA]
Açık kalan nokta: [PBK'dan — bunu ELE AL veya gerekçelendir]
Geçiş beklentisi: [PBK'dan — bağlantıyı kur]
─────────────────────────────────
Şimdi bu bölümün bir sonraki paragrafı için A/B/C/D alternatifleri üret.
```

Bu adım atlanamaz. Bölümün ilk paragrafında PBK yoktur — o zaman bölüm açılış signpost'u yeterlidir.

---

## Kural 3: Bölüm İçi Argüman İzleyici

Her bölüm yazımına başlarken bir argüman izleyici oluşturulur:

```
╔══════════════════════════════════════════════════════╗
║  ARGÜMAN İZLEYİCİ — [Bölüm X.Y]                     ║
╠══════════════════════════════════════════════════════╣
║  Bölümün tezi: [tek cümle]                           ║
║                                                      ║
║  Kanıtlanması gereken alt iddialar:                  ║
║  □ [1] ...                                           ║
║  □ [2] ...                                           ║
║  □ [3] ...                                           ║
║                                                      ║
║  Ele alınması gereken karşı argümanlar:              ║
║  □ [K1] ...                                          ║
║                                                      ║
║  Durum:                                              ║
║  ■ [1] — Paragraf 2'de kanıtlandı ✓                 ║
║  □ [2] — henüz ele alınmadı                         ║
║  □ [3] — henüz ele alınmadı                         ║
║  □ [K1] — henüz ele alınmadı                        ║
╚══════════════════════════════════════════════════════╝
```

**Kaynak:** `argument_map.md` veya `_notlar.md` dosyasından türetilir.

**Kural:** Bölümün son paragrafı yazılmadan önce tüm kutucuklar ✓ olmalı. Eksik kalanlar varsa AI uyarır: "Bu alt iddia henüz ele alınmadı: [X]. Son paragrafta mı yoksa ayrı bir paragrafta mı ele alalım?"

---

## Kural 4: Tekrar Önleme (Gerçek Zamanlı)

Alternatifler üretilirken şu kontroller otomatik çalışır:

### 4a. Terim Çeşitliliği
Önceki PBK'daki terimler **aynı formda tekrarlanmaz**. Eş anlamlı veya farklı yapı kullanılır:

```
Paragraf N: "ampirik bulgular göstermektedir"
Paragraf N+1:
  ✅ "veriler ortaya koymaktadır" (farklı yapı)
  ✅ "araştırma sonuçları desteklemektedir" (farklı terim)
  ❌ "ampirik bulgular göstermektedir" (birebir tekrar)
```

**İstisna:** `TERMINOLOJI.md`'deki sabit terimler tekrarlanabilir (örn. "CBDC", "merkez bankası dijital parası"). Bunlar tutarlılık gereği korunur.

### 4b. Argüman Tekrarı
Aynı alt iddia iki kez kanıtlanmaz. Argüman İzleyici'de ✓ işaretli madde yeniden kanıtlanıyorsa AI uyarır:

```
⚠️  Bu paragraf "[alt iddia 1]"i yeniden kanıtlıyor.
    Bu, Paragraf 2'de zaten ele alındı.
    Seçenekler:
    (a) Bu paragrafı sil, sonraki alt iddiaya geç
    (b) Paragraf 2'deki kanıtı güçlendir (birleştir)
    (c) Farklı açıdan ele al (belirt: hangi açı?)
```

### 4c. Yapısal Tekrar
Ardışık paragraflar aynı yapıyı kullanmaz:

```
Paragraf N: [İddia] → [Kaynak A] → [Gerekçe]
Paragraf N+1:
  ❌ [İddia] → [Kaynak B] → [Gerekçe]  (aynı yapı — monoton)
  ✅ [Karşı argüman] → [Çürütme + Kaynak B] → [Sentez]  (farklı yapı)
  ✅ [Kaynak B bulgusu] → [Paragraf N ile karşılaştırma] → [Sentez]
```

---

## Kural 5: Bağlam Sürekliliği Puanı

Drafting Alternatives puanlama matrisine **dördüncü boyut** eklenir:

| Kriter | Ölçüt |
|--------|-------|
| **Bağlam (Coherence)** | Önceki paragrafla anlam bağı var mı? Argüman İzleyici'de yeni bir kutuyu mu dolduruyor? Terim tekrarı var mı? |

Puanlama:
- ★★★★★ — Önceki paragraftan doğal geçiş + yeni alt iddia ele alınıyor + terim çeşitliliği var
- ★★★★ — Geçiş iyi ama küçük terim tekrarı veya yapısal benzerlik
- ★★★ — Geçiş var ama önceki paragrafla bağ zayıf
- ★★ — Önceki paragrafla bağlantı kopuk veya aynı alt iddiayı tekrarlıyor
- ★ — Bağlam tamamen kopuk, bölüm tezinden sapma

---

## Kural 6: Oturum Kesintisinde PBK Aktarımı

Oturum bitmek üzereyken (context doluyor / kullanıcı durduruyor):

1. Son PBK, `DURUM_OZETI.md`'ye yazılır:
```markdown
## Yazım Bağlamı (Sonraki Oturum İçin)
- Son paragraf (#N): [ana iddia özeti]
- Kullanılan terimler: [liste]
- Açık kalan: [nokta]
- Sonraki paragrafın görevi: [geçiş yönü]
- Argüman İzleyici durumu: [X/Y alt iddia tamamlandı]
```

2. Sonraki oturum başında AI bu bloğu okur ve PBK'yı yeniden oluşturur.

---

## Akış Özeti

```
Bölüm yazımı başlıyor
    │
    ├─ Argüman İzleyici oluştur (_notlar.md + argument_map.md'den)
    │
    ├─ Paragraf 1: Bölüm açılış signpost + ilk alt iddia
    │   └─ PBK #1 oluştur
    │
    ├─ Paragraf 2: PBK #1 oku → Drafting Alternatives üret
    │   ├─ Zorunlu girdi: PBK #1 + Argüman İzleyici
    │   ├─ Tekrar kontrolü (terim, argüman, yapı)
    │   ├─ Puanlama: Savunma + Akıcılık + Özgünlük + Bağlam
    │   ├─ Kullanıcı seçer → PBK #2 oluştur
    │   └─ Argüman İzleyici güncelle (✓ işaretle)
    │
    ├─ Paragraf 3–N: aynı döngü
    │
    ├─ Son paragraf öncesi: Argüman İzleyici kontrolü
    │   └─ Eksik alt iddia varsa → uyar
    │
    └─ Bölüm kapanış signpost + quality-control kontrol listesi
```

---

## Entegrasyon

| Dosya | Değişiklik |
|-------|-----------|
| `drafting-alternatives.md` | Puanlama matrisine "Bağlam" boyutu eklendi |
| `quality-control.md` | Paragraf düzeyinde gerçek zamanlı kontrol eklendi |
| `session-structure.md` | Oturum sonunda PBK aktarımı eklendi |
| Yazım fazı dosyaları | Bu tekniğe referans eklendi |
