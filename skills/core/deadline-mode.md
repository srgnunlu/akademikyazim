---
title: "Deadline Mode — Iron Rule 1 Adaptation Under Time Pressure"
title_tr: "Deadline Modu — Zaman Baskısı Altında Demir Kural 1 Uyarlaması"
node_type: core
description: "Activates when user has a hard deadline (conference, course, submission) < 7 days. Relaxes Iron Rule 1 drafting requirement but enforces [SOURCE NEEDED] tagging and blocks finalization until all tags are cleared."
description_tr: "Kullanıcının < 7 günlük sert bir son tarihi olduğunda etkinleşir. Demir Kural 1 taslak gereksinimini gevşetir ama [KAYNAK GEREKLİ] etiketlemesini zorunlu kılar ve tüm etiketler temizlenene kadar bitişi engeller."
tags: [core, deadline, iron-rule-1, source-needed, time-pressure, always-active]
links_to:
  - skills/core/iron-rules.md
  - skills/core/source-policy.md
  - skills/phases/thesis/phase-7-finalization.md
language: bilingual
version: "1.0"
---

# Deadline Modu / Deadline Mode

## Ne Zaman Aktif Olur?

**TR:** Kullanıcı şunlardan birini söylediğinde otomatik olarak aktifleştir:
- "Yarın/bugün/3 gün içinde teslim etmem gerekiyor"
- "Konferans son tarihi geliyor"
- "Çok az zamanım var, yazmaya başlamalıyım"
- `/deadline-mode` komutu

**EN:** Activate automatically when user signals hard deadline pressure:
- "I have to submit tomorrow / in 3 days"
- "Conference deadline is coming up"
- `/deadline-mode` command

**Aktivasyon koşulları / Activation conditions:**

| Durum | Deadline Modu |
|-------|---------------|
| Teslim < 7 gün | ✅ Etkinleşebilir (kullanıcı onayıyla) |
| Teslim ≥ 7 gün | ❌ Normal iş akışı zorunlu |
| Tez (doktora/yüksek lisans) | ❌ HİÇBİR ZAMAN — akademik kayıt riski çok yüksek |
| Konferans bildiri / ders ödevi | ✅ Uygun |
| Dergi makalesi | ✅ Uygun (ancak post-deadline revizyon planı zorunlu) |

> **Hard rule:** Deadline modu ASLA bir tezde kullanılmaz. Tez süreç disiplini bozulursa uzun vadeli zarar çok büyüktür.

---

## Aktivasyon Protokolü

Deadline modu önerildiğinde şunu söyle:

```
⚠️ DEADLINE MODU AKTİF

Normal iş akışının dışına çıkıyoruz:
✓ Kaynak olmadan taslak yazabilirsin
✓ Her kaynaksız iddia [KAYNAK GEREKLİ] ile etiketlenir
✗ [KAYNAK GEREKLİ] etiketi kalan hiçbir bölüm teslime giremez

Son teslimden önce tüm etiketleri kapatmak için plan yapalım.
Deadline: [TARİH]. Kaç [KAYNAK GEREKLİ] kabul edilebilir?
```

---

## [SOURCE NEEDED] / [KAYNAK GEREKLİ] Etiket Protokolü

### Etiket Kullanımı

```markdown
Dijital para birimlerinin benimsenmesi son yıllarda hızla artmaktadır
[KAYNAK GEREKLİ: CBDC benimseme istatistiği, 2022-2024].

Merkez bankası dijital paraları geleneksel para politikasını
temelden değiştirebilir [KAYNAK GEREKLİ: para politikası etkisi,
BIS veya Fed araştırması].
```

**Etiket formatı:**
```
[KAYNAK GEREKLİ: <iddia_özeti>, <beklenen_kaynak_türü>]
[SOURCE NEEDED: <claim_summary>, <expected_source_type>]
```

### Etiket Takip Tablosu

Her yazım oturumu sonunda `DEADLINE_TAKIP.md` güncellenir:

```markdown
## Deadline Takip — [BELGE ADI]
Deadline: [TARİH] | Kalan süre: [X gün]
Son güncelleme: [TARİH]

| # | Bölüm | İddia özeti | Beklenen kaynak | Durum |
|---|-------|-------------|-----------------|-------|
| 1 | 2.1 | CBDC benimseme % | BIS/IMF raporu | 🔴 Açık |
| 2 | 2.3 | Para pol. etkisi | Merkez bankası lit. | 🔴 Açık |
| 3 | 3.1 | Örnek ülke uygulaması | Ülke CB raporu | 🟡 Aranıyor |

Açık: [N] | Aranan: [N] | Kapatılan: [N]
```

---

## Finalizasyon Kapısı (Phase Gate)

**Deadline modunda teslim görevlendirmesi şu koşulda açılır:**

```
☑ [KAYNAK GEREKLİ] etiketi kalan paragraf SIFIR
☑ Tüm bulunan kaynaklar /sources/ klasöründe
☑ Atıflar doğrulanmış (Citation Verifier veya manuel)
☑ DEADLINE_TAKIP.md'de tüm satırlar ✅ Kapatıldı
```

**Açık etiket varsa:**
```
⛔ TESLİM KAPISI KAPALI

[N] adet [KAYNAK GEREKLİ] etiketi hâlâ açık:
  → Bölüm 2.1: CBDC benimseme istatistiği
  → Bölüm 3.2: Para politikası etkisi

Seçenekler:
A) Kaynağı bul ve eklediğinde etiketi kapat
B) İddiayı daha zayıf/genel bir ifadeyle değiştir
C) İddiayı tamamen çıkar

⚠️ Etiketli içerikle teslim: akademik dürüstlük ihlali riski.
```

---

## Kaynak Bulma Hızlandırıcısı

Deadline modunda kaynakları hızlı bulmak için öncelik sırası:

```
1. MCP Server → search_papers("<iddia>") — anlık arama
2. agents/run.py source_hunter — arka planda
3. Semantic Scholar / Google Scholar — 5 dakika
4. Mevcut /sources/ klasörü — zaten elde olan kaynaklar
5. Danışmanın önerisi — 1 e-posta ile
```

> **Kural:** "Kaynak bulamıyorum" = iddiayı ya zayıflatırsın ya çıkarırsın.
> Kaynak olmadan teslim etmek, etiketleri görmezden gelmek demektir.

---

## Deadline Modu vs Normal Mod Karşılaştırması

| Özellik | Normal Mod | Deadline Modu |
|---------|------------|---------------|
| Taslak yazma | Kaynak olmalı | Kaynaksız OK |
| Etiketleme | [KAYNAK BEKLENİYOR] (önerim) | [KAYNAK GEREKLİ] (zorunlu) |
| Finalizasyon kapısı | Tüm kaynaklar doğrulanmış | Tüm etiketler kapatılmış |
| Tez projeleri | Geçerli | ❌ Yasak |
| Kalite kontrolü | Tam | Temel (imla, atıf formatı) |
| Git commit | Oturum sonunda | Her bölüm sonunda |
| Advisor checkpoint | Phase gate'te | Teslim öncesi en az 1 |

---

## Deadline Sonrası Borç Temizleme

Deadline modunda yazılan içerik sonradan düzenlenmelidir:

```markdown
## Post-Deadline Kaynak Borç Listesi
Teslim: [TARİH]
İyileştirme hedef tarihi: [4-6 hafta sonra]

| Bölüm | Zayıf iddia / Çıkarılan içerik | Hedef kaynak |
|-------|-------------------------------|--------------|
| 2.1 | "hızla artmaktadır" → genel söylem | BIS 2024 raporu |
```

Revizyon veya yayın öncesi bu liste kapatılmalıdır.
