# SecToolSet (English)

A curated, English-language index of **833 open-source security tools and resources** – cleaned, de-duplicated and enriched with GitHub activity data.

Built from the Chinese-language [bollwarm/SecToolSet](https://github.com/bollwarm/SecToolSet) list (Apache-2.0): descriptions translated, dead/empty repositories and duplicates removed, typos in links fixed, and a new **SOC, SOAR & Detection Engineering** section added.

**Legend:** ⚠️ third-party offensive code / PoC / malware sample – read the source and run only in an isolated lab · 🗄️ archived upstream · 💤 no commits for 3+ years · ⭐ and dates are refreshed weekly by CI.

_Metadata last refreshed: 2026-11-19_

## Categories

| Category | Entries | Description |
|---|--:|---|
| [SOC, SOAR & Detection Engineering](docs/soc-soar.md) | 43 | SOAR platforms and content (incl. Cortex XSOAR/XSIAM), detection-as-code rule sets, SIEM/NSM telemetry, DFIR and detection testing. |
| [Practice Labs & CTF](docs/labs-ctf.md) | 72 | Deliberately vulnerable apps, training platforms, CTF archives and OSCP/OSCE prep. |
| [Scanners](docs/scanners.md) | 77 | Network, subdomain, web, TLS, code and secrets scanners. |
| [Penetration Testing](docs/pentest.md) | 138 | Offensive frameworks, post-exploitation, fuzzing, web, MITM and password attacks. |
| [Vulnerabilities, PoCs & Exploits](docs/exploits.md) | 63 | Vulnerability databases, PoC collections and exploit development tooling. |
| [Binary & Code Analysis](docs/binary-analysis.md) | 51 | Reverse engineering, binary rewriting, static analysis and mobile app security. |
| [Defense, Hardening & Monitoring](docs/defense.md) | 165 | Hardening baselines, WAFs, host/network monitoring, forensics, audit and DevSecOps. |
| [Threat Intelligence & Honeypots](docs/threat-intel.md) | 62 | Threat intel feeds and platforms, OSINT, DFIR resources and honeypots. |
| [AI & LLM Security](docs/ai-llm.md) | 13 | LLM vulnerability scanners, jailbreak and prompt-injection research, AI security frameworks. |
| [Docs & Learning](docs/docs.md) | 111 | Reading lists, awesome lists, courses, cheat sheets and programming resources. |
| [Black Hat USA 2018 Arsenal](docs/blackhat-2018.md) | 38 | Tools presented at the Black Hat USA 2018 Arsenal (historical snapshot). |

## How this repo works

- `data/tools.json` is the single source of truth (category, section, name, description, url, risk flag).
- `data/meta.json` holds stars / last-commit / archived status, refreshed weekly by `.github/workflows/refresh.yml` via `python scripts/build.py --enrich`.
- `README.md` and `docs/*.md` are **generated** – edit the JSON, then run `python scripts/build.py`.
- `.github/workflows/links.yml` runs [lychee](https://github.com/lycheeverse/lychee) weekly and opens an issue for broken links.

See [CONTRIBUTING.md](CONTRIBUTING.md) to add a tool.

## Disclaimer

Listed for research, defense and authorized testing only. Inclusion is not an endorsement; third-party code – especially entries marked ⚠️ – can be backdoored or trigger AV/EDR. Review before running and never test systems you are not authorized to test.

## License

Apache-2.0. Derived from bollwarm/SecToolSet – see [NOTICE](NOTICE).
