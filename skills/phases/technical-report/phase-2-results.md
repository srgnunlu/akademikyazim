---
title: "Phase 2 — Results & Discussion"
title_tr: "Faz 2 — Sonuçlar ve Tartışma"
node_type: phase
phase_number: 2
document_type: technical-report
phase_gate_in: "phase-1-methods.md"
phase_gate_out: null
description: "Present and interpret the experimental results. Distinguish results (what was observed) from discussion (what it means). Include visualizations."
description_tr: "Deneysel sonuçları sunar ve yorumlar. Sonuçları (gözlemlenen) tartışmadan (ne anlama geldiğinden) ayırt eder. Görselleştirmeler ekler."
tags: [phase, technical-report, results, discussion, visualization, reproducibility]
outputs:
  - "results_section.md"
  - "figures/"
  - "tables/"
links_to:
  - skills/core/iron-rules.md
  - skills/core/guided-writing-mode.md
  - skills/core/reviewer-mode.md
language: bilingual
version: "2.0"
---

# Phase 2 — Results & Discussion
# Faz 2 — Sonuçlar ve Tartışma

---

## Overview / Genel Bakış

**EN:**
This is the final phase of the technical report. You will present your experimental or analytical results, discuss their meaning in relation to your hypothesis, analyze errors and limitations, and ensure reproducibility. The Results section is factual (what happened); the Discussion section is interpretive (what it means). Never mix the two.

**TR:**
Bu, teknik raporun son aşamasıdır. Deneysel veya analitik sonuçlarınızı sunacak, bunların hipotezinizle ilişkisini tartışacak, hata ve sınırlılıkları analiz edecek ve tekrarlanabilirliği sağlayacaksınız. Sonuçlar bölümü olgusaldır (ne oldu); Tartışma bölümü yorumsaldır (ne anlama geliyor). İkisini asla karıştırmayın.

---

## 2.1 Results Presentation / Sonuçların Sunumu

### Tables / Tablolar

**EN:**
- Every table must have a descriptive caption above it (Table 1: ...)
- Include units in column headers
- Highlight key values (bold or shading) only if conventions in your field allow it
- Raw data goes in appendices; processed/summarized data goes in the main body
- Reference every table in the text before it appears ("As shown in Table 1, ...")

**TR:**
- Her tablonun üzerinde açıklayıcı bir başlık olmalıdır (Tablo 1: ...)
- Sütun başlıklarında birimleri belirtin
- Anahtar değerleri yalnızca alanınızdaki kurallar izin veriyorsa vurgulayın (kalın veya gölgeleme)
- Ham veriler eklere gider; işlenmiş/özetlenmiş veriler ana metne gider
- Her tabloya metinde görünmeden önce atıfta bulunun ("Tablo 1'de görüldüğü gibi, ...")

### Figures & Data Visualization / Şekiller ve Veri Görselleştirme

**EN:**
- Choose the right chart type: bar (comparison), line (trend), scatter (correlation), box (distribution)
- Every figure must have a descriptive caption below it (Figure 1: ...)
- Axes must be labeled with units
- Use consistent color schemes across all figures
- Error bars or confidence intervals must be included where applicable
- Avoid 3D charts unless the third dimension carries real information
- Save figures as vector formats (SVG, PDF) for print quality

**TR:**
- Doğru grafik türünü seçin: çubuk (karşılaştırma), çizgi (trend), dağılım (korelasyon), kutu (dağılım)
- Her şeklin altında açıklayıcı bir başlık olmalıdır (Şekil 1: ...)
- Eksenlerde birimlerle etiketleme yapılmalıdır
- Tüm şekillerde tutarlı renk şemaları kullanın
- Geçerli olduğu yerlerde hata çubukları veya güven aralıkları ekleyin
- Üçüncü boyut gerçek bilgi taşımıyorsa 3B grafiklerden kaçının
- Baskı kalitesi için şekilleri vektör formatlarında (SVG, PDF) kaydedin

### Writing the Results Section / Sonuçlar Bölümünü Yazmak

**EN:**
The Results section reports what you observed — nothing more. Structure options:

- **Chronological:** Present results in the order experiments were conducted
- **By hypothesis:** Group results by which hypothesis they test
- **By importance:** Lead with the most significant finding

For each result:
1. State the finding clearly in one sentence
2. Reference the supporting table or figure
3. Report statistical significance if applicable (p-values, confidence intervals)
4. Do NOT interpret — save that for Discussion

> **Guided Writing Mode:** TezAtlas generates A/B draft options for each results paragraph. The Academic Writing Note explains which presentation structure fits your data type and why. See `skills/core/guided-writing-mode.md`.

**TR:**
Sonuçlar bölümü gözlemlediğinizi raporlar — ne fazla ne eksik. Yapı seçenekleri:

- **Kronolojik:** Sonuçları deneylerin yapıldığı sırayla sunun
- **Hipoteze göre:** Sonuçları test ettikleri hipoteze göre gruplandırın
- **Öneme göre:** En önemli bulguyla başlayın

Her sonuç için:
1. Bulguyu tek cümlede net olarak belirtin
2. Destekleyici tablo veya şekle atıfta bulunun
3. Varsa istatistiksel anlamlılığı raporlayın (p-değerleri, güven aralıkları)
4. Yorumlamayın — bunu Tartışma'ya bırakın

> **Rehberli Yazım Modu:** TezAtlas her sonuç paragrafı için A/B taslak seçenekleri üretir. Akademik Yazım Notu hangi sunum yapısının veri türünüze uyduğunu ve nedenini açıklar. Bkz: `skills/core/guided-writing-mode.md`.

---

## 2.2 Discussion: Findings vs. Hypothesis / Tartışma: Bulgular ve Hipotez

**EN:**
The Discussion section interprets your results. Address these questions systematically:

1. **Confirmation or rejection?** Do the results support your original hypothesis from Phase 0? State this explicitly.
2. **Expected vs. unexpected:** Which results matched your predictions? Which surprised you? Unexpected results are often the most scientifically interesting — do not hide them.
3. **Comparison with prior work:** How do your results compare to published findings? Where do they agree? Where do they diverge? (Use sources from your `/sources` folder — Iron Rule 1)
4. **Causal explanations:** What mechanisms might explain your results? Be careful to distinguish correlation from causation.
5. **Practical implications:** What do these results mean for the field or application domain?

Structure recommendation:
```
For each major finding:
  → State the finding (reference Results section)
  → Interpret its meaning
  → Compare with existing literature
  → Explain discrepancies if any
  → State implications
```

**TR:**
Tartışma bölümü sonuçlarınızı yorumlar. Bu soruları sistematik olarak ele alın:

1. **Doğrulama mı ret mi?** Sonuçlar Faz 0'daki orijinal hipotezinizi destekliyor mu? Bunu açıkça belirtin.
2. **Beklenen ve beklenmeyen:** Hangi sonuçlar tahminlerinizle eşleşti? Hangileri sizi şaşırttı? Beklenmeyen sonuçlar genellikle bilimsel açıdan en ilginç olanlardır — gizlemeyin.
3. **Önceki çalışmalarla karşılaştırma:** Sonuçlarınız yayınlanmış bulgularla nasıl karşılaştırılıyor? Nerede uyuşuyorlar? Nerede ayrılıyorlar? (`/sources` klasöründeki kaynakları kullanın — Demir Kural 1)
4. **Nedensel açıklamalar:** Sonuçlarınızı hangi mekanizmalar açıklayabilir? Korelasyonu nedensellikten ayırmaya dikkat edin.
5. **Pratik çıkarımlar:** Bu sonuçlar alan veya uygulama alanı için ne anlama geliyor?

---

## 2.3 Error Analysis & Limitations / Hata Analizi ve Sınırlılıklar

**EN:**
Every technical report must honestly assess its own weaknesses. This is not optional — it demonstrates scientific maturity.

### Systematic Errors / Sistematik Hatalar
- Measurement instrument limitations
- Calibration issues
- Environmental factors not controlled
- Sample selection bias

### Random Errors / Rastgele Hatalar
- Statistical noise in measurements
- Variability between trials
- Quantify with standard deviation, standard error, or confidence intervals

### Limitations / Sınırlılıklar
Address each of the following:
- **Scope limitations:** What was deliberately excluded and why?
- **Methodological limitations:** What constraints did your method impose?
- **Data limitations:** Sample size, measurement precision, missing data
- **Generalizability:** Can results be extended beyond this specific experiment?
- **Time constraints:** What would you have done differently with more time?

> **Iron Rule 1 applies:** Every limitation claim should reference the relevant methodological literature from your sources. Do not make unsupported assertions about your own limitations.

**TR:**
Her teknik rapor kendi zayıflıklarını dürüstçe değerlendirmelidir. Bu isteğe bağlı değildir — bilimsel olgunluk gösterir.

Her birini ele alın:
- **Kapsam sınırlılıkları:** Kasıtlı olarak neyi dışladınız ve neden?
- **Yöntemsel sınırlılıklar:** Yönteminiz hangi kısıtlamaları dayattı?
- **Veri sınırlılıkları:** Örneklem büyüklüğü, ölçüm hassasiyeti, eksik veri
- **Genellenebilirlik:** Sonuçlar bu spesifik deneyin ötesine taşınabilir mi?
- **Zaman kısıtlamaları:** Daha fazla zamanınız olsaydı neyi farklı yapardınız?

---

## 2.4 Reproducibility Checklist / Tekrarlanabilirlik Kontrol Listesi

Before completing this phase, verify that another researcher could reproduce your work:

**EN:**

- [ ] All raw data is available (appendix or repository link)
- [ ] Software versions and dependencies are documented
- [ ] Hardware/equipment specifications are listed (from Phase 1)
- [ ] Step-by-step procedure is complete enough to follow without asking the author
- [ ] All parameters, settings, and configurations are recorded
- [ ] Statistical methods and significance thresholds are stated
- [ ] Code is version-controlled and accessible (if computational work)
- [ ] Figures can be regenerated from the provided data
- [ ] Negative results are included, not just positive ones
- [ ] Environmental conditions are documented (if applicable)

**TR:**

- [ ] Tüm ham veriler mevcut (ek veya depo bağlantısı)
- [ ] Yazılım sürümleri ve bağımlılıklar belgelendi
- [ ] Donanım/ekipman özellikleri listeli (Faz 1'den)
- [ ] Adım adım prosedür yazara sormadan takip edilecek kadar tam
- [ ] Tüm parametreler, ayarlar ve yapılandırmalar kayıtlı
- [ ] İstatistiksel yöntemler ve anlamlılık eşikleri belirtildi
- [ ] Kod sürüm kontrolünde ve erişilebilir (hesaplamalı çalışma ise)
- [ ] Şekiller sağlanan verilerden yeniden üretilebilir
- [ ] Negatif sonuçlar da dahil edildi, sadece pozitif olanlar değil
- [ ] Çevresel koşullar belgelendi (uygulanabilirse)

---

## 2.5 AI Reviewer Gate / AI Hakem Kapısı

**EN:**
Before marking this phase (and the technical report) as complete, an AI Peer Review session is mandatory. Claude will review your Results & Discussion as a Senior Peer Reviewer, checking:

1. **Data-claim alignment:** Does every claim in the Discussion have supporting data in Results?
2. **Interpretation restraint:** Are you over-interpreting or under-interpreting the data?
3. **Limitation honesty:** Are limitations comprehensive and honest, or superficial?
4. **Reproducibility:** Would another researcher be able to replicate this from what you wrote?
5. **Hypothesis verdict:** Is the hypothesis confirmation/rejection clearly stated?

Use `/ai-review` to trigger the review at any time, or it will run automatically at the phase gate.

**TR:**
Bu aşamayı (ve teknik raporu) tamamlanmış olarak işaretlemeden önce, bir AI Hakem İncelemesi oturumu zorunludur. Claude, Sonuçlar ve Tartışma bölümünüzü Kıdemli Hakem olarak inceleyecektir:

1. **Veri-iddia uyumu:** Tartışma'daki her iddianın Sonuçlar'da destekleyici verisi var mı?
2. **Yorum kısıtlaması:** Veriyi fazla mı yoksa az mı yorumluyorsunuz?
3. **Sınırlılık dürüstlüğü:** Sınırlılıklar kapsamlı ve dürüst mü, yoksa yüzeysel mi?
4. **Tekrarlanabilirlik:** Başka bir araştırmacı yazdıklarınızdan bunu tekrarlayabilir mi?
5. **Hipotez kararı:** Hipotezin doğrulanması/reddedilmesi açıkça belirtildi mi?

İncelemeyi istediğiniz zaman tetiklemek için `/ai-review` kullanın veya faz kapısında otomatik olarak çalışacaktır.

---

## Deliverables / Çıktılar

| Output | Description |
|--------|-------------|
| `results_section.md` | Complete Results & Discussion section |
| `figures/` | All figures in vector format with captions |
| `tables/` | All data tables |
| `appendix_raw_data.md` | Raw data appendix (or repository link) |

---

## Phase Transition / Faz Geçişi

This is the final phase of the Technical Report workflow. Upon passing the AI Reviewer Gate:

1. Run `/ai-review` for final comprehensive review
2. Run `/submission-check` if submitting to an institution
3. Compile final document with `/latex` or `/compile-pdf` if using LaTeX output format
4. Git commit (Iron Rule 6)

**Gate in:** phase-1-methods.md completed
**Gate out:** AI Peer Review passed + Reproducibility Checklist complete
