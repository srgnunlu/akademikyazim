---
title: "Adaptive Output Transformer"
title_tr: "Uyarlanabilir Çıktı Dönüştürücü"
node_type: architecture
priority: high
description: "Generates derivative outputs (policy briefs, blog posts, press releases) from a finalized core project without fabricating new claims."
description_tr: "Tamamlanmış bir çekirdek projeden yeni iddialar uydurmadan türev çıktılar (politika özetleri, blog yazıları, basın bültenleri) üretir."
tags: [architecture, transformation, dissemination, derivative-output, impact]
links_to:
  - skills/phases/report/phase-5-dissemination.md
  - skills/architecture/ai-provenance-layer.md
language: bilingual
version: "1.0"
---

# Adaptive Output Transformer / Uyarlanabilir Çıktı Dönüştürücü

## Purpose / Amaç

**EN:** A published paper is the beginning of impact, not the end. The Adaptive Output Transformer takes a finalized Phase 7 academic document (thesis or article) and restructures it for different audiences. It strictly enforces the rule: *transform, do not invent*.
**TR:** Yayınlanmış bir makale etkinin sonu değil, başlangıcıdır. Uyarlanabilir Çıktı Dönüştürücü, tamamlanmış bir Faz 7 akademik belgesini (tez veya makale) alır ve farklı hedef kitleler için yeniden yapılandırır. Şu kuralı kesinlikle uygular: *dönüştür, icat etme*.

---

## Output Profiles / Çıktı Profilleri

When the user requests a transformation, the AI applies one of the following structural profiles:

### 1. The Policy Brief (For Government/NGOs)
*   **Length:** 1-2 pages.
*   **Structure:** Executive Summary → The Problem → Findings (Bullet points) → Policy Recommendations.
*   **Transformation Rule:** Strip all methodological jargon. Elevate the "practical implications" from the conclusion to the top of the document.

### 2. The Press Release (For Journalists)
*   **Length:** 500-800 words.
*   **Structure:** Catchy Headline → The "Hook" (Why this matters right now) → The Core Finding (The "What") → Quotes (Generated from the author's conclusions) → About the Research (The "How").
*   **Transformation Rule:** Assume a 10th-grade reading level. Translate statistical significance into real-world impact metrics (e.g., "instead of 'p<0.05', say 'a clear, measurable decrease'").

### 3. The Academic Twitter/X Thread
*   **Length:** 5-8 tweets.
*   **Structure:** 1/ The Hook (Question/Gap) → 2/ The Core Finding (Image/Chart) → 3/ Methodology (Brief) → 4/ Surprising Detail → 5/ Conclusion/Implications → 6/ Link to paper.
*   **Transformation Rule:** Keep sentences short. Suggest placeholders for visual assets (e.g., `[Insert Figure 2 here]`).

### 4. The Conference Presentation Deck Outline
*   **Structure:** Standard 15-minute academic presentation flow. Title → Background → Gap → Methods → Results (Visual) → Contribution.

---

## The "No Fabrication" Constraint / İcat Etmeme Kısıtı

**EN:** The Transformer is prone to hallucinating "catchy" implications that the original paper did not actually claim. 
**AI Action:** Every time the AI generates a derivative output, it MUST run an internal consistency check against the original text. If the Press Release claims the research will "revolutionize the industry", but the paper's conclusion says "offers a modest improvement", the AI must downgrade the PR language to match the paper's exact scope.

*Prompting Rule:* "I have generated the Policy Brief based on your paper. Please note I translated your finding about 'reduced cognitive load' into a recommendation for 'shorter working hours.' Please verify this logical leap."