#!/usr/bin/env python3
"""Generate a simple GitHub Pages homepage from README.md."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
PAGES_PATH = ROOT / "docs" / "index.md"
REPO_URL = "https://github.com/ideas-no996/awesome-android-keyboards"


def github_links(markdown: str) -> str:
    replacements = {
        "(LICENSE)": f"({REPO_URL}/blob/main/LICENSE)",
        "(data/keyboards.yml)": f"({REPO_URL}/blob/main/data/keyboards.yml)",
        "(CONTRIBUTING.md)": f"({REPO_URL}/blob/main/CONTRIBUTING.md)",
        "(docs/evaluation-criteria.md)": f"({REPO_URL}/blob/main/docs/evaluation-criteria.md)",
    }
    for old, new in replacements.items():
        markdown = markdown.replace(old, new)
    return markdown


def simplify_for_pages(markdown: str) -> str:
    markdown = markdown.split("\n## Detailed Entries\n", 1)[0].rstrip()
    markdown = markdown.replace("# Awesome Android Keyboards\n\n", "", 1)
    markdown = markdown.replace("- [Detailed Entries](#detailed-entries)\n", "")
    markdown = markdown.replace("- [Maintenance](#maintenance)\n", "")
    markdown = markdown.replace(
        "The tables stay intentionally compact. Full evaluation fields live in `data/keyboards.yml` and the collapsible detail blocks below.",
        "The tables stay intentionally compact. Full evaluation fields live in `data/keyboards.yml`; the complete README contains the longer detail blocks.",
    )
    return markdown


def main() -> int:
    readme = README_PATH.read_text(encoding="utf-8")
    readme = simplify_for_pages(readme)
    readme = github_links(readme)
    front_matter = """---
layout: default
title: Awesome Android Keyboards
description: A curated Android keyboard and Android IME ecosystem index.
---

"""
    notice = (
        "> This page is generated from the repository README. "
        "Edit `data/keyboards.yml`, then run `python scripts/generate_readme.py` "
        "and `python scripts/generate_pages.py`.\n\n"
    )
    footer = (
        "\n\n## More\n\n"
        f"- [View the full README and detailed entries]({REPO_URL})\n"
        f"- [Contribute a keyboard or correction]({REPO_URL}/blob/main/CONTRIBUTING.md)\n"
    )
    PAGES_PATH.write_text(front_matter + notice + readme + footer, encoding="utf-8")
    print(f"Generated {PAGES_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
