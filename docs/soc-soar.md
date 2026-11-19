# SOC, SOAR & Detection Engineering

SOAR platforms and content (incl. Cortex XSOAR/XSIAM), detection-as-code rule sets, SIEM/NSM telemetry, DFIR and detection testing.

**Legend:** ⚠️ third-party offensive code / PoC / malware sample – read the source and run only in an isolated lab · 🗄️ archived upstream · 💤 no commits for 3+ years · ⭐ and dates are refreshed weekly by CI.

[← Back to index](../README.md)

- [SOAR Platforms & Content](#soar-platforms--content) (9)
- [Detection Engineering & Rules](#detection-engineering--rules) (15)
- [SIEM, NSM & Telemetry](#siem-nsm--telemetry) (6)
- [DFIR & Threat Hunting](#dfir--threat-hunting) (7)
- [Detection Testing & Adversary Emulation](#detection-testing--adversary-emulation) (3)
- [Threat Intelligence Platforms](#threat-intelligence-platforms) (3)

## SOAR Platforms & Content

| Tool | Description | ⭐ | Last commit |
|---|---|--:|---|
| [Cortex XSOAR content](https://github.com/demisto/content) | Official XSOAR/XSIAM content repo: integrations, playbooks, scripts, layouts, content packs | 1.3k | 2026-11-19 |
| [Cortex Analyzers](https://github.com/TheHive-Project/Cortex-Analyzers) | Analyzers and responders for observable enrichment and response | 495 | 2026-11-19 |
| [XSOAR dockerfiles](https://github.com/demisto/dockerfiles) | Docker images used by XSOAR integrations and automations | 90 | 2026-11-19 |
| [Tracecat](https://github.com/TracecatHQ/tracecat) | Open-source automation platform for security and IT teams (SOAR alternative) | 3.9k | 2026-11-18 |
| [Shuffle](https://github.com/Shuffle/Shuffle) | Open-source SOAR with a visual workflow editor and OpenAPI-based apps | 2.5k | 2026-11-18 |
| [demisto-sdk](https://github.com/demisto/demisto-sdk) | CLI to create, validate, lint, test and upload XSOAR/XSIAM content | 90 | 2026-11-17 |
| [XSOAR developer docs](https://github.com/demisto/content-docs) | Source of xsoar.pan.dev: integration, playbook and content-pack development guides | 47 | 2026-11-17 |
| [DFIR-IRIS](https://github.com/dfir-iris/iris-web) | Collaborative incident response case management platform | 1.6k | 2026-09-23 |
| [TheHive](https://github.com/TheHive-Project/TheHive) 🗄️ | Security incident response platform (case management) | 4.0k | 2025-07-25 |

## Detection Engineering & Rules

| Tool | Description | ⭐ | Last commit |
|---|---|--:|---|
| [Microsoft Sentinel](https://github.com/Azure/Azure-Sentinel) | Sentinel analytics rules, hunting queries, workbooks, playbooks and connectors | 6.3k | 2026-11-19 |
| [Elastic detection rules](https://github.com/elastic/detection-rules) | Detection rules for Elastic Security, with tooling and tests | 3.0k | 2026-11-19 |
| [Splunk Security Content](https://github.com/splunk/security_content) | Splunk detections, analytic stories and playbooks mapped to ATT&CK | 1.7k | 2026-11-19 |
| [Sigma](https://github.com/SigmaHQ/sigma) | Generic, SIEM-agnostic detection rule format and rule repository | 11.5k | 2026-11-18 |
| [Sublime rules](https://github.com/sublime-security/sublime-rules) | Email security detection rules (MQL) for phishing and BEC | 382 | 2026-11-18 |
| [signature-base](https://github.com/Neo23x0/signature-base) | YARA rules and IOCs used by LOKI and THOR | 3.1k | 2026-11-17 |
| [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator) | Annotate and visualize ATT&CK matrices (coverage, threat profiles) | 2.5k | 2026-11-17 |
| [Panther analysis](https://github.com/panther-labs/panther-analysis) | Python detections and queries for the Panther SIEM | 474 | 2026-11-16 |
| [sigma-cli](https://github.com/SigmaHQ/sigma-cli) | CLI to convert Sigma rules using pySigma backends | 225 | 2026-11-11 |
| [pySigma](https://github.com/SigmaHQ/pySigma) | Python library to parse and convert Sigma rules to SIEM queries | 613 | 2026-11-09 |
| [DeTTECT](https://github.com/rabobank-cdc/DeTTECT) | Score and visualize data-source quality, visibility and detection coverage against ATT&CK | 2.4k | 2026-11-05 |
| [MITRE CTI](https://github.com/mitre/cti) | ATT&CK and CAPEC data in STIX 2.0 | 2.2k | 2026-11-05 |
| [awesome-detection-engineering](https://github.com/infosecB/awesome-detection-engineering) | Detection engineering resources | 1.4k | 2026-10-12 |
| [awesome-detection-rules](https://github.com/jatrost/awesome-detection-rules) | Index of public detection rule repositories | 300 | 2024-05-05 |
| [ADS framework](https://github.com/palantir/alerting-detection-strategy-framework) 💤 | Palantir's Alerting and Detection Strategy framework for documenting detections | 931 | 2021-04-29 |

## SIEM, NSM & Telemetry

| Tool | Description | ⭐ | Last commit |
|---|---|--:|---|
| [CrowdSec](https://github.com/crowdsecurity/crowdsec) | Collaborative behavior-based IPS with shared blocklists | 15.7k | 2026-11-19 |
| [Zeek](https://github.com/zeek/zeek) | Network security monitor producing rich protocol logs | 8.3k | 2026-11-18 |
| [Suricata](https://github.com/OISF/suricata) | Network IDS/IPS and NSM engine | 6.9k | 2026-11-18 |
| [Wazuh](https://github.com/wazuh/wazuh) | Open-source XDR/SIEM: endpoint agent, log analysis, FIM, compliance | 17.8k | 2026-11-17 |
| [Falco](https://github.com/falcosecurity/falco) | Cloud-native runtime threat detection for containers, Kubernetes and Linux | 9.6k | 2026-11-06 |
| [Security Onion](https://github.com/Security-Onion-Solutions/securityonion) | Distribution for threat hunting, NSM and log management | 5.0k | 2026-11-02 |

## DFIR & Threat Hunting

| Tool | Description | ⭐ | Last commit |
|---|---|--:|---|
| [Velociraptor](https://github.com/Velocidex/velociraptor) | Endpoint visibility, hunting and collection with VQL | 4.5k | 2026-11-19 |
| [Chainsaw](https://github.com/WithSecureOpenSource/chainsaw) | Rapidly search and hunt through Windows forensic artefacts with Sigma | 3.7k | 2026-11-15 |
| [Timesketch](https://github.com/google/timesketch) | Collaborative forensic timeline analysis | 3.5k | 2026-11-12 |
| [Hayabusa](https://github.com/Yamato-Security/hayabusa) | Fast Windows event log timeline and threat hunting (Sigma-based) | 3.5k | 2026-11-10 |
| [LOKI](https://github.com/Neo23x0/Loki) | Simple IOC and YARA scanner | 3.8k | 2026-01-09 |
| [Security Datasets](https://github.com/OTRF/Security-Datasets) 💤 | Recorded attack telemetry for building and testing detections | 1.9k | 2023-09-20 |
| [HELK](https://github.com/Cyb3rWard0g/HELK) 💤 | Hunting ELK stack with Jupyter and Spark | 3.9k | 2021-05-09 |

## Detection Testing & Adversary Emulation

| Tool | Description | ⭐ | Last commit |
|---|---|--:|---|
| [CALDERA](https://github.com/apache/caldera) | Automated adversary emulation platform (MITRE) | 7.5k | 2026-11-19 |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | Small, ATT&CK-mapped tests to validate detections | 12.9k | 2026-11-06 |
| [APTSimulator](https://github.com/NextronSystems/APTSimulator) | Batch script that simulates APT artefacts to test detections | 2.8k | 2025-09-23 |

## Threat Intelligence Platforms

| Tool | Description | ⭐ | Last commit |
|---|---|--:|---|
| [OpenCTI connectors](https://github.com/OpenCTI-Platform/connectors) | Import/enrichment/export connectors for OpenCTI | 597 | 2026-11-19 |
| [MISP](https://github.com/MISP/MISP) | Threat intelligence sharing platform | 6.7k | 2026-11-18 |
| [IntelMQ](https://github.com/certtools/intelmq) | Collect, parse and enrich threat feeds for CERTs/SOCs | 1.1k | 2026-04-24 |
