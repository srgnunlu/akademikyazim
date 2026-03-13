---
title: "Phase 6 — Peer Review Response Cycle"
title_tr: "Faz 6 — Hakem Değerlendirme Yanıt Döngüsü"
node_type: phase
phase_number: 6
document_type: article
phase_gate_in: "phase-5-revision.md"
phase_gate_out: "PUBLISHED"
description: "Managing the peer review response loop: parsing reviewer comments, categorizing responses (accept/revise/reject), writing point-by-point responses, and tracking revision cycles until acceptance."
description_tr: "Hakem yorumlarını ayrıştırma, yanıt kategorilendirme, nokta-nokta yanıt yazma ve kabul aşamasına kadar revizyon döngüsünü yönetme."
tags: [phase, article, peer-review, revision-cycle, publication]
outputs:
  - "reviewer_response.md (point-by-point)"
  - "manuscript_revised_v2.md, v3.md ..."
  - "cover_letter_revision.md"
links_to:
  - skills/core/iron-rules.md
  - skills/core/academic-integrity.md
language: bilingual
version: "1.0"
---

# Phase 6 — Peer Review Response Cycle

## Phase Gate
**Enter:** Manuscript submitted (Phase 5 complete)
**Exit:** Acceptance letter received OR decision to abandon journal and resubmit elsewhere

---

## Step 1: Triage Reviewer Comments / Hakem Yorum Triajı

When decision arrives (Accept / Minor Revision / Major Revision / Reject):

**Accept / Minor Revision:** Proceed to Step 2.

**Major Revision:**
- Build a response matrix: reviewer comment → your response → manuscript change
- Estimate revision time realistically
- If >6 months revision needed → consider whether journal is right fit

**Reject with comments:**
- Extract useful methodological feedback
- Identify target journal for resubmission
- Apply feedback before resubmitting (do not send unchanged manuscript elsewhere)

**Reject without review (desk rejection):**
- Check: was the scope fit correct?
- Revise journal targeting → go back to Phase 5 submission checklist

---

## Step 2: Point-by-Point Response Document / Nokta-Nokta Yanıt

Format:
```
Reviewer 1, Comment 3:
> [Reviewer's exact words]

Response: [Your response — thank, acknowledge or politely disagree]
Manuscript change: [Page X, paragraph Y — what changed]
```

Rules:
- Never dismiss a reviewer comment without explanation
- If you disagree: explain with evidence, not emotion
- Every "we have revised" claim must be verifiable in the manuscript

---

## Step 3: Revision Tracking / Revizyon Takibi

- Track revision versions: `manuscript_v2.md`, `manuscript_v3.md`
- Git commit after each revision cycle
- Keep `reviewer_response.md` updated across cycles

---

## Step 4: Resubmission / Yeniden Gönderim

Checklist:
- [ ] Point-by-point response document complete
- [ ] All manuscript changes tracked (git diff or change tracking)
- [ ] Cover letter updated (mention "revised manuscript in response to reviewer comments")
- [ ] Word count still within journal limits
- [ ] All new citations added since Phase 5 are in /sources/ folder (Iron Rule 1)

---

## Completion Criteria / Tamamlanma Kriterleri

✅ **Acceptance received** — proceed to production/copyediting
✅ **Or: strategic rejection** — resubmit to new journal (restart Phase 5 with new target)
