---
title: "Academic Writing Style Linter — Real-time"
title_tr: "Akademik Yazım Stili Denetleyicisi — Gerçek Zamanlı"
node_type: technique
description: "Real-time inline feedback during Phase 6 writing: passive voice density, hedge word frequency, overclaiming detection, sentence length variance, discipline-appropriate register. tools/style_linter.py."
description_tr: "Faz 6 yazımı sırasında gerçek zamanlı satır içi geri bildirim: pasif çatı yoğunluğu, çekince kelime sıklığı, aşırı iddia tespiti, cümle uzunluğu varyansı, alana uygun tarz. tools/style_linter.py."
tags: [technique, style-linter, realtime, passive-voice, hedging, phase-6, writefull, inline-feedback]
links_to:
  - skills/techniques/style-checker.md
  - tools/style_linter.py
language: bilingual
version: "1.0"
---

# Akademik Yazım Stili Denetleyicisi — Gerçek Zamanlı

## Kullanım / Usage

```bash
# Tek dosya (İngilizce)
python3 tools/style_linter.py bolum3.md

# Türkçe metin
python3 tools/style_linter.py bolum3.md --lang tr

# Dizindeki tüm taslaklar
python3 tools/style_linter.py --dir draft/ --lang tr

# Daha sıkı pasif eşiği (yöntem bölümü değilse)
python3 tools/style_linter.py bolum4.md --lang tr --threshold 0.15

# Makine çıktısı (CI/pipeline için)
python3 tools/style_linter.py paper.md --json
```

---

## Örnek Çıktı / Sample Output

```
Stil Denetim Raporu — bolum3.md
══════════════════════════════════════════════
Kelime: 2847 | Cümle: 184 | Puan: 74/100 ⚠️
──────────────────────────────────────────────
Pasif çatı:      %18  ✅
Çekince zinciri: 2     ⚠️
Aşırı iddia:     1     ❌

❌ Hatalar:
  Satır 142: Aşırı iddia: "definitively proves"
    → Öneri: provides evidence for

⚠️  Uyarılar:
  Satır 67: Çekince zinciri (3 kelime): perhaps + might + possibly
    → Çekince katmanlarını azaltın
  Satır 198: Çekince zinciri (3 kelime): seemingly + apparently + arguably
    → Çekince katmanlarını azaltın
```

---

## Denetlenen Boyutlar / Dimensions Checked

| Boyut | Eşik | Dil |
|-------|------|-----|
| Pasif çatı | > %25 (varsayılan) | EN + TR |
| Çekince zinciri | ≥ 3 kelime aynı cümlede | EN + TR |
| Aşırı iddia | Regex pattern eşleşmesi | EN + TR |
| Cümle uzunluğu | > 60 kelime | Dil agnostik |

---

## Faz 6 ile Entegrasyon / Phase 6 Integration

**Yazım sırasında** (her paragraf sonrası — opsiyonel):
```bash
python3 tools/style_linter.py --quiet bolum.md
```

**Faz geçiş kapısında** (Phase 6 → 7 — önerilen):
```bash
python3 tools/style_linter.py bolum.md --lang tr
# Puan ≥ 70 → geçiş onaylandı
# Puan < 70 → revizyona yönlendir
```

---

## Stil Denetleyicisi vs. Style Checker (#34)

| #34 Style Checker | #72 Style Linter |
|-------------------|-----------------|
| Kavramsal açıklama (bu dosya) | Çalıştırılabilir araç (`tools/style_linter.py`) |
| Phase gate protokolü | Gerçek zamanlı + gate |
| Temel denetim kuralları | Regex tabanlı otomatik tespit |

Bütünleşik kullanım: #34 hangi kuralların uygulandığını açıklar, #72 araştırmacı bunları otomatik taramak için çalıştırır.

---

## Puan Sistemi / Scoring

| Puan | Durum |
|------|-------|
| 80-100 | ✅ İyi — faz geçişi onaylandı |
| 60-79 | ⚠️ Dikkat — birkaç sorun var |
| < 60 | ❌ Revizyon gerekli |

Puan düşürücüler:
- Pasif oranı her %5 aşım için: -5
- Her çekince zinciri: -5 (maks. -20)
- Her aşırı iddia: -10 (maks. -30)
