#!/usr/bin/env python3
"""
Pre-commit hook: block PDF files from being committed to sources/.
PDFs are gitignored by default; this catches gitignore bypasses.
"""
import sys


def main():
    files = sys.argv[1:]
    if not files:
        sys.exit(0)

    print("PDF files detected in sources/ — these should NOT be committed:")
    for f in files:
        print(f"  ✗ {f}")
    print()
    print("PDFs are excluded via .gitignore to protect research data privacy.")
    print("If you intentionally want to track a PDF, use:")
    print("  git add --force <file>")
    print("But this is strongly discouraged — keep PDFs local only.")
    sys.exit(1)


if __name__ == "__main__":
    main()
