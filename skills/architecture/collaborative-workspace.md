---
title: "Collaborative Research Workspace"
title_tr: "İşbirlikçi Araştırma Çalışma Alanı"
node_type: architecture
priority: high
description: "Workflows for multi-author projects. Manages conflict resolution for shared source notes, authorship contribution logs (CRediT), and review assignment."
description_tr: "Çok yazarlı projeler için iş akışları. Paylaşılan kaynak notları, yazarlık katkı günlükleri (CRediT) ve inceleme ataması için çakışma çözümünü yönetir."
tags: [architecture, collaboration, co-authorship, multi-user, credit-taxonomy, conflict-resolution]
links_to:
  - skills/tooling/git-workflow.md
  - skills/architecture/feedback-integration-engine.md
language: bilingual
version: "1.0"
---

# Collaborative Research Workspace / İşbirlikçi Araştırma Çalışma Alanı

## Purpose / Amaç

**EN:** Modern academic outputs (especially in STEM and Medical sciences) are rarely solo endeavors. This node defines how TezAtlas handles multiple researchers working on the same project, ensuring intellectual conflicts are resolved systematically rather than lost in edit wars.
**TR:** Modern akademik çıktılar (özellikle STEM ve Tıp bilimlerinde) nadiren tek kişilik çabalardır. Bu node, TezAtlas'ın aynı proje üzerinde çalışan birden fazla araştırmacıyı nasıl ele aldığını tanımlayarak, entelektüel çakışmaların düzenleme savaşlarında kaybolmak yerine sistematik olarak çözülmesini sağlar.

---

## 1. Shared Source Note Conflict Resolution / Paylaşılan Kaynak Notu Çakışma Çözümü

**EN:** When two researchers read the same source and draw different conclusions in `_notlar.md`.
**Trigger:** Merging notes or updating the `reading_report.md` in Phase 3.
**AI Action:**
*   Detect contradictions: "Researcher A noted that Smith (2023) supports Hypothesis 1. Researcher B noted that Smith (2023) contradicts Hypothesis 1 due to the sample size limitation."
*   Prompt resolution: "Before we map this argument to the chapter outline, how do you want to integrate these opposing views of Smith (2023)? Should we dedicate a paragraph to this methodological disagreement?"

## 2. Authorship Contribution Log (CRediT Taxonomy) / Yazarlık Katkı Günlüğü

**EN:** To prevent disputes at submission time, contributions must be logged as they happen.
**Trigger:** Project start (Phase 0) and at every major Phase Gate.
**Protocol:** 
The AI maintains an `authorship_log.md` based on the CRediT (Contributor Roles Taxonomy).
*   **Roles:** Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Resources, Data Curation, Writing - Original Draft, Writing - Review & Editing, Visualization, Supervision, Project Administration, Funding Acquisition.
*   **AI Prompt (End of Phase 3):** "Phase 3 (Reading/Analysis) is complete. Who was responsible for 'Investigation' and 'Data Curation' in this phase? I will update the `authorship_log.md`."

## 3. Section Ownership and Review Assignment / Bölüm Sahipliği ve İnceleme Ataması

**EN:** In Phase 4 (Structure/Outline), the AI forces the assignment of *Authors* and *Reviewers* to every sub-section.
**AI Action:** 
Do not allow `chapter_outline.md` to be finalized unless every header has:
`[Author: Name] [Reviewer: Name]`

## 4. The "Co-Author Checkpoint" (Modifying Iron Rule 5)

**EN:** In a multi-author paper, Iron Rule 5 (Supervisor Checkpoints) is adapted. The gate out of Phase 5 (Drafting) and into Phase 6 (Revision) requires the assigned Reviewer (from Step 3) to formally approve the section. The AI uses the FIRE system (`feedback-integration-engine.md`) to process the co-author's review.