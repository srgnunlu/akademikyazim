---
title: "Drafting Alternatives Matrix"
title_tr: "Taslak Alternatifleri Matrisi"
node_type: technique
priority: high
description: "Presents multiple drafting alternatives (A, B, C) with pros, cons, and scored evaluations during the writing phase to give the user ultimate editorial control."
description_tr: "Kullanıcıya nihai editoryal kontrolü vermek için yazım aşamasında avantajları, dezavantajları ve puanlanmış değerlendirmeleriyle birlikte birden fazla taslak alternatifi (A, B, C) sunar."
tags: [technique, drafting, writing, alternatives, scoring, evaluation]
links_to:
  - skills/core/iron-rules.md
  - skills/ux/anxiety-aware-language.md
  - skills/techniques/paragraph-coherence.md
  - skills/techniques/natural-voice.md
language: bilingual
version: "3.0"
---

# Drafting Alternatives Matrix / Taslak Alternatifleri Matrisi

## Purpose / Amaç

**EN:** The AI should not force a single block of text on the user. To maintain the author's editorial agency and intellectual ownership, the AI must generate multiple drafting options for any substantive paragraph or section, evaluate them transparently, and let the user decide. This file defines the detailed scoring matrix. For the complete Guided Writing Mode format (including Academic Writing Note and source evidence layer), see `skills/core/guided-writing-mode.md`.
**TR:** YZ, kullanıcıya tek bir metin bloğunu dayatmamalıdır. Yazarın editoryal otoritesini ve entelektüel sahipliğini korumak için YZ, herhangi bir önemli paragraf veya bölüm için birden fazla taslak seçeneği oluşturmalı, bunları şeffaf bir şekilde değerlendirmeli ve kararı kullanıcıya bırakmalıdır. Bu dosya detaylı puanlama matrisini tanımlar. Tam Guided Writing Mode formatı (Akademik Yazım Notu ve kaynak kanıtı katmanı dahil) için bkz. `skills/core/guided-writing-mode.md`.

---

## 0. Bağlam Hazırlığı / Context Preparation

**EN:** Before generating alternatives, the AI MUST read the Paragraph Context Card (PBK) from `paragraph-coherence.md`. If this is NOT the first paragraph of the section, the following context is mandatory input for every alternative:
**TR:** Alternatifler üretmeden ÖNCE, AI `paragraph-coherence.md`'deki Paragraf Bağlam Kartını (PBK) okumalıdır. Bölümün ilk paragrafı DEĞİLSE, aşağıdaki bağlam her alternatif için zorunlu girdidir:

```
Zorunlu Girdi (ilk paragraf hariç):
  ● Önceki paragrafın ana iddiası (PBK'dan)
  ● Kullanılan terimler — bunları aynı formda TEKRARLAMA
  ● Açık kalan nokta — ele al veya neden atlandığını belirt
  ● Geçiş beklentisi — bağlantıyı kur
  ● Argüman İzleyici — hangi alt iddia sırada?
```

İlk paragrafta PBK yoktur; bölüm açılış signpost'u (`academic-writing-quality.md`) yeterlidir.

---

## 1. The Generation Rule / Üretim Kuralı

**Trigger:** During the Drafting/Writing phase (e.g., Thesis Phase 6, Article Phase 4) when the user asks to draft a section or paragraph from their notes.
**Action:** Do NOT output a single draft. Generate 3 to 4 distinct alternatives (labeled A, B, C, D).

**Variation Strategies:**
*   *Alternative A:* Direct, punchy, empirical focus (Data-first).
*   *Alternative B:* Theoretical, narrative-driven, focusing on the literature gap.
*   *Alternative C:* Highly cautious, heavily hedged, explicitly addressing counter-arguments.
*   *Alternative D:* (If applicable) A bold, synthesized approach.

## 2. The Evaluation Matrix / Değerlendirme Matrisi

For each alternative, provide:
1.  **Metin (The Text)**
2.  **Avantajlar (Pros):** What makes this version strong?
3.  **Dezavantajlar (Cons):** What are the risks or weaknesses of this version?
4.  **Puan (Score):** Out of 5.0.

**Scoring Criteria / Puanlama Kriterleri:**
*   **Savunma (Defense/Support):** How well is it anchored in cited sources? (Iron Rule 1: Master's/PhD students cannot make unsupported claims).
*   **Akıcılık (Fluency):** Is the transition from the previous paragraph smooth?
*   **Özgünlük (Originality):** Does it clearly highlight the user's contribution?
*   **Bağlam (Coherence):** (`paragraph-coherence.md`) Does this alternative: (a) flow from the previous paragraph's PBK, (b) advance a NEW sub-claim in the Argument Tracker, (c) avoid term and structural repetition? / Bu alternatif: (a) önceki paragrafın PBK'sından doğal akıyor mu, (b) Argüman İzleyici'de YENİ bir alt iddiayı ilerletiyor mu, (c) terim ve yapısal tekrardan kaçınıyor mu?

*Constraint:* Order the alternatives descending by Total Score (highest first).

## 3. Presentation Format / Sunum Formatı

After presenting the text of the alternatives, summarize the evaluation in an ASCII table:

```text
 ┌─────┬─────────┬──────────┬──────────┬────────┬────────┐
 │     │ Savunma │ Akıcılık │ Özgünlük │ Bağlam │ Toplam │
 ├─────┼─────────┼──────────┼──────────┼────────┼────────┤
 │ A   │ ★★★★★   │ ★★★★     │ ★★★      │ ★★★★★  │ 4.5/5  │
 ├─────┼─────────┼──────────┼──────────┼────────┼────────┤
 │ B   │ ★★★★★   │ ★★★★★    │ ★★★      │ ★★★★   │ 4.2/5  │
 ├─────┼─────────┼──────────┼──────────┼────────┼────────┤
 │ C   │ ★★★★    │ ★★★★     │ ★★★★★    │ ★★★    │ 3.8/5  │
 ├─────┼─────────┼──────────┼──────────┼────────┼────────┤
 │ D   │ ★★★     │ ★★★★★    │ ★★       │ ★★★★   │ 3.5/5  │
 └─────┴─────────┴──────────┴──────────┴────────┴────────┘
```

## 4. Iteration and Mitigation / İterasyon ve Giderme

**AI Action:** When the user selects an option (e.g., "I choose B"), the AI must:
1.  Remember the choice for the context of the next paragraph.
2.  Specifically identify the stated "Dezavantaj" (Con) of that chosen option.
3.  **Do NOT immediately present a final version.** Instead, generate a *new* set of sub-alternatives (e.g., B.1, B.2, B.3) that attempt to mitigate that specific disadvantage using different strategies.
    *   *Example:* "You chose B. Its main disadvantage was a lack of empirical grounding. Here are 3 ways we can solve that:"
        *   **B.1:** Adds a brief statistical citation from [Source X].
        *   **B.2:** Adds a qualitative example from [Source Y].
        *   **B.3:** Changes the verb from "proves" to "suggests" to lower the empirical burden.
4.  Present the new sub-alternatives with the same scoring matrix (Savunma, Akıcılık, Özgünlük, Bağlam).
5.  Allow the user to make the final selection. This ensures the user retains control even during the revision of a draft.
6.  After final selection: update the Paragraph Context Card (PBK) and Argument Tracker per `paragraph-coherence.md`. This step is MANDATORY before generating the next paragraph's alternatives. / Son seçimden sonra: `paragraph-coherence.md`'ye göre Paragraf Bağlam Kartını (PBK) ve Argüman İzleyiciyi güncelle. Bu adım, sonraki paragrafın alternatifleri üretilmeden ÖNCE zorunludur.

## 5. The Iron Rule Check / Demir Kural Kontrolü

**EN:** Every alternative MUST obey Iron Rule 1 and 4. You cannot invent a beautifully fluent sentence (Alternative D) if it lacks a citation. A master's student cannot write an unsupported sentence. If a claim lacks backing, its "Savunma" score must be 0, and it should be heavily penalized or flagged with `[KAYNAK BEKLENİYOR]`.
**TR:** Her alternatif Demir Kural 1 ve 4'e UYMALIDIR. Atıfı yoksa güzel ve akıcı bir cümle (Alternatif D) uyduramazsınız. Bir yüksek lisans öğrencisi dayanaksız bir cümle kuramaz. Bir iddia dayanaktan yoksunsa "Savunma" puanı 0 olmalı ve ağır şekilde cezalandırılmalı veya `[KAYNAK BEKLENİYOR]` ile işaretlenmelidir.

## 6. Natural Voice Filter (v3.0) / Doğal Ses Filtresi

**EN:** Every alternative MUST pass the Natural Voice triple filter from `natural-voice.md` before being presented to the user:
**TR:** Her alternatif kullanıcıya sunulmadan ÖNCE `natural-voice.md`'deki Doğal Ses üçlü filtresinden geçmelidir:

1. **Blacklist scan:** No AI-tell vocabulary or patterns (see blacklist in `natural-voice.md`). If found → replace with specific, concrete language.
2. **Burstiness check:** Sentence length must span at least 3 bands (short ≤10, medium 11-22, long ≥23 words). No 3 consecutive same-band sentences. Paragraph openings must vary.
3. **Style profile match:** If `YAZIM_PROFILI.md` exists, check against user's declared preferences (avoided constructs, punctuation habits, paragraph length). Flag mismatches as ⚠️ next to the alternative.

Alternatives that fail filter 1 or 2 are regenerated. Filter 3 mismatches are flagged but not auto-rejected (user may intentionally deviate).