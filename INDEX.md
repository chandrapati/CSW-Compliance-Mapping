# Control-ID Index

A lookup index across all eleven frameworks in this repository.
Use it to jump from a specific control / requirement / article to the
runbook section that explains how Cisco Secure Workload (CSW)
supports evidence for it.

> **Linking convention.** Most links point to the runbook root rather
> than a specific anchor — section anchors aren't stable across
> renderers. Once on the page, your browser's *Find* (Ctrl/Cmd+F) on
> the control ID is the fastest way to land in the right paragraph.

> **Why no entries for some controls?** A blank cell or omission means
> the control is intentionally outside CSW's scope (e.g., physical
> access, training, cryptographic primitives). The relevant runbook
> calls these out explicitly.

---

## Quick start by question

| If you're asking… | Start here |
|---|---|
| "How do I prove my segmentation actually works?" | [PCI Req 1](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md), [HIPAA §164.312(a)(1)](./HIPAA/CSW-HIPAA-Technical-Runbook.md), [NIST AC-4](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md), [DORA Art. 9](./DORA/CSW-DORA-Technical-Runbook.md) |
| "How do I demonstrate continuous monitoring?" | [NIST CA-7 / SI-4](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md), [PCI Req 11](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md), [SOC 2 CC7.2](./SOC2/CSW-SOC2-Technical-Runbook.md), [NIS2 Art. 21(2)(b)](./NIS2/CSW-NIS2-Technical-Runbook.md) |
| "How do I produce an incident-reporting evidence pack?" | [DORA Art. 19](./DORA/CSW-DORA-Technical-Runbook.md), [NIS2 Art. 23](./NIS2/CSW-NIS2-Technical-Runbook.md), [HIPAA §164.308(a)(6)](./HIPAA/CSW-HIPAA-Technical-Runbook.md) |
| "How do I show my supply chain / third-party exposure?" | [DORA Art. 28](./DORA/CSW-DORA-Technical-Runbook.md), [NIS2 Art. 21(2)(d)](./NIS2/CSW-NIS2-Technical-Runbook.md), [ISO A.5.19–A.5.22](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md) |
| "Where does CSW fit in a Zero Trust architecture?" | [NIST 800-207 Tenets](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md), [NIST 800-207A PDP/PEP/PA/PIP](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md), [CISA ZTMM](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.md) |
| "How do I evidence vulnerability management?" | [PCI Req 6, 11.3](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md), [NIST RA-5](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md), [ISO A.8.8](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md), [NIS2 Art. 21(2)(e)](./NIS2/CSW-NIS2-Technical-Runbook.md) |

---

## HIPAA Security Rule

Source: [`HIPAA/CSW-HIPAA-Technical-Runbook.md`](./HIPAA/CSW-HIPAA-Technical-Runbook.md)

| Citation | Topic | CSW can support evidence for |
|---|---|---|
| §164.306(a) | General requirements (admin, physical, technical safeguards) | Workload inventory, segmentation, telemetry baseline |
| §164.308(a)(1)(ii)(A) | Risk analysis | Workload inventory + ADM dependency graph (where monitored) |
| §164.308(a)(1)(ii)(B) | Risk management | Label/scope segmentation + drift detection |
| §164.308(a)(1)(ii)(D) | Information system activity review | Flow + process telemetry (exported to SIEM where integrated) |
| §164.308(a)(4) | Information access management | Identity/label-based segmentation |
| §164.308(a)(6) | Security incident procedures | Forensic timeline reconstruction |
| §164.312(a)(1) | Access control | Workload-level enforcement, deny-by-default |
| §164.312(b) | Audit controls | Process + flow telemetry; SIEM export when configured |
| §164.312(c)(1) | Integrity | Process / package change detection |
| §164.312(e)(1) | Transmission security | Plaintext-protocol DENY enforcement |
| §164.314(a) | Business Associate Agreements (technical companion) | Egress observation to BA endpoints |

---

## SOC 2 — Trust Services Criteria

Source: [`SOC2/CSW-SOC2-Technical-Runbook.md`](./SOC2/CSW-SOC2-Technical-Runbook.md)

| Criterion | Topic | CSW can support evidence for |
|---|---|---|
| CC6.1 | Logical & physical access controls | Workload segmentation, deny-by-default policy |
| CC6.6 | Restricting access to system resources | Per-process / per-port enforcement |
| CC6.7 | Restricting movement of information | Egress allow-listing |
| CC6.8 | Detecting unauthorised software | Process inventory, anomaly rules |
| CC7.1 | System operations — vulnerability management | CVE / exposure backlog with prioritisation signals |
| CC7.2 | System monitoring | Flow + process telemetry, SIEM forwarding |
| CC7.3 | Incident response | Forensic export + quarantine policy |
| CC7.4 | Recovery from incidents | Containment evidence + post-recovery diff |
| CC8.1 | Change management (technical companion) | Policy diff history, ADM drift |

---

## PCI DSS v4.0

Source: [`PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md`](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md)

| Requirement | Topic | CSW can support evidence for |
|---|---|---|
| Req 1 | Network security controls | CDE segmentation, simulation→enforce |
| Req 1.2.1 | Documented & approved flows | ADM-derived approved flow inventory |
| Req 2 | Secure configurations | Process / package baseline, drift |
| Req 6 | Develop & maintain secure software | Vulnerability inventory, CI/CD gating |
| Req 6.3.3 | Address vulnerabilities per risk ranking | CVSS + EPSS + reachability prioritisation |
| Req 7 | Restrict access by need-to-know | Identity-based workload segmentation |
| Req 10 | Log and monitor all access | Flow + process telemetry, SIEM export |
| Req 10.7.2 | Detect failures of critical controls | Sensor offline + enforcement gap alerts |
| Req 11.3 | Vulnerability scanning | Exposure insight from CSW-supported assessments — align with the Req 11 internal / ASV modalities your QSA expects |
| Req 11.4 | Network intrusion detection | Behavioural rules + conversation-graph anomaly |
| Req 11.5 | Detect changes/alterations | Process / package / configuration drift |
| Req 12.3.2 | Targeted risk analysis | CSW vulnerability + ADM data feeds risk analysis |

---

## NIST SP 800-53 Rev 5

Source: [`NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md`](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md)

| Control | Topic | CSW can support evidence for |
|---|---|---|
| AC-3 | Access enforcement | Workload-level policy enforcement |
| AC-4 | Information flow enforcement | Segmentation by label/scope |
| AC-6 | Least privilege | Deny-by-default policy + minimal allow |
| AU-2 / AU-12 | Auditable events | Process + flow telemetry |
| CA-7 | Continuous monitoring | Inventory snapshots + ADM drift signalling on whatever cadence you operate |
| CM-2 | Baseline configuration | Process / package baseline |
| CM-3 | Configuration change control | Policy diff history |
| CM-7 | Least functionality | Process + port allow-listing |
| CM-8 | System component inventory | Workload inventory reconciled with authoritative CMDB / cloud registers |
| IR-4 | Incident handling | Quarantine policy + forensic export |
| RA-5 | Vulnerability monitoring & scanning | Exposure monitoring backlog for workloads CSW observes |
| SA-11 | Developer testing & evaluation (technical evidence) | Pre-deploy vulnerability gating |
| SC-7 | Boundary protection | Egress allow-listing, plaintext-protocol DENY |
| SC-13 | Cryptographic protection | Plaintext-protocol DENY (FIPS-validated modules out of scope) |
| SI-4 | System monitoring | Behavioural rules + SIEM forwarding |
| SI-5 | Security alerts, advisories, directives | Vulnerability dashboards, exploit indicators |
| SR-3 / SR-6 | Supply chain controls (technical companion) | Egress observation to supplier endpoints |

---

## ISO/IEC 27001:2022 — Annex A

Source: [`ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md`](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md)

| Annex A | Topic | CSW can support evidence for |
|---|---|---|
| A.5.7 | Threat intelligence | Vulnerability + EPSS feed, IOC ingestion |
| A.5.19–A.5.22 | Supplier relationships (technical) | Supplier egress reconciliation |
| A.5.23 | Information security for cloud services | Cloud-account inventory + segmentation |
| A.5.30 | ICT readiness for business continuity (technical) | Containment + segmentation evidence |
| A.8.1 | User endpoint devices (workload portion) | Server / workload inventory baseline |
| A.8.8 | Management of technical vulnerabilities | CVE remediation tracking for workloads under observation |
| A.8.9 | Configuration management | Process / package baseline |
| A.8.16 | Monitoring activities | Behavioural rules + SIEM forwarding |
| A.8.20 | Networks security | Workload-level segmentation |
| A.8.21 | Security of network services | Per-service allow-listing |
| A.8.22 | Segregation of networks | Per-scope segmentation workspaces |
| A.8.23 | Web filtering (egress portion) | Egress allow-listing for HTTP/HTTPS workloads |
| A.8.24 | Use of cryptography | Plaintext-protocol DENY (no crypto primitives) |

---

## CISA Zero Trust Maturity Model v2.0

Source: [`CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.md`](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.md)

| Pillar | Example maturity path (varies by deployment) | CSW can support evidence for |
|---|---|---|
| Identity | Initial → Advanced | Identity-aware labels; integration with IdP-fed scopes (where deployed) |
| Devices | Initial → Advanced | Process-level fingerprinting; anomaly detection (tuning-dependent) |
| Networks | Often Advanced → Optimal aspiration | Enforcement / simulation workflows; observability-heavy ADM cadence — not an automatic Optimal-tier outcome |
| Applications & Workloads | Traditional → Advanced | Workload-level policy; vulnerability management views |
| Data | Traditional → Advanced | Conversation visibility; plaintext-protocol posture (encryption primitives still elsewhere) |

Cross-cutting capabilities — Visibility & Analytics; Automation &
Orchestration; Governance — *may* map to dashboard, API, and policy-
as-code workflows **when** customers wire those programmes up; the
pillars describe outcomes, not a guarantee of maturity tier.

---

## FIPS 140 (140-2 / 140-3)

Source: [`FIPS-140/CSW-FIPS-Technical-Runbook.md`](./FIPS-140/CSW-FIPS-Technical-Runbook.md)

CSW is **not a FIPS-validated cryptographic module**. The runbook
describes how CSW can support elements of an organisation's posture
toward FIPS — for instance by restricting obvious plaintext transports
and aligning workload inventory evidence with cryptographic usage
reviews — alongside **validated libraries and HSMs** that actually claim
modules. Statements like *"every in-scope workload only uses validated
cryptography"* still require cryptographic architecture and key
custody disciplines outside CSW.

| Requirement | CSW position |
|---|---|
| Cryptographic module validation | Out of scope — use a FIPS-validated library (OpenSSL FIPS, BouncyCastle FIPS) |
| Algorithm implementation testing | Out of scope — handled by NIST CMVP testing laboratory |
| Key generation & storage | Out of scope — use a FIPS-validated HSM |
| Module self-tests | Out of scope — handled by the cryptographic library |
| Use of FIPS-validated modules across the estate (programme assurance) | **In scope** — workload inventory + plaintext-protocol DENY evidence |

---

## NIST SP 800-207 — Zero Trust Architecture (Seven Tenets)

Source: [`NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md`](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md)

| Tenet | CSW can support evidence for |
|---|---|
| Tenet 1 — All data sources & computing services are resources | Workload/asset inventory plus cloud-account context (configured per your rollout) |
| Tenet 2 — All communication is secured regardless of network location | Plaintext-protocol DENY as one layer — TLS validation / crypto still owned elsewhere |
| Tenet 3 — Access to individual resources is granted on a per-session basis | Identity- and label-based segmentation per scope |
| Tenet 4 — Access is determined by dynamic policy | ADM-informed policy intents + drift/change signals (with human approvals) |
| Tenet 5 — Enterprise monitors integrity & posture of all assets | Posture telemetry (packages, CVE, flows)—interpret coverage with judgment |
| Tenet 6 — All resource authentication & authorisation is dynamic & strictly enforced | Identity-aware segmentation and enforcement at the workload (authn stacks still complementary) |
| Tenet 7 — Enterprise collects posture information & uses it to improve security | Evidence feeds into SIEM / metrics packs on a cadence you configure |

---

## NIST SP 800-207A — Zero Trust Logical Components (PDP/PEP/PA/PIP)

Source: [`NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md`](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md)

| Component | CSW role |
|---|---|
| Policy Decision Point (PDP) — Policy Engine | CSW Defend segmentation plane evaluates authored policy intents *(logical PEP/PIP analogue — map to official ZTA artefacts per assessor guidance)* |
| Policy Decision Point (PDP) — Policy Administrator | CSW Workspace administration + change history |
| Policy Enforcement Point (PEP) | CSW agent enforces decisions at the workload |
| Policy Information Point (PIP) | CSW telemetry (vulnerability, process, flow, package) feeds the policy decision |

---

## DORA — Regulation (EU) 2022/2554

> **Incident timelines.** The hour-based shorthand in Article 19 is widely
> discussed, but operative deadlines and classifications depend on the
> **Regulatory Technical Standards** and supervisory guidance **in force
> when you report**. Confirm against those instruments (and competent
> authority instructions) rather than relying on this index alone.

Source: [`DORA/CSW-DORA-Technical-Runbook.md`](./DORA/CSW-DORA-Technical-Runbook.md)

| Article | Topic | CSW can support evidence for |
|---|---|---|
| Art. 5 | Management body accountability | Quarterly evidence pack to management body |
| Art. 6 | ICT risk management framework | Centralised inventory, policy and detection state |
| Art. 8(1)–(6) | ICT asset inventory | Workload inventory + ADM dependency graph reconciled with authoritative registers |
| Art. 9(2)(a) | Network segmentation | Important-business-function scopes, simulation→enforce |
| Art. 9(2)(b) | Identification of unauthorised activities | ADM drift, conversation-graph anomalies |
| Art. 9(4)(g) | Continuous review of segmentation | Policy diff reports on an agreed supervisory cadence |
| Art. 10 | Detection | Behavioural rules + SIEM forwarding |
| Art. 11 | Response and recovery | Quarantine policy + forensic export bundle |
| Art. 13 | Learning and evolving | Quarterly metrics pack |
| Art. 17 | Incident management process | Forensic timeline reconstruction |
| Art. 18 | Classification of incidents | IBF labels + flow context inform classification |
| Art. 19 | Incident reporting (timing per RTS / supervisory guidance) | Artefact-heavy dossier templates in runbook — separate from statutory filing clocks |
| Art. 24 | Testing programme | Vulnerability + scenario test evidence |
| Art. 25(1) | Baseline tests | CVE dashboard + reachability queries |
| Art. 26 | TLPT (every 3 years for significant entities) | Red-team activity reconstruction |
| Art. 28(3) | Register of Information | Third-party egress reconciliation |
| Art. 28(4) | Third-party risk monitoring | Monitored egress patterns reconciled against the Register (where integrations exist) |
| Art. 30(2)(c) | Contractual right to monitor | Technical evidence supporting contractual right |

---

## NIS2 — Directive (EU) 2022/2555

> **Incident timelines (national law).** NIS2 Article 23 phases (24 h /
> 72 h / ~one month narrative) inherit detail from delegated acts plus
> **your Member State’s transposing statute** — confirm operative wording with
> local counsel / competent authority / CSIRT.

Source: [`NIS2/CSW-NIS2-Technical-Runbook.md`](./NIS2/CSW-NIS2-Technical-Runbook.md)

| Provision | Topic | CSW can support evidence for |
|---|---|---|
| Art. 20(1) | Management body accountability | Quarterly NIS2 pack |
| Art. 20(2) | Management body training | Pack section commentary as reusable training input |
| Art. 21(2)(a) | Risk analysis & IS-security policies | Workspace Intents grounded in observed behaviour |
| Art. 21(2)(b) | Incident handling | Detection rules + SIEM forwarding + 6-artefact dossier |
| Art. 21(2)(c) | Business continuity / backup / crisis | Containment + forensic preservation only (backups out of scope) |
| Art. 21(2)(d) | Supply chain security | Supplier egress reconciliation |
| Art. 21(2)(e) | Security in acquisition / dev / maintenance, vuln handling | Vulnerability inventory + CI/CD gate + CVE-to-attack-path |
| Art. 21(2)(f) | Effectiveness assessment | Quarterly effectiveness pack |
| Art. 21(2)(g) | Cyber hygiene + training | Patch & process telemetry (training out of scope) |
| Art. 21(2)(h) | Cryptography / encryption | Plaintext-protocol DENY (no crypto primitives) |
| Art. 21(2)(i) | HR sec / access control / asset management | Inventory + label discipline supporting asset-management evidence |
| Art. 21(2)(j) | MFA / secured comms | Identity-based segmentation (workload-to-workload analogue) |
| Art. 23(1) | 24-h early warning | 6-artefact dossier (initial pass) |
| Art. 23(2) | 72-h notification | Same dossier, progressively complete |
| Art. 23(3) | 1-month final report | Same dossier, plus root-cause and remediation |
| Art. 32 / 33 | Supervisory measures | On-demand audit-ready exports |

---

## Reverse Lookup — common CSW capabilities → frameworks

| CSW capability | Frameworks it often supports (apply judgment per deployment) |
|---|---|
| Workload inventory views | HIPAA §164.308(a)(1)(ii)(A) · PCI Req 2 · NIST CM-8 · ISO A.8.1 · CISA ZTMM Devices · 800-207 Tenet 1 · DORA Art. 8 · NIS2 Art. 21(2)(i) |
| Workload-level segmentation (allow-list / deny-by-default) | HIPAA §164.312(a)(1) · SOC 2 CC6.1 · PCI Req 1, 7 · NIST AC-3, AC-4, SC-7 · ISO A.8.20–A.8.22 · CISA ZTMM Networks · 800-207 Tenets 3, 6 · 800-207A PEP · DORA Art. 9 · NIS2 Art. 21(2)(a), (j) |
| ADM (application dependency mapping) | PCI Req 1.2.1 · NIST CA-7, CM-2 · ISO A.8.16 · DORA Art. 8(6) · NIS2 Art. 21(2)(a) |
| Exposure / vulnerability views + conversational reachability | PCI Req 6.3.3, 11.3 · NIST RA-5, SI-5 · ISO A.8.8 · DORA Art. 25(1) · NIS2 Art. 21(2)(e) |
| Process + flow telemetry into SIEM | HIPAA §164.312(b) · SOC 2 CC7.2 · PCI Req 10 · NIST AU-2, AU-12, SI-4 · ISO A.8.16 · DORA Art. 10 · NIS2 Art. 21(2)(b) |
| Quarantine policy + forensic export | HIPAA §164.308(a)(6) · SOC 2 CC7.3, CC7.4 · NIST IR-4 · DORA Art. 11 · NIS2 Art. 21(2)(b) |
| Egress observation + supplier reconciliation | ISO A.5.19–A.5.22 · NIST SR-3, SR-6 · DORA Art. 28 · NIS2 Art. 21(2)(d) |
| Plaintext-protocol DENY enforcement | HIPAA §164.312(e)(1) · NIST SC-7, SC-13 (programme support) · ISO A.8.24 · 800-207 Tenet 2 · NIS2 Art. 21(2)(h) · FIPS 140 (programme support) |
| Quarterly evidence pack to management body | DORA Art. 5 · NIS2 Art. 20 · ISO Clause 9.3 (management review input) · SOC 2 CC4.1 |

---

## Disclaimer

This index is curated for navigation, not certification. Listing a control
means that a properly scoped Cisco Secure Workload deployment may help you
assemble material artefacts aligned with that expectation — it does **not**
by itself constitute compliance with that control or satisfy supervisory filing
obligations.

Consult each framework runbook plus the disclaimer in [`README.md`](./README.md)
for supervisory reporting expectations, product coverage considerations,
and out-of-scope notes.

**Guidelines.** The tables above summarise typical ways teams discuss
Cisco Secure Workload alongside each control. They are reference points,
not prescriptions—use professional judgment in your environment and with
your assessors. Where mappings use language like *continuous*, *always-on*,
or similar shorthand, that reflects typical operating rhythm—calendar it
and prioritise refreshes using your team's judgment.
