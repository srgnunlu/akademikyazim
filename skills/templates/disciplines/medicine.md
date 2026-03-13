---
title: "Medicine & Health Sciences Module"
title_tr: "Tıp ve Sağlık Bilimleri Modülü"
node_type: template
priority: high
description: "Discipline-specific rules for Medicine. Enforces EQUATOR guidelines (CONSORT, PRISMA, STROBE), IRB/Ethics approval checks, and Vancouver citation format."
description_tr: "Tıp için disipline özgü kurallar. EQUATOR yönergelerini (CONSORT, PRISMA, STROBE), Etik Kurul onayı kontrollerini ve Vancouver atıf formatını zorunlu kılar."
tags: [discipline, medicine, health, rct, consort, prisma, ethics]
links_to:
  - skills/core/iron-rules.md
  - skills/core/research-ethics.md
language: bilingual
version: "1.0"
---

# Medicine & Health Sciences Module / Tıp ve Sağlık Bilimleri Modülü

## Purpose / Amaç

**EN:** Health sciences require strict adherence to international reporting guidelines to ensure reproducibility, patient safety, and transparency. This module overrides general defaults to enforce medical standards.
**TR:** Sağlık bilimleri, tekrarlanabilirlik, hasta güvenliği ve şeffaflığı sağlamak için uluslararası raporlama yönergelerine sıkı sıkıya bağlı kalmayı gerektirir. Bu modül, tıbbi standartları uygulamak için genel varsayılanları geçersiz kılar.

---

## 1. Citation Standard: Vancouver / Atıf Standardı: Vancouver

Unless explicitly instructed otherwise by a target journal, default to Vancouver style.
*   **In-text:** Numbered in parentheses (1) or superscript^1^ in order of appearance.
*   **Bibliography:** 
    *   *Article:* Author AA, Author BB, Author CC. Title of article. Abbreviated Journal Title. Year;Volume(Issue):Pages.
    *   List up to 6 authors, then add "et al."

## 2. The EQUATOR Network Enforcement / EQUATOR Ağı Uygulaması

Before Phase 4 (Writing) begins, the AI MUST ask the user to declare the study design and enforce the corresponding checklist:
*   **Randomized Controlled Trial (RCT):** Enforce **CONSORT** checklist. Require Trial Registration Number (e.g., ClinicalTrials.gov) in Phase 1.
*   **Systematic Review / Meta-Analysis:** Enforce **PRISMA** checklist. Require PROSPERO registration number.
*   **Observational Study (Cohort, Case-Control):** Enforce **STROBE** checklist.
*   **Case Report:** Enforce **CARE** checklist.

*AI Action:* Do not allow the user to output the final draft without verifying that all required items from the relevant checklist are present in the text.

## 3. Ethics & Data Privacy (IRB/KVKK/GDPR) / Etik ve Veri Gizliliği

In Phase 1 (Methodology/Sources), force the following declarations:
1.  **Ethics Approval:** "This study was approved by the Institutional Review Board of [Institution] (Approval No: [XXX])." If not approved, why?
2.  **Informed Consent:** "Informed consent was obtained from all individual participants included in the study."
3.  **Data De-identification:** How was patient data anonymized? (No names, MRNs, exact dates of birth in the text).

## 4. Hierarchy of Evidence / Kanıt Hiyerarşisi

When the *Proactive Methodological Guardian* assesses the strength of a claim, it must use the medical hierarchy of evidence:
1.  Systematic Reviews / Meta-analyses of RCTs
2.  Randomized Controlled Trials (RCTs)
3.  Cohort Studies
4.  Case-Control Studies
5.  Cross-Sectional Studies
6.  Case Series / Case Reports
7.  Expert Opinion / Mechanistic Reasoning

*AI Prompting Rule:* If a user uses a cross-sectional study (Level 5) to claim a treatment "cures" a disease (requires Level 1/2), the AI MUST intervene and force the user to downgrade the verb to "is associated with" or "may improve".