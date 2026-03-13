# Literatür Zekası Katmanı / Literature Intelligence Layer

## Amaç

Yazma fazlarında (Phase 5-6) otomatik kaynak ilişkilendirme, çelişki uyarıları ve argüman eşleştirmesi sağlar.

## Ne Zaman Aktif?

- `/review-draft` çağrıldığında (Katman 4: Literatür Uyumluluğu)
- Yazma oturumlarında paragraf düzeyinde öneri
- Her bölüm tipine özel kontroller

## Nasıl Çalışır?

`core/literature_intel.py` modülü:

1. **NoteIndex**: `notes/` klasöründeki tüm notları anahtar kelime bazlı indeksler
2. **ArgumentIndex**: `ARGUMENTS.md`'deki argümanları indeksler
3. **LiteratureIntel**: Paragraf bazlı analiz motoru

### Analiz Türleri

| Analiz | Açıklama | Çıktı |
|--------|----------|-------|
| `find_related` | Metinle en ilgili kaynakları bulur | Sıralı kaynak listesi |
| `find_contradicting` | Metinle çelişen kaynakları tespit eder | Çelişki uyarıları |
| `find_matching` | Metinle eşleşen argümanları bulur | Argüman eşleştirmesi |
| `analyze_paragraph` | Tüm analizleri tek paragraf için çalıştırır | Kapsamlı rapor |
| `review_for_section` | Bölüm bazlı inceleme | Bölüme özel kontroller |

### Bölüm Algılama

Otomatik algılama mekanizması:
1. **Dosya adından**: `giris.md` → Intro, `literatur.md` → Literature Review
2. **İçerikten**: Anahtar kelime yoğunluğuna göre bölüm tipi tespiti
3. **STATUS.md** ile çapraz kontrol

### Bölüme Özel Araçlar

| Bölüm | Önerilen Araçlar | Kontroller |
|-------|------------------|------------|
| Giriş | `/so-what`, `/knowledge-map` | RQ netliği, kapsam kontrolü |
| Literatür | `/intake`, `/contradictions`, `/citation-chain`, `/gaps` | Kapsam yeterliliği |
| Yöntem | `/method-audit` | İç tutarlılık, geçerlilik |
| Bulgular | — | Over-claiming kontrolü |
| Tartışma | `/assumptions`, `/knowledge-map`, `/devil-advocate` | Argüman bütünlüğü |
| Sonuç | `/so-what`, `/synthesize` | Genelleme kontrolü |

## Iron Rules

- Iron Rule 1: Kaynak önerileri sadece `notes/` klasöründen
- Iron Rule 4: Hiçbir kaynak fabrike edilmez
- Öneriler, uyarılar ve eşleştirmeler tamamen lokal veriye dayanır
