---
title: "Deep Comparative Analysis — Multi-Source Synthesis Technique"
title_tr: "Derin Karşılaştırmalı Analiz — Çoklu Kaynak Sentez Tekniği"
node_type: technique
description: "Loads 5+ source notes simultaneously into context for cross-source theme extraction, contradiction detection, and evidence strength matrix. Uses Claude's 200K context window. Output: COMPARATIVE_ANALYSIS.md. Runs at Phase 3→4 transition."
description_tr: "5+ kaynak notunu aynı anda bağlama yükleyerek çapraz tema çıkarımı, çelişki tespiti ve kanıt güç matrisi üretir. Claude'un 200K context penceresini kullanır. Çıktı: COMPARATIVE_ANALYSIS.md. Faz 3→4 geçişinde çalışır."
tags: [technique, comparative-analysis, synthesis, phase-3, phase-4, multi-source, 200k-context]
links_to:
  - skills/phases/thesis/phase-3-reading.md
  - skills/phases/thesis/phase-4-structure.md
  - skills/techniques/saturation-check.md
  - skills/templates/tpl-comparative-analysis.md
language: bilingual
version: "1.0"
---

# Derin Karşılaştırmalı Analiz / Deep Comparative Analysis

## Ne Zaman Çalıştırılır?

**Tetikleyiciler:**
- Faz 3 okuma döngüsü tamamlandı (okuma doygunluğu ≥ 80%)
- Faz 4 yapı aşamasına geçmeden önce
- Kullanıcı "kaynakları karşılaştır", "çelişkileri bul", "sentez yap" dediğinde

**Minimum koşul:** En az 5 kaynak notu tamamlanmış olmalı.

---

## Analiz Protokolü

### Adım 1 — Kaynak Yükleme

```
Şu kaynak notlarını yükle (hepsini tek seferde):
- notlar/kaynak1_notlar.md
- notlar/kaynak2_notlar.md
- notlar/kaynak3_notlar.md
- notlar/kaynak4_notlar.md
- notlar/kaynak5_notlar.md
[+ araştırma sorusu: STATUS.md'den]
```

Claude'un 200K token bağlamı ~40-50 kaynak notunu karşılayabilir.
Daha fazla kaynak varsa: en alakalı olanları seç ve gerisi için ayrı bir döngü çalıştır.

### Adım 2 — Beş Analizin Sırayla Yürütülmesi

#### 2a. Tema Çıkarımı

Her kaynakta tekrarlayan temalar + her tema için hangi kaynağın vurgu yaptığını haritalama.

```
TEMA MATRİSİ
─────────────────────────────────────────────────────
Tema                K1   K2   K3   K4   K5   Toplam
─────────────────────────────────────────────────────
CBDC benimseme hızı  ●    ●    ○    ●    ●    4/5
Para pol. etkisi     ●    ○    ●    ○    ●    3/5
Finansal kapsayıcılık ○   ●    ●    ●    ○   3/5
Gizlilik riskleri    ●    ○    ●    ●    ●    4/5
─────────────────────────────────────────────────────
● = güçlü vurgu  ○ = sınırlı/yok
```

#### 2b. Çelişki Tespiti

Kaynakların birbirine zıt sonuçlar çıkardığı noktalar — sayfa referansıyla.

```
ÇELIŞKILER
─────────────────────────────────────────────────────
Çelişki #1: CBDC ve enflasyon

  K2 (Auer et al. 2022, s.14): "CBDC benimsemesi
  enflasyonu artırabilir çünkü..."

  K4 (BIS 2023, s.8): "CBDC enflasyon üzerinde
  nötr bir etki bırakır çünkü..."

  → Metodoloji farkı: K2 simülasyon, K4 ampirik
  → Tezde nasıl ele alınacak: [kullanıcı kararı]
─────────────────────────────────────────────────────
```

#### 2c. Metodoloji Deseni

Kaynaklar hangi yöntemleri kullanıyor? Baskın yöntem var mı?

```
METODOLOJİ PATERNİ
─────────────────────────────────────────────────────
Yöntem                  Kaynak sayısı  Kaynaklar
─────────────────────────────────────────────────────
Sistematik derleme      3/5            K1, K3, K5
DSGE simülasyonu        1/5            K2
Vaka analizi            1/5            K4
─────────────────────────────────────────────────────
→ Alanda niteliksel çalışma eksikliği var
→ Tez yöntemi kararı için bağlam sağlar
```

#### 2d. Kanıt Güç Matrisi

Her ana iddia için destekleyen kanıtın gücü (birden fazla bağımsız kaynak = güçlü):

```
KANIT GÜÇ MATRİSİ
─────────────────────────────────────────────────────
İddia                    Güçlü  Orta  Zayıf  Boşluk
─────────────────────────────────────────────────────
CBDC tasarım çeşitliliği  ●●●   ●     —      —
Perakende vs toptan ayrımı ●●    ●●    —      —
Gizlilik trade-off        ●     ●     ●      —
Siber güvenlik riski      —     ●     —      ●●
─────────────────────────────────────────────────────
● = 1 kaynak  ●● = 2 kaynak  ●●● = 3+ kaynak
BOŞLUK = hiçbir kaynak bu konuyu ele almıyor
```

#### 2e. Okuma Boşlukları

Tema matrisinde ve kanıt gücünde boşluk olan alanlar → ek okuma önerileri:

```
OKUMA BOŞLUKLARI
─────────────────────────────────────────────────────
1. Siber güvenlik riski: Sadece 1 kaynak var, ikincil
   Öneri: Kaynak Avcısı ile CBDC + cybersecurity ara

2. Gelişmekte olan piyasalar perspektifi: Tüm kaynaklar
   gelişmiş ekonomi odaklı
   Öneri: IMF WP serisi, Afrika + LatAm merkez bankası
─────────────────────────────────────────────────────
```

---

## Çıktı: COMPARATIVE_ANALYSIS.md

Şablon için bkz. [[tpl-comparative-analysis]].

Dosya konumu: proje kök dizini / `COMPARATIVE_ANALYSIS.md`

Bu dosya:
- Faz 4 yapı çalışmasında (tez/makale taslağı) doğrudan besler
- Hangi argümanın hangi kaynakla desteklendiğini gösterir
- Zayıf kanıt noktalarını görünür kılar
- Çelişki paragrafları için ham materyali sağlar

---

## Sınırlamalar

- Bu teknik **notlara** dayalıdır — ham PDF'lere değil. Notlar önce alınmalı.
- Kaynaklar arası çelişki = araştırma fırsatı; "sorun" değil
- Üretilen matrisleri körce alma — araştırma sorunla bağlantısını sen kur
- Tüm iddiaların hâlâ `/sources/` dosyasına dayalı olması zorunlu (Demir Kural 1)

---

## Hız Rehberi

| Kaynak sayısı | Yaklaşık süre | Notlar |
|--------------|---------------|--------|
| 5-10 kaynak  | 15-20 dk | Tek oturumda yapılabilir |
| 10-20 kaynak | 30-40 dk | Temalar önceden belirlenebilir |
| 20-40 kaynak | 2-3 oturum | Konuya göre grupla |
| 40+ kaynak   | Birden fazla döngü | Deferred pool'u da dahil et |
