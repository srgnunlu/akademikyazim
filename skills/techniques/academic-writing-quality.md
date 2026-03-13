---
title: "Academic Writing Quality — Prose Standards for Publication"
title_tr: "Akademik Yazı Kalitesi — Yayın Standartlarında Düzyazı"
node_type: technique
description: "Active quality protocol for academic prose: hedging, signposting, argument flow (claim-evidence-warrant), register, and eliminating padding. Fires at Phase 5/6 writing stages across all document types."
description_tr: "Akademik düzyazı için aktif kalite protokolü: hedging, yol gösterme, argüman akışı (iddia-kanıt-gerekçe), üslup ve dolgu temizleme. Tüm belge türlerinde Faz 5/6 yazım aşamalarında tetiklenir."
tags: [writing-quality, hedging, signposting, argument-flow, register, academic-prose, phase-5, phase-6]
links_to:
  - skills/core/writing-psychology.md
  - skills/core/quality-control.md
  - skills/techniques/literature-synthesis.md
  - skills/techniques/pre-submission-review.md
used_by:
  - skills/phases/thesis/phase-6-writing.md
  - skills/phases/article/phase-4-writing.md
  - skills/phases/article/phase-5-revision.md
  - skills/phases/conference/phase-3-writing.md
language: bilingual
version: "1.0"
---

# Akademik Yazı Kalitesi / Academic Writing Quality

Kaynak disiplini gerekli ama yeterli değil.
Mükemmel kaynak altyapısı zayıf düzyazıyla boşa gider.

Bu node, her yazım oturumunun sonunda çalışır.

---

## 1. Hedging — Akademik Çekinme Dili

Akademik yazıda kesinlik değil, kanıta dayalı ihtiyat standarttır.
Aşırı kesinlik: hakemleri uyarır. Aşırı çekinme: argümanı zayıflatır.

**Güçlü hedging kalıpları (TR):**
```
"Bulgular X'e işaret etmektedir."          ✅
"Veriler X'i destekler niteliktedir."      ✅
"Bu durum X olarak değerlendirilebilir."   ✅
"Sonuçlar X olduğunu göstermektedir."      ✅ (nicel veri varsa)
"X olduğu söylenebilir."                  ⚠️  (zayıf — spesifikleştir)
"X'tir." (mutlak iddia, kanıtsız)          ❌
"X olduğu açıktır."                        ❌ (açık değil, kanıtla)
```

**Güçlü hedging kalıpları (EN):**
```
"The findings suggest that X..."           ✅
"This appears to indicate X..."            ✅
"The data are consistent with X..."        ✅
"X is clearly the case."                  ❌
"Obviously, X."                            ❌
```

**Claude'a hedging denetimi için prompt:**
```
Bu paragraftaki her iddianın kanıt düzeyi ile
hedging yoğunluğu arasında uyum var mı?
Aşırı güçlü veya aşırı zayıf ifadeleri işaretle.
```

---

## 2. Signposting — Yol Gösterme

Okuyucu her an "şu an neredeyim, nereye gidiyorum?" bilmeli.

**Bölüm açılışı:**
```
TR: "Bu bölümde X ele alınmakta; Y analiz edilmekte ve Z tartışılmaktadır."
EN: "This section examines X, analyses Y, and discusses Z."
```

**Paragraf geçişleri:**
```
TR: "X gösterildikten sonra şimdi Y'ye geçilebilir."
    "Bununla birlikte..." / "Öte yandan..." / "Bu bağlamda..."
EN: "Having established X, this section now turns to Y."
    "Furthermore..." / "In contrast..." / "Building on this..."
```

**Bölüm kapanışı:**
```
TR: "Bu bölümde X, Y ve Z incelenmiştir. Bir sonraki bölümde..."
EN: "This section has examined X, Y, and Z. The following section will..."
```

**Hatalı signposting örnekleri:**
```
❌ "Yukarıda belirtildiği gibi..." (kaçıncı kez belirtildi?)
❌ "Aşağıda görüleceği üzere..." (okuyucuyu bekletme, şimdi söyle)
❌ Geçiş cümlesi olmadan paragraf başlatmak
```

---

## 3. Argüman Akışı — İddia / Kanıt / Gerekçe

Her paragrafın üç parçası olmalı:

```
[İDDİA]   Bu paragrafın ana önermesi — 1 cümle
[KANIK]   Bu iddiayı destekleyen kaynak, veri veya örnek
[GEREKÇE] Kanıtın iddiayı neden desteklediği — bağlantı cümlesi
```

**Kötü paragraf (iddia var, kanıt yok):**
> "Dijital para birimleri merkez bankacılığını köklü biçimde dönüştürmektedir. Bu dönüşüm hız kazanmaktadır. Dünya genelinde pek çok merkez bankası bu alanda çalışmaktadır."

**İyi paragraf (İ-K-G yapısı):**
> "Dijital merkez bankası paraları, geleneksel para politikası araçlarını genişletme potansiyeli taşımaktadır [İDDİA]. BIS (2022) anketine göre merkez bankalarının %93'ü CBDC araştırması yürütmektedir ve %26'sı pilot aşamasındadır [KANIK]. Bu yoğun araştırma faaliyeti, CBDC'nin teorik tartışmadan uygulama gündemine geçtiğini göstermektedir [GEREKÇE]."

**Claude'a yapı denetimi için prompt:**
```
Bu paragrafta iddia, kanıt ve gerekçeyi ayrı ayrı işaretle.
Eksik olan hangisi? Kanıt kaynağı /sources/ klasöründe mevcut mu?
```

---

## 4. Register — Akademik Üslup

| Kaçın | Kullan |
|-------|--------|
| "Ben düşünüyorum ki" | "Bu çalışma öne sürmektedir ki" |
| "Çok önemli" | "Kritik öneme sahip" / nicel ise "istatistiksel olarak anlamlı" |
| "Açıkça görülüyor" | Kanıtı göster, "açıkça" deme |
| "vs." | "ile karşılaştırıldığında" |
| Ünlem işareti (!) | Yok — akademik yazıda asla |
| "vb." (belirsiz liste) | Listeyi tamamla veya "başta X olmak üzere" |
| Kısaltmalar (ilk kullanımda) | Açık yaz, sonra kısalt: "Türk Lirası (TL)" |

**Edilgen (pasif) yapı:**
Türkçe akademik yazıda edilgen tercih edilir:
```
✅ "Veriler analiz edilmiştir."
✅ "Bulgular değerlendirilmektedir."
⚠️ "Ben verileri analiz ettim." (birinci tekil — sakın)
```

İngilizce'de alan normu değişir:
```
Doğa bilimleri → pasif ("The sample was heated to...")
Sosyal bilimler → aktif giderek artıyor ("We argue that...")
```

---

## 5. Dolgu ve Tekrar Temizleme

Akademik yazının en yaygın kalite düşürücüsü: boş söylemek.

**Dolgu kalıpları — hepsini sil:**
```
"Bu çalışmanın önemi tartışılmaz."
"Günümüz dünyasında..."
"Tarih boyunca insanlar..."
"Sonuç olarak, sonuçlar göstermektedir ki..."
"Bu bağlamda bu konunun önemi büyüktür."
```

**Tekrar testi:**
Her cümleyi sor: "Bu cümle çıkarılsaydı okuyucu ne kaybederdi?"
Cevap "hiçbir şey" ise — sil.

**Claude'a dolgu denetimi için prompt:**
```
Bu bölümde semantik içerik taşımayan cümleleri listele.
Her cümle için: "Bu olmadan ne kaybedilir?" sorusunu yanıtla.
```

---

## Yazım Kalitesi Kontrol Akışı

Her bölüm tamamlandığında sırayla çalıştır:

```
1. Hedging uygun mu?          → Aşırı güçlü / zayıf ifade var mı?
2. Signpost tam mı?           → Bölüm açılış/kapanış + paragraf geçişleri
3. Her paragraf İ-K-G mi?     → Kanıtsız iddia var mı?
4. Register akademik mi?      → Birinci tekil, ünlem, dolgu var mı?
5. Tekrar temizlendi mi?      → Silinebilecek cümle kaldı mı?
```

Tüm 5 adım geçilmeden bir sonraki bölüme geçilmez.
