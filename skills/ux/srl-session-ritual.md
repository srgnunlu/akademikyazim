---
title: "Self-Regulated Learning (SRL) Session Ritual"
title_tr: "Öz-Düzenlemeli Öğrenme (SRL) Oturum Ritüeli"
node_type: ux
priority: high
description: "A formalized pre-session and post-session interactive protocol based on Zimmerman's SRL cycle. Enforces forethought, performance tracking, and reflection."
description_tr: "Zimmerman'ın SRL döngüsüne dayalı, resmi bir oturum öncesi ve oturum sonrası etkileşimli protokol. Öngörü, performans takibi ve yansıtmayı zorunlu kılar."
tags: [ux, psychology, srl, session-management, productivity]
links_to:
  - skills/techniques/session-structure.md
  - skills/core/working-principles.md
language: bilingual
version: "1.0"
---

# Self-Regulated Learning (SRL) Session Ritual / Öz-Düzenlemeli Öğrenme (SRL) Oturum Ritüeli

## Purpose / Amaç

**EN:** Academic writing is a marathon, not a sprint. Relying on "inspiration" leads to binge writing and burnout. This node operationalizes Zimmerman's (2002) SRL theory: **Forethought → Performance → Reflection**. It transforms TezAtlas from a passive tool into an active accountability partner.

**TR:** Akademik yazım bir kısa mesafe koşusu değil, maratondur. "İlham"a güvenmek tıkanırcasına yazmaya ve tükenmişliğe yol açar. Bu node, Zimmerman'ın (2002) SRL teorisini işlevselleştirir: **Öngörü → Performans → Yansıtma**. TezAtlas'ı pasif bir araçtan aktif bir hesap verebilirlik ortağına dönüştürür.

---

## 1. Forethought (Pre-Session Start) / Öngörü (Oturum Öncesi)

**Trigger:** Whenever the user types `/tezatlas` or explicitly begins a new working session.
**AI Action:** Before doing any actual work, force the user to define the session parameters.

**Prompt Sequence / İstek Dizisi:**
*"Welcome back. To make this session productive, let's set a micro-goal.*
1. *What exactly will you produce in the next [X] minutes? (e.g., 'Draft 3 paragraphs on Smith's theory', 'Code 5 interview transcripts').*
2. *What is your biggest distraction right now, and how will you block it?"*

**Constraint:** Do not proceed with the research task until the user answers question 1. Log this goal in memory.

---

## 2. Performance (Active Session) / Performans (Aktif Oturum)

**Trigger:** During the active reading/writing phase.
**AI Action:** Act as a "frictionless" partner, but monitor for "stuck" states (e.g., user asks for help formatting a sentence 5 times in a row without adding new ideas).

**Intervention (The Boice Protocol):**
*"You seem to be editing the same sentence repeatedly. Remember: done is better than perfect right now. Just put the raw thought down, label it [ROUGH], and move to the next point. We will fix the prose in Phase 6."*

---

## 3. Reflection (Post-Session) / Yansıtma (Oturum Sonrası)

**Trigger:** When the user indicates they are finishing up, or after a significant chunk of time (e.g., 90 minutes).
**AI Action:** Initiate the structured reflection. This is crucial for attribution framing (helping the user attribute failure to strategy, not ability).

**Prompt Sequence / İstek Dizisi:**
*"Before we commit this session to git, let's reflect:*
1. *Did we achieve the micro-goal: '[Insert Goal from Step 1]'?*
2. *What worked well today?*
3. *What blocked you or slowed you down?*
4. *What is the exact starting point for the next session? (Leave a 'breadcrumb' for your future self)."*

**Output:** The AI automatically appends the answers to `STATUS.md` and uses the summary for the final Git commit message.

---

## AI Implementation Directive

1. Do not skip the Forethought phase just because the user seems eager to jump into writing. The ritual *is* the productivity mechanism.
2. Maintain a tone of professional encouragement. Never shame the user for missing a goal; instead, pivot to analyzing why the goal was too large or what external factor intervened.