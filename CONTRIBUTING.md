# Contributing

1. Add an object to `data/tools.json`:

   ```json
   {"category": "soc-soar", "section": "Detection Engineering & Rules",
    "name": "Tool name", "description": "One line, in English, no trailing period",
    "url": "https://github.com/owner/repo", "repo": "owner/repo",
    "risk": false, "source": "new"}
   ```

   - `category` must be one of the slugs in `scripts/build.py` → `CATEGORIES`.
   - `repo` is `owner/repo` for GitHub projects, otherwise `null`.
   - Set `risk: true` for PoCs, exploits, malware samples, backdoors, AV-evasion or C2 code.
2. Run `python scripts/build.py` (optionally `GITHUB_TOKEN=$(gh auth token) python scripts/build.py --enrich`).
3. Commit `data/` together with the regenerated `README.md` and `docs/`.

CI (`build-check`) fails if the generated Markdown is out of date.

Entries are removed when the repository is deleted or the link is permanently dead.
Archived or stale projects stay listed but are marked 🗄️ / 💤.
