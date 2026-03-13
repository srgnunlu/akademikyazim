---
title: "Phase 2 — Reading"
title_tr: "Aşama 2 — Okuma"
node_type: phase
phase_number: 2
document_type: report
phase_gate_in: "phase-1-evidence.md"
phase_gate_out: "phase-3-analysis.md"
description: "Process collected evidence using the 3-level reading system at a faster pace appropriate for action-oriented reports. Apply the [POLICY] tag for policy-relevant evidence. Iron Rules apply — every claim will need a traceable source in the final report."
description_tr: "Eylem odaklı raporlar için uygun daha hızlı bir tempoyla 3 düzeyli okuma sistemini kullanarak toplanan kanıtları işleyin. Politikayla ilgili kanıtlar için [POLİTİKA] etiketini uygulayın. Demir Kurallar geçerlidir — nihai rapordaki her iddianın izlenebilir bir kaynağa ihtiyacı olacaktır."
tags: [phase, report, reading, policy, annotation, iron-rules]
outputs:
  - "reading_notes.md"
links_to:
  - skills/core/iron-rules.md
  - skills/phases/report/phase-1-evidence.md
language: bilingual
version: "1.0"
---

# Phase 2 — Reading
# Aşama 2 — Okuma

## Gate Rule / Geçiş Kuralı

**EN:** Iron Rules apply to every source. A policy report that misattributes statistics or misrepresents findings causes direct decision-making harm. No claim enters the report without a traceable source.

**TR:** Demir Kurallar her kaynağa uygulanır. İstatistikleri yanlış atıflandıran veya bulguları yanlış temsil eden bir politika raporu, karar alma sürecine doğrudan zarar verir. Raporda izlenebilir kaynağı olmayan hiçbir iddia yer almaz.

---

## 1. The 3-Level System (Report Version) / 3 Düzeyli Sistem (Rapor Versiyonu)

**EN:** Same structure as thesis reading but at a faster pace because reports are action-oriented and timelines are usually shorter.

**TR:** Tez okumasıyla aynı yapı, ancak raporlar eylem odaklı olduğundan ve zaman çizelgeleri genellikle daha kısa olduğundan daha hızlı bir tempoyla.

**Level 1 — Scan / Tarama (5–10 min per source)**
- Read title, abstract/executive summary, headings, conclusion
- Decision: relevant enough to read fully? Tag: `[READ]` or `[SKIP]`

**Level 2 — Read / Okuma (full document)**
- Read fully; annotate key passages
- Mark claims that will be used in the report with source + page

**Level 3 — Extract / Çıkarma**
- Extract specific data points, statistics, quotations with full citation
- These form the evidence base for Phase 3

---

## 2. Annotation Tags / Açıklama Etiketleri

**EN:** Apply tags consistently. In a report context, prioritize tags that map to recommendations.

**TR:** Etiketleri tutarlı biçimde uygulayın. Rapor bağlamında önerilere eşleşen etiketlere öncelik verin.

| Tag / Etiket | Use / Kullanım |
|-------------|----------------|
| `[KEY]` | Core finding for the report's argument |
| `[POLICY]` | Policy-relevant evidence (specific to reports — not in thesis system) |
| `[DATA]` | Statistic or data point — record exact figure and source |
| `[REC]` | Evidence that directly supports a specific recommendation |
| `[LIMIT]` | Limitation of the evidence |
| `[CONTRA]` | Contradicts another source |
| `[QUOTE]` | Direct quotation suitable for report |
| `[SKIP]` | Not relevant to scope |

---

## 3. [POLICY] Tag — Special Handling / [POLİTİKA] Etiketi — Özel İşleme

**EN:** The [POLICY] tag is unique to the report document type. Apply it to evidence that:
- Describes an existing policy, regulation, or legal framework
- Reports outcomes of policy interventions elsewhere
- Is produced by a policy-making body (government, parliament, regulatory agency)
- Can directly justify or constrain a recommendation

**TR:** [POLİTİKA] etiketi rapor belge türüne özgüdür. Şunlar için uygulayın:
- Mevcut bir politika, düzenleme veya yasal çerçeve tanımlayan
- Başka yerlerdeki politika müdahalelerinin sonuçlarını raporlayan
- Bir politika yapıcı kurum (hükümet, parlamento, düzenleyici kurum) tarafından üretilen
- Doğrudan bir öneriyi meşrulaştırabilecek veya kısıtlayabilecek

---

## 4. Data Point Tracking / Veri Noktası Takibi

**EN:** For every statistic that will appear in the report, record source information in full at extraction time. Never reconstruct citations from memory later.

**TR:** Raporda yer alacak her istatistik için çıkarma sırasında kaynak bilgisini tam olarak kaydedin. Daha sonra atıfları bellekten yeniden oluşturmayın.

```markdown
## Data Points / Veri Noktaları

| Stat / İstatistik | Value / Değer | Source / Kaynak | Page/URL | Year | Notes |
|-------------------|---------------|-----------------|----------|------|-------|
| | | | | | |
```

---

## 5. Reading Pace for Reports / Raporlar için Okuma Temposu

**EN:** Reports are typically produced under time constraints. Apply these efficiency principles without compromising accuracy:
- Level 1 scan all sources before committing to Level 2 reading
- Level 2 read only sources that pass the Level 1 gate
- Prioritize sources tagged [POLICY] and [DATA] — these are highest-value for report writing
- Secondary sources (Tier 4) should rarely reach Level 2 — use them only to locate primary sources

**TR:** Raporlar genellikle zaman kısıtlamaları altında üretilir. Doğruluğu zedelemeden bu verimlilik ilkelerini uygulayın:
- Düzey 2 okumasına geçmeden önce tüm sourcesı Düzey 1 taramasından geçirin
- Yalnızca Düzey 1 geçidini geçen sourcesı Düzey 2'de okuyun
- [POLİTİKA] ve [VERİ] etiketli sourcesa öncelik verin — bunlar rapor yazımı için en yüksek değerli
- İkincil sources (Katman 4) nadiren Düzey 2'ye ulaşmalı — yalnızca birincil sourcesı bulmak için kullanın

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] All evidence_inventory.md sources scanned at Level 1 / Tüm sources Düzey 1'de tarandı
- [ ] Key sources read at Level 2 / Temel sources Düzey 2'de okundu
- [ ] All data points extracted with full source citations / Tüm veri noktaları tam kaynak atıflarıyla çıkarıldı
- [ ] [POLICY] tags applied where relevant / [POLİTİKA] etiketleri ilgili yerlere uygulandı
- [ ] Iron Rules: no unattributed claims / Demir Kurallar: atıfsız iddia yok
- [ ] exec_summary updated / exec_summary güncellendi

**Gate in:** phase-1-evidence.md
**Gate out:** → phase-3-analysis.md
