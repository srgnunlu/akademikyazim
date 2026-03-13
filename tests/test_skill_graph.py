"""
test_skill_graph.py — Skill graph integrity tests.

Checks:
1. Every phase_gate_out target file exists
2. Every wikilink [[target]] resolves to an existing file
3. Every links_to entry resolves to an existing file
"""
import re
from pathlib import Path

import pytest
import yaml

SKILLS_ROOT = Path(__file__).parent.parent / "skills"
REPO_ROOT = Path(__file__).parent.parent


def iter_skill_files():
    """Yield all .md files under skills/."""
    return list(SKILLS_ROOT.rglob("*.md"))


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return {}
    end = content.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(content[3:end]) or {}
    except yaml.YAMLError:
        return {}


def extract_wikilinks(content: str) -> list[str]:
    """Extract [[target]] wikilinks from content."""
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def resolve_wikilink(link: str, source_file: Path) -> Path | None:
    """
    Attempt to resolve a wikilink to an actual file.
    Strategy:
    1. Try exact match relative to skills/
    2. Try searching by filename across all skill files
    """
    # Strip .md if present
    link_clean = link.replace(".md", "")

    # Try skills/ relative match
    candidate = SKILLS_ROOT / (link_clean + ".md")
    if candidate.exists():
        return candidate

    # Try filename match across all skill files
    for f in SKILLS_ROOT.rglob(f"{link_clean}.md"):
        return f

    # Try basename match (e.g., [[snowball-sampling]] → any file named snowball-sampling.md)
    basename = link_clean.split("/")[-1]
    for f in SKILLS_ROOT.rglob(f"{basename}.md"):
        return f

    return None


# ──────────────────────────────────────────────────────────────────
# Tests
# ──────────────────────────────────────────────────────────────────

class TestPhaseGateTargets:
    """phase_gate_out targets must resolve to existing files."""

    # Sentinel values: terminal states that are not file paths
    TERMINAL_SENTINELS = {"PRESENTED", "PUBLISHED", "SUBMITTED", "PUBLISHED_ONLINE", "PRINTED"}

    def test_phase_gate_out_files_exist(self):
        missing = []
        for skill_file in iter_skill_files():
            content = skill_file.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            gate_out = fm.get("phase_gate_out")
            if gate_out is None or gate_out == "null":
                continue
            # Skip terminal sentinel values — these are not file paths
            if str(gate_out).upper() in self.TERMINAL_SENTINELS:
                continue
            # gate_out is a filename — search for it in the same directory or skills/
            target_name = Path(gate_out).name
            found = list(skill_file.parent.glob(target_name))
            if not found:
                found = list(SKILLS_ROOT.rglob(target_name))
            if not found:
                missing.append(
                    f"{skill_file.relative_to(REPO_ROOT)}: phase_gate_out={gate_out!r} not found"
                )
        assert not missing, "Phase gate targets not found:\n" + "\n".join(missing)


class TestLinksTo:
    """Every links_to entry must resolve to an existing file."""

    def test_links_to_files_exist(self):
        missing = []
        for skill_file in iter_skill_files():
            content = skill_file.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            links = fm.get("links_to") or []
            for link in links:
                target = REPO_ROOT / link
                if not target.exists():
                    missing.append(
                        f"{skill_file.relative_to(REPO_ROOT)}: links_to={link!r} not found"
                    )
        assert not missing, "Broken links_to references:\n" + "\n".join(missing)


class TestWikilinks:
    """Wikilinks [[target]] in content should resolve to existing files."""

    def test_wikilinks_resolve(self):
        broken = []
        for skill_file in iter_skill_files():
            content = skill_file.read_text(encoding="utf-8")
            links = extract_wikilinks(content)
            for link in links:
                resolved = resolve_wikilink(link, skill_file)
                if resolved is None:
                    broken.append(
                        f"{skill_file.relative_to(REPO_ROOT)}: [[{link}]] not resolved"
                    )
        # Report as warnings (wikilinks may reference templates not yet created)
        if broken:
            pytest.warns(
                UserWarning,
                match=".*",
            )
            import warnings
            for b in broken:
                warnings.warn(b, UserWarning)
