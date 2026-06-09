#!/usr/bin/env python3
"""Generate README.md from data/keyboards.yml."""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "keyboards.yml"
README_PATH = ROOT / "README.md"
REPO = "ideas-no996/awesome-android-keyboards"

CATEGORIES = [
    "Commercial Keyboards",
    "Open Source Keyboards",
    "Rime-based Keyboards",
    "Privacy-focused Keyboards",
    "AI-assisted Keyboards",
    "Developer / Hacker Keyboards",
    "Theme and Customization Resources",
    "Android IME Development Resources",
]


def value(text: Any) -> str:
    if text is True:
        return "Yes"
    if text is False:
        return "No"
    if text is None:
        return "N/A"
    if isinstance(text, list):
        return ", ".join(str(item) for item in text) if text else "N/A"
    return str(text)


def link(label: str, url: str | None) -> str:
    return f"[{label}]({url})" if url else "N/A"


def stars(item: dict[str, Any]) -> str:
    count = item.get("stars")
    if count is None:
        return "N/A"
    return f"{count:,}"


def date_only(text: str | None) -> str:
    if not text:
        return "N/A"
    return text[:10]


def anchors(title: str) -> str:
    return title.lower().replace("/", "").replace(" ", "-")


def badges(last_updated: str) -> list[str]:
    badge_date = last_updated.replace("-", "--")
    return [
        "[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)",
        "[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](LICENSE)",
        f"![Last Updated](https://img.shields.io/badge/last%20updated-{badge_date}-blue)",
        f"[![GitHub Stars](https://img.shields.io/github/stars/{REPO}?style=social)](https://github.com/{REPO}/stargazers)",
    ]


def recommendations(items: list[dict[str, Any]]) -> list[str]:
    by_name = {item["name"]: item for item in items}
    picks = [
        ("普通用户推荐", ["Gboard", "Microsoft SwiftKey", "HeliBoard"]),
        ("隐私优先推荐", ["HeliBoard", "FUTO Keyboard", "FlorisBoard", "Simple Keyboard"]),
        ("中文输入推荐", ["Trime", "Fcitx5 for Android", "WeChat Keyboard", "Sogou IME"]),
        ("适合二次开发推荐", ["FlorisBoard", "HeliBoard", "Simple Keyboard", "Unexpected Keyboard"]),
        ("适合 iOS-like 主题改造推荐", ["FlorisBoard", "HeliBoard", "AnySoftKeyboard", "Trime"]),
        ("适合 Glassmorphism 主题改造推荐", ["FlorisBoard", "HeliBoard", "FUTO Keyboard", "Trime"]),
    ]
    lines = []
    for label, names in picks:
        linked = []
        for name in names:
            item = by_name.get(name)
            if item:
                target = item.get("repo_url") or item.get("website_url") or item.get("play_store_url")
                linked.append(link(name, target))
        lines.append(f"- **{label}:** " + ", ".join(linked))
    return lines


def category_table(items: list[dict[str, Any]]) -> list[str]:
    lines = [
        "| Name | Source | License | Stars | Signals | Short review |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for item in sorted(items, key=lambda row: row["name"].lower()):
        source = item.get("repo_url") or item.get("website_url") or item.get("play_store_url")
        signals = (
            f"Chinese: {value(item.get('chinese_support'))}<br>"
            f"Theme: {value(item.get('theme_system'))}<br>"
            f"Offline: {value(item.get('offline_support'))}<br>"
            f"Privacy: {value(item.get('privacy_level'))}"
        )
        lines.append(
            "| {name} | {source} | {license} | {stars} | {signals} | {review} |".format(
                name=item["name"],
                source=link(item["name"], source),
                license=value(item.get("license")),
                stars=stars(item),
                signals=signals,
                review=value(item.get("recommendation_reason")),
            )
        )
    return lines


def detail_block(item: dict[str, Any]) -> list[str]:
    source_links = [
        link("Repository", item.get("repo_url")),
        link("Website", item.get("website_url")),
        link("F-Droid", item.get("fdroid_url")),
        link("Play Store", item.get("play_store_url")),
    ]
    source_links = [entry for entry in source_links if entry != "N/A"]
    sources = [link(f"Source {index + 1}", url) for index, url in enumerate(item.get("source_urls") or [])]
    return [
        f"<details>",
        f"<summary><strong>{item['name']}</strong> details</summary>",
        "",
        f"- **Name:** {item['name']}",
        f"- **Repository / Website:** {'; '.join(source_links) if source_links else 'N/A'}",
        f"- **License:** {value(item.get('license'))}",
        f"- **Stars:** {stars(item)}",
        f"- **Last commit:** {date_only(item.get('last_commit'))}",
        f"- **Last release:** {date_only(item.get('last_release'))}",
        f"- **Tech stack:** {value(item.get('tech_stack'))}",
        f"- **Chinese support:** {value(item.get('chinese_support'))}",
        f"- **Theme system:** {value(item.get('theme_system'))}",
        f"- **Offline support:** {value(item.get('offline_support'))}",
        f"- **Privacy:** {value(item.get('privacy_level'))}",
        f"- **Development feasibility:** {value(item.get('development_feasibility'))}",
        f"- **Recommended use case:** {value(item.get('recommendation_reason'))}",
        f"- **Short review:** {value(item.get('notes'))}",
        f"- **Sources:** {'; '.join(sources) if sources else 'N/A'}",
        f"- **Last verified:** {value(item.get('last_verified'))}",
        "",
        "</details>",
    ]


def main() -> int:
    data = yaml.safe_load(DATA_PATH.read_text(encoding="utf-8"))
    items = data["keyboards"]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        grouped[item["category"]].append(item)
        for category in item.get("secondary_categories") or []:
            grouped[category].append(item)

    now = datetime.now(timezone.utc).date().isoformat()
    last_updated = value(data.get("metadata", {}).get("last_updated") or now)
    lines = [
        "# Awesome Android Keyboards",
        "",
        " ".join(badges(last_updated)),
        "",
        "> A curated, maintainable map of Android keyboard and input method ecosystems.",
        "",
        "Awesome Android Keyboards is a professional index for the android keyboard ecosystem: Android IME apps, input method engines, privacy keyboard choices, open-source keyboard projects, Rime and Trime front-ends, F-Droid packages, commercial keyboards, developer keyboards, theme systems, and Android InputMethodService resources. It is built for users comparing daily keyboards, developers studying Android IME architecture, Chinese input method users evaluating Rime-based workflows, and maintainers looking for realistic open-source keyboard bases.",
        "",
        "The list is intentionally conservative. It does not rank projects by hype, copy marketing text, or treat closed-source claims as implementation facts. Each entry is backed by structured data in YAML, source links, maintenance notes, privacy/network signals, theme suitability, Chinese input support, and a short original review.",
        "",
        f"Data file: [`data/keyboards.yml`](data/keyboards.yml). Generated from structured data on {now}.",
        "",
        "## Table of Contents",
        "",
        "- [Quick Recommendations](#quick-recommendations)",
        "- [Categories](#categories)",
    ]
    for category in CATEGORIES:
        lines.append(f"  - [{category}](#{anchors(category)})")
    lines.extend(
        [
            "- [Detailed Entries](#detailed-entries)",
            "- [Maintenance](#maintenance)",
            "",
            "## Quick Recommendations",
            "",
        ]
    )
    lines.extend(recommendations(items))
    lines.extend(
        [
            "",
            "## Categories",
            "",
            "The tables stay intentionally compact. Full evaluation fields live in `data/keyboards.yml` and the collapsible detail blocks below.",
            "",
        ]
    )

    for category in CATEGORIES:
        lines.extend([f"### {category}", ""])
        entries = grouped.get(category, [])
        if entries:
            lines.extend(category_table(entries))
        else:
            lines.append("_No entries yet. Contributions are welcome when they include sources and a recommendation reason._")
        lines.append("")

    lines.extend(["## Detailed Entries", ""])
    for category in CATEGORIES:
        entries = grouped.get(category, [])
        if not entries:
            continue
        lines.extend([f"### {category} Entry Details", ""])
        for item in sorted(entries, key=lambda row: row["name"].lower()):
            lines.extend(detail_block(item))
            lines.append("")

    lines.extend(
        [
            "## Maintenance",
            "",
            "- Update GitHub stats with `python scripts/update_github_stats.py`.",
            "- Regenerate this README with `python scripts/generate_readme.py`.",
            "- Use `GITHUB_TOKEN` for higher GitHub API limits; never commit tokens.",
            "- See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/evaluation-criteria.md`](docs/evaluation-criteria.md) before adding entries.",
            "",
            "## License",
            "",
            "Released under CC0-1.0. See [`LICENSE`](LICENSE).",
            "",
        ]
    )

    README_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated {README_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
