#!/usr/bin/env python3
"""
Pre-commit hook: validate frontmatter schema for skill node .md files.
Checks required fields per node_type. Exits non-zero on failure.
"""
import sys
import re
import yaml

REQUIRED_BY_NODE_TYPE = {
    "core": ["title", "node_type", "description", "tags", "language", "version"],
    "phase": ["title", "node_type", "description", "tags", "language", "version"],
    "phase-fork": ["title", "node_type", "description", "tags", "language", "version"],
    "technique": ["title", "node_type", "description", "tags", "language"],
    "template": ["title", "node_type", "description", "tags", "language"],
    "tooling": ["title", "node_type", "description", "tags", "language"],
    "foundation": ["title", "node_type", "description", "tags", "language", "version"],
    "moc": ["title", "node_type", "description", "tags", "language"],
}
ALL_REQUIRED = ["title", "node_type", "description", "tags", "language"]
VALID_LANGUAGES = {"bilingual", "tr", "en", "tr+en"}
VALID_NODE_TYPES = set(REQUIRED_BY_NODE_TYPE.keys())


def extract_frontmatter(content: str) -> dict | None:
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return None


def check_file(path: str) -> list[str]:
    errors = []
    try:
        content = open(path, encoding="utf-8").read()
    except OSError as e:
        return [f"{path}: cannot read — {e}"]

    fm = extract_frontmatter(content)
    if fm is None:
        return [f"{path}: missing or invalid YAML frontmatter"]

    # Check all required fields
    for field in ALL_REQUIRED:
        if field not in fm or fm[field] is None:
            errors.append(f"{path}: missing required field '{field}'")

    node_type = fm.get("node_type", "")
    if node_type and node_type not in VALID_NODE_TYPES:
        errors.append(
            f"{path}: unknown node_type '{node_type}' "
            f"(valid: {', '.join(sorted(VALID_NODE_TYPES))})"
        )
    elif node_type in REQUIRED_BY_NODE_TYPE:
        for field in REQUIRED_BY_NODE_TYPE[node_type]:
            if field not in fm or fm[field] is None:
                errors.append(
                    f"{path}: node_type='{node_type}' requires field '{field}'"
                )

    lang = fm.get("language", "")
    if lang and lang not in VALID_LANGUAGES:
        errors.append(
            f"{path}: invalid language '{lang}' "
            f"(valid: {', '.join(sorted(VALID_LANGUAGES))})"
        )

    tags = fm.get("tags", None)
    if tags is not None and not isinstance(tags, list):
        errors.append(f"{path}: 'tags' must be a YAML list")

    return errors


def main():
    files = sys.argv[1:]
    if not files:
        print("check_frontmatter: no files passed")
        sys.exit(0)

    all_errors = []
    for path in files:
        all_errors.extend(check_file(path))

    if all_errors:
        print("Frontmatter validation failed:")
        for err in all_errors:
            print(f"  ✗ {err}")
        sys.exit(1)

    print(f"Frontmatter OK ({len(files)} file(s))")
    sys.exit(0)


if __name__ == "__main__":
    main()
