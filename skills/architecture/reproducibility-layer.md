---
title: "Reproducibility & Data Provenance Layer"
title_tr: "Tekrarlanabilirlik ve Veri Kaynağı Katmanı"
node_type: architecture
priority: high
description: "Documents every methodological decision, software version, and data cleaning step to automatically generate a methods appendix and a replication package."
description_tr: "Otomatik olarak bir yöntemler eki ve bir replikasyon paketi oluşturmak için her metodolojik kararı, yazılım sürümünü ve veri temizleme adımını belgeler."
tags: [architecture, reproducibility, open-science, fair-principles, data-management]
links_to:
  - skills/templates/disciplines/stem.md
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# Reproducibility & Data Provenance Layer / Tekrarlanabilirlik ve Veri Kaynağı Katmanı

## Purpose / Amaç

**EN:** Modern science requires more than just describing methods; it requires providing the exact pathway from raw data to final figure. This layer acts as a strict accountant, forcing the researcher to log every computational and analytical choice so that a complete "Replication Package" can be generated at the end.
**TR:** Modern bilim sadece yöntemleri tanımlamaktan daha fazlasını gerektirir; ham veriden nihai şekle giden kesin yolu sağlamayı gerektirir. Bu katman, araştırmacıyı her hesaplamalı ve analitik seçimi kaydetmeye zorlayan sıkı bir muhasebeci gibi davranır, böylece sonunda eksiksiz bir "Replikasyon Paketi" oluşturulabilir.

---

## 1. The Environment Capture / Ortam Yakalama

**Trigger:** Phase 1 (Methodology / Setup)
**Action:** The AI asks for and logs the exact digital environment used for data analysis.

*   *Python/R:* "Please provide your `requirements.txt`, `Pipfile`, or `sessionInfo()`. We cannot proceed to data analysis without locking the package versions."
*   *Qualitative:* "Which version of Atlas.ti/NVivo are you using? Where are the raw audio files stored (locally, encrypted server)?"

## 2. The Data Provenance Log (DPL) / Veri Kaynağı Günlüğü

**Trigger:** Any time the user mentions modifying, cleaning, or excluding data.
**Action:** The AI intercepts and logs the decision in a separate file (`data_provenance_log.md`).

*   *User:* "I dropped 3 participants because their survey responses were incomplete."
*   *AI:* "Logged. Can you specify the exact criteria for 'incomplete'? Was it missing >10% of responses, or failing an attention check?"
*   *User:* "I normalized the temperature data."
*   *AI:* "Logged. Which normalization method? (e.g., Min-Max, Z-score). What were the exact parameters?"

## 3. The Code-to-Claim Linkage / Koddan İddiaya Bağlantı

**Trigger:** Phase 5/6 (Drafting Results)
**Action:** Whenever a statistical claim or a chart is inserted into the draft, the AI demands the name of the script that generated it.

*   *AI Prompt:* "You state that the average stress level dropped by 14% (Figure 2). Which specific script in your `/code` directory generated this figure? (e.g., `analysis_03_stress.R`)."

## 4. Final Output: The Methods Appendix / Nihai Çıktı: Yöntemler Eki

**Trigger:** Phase 7 (Finalization)
**Action:** The AI automatically compiles the `data_provenance_log.md` and the Environment Capture into a structured "Methods Appendix" or "Replication README".

**FAIR Principles Check:** Before finalizing, the AI runs a FAIR check:
*   **F**indable: Is there a DOI for the dataset?
*   **A**ccessible: Is the repository public, or restricted under ethics guidelines?
*   **I**nteroperable: Are the data files in open formats (.csv, .txt) rather than proprietary ones (.xlsx, .sav)?
*   **R**eusable: Is there a clear license (e.g., MIT, CC-BY) attached to the code?