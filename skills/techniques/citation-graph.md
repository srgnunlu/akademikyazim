---
title: "Citation Graph Discovery — ResearchRabbit Protocol"
title_tr: "Atıf Grafiği Keşfi — ResearchRabbit Protokolü"
node_type: technique
description: "Structured snowball sampling via citation graph: given a seed paper, fetch citing/cited papers via Semantic Scholar (MCP server), score relevance, expand deferred source pool. Automates the most time-consuming part of literature discovery."
description_tr: "Atıf grafiği üzerinden yapılandırılmış kartopu örneklemesi: bir tohum makaleden, Semantic Scholar (MCP sunucu) aracılığıyla alıntılayan/alıntılanan makaleleri getir, ilgililik puanla, ertelenmiş kaynak havuzunu genişlet."
tags: [technique, citation-graph, snowball-sampling, semantic-scholar, mcp, phase-2, phase-3]
links_to:
  - skills/techniques/snowball-sampling.md
  - skills/core/agent-orchestration.md
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Atıf Grafiği Keşfi / Citation Graph Discovery

## Ne Zaman Kullan?

- Faz 2 başlangıcı: Tohum kaynak listesi hazır, genişletme gerekiyor
- Faz 3 okuma: Kaynak doygunluğuna ulaşılmadı (< 80%)
- `/kaynak-genişlet [doi]` komutu

**Gereksinim:** MCP server aktif olmalı (`mcp_server/server.py`, bkz. `mcp_server/README.md`)

---

## Protokol: 3 Genişleme Turu

### Tur 1 — İleri Arama (Yeni Çalışmalar)

Tohum makaleyi alıntılayan daha yeni çalışmaları bul:

```
MCP Tool: get_citations(paper_id="DOI:10.xxxx/...", limit=20)
```

Her sonuç için ilgililik puanla:
- **Yüksek (3):** Araştırma sorusuyla doğrudan örtüşen başlık + aynı metodoloji
- **Orta (2):** İlgili ama odak noktası farklı
- **Düşük (1):** Yalnızca konuya değinen, merkezi değil
- **İlgisiz (0):** Atla

### Tur 2 — Geri Arama (Temel Kaynaklar)

Tohum makalenin atıfta bulunduğu temel çalışmaları bul:

```
MCP Tool: get_references(paper_id="DOI:10.xxxx/...", limit=50)
```

Aynı puanlama. Özellikle dikkat: düşük yıllı, yüksek atıf sayılı kaynaklar = alandaki kurucu çalışmalar.

### Tur 3 — Tam Genişleme (İki Yön)

Puanı Yüksek (3) olan her kaynak için Tur 1+2'yi tekrarla:

```
MCP Tool: get_related_papers(paper_id="...", direction="both", limit=10)
```

---

## Çıktı: Ertelenmiş Kaynak Havuzu

Her tur sonunda `KAYNAK_ENVANTERI.md`'ye ekle:

```markdown
| DOI/ID | Başlık (kısaltılmış) | Yıl | Atıf | İlgililik | Kaynak | Durum |
|--------|---------------------|-----|------|-----------|--------|-------|
| 10.xxx | CBDC monetary policy... | 2023 | 145 | 3 | get_citations(K1) | 🔵 Havuzda |
| 10.yyy | Digital currency design | 2021 | 89 | 3 | get_references(K1) | 🔵 Havuzda |
| 10.zzz | Payment systems review | 2022 | 34 | 2 | get_citations(K1) | 🟡 İnceleniyor |
```

Durum kodları: 🔵 Havuzda → 🟡 İnceleniyor → 🟢 Aktif kaynak → 🔴 Elendi

---

## Öncelik Sıralaması

Hangi kaynakları önce okuyacağına karar vermek için:

```
Öncelik = İlgililik × log(AtıfSayısı + 1)
```

Pratik olarak:
1. İlgililik=3 ve atıf sayısı > 100 → Mutlaka oku
2. İlgililik=3 ve atıf sayısı 20-100 → Üç ay içinde oku
3. İlgililik=2 → Ertelenmiş havuzda tut, ilk iki grup bitmeden okuma
4. İlgililik=1 → Sadece başlık+özet kontrolü

---

## Doygunluk Kontrolüne Bağlantı

Her atıf grafiği genişleme turunu `saturation-check.md` protokolüyle bitir:

- Yeni Yüksek (3) kaynak bulunamadıysa → **Doygunluk sinyali**
- Her yeni kaynağın referansları önceki listeden geliyor → **Alan sınırına ulaşıldı**
- Yeni kaynak bulunuyorsa ama hepsi 2019 öncesi → **Literatür durağan, yeni okuma yok**

---

## Hız Rehberi

| Tohum sayısı | Beklenen havuz büyümesi | Süre |
|-------------|------------------------|------|
| 1 tohum, 2 tur | +15-30 kaynak | 10 dk |
| 3 tohum, 2 tur | +40-80 kaynak | 25 dk |
| 5 tohum, 3 tur | +80-150 kaynak | 45 dk |

Hepsini okuma — öncelik sıralamasıyla filtrele. Hedefe (20-30 aktif kaynak) odaklan.
