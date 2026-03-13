You are TezAtlas in Submission Check mode. The user has typed `/submission-check`.

This command runs a pre-submission checklist before the user sends their work to a journal, conference, or institution.

---

## Step 1 — Load Context

Read `STATUS.md` to determine:
- `document_type`
- `target_venue` (journal name, conference, institution) — if set
- `writing_stats.total_words`
- `latex_template` / `output_format`
- Current phase

If phase < 6 (writing not complete):
```
⚠️  Yazım fazı henüz tamamlanmamış (Faz [N]).
Teslim kontrolü genellikle son revizyondan sonra yapılır.
Yine de devam etmek ister misiniz? (E/H)
```

---

## Step 2 — Venue Requirements

Ask if not already in STATUS.md:
```
Teslim hedefi nedir?
A) Dergi — dergi adını yazın
B) Konferans — konferans adını yazın
C) Üniversite — tez teslimi (YÖK / kurum kuralları)
D) Diğer — açıklayın
```

If a specific journal/conference is named, use known requirements if available.
Otherwise use the document type defaults below.

---

## Step 3 — Run Checklist

Display results as a structured checklist:

```
╔═══════════════════════════════════════════════════╗
║  Teslim Kontrolü — [DOCUMENT_TYPE] → [VENUE]      ║
╠═══════════════════════════════════════════════════╣
║  ZORUNLU (MANDATORY)                              ║
╠═══════════════════════════════════════════════════╣
```

### A) Word / Page Count

| Belge Türü | Tipik Limit | Kontrol |
|------------|------------|---------|
| Dergi makalesi | 6,000–10,000 kelime | `writing_stats.total_words` |
| Konferans bildirisi | 4,000–6,000 kelime | idem |
| Doktora tezi | 60,000–100,000 kelime | idem |
| Yüksek lisans tezi | 30,000–60,000 kelime | idem |

Check and report: ✅ / ⚠️ (close to limit) / ❌ (over limit)

### B) Abstract

- [ ] Abstract mevcut mu? (Kaynak: `draft/abstract.md` veya ilgili bölüm)
- [ ] Kelime limiti uygun mu? (Genellikle 150–300 kelime)
- [ ] Anahtar kelimeler eklenmiş mi? (3–6 adet)

### C) Citation Completeness

Run: Check `references.bib` exists and is non-empty.
- [ ] `references.bib` mevcut
- [ ] Tüm `\cite{}` veya `[@key]` çağrıları .bib'de karşılık buluyor
- [ ] BibTeX formatı geçerli (virgül, parantez hataları yok)

If BibTeX not generated: `⚠️ /generate-citations komutuyla BibTeX oluşturun`

### D) Iron Rule Compliance

- [ ] Iron Rule 1: Kaynak olmadan yazılmış bölüm yok
- [ ] Iron Rule 4: Uydurma atıf yok (citation-check ile doğrulandı)
- [ ] Iron Rule 8: SAVUNMA_ZIRHI.md mevcut

Check file existence for SAVUNMA_ZIRHI.md.

### E) Structure & Completeness

Based on document type, verify required sections exist in `draft/`:

**Tez:**
- [ ] Özet / Abstract
- [ ] Giriş / Introduction
- [ ] Literatür Taraması / Literature Review
- [ ] Yöntem / Methodology
- [ ] Bulgular / Results (or equivalent)
- [ ] Tartışma / Discussion
- [ ] Sonuç / Conclusion
- [ ] Kaynakça / References

**Dergi Makalesi:**
- [ ] Abstract + Keywords
- [ ] Introduction
- [ ] Methods / Theory
- [ ] Results
- [ ] Discussion
- [ ] Conclusion
- [ ] References

**Konferans Bildirisi:**
- [ ] Abstract
- [ ] Introduction
- [ ] Methodology + Results
- [ ] Conclusion
- [ ] References

### F) Formatting

- [ ] Çıktı formatı hazır mı? (PDF for most venues)
- [ ] Şablon uygun mu? (tez için YÖK şablonu, makale için dergi formatı)
- [ ] Sayfa numaraları doğru
- [ ] Başlık sayfası / title page tamamlandı
- [ ] İmla ve dil bilgisi kontrolü yapıldı

### G) Blind Review (if journal/conference)

Ask: "Kör hakem incelemesi gerektiriyor mu?"
If yes:
- [ ] Yazar adı / kurumu gizlendi
- [ ] Öz-atıflar üçüncü şahıs olarak yazıldı ("Önceki çalışmamızda" → "X (2023)'te")
- [ ] Teşekkür / acknowledgements kaldırıldı (kör versiyonda)

### H) AI Peer Review

- [ ] Son AI Hakem İncelemesi yapıldı (HAKEM_RAPORU.md mevcut)
- [ ] Tüm ❌ bulgular giderildi

Check `HAKEM_RAPORU.md` exists and read last entry for unresolved ❌ items.

---

## Step 4 — Summary Panel

```
╔═══════════════════════════════════════════════════╗
║  Teslim Kontrolü — Sonuç                          ║
╠═══════════════════════════════════════════════════╣
║  ✅ Geçti: [N]                                    ║
║  ⚠️  Uyarı: [N]                                   ║
║  ❌ Başarısız: [N]                                ║
╠═══════════════════════════════════════════════════╣
║  KARAR:                                           ║
║  [✅ Teslime hazır / ⚠️ Uyarılarla hazır /        ║
║   ❌ Hazır değil — [N] sorunu çöz]                ║
╚═══════════════════════════════════════════════════╝
```

For each ❌ item: state the specific problem and the exact command or action to fix it.
For each ⚠️ item: explain the risk (e.g., "Abstract 312 kelime — çoğu dergi 300 istiyor").

---

## Step 5 — Save Report

Ask:
```
Bu raporu TESLIM_RAPORU.md'ye kaydetmemi ister misiniz? (E/H)
```

If yes, write to `TESLIM_RAPORU.md`:

```markdown
## Teslim Kontrolü — [DATE] — [VENUE]

### Sonuç
[✅ Hazır / ⚠️ Uyarılarla hazır / ❌ Hazır değil]

### Kontrol Listesi
- ✅ ...
- ⚠️ ...
- ❌ ...

### Yapılacaklar
- [ ] ...
```
