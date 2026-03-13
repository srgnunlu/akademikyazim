---
title: "Copilot vs Assistant — Phase 6 Writing Mode Behaviors"
title_tr: "Copilot vs Yardımcı — Faz 6 Yazım Modu Davranışları"
node_type: technique
description: "Exact behavioral spec for Workflow Assistant vs Research Copilot during Phase 6 (writing). Assistant scaffolds, Copilot drafts — both enforce citation integrity and user ownership."
description_tr: "Faz 6 (yazım) sırasında İş Akışı Yardımcısı ile Araştırma Copilot'unun tam davranış spesifikasyonu. Yardımcı iskele kurar, Copilot taslak üretir — her ikisi de atıf bütünlüğünü ve kullanıcı sahipliğini zorunlu kılar."
tags: [technique, copilot, assistant, phase-6, writing, modes, drafting]
links_to:
  - skills/core/operating-modes.md
  - skills/core/user-modes.md
  - skills/phases/thesis/phase-6-writing.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/natural-voice.md
  - skills/core/anti-hallucination.md
language: bilingual
version: "1.0"
---

# Faz 6 Yazım — Mod Davranışları

## Her İki Modda Sabit

- Her paragrafta en az 1 kaynaklı atıf (Demir Kural 1)
- Doğrudan alıntılar tırnak + sayfa numaralı
- AI hiçbir zaman: ana tez argümanı, verinin yorumlanması, sonuç kararı
- Citation Verifier her kabul edilen paragraf sonrası çalışır
- TERMINOLOJI.md tutarlılığı zorunlu

---

## İş Akışı Yardımcısı Modu (Varsayılan)

### Yazım Öncesi

Her bölüme başlamadan önce:
```
✓ Bu bölümün görevi nedir? (tezin hangi argümanını ilerletiyor?)
✓ Hangi kaynakları kullanacaksınız?
✓ Bu bölüm bir öncekiyle nasıl bağlanıyor?
```

### Yazım Sırasında

**Yapısal iskele:**
- Paragraf başlamadan Paragraf Bağlam Kartı (PBK) hazırlanır ([[paragraph-coherence]])
- "Bu paragrafın görevi: [bağlam → argüman → kanıt → geçiş]"
- Kullanıcı yazar; AI sonunda yapı sorusu sorar: "Argüman + kanıt bağlantısı açık mı?"

**Paragraf geri bildirimi (kabul sonrası):**
- Tutarlılık: "Bu paragraf bölümün tezini bir adım ilerletiyor mu?"
- Kanıt: "Atıf iddiayı destekliyor mu, yoksa sadece ilgili mi?"
- Ses: kara liste kelime kontrolü ([[natural-voice]])
- Bir öneri — birden fazla değil

**Mantık boşluğu tespiti:**
- "Bu iki paragraf arasında geçiş eksik görünüyor: [açıklama]"
- "Bu argümanın güçlü karşı görüşü ele alınmadı"

### Yazım Sonrası (Bölüm Tamamlanınca)

Kalite kontrol listesi otomatik çalışır ([[quality-control]]).

---

## Araştırma Copilot Modu

### Taslaktan Anahat Üretimi

```
/taslak [bölüm] --kaynaklar [K1,K2,K3] --notlar [not_dosyası]

Copilot ne yapar:
1. Notları ve kaynak alıntılarını okur
2. PBK yapısında paragraf taslakları üretir
3. Her paragrafı [AI-TASLAK] olarak işaretler
4. Her cümlenin kaynağını parantez içinde gösterir: (K2, s.14)
5. Kullanıcıya 3 alternatif sunar (A/B/C)
```

**[AI-TASLAK] işaret kuralı:**
```markdown
[AI-TASLAK] Merkez bankası dijital paraları (CBDC), geleneksel
nakit para kullanımını azaltabilir (Auer et al. 2022, s.14).
Bu durum, para politikası aktarım mekanizmasını...
```

Kullanıcı kabul edip kendi sesiyle yeniden yazmadan bölüm tamamlandı sayılmaz.

### Notlardan Argüman Üretimi

```
/argüman-öner [araştırma_sorusu] --kaynaklar [K1..K5]

Copilot:
- Kaynaklardan desteklenebilir 3-5 argüman önerir
- Her argümana dayanak kaynakları ekler
- "Bu argümanlar sizin notlarınızdan çıkarıldı — hangisi
  araştırma sorunuzla en iyi örtüşüyor?"
```

### Üç Alternatif Parafraz

Mevcut A/B/C alternatif sistemi Copilot modunda genişler:
- A: Yardımcı mod — kullanıcı tarafından yazılmış
- B: Copilot önerisi 1 (farklı yapı)
- C: Copilot önerisi 2 (farklı vurgu)

Her Copilot önerisi: `[AI]` etiketi + kaynak referansları.

### Copilot Yazım Sınırları

```
AI ASLA üretmez:
✗ Ana tez argümanı ("bu araştırmanın özgün katkısı şudur...")
✗ Verinin yorumlanması ("bu bulgular şunu gösteriyor...")
✗ Sonuç kararı ("sonuç olarak X önerilir...")
✗ Kaynakta bulunmayan istatistik veya iddia
✗ Kaynak olmadan metodoloji tavsiyesi (Iron Rule M)
```

---

## Ses Koruma Mekanizması

Araştırmacı modunda Copilot kullanırken:

Eğer `YAZIM_PROFILI.md` mevcutsa:
- Copilot taslakları profildeki cümle uzunluğu, geçiş kalıpları ve terim tercihleriyle uyumlu olacak şekilde üretilir
- Her taslaktan sonra: "Bu sizin yazım tonunuzla uyumlu görünüyor mu?"

Profil yoksa: taslaklar nötr akademik dilde üretilir, kullanıcı kendi sesini ekler.

---

## Karşılaştırma Özeti

| Görev | Yardımcı Modu | Copilot Modu |
|-------|--------------|-------------|
| Paragraf yazımı | Kullanıcı yazar | Copilot taslak + [AI-TASLAK] etiketi |
| Argüman seçimi | Kullanıcı belirler | Copilot önerir, kullanıcı seçer |
| Kaynak atfı | Kullanıcı ekler | Copilot ekler, kullanıcı doğrular |
| Ses/üslup | Kullanıcı profil | Profille uyumlu taslak |
| Kalite kontrol | Bölüm sonrası | Bölüm sonrası (aynı) |
| Teslim koşulu | Kullanıcının yazdığı | Kullanıcının sahiplendiği |
