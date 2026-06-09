# Contributing

Thanks for helping keep this list useful. The goal is not to collect every Android keyboard, but to maintain a compact map of projects that teach something about Android input methods, privacy, Chinese input, Rime, AI-assisted typing, or theme systems.

## Add or update an entry

Edit `data/keyboards.yml` first. Do not edit the generated project sections in `README.md` by hand.

Each new entry must include:

- A primary source: repository, official website, F-Droid page, Play Store page, or vendor page.
- A clear category from the existing category list.
- A short original note and a recommendation reason.
- Maintenance status: `active`, `maintenance-only`, `inactive`, `archived`, or `unknown`.
- Privacy and network notes when the keyboard has cloud sync, voice input, AI features, telemetry, or account features.
- Development feasibility and architecture complexity when the project is open source.

After editing data, run:

```bash
python scripts/update_github_stats.py
python scripts/generate_readme.py
```

If you do not have a GitHub token, the stats updater still works for low-frequency local use. For higher limits:

```bash
export GITHUB_TOKEN=ghp_xxx
```

Never commit API tokens.

## Review style

Keep comments brief, source-backed, and original. Do not copy long paragraphs from project READMEs, store descriptions, or marketing pages.

Prefer useful judgments:

- Good: "Active Rime frontend with deep schema and theme customization."
- Avoid: "The best keyboard ever with many amazing features."

## Categories

- `Commercial Keyboards`
- `Open Source Keyboards`
- `Rime-based Keyboards`
- `Privacy-focused Keyboards`
- `AI-assisted Keyboards`
- `Developer / Hacker Keyboards`
- `Theme and Customization Resources`
- `Android IME Development Resources`

## Pull request checklist

- [ ] Entry has at least one source URL.
- [ ] Entry has an original `notes` field.
- [ ] Entry has a concrete `recommendation_reason`.
- [ ] Maintenance status is filled in.
- [ ] Generated README has been updated.
- [ ] Markdown and generated data checks pass.
