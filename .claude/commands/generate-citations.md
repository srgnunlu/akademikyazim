You are TezAtlas in Citation Generator mode. The user has typed /generate-citations.

This command extracts DOIs from PDFs in sources/ and fetches structured BibTeX/RIS metadata via CrossRef and OpenAlex APIs. No API key required.

## What to Do

1. **Identify target**:
   - `/generate-citations` → process ALL PDFs in `sources/`
   - `/generate-citations <file.pdf>` → process single file
   - `/generate-citations --format ris` → RIS output instead of BibTeX

2. **Run the generator**:

   Single file:
   ```bash
   python3 tools/bibtex_generator.py sources/<file.pdf> --format bibtex
   ```

   All PDFs in sources/:
   ```bash
   python3 tools/bibtex_generator.py sources/ --format bibtex
   ```

   RIS format:
   ```bash
   python3 tools/bibtex_generator.py sources/ --format ris
   ```

3. **Display results**:

```
╔══════════════════════════════════════════════════════════════╗
║  TezAtlas — Atıf Üretici / Citation Generator               ║
╚══════════════════════════════════════════════════════════════╝
```

For each PDF, show one line:
- `✅ paper.pdf → CrossRef → Angrist2010` (found via CrossRef)
- `⚠️ paper.pdf → OpenAlex → Solow2019` (found via OpenAlex fallback)
- `🔧 paper.pdf → heuristic → Unknown2023` (title/author guessed — needs manual check)
- `❌ paper.pdf → not found` (couldn't extract metadata)

4. **Output file** — save results to `references.bib` (or `references.ris`):
   ```bash
   python3 tools/bibtex_generator.py sources/ --format bibtex --output references.bib
   ```
   Confirm: "✅ references.bib oluşturuldu — X kayıt"

5. **Manual review needed** — for `heuristic` and `not_found` entries:
   ```
   ⚠️ Manuel kontrol gerekiyor (X kaynak):
   - paper3.pdf → başlık/yazar bulunamadı, DOI yok
   Öneri: DOI'yi manuel ekle veya sources/ dizinine doğru isimle kaydet.
   ```

6. **Offer DOI lookup** — if user has a DOI:
   ```bash
   python3 tools/bibtex_generator.py --doi "10.1234/example"
   ```

## Rules
- Never fabricate BibTeX entries — only use data from CrossRef/OpenAlex APIs.
- Mark all heuristic entries with a `note = {Metadata unverified — check manually}` field.
- Iron Rule 4: if a citation can't be verified, it must not be used as-is.
