#!/usr/bin/env python3
"""Update GitHub-derived fields in data/keyboards.yml.

The script uses GITHUB_TOKEN when present and also works unauthenticated for
small, low-frequency runs. It only changes GitHub-backed projects.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "keyboards.yml"
GITHUB_RE = re.compile(r"^https://github\.com/([^/]+)/([^/#?]+)")
RATE_LIMITED = False


def github_json(path: str, token: str | None) -> dict[str, Any] | list[Any] | None:
    global RATE_LIMITED
    if RATE_LIMITED:
        return None

    url = f"https://api.github.com{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-android-keyboards",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            remaining = response.headers.get("X-RateLimit-Remaining")
            if remaining == "0":
                reset = response.headers.get("X-RateLimit-Reset")
                print(f"GitHub rate limit exhausted; reset={reset}", file=sys.stderr)
            return yaml.safe_load(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        if exc.code == 403:
            RATE_LIMITED = True
            print(
                "GitHub API rate limit reached; stopping this update early. "
                "Set GITHUB_TOKEN for higher limits.",
                file=sys.stderr,
            )
            return None
        if exc.code == 404:
            return None
        print(f"GitHub API error {exc.code} for {url}: {exc.reason}", file=sys.stderr)
        return None
    except urllib.error.URLError as exc:
        print(f"Network error for {url}: {exc.reason}", file=sys.stderr)
        return None


def repo_slug(repo_url: str | None) -> tuple[str, str] | None:
    if not repo_url:
        return None
    match = GITHUB_RE.match(repo_url)
    if not match:
        return None
    owner, repo = match.groups()
    return owner, repo.removesuffix(".git")


def latest_release(owner: str, repo: str, token: str | None) -> str | None:
    release = github_json(f"/repos/{owner}/{repo}/releases/latest", token)
    if isinstance(release, dict):
        return release.get("published_at") or release.get("created_at")
    return None


def latest_commit(owner: str, repo: str, branch: str, token: str | None) -> str | None:
    commits = github_json(f"/repos/{owner}/{repo}/commits?sha={branch}&per_page=1", token)
    if isinstance(commits, list) and commits:
        commit = commits[0].get("commit", {})
        return commit.get("committer", {}).get("date") or commit.get("author", {}).get("date")
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=DATA_PATH)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--sleep", type=float, default=0.2, help="Delay between repositories.")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    data = yaml.safe_load(args.data.read_text(encoding="utf-8"))
    updated = 0

    for item in data.get("keyboards", []):
        if RATE_LIMITED:
            break
        slug = repo_slug(item.get("repo_url"))
        if not slug:
            continue
        owner, repo = slug
        repo_data = github_json(f"/repos/{owner}/{repo}", token)
        if not isinstance(repo_data, dict):
            continue

        default_branch = repo_data.get("default_branch") or "main"
        item["stars"] = repo_data.get("stargazers_count")
        item["forks"] = repo_data.get("forks_count")
        item["license"] = (repo_data.get("license") or {}).get("spdx_id") or item.get("license") or "Unknown"
        item["archived"] = bool(repo_data.get("archived"))
        item["last_commit"] = latest_commit(owner, repo, default_branch, token) or repo_data.get("pushed_at")
        item["last_release"] = latest_release(owner, repo, token) or item.get("last_release")
        item["last_verified"] = datetime.now(timezone.utc).date().isoformat()
        updated += 1
        if args.sleep:
            time.sleep(args.sleep)

    data.setdefault("metadata", {})["last_updated"] = datetime.now(timezone.utc).date().isoformat()

    if args.dry_run:
        print(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
    else:
        args.data.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    print(f"Updated {updated} GitHub-backed entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
