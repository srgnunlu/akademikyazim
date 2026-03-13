#!/usr/bin/env python3
"""
import_project.py — TezAtlas Mid-Project Import Tool

Scans an existing directory for academic work artifacts (PDFs, notes, drafts,
bibliography files) and determines the appropriate TezAtlas phase. Creates
STATUS.md at the detected phase so users can start where they actually are.

Usage:
  python3 scripts/import_project.py --dir . --type thesis --lang tr --field law
  python3 scripts/import_project.py --dir ~/thesis --type article --lang en --field cs --title "My Paper"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).parent.parent

# ── Detection patterns ────────────────────────────────────────────────────────

PDF_EXTENSIONS = {".pdf"}
NOTE_EXTENSIONS = {".md", ".txt", ".docx"}
BIB_EXTENSIONS = {".bib", ".ris", ".enw", ".nbib"}
DRAFT_EXTENSIONS = {".md", ".docx", ".tex", ".odt"}

# Patterns that suggest a file is a draft chapter/section (not a note)
DRAFT_PATTERNS = [
    r"(giris|giriş|introduction|intro)",
    r"(literatur|literatür|literature|lit.?review|related.?work)",
    r"(yontem|yöntem|method|methodology)",
    r"(bulgular|sonuclar|results|findings|analysis)",
    r"(tartisma|tartışma|discussion)",
    r"(sonuc|sonuç|conclusion)",
    r"(chapter|bolum|bölüm)",
    r"(abstract|ozet|özet)",
    r"(draft|taslak)",
]

DRAFT_RE = re.compile("|".join(DRAFT_PATTERNS), re.IGNORECASE)

# Patterns for notes (shorter, source-focused)
NOTE_PATTERNS = [
    r"(note|not|okuma|reading)",
    r"(summary|ozet|özet)",
    r"(review|inceleme)",
]

NOTE_RE = re.compile("|".join(NOTE_PATTERNS), re.IGNORECASE)


# ── Scanning ──────────────────────────────────────────────────────────────────

def scan_directory(project_dir: Path) -> dict:
    """Scan directory for academic work artifacts."""
    result = {
        "pdfs": [],
        "notes": [],
        "drafts": [],
        "bib_files": [],
        "has_sources_dir": False,
        "has_notes_dir": False,
        "has_outline": False,
        "has_status": False,
        "has_arguments": False,
        "has_reading_report": False,
        "total_word_count": 0,
        "draft_sections": [],
    }

    # Check for existing TezAtlas files
    result["has_status"] = (project_dir / "STATUS.md").exists()
    result["has_arguments"] = (project_dir / "ARGUMENTS.md").exists()
    result["has_reading_report"] = (project_dir / "READING_REPORT.md").exists()
    result["has_sources_dir"] = (project_dir / "sources").is_dir()
    result["has_notes_dir"] = (project_dir / "notes").is_dir()

    # Check for outline
    for name in ["outline", "yapi", "yapı", "iskelet", "structure", "plan"]:
        for ext in [".md", ".txt", ".docx"]:
            if (project_dir / f"{name}{ext}").exists():
                result["has_outline"] = True
                break

    # Scan all files recursively (but skip hidden dirs, node_modules, etc.)
    skip_dirs = {".git", "node_modules", ".next", "__pycache__", "venv", ".venv",
                 "website", "mcp_server", "scripts", "tests", "core", "agents",
                 "skills", "tools", ".claude", ".devcontainer"}

    for path in _walk_files(project_dir, skip_dirs):
        ext = path.suffix.lower()
        rel = path.relative_to(project_dir)
        rel_str = str(rel)

        # PDFs
        if ext in PDF_EXTENSIONS:
            result["pdfs"].append(rel_str)

        # Bibliography files
        elif ext in BIB_EXTENSIONS:
            result["bib_files"].append(rel_str)

        # Markdown/text files — classify as draft or note
        elif ext in NOTE_EXTENSIONS and ext != ".docx":
            # Skip TezAtlas system files
            if path.name in {"STATUS.md", "READING_REPORT.md", "ARGUMENTS.md",
                             "DASHBOARD.md", "SOURCE_MAP.md", "GAPS.md",
                             "CONTRADICTIONS.md", "ASSUMPTIONS.md",
                             "KNOWLEDGE_MAP.md", "CITATION_CHAIN.md",
                             "SO_WHAT.md", "SYNTHESIS.md", "README.md",
                             "CHANGELOG.md", "CLAUDE.md", ".gitignore"}:
                continue

            content = _safe_read(path)
            word_count = len(content.split())

            # Files inside notes/ directory are always notes
            in_notes_dir = rel_str.startswith("notes/") or "/notes/" in rel_str

            if in_notes_dir and word_count > 20:
                result["notes"].append(rel_str)
            elif DRAFT_RE.search(path.stem) and word_count > 200:
                result["drafts"].append(rel_str)
                result["draft_sections"].append(path.stem.lower())
                result["total_word_count"] += word_count
            elif word_count > 50:
                # Note-like files outside notes/
                if NOTE_RE.search(path.stem):
                    result["notes"].append(rel_str)
                elif word_count > 500:
                    # Longer files are likely drafts
                    result["drafts"].append(rel_str)
                    result["total_word_count"] += word_count

        # .tex and .docx drafts
        elif ext in {".tex", ".docx"}:
            if DRAFT_RE.search(path.stem):
                result["drafts"].append(rel_str)

    return result


def _walk_files(directory: Path, skip_dirs: set) -> list[Path]:
    """Walk directory tree, skipping specified directories."""
    files = []
    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                if item.name not in skip_dirs and not item.name.startswith("."):
                    files.extend(_walk_files(item, skip_dirs))
            else:
                files.append(item)
    except PermissionError:
        pass
    return files


def _safe_read(path: Path) -> str:
    """Read text file safely."""
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


# ── Phase Detection ───────────────────────────────────────────────────────────

def detect_phase(scan: dict) -> tuple[int, str, list[str]]:
    """
    Determine the appropriate starting phase based on scan results.

    Returns: (phase_number, phase_name, reasons)
    """
    reasons = []
    pdf_count = len(scan["pdfs"])
    note_count = len(scan["notes"])
    draft_count = len(scan["drafts"])
    word_count = scan["total_word_count"]

    # Phase 6-7: Has substantial drafts + revision indicators
    if draft_count >= 3 and word_count > 10000:
        reasons.append(f"{draft_count} draft files found ({word_count:,} words)")
        if pdf_count > 0:
            reasons.append(f"{pdf_count} PDF sources available")
        if note_count > 0:
            reasons.append(f"{note_count} notes present")
        return 6, "Revizyon / Revision", reasons

    # Phase 5: Has some drafts, writing in progress
    if draft_count >= 1 and word_count > 2000:
        reasons.append(f"{draft_count} draft files found ({word_count:,} words)")
        if pdf_count > 0:
            reasons.append(f"{pdf_count} PDF sources available")
        return 5, "Yazım / Writing", reasons

    # Phase 4: Has outline or structure
    if scan["has_outline"]:
        reasons.append("Outline/structure file detected")
        if pdf_count > 0:
            reasons.append(f"{pdf_count} PDF sources available")
        if note_count > 0:
            reasons.append(f"{note_count} notes present")
        return 4, "Yapı / Outline", reasons

    # Phase 3: Has notes (reading done or in progress)
    if note_count >= 3:
        reasons.append(f"{note_count} reading notes found")
        if pdf_count > 0:
            reasons.append(f"{pdf_count} PDF sources available")
        return 3, "Okuma / Reading", reasons

    # Phase 2: Has PDFs but few/no notes (sources collected, reading not started)
    if pdf_count >= 3:
        reasons.append(f"{pdf_count} PDF sources found")
        if note_count > 0:
            reasons.append(f"{note_count} notes (reading started)")
            return 3, "Okuma / Reading", reasons
        return 2, "Kaynak Toplama / Source Collection", reasons

    # Phase 1: Has some materials but not enough
    if pdf_count > 0 or note_count > 0 or scan["bib_files"]:
        if pdf_count > 0:
            reasons.append(f"{pdf_count} PDF(s) found")
        if note_count > 0:
            reasons.append(f"{note_count} note(s) found")
        if scan["bib_files"]:
            reasons.append(f"{len(scan['bib_files'])} bibliography file(s) found")
        return 1, "Araştırma Sorusu / Research Question", reasons

    # Phase 0: Nothing found
    reasons.append("No existing academic work detected")
    return 0, "Başlangıç / Onboarding", reasons


# ── Project Setup ─────────────────────────────────────────────────────────────

def setup_project(
    project_dir: Path,
    scan: dict,
    phase: int,
    doc_type: str,
    lang: str,
    field: str,
    title: str,
) -> dict:
    """
    Set up TezAtlas project structure at the detected phase.
    Preserves existing files, only creates missing infrastructure.
    """
    today = date.today().isoformat()
    created = []
    skipped = []
    moved = []

    # Ensure core directories exist
    for subdir in ["sources", "notes", "cikti"]:
        d = project_dir / subdir
        d.mkdir(exist_ok=True)
        (d / ".gitkeep").touch(exist_ok=True)

    # Move PDFs to sources/ if they're scattered
    sources_dir = project_dir / "sources"
    for pdf_rel in scan["pdfs"]:
        pdf_path = project_dir / pdf_rel
        if not str(pdf_rel).startswith("sources/"):
            dest = sources_dir / pdf_path.name
            if not dest.exists():
                try:
                    pdf_path.rename(dest)
                    moved.append(f"{pdf_rel} → sources/{pdf_path.name}")
                except Exception:
                    pass  # Skip if can't move

    # Move loose notes to notes/ if they're scattered
    notes_dir = project_dir / "notes"
    for note_rel in scan["notes"]:
        note_path = project_dir / note_rel
        if not str(note_rel).startswith("notes/"):
            dest = notes_dir / note_path.name
            if not dest.exists():
                try:
                    note_path.rename(dest)
                    moved.append(f"{note_rel} → notes/{note_path.name}")
                except Exception:
                    pass

    # Build phase status with completed phases marked
    doc_types = {
        "thesis": ("Tez", "Thesis"),
        "article": ("Makale", "Article"),
        "conference": ("Konferans Bildirisi", "Conference Paper"),
        "lit-review": ("Literatür Derlemesi", "Literature Review"),
        "report": ("Araştırma Raporu", "Research Report"),
        "book-chapter": ("Kitap Bölümü", "Book Chapter"),
        "grant-proposal": ("Hibe Başvurusu", "Grant Proposal"),
        "research-proposal": ("Araştırma Önerisi", "Research Proposal"),
    }
    doc_tr, doc_en = doc_types.get(doc_type, ("Belge", "Document"))
    lang_label = {"tr": "Türkçe", "en": "English", "both": "Bilingual"}.get(lang, lang)

    phase_names = [
        "Başlangıç / Onboarding",
        "Araştırma Sorusu",
        "Metodoloji (ampirik ise)",
        "Okuma",
        "Yapı / Outline",
        "Yazım",
        "Revizyon",
        "Finalizasyon",
    ]

    phase_rows = []
    for i, name in enumerate(phase_names):
        if i < phase:
            status = "✅ Tamamlandı (import)"
            done = today
        elif i == phase:
            status = "⏳ Devam ediyor"
            done = "—"
        else:
            status = "⏸ Bekliyor"
            done = "—"
        phase_rows.append(f"| {i} | {name} | {status} | {done} |")

    phase_table = "\n".join(phase_rows)

    pdf_count = len(scan["pdfs"])
    note_count = len(scan["notes"])

    status_content = f"""# STATUS.md — TezAtlas Proje Durumu

## Proje Kimliği

```yaml
title: "{title}"
document_type: {doc_type}
field: {field}
language: {lang_label}
created: "{today}"
last_updated: "{today}"
current_phase: {phase}
imported: true
import_date: "{today}"
```

## Faz İlerlemesi

| Faz | Ad | Durum | Tamamlanma |
|-----|----|-------|------------|
{phase_table}

## Kaynak Havuzu

```yaml
sources:
  total_collected: {pdf_count}
  read: {note_count}
  active: {max(0, pdf_count - note_count)}
  deferred: 0
  saturation_reached: false
```

## Yazım Takibi

```yaml
writing_schedule:
  current_streak: 0
  longest_streak: 0
  last_session_date: null
  total_sessions: 0

wellbeing:
  last_session_date: "{today}"
  days_inactive: 0
  goals_missed_consecutive: 0
  last_advisor_checkpoint: null
  attrition_risk: low

motivation:
  why_statement: null
  recorded_at: null
```

## İçe Aktarma Notları / Import Notes

Bu proje TezAtlas `/import` komutuyla faz {phase}'e yerleştirildi.
Önceki fazlar otomatik tamamlandı olarak işaretlendi.

<!-- Danışman geri bildirimleri, kararlar, önemli notlar -->
"""

    # Write STATUS.md
    status_path = project_dir / "STATUS.md"
    if status_path.exists():
        skipped.append("STATUS.md (already exists)")
    else:
        status_path.write_text(status_content, encoding="utf-8")
        created.append("STATUS.md")

    # Write READING_REPORT.md if not exists
    rr_path = project_dir / "READING_REPORT.md"
    if not rr_path.exists():
        rr_content = f"""# READING_REPORT.md — Okuma Raporu

**Proje:** {title}
**Başlangıç:** {today}

## Kaynak Envanteri

| # | Yazar(lar) | Yıl | Başlık | Durum | Alaka | Notlar |
|---|-----------|-----|--------|-------|-------|--------|
| 1 | | | | 🔵 Havuzda | | |

**Durum kodları:** 🔵 Havuzda → 🟡 Okunuyor → 🟢 Tamamlandı → 🔴 Elendi

## Özet Notlar

<!-- Okuma süreci notları -->
"""
        rr_path.write_text(rr_content, encoding="utf-8")
        created.append("READING_REPORT.md")
    else:
        skipped.append("READING_REPORT.md")

    # Write ARGUMENTS.md if not exists
    arg_path = project_dir / "ARGUMENTS.md"
    if not arg_path.exists():
        arg_content = f"""# ARGUMENTS.md — Argüman İzleyici

**Proje:** {title}
**Son güncelleme:** {today}

## Aktif İddialar

| # | İddia | Kaynak | Kanıt Gücü | Durum |
|---|-------|--------|-----------|-------|
| 1 | | | ○ | 🔴 BOŞLUK |

**Kanıt gücü:** ●●● Güçlü · ●●○ Orta · ●○○ Zayıf · ○ Kanıt yok
"""
        arg_path.write_text(arg_content, encoding="utf-8")
        created.append("ARGUMENTS.md")
    else:
        skipped.append("ARGUMENTS.md")

    return {
        "created": created,
        "skipped": skipped,
        "moved": moved,
    }


# ── Report ────────────────────────────────────────────────────────────────────

def print_report(scan: dict, phase: int, phase_name: str, reasons: list[str],
                 setup_result: dict) -> None:
    """Print import analysis report."""
    print()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║  TezAtlas — Import Analysis / İçe Aktarma Analizi           ║")
    print("╠══════════════════════════════════════════════════════════════╣")

    # Scan results
    print(f"║  📄 PDF sources:  {len(scan['pdfs']):>4}                                    ║")
    print(f"║  📝 Notes:        {len(scan['notes']):>4}                                    ║")
    print(f"║  ✍️  Drafts:       {len(scan['drafts']):>4}  ({scan['total_word_count']:,} words)               ║")
    print(f"║  📚 Bib files:    {len(scan['bib_files']):>4}                                    ║")
    print("║                                                              ║")
    print(f"║  🎯 Detected Phase: {phase} — {phase_name:<36} ║")
    print("║                                                              ║")

    for reason in reasons:
        r = reason[:54]
        print(f"║  • {r:<56} ║")

    print("╠══════════════════════════════════════════════════════════════╣")

    if setup_result["created"]:
        print("║  📁 Created:                                                ║")
        for f in setup_result["created"]:
            print(f"║     + {f:<53} ║")

    if setup_result["moved"]:
        print("║  📦 Organized:                                              ║")
        for m in setup_result["moved"]:
            m_short = m[:53]
            print(f"║     → {m_short:<53} ║")

    if setup_result["skipped"]:
        print("║  ⏭️  Skipped (already exist):                                ║")
        for s in setup_result["skipped"]:
            print(f"║     = {s:<53} ║")

    print("╠══════════════════════════════════════════════════════════════╣")
    print("║  ✅ Project imported. Run /tezatlas to start working.        ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()


def print_json_report(scan: dict, phase: int, phase_name: str,
                      reasons: list[str], setup_result: dict) -> None:
    """Print machine-readable JSON report."""
    report = {
        "phase": phase,
        "phase_name": phase_name,
        "reasons": reasons,
        "scan": {
            "pdf_count": len(scan["pdfs"]),
            "note_count": len(scan["notes"]),
            "draft_count": len(scan["drafts"]),
            "word_count": scan["total_word_count"],
            "bib_count": len(scan["bib_files"]),
            "pdfs": scan["pdfs"],
            "notes": scan["notes"],
            "drafts": scan["drafts"],
        },
        "setup": setup_result,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


# ── CLI ───────────────────────────────────────────────────────────────────────

DOCUMENT_TYPES = [
    "thesis", "article", "conference", "lit-review",
    "report", "book-chapter", "grant-proposal", "research-proposal",
]

FIELDS = [
    "economics", "law", "education", "psychology", "sociology", "history",
    "engineering", "medicine", "management", "political-science", "linguistics",
    "philosophy", "literature", "computer-science", "environmental-science",
    "other",
]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TezAtlas — Import existing academic work / Mevcut çalışmayı içe aktar",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/import_project.py --dir . --type thesis --lang tr --field law
  python3 scripts/import_project.py --dir ~/thesis --type article --lang en --field cs
  python3 scripts/import_project.py --dir . --type thesis --lang tr --field law --scan-only
        """,
    )
    parser.add_argument("--dir", type=Path, default=Path("."),
                        help="Project directory to scan (default: current)")
    parser.add_argument("--type", choices=DOCUMENT_TYPES, required=True,
                        help="Document type")
    parser.add_argument("--lang", choices=["tr", "en", "both"], default="tr",
                        help="Working language (default: tr)")
    parser.add_argument("--field", choices=FIELDS, default="other",
                        help="Academic field (default: other)")
    parser.add_argument("--title", default="[İçe Aktarılan Proje]",
                        help="Working title")
    parser.add_argument("--scan-only", action="store_true",
                        help="Only scan, don't create files")
    parser.add_argument("--json", action="store_true",
                        help="JSON output")
    parser.add_argument("--phase-override", type=int, choices=range(8),
                        help="Override detected phase")

    args = parser.parse_args()
    project_dir = args.dir.resolve()

    if not project_dir.is_dir():
        print(f"Error: {project_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Scan
    scan = scan_directory(project_dir)

    # Detect phase
    phase, phase_name, reasons = detect_phase(scan)

    # Allow override
    if args.phase_override is not None:
        phase = args.phase_override
        phase_names = [
            "Başlangıç / Onboarding", "Araştırma Sorusu", "Metodoloji",
            "Okuma", "Yapı / Outline", "Yazım", "Revizyon", "Finalizasyon",
        ]
        phase_name = phase_names[phase]
        reasons.append(f"Phase overridden to {phase} by user")

    if args.scan_only:
        if args.json:
            print_json_report(scan, phase, phase_name, reasons, {"created": [], "skipped": [], "moved": []})
        else:
            print(f"\nScan Results: Phase {phase} — {phase_name}")
            for r in reasons:
                print(f"  • {r}")
            print(f"\nPDFs: {len(scan['pdfs'])}, Notes: {len(scan['notes'])}, "
                  f"Drafts: {len(scan['drafts'])} ({scan['total_word_count']:,} words)")
        sys.exit(0)

    # Setup
    setup_result = setup_project(
        project_dir, scan, phase,
        doc_type=args.type, lang=args.lang, field=args.field, title=args.title,
    )

    if args.json:
        print_json_report(scan, phase, phase_name, reasons, setup_result)
    else:
        print_report(scan, phase, phase_name, reasons, setup_result)


if __name__ == "__main__":
    main()
