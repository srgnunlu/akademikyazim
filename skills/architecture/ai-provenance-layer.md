---
title: "AI Provenance & Reasoning Layer"
title_tr: "YZ Kaynak ve Gerekçelendirme Katmanı"
node_type: architecture
priority: critical
description: "The technical backbone for 'Draft Generator' mode. Tags every AI-generated sentence with its source file, the specific passage, and the reasoning connecting the source to the claim. Makes AI intellectual contribution legible and auditable."
description_tr: "'Taslak Oluşturucu' (Copilot) modunun teknik omurgası. Yapay zeka tarafından oluşturulan her cümleyi kaynak dosyası, belirli pasajı ve kaynağı iddiaya bağlayan akıl yürütmesi ile etiketler. YZ entelektüel katkısını okunaklı ve denetlenebilir hale getirir."
tags: [architecture, provenance, hallucination-prevention, audit, transparency]
links_to:
  - skills/core/iron-rules.md
  - skills/core/modes.md
language: bilingual
version: "1.0"
---

# AI Provenance & Reasoning Layer / YZ Kaynak ve Gerekçelendirme Katmanı

## Core Function / Temel İşlev

**EN:** The fundamental problem with AI-generated text in academia is untraceability. When an LLM produces a fluent paragraph summarizing three papers, the human author cannot easily verify if the AI hallucinated a connection or accurately represented the authors. The Provenance Layer solves this by making the AI "show its work" for every single claim it generates in Draft Generator mode.

**TR:** Akademide YZ tarafından üretilen metinlerin temel sorunu izlenebilirliğin olmamasıdır. Bir LLM üç makaleyi özetleyen akıcı bir paragraf ürettiğinde, yazar, yapay zekanın bir bağlantı uydurup uydurmadığını veya yazarları doğru temsil edip etmediğini kolayca doğrulayamaz. Kaynak Katmanı, Taslak Oluşturucu modunda ürettiği her iddia için YZ'nin "işlemlerini göstermesini" sağlayarak bunu çözer.

---

## The Provenance Tag Structure / Kaynak Etiketi Yapısı

When operating in **Draft Generator** mode, the AI must NOT output standard markdown paragraphs. It must wrap every substantive claim in a custom HTML/Markdown hybrid tag that contains the meta-data of its reasoning.

### Example AI Output Format:

```markdown
<ai_claim>
  <text>Smith (2022) demonstrated that continuous deployment increases system fragility by 14% in legacy architectures.</text>
  <provenance>
    <source>sources/smith_2022_deployment.pdf</source>
    <location>Page 4, Table 2</location>
    <original_quote>"In our sample of 50 legacy monolithic systems, the shift to continuous deployment correlated with a 14.2% increase in critical incident tickets."</original_quote>
    <reasoning>Summarized the specific finding regarding legacy systems to support the user's argument about deployment frequency.</reasoning>
    <confidence>High - direct data extraction</confidence>
  </provenance>
</ai_claim>
```

---

## Hallucination Risk Scoring / Halüsinasyon Risk Puanlaması

The AI must self-evaluate the risk of its own generation. 

*   **🟢 Low Risk:** The text is a direct paraphrase or data extraction from a single, explicitly provided source file. (e.g., "The sample size was 400").
*   **🟡 Medium Risk:** The text synthesizes two or more provided sources, drawing a connection that the original authors did not explicitly make themselves. (e.g., "While Jones argues X, this seems to contradict Smith's finding of Y").
*   **🔴 High Risk:** The text relies on the AI's internal pre-training data rather than a file in the `/sources/` folder. **(Note: Under Iron Rule 1 and 4, High Risk outputs are strictly forbidden. The AI must refuse to generate the text instead).**

---

## The Audit Protocol (User Interaction) / Denetim Protokolü (Kullanıcı Etkileşimi)

**EN:** When the AI delivers a drafted section to the user, it presents the text normally but with visual markers (e.g., footnotes or blockquotes). The user is required to run the "Audit Check" before accepting the text.

**TR:** YZ taslak halindeki bir bölümü kullanıcıya sunduğunda, metni normal bir şekilde ancak görsel işaretlerle (örn. dipnotlar veya alıntılar) sunar. Kullanıcının metni kabul etmeden önce "Denetim Kontrolü"nü çalıştırması gerekir.

**Process:**
1. AI generates draft with embedded `<ai_claim>` tags.
2. AI prompts: *"I have drafted this section based on your notes. Please review the provenance data. Type 'audit [paragraph number]' to see exactly where I got these claims."*
3. The user must review the original quotes to ensure the AI did not twist the context of the source.
4. Only after the user confirms (e.g., by typing `accept draft`) does the AI strip the `<provenance>` tags and format it as clean academic text.

---

## AI Implementation Directive

1. If the `modes.md` file indicates the user is in **Draft Generator** mode, the Provenance Layer is MANDATORY.
2. You cannot output substantive claims (arguments, data, definitions) without identifying exactly which file in the `/sources/` directory it came from.
3. If you cannot find a source in the directory to support a sentence you want to write, you must output a `[SOURCE NEEDED - Could not verify locally]` placeholder instead of generating the sentence.
