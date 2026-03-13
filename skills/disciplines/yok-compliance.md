---
title: "YÖK Tez Format Uyum Kılavuzu"
title_en: "YÖK Thesis Format Compliance Guide"
node_type: tooling
description: "YÖK (Yükseköğretim Kurulu) tez yazım kılavuzu kuralları, üniversite bazlı ek kısıtlamalar ve TezAtlas format kontrol listesi. Faz 0'da yükle."
description_en: "YÖK thesis format rules, university-specific additions, and TezAtlas format checklist. Load at Phase 0."
tags: [yok, formatting, turkish-universities, compliance, thesis, discipline]
links_to:
  - skills/moc/MOC-universities.md
  - skills/phases/thesis/phase-0-identity.md
  - skills/templates/tpl-yok-cover.md
language: bilingual
version: "1.0"
---

# YÖK Tez Format Uyum Kılavuzu

## YÖK Temel Format Kuralları

*Kaynak: YÖK Tez Yazım Kılavuzu (güncel sürüm için üniversitenin araştırma ofisini teyit et)*

### Sayfa Düzeni

| Parametre | YÖK Standardı |
|-----------|---------------|
| Kağıt boyutu | A4 (210 × 297 mm) |
| Sol kenar | 3,5 cm |
| Sağ kenar | 2,5 cm |
| Üst kenar | 3,0 cm |
| Alt kenar | 2,5 cm |
| Yazı tipi | Times New Roman veya Arial |
| Ana metin boyutu | 12 punto |
| Dipnot boyutu | 10 punto |
| Satır aralığı | 1,5 |
| Paragraf girintisi | 1,25 cm (ilk satır) |
| Paragraf arası boşluk | 6 nk önce, 6 nk sonra (bazı üniversiteler 0 ister) |

### Sayfa Numaralandırma

- **Ön sayfalar** (kapak → içindekiler): Roma rakamı (i, ii, iii …)
- **Kapak sayfası**: Numarasız (ama i sayılır)
- **Ana metin başlangıcı**: Arap rakamı (1'den başlar)
- **Numaralandırma konumu**: Alt orta VEYA alt sağ (üniversiteye göre)

### Başlık Hiyerarşisi

```
BÖLÜM 1 (Tümü büyük, bold, 14p, ortalanmış)
  1.1 Alt Bölüm (Title Case, bold, 12p, sola hizalı)
    1.1.1 Alt Alt Bölüm (Title Case, bold, 12p, sola hizalı)
      1.1.1.1 Dördüncü Seviye (Normal, bold+italic, 12p)
```

---

## Ön Sayfalar Sırası

Aşağıdaki sıra YÖK standardıdır. Üniversiteye göre ek sayfalar eklenebilir:

```
1. Dış Kapak (harici kapak, ciltlenmiş)
2. İç Kapak (tez başlığı, öğrenci bilgileri)
3. Jüri Onay Sayfası
4. Etik Beyan Sayfası ← YÖK 2020 sonrası zorunlu
5. Önsöz / Teşekkür (opsiyonel)
6. İçindekiler
7. Tablolar Listesi (varsa)
8. Şekiller Listesi (varsa)
9. Kısaltmalar Listesi (varsa)
10. Özet (Türkçe)
11. Abstract (İngilizce)
← BURADAN ANA METİN BAŞLAR →
```

---

## Üniversite Bazlı Farklılıklar

### ODTÜ (METU)
- Yazı tipi: Times New Roman, 12p (EN veya TR)
- Kenarlar: Sol 3,5 / Sağ 2,5 / Üst 3 / Alt 2,5
- Tez İngilizce yazılabilir; özet her iki dilde zorunlu
- Jüri sayfasında imza yeri: 5 jüri üyesi (doktora)
- Format kılavuzu: [thesis.metu.edu.tr](https://thesis.metu.edu.tr)
- **Fark:** Abstract + Özet AYRI sayfalar, her ikisi zorunlu

### İTÜ (ITU)
- Yazı tipi: Times New Roman, 12p
- Kenarlar: Sol 4 / Sağ 2,5 / Üst 3 / Alt 2,5 (**sol daha geniş**)
- Satır aralığı: 1,5
- Başlıklar: Büyük harf, koyu, ortalı
- Kapak rengi: Lacivert (lisans), Bordo (yüksek lisans), Siyah (doktora)
- **Fark:** Kapak rengi teze göre değişir; baskı zorunluluğu vardır

### Boğaziçi Üniversitesi (BOUN)
- İngilizce tez standart; Türkçe özet zorunlu (İng. tezde)
- Yazı tipi: Times New Roman veya benzeri serif, 12p
- Kenarlar: 2,54 cm her taraf (APA standart)
- **Fark:** Daha liberal format, danışman onayı belirleyici

### Hacettepe Üniversitesi (HÜ)
- Yazı tipi: Times New Roman, 12p
- Kenarlar: Sol 3,5 / Sağ 2,5 / Üst 3 / Alt 2,5
- Sağlık bilimleri tezleri: CONSORT/STROBE ek tabloları zorunlu olabilir
- Etik kurul belgesi ön sayfalara eklenir
- **Fark:** Sağlık tezlerinde ekler (etik, istatistik danışmanlığı) zorunlu

### Ankara Üniversitesi (AÜ)
- Yazı tipi: Times New Roman, 12p
- Kenarlar: Sol 4 / Sağ 2,5 / Üst 3 / Alt 2,5
- Hukuk fakültesi tezleri: dipnot yoğun, Chicago Turabian stili
- **Fark:** Sol kenar 4 cm (ciltleme payı daha fazla)

### İstanbul Üniversitesi (İÜ)
- Yazı tipi: Times New Roman, 12p
- Kenarlar: Sol 3,5 / Sağ 2,5 / Üst 3 / Alt 2,5
- Kaynakça: APA 7 (fen/sosyal), Chicago 17 (hukuk/beşeri)
- **Fark:** Fakülteye göre atıf stili değişir

---

## TezAtlas Format Kontrol Listesi (Faz 7 Öncesi)

Tez bitirilmeden önce bu listeyi çalıştır:

**Sayfa Düzeni:**
- [ ] Kenar boşlukları üniversite kılavuzuna uygun mu?
- [ ] Yazı tipi ve punto tutarlı mı (tüm metinde)?
- [ ] Satır aralığı doğru mu?
- [ ] Sayfa numaraları doğru konumda ve formatında mı?

**Ön Sayfalar:**
- [ ] Kapak sayfası tam ve doğru mu? (`tpl-yok-cover.md` ile karşılaştır)
- [ ] Jüri onay sayfası üniversite formatında mı?
- [ ] Etik beyan sayfası var mı ve imzalı mı?
- [ ] Özet (TR) + Abstract (EN) her ikisi de var mı?
- [ ] Özet 150-350 kelime aralığında mı? (YÖK standardı)
- [ ] Abstract aynı aralıkta mı?

**İçerik:**
- [ ] İçindekiler tablosu güncel mi? (son bölüm değişiklikleri yansıdı mı?)
- [ ] Tablo ve şekil listesi numaraları doğru mu?
- [ ] Kısaltmalar listesi eksiksiz mi?

**Kaynakça:**
- [ ] Atıf stili tutarlı mi (karışık APA/Chicago yok)?
- [ ] Kaynakçadaki her eser metinde geçiyor mu?
- [ ] Metindeki her kaynak kaynakçada var mı?

**YÖK'e Yükleme:**
- [ ] PDF/A formatında mı? (YÖK Tez Merkezi zorunluluğu)
- [ ] Dosya boyutu < 100 MB mi?
- [ ] Gömülü fontlar var mı?
- [ ] YÖK Tez Merkezi başvurusu tamamlandı mı?

---

## YÖK Tez Merkezi Yükleme Notları

- **URL:** [tez.yok.gov.tr](https://tez.yok.gov.tr)
- **Format:** PDF/A-1b tercih edilir (uzun dönem arşiv standardı)
- **Gizlilik:** Erişim kısıtlaması (6 ay / 1 yıl / süresiz) talep edilebilir
- **Telif:** Yükleme = telif devri değildir; öğrenci hakları korunur
- **Veri güvenliği:** Hasta verisi içeren tezler: kimlik bilgileri anonimleştirilmeli

---

## Atıf Stillerinin Üniversite-Disiplin Matrisi

| Disiplin | Yaygın Stil | Notlar |
|----------|-------------|--------|
| Fen/Mühendislik | APA 7 / IEEE | IEEE: metin içi numara [1] |
| Sosyal Bilimler | APA 7 | Türkçe APA çevirisi için TPA (Türk Psikoloji Derneği) rehberi |
| Hukuk | Chicago 17 (dipnot) | Yargıtay/Danıştay kararları özel format gerektirir |
| Tıp/Sağlık | Vancouver / APA 7 | Vancouver: numara sistemi, çok tercih edilen |
| Beşeri Bilimler | Chicago 17 / MLA 9 | Tarih: Chicago; Edebiyat: MLA |
| İlahiyat | Chicago 17 | Arapça/Osmanlıca kaynak formatı özel |
