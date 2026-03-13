# Proactive Command Suggestions

## When to Suggest Commands

Claude should proactively suggest relevant commands at natural moments — not every turn, but when the context clearly calls for a specific tool. Never spam suggestions.

### Reading Phase (Phase 2-3)

| Trigger | Suggest | Message (adapt to user's language) |
|---------|---------|--------|
| User adds 5th source note to notes/ | `/intake` | "You now have enough sources for a source map. Want to run `/intake` to see how they cluster?" |
| User adds 8th+ source note | `/contradictions` | "With this many sources, it's worth checking for contradictions: `/contradictions`" |
| User mentions a key concept repeatedly | `/citation-chain` | "You keep referencing [concept]. Want to trace its intellectual lineage with `/citation-chain`?" |
| User asks "do I have enough sources?" | `/gaps` | "Let's check: `/gaps` will show what's missing" |
| User expresses uncertainty about methodology | `/method-audit` | "Want to audit the methodological landscape? `/method-audit`" |
| Reading phase nearing completion | `/knowledge-map` | "Before moving to writing, let's build your field's knowledge map: `/knowledge-map`" |

### Pre-Writing Phase (Phase 4-5)

| Trigger | Suggest | Message |
|---------|---------|---------|
| User is about to write Introduction | `/so-what` | "Before writing the intro, let's nail down the 3 essential statements: `/so-what`" |
| User is about to write Literature Review | `/synthesize` | "Time to synthesize: `/synthesize` will organize sources by argument" |
| User drafts an argument without citation | `/citation-check` | "That claim needs a source. Want to verify with `/citation-check`?" |
| User mentions assumptions or "we assume" | `/assumptions` | "Want to surface the hidden assumptions in your sources? `/assumptions`" |

### Writing Phase (Phase 5-6)

| Trigger | Suggest | Message |
|---------|---------|---------|
| User completes a draft section | `/review-draft` | "Section done? Let's run a 4-layer review: `/review-draft <file>`" |
| User makes a strong claim | `/devil-advocate` | "Strong claim. Want to stress-test it? `/devil-advocate`" |
| User writing Discussion chapter | `/assumptions` + `/knowledge-map` | "For the discussion, these tools help: `/assumptions` for hidden foundations, `/knowledge-map` for positioning" |
| User writing Conclusion | `/so-what` | "For the conclusion, revisit your 3 essential statements: `/so-what`" |

### General (any phase)

| Trigger | Suggest | Message |
|---------|---------|---------|
| User asks "what can you do?" | Show toolbox | Display the full Arac Kutusu from `/tezatlas` |
| User seems stuck or unsure | Suggest most relevant tool | Pick the single most relevant command for current phase |
| User hasn't used any analysis tool in 3+ sessions | Gentle reminder | "Remember, you have literature analysis tools available. `/status` to see where you are, then pick a tool." |

## After Each Command Completes — Automatic Next Step

When any literature intelligence or analysis command finishes, always close with a single next-step suggestion. Use this chain:

| Command completed | Suggest next |
|---|---|
| `/intake` | `/contradictions` — "Kaynak haritası hazır. Şimdi çelişkileri tarayalım." |
| `/contradictions` | `/citation-chain` — "Çelişkiler belirlendi. Bu tartışmanın entelektüel kökenini izleyelim." |
| `/citation-chain` | `/gaps` — "Atıf zinciri çıktı. Şimdi cevaplanmamış soruları bulalım." |
| `/gaps` | `/assumptions` — "Boşluklar belirlendi. Bu boşlukların arkasındaki varsayımları sorgulayalım." |
| `/assumptions` | `/knowledge-map` — "Varsayımlar netleşti. Alan haritasını çizelim." |
| `/knowledge-map` | `/so-what` — "Harita hazır. Şimdi 3 temel soruyu cevaplayalım." |
| `/so-what` | `/synthesize` — "Önem testi geçildi. Argüman bazlı senteze geçelim." |
| `/synthesize` | `/review-draft <file>` — "Sentez hazır. Taslak bölümleri incelemeye başlayalım." |
| `/review-draft` | `/devil-advocate` — "Taslak incelendi. En güçlü argümanı 4 açıdan sorgulayalım." |
| `/devil-advocate` | `/citation-check "<claim>"` — "Argüman sağlamlaştı. Kritik iddianın kaynak doğrulamasını yapalım." |

This chain ensures the 9 Literature Intelligence tools are used in sequence, not in isolation. Always surface the next step — never leave the user wondering "now what?".

## How to Suggest

- **One suggestion at a time** — never list 5 commands at once
- **Brief** — one sentence, not a paragraph
- **Actionable** — include the exact command to type
- **Contextual** — explain WHY this tool is relevant right now
- **Non-blocking** — suggest, don't insist. If user ignores, move on
- **Language-matched** — use the user's project language (from STATUS.md)
