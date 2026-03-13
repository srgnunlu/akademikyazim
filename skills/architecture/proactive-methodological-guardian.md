---
title: "Proactive Methodological Guardian"
title_tr: "Proaktif Metodolojik Gardiyan"
node_type: architecture
priority: critical
description: "Always-on monitoring that detects methodological flaws in real-time and suggests candidate sources for unsourced claims. Acts as an active background checker."
description_tr: "Metodolojik kusurları gerçek zamanlı olarak tespit eden ve kaynaksız iddialar için aday kaynaklar öneren, her zaman açık izleme sistemi. Aktif bir arka plan denetleyicisi olarak hareket eder."
tags: [architecture, background-monitoring, real-time, flaw-detection, guardian]
links_to:
  - skills/architecture/methodological-oracle.md
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Proactive Methodological Guardian / Proaktif Metodolojik Gardiyan

## Core Function / Temel İşlev

**EN:** Unlike phase gates which are explicit checkpoints, the Proactive Methodological Guardian (PMG) runs constantly in the background during active writing or drafting phases (e.g., Phase 5, Phase 6). It watches the text stream for logical leaps, unsourced absolute claims, and methodological contradictions *as they are being written*.

**TR:** Açık kontrol noktaları olan faz kapılarının aksine, Proaktif Metodolojik Gardiyan (PMG), aktif yazma veya taslak oluşturma aşamalarında (örn. Faz 5, Faz 6) arka planda sürekli olarak çalışır. Metin akışını, mantıksal sıçramalar, kaynaksız kesin iddialar ve metodolojik çelişkiler açısından *yazıldıkları anda* izler.

---

## The 3 Guardian Triggers / Gardiyan Tetikleyicileri

### 1. The Over-Claim Detector (Hedging Failure) / Aşırı İddia Dedektörü
**Trigger:** Detection of absolute words ("proves", "definitively shows", "always", "never", "clearly") connected to empirical results.
**Action:** Immediate inline intervention.
**Prompt:** *"You used the word 'proves'. In empirical research, a single study rarely 'proves' anything; it 'suggests', 'indicates', or 'provides evidence for'. Do you want to soften this claim to match the strength of your data?"*

### 2. The Silent Variable Monitor / Sessiz Değişken İzleyici
**Trigger:** The text draws a conclusion linking Variable A to Variable B, but ignores Variable C which was discussed earlier in the literature review or methods.
**Action:** Flag the missing context.
**Prompt:** *"You are attributing the change in Y entirely to X here, but in your methods section you noted that Z was also a factor. Have you controlled for Z in this specific conclusion?"*

### 3. The Proactive Iron Rule 1 Enforcer / Proaktif Demir Kural 1 Uygulayıcısı
**Trigger:** A sentence makes a factual, historical, or statistical claim that lacks a citation, AND the claim is not common knowledge.
**Action:** Do not just say "add citation". Look at the `evidence_inventory.md` or `/sources/` folder and suggest a match.
**Prompt:** *"This sentence reads like a claim that requires a source. Based on your /sources/ folder, [Author, Year] discusses this topic on page [X]. Is this the source you meant to use here? If not, please find the correct source before moving on."*

---

## Architectural Difference from Phase Gates / Faz Kapılarından Mimari Farkı

**EN:** Phase gates are blocking functions ("You cannot move to Phase 4 until X is done"). The Guardian is an assistive friction function. It creates small, immediate moments of friction during drafting to prevent massive structural failures later during peer review or defense. 

**TR:** Faz kapıları engelleyici işlevlerdir ("X yapılana kadar Faz 4'e geçemezsiniz"). Gardiyan ise yardımcı bir sürtünme işlevidir. Yazım sırasında küçük, anlık sürtünme anları yaratarak, hakem değerlendirmesi veya savunma sırasında daha sonra ortaya çıkabilecek devasa yapısal hataları önler.

---

## AI Implementation Directive

When this node is active during writing phases, the AI must:
1. Actively scan the user's input stream for the 3 triggers.
2. If a trigger is hit, pause the writing flow and ask the user to resolve the specific guardian prompt before continuing to the next paragraph.
3. Maintain a "soft" tone. The Guardian is a safety net, not a punishing evaluator.
