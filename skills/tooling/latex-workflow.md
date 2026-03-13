---
title: "LaTeX Workflow for Academic Writing"
title_tr: "Akademik Yazım için LaTeX İş Akışı"
node_type: tooling
description: "Practical LaTeX setup, package selection, figure/table handling, BibTeX/biber workflow, and arXiv submission checklist for academic documents."
description_tr: "Akademik belgeler için pratik LaTeX kurulumu, paket seçimi, şekil/tablo yönetimi, BibTeX/biber iş akışı ve arXiv gönderim kontrol listesi."
tags: [tooling, latex, overleaf, bibtex, stem, formatting]
links_to:
  - skills/core/iron-rules.md
  - skills/tooling/citation-formats.md
language: bilingual
version: "1.0"
---

# LaTeX Workflow for Academic Writing / Akademik Yazım için LaTeX İş Akışı

## 1. Overleaf vs Local Setup

| Feature | Overleaf | Local (TeX Live / MiKTeX) |
|---------|----------|--------------------------|
| Setup time | Zero — browser ready | 30–90 min |
| Collaboration | Real-time, link sharing | Git-based |
| Compilation speed | Slower on large docs | Fast, local CPU |
| Data privacy | Cloud — sensitive data risk | Local — TezAtlas default |
| Version history | Built-in (limited on free) | Full git control |
| Offline access | No | Yes |

**Recommendation:** Local setup for thesis and sensitive-data projects. Overleaf for quick collaborative drafts. TezAtlas default: local (see `skills/core/data-privacy.md`).

---

## 2. Essential Packages

```latex
% Encoding — always first
\usepackage[utf8]{inputenc}       % Turkish + non-ASCII
\usepackage[T1]{fontenc}          % Proper font encoding
\usepackage[turkish,english]{babel}

% Bibliography — biblatex + biber preferred
\usepackage[backend=biber, style=apa]{biblatex}

% Layout + links
\usepackage{geometry}
\geometry{a4paper, margin=2.5cm}
\usepackage[hidelinks]{hyperref}
\usepackage{cleveref}             % \cref{fig:1} → "Figure 1"

% Math
\usepackage{amsmath, amssymb, amsthm}

% Tables
\usepackage{booktabs}             % \toprule \midrule \bottomrule
\usepackage{tabularx}

% Figures
\usepackage{graphicx}
\usepackage{subcaption}

% Algorithms
\usepackage[ruled,vlined]{algorithm2e}

% Typography
\usepackage{microtype}            % Better justification
\usepackage{setspace}             % Line spacing
```

**Package load order:** `inputenc`/`fontenc` first → content packages → `hyperref` near last → `cleveref` after `hyperref`.

---

## 3. BibTeX vs Biber

| | BibTeX | Biber |
|-|--------|-------|
| Works with | `natbib`, legacy styles | `biblatex` |
| Unicode / Turkish | Limited, workarounds needed | Full UTF-8 native |
| Sorting | Basic | Locale-aware, configurable |
| Multiple bibliographies | Difficult | Native support |
| Active development | Frozen | Active |

**Use Biber + biblatex** for all new projects. Use BibTeX + natbib only if a journal's `.sty` template requires it.

**Compile order with Biber:**
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

**TezAtlas integration:** `bibtex_generator.py` → `sources/references.bib` → add to LaTeX:
```latex
\addbibresource{sources/references.bib}
```

---

## 4. Figure Handling

```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=0.8\linewidth]{figures/diagram.pdf}
  \caption{Caption text. \textit{Source:} Author, Year.}
  \label{fig:diagram}
\end{figure}
```

**Format guide:**

| Format | Type | Best for |
|--------|------|----------|
| PDF | Vector | Diagrams, plots — preferred |
| EPS | Vector | Legacy journal submissions |
| PNG | Raster | Screenshots — 300 dpi min |
| JPEG | Raster | Photos only (avoid for line art) |

Always export plots as PDF: `plt.savefig('fig.pdf')` (matplotlib) / `ggsave('fig.pdf')` (R).

**Subfigures:**
```latex
\begin{subfigure}[b]{0.45\linewidth}
  \includegraphics[width=\linewidth]{figures/a.pdf}
  \caption{Panel A}\label{fig:a}
\end{subfigure}
```

---

## 5. Table Best Practices

No vertical lines. Three horizontal rules only.

```latex
\begin{table}[htbp]
  \centering
  \caption{Caption goes ABOVE the table.}
  \label{tab:results}
  \begin{tabular}{lcc}
    \toprule
    Variable & Group A & Group B \\
    \midrule
    Mean     & 3.21    & 4.56    \\
    SD       & 0.45    & 0.78    \\
    $n$      & 120     & 118     \\
    \bottomrule
  \end{tabular}
\end{table}
```

Rules: Caption **above** tables (APA/most journals). Never `\hline`. Use `tabularx` with `X` column for auto-width text.

---

## 6. arXiv Submission Checklist

- [ ] All figures as separate files (PDF/EPS/PNG) in `figures/`
- [ ] `.bbl` file included — arXiv does not run biber; compile locally first
- [ ] No absolute paths in `\includegraphics{}`
- [ ] Removed draft options and `\usepackage{showkeys}`
- [ ] Fonts embedded, no missing glyphs in compiled PDF
- [ ] ORCID in author metadata
- [ ] Source zip: `main.tex`, custom `.sty`/`.cls`, `figures/`, `references.bib`, `main.bbl`

**Generating `.bbl` for arXiv:**
```bash
pdflatex main && biber main && pdflatex main
# main.bbl now exists — include in arXiv upload
```

---

## 7. Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Unicode character` | Missing encoding | `\usepackage[utf8]{inputenc}` |
| Turkish ş/ğ/ü broken | Wrong font encoding | Add `\usepackage[T1]{fontenc}` |
| `biber: file not found` | Stale aux files | `rm *.aux *.bcf *.blg` then recompile |
| Overfull hbox | Long words/URLs | Add `\usepackage{microtype}` |
| `undefined \cref` | Load order | Load `cleveref` after `hyperref` |
| arXiv font not found | Custom font not uploaded | Include `.sty` or use standard fonts |
| Too many floats | Accumulated unplaced floats | `\clearpage` or `[H]` + `placeins` |

---

## 8. Recommended Project Structure

```
project/
├── main.tex
├── chapters/
│   ├── introduction.tex
│   └── methodology.tex
├── figures/           # vector PDFs preferred
├── sources/
│   ├── references.bib # from bibtex_generator.py
│   └── *.pdf          # local — not committed (data-privacy.md)
└── output/
    └── main.pdf
```

Iron Rule 1 reminder: every `\cite{}` key must have a corresponding file in `sources/`. No citation from memory.
