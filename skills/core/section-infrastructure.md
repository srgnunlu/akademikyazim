# Bölüm Bazlı Altyapı / Section Infrastructure

## Amaç

Her akademik bölüm tipi kendi araç setine ve kalite kontrollerine sahiptir.
Bu kılavuz, bölüm algılama mekanizmasını ve her bölüm için özel kuralları tanımlar.

## Bölüm Tipleri

### 1. Giriş (Introduction)
**Amaç:** Araştırma sorusunu bağlamlandır ve gerekçelendir.

**Algılama:**
- Dosya adı: `giris`, `giriş`, `introduction`, `intro`
- İçerik: "araştırma sorusu", "amaç", "kapsam", "significance"

**Özel araçlar:** `/so-what`, `/knowledge-map`

**Kontroller:**
- [ ] Araştırma sorusu açık ve net mi?
- [ ] Kapsam belirli mi (ne DAHİL, ne HARİÇ)?
- [ ] Motivasyon somut mu?
- [ ] "So what?" sorusuna cevap veriyor mu?

### 2. Literatür Taraması (Literature Review)
**Amaç:** Mevcut bilgi birikimini sistematik olarak haritalandır.

**Algılama:**
- Dosya adı: `literatur`, `literatür`, `literature_review`, `related_work`
- İçerik: "literatür taraması", "mevcut çalışmalar", "prior research"

**Özel araçlar:** `/intake`, `/contradictions`, `/citation-chain`, `/gaps`

**Kontroller:**
- [ ] Kaynak çeşitliliği yeterli mi? (farklı yıllar, yöntemler, perspektifler)
- [ ] Sistematik bias var mı? (sadece destekleyen kaynaklar?)
- [ ] Kapsama yeterli mi? (tüm argümanlar kaynak desteğine sahip mi?)
- [ ] Sentez mi yoksa özet mi? (kaynaklar birbiriyle konuşuyor mu?)

### 3. Yöntem (Methodology)
**Amaç:** Araştırma tasarımını şeffaf ve tekrarlanabilir şekilde açıkla.

**Algılama:**
- Dosya adı: `yontem`, `yöntem`, `methodology`, `methods`
- İçerik: "örneklem", "veri toplama", "research design"

**Özel araçlar:** `/method-audit`

**Kontroller:**
- [ ] Yöntem araştırma sorusuyla uyumlu mu?
- [ ] İç geçerlilik tehditleri ele alınmış mı?
- [ ] Dış geçerlilik sınırları belirtilmiş mi?
- [ ] Etik onay (gerekiyorsa) belgelenmiş mi?

### 4. Bulgular (Results)
**Amaç:** Verileri nesnel olarak sun, yorum katma.

**Algılama:**
- Dosya adı: `bulgular`, `sonuclar`, `results`, `findings`
- İçerik: "tablo", "grafik", "istatistik", "analiz sonucu"

**Özel araçlar:** (veri-iddia eşleştirme)

**Kontroller:**
- [ ] Over-claiming yok mu? (veri desteklediğinden fazla iddia)
- [ ] Tüm veriler sunulmuş mu? (cherry-picking yok mu?)
- [ ] Tablolar ve grafikler bağımsız okunabilir mi?
- [ ] İstatistiksel anlamlılık doğru raporlanmış mı?

### 5. Tartışma (Discussion)
**Amaç:** Bulguları literatürle karşılaştır, yorumla, sınırlılıkları belirt.

**Algılama:**
- Dosya adı: `tartisma`, `tartışma`, `discussion`, `interpretation`
- İçerik: "tartışma", "karşılaştırma", "sınırlılık", "limitation"

**Özel araçlar:** `/assumptions`, `/knowledge-map`, `/devil-advocate`

**Kontroller:**
- [ ] Bulgular literatürle karşılaştırılmış mı?
- [ ] Beklenmedik sonuçlar açıklanmış mı?
- [ ] Sınırlılıklar dürüstçe belirtilmiş mi?
- [ ] Alternatif açıklamalar ele alınmış mı?

### 6. Sonuç (Conclusion)
**Amaç:** Katkıyı özetle, öneriler sun, gelecek araştırmayı yönlendir.

**Algılama:**
- Dosya adı: `sonuc`, `sonuç`, `conclusion`, `summary`
- İçerik: "sonuç", "öneri", "katkı", "future research"

**Özel araçlar:** `/so-what`, `/synthesize`

**Kontroller:**
- [ ] Aşırı genelleme yok mu?
- [ ] Katkı net ve somut mu?
- [ ] Öneriler veri destekli mi?
- [ ] Gelecek araştırma somut mu?

## Otomatik Algılama Mekanizması

`core/literature_intel.py` → `detect_section_type()` fonksiyonu:

1. **Dosya adından**: Stem'i normalize et, bilinen isimleri eşleştir
2. **İçerik analizinden**: İlk 2000 karakterde anahtar kelime yoğunluğu
3. **Eşik**: En az 2 anahtar kelime eşleşmesi gerekli

## Kullanım

`/review-draft` komutu bölüm tipini otomatik algılar ve:
- İlgili kontrolleri çalıştırır
- Bölüme özel araçları önerir
- Katman 4 (Literatür Uyumluluğu) raporunu bölüme göre özelleştirir

## Esneklik

- Bölümler arası geçiş serbest (Intro yazarken Method'a geçilebilir)
- Algılama hatalıysa kullanıcı düzeltebilir
- Tüm kontroller öneri niteliğinde — zorunlu değil
