---
title: "Phase 3 — Analysis & Recommendations"
title_tr: "Aşama 3 — Analiz ve Öneriler"
node_type: phase
phase_number: 3
document_type: report
phase_gate_in: "phase-2-reading.md"
phase_gate_out: "phase-4-writing.md"
description: "Synthesize evidence into key findings. Develop recommendations that are specific, actionable, and each linked to at least one evidence source. Include risk and limitation assessment for each recommendation."
description_tr: "Kanıtları temel bulgulara dönüştürün. Özgül, uygulanabilir ve her biri en az bir kanıt kaynağına bağlı öneriler geliştirin. Her öneri için risk ve sınırlılık değerlendirmesi ekleyin."
tags: [phase, report, analysis, recommendations, evidence-linked, risk]
outputs:
  - "findings_and_recommendations.md"
links_to:
  - skills/core/iron-rules.md
  - skills/phases/report/phase-2-reading.md
language: bilingual
version: "1.0"
---

# Phase 3 — Analysis & Recommendations
# Aşama 3 — Analiz ve Öneriler

## Gate Rule / Geçiş Kuralı

**EN:** Every recommendation must be traceable to at least one piece of evidence from the evidence inventory. Recommendations not grounded in evidence are opinions; label them as such or remove them.

**TR:** Her öneri, kanıt envanterinden en az bir kanıt parçasına izlenebilir olmalıdır. Kanıta dayanmayan öneriler görüştür; ya bu şekilde etiketleyin ya da kaldırın.

---

## 1. Synthesizing Key Findings / Temel Bulguları Sentezleme

**EN:** Group the annotated evidence from Phase 2 into findings. A finding is a factual statement about the current situation, supported by evidence. Findings are not recommendations — they describe what IS, not what SHOULD BE.

**TR:** Aşama 2'deki açıklamalı kanıtları bulgulara gruplandırın. Bulgu, kanıtla desteklenen mevcut duruma ilişkin olgusal bir ifadedir. Bulgular öneri değildir — OLMASI GEREKEN'i değil, OLAN'ı tanımlar.

```markdown
## Key Findings / Temel Bulgular

### Finding 1 / Bulgu 1
**Statement / İfade:** [factual statement / olgusal ifade]
**Evidence / Kanıt:** E01, E04, E07 (from evidence_inventory.md)
**Evidence strength / Kanıt gücü:** [strong/moderate/limited/contested]

### Finding 2 / Bulgu 2
...
```

---

## 2. From Findings to Recommendations / Bulgulardan Önerilere

**EN:** Each recommendation is a response to one or more findings. Map the relationship explicitly. A report with recommendations that do not connect to findings has a logic gap that reviewers will identify.

**TR:** Her öneri, bir veya daha fazla bulguya verilen bir yanıttır. İlişkiyi açıkça eşleştirin. Bulgularla bağlantılı olmayan önerilere sahip bir raporun, gözlemcilerin belirleyeceği bir mantık boşluğu vardır.

```
Finding → Recommendation mapping / Bulgu → Öneri eşleştirmesi:
F1 → R1, R2
F2 → R2, R3
F3 → R4
```

---

## 3. Recommendation Quality Criteria / Öneri Kalite Kriterleri

**EN:** Each recommendation must pass all four tests before inclusion:

**TR:** Her öneri dahil edilmeden önce dört testi geçmelidir:

1. **Specific / Özgül** — Names who does what, not "stakeholders should consider"
2. **Actionable / Uygulanabilir** — The named actor has the authority and capacity to act
3. **Evidence-linked / Kanıta bağlı** — Traceable to at least one evidence source
4. **Time-bounded / Zaman sınırlı** — Short/medium/long term specified

```markdown
## Recommendations / Öneriler

### Recommendation 1 / Öneri 1
**Text / Metin:** [specific action statement]
**Actor / Aktör:** [who implements / kim uygular]
**Timeline / Zaman çizelgesi:** [short / medium / long term]
**Evidence base / Kanıt temeli:** E___, Finding F___
**Prerequisites / Ön koşullar:**

### Recommendation 2 / Öneri 2
...
```

---

## 4. Risk & Limitations / Risk ve Sınırlılıklar

**EN:** For each recommendation, assess:
- Implementation risks (political, financial, technical, capacity)
- Evidence quality — how confident are we in the evidence base?
- What happens if this recommendation is not followed?

**TR:** Her öneri için değerlendirin:
- Uygulama riskleri (siyasi, mali, teknik, kapasite)
- Kanıt kalitesi — kanıt tabanına ne kadar güveniyoruz?
- Bu öneri takip edilmezse ne olur?

```markdown
## Risk Register / Risk Kaydı

| Recommendation | Risk | Likelihood | Impact | Mitigation |
|---------------|------|-----------|--------|------------|
| R1 | | H/M/L | H/M/L | |
| R2 | | | | |
```

---

## 5. Update Executive Summary / Yönetici Özetini Güncelleme

**EN:** Update exec_summary with actual findings and recommendations. At this point the document should be nearly final — the findings are known, the recommendations are formed.

**TR:** exec_summary'yi gerçek bulgular ve önerilerle güncelleyin. Bu noktada belge neredeyse nihai olmalıdır — bulgular biliniyor, öneriler oluşturulmuştur.

---

## Completion Checklist / Tamamlama Kontrol Listesi

- [ ] Key findings written as factual, evidence-supported statements / Temel bulgular olgusal, kanıt destekli ifadeler olarak yazıldı
- [ ] Every recommendation is specific, actionable, evidence-linked, time-bounded / Her öneri özgül, uygulanabilir, kanıta bağlı, zaman sınırlı
- [ ] Finding-to-recommendation mapping documented / Bulgu-öneri eşleştirmesi belgelendi
- [ ] Risk register completed / Risk kaydı tamamlandı
- [ ] findings_and_recommendations.md finalized / findings_and_recommendations.md kesinleştirildi
- [ ] exec_summary updated to reflect actual findings / exec_summary gerçek bulgularla güncellendi

**Gate in:** phase-2-reading.md
**Gate out:** → phase-4-writing.md
