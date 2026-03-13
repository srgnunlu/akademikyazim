---
title: "Citation Formats & Rules"
title_tr: "Atıf Formatları ve Kuralları"
node_type: tooling
priority: high
description: "Centralized reference for academic citation styles (APA 7, Chicago 17, MLA 9, IEEE, Bluebook). Guides the AI on how to format bibliographies and in-text citations correctly."
description_tr: "Akademik atıf stilleri (APA 7, Chicago 17, MLA 9, IEEE, Bluebook) için merkezi referans. YZ'yi kaynakçaları ve metin içi atıfları nasıl doğru şekilde biçimlendireceği konusunda yönlendirir."
tags: [tooling, citation, reference, formatting, bibliography]
links_to:
  - skills/core/iron-rules.md
  - skills/moc/MOC-citations.md
language: bilingual
version: "1.0"
---

# Citation Formats & Rules / Atıf Formatları ve Kuralları

## Purpose / Amaç

**EN:** Different disciplines require fundamentally different citation structures. This node ensures TezAtlas applies the correct stylistic rules automatically, preventing the researcher from wasting hours formatting commas and italics.

**TR:** Farklı disiplinler temelde farklı atıf yapıları gerektirir. Bu node, TezAtlas'ın doğru biçimsel kuralları otomatik olarak uygulamasını sağlayarak, araştırmacının virgülleri ve italikleri biçimlendirmek için saatler harcamasını önler.

---

## 1. APA 7th Edition (Social Sciences, Education, Psychology)

**Core Logic:** Author-Date. Emphasizes the recency of the research.
**In-text:** (Smith, 2023, p. 14) or (Smith & Jones, 2023) or (Smith et al., 2023) for 3+ authors.
**Bibliography:**
*   *Book:* Author, A. A. (Year). *Title of book* (Edition). Publisher.
*   *Article:* Author, A. A., & Author, B. B. (Year). Title of article. *Title of Periodical, volume number*(issue number), pages. DOI

---

## 2. Chicago 17th Edition (Notes and Bibliography) (Humanities, History)

**Core Logic:** Footnotes/Endnotes. Allows for discursive notes alongside citations.
**In-text:** Superscript number.^1
**Footnote:** 1. Firstname Lastname, *Title of Book* (Place of Publication: Publisher, Year), page.
**Bibliography:** (Note the reversed name order and different punctuation)
*   *Book:* Lastname, Firstname. *Title of Book*. Place of Publication: Publisher, Year.

---

## 3. MLA 9th Edition (Literature, Cultural Studies)

**Core Logic:** Author-Page. Emphasizes the specific location of the text being analyzed, often without a date in the text itself.
**In-text:** (Smith 14) or (Smith and Jones 14-15).
**Bibliography (Works Cited):**
*   *Book:* Lastname, Firstname. *Title of Book*. Publisher, Year.
*   *Article:* Lastname, Firstname. "Title of Article." *Title of Journal*, vol. X, no. Y, Year, pp. ZZ-AA.

---

## 4. IEEE (Engineering, Computer Science)

**Core Logic:** Numbered. Emphasizes brevity and sequential flow.
**In-text:** [1] or [1, p. 14]. Numbers are assigned in the order sources are first cited.
**Bibliography:** (Numbered list)
*   [1] A. A. Author, *Title of Book*. Location: Publisher, Year.
*   [2] A. A. Author, "Title of article," *Abbrev. Title of Journal*, vol. x, no. x, pp. xxx-xxx, Abbrev. Month, Year.

---

## 5. Bluebook (US Law) / OSCOLA (UK Law) / Hukuk (TR)

**Core Logic:** Deeply specialized rules prioritizing the hierarchy of legal authority (Statutes > Cases > Secondary Sources).
*For detailed legal citation rules, including Turkish legal conventions (Yargıtay/AYM), the AI MUST load the specific discipline module:* `skills/templates/disciplines/hukuk.md`.

---

## AI Implementation Directive

1. In Phase 0 of any document type, ask the user: *"Which citation style are we using for this project (e.g., APA, Chicago, IEEE)?"* and save this to `STATUS.md`.
2. When generating text in Phase 5 or Phase 6, strictly adhere to the chosen format's in-text citation rules.
3. During Phase 7 (Finalization), use this node to audit and format the entire bibliography, ensuring perfect compliance with the selected style.