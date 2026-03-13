---
title: "Citation Formatting — Style Guides and Reference Management"
title_tr: "Atıf Formatı — Stil Kılavuzları ve Kaynak Yönetimi"
node_type: technique
description: "Practical guide to citation formatting across APA 7, MLA 9, Chicago 17, Bluebook, and Vancouver styles. Includes discipline-to-style mapping, common citation patterns with examples, and AI-assisted format checking protocol."
description_tr: "APA 7, MLA 9, Chicago 17, Bluebook ve Vancouver atıf stillerine pratik kılavuz. Disipline göre stil eşleştirme, somut örneklerle yaygın atıf kalıpları ve AI destekli format kontrol protokolü içerir."
tags: [citation, APA, MLA, Chicago, Bluebook, Vancouver, references, bibliography, formatting]
links_to:
  - skills/core/iron-rules.md
  - skills/core/source-policy.md
  - skills/techniques/pre-submission-review.md
used_by:
  - skills/phases/thesis/phase-6-writing.md
  - skills/phases/article/phase-4-writing.md
  - skills/phases/article/phase-5-revision.md
  - skills/phases/grant-proposal/phase-4-writing.md
language: bilingual
version: "1.0"
---

# Atıf Formatı / Citation Formatting

Iron Rule 1: Atıf yapabilmek için kaynak `/sources/` klasöründe fiziksel olarak mevcut olmalı. Format doğru olsa bile kaynaksız atıf yasaktır.

---

## Disipline Göre Stil Seçimi

**Dergi/kurum stili her zaman önceliklidir.** Bu tablo varsayılan başlangıç noktasıdır:

| Disiplin | Standart Stil | Not |
|----------|--------------|-----|
| Sosyal Bilimler, Psikoloji, Eğitim | **APA 7** | En yaygın; Türkiye'de de standart |
| Beşeri Bilimler, Edebiyat, Dil Bilimi | **MLA 9** | Parenthetical atıf |
| Tarih, Felsefe, Sanat Tarihi | **Chicago 17** | Dipnot sistemi |
| Hukuk (ABD) | **Bluebook** | Mahkeme kararları + mevzuat |
| Hukuk (Türkiye) | **APA 7 veya kurum stili** | YÖK standartı yok; dergi belirler |
| Tıp, Hemşirelik, Eczacılık | **Vancouver** | Numaralı sistem |
| Ekonomi, Finans | **APA 7** | Bazen Chicago; dergi belirler |
| Mühendislik, Bilgisayar | **IEEE** | Numaralı; köşeli parantez |

---

## APA 7 — Temel Kalıplar

### Dergi Makalesi
```
Yazar, A. A., & Yazar, B. B. (Yıl). Makale başlığı: Alt başlık. Dergi Adı, cilt(sayı), sayfa–sayfa. https://doi.org/xxxxx
```
**Örnek:**
```
Kaya, M., & Demir, S. (2021). Dijital merkez bankası paralarının hukuki statüsü: Karşılaştırmalı bir analiz. Banka ve Finans Hukuku Dergisi, 12(3), 45–78. https://doi.org/10.xxxx/bfhd.2021.003
```

### Kitap
```
Yazar, A. A. (Yıl). Kitap adı: Alt başlık (Baskı no.). Yayınevi.
```
**Örnek:**
```
Yılmaz, H. (2019). Türk anayasa hukukunda yargısal denetim (3. bs.). Seçkin Yayıncılık.
```

### Kitap Bölümü
```
Yazar, A. A. (Yıl). Bölüm başlığı. B. Editör (Ed.), Kitap adı (ss. xx–xx). Yayınevi.
```

### Kurumsal Rapor
```
Kurum Adı. (Yıl). Rapor başlığı (Rapor No. XXX). https://...
```
**Örnek:**
```
Türkiye Cumhuriyet Merkez Bankası. (2023). Dijital Türk lirası araştırma raporu (Çalışma Kağıdı No. 23/04). https://www.tcmb.gov.tr/...
```

### Web Kaynağı
```
Yazar, A. A. (Yıl, Ay Gün). Sayfa başlığı. Site Adı. Erişim tarihi: Ay Gün, Yıl, https://...
```
*Erişim tarihi: yalnızca içerik sık değişiyorsa ekle.*

---

## Chicago 17 — Dipnot Sistemi

İki sistem: **Notes-Bibliography** (beşeri bilimler) ve **Author-Date** (sosyal bilimler).

### Dipnot Formatı (Notes-Bibliography):
```
¹ Ad Soyad, Kitap Adı (Yayın yeri: Yayınevi, Yıl), sayfa.
¹ Mehmet Kaya, Osmanlı İktisat Tarihi (İstanbul: İletişim Yayınları, 2018), 145.
```

### Kaynakça Formatı (Bibliography):
```
Soyad, Ad. Kitap Adı. Yayın yeri: Yayınevi, Yıl.
Kaya, Mehmet. Osmanlı İktisat Tarihi. İstanbul: İletişim Yayınları, 2018.
```

Dipnot ve kaynakça formatı farklıdır — ikisini karıştırma.

---

## Bluebook — Hukuki Atıflar (Legal Citations)

### Kanun / Mevzuat:
```
[TR] 6698 sayılı Kişisel Verilerin Korunması Kanunu, RG, 07.04.2016, S. 29677.
[US] Americans with Disabilities Act of 1990, Pub. L. No. 101-336, 104 Stat. 327.
```

### Mahkeme Kararı:
```
[TR] Anayasa Mahkemesi, E. 2021/14, K. 2022/87, 15.09.2022.
[US] Brown v. Board of Education, 347 U.S. 483 (1954).
```

Türk hukuku için: [mevzuat.gov.tr](https://www.mevzuat.gov.tr), [kazanci.com.tr](https://www.kazanci.com.tr), [lexpera.com.tr](https://www.lexpera.com.tr)

---

## Vancouver — Tıp ve Sağlık

Numaralı sistem: metinde `[1]`, `[2]` — kaynakça sıra numarasıyla.

```
1. Yazar AA, Yazar BB. Makale başlığı. Dergi Kısaltması. Yıl;cilt(sayı):sayfa-sayfa.
1. Şahin M, Çelik R. COVID-19 sonrası pulmoner rehabilitasyon. Türk Göğüs Has Derg. 2022;23(1):12-19.
```

---

## AI Format Kontrol Protokolü

Claude'dan atıf kontrolü istemek için bu prompt'u kullan:

```
Aşağıdaki kaynakçayı APA 7 kurallarına göre kontrol et.
Her hata için: (1) hatalı orijinal satır, (2) düzeltilmiş versiyon, (3) hangi kural ihlal edildi.

[Kaynakçanı buraya yapıştır]
```

**Uyarı:** Claude format hatalarını iyi bulur ama DOI numarasını ve sayfa numarasını `/sources/` klasöründeki PDF'e karşı sen doğrulamalısın. Iron Rule 4 burada geçerli — AI'ın söylediğine güvenme, kaynağı aç, kontrol et.

---

## Sık Yapılan Hatalar

- Yazar adı formatı tutarsız (kimi "A. A. Yazar", kimi "Yazar, A.")
- DOI yerine sadece URL yazmak
- Erişim tarihi gereksiz yere eklenmek (sabit sayfalarda gerek yok)
- Türkçe kaynakta İngilizce stil uygulamak (yayınevi adı çevrilmez)
- Kitap bölümünde editör adını unutmak
- "et al." eşiği yanlış (APA 7: 3+ yazar → et al., ilk atıftan itibaren)
- İtalik / düz yazım karıştırmak (APA: dergi adı ve kitap adı italik; makale başlığı değil)
- Sayfa aralığı eksik (s. 45 yerine s. 45–67 olmalı)
