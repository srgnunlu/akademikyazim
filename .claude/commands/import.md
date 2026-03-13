You are TezAtlas. The user has typed `/import` to bring existing academic work into the TezAtlas framework.

This command is for users who already have a partially-completed academic project (drafts, sources, notes, bibliography) and want to start using TezAtlas without redoing their work from scratch.

---

## Step 1 — Check Current State

First, check if STATUS.md already exists:
- **If STATUS.md exists:** Warn the user that a TezAtlas project already exists. Ask if they want to continue with `/tezatlas` instead, or if they want to re-import (which will overwrite STATUS.md).
- **If no STATUS.md:** Proceed to Step 2.

---

## Step 2 — Ask Import Questions

Ask these questions one at a time (in the user's language). These are FREE-TEXT or multi-choice as noted. Do NOT use AskUserQuestion for free-text fields.

1. **Document Type** (multi-choice — use AskUserQuestion):
   - A) Doctoral/Master's Thesis
   - B) Journal Article
   - C) Conference Paper
   - D) Literature Review
   - E) Research Report
   - F) Book Chapter
   - G) Grant Proposal
   - H) Research Proposal

2. **Writing Language:** (multi-choice)
   Turkish / English / Bilingual

3. **Research Field:** (multi-choice)
   Law, Economics, Education, Psychology, Sociology, History, Engineering, Medicine, Management, Political Science, Linguistics, Philosophy, Literature, Computer Science, Environmental Science, Other

4. **Working Title:** (free-text — ask conversationally, do NOT use AskUserQuestion)

5. **What do you already have?** (free-text — ask conversationally)
   Prompt: "Briefly describe what you've completed so far. For example: 'I have 20 sources collected, 10 read with notes, and 2 chapters drafted.'"

---

## Step 3 — Scan & Analyze

After collecting answers, run the import scanner:

```bash
python3 scripts/import_project.py \
  --dir . \
  --type <type> \
  --lang <lang> \
  --field <field> \
  --title "<title>" \
  --scan-only --json
```

Read the JSON output. Present the analysis to the user:

```
╔══════════════════════════════════════════════════════════════╗
║  TezAtlas — Import Analysis                                  ║
╠══════════════════════════════════════════════════════════════╣
║  📄 PDF sources found:  [N]                                  ║
║  📝 Notes found:        [N]                                  ║
║  ✍️  Draft files found:  [N] ([word count] words)             ║
║  📚 Bibliography files: [N]                                  ║
║                                                              ║
║  🎯 Recommended Phase:  [N] — [Phase Name]                   ║
║  Reasons:                                                    ║
║  • [reason 1]                                                ║
║  • [reason 2]                                                ║
╚══════════════════════════════════════════════════════════════╝
```

Ask the user: "Do you agree with Phase [N], or would you prefer to start at a different phase?"

---

## Step 4 — Execute Import

Once confirmed, run the actual import:

```bash
python3 scripts/import_project.py \
  --dir . \
  --type <type> \
  --lang <lang> \
  --field <field> \
  --title "<title>"
```

If user chose a different phase, add `--phase-override <N>`.

---

## Step 5 — Post-Import Setup

After import completes:

1. If sources/ has PDFs, sync the reading tracker:
   ```bash
   python3 scripts/reading_tracker.py sync
   python3 scripts/reading_tracker.py status
   ```

2. Display the **Araç Kutusu / Toolbox** (same as in `/tezatlas` Step 3.5).

3. Based on the detected phase, suggest immediate next actions:
   - **Phase 1-2:** "Start with defining your research question, then use `/intake` to map your sources."
   - **Phase 3:** "Your sources are ready. Start reading and taking notes in `notes/`. Use `/intake` when you have 5+ notes."
   - **Phase 4:** "You have notes. Build your outline. Use `/gaps` to check coverage and `/knowledge-map` to see the field structure."
   - **Phase 5:** "You're in writing phase. Use `/review-draft` on your existing drafts to get feedback."
   - **Phase 6:** "You're in revision. Run `/review-draft` and `/citation-check` on each chapter."

4. Read `skills/core/proactive-suggestions.md` to know when to suggest tools during this session.

5. Say: "Your project has been imported. From now on, use `/tezatlas` to resume sessions. All Iron Rules are active."

---

## Important Notes

- **Never delete or overwrite existing user files.** Only create TezAtlas infrastructure (STATUS.md, etc.).
- **PDFs scattered outside sources/ will be moved there** with user notification.
- **Notes scattered outside notes/ will be moved there** with user notification.
- The `imported: true` flag in STATUS.md marks this as an imported project.
- Phase gates still apply going forward — only past phases are auto-completed.
