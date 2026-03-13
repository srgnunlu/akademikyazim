---
title: "Cognitive Augmentation Workspace (CAW)"
title_tr: "Bilişsel Güçlendirme Çalışma Alanı (CAW)"
node_type: core
description: "As the user reads and writes, auto-extract claims, evidence, and counter-arguments. Gap detector: which arguments lack evidence? Contradiction detector: source A says X, source B says ¬X. Devil's Advocate: challenges assumptions before writing. Lives at Phase 3-4 transition."
description_tr: "Kullanıcı okurken ve yazarken: iddialar, kanıtlar ve karşı argümanları otomatik çıkar. Boşluk tespiti: hangi argümanlar kanıtsız? Çelişki tespiti: kaynak A X diyor, kaynak B ¬X. Şeytan'ın Avukatı: yazım öncesi varsayımlara meydan okur. Faz 3-4 geçişinde yaşar."
tags: [core, caw, argument-map, gap-detection, contradiction, devils-advocate, phase-3, phase-4]
links_to:
  - skills/techniques/argument-mapping.md
  - skills/techniques/comparative-analysis.md
  - skills/phases/thesis/phase-3-reading.md
  - skills/phases/thesis/phase-4-structure.md
  - skills/core/anti-hallucination.md
language: bilingual
version: "1.0"
---

# Bilişsel Güçlendirme Çalışma Alanı (CAW)

## Ne Yapar?

CAW, Claude'un 200K context penceresini kullanarak okuma ve yazma oturumlarında **aktif argüman izleme** yapar. Araç değil — bir düşünme ortağı protokolü.

Dört bileşen:
1. **İddia Çıkarımı** — her kabul edilen paragraftan iddiaları otomatik listele
2. **Boşluk Tespiti** — hangi iddiaların kanıt desteği yok?
3. **Çelişki Tespiti** — kaynaklar arası zıt sonuçları işaretle
4. **Şeytan'ın Avukatı** — yazım başlamadan varsayımlara meydan oku

---

## 1. İddia Çıkarımı / Claim Extraction

Okuma veya yazım sırasında, her not / kabul edilen paragraf sonrası:

```
Argüman İzleyici (Güncel)
─────────────────────────────────────────────
İddia               Kaynak        Kanıt Gücü
─────────────────────────────────────────────
CBDC benimseme hızı Auer(2022)    ●● Orta
Para pol. aktarımı  BIS(2023)     ●● Orta
Gizlilik trade-off  [Kaynak yok]  ○  BOŞLUK
Siber risk          ECB(2021)     ● Zayıf
─────────────────────────────────────────────
```

İzleyici `ARGUMENTS.md` dosyasına yazar (proje kök dizini).

---

## 2. Boşluk Tespiti / Gap Detection

Kanıt gücü ○ (sıfır) olan her iddia için:

```
⚠️ KANIT BOŞLUĞU: "Gizlilik trade-off"

Bu iddia henüz kaynaklı kanıta sahip değil.
Seçenekler:
A) Kaynak Avcısı ile ara: python agents/run.py source_hunter --query "CBDC privacy"
B) Bu iddiayı şimdilik kaldır — sonra ekle ([KAYNAK GEREKLİ] etiketiyle)
C) İddianın kapsamını daraltalım — ne tam olarak iddia ediyoruz?
```

---

## 3. Çelişki Tespiti / Contradiction Detection

Birden fazla kaynak yüklüyken (Comparative Analysis veya yazım sırasında):

```
⚠️ ÇELİŞKİ TESPİT EDİLDİ

Konu: CBDC ve enflasyon etkisi

Auer et al. (2022), s.14:
"CBDC benimsemesi para arzını genişleterek enflasyonu artırabilir."

BIS (2023), s.8:
"CBDC para politikası aktarımını güçlendirir; doğrudan enflasyon
etkisi ampirik olarak belirsizdir."

Bu çelişkiyi tezinizde nasıl ele alacaksınız?
A) Metodoloji farkını açıkla (simülasyon vs ampirik)
B) Her iki görüşü sun, kendi pozisyonunu belirt
C) Daha güçlü kanıt için ek kaynak ara
```

---

## 4. Şeytan'ın Avukatı / Devil's Advocate

Faz 4 yapı aşamasına geçmeden veya istendiğinde (`/şeytan-avukatı`):

```
Araştırma sorunuz: "[ARAŞTIRMA SORUSU]"
Temel argümanınız: "[ANA İDDİA]"

Şeytan'ın Avukatı olarak 3 itirazı sunuyorum:

1. "Ölçüm geçerliliği sorunu: [CBDC benimseme metriği] nasıl
   ölçüldüğü tartışmalı. X ve Y farklı tanımlar kullanıyor.
   Sizin tanımınız hangisine dayanıyor?"

2. "Seçim yanlılığı: Vaka seçiminiz [ülkeler] CBDC konusunda
   erken benimseyenler — bulgular benimsememiş ülkelere
   genellenebilir mi?"

3. "Nedensellik vs korelasyon: [Para politikası etkisi iddiası]
   nedensellik mi gösteriyor, korelasyon mu? Hangi mekanizma?"

Bu itirazlardan hangisini tezinizde ele almak istersiniz?
```

**Şeytan'ın Avukatı kuralı:** Sorular sorar, cevap vermez. Araştırmacı kendi yanıtını geliştirir.

---

## ARGUMENTS.md Şablonu

```markdown
# Argüman İzleyici
Proje: [PROJE ADI] | Son güncelleme: [TARİH]

## Aktif İddialar

| # | İddia | Kaynak | Kanıt Gücü | Durum |
|---|-------|--------|-----------|-------|
| 1 | [iddia] | [kaynak] | ●●● | ✅ Güçlü |
| 2 | [iddia] | [kaynak] | ●● | 🟡 Destekleniyor |
| 3 | [iddia] | — | ○ | 🔴 BOŞLUK |

## Çelişkiler

| # | Konu | Kaynak A | Kaynak B | Ele Alış |
|---|------|---------|---------|---------|
| 1 | [konu] | [görüş] | [zıt görüş] | [karar] |

## Şeytan'ın Avukatı — Bekleyen İtirazlar

- [ ] [İtiraz 1] — Bölüm [X]'te ele alınacak
- [ ] [İtiraz 2] — Kapsam dışı bırakılacak (gerekçe: [])
```

---

## Aktivasyon Noktaları

| Ne zaman | Otomatik mı? |
|----------|-------------|
| Her not dosyası kaydedildiğinde | Opsiyonel (hafif mod) |
| Faz 3 tamamlanınca | ✅ Önerilen |
| Faz 3→4 geçişinde | ✅ Zorunlu (Comparative Analysis ile birlikte) |
| Yazımda yeni iddia eklendiğinde | Opsiyonel |
| `/şeytan-avukatı` komutu | ✅ On demand |

---

## Sınırlamalar

- CAW notlara dayanır — ham PDF'lere değil. Notlar önce alınmalı
- Çelişki tespiti yanlış pozitif verebilir: benzer kelimeler, farklı bağlamlar
- Boşluk = kanıt yok şu an; araştırmacı gerçekten kanıt olmadığını biliyorsa iddia kaldırılır
- Tüm iddialar hâlâ Demir Kural 1'e tabidir
