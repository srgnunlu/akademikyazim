"""
core/literature_intel.py — TezAtlas Literatür Zekası Katmanı
                            Literature Intelligence Layer

Proaktif kaynak ilişkilendirme, argüman uyarıları ve bölüm bazlı analiz sunar.
Yazma fazlarında (Phase 5-6) aktif olur.

Kullanım:
    from core.literature_intel import LiteratureIntel
    intel = LiteratureIntel(project_dir)
    suggestions = intel.analyze_paragraph(text)
    review = intel.review_for_section(draft_text, section_type)
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

# ── Shared patterns ───────────────────────────────────────────────────────────

_WORD_PATTERN = re.compile(r"\b[a-zA-ZçğıöşüÇĞİÖŞÜ]{4,}\b")

_STOP_WORDS = {
    "için", "ile", "bir", "olan", "olarak", "ancak", "fakat", "daha", "gibi",
    "this", "that", "with", "from", "have", "been", "their", "they", "will",
    "more", "also", "such", "these", "those", "into", "other", "which",
    "when", "where", "what", "were", "than", "then", "some", "each",
    "veya", "yahut", "yani", "hem", "ise", "ama", "öyle", "böyle",
    "kadar", "sonra", "önce", "üzere", "göre", "karşı", "arasında",
}

_CLAIM_PATTERN = re.compile(
    r"\b(bulgu|sonuç|iddia|göstermektedir|savunmaktadır|kanıtlamaktadır|"
    r"finds?|shows?|demonstrates?|argues?|claims?|suggests?|concludes?|"
    r"proves?|reveals?|confirms?)\b",
    re.IGNORECASE,
)

_NEGATION_PATTERN = re.compile(
    r"\b(değil|aksine|karşın|rağmen|oysa|ancak|fakat|"
    r"not|no|contrary|despite|however|although|whereas|in contrast)\b",
    re.IGNORECASE,
)


def _extract_keywords(text: str, top_n: int = 10) -> list[str]:
    words = _WORD_PATTERN.findall(text.lower())
    freq: dict[str, int] = defaultdict(int)
    for w in words:
        if w not in _STOP_WORDS:
            freq[w] += 1
    return sorted(freq, key=lambda w: -freq[w])[:top_n]


# ── Section type detection ────────────────────────────────────────────────────

SECTION_TYPES = {
    "intro": {
        "names_tr": ["giris", "giriş", "giris_bolumu", "introduction", "intro"],
        "names_en": ["introduction", "intro", "background"],
        "keywords_tr": ["araştırma sorusu", "amaç", "kapsam", "önem", "motivasyon"],
        "keywords_en": ["research question", "aim", "scope", "significance", "motivation"],
    },
    "literature": {
        "names_tr": ["literatur", "literatür", "lit_tarama", "kaynak_taramasi"],
        "names_en": ["literature", "lit_review", "literature_review", "related_work"],
        "keywords_tr": ["literatür taraması", "kaynak incelemesi", "mevcut çalışmalar"],
        "keywords_en": ["literature review", "related work", "prior research", "existing studies"],
    },
    "method": {
        "names_tr": ["yontem", "yöntem", "metodoloji", "arastirma_yontemi"],
        "names_en": ["method", "methodology", "research_design", "methods"],
        "keywords_tr": ["yöntem", "örneklem", "veri toplama", "analiz yöntemi"],
        "keywords_en": ["method", "sample", "data collection", "research design"],
    },
    "results": {
        "names_tr": ["bulgular", "sonuclar", "sonuçlar", "veriler"],
        "names_en": ["results", "findings", "data", "analysis"],
        "keywords_tr": ["bulgular", "tablo", "grafik", "istatistik", "analiz sonucu"],
        "keywords_en": ["results", "table", "figure", "statistic", "analysis"],
    },
    "discussion": {
        "names_tr": ["tartisma", "tartışma", "degerlendirme", "değerlendirme"],
        "names_en": ["discussion", "interpretation", "implications"],
        "keywords_tr": ["tartışma", "yorum", "karşılaştırma", "sınırlılık"],
        "keywords_en": ["discussion", "interpretation", "comparison", "limitation"],
    },
    "conclusion": {
        "names_tr": ["sonuc", "sonuç", "sonuc_ve_oneriler"],
        "names_en": ["conclusion", "conclusions", "summary"],
        "keywords_tr": ["sonuç", "öneri", "katkı", "gelecek araştırma"],
        "keywords_en": ["conclusion", "recommendation", "contribution", "future research"],
    },
}

# Section-specific recommended tools
SECTION_TOOLS = {
    "intro": ["/so-what", "/knowledge-map"],
    "literature": ["/intake", "/contradictions", "/citation-chain", "/gaps"],
    "method": ["/method-audit"],
    "results": [],
    "discussion": ["/assumptions", "/knowledge-map", "/devil-advocate"],
    "conclusion": ["/so-what", "/synthesize"],
}

# Section-specific checks
SECTION_CHECKS = {
    "intro": ["rq_clarity", "scope_control"],
    "literature": ["coverage_sufficiency", "bias_check"],
    "method": ["internal_consistency", "validity"],
    "results": ["overclaiming_check"],
    "discussion": ["argument_integrity", "limitations"],
    "conclusion": ["generalization_check", "contribution_clarity"],
}


def detect_section_type(filepath: Path | None = None, content: str = "") -> str | None:
    """
    Dosya adı ve içerikten bölüm tipini algılar.

    Returns: section type key or None if undetermined.
    """
    # 1. Filename detection
    if filepath:
        stem = filepath.stem.lower().replace("-", "_").replace(" ", "_")
        for section_type, info in SECTION_TYPES.items():
            all_names = info["names_tr"] + info["names_en"]
            for name in all_names:
                if name in stem:
                    return section_type

    # 2. Content-based detection
    if content:
        content_lower = content[:2000].lower()
        scores: dict[str, int] = defaultdict(int)

        for section_type, info in SECTION_TYPES.items():
            for kw in info["keywords_tr"] + info["keywords_en"]:
                if kw.lower() in content_lower:
                    scores[section_type] += 1

        if scores:
            best = max(scores, key=lambda k: scores[k])
            if scores[best] >= 2:
                return best

    return None


# ── Literature Intelligence Engine ────────────────────────────────────────────

class NoteIndex:
    """In-memory index of all notes for fast matching."""

    def __init__(self, notes_dir: Path):
        self.notes: list[dict] = []
        self._keyword_index: dict[str, list[int]] = defaultdict(list)
        self._load(notes_dir)

    def _load(self, notes_dir: Path) -> None:
        if not notes_dir.is_dir():
            return
        for i, path in enumerate(sorted(notes_dir.glob("*.md"))):
            content = path.read_text(encoding="utf-8")
            title = path.stem
            for line in content.splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

            # Extract DOI
            doi = ""
            doi_match = re.search(r"10\.\d{4,9}/\S+", content)
            if doi_match:
                doi = doi_match.group(0).rstrip(".,;)")

            # Extract claims
            text_flat = re.sub(r"\n+", " ", content)
            sentences = re.split(r"(?<=[.!?])\s+", text_flat)
            claims = [
                s.strip() for s in sentences
                if 20 < len(s.strip()) < 400 and _CLAIM_PATTERN.search(s)
            ]

            keywords = _extract_keywords(content)
            note = {
                "index": i,
                "file": path.name,
                "title": title,
                "doi": doi,
                "claims": claims,
                "keywords": keywords,
                "content": content,
            }
            self.notes.append(note)

            # Build keyword index
            for kw in keywords:
                self._keyword_index[kw].append(i)

    def find_related(self, text: str, top_n: int = 5) -> list[dict]:
        """Metinle en ilgili notları bulur."""
        keywords = _extract_keywords(text, 8)
        scores: dict[int, int] = defaultdict(int)

        for kw in keywords:
            for idx in self._keyword_index.get(kw, []):
                scores[idx] += 1

        ranked = sorted(scores.items(), key=lambda x: -x[1])
        results = []
        for idx, score in ranked[:top_n]:
            if score >= 2:  # At least 2 keyword overlap
                note = self.notes[idx]
                results.append({
                    **note,
                    "relevance_score": score,
                })
        return results

    def find_contradicting(self, text: str) -> list[dict]:
        """Metinle çelişen kaynakları bulur."""
        related = self.find_related(text, top_n=10)
        text_negated = bool(_NEGATION_PATTERN.search(text))
        contradictions = []

        text_kw = set(_extract_keywords(text, 8))

        for note in related:
            for claim in note["claims"][:5]:
                claim_negated = bool(_NEGATION_PATTERN.search(claim))
                claim_kw = set(_extract_keywords(claim, 5))
                shared = text_kw & claim_kw

                if len(shared) >= 2 and text_negated != claim_negated:
                    contradictions.append({
                        "source": note["file"],
                        "title": note["title"],
                        "claim": claim,
                        "shared_keywords": sorted(shared),
                    })
                    break

        return contradictions


class ArgumentIndex:
    """In-memory index of ARGUMENTS.md arguments."""

    def __init__(self, project_dir: Path):
        self.arguments: list[dict] = []
        self._load(project_dir / "ARGUMENTS.md")

    def _load(self, path: Path) -> None:
        if not path.exists():
            return
        content = path.read_text(encoding="utf-8")
        for line in content.splitlines():
            line = line.strip()
            if not line.startswith("|") or "---" in line:
                continue
            parts = [p.strip() for p in line.strip("|").split("|")]
            if len(parts) < 2:
                continue
            first = parts[0]
            if re.match(r"^(#|No|Num|İddia|Argüman|Claim|Argument)\b", first, re.IGNORECASE):
                continue
            claim = parts[1] if len(parts) > 1 else parts[0]
            # Skip header-like rows
            if re.match(r"^(İddia|Argüman|Claim|Argument|Kaynak|Source)\b", claim, re.IGNORECASE):
                continue
            if claim and len(claim) >= 5:
                self.arguments.append({
                    "index": len(self.arguments) + 1,
                    "claim": claim,
                    "keywords": _extract_keywords(claim),
                })

    def find_matching(self, text: str) -> list[dict]:
        """Metinle eşleşen argümanları bulur."""
        text_kw = set(_extract_keywords(text, 8))
        matches = []
        for arg in self.arguments:
            overlap = text_kw & set(arg["keywords"])
            if len(overlap) >= 2:
                matches.append({
                    **arg,
                    "overlap": sorted(overlap),
                })
        return matches


class LiteratureIntel:
    """
    Literatür Zekası motoru.

    Yazma fazlarında paragraf bazında kaynak önerisi, çelişki uyarısı
    ve argüman eşleştirmesi sağlar.
    """

    def __init__(self, project_dir: Path):
        self.project_dir = project_dir
        self.note_index = NoteIndex(project_dir / "notes")
        self.arg_index = ArgumentIndex(project_dir)

    def analyze_paragraph(self, text: str) -> dict:
        """
        Bir paragraf için literatür zekası analizi.

        Returns:
            {
                "related_sources": [...],
                "contradictions": [...],
                "matching_arguments": [...],
                "unsupported_claims": [...],
                "suggestions": [...],
            }
        """
        related = self.note_index.find_related(text, top_n=5)
        contradictions = self.note_index.find_contradicting(text)
        matching_args = self.arg_index.find_matching(text)

        # Check for unsupported claims
        sentences = re.split(r"(?<=[.!?])\s+", text)
        unsupported = []
        for sent in sentences:
            sent = sent.strip()
            if len(sent) < 20:
                continue
            if _CLAIM_PATTERN.search(sent):
                # Check if any source supports this claim
                claim_related = self.note_index.find_related(sent, top_n=3)
                if not claim_related:
                    unsupported.append(sent)

        # Generate suggestions
        suggestions = []
        if related:
            top = related[0]
            suggestions.append(
                f"Bu yazınla en ilgili kaynak: {top['title']} ({top['file']})"
            )
        if contradictions:
            c = contradictions[0]
            suggestions.append(
                f"⚠️ Dikkat: {c['title']} bu iddiaya karşı görüş içeriyor"
            )
        if unsupported:
            suggestions.append(
                f"⚠️ {len(unsupported)} iddia cümlesi kaynak desteği bulunamadı"
            )
        if matching_args:
            args_str = ", ".join(f"#{a['index']}" for a in matching_args[:3])
            suggestions.append(
                f"Bu paragraf şu argümanlarla ilişkili: {args_str}"
            )

        return {
            "related_sources": related,
            "contradictions": contradictions,
            "matching_arguments": matching_args,
            "unsupported_claims": unsupported,
            "suggestions": suggestions,
        }

    def review_for_section(
        self,
        draft_text: str,
        section_type: str | None = None,
        filepath: Path | None = None,
    ) -> dict:
        """
        Bölüm bazlı literatür uyumluluğu incelemesi.

        Returns:
            {
                "section_type": str,
                "paragraph_analyses": [...],
                "overall_coverage": float,
                "contradictions": [...],
                "unsupported_claims": [...],
                "recommended_tools": [...],
                "checks": [...],
            }
        """
        # Detect section type
        if not section_type:
            section_type = detect_section_type(filepath, draft_text)

        # Analyze each paragraph
        paragraphs = [p.strip() for p in draft_text.split("\n\n") if p.strip() and len(p.strip()) > 30]
        paragraph_analyses = []
        all_contradictions = []
        all_unsupported = []

        for para in paragraphs:
            analysis = self.analyze_paragraph(para)
            paragraph_analyses.append(analysis)
            all_contradictions.extend(analysis["contradictions"])
            all_unsupported.extend(analysis["unsupported_claims"])

        # Overall coverage: what % of paragraphs have related sources?
        covered = sum(1 for a in paragraph_analyses if a["related_sources"])
        overall_coverage = covered / max(1, len(paragraph_analyses))

        # Section-specific tools and checks
        recommended_tools = SECTION_TOOLS.get(section_type or "", [])
        checks = SECTION_CHECKS.get(section_type or "", [])

        return {
            "section_type": section_type,
            "paragraph_analyses": paragraph_analyses,
            "overall_coverage": overall_coverage,
            "contradictions": all_contradictions,
            "unsupported_claims": all_unsupported,
            "recommended_tools": recommended_tools,
            "checks": checks,
        }
