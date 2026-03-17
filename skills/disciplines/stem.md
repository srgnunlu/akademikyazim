---
title: "STEM & Engineering Module"
title_tr: "STEM ve Mühendislik Modülü"
node_type: template
priority: high
description: "Discipline-specific rules for Computer Science, Engineering, and Hard Sciences. Focuses on computational reproducibility, LaTeX workflows, and code integration."
description_tr: "Bilgisayar Bilimleri, Mühendislik ve Temel Bilimler için disipline özgü kurallar. Hesaplamalı tekrarlanabilirlik, LaTeX iş akışları ve kod entegrasyonuna odaklanır."
tags: [discipline, stem, engineering, cs, latex, github, reproducibility]
links_to:
  - skills/core/iron-rules.md
language: bilingual
version: "1.0"
---

# STEM & Engineering Module / STEM ve Mühendislik Modülü

## Purpose / Amaç

**EN:** STEM research relies heavily on mathematical notation, computational environments, and algorithmic reproducibility. This module adapts TezAtlas for technical workflows where code and data are just as important as prose.
**TR:** STEM araştırmaları matematiksel gösterime, hesaplamalı ortamlara ve algoritmik tekrarlanabilirliğe büyük ölçüde dayanır. Bu modül TezAtlas'ı kod ve verinin metin kadar önemli olduğu teknik iş akışlarına uyarlar.

---

## 1. Citation Standard: IEEE / Atıf Standardı: IEEE

Unless submitting to an APA or Vancouver journal, default to IEEE style.
*   **In-text:** Numbered in brackets [1].
*   **Bibliography:** Numbered list, abbreviated journal titles.

## 2. Computational Reproducibility / Hesaplamalı Tekrarlanabilirlik

In Phase 1 (Methodology) of any STEM paper, the AI must ensure the "Environment Profile" is documented.
*   **Code Repository:** Does a GitHub/GitLab link exist?
*   **Environment:** Is there a `requirements.txt`, `environment.yml`, or `Dockerfile`?
*   **Random Seeds:** Are random seeds explicitly stated for machine learning / simulation results?
*   **Data Availability:** "Data underlying the results presented in this paper are available in [Repository Name] at [URL]."

## 3. LaTeX Workflow Integration / LaTeX İş Akışı Entegrasyonu

*   **Math Environments:** Do not use raw Unicode math. Always use valid LaTeX syntax (e.g., `$E = mc^2$` for inline, `\begin{equation}...\end{equation}` for blocks).
*   **Citations:** When in Draft Generator mode, generate citations as `\cite{smith2023}` instead of plain text if the user indicates they are writing for a `.tex` file.
*   **Algorithmic Pseudocode:** When presenting an algorithm, automatically format it using a structure compatible with `algorithm2e` or `algorithmicx` packages.

## 4. Pre-print Strategy (arXiv) / Ön Baskı Stratejisi

In Phase 0 (Claim/Venue), remind the user about preprint servers (arXiv, bioRxiv, ChemRxiv).
*   **AI Prompt:** *"In CS and Physics, it is standard to post a preprint to arXiv simultaneously with journal submission. Shall we prepare the arXiv-compliant LaTeX source package at the end of Phase 7?"*