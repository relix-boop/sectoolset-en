#!/usr/bin/env python3
"""Render README.md and docs/*.md from data/tools.json (+ data/meta.json).

Usage:
  python scripts/build.py            # render markdown from data/
  python scripts/build.py --enrich   # refresh stars / last commit / archived via GitHub GraphQL, then render
  python scripts/build.py --check    # fail if rendered markdown is out of date (for CI)

--enrich needs a token in GITHUB_TOKEN (Actions provides one; locally: GITHUB_TOKEN=$(gh auth token)).
Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.request
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"
STALE_YEARS = 3

CATEGORIES = OrderedDict([
    ("soc-soar", ("SOC, SOAR & Detection Engineering",
                  "SOAR platforms and content (incl. Cortex XSOAR/XSIAM), detection-as-code rule sets, "
                  "SIEM/NSM telemetry, DFIR and detection testing.")),
    ("labs-ctf", ("Practice Labs & CTF", "Deliberately vulnerable apps, training platforms, CTF archives and OSCP/OSCE prep.")),
    ("scanners", ("Scanners", "Network, subdomain, web, TLS, code and secrets scanners.")),
    ("pentest", ("Penetration Testing", "Offensive frameworks, post-exploitation, fuzzing, web, MITM and password attacks.")),
    ("exploits", ("Vulnerabilities, PoCs & Exploits", "Vulnerability databases, PoC collections and exploit development tooling.")),
    ("binary-analysis", ("Binary & Code Analysis", "Reverse engineering, binary rewriting, static analysis and mobile app security.")),
    ("defense", ("Defense, Hardening & Monitoring", "Hardening baselines, WAFs, host/network monitoring, forensics, audit and DevSecOps.")),
    ("threat-intel", ("Threat Intelligence & Honeypots", "Threat intel feeds and platforms, OSINT, DFIR resources and honeypots.")),
    ("ai-llm", ("AI & LLM Security", "LLM vulnerability scanners, jailbreak and prompt-injection research, AI security frameworks.")),
    ("docs", ("Docs & Learning", "Reading lists, awesome lists, courses, cheat sheets and programming resources.")),
    ("blackhat-2018", ("Black Hat USA 2018 Arsenal", "Tools presented at the Black Hat USA 2018 Arsenal (historical snapshot).")),
])

GQL_FIELDS = "nameWithOwner stargazerCount isArchived pushedAt defaultBranchRef { target { ... on Commit { committedDate } } }"


def load():
    tools = json.loads((DATA / "tools.json").read_text(encoding="utf-8"))
    meta_path = DATA / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    return tools, meta


def enrich(tools, meta):
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("--enrich needs GITHUB_TOKEN")
    repos = sorted({t["repo"] for t in tools if t.get("repo")})
    for i in range(0, len(repos), 50):
        chunk = repos[i:i + 50]
        parts = []
        for j, r in enumerate(chunk):
            owner, name = r.split("/", 1)
            parts.append(f'r{j}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{ {GQL_FIELDS} }}')
        body = json.dumps({"query": "query {" + " ".join(parts) + "}"}).encode()
        req = urllib.request.Request("https://api.github.com/graphql", data=body,
                                     headers={"Authorization": f"bearer {token}", "User-Agent": "sectoolset-build"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.load(resp).get("data") or {}
        for j, r in enumerate(chunk):
            node = data.get(f"r{j}")
            m = meta.setdefault(r, {})
            if not node:
                m["missing"] = True
                continue
            m.pop("missing", None)
            m["stars"] = node["stargazerCount"]
            m["archived"] = node["isArchived"]
            commit = ((node.get("defaultBranchRef") or {}).get("target") or {}).get("committedDate")
            m["last_commit"] = (commit or node["pushedAt"] or "")[:10]
            if node["nameWithOwner"].lower() != r.lower():
                m["renamed_to"] = node["nameWithOwner"]
        print(f"enriched {min(i + 50, len(repos))}/{len(repos)}", file=sys.stderr)
    meta["_updated"] = dt.date.today().isoformat()
    (DATA / "meta.json").write_text(json.dumps(meta, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def fmt_stars(n):
    if n is None:
        return "–"
    return f"{n / 1000:.1f}k" if n >= 1000 else str(n)


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def render_table(rows, meta, today):
    out = ["| Tool | Description | ⭐ | Last commit |", "|---|---|--:|---|"]

    def sort_key(t):
        m = meta.get(t.get("repo") or "", {})
        return (m.get("last_commit") or "0000", m.get("stars") or 0)

    for t in sorted(rows, key=sort_key, reverse=True):
        m = meta.get(t.get("repo") or "", {})
        url = t["url"]
        if m.get("renamed_to"):
            url = f"https://github.com/{m['renamed_to']}"
        flags = []
        if t.get("risk"):
            flags.append("⚠️")
        if m.get("archived"):
            flags.append("🗄️")
        last = m.get("last_commit") or ""
        if last and (today - dt.date.fromisoformat(last)).days > 365 * STALE_YEARS:
            flags.append("💤")
        name = f"[{cell(t['name'])}]({url})" + (" " + " ".join(flags) if flags else "")
        out.append(f"| {name} | {cell(t['description'])} | {fmt_stars(m.get('stars')) if t.get('repo') else ''} | {last} |")
    return "\n".join(out)


LEGEND = ("**Legend:** ⚠️ third-party offensive code / PoC / malware sample – read the source and run only in an isolated lab · "
          "🗄️ archived upstream · 💤 no commits for 3+ years · ⭐ and dates are refreshed weekly by CI.")


def render(tools, meta):
    # staleness is measured against the last metadata refresh so output is reproducible
    today = dt.date.fromisoformat(meta["_updated"]) if meta.get("_updated") else dt.date.today()
    files = {}
    counts = OrderedDict()
    for slug, (title, intro) in CATEGORIES.items():
        rows = [t for t in tools if t["category"] == slug]
        counts[slug] = len(rows)
        sections = OrderedDict()
        for t in rows:
            sections.setdefault(t["section"], []).append(t)
        md = [f"# {title}", "", intro, "", LEGEND, "", "[← Back to index](../README.md)", ""]
        if len(sections) > 1:
            md += [f"- [{s}](#{anchor(s)}) ({len(v)})" for s, v in sections.items()] + [""]
        for s, v in sections.items():
            md += [f"## {s}", "", render_table(v, meta, today), ""]
        files[DOCS / f"{slug}.md"] = "\n".join(md)

    total = sum(counts.values())
    updated = meta.get("_updated", "not yet – run the *Refresh metadata* workflow")
    readme = [
        "# SecToolSet (English)",
        "",
        f"A curated, English-language index of **{total} open-source security tools and resources** – "
        "cleaned, de-duplicated and enriched with GitHub activity data.",
        "",
        "Built from the Chinese-language [bollwarm/SecToolSet](https://github.com/bollwarm/SecToolSet) list "
        "(Apache-2.0): descriptions translated, dead/empty repositories and duplicates removed, typos in links fixed, "
        "and a new **SOC, SOAR & Detection Engineering** section added.",
        "",
        LEGEND,
        "",
        f"_Metadata last refreshed: {updated}_",
        "",
        "## Categories",
        "",
        "| Category | Entries | Description |",
        "|---|--:|---|",
    ]
    for slug, (title, intro) in CATEGORIES.items():
        readme.append(f"| [{title}](docs/{slug}.md) | {counts[slug]} | {intro} |")
    readme += [
        "",
        "## How this repo works",
        "",
        "- `data/tools.json` is the single source of truth (category, section, name, description, url, risk flag).",
        "- `data/meta.json` holds stars / last-commit / archived status, refreshed weekly by "
        "`.github/workflows/refresh.yml` via `python scripts/build.py --enrich`.",
        "- `README.md` and `docs/*.md` are **generated** – edit the JSON, then run `python scripts/build.py`.",
        "- `.github/workflows/links.yml` runs [lychee](https://github.com/lycheeverse/lychee) weekly and opens an issue for broken links.",
        "",
        "See [CONTRIBUTING.md](CONTRIBUTING.md) to add a tool.",
        "",
        "## Disclaimer",
        "",
        "Listed for research, defense and authorized testing only. Inclusion is not an endorsement; "
        "third-party code – especially entries marked ⚠️ – can be backdoored or trigger AV/EDR. "
        "Review before running and never test systems you are not authorized to test.",
        "",
        "## License",
        "",
        "Apache-2.0. Derived from bollwarm/SecToolSet – see [NOTICE](NOTICE).",
        "",
    ]
    files[ROOT / "README.md"] = "\n".join(readme)
    return files


def anchor(s):
    a = s.lower()
    out = []
    for ch in a:
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch == " ":
            out.append("-")
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--enrich", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    tools, meta = load()
    if args.enrich:
        enrich(tools, meta)
    files = render(tools, meta)
    if args.check:
        stale = [str(p.relative_to(ROOT)) for p, c in files.items()
                 if not p.exists() or p.read_text(encoding="utf-8") != c]
        if stale:
            sys.exit("Out of date – run `python scripts/build.py`: " + ", ".join(stale))
        print("markdown up to date")
        return
    DOCS.mkdir(exist_ok=True)
    for p, c in files.items():
        p.write_text(c, encoding="utf-8")
    print(f"wrote {len(files)} files, {len(tools)} entries")


if __name__ == "__main__":
    main()
