---
title: "Natural Voice — AI Voice Filter, Burstiness Control & Writing Style Profile"
title_tr: "Doğal Ses — YZ Ses Filtresi, Burstiness Kontrolü ve Yazım Stili Profili"
node_type: technique
priority: high
description: "Three-layer system to ensure AI-assisted academic text reads as authentically human: (1) AI vocabulary blacklist filters known AI-tell words, (2) burstiness control enforces sentence-length variation and structural diversity, (3) writing style profile matches output to the user's personal writing fingerprint."
description_tr: "YZ destekli akademik metnin otantik insan yazımı gibi okunmasını sağlayan üç katmanlı sistem: (1) YZ kelime kara listesi bilinen YZ-işaret kelimelerini filtreler, (2) burstiness kontrolü cümle uzunluğu varyasyonunu ve yapısal çeşitliliği zorunlu kılar, (3) yazım stili profili çıktıyı kullanıcının kişisel yazım parmak izine eşler."
tags: [technique, writing, natural-voice, ai-detection, burstiness, style-profile, blacklist, always-active-during-writing]
links_to:
  - skills/techniques/drafting-alternatives.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/academic-writing-quality.md
  - skills/core/quality-control.md
  - skills/templates/tpl-writing-profile.md
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

# Doğal Ses / Natural Voice

## Neden Gerekli

YZ tarafından üretilen akademik metin yapısal olarak "çok temiz"dir — ve bu temizlik paradoks olarak onu ele verir. Detektörler (Turnitin, GPTZero, Pangram) iki temel metriği ölçer:

- **Perplexity (tahmin edilemezlik):** YZ metninde düşük — çünkü YZ en olası kelimeyi seçer.
- **Burstiness (ritim varyasyonu):** YZ metninde düşük — çünkü cümleler hep benzer uzunlukta.

Bunlara ek olarak belirli kelimeler, kalıplar ve yapısal tercihler YZ yazımını imzalar gibi işaretler.

TezAtlas'ın amacı "detektörden kaçmak" değil — **kullanıcının sesini korumaktır.** Akademik metin, yazarının düşünce biçimini yansıtmalıdır.

---

## Katman 1: YZ Kelime Kara Listesi

Aşağıdaki kelime ve kalıplar Drafting Alternatives üretilirken **kullanılamaz.** Alternatif üretimde bu kelimeler görülürse otomatik olarak değiştirilir veya alternatif yeniden üretilir.

### 1a. İngilizce Kara Liste

**Kelimeler (tek kelime):**
```
delve, crucial, multifaceted, tapestry, landscape, meticulous,
meticulously, pivotal, underscore, vibrant, intricate, intricacies,
interplay, bolster, bolstered, garner, robust, holistic,
comprehensive, cutting-edge, embark, harness, testament, realm,
navigate, elevate, unleash, daunting, commendable, noteworthy,
groundbreaking, transformative, synergy, paradigm, nuanced,
streamline, leverage, foster, spearhead, unravel, underpin,
underpins, bustling, invaluable, indispensable, illuminating
```

**Kalıplar (çok kelime):**
```
"It is important to note that..."
"It is worth noting that..."
"In today's [adjective] world..."
"In today's digital age..."
"In the ever-evolving landscape of..."
"This serves as a testament to..."
"Not only... but also..." (art arda 2+ kez kullanıldığında)
"It's important to understand that..."
"From a broader perspective..."
"This is a game changer..."
"Designed to enhance..."
"In this article, we will explore..."
```

**Geçiş klişeleri (paragraf başında yasaklı):**
```
"Furthermore,"
"Moreover,"
"Additionally,"
"It is crucial to..."
"Firstly,... Secondly,... Lastly,..."
"In conclusion,"
"In summary,"
"Overall,"
"To summarize,"
```

### 1b. Türkçe Kara Liste

**Kelimeler:**
```
derinlemesine (tek başına geçiş olarak), kapsamlı bir şekilde,
çok yönlü, bütüncül, paradigma (gereksiz kullanımda), sinerji,
dönüştürücü, yenilikçi (klişe olarak), dinamik (içi boş kullanımda),
stratejik öneme sahip (gerekçesiz), önemle belirtilmelidir ki,
tartışmasız, yadsınamaz, kuşkusuz (kanıt olmadan)
```

**Kalıplar:**
```
"Günümüz dünyasında..."
"Bu bağlamda önem arz etmektedir."
"Sonuç olarak, yukarıda ele alınan..."
"Ayrıca belirtilmelidir ki..."
"Öte yandan değinilmesi gereken bir diğer husus..."
"Tüm bu değerlendirmeler ışığında..."
"Bu durum, ... açısından son derece önemlidir."
"Bilindiği üzere..."
"Hiç şüphesiz ki..."
"Dikkat çekici bir şekilde..."
```

### 1c. İzin Verilenler

Kara listedeki kelimeler **tamamen yasaklı değildir** — ancak şu koşullarda kullanılabilir:
- Doğrudan alıntı içinde (kaynaktan aynen aktarılıyorsa)
- Terim olarak `TERMINOLOJI.md`'de tanımlıysa (ör. "paradigma" bir teorik çerçevenin adıysa)
- Bir oturumda aynı kara liste kelimesi en fazla **1 kez** geçebilir

### 1d. Ne Kullanılmalı?

Kara liste kelimesi yerine:
- **Spesifik ol.** "Crucial" yerine → ne için kritik olduğunu söyle.
- **Somut ol.** "Landscape" yerine → tam olarak hangi alan, hangi bağlam.
- **Doğrudan söyle.** "It is important to note that" yerine → doğrudan söyle.
- **Geçişi içerikle kur.** "Furthermore" yerine → önceki cümlenin içeriğinden geçiş yap.

---

## Katman 2: Burstiness Kontrolü

YZ metninin en güçlü imzası cümle uzunluğundaki monotonluktur. İnsan yazıda kısa vurgular ve uzun akışlar karışır. YZ'de her cümle 18-22 kelime civarındadır.

### 2a. Cümle Uzunluğu Varyasyonu (Zorunlu)

Her paragrafta cümle uzunlukları **en az 3 farklı bant**ta olmalıdır:

| Bant | Kelime sayısı | Örnek kullanım |
|------|--------------|----------------|
| Kısa | 3–10 | Vurgu, sonuç, karşıtlık |
| Orta | 11–22 | Standart akademik cümle |
| Uzun | 23–40+ | Bağlam kurma, koşullu ifade, çok kaynaklı sentez |

**Kural:** Bir paragrafta 4+ cümle varsa en az bir kısa (≤10) ve en az bir uzun (≥23) cümle bulunmalıdır. Ardışık 3 cümle aynı bantta olamaz.

**Kontrol anı:** Drafting Alternatives üretildikten sonra, puanlama öncesinde.

### 2b. Paragraf Açılış Çeşitliliği (Zorunlu)

Ardışık paragraflar aynı yapıyla başlayamaz. Kontrol tablosu:

| Açılış tipi | Açıklama | Örnek |
|------------|----------|-------|
| İddia | Doğrudan bir önerme | "Merkez bankaları bu aracı..." |
| Soru | Retorik veya araştırma sorusu | "Peki bu politika değişikliği..." |
| Veri/Bulgu | Sayısal veya ampirik giriş | "2023 verilerine göre..." |
| Karşıtlık | Önceki paragrafı sorgulama | "Ancak bu görüşe karşı..." |
| Tarihsel/Bağlam | Zaman çerçevesi kurma | "2008 krizinden bu yana..." |
| Kaynak | Bir yazarın pozisyonuyla açma | "Stiglitz'in (2019) ifadesiyle..." |

**Kural:** Aynı açılış tipi ardışık 2 paragrafta kullanılamaz. Bir bölümde en az 3 farklı açılış tipi kullanılmalıdır.

### 2c. Yapısal Çeşitlilik

YZ metni her cümlede Özne-Yüklem-Nesne sırası kullanır. İnsan yazıda:
- Bazen yan cümle öne gelir: "Her ne kadar veriler X'i gösterse de..."
- Bazen yüklem başta durur (Türkçe'de özellikle): "Gösterilmiştir ki..."
- Bazen parantez içi açıklama cümleyi böler
- Bazen çok kısa bir cümle önceki uzun cümlenin etkisini artırır

**Kural:** Bir paragraftaki cümlelerin en az %30'u standart Ö-Y-N dışı bir yapıda olmalıdır.

### 2d. Liste/Madde Kullanımı

YZ sık sık bullet point listesi üretir. Akademik yazıda:
- Madde listeleri **yalnızca** gerçekten paralel yapıda olan öğeler için kullanılır (yöntem adımları, değişken listesi)
- Argüman, analiz ve tartışma **asla** madde listesiyle sunulmaz
- Bir bölümde madde listesi oranı toplam metnin %15'ini geçemez

---

## Katman 3: Yazım Stili Profili

Her kullanıcının kendine özgü yazma parmak izi vardır. Bu profil onboarding'de veya ilk yazım oturumunda oluşturulur ve `YAZIM_PROFILI.md` dosyasında saklanır.

### 3a. Profil Oluşturma

İki yöntem:

**Yöntem A — Örnek metin analizi (önerilen):**
Kullanıcıdan daha önce yazdığı 2-3 sayfalık bir akademik metin istenir. AI bu metni analiz ederek profili otomatik oluşturur:
- Ortalama cümle uzunluğu ve varyasyonu
- Tercih ettiği geçiş yapıları
- Noktalama alışkanlıkları (noktalı virgül sıklığı, tire kullanımı, parantez kullanımı)
- Paragraf uzunluğu tercihi
- Edilgen/etken yapı oranı
- Sıkça kullandığı kalıplar

**Yöntem B — Soru-cevap:**
Kullanıcıya doğrudan sorulur (şablon: `tpl-writing-profile.md`)

### 3b. Profil Dosyası Formatı

```markdown
## YAZIM_PROFILI.md

### Cümle Tercihleri
- Ortalama cümle uzunluğu: [X] kelime
- Uzunluk varyasyonu: [düşük/orta/yüksek]
- Kısa vurgu cümleleri kullanır mı: [evet/hayır]

### Noktalama
- Noktalı virgül: [sık/nadir/hiç]
- Tire arası açıklama (— ... —): [sık/nadir/hiç]
- Parantez içi açıklama: [sık/nadir/hiç]
- İki nokta (:) ile liste açma: [sık/nadir/hiç]

### Paragraf Yapısı
- Tercih edilen paragraf uzunluğu: [kısa 3-5 cümle / orta 5-8 / uzun 8+]
- Madde listesi tercihi: [sık/nadir/hiç — argümanı düzyazıyla mı anlatır?]
- Paragraf geçiş stili: [geçiş cümlesiyle / içerikle / bağlaçla]

### Üslup
- Edilgen/etken oranı: [ağırlıklı edilgen / dengeli / ağırlıklı etken]
- Hedging yoğunluğu: [çekingen / dengeli / kararlı]
- Doğrudan alıntı sıklığı: [sık/nadir]
- Retorik soru kullanır mı: [evet/hayır]

### Kaçınılanlar (kullanıcı beyanı)
- [kullanıcının "ben bunu yapmam" dediği şeyler]
- Örnek: "Tire arası cümle yazmıyorum"
- Örnek: "Noktalı virgül kullanmıyorum, yeni cümle başlarım"
- Örnek: "Madde listesi yerine uzun paragraflar tercih ederim"
```

### 3c. Profil Uygulama Kuralı

Draft Generator modunda her alternatif üretilirken `YAZIM_PROFILI.md` okunur ve şu kontroller yapılır:

1. **Kaçınılan yapı kontrolü:** Profilde "hiç" veya "kaçınılan" olarak işaretlenen yapı kullanılmışsa → alternatif yeniden üretilir
2. **Uzunluk uyumu:** Cümle ve paragraf uzunlukları profilin bantlarına uymalı
3. **Noktalama uyumu:** Profilde "hiç" olan noktalama işareti kullanılmışsa → düzeltilir
4. **Üslup uyumu:** Edilgen/etken oranı profille tutarlı olmalı

**Thought Partner modunda** profil uygulanmaz (kullanıcı kendisi yazıyor). Ancak kullanıcı yazarken profille çelişen bir yapı kullanırsa AI bunu işaretlemez — bu kullanıcının bilinçli tercihi olabilir.

### 3d. Profil Evrimi

Profil statik değildir:
- Her yazım oturumunda AI, kullanıcının seçimlerini gözlemler
- Kullanıcı sürekli olarak B alternatifini seçiyorsa (daha uzun, daha akıcı) → profil güncellemesi önerilir
- Kullanıcı "bundan sonra noktalı virgül de kullanayım" derse → profil güncellenir
- `DERSLER.md`'ye yazılacak stil dersleri profili otomatik günceller

---

## Üç Katmanın Birlikte Çalışması

```
Drafting Alternatives tetiklendi
    │
    ├─ 1. YAZIM_PROFILI.md oku → kullanıcı parmak izi yükle
    │
    ├─ 2. Alternatifleri üret (paragraph-coherence.md bağlamıyla)
    │
    ├─ 3. Kara Liste Filtresi
    │   └─ Yasaklı kelime/kalıp var mı? → varsa değiştir
    │
    ├─ 4. Burstiness Kontrolü
    │   ├─ Cümle uzunluk bantları (3 bant zorunlu)
    │   ├─ Ardışık paragraf açılış çeşitliliği
    │   ├─ Yapısal çeşitlilik (≥%30 non-SVO)
    │   └─ Geçemezse → alternatifi yeniden üret
    │
    ├─ 5. Stil Profili Uyumu
    │   ├─ Kaçınılan yapı var mı?
    │   ├─ Uzunluk profilinde mi?
    │   └─ Noktalama tercihleriyle uyumlu mu?
    │
    └─ 6. Puanlama matrisine sun
        (Savunma + Akıcılık + Özgünlük + Bağlam)
        + her alternatifin yanında: "Profil uyumu: ✓/⚠️"
```

---

## Kalite Kontrol Entegrasyonu

Her bölüm sonrası [[quality-control]] kontrol listesine eklenen maddeler:

```
Doğal Ses Kontrolü (natural-voice):
- [ ] Kara liste kelimesi paragraf başında veya geçiş olarak kullanılmamış mı?
- [ ] Cümle uzunluk varyasyonu yeterli mi? (3 bant zorunlu)
- [ ] Ardışık paragraflar farklı yapıyla mı açılıyor?
- [ ] Madde listesi oranı %15'in altında mı?
- [ ] YAZIM_PROFILI.md ile uyumlu mu?
```
