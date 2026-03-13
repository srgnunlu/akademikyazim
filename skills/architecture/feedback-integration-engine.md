---
title: "Feedback Integration & Response Engine (FIRE)"
title_tr: "Geri Bildirim Entegrasyon ve Yanıt Motoru (FIRE)"
node_type: architecture
priority: high
description: "Universal feedback ingestor. Parses reviewer comments, supervisor notes, and auto-drafts a point-by-point response document linked directly to manuscript changes."
description_tr: "Evrensel geri bildirim alıcısı. Hakem yorumlarını, danışman notlarını ayrıştırır ve makale değişiklikleriyle doğrudan bağlantılı madde madde bir yanıt belgesi taslağı oluşturur."
tags: [architecture, feedback, peer-review, response, revision]
links_to:
  - skills/phases/article/phase-6-revision-cycle.md
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Feedback Integration & Response Engine (FIRE) / Geri Bildirim Entegrasyon ve Yanıt Motoru (FIRE)

## Core Function / Temel İşlev

**EN:** Academic revision is often chaotic. Authors receive a PDF with 40 comments, an email with 3 bullet points, and a docx with track changes. FIRE acts as an ingestor and structured response generator. It takes unstructured feedback, categorizes it, forces the author to address each point, and outputs a professional "Response to Reviewers" document.

**TR:** Akademik revizyon genellikle kaotiktir. Yazarlar 40 yorum içeren bir PDF, 3 madde içeren bir e-posta ve değişiklikleri izle (track changes) içeren bir docx alırlar. FIRE bir alıcı ve yapılandırılmış yanıt oluşturucu olarak işlev görür. Yapılandırılmamış geri bildirimi alır, kategorize eder, yazarı her noktayı ele almaya zorlar ve profesyonel bir "Hakemlere Yanıt" belgesi üretir.

---

## The FIRE Workflow / FIRE İş Akışı

### Step 1: Ingestion & Parsing / Alım ve Ayrıştırma
**User Action:** Uploads reviewer reports (PDF/Text) or supervisor emails.
**AI Action:** Extracts every distinct piece of feedback and assigns it a unique ID (e.g., `[Rev1-Point1]`, `[Sup-Point3]`).

### Step 2: Semantic Categorization / Semantik Kategorizasyon
**AI Action:** Sorts the parsed feedback into categories to help the author prioritize:
- 🔴 **Fatal/Structural:** Demands for new data, new experiments, or major methodological shifts.
- 🟡 **Substantive:** Requests for clearer definitions, additional literature, or toning down claims.
- 🟢 **Cosmetic/Line-Edits:** Typos, formatting, minor rephrasing.

### Step 3: The Response Matrix (Interactive) / Yanıt Matrisi (Etkileşimli)
**AI Action:** Presents the user with one piece of feedback at a time, starting with the 🔴 Structural issues.
**Prompt to User:** 
*"Reviewer 1 says: 'The sample size is too small to justify the conclusion in paragraph 4.'*
*How do you want to handle this?*
*A) Agree and change the text (I will help you draft the change).*
*B) Agree but explain why it can't be changed (I will help you draft the limitation).*
*C) Disagree and rebut (Provide your evidence, and I will draft the polite rebuttal)."*

### Step 4: Auto-Drafting the Response Document / Yanıt Belgesinin Otomatik Oluşturulması
**AI Action:** Once all points are addressed, FIRE compiles `Response_to_Reviewers.md`.
**Format:**
> **Reviewer 1, Comment 1:** [Text of the comment]
> **Our Response:** [Polite agreement/disagreement based on user input]
> **Action Taken:** "We have updated Section 3, Paragraph 2 to reflect this: *'[New quoted text here]'*"

---

## Dealing with Conflicting Feedback / Çelişen Geri Bildirimlerle Başa Çıkma

**EN:** A common academic nightmare: Reviewer 1 says "expand this section", Reviewer 2 says "cut this section". FIRE automatically detects direct contradictions in the ingested feedback and highlights them in a "Conflict Resolution Protocol".
**TR:** Yaygın bir akademik kabus: 1. Hakem "bu bölümü genişlet" der, 2. Hakem "bu bölümü kes" der. FIRE, alınan geri bildirimlerdeki doğrudan çelişkileri otomatik olarak algılar ve bunları bir "Çatışma Çözüm Protokolü"nde vurgular.

**FIRE Prompt:** *"Reviewer 1 and Reviewer 2 have given conflicting advice on Section 4. The standard academic strategy is to choose the reviewer whose advice aligns best with the Editor's tone, or to find a middle ground. Which path shall we take?"*

---

## AI Implementation Directive

When FIRE is activated (typically in Phase 6 of Article/Thesis):
1. Expect unstructured text input containing feedback.
2. Do NOT immediately rewrite the user's manuscript. The primary output is the `Response_to_Reviewers.md` document.
3. Ensure the tone of the response document is unfailingly polite, objective, and deferential, even if the user's input is frustrated. Translate "This reviewer didn't read the paper" into "We respectfully direct the reviewer's attention to page 4, where..."
