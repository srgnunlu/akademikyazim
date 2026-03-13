#!/usr/bin/env python3
"""
scripts/citation_chain.py — TezAtlas Atıf Zinciri Üreticisi
                              Citation Chain / Intellectual Lineage

notes/*.md dosyalarından en çok referans edilen kavramları tespit eder ve
her kavramın entelektüel soy ağacını oluşturur: kim başlattı → kim sorguladı
→ kim geliştirdi → güncel konsensüs.

Kullanım:
    python3 scripts/citation_chain.py                   # varsayılan
    python3 scripts/citation_chain.py --concept "kavram"
    python3 scripts/citation_chain.py --output CITATION_CHAIN.md

Çıktı: CITATION_CHAIN.md — kavram bazlı entelektüel soy ağacı
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

# ── Patterns ──────────────────────────────────────────────────────────────────

_WORD_PATTERN = re.compile(r"\b[a-zA-ZçğıöşüÇĞİÖŞÜ]{4,}\b")

_STOP_WORDS = {
    "için", "ile", "bir", "olan", "olarak", "ancak", "fakat", "daha", "gibi",
    "this", "that", "with", "from", "have", "been", "their", "they", "will",
    "more", "also", "such", "these", "those", "into", "other", "which",
    "when", "where", "what", "were", "than", "then", "some", "each",
    "veya", "yahut", "yani", "hem", "ise", "ama", "öyle", "böyle",
    "kadar", "sonra", "önce", "üzere", "göre", "karşı", "arasında",
    "araştırma", "çalışma", "research", "study", "studies", "analysis",
    "literature", "review", "paper", "article", "journal", "kaynak",
    "makale", "tablo", "figure", "table", "section", "bölüm",
}

# Stance markers for lineage classification
_FOUNDATIONAL_MARKERS = re.compile(
    r"\b(ortaya koy|ilk kez|öncü|temel atan|kurucusu|kavramını geliştir|"
    r"pioneered?|first proposed|originated?|introduced|foundational|seminal|"
    r"coined|established the concept)\b",
    re.IGNORECASE,
)

_CHALLENGE_MARKERS = re.compile(
    r"\b(eleştir|sorgula|karşı çık|itiraz|revize et|reddet|"
    r"challeng|question|critic|objection|revise|reject|refut|dispute|rebut)\b",
    re.IGNORECASE,
)

_DEVELOPMENT_MARKERS = re.compile(
    r"\b(geliştir|genişlet|uyarla|entegre et|birleştir|rafine et|"
    r"develop|extend|expand|adapt|integrat|combin|refin|build(?:s|ing)?\s+(?:on|upon))\b",
    re.IGNORECASE,
)

_CLAIM_PATTERN = re.compile(
    r"\b(bulgu|sonuç|iddia|göstermektedir|savunmaktadır|"
    r"finds?|shows?|demonstrates?|argues?|claims?|suggests?|concludes?)\b",
    re.IGNORECASE,
)

# Author-year citation patterns: Smith (2020), Yılmaz (2019), etc.
_CITATION_PATTERN = re.compile(
    r"([A-ZÇĞİÖŞÜ][a-zçğıöşü]+(?:\s+(?:ve|and|&|et\s+al\.?))?)\s*\((\d{4})\)"
)


def extract_keywords(text: str, top_n: int = 10) -> list[str]:
    words = _WORD_PATTERN.findall(text.lower())
    freq: dict[str, int] = defaultdict(int)
    for w in words:
        if w not in _STOP_WORDS:
            freq[w] += 1
    return sorted(freq, key=lambda w: -freq[w])[:top_n]


# ── Parsers ───────────────────────────────────────────────────────────────────

def parse_note(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    title = path.stem
    for line in content.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Author + Year
    author = ""
    for line in content.splitlines():
        m = re.match(r"^(?:Yazar|Author)\s*:\s*(.+)", line, re.IGNORECASE)
        if m:
            author = m.group(1).strip()
            break

    year = ""
    ym = re.search(r"\b(19[89]\d|20[0-2]\d)\b", content[:500])
    if ym:
        year = ym.group(1)

    # Extract inline citations
    citations = _CITATION_PATTERN.findall(content)

    text_flat = re.sub(r"\n+", " ", content)
    sentences = re.split(r"(?<=[.!?])\s+", text_flat)

    # Classify sentences by stance
    foundational = []
    challenges = []
    developments = []
    claims = []

    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 20 or len(sent) > 400:
            continue
        if _FOUNDATIONAL_MARKERS.search(sent):
            foundational.append(sent)
        if _CHALLENGE_MARKERS.search(sent):
            challenges.append(sent)
        if _DEVELOPMENT_MARKERS.search(sent):
            developments.append(sent)
        if _CLAIM_PATTERN.search(sent):
            claims.append(sent)

    return {
        "file": path.name,
        "title": title,
        "author": author,
        "year": year,
        "citations": citations,  # list of (author, year)
        "foundational": foundational,
        "challenges": challenges,
        "developments": developments,
        "claims": claims,
        "keywords": extract_keywords(content),
        "content": content,
    }


# ── Analysis ──────────────────────────────────────────────────────────────────

def find_key_concepts(notes: list[dict], top_n: int = 5) -> list[str]:
    """En çok referans edilen kavramları tespit eder."""
    all_text = " ".join(n["content"][:1000] for n in notes)
    return extract_keywords(all_text, top_n)


def build_lineage(
    concept: str,
    notes: list[dict],
) -> dict:
    """Bir kavram için entelektüel soy ağacı oluşturur."""

    # Find notes that discuss this concept
    related_notes = []
    for note in notes:
        if concept in note["keywords"] or concept.lower() in note["content"].lower():
            related_notes.append(note)

    if not related_notes:
        return {"concept": concept, "stages": [], "related_notes": []}

    # Sort by year to establish chronological lineage
    related_notes.sort(key=lambda n: n["year"] or "9999")

    # Classify each related note's role
    stages = []

    for note in related_notes:
        role = "mention"  # default
        evidence = ""

        # Check content near concept mention for stance
        concept_idx = note["content"].lower().find(concept.lower())
        if concept_idx >= 0:
            context = note["content"][max(0, concept_idx - 200):concept_idx + 200]
        else:
            context = note["content"][:500]

        if _FOUNDATIONAL_MARKERS.search(context):
            role = "founder"
            for s in note["foundational"]:
                if concept.lower() in s.lower():
                    evidence = s
                    break
        elif _CHALLENGE_MARKERS.search(context):
            role = "challenger"
            for s in note["challenges"]:
                if concept.lower() in s.lower():
                    evidence = s
                    break
        elif _DEVELOPMENT_MARKERS.search(context):
            role = "developer"
            for s in note["developments"]:
                if concept.lower() in s.lower():
                    evidence = s
                    break

        if not evidence:
            for s in note["claims"]:
                if concept.lower() in s.lower():
                    evidence = s
                    break

        stages.append({
            "file": note["file"],
            "title": note["title"],
            "author": note["author"],
            "year": note["year"],
            "role": role,
            "evidence": evidence,
        })

    # Build cited-by network
    citation_network = []
    all_cited = Counter()
    for note in related_notes:
        for cited_author, cited_year in note["citations"]:
            all_cited[(cited_author, cited_year)] += 1
    # Top cited within this concept's network
    top_cited = all_cited.most_common(5)
    for (auth, yr), count in top_cited:
        citation_network.append({
            "author": auth,
            "year": yr,
            "cited_by_count": count,
        })

    return {
        "concept": concept,
        "stages": stages,
        "citation_network": citation_network,
        "related_notes": related_notes,
    }


# ── Report writer ─────────────────────────────────────────────────────────────

_ROLE_EMOJI = {
    "founder": "🟢",
    "challenger": "🔴",
    "developer": "🔵",
    "mention": "⚪",
}

_ROLE_LABEL = {
    "founder": "Kurucu / Founder",
    "challenger": "Sorgulayan / Challenger",
    "developer": "Geliştiren / Developer",
    "mention": "Bahseden / Mention",
}


def write_report(
    lineages: list[dict],
    notes: list[dict],
    output_path: Path,
) -> None:
    lines = [
        "# Atıf Zinciri / Citation Chain",
        "",
        f"_Oluşturulma: {date.today().isoformat()} — {len(notes)} kaynak analiz edildi_",
        "",
        "> Her kavramın entelektüel soy ağacı: kim başlattı → kim sorguladı → kim geliştirdi",
        "",
        "**Renk kodları:** 🟢 Kurucu | 🔴 Sorgulayan | 🔵 Geliştiren | ⚪ Bahseden",
        "",
        "---",
        "",
    ]

    for lineage in lineages:
        concept = lineage["concept"]
        stages = lineage["stages"]

        lines += [
            f"## Kavram: {concept.title()}",
            "",
        ]

        if not stages:
            lines += [
                "_(Bu kavramla ilgili yeterli veri bulunamadı)_",
                "",
                "---",
                "",
            ]
            continue

        # ASCII tree
        lines.append("```")
        lines.append(f"  {concept.title()}")
        for i, s in enumerate(stages):
            emoji = _ROLE_EMOJI.get(s["role"], "⚪")
            connector = "├──" if i < len(stages) - 1 else "└──"
            year_str = f" ({s['year']})" if s["year"] else ""
            author_str = s["author"] or s["title"][:30]
            lines.append(f"  {connector} {emoji} {author_str}{year_str} [{_ROLE_LABEL[s['role']]}]")
        lines.append("```")
        lines.append("")

        # Detailed entries
        for s in stages:
            emoji = _ROLE_EMOJI.get(s["role"], "⚪")
            label = _ROLE_LABEL.get(s["role"], "—")
            lines += [
                f"**{emoji} {s['author'] or s['title']}** ({s['year'] or '?'}) — {label}",
                f"- Dosya: `{s['file']}`",
            ]
            if s["evidence"]:
                lines.append(f"- > _{s['evidence'][:200]}_")
            lines.append("")

        # Citation network
        if lineage["citation_network"]:
            lines += [
                "**En çok atıf alan (bu kavram ağı içinde):**",
                "",
            ]
            for c in lineage["citation_network"][:3]:
                lines.append(f"- {c['author']} ({c['year']}) — {c['cited_by_count']} atıf")
            lines.append("")

        lines += ["---", ""]

    # Next steps
    lines += [
        "## Sonraki Adımlar",
        "",
        "1. Kurucu (🟢) kaynakları okuyup anladığınızdan emin olun",
        "2. Sorgulayan (🔴) kaynakları ARGUMENTS.md'de karşı görüş olarak kaydedin",
        "3. Geliştiren (🔵) kaynakları sentezinize entegre edin",
        "4. Eksik halkaları `/gaps` ile tespit edin",
        "5. Güncelle: `python3 scripts/citation_chain.py`",
        "",
    ]

    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TezAtlas — Atıf Zinciri Üreticisi"
    )
    parser.add_argument(
        "--notes", metavar="DIR", default="notes",
        help="Not dizini (varsayılan: ./notes/)",
    )
    parser.add_argument(
        "--output", metavar="FILE", default="CITATION_CHAIN.md",
        help="Çıktı dosyası (varsayılan: CITATION_CHAIN.md)",
    )
    parser.add_argument(
        "--concept", metavar="KEYWORD",
        help="Belirli bir kavram için zincir oluştur",
    )
    parser.add_argument(
        "--top", metavar="N", type=int, default=5,
        help="En çok referans edilen N kavram (varsayılan: 5)",
    )
    parser.add_argument(
        "--project-dir", metavar="DIR", default=".",
        help="Proje kök dizini",
    )
    args = parser.parse_args()

    project_dir = Path(args.project_dir).resolve()
    notes_dir = project_dir / args.notes
    output_path = project_dir / args.output

    if not notes_dir.is_dir():
        print("⚠️  Not dizini bulunamadı:", notes_dir)
        sys.exit(0)

    note_files = sorted(notes_dir.glob("*.md"))
    if not note_files:
        print("ℹ️  notes/ dizininde hiç .md dosyası yok.")
        sys.exit(0)

    print(f"📝 {len(note_files)} not dosyası taranıyor...")
    notes = []
    for path in note_files:
        note = parse_note(path)
        notes.append(note)
        cit_count = len(note["citations"])
        print(f"   • {path.name}: {cit_count} satır içi atıf")

    # Determine concepts to trace
    if args.concept:
        concepts = [args.concept.lower()]
        print(f"\n🔍 Kavram zinciri: {args.concept}")
    else:
        concepts = find_key_concepts(notes, args.top)
        print(f"\n🔍 En çok referans edilen {len(concepts)} kavram: {', '.join(concepts)}")

    print("\n🔗 Atıf zincirleri oluşturuluyor...")
    lineages = []
    for concept in concepts:
        lineage = build_lineage(concept, notes)
        lineages.append(lineage)
        stage_count = len(lineage["stages"])
        print(f"   • {concept}: {stage_count} aşama")

    write_report(lineages, notes, output_path)

    print()
    print(f"{'─' * 50}")
    print(f"  İzlenen kavram       : {len(concepts)}")
    total_stages = sum(len(l["stages"]) for l in lineages)
    print(f"  Toplam zincir halkası: {total_stages}")
    print(f"  Rapor                : {output_path.name}")
    print(f"{'─' * 50}")
    print()
    print("✅ CITATION_CHAIN.md oluşturuldu.")


if __name__ == "__main__":
    main()
