# Development Notes

## Repository model

`data/keyboards.yml` is the source of truth. `README.md` is generated from it.

The intended workflow is:

```bash
python scripts/update_github_stats.py
python scripts/generate_readme.py
```

## GitHub API behavior

`scripts/update_github_stats.py` reads `GITHUB_TOKEN` from the environment when available. Without a token, it uses unauthenticated GitHub API requests and is suitable for occasional local updates.

The updater fills:

- `stars`
- `forks`
- `last_commit`
- `last_release`
- `license`
- `archived`
- `last_verified`

Non-GitHub projects are left untouched.

## Data principles

- Keep marketing claims out of the data file.
- Prefer short factual notes over feature lists.
- Track uncertainty with `unknown`, `partial`, or concise notes.
- Use official sources first, then package indexes such as F-Droid or Play Store.
- Keep category assignment stable; add secondary tags later only when needed.

## Future improvements

- Add schema validation for `data/keyboards.yml`.
- Add package index update scripts for F-Droid and Play Store metadata.
- Add optional screenshots or theme-gallery links once licensing is clear.
- Track Android target SDK and build status for open-source projects.
- Split keyboard engines, theme resources, and user-facing apps if the list grows.
