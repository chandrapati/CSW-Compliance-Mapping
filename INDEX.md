# Control-ID Index

A lookup index across all sixteen frameworks in this repository.
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
| "How do I prove my segmentation actually works?" | [PCI Req 1](./PCI-DSS-v4/pci-runbook.md), [HIPAA §164.312(a)(1)](./HIPAA/CSW-HIPAA-Technical-Runbook.md), [NIST AC-4](./NIST-800-53/nist-runbook.md), [DORA Art. 9](./DORA/CSW-DORA-Technical-Runbook.md), [NERC CIP-005 R1](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md), [TSA SD Section III.A](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md), [CIS Safeguard 13.4](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md), [CSF PR.IR-01](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md), [CMMC SC.L2-3.13.1 / 3.13.6](./CMMC-2/CSW-CMMC-Technical-Runbook.md) |
| "How do I demonstrate continuous monitoring?" | [NIST CA-7 / SI-4](./NIST-800-53/nist-runbook.md), [PCI Req 11](./PCI-DSS-v4/pci-runbook.md), [SOC 2 CC7.2](./SOC2/soc2-runbook.md), [NIS2 Art. 21(2)(b)](./NIS2/CSW-NIS2-Technical-Runbook.md), [NERC CIP-007 R4](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md), [TSA SD Section III.C](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md), [CIS Safeguards 13.1 / 13.6](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md), [CSF DE.CM-01 / DE.CM-09](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md), [CMMC SI.L2-3.14.6](./CMMC-2/CSW-CMMC-Technical-Runbook.md) |
| "How do I produce an incident-reporting evidence pack?" | [DORA Art. 19](./DORA/CSW-DORA-Technical-Runbook.md), [NIS2 Art. 23](./NIS2/CSW-NIS2-Technical-Runbook.md), [HIPAA §164.308(a)(6)](./HIPAA/CSW-HIPAA-Technical-Runbook.md), [NERC CIP-008](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md), [TSA CIRP / 24-hour CISA](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md), [CIS Control 17](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md), [CSF RS.AN-03 / RS.AN-07](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md), [CMMC IR.L2-3.6.x](./CMMC-2/CSW-CMMC-Technical-Runbook.md) |
| "How do I show my supply chain / third-party exposure?" | [DORA Art. 28](./DORA/CSW-DORA-Technical-Runbook.md), [NIS2 Art. 21(2)(d)](./NIS2/CSW-NIS2-Technical-Runbook.md), [ISO A.5.19–A.5.22](./ISO-27001-2022/iso27001-runbook.md), [NERC CIP-013](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md), [CIS Control 15](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md), [CSF GV.SC-04 / GV.SC-07](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md) |
| "Where does CSW fit in a Zero Trust architecture?" | [NIST 800-207 Tenets](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md), [NIST 800-207A PDP/PEP/PA/PIP](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md), [CISA ZTMM](./CISA-ZeroTrust/cisa-ztmm-runbook.md), [CSF PR.IR / PR.AA](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md) |
| "How do I evidence vulnerability management?" | [PCI Req 6, 11.3](./PCI-DSS-v4/pci-runbook.md), [NIST RA-5](./NIST-800-53/nist-runbook.md), [ISO A.8.8](./ISO-27001-2022/iso27001-runbook.md), [NIS2 Art. 21(2)(e)](./NIS2/CSW-NIS2-Technical-Runbook.md), [NERC CIP-010 R3](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md), [TSA SD Section III.D](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md), [CIS Control 7](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md), [CSF ID.RA-01 / ID.RA-05](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md), [CMMC RA.L2-3.11.2 / 3.11.3](./CMMC-2/CSW-CMMC-Technical-Runbook.md) |
| "How do I evidence IT/OT segmentation on the IT side?" | [NERC CIP-005 R1 (IT-side ESP enclave)](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md), [TSA SD Section III.A](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md), [NIST AC-4 / SC-7](./NIST-800-53/nist-runbook.md) |
| "How do I evidence asset and software inventory?" | [CIS Controls 1 + 2](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md), [NIST CM-8](./NIST-800-53/nist-runbook.md), [CSF ID.AM-01 / ID.AM-02](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md), [CMMC CM.L2-3.4.1 / 3.4.6](./CMMC-2/CSW-CMMC-Technical-Runbook.md) |
| "How do I evidence governance to my management body?" | [DORA Art. 5](./DORA/CSW-DORA-Technical-Runbook.md), [NIS2 Art. 20](./NIS2/CSW-NIS2-Technical-Runbook.md), [CSF GV.OV-01/02/03](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md), [SOC 2 CC4.1](./SOC2/soc2-runbook.md) |
| "What does CSW look like for a CMMC L2 (CUI) scope?" | [CMMC AC.L2-3.1.1 / 3.1.3](./CMMC-2/CSW-CMMC-Technical-Runbook.md), [CMMC SC.L2-3.13.1 / 3.13.6](./CMMC-2/CSW-CMMC-Technical-Runbook.md), [NIST 800-53 AC-4](./NIST-800-53/nist-runbook.md) |

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

Source: [`SOC2/soc2-runbook.md`](./SOC2/soc2-runbook.md)

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

Source: [`PCI-DSS-v4/pci-runbook.md`](./PCI-DSS-v4/pci-runbook.md)

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

Source: [`NIST-800-53/nist-runbook.md`](./NIST-800-53/nist-runbook.md)

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

Source: [`ISO-27001-2022/iso27001-runbook.md`](./ISO-27001-2022/iso27001-runbook.md)

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

Source: [`CISA-ZeroTrust/cisa-ztmm-runbook.md`](./CISA-ZeroTrust/cisa-ztmm-runbook.md)

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

Source: [`FIPS-140/fips-runbook.md`](./FIPS-140/fips-runbook.md)

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

## NERC CIP — North American Bulk Electric System (IT-side mapping)

> **Scope.** CSW addresses the **IT side** of the IT/OT boundary —
> EACMS, jump hosts, vendor-access servers, identity/PKI, BCSI hosts.
> CSW is **not** an Electronic Access Point (EAP) and does not enforce
> on PLCs / RTUs / IEDs / HMIs. Pair with your boundary firewall and
> your OT-aware monitoring stack (Cisco Cyber Vision, Claroty, Nozomi,
> Dragos) for end-to-end coverage. Draft v1 — apply SME judgment.

Source: [`NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md`](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md)

| Standard / Requirement | Topic | CSW can support evidence for (IT-side) |
|---|---|---|
| CIP-002 R1 | BES Cyber System identification | Inventory + scope labelling for the IT estate supporting BCS |
| CIP-003 R1 | Senior Manager accountability | Quarterly evidence pack covering CIP-005/007/010/013 IT-side outputs |
| CIP-005 R1 | Electronic Security Perimeter | IT-side enclave segmentation; deny-by-default to EAP-IP set; documented exception list |
| CIP-005 R1.5 | Boundary control review | Quarterly enforcement diff report |
| CIP-005 R2 | Interactive Remote Access (IRA) | Intermediate-system enforcement; per-session flow telemetry; weekly IRA-pattern report |
| CIP-007 R1 | Ports and services baseline | Per-workload listening-port inventory with last-flow timestamp |
| CIP-007 R2 | Patch management | Continuous CVE inventory feeding the patch programme |
| CIP-007 R3 | Malicious code prevention | Behavioural rules + simulation→enforcement progression |
| CIP-007 R4 | Security event monitoring | Process + flow telemetry to SIEM with retention |
| CIP-008 R1 | Incident response plan | Six-artefact reconstruction bundle |
| CIP-008 R4 | Reportable Cyber Security Incident notification | Containment evidence + dossier supporting E-ISAC notification |
| CIP-010 R1 | Configuration baseline | Daily software + listening-port baseline with diff and disposition |
| CIP-010 R1.5 | Unauthorised change monitoring | Daily diff vs. previous day with disposition column |
| CIP-010 R3.1 | Active vulnerability assessment (Highs) | Per-workload CVE list with CVSS / exploit / EPSS context |
| CIP-010 R3.2 | Pre-commissioning VA | First-sighting CVE inventory before ESP connection |
| CIP-011 R1.1 | BCSI access controls | Egress and access pattern monitoring on `bes_role=bcsi-host` workloads |
| CIP-013 R1.2.5 | Vendor remote access | EACMS egress allowlist scoped to vendor register |
| CIP-013 R1.2.6 | Vendor incident coordination | Vendor-egress flow record for the incident window |

---

## TSA Pipeline — Security Directive 2021-02 series (IT-side mapping)

> **Scope.** CSW addresses the **IT side** of the IT/OT boundary —
> SCADA jump servers, historians, MES/EAM, engineering workstations,
> vendor-access hosts, identity/PKI. CSW is **not** an OT-protocol
> deep-packet-inspection tool and does not enforce on RTUs / flow
> computers / PLCs / IEDs / HMIs. Pair with your IT/OT firewall and
> your OT-aware sensors. Draft v1 — apply SME judgment.

Source: [`TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md`](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md)

| SD provision | Topic | CSW can support evidence for (IT-side) |
|---|---|---|
| Section II | Critical Cyber System identification | Inventory + scope labelling for CSW-managed workloads supporting CCS |
| Section II | Cybersecurity Coordinator | Quarterly evidence pack to the Coordinator |
| Section III.A | Network segmentation (IT/OT) | Per-site IT-side enclave segmentation; deny-by-default to IT/OT boundary firewall |
| Section III.A | Documented data flows | Observed IT→OT flow inventory + reconciliation against architecture |
| Section III.A | New-flow change control | Continuous monitoring for new IT→OT edges |
| Section III.B | Access control measures | Workload-level least-privilege; quarterly access review with sunset log |
| Section III.C | Continuous monitoring & detection | Behavioural rules + flow telemetry to SIEM; conversation-graph anomalies |
| Section III.C | SIEM integration | Forwarding configuration to Splunk / QRadar / Sentinel / Cisco XDR |
| Section III.C | Detection latency | Per-CCS-function MTTD report |
| Section III.D | Unpatched-system risk reduction | Continuous CVE inventory + compensating-control register |
| Section III.D | Patch verification | Diff report showing patched version + automatic CVE drop |
| Cybersecurity Incident Response Plan | Detection, response, 24-hour CISA reporting | Six-artefact reconstruction bundle |
| Cybersecurity Assessment Plan (CAP) | Annual implementation assessment | Per-SD-section evidence pack with prior-period delta |
| Cybersecurity Architecture Design Review | Periodic architecture review | Workload inventory + dependency graph + observed flow inventory |

---

## CIS Critical Security Controls v8.1 (IG2 lead)

> **Scope.** CIS Controls v8.1, 18 Controls and ~153 Safeguards.
> Default depth is **Implementation Group 2 (IG2)**; IG1 and IG3
> deltas are called out where the work materially changes. CSW is
> direct on six Controls (1, 2, 4, 7, 8, 13) and supporting on
> seven; out of scope on Controls 5 (account mgmt), 9 (email/web),
> 11 (data recovery), 14 (training).

Source: [`CIS-Controls-v8/CSW-CIS-Technical-Runbook.md`](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md)

| Safeguard | Topic | CSW can support evidence for |
|---|---|---|
| 1.1 / 1.5 | Inventory of enterprise assets; passive discovery | Continuous workload inventory + cloud-orchestrator polling |
| 1.2 | Address unauthorised assets | Quarantine policy applied to net-new workloads |
| 2.1 | Software inventory | Per-workload package + version inventory |
| 2.3 / 2.5 / 2.6 | Address unauthorised software; allow-list | Allow-list deviation alerting + (IG3) behavioural block |
| 4.1 | Secure configuration process | Daily baseline + drift report tied to change ticket |
| 4.4 / 4.6 | Default deny on FW; secure software config | CSW segmentation enforcement + per-workload listening-port inventory |
| 7.1–7.7 | Continuous vulnerability management | Continuous CVE inventory + reachability prioritisation + patch SLA tracking |
| 8.2 / 8.5 | Collect audit logs; detailed audit logs | SIEM forwarding with per-flow + per-process detail |
| 8.7 / 8.10 | Retain audit logs (≥90 days IG2) | SIEM retention policy + CSW window |
| 8.11 | Audit log reviews | Quarterly review of CSW alert summary |
| 12.2 | Use secure protocols | Plaintext-flow detection + DENY enforcement |
| 12.4 | Architecture diagrams | ADM dependency export |
| 13.1 / 13.6 | Centralised monitoring; flow logs | CSW flow telemetry + SIEM forwarding |
| 13.2 / 13.3 | Host + network IDS | Behavioural rule catalogue + anomaly detection |
| 13.4 | Traffic filtering between segments | CSW segmentation policy + simulation→enforcement log |
| 13.5 | Remote-asset access control | Bastion-source-restricted mgmt protocol allow rules |
| 13.7–13.10 (IG3) | HIPS / NIPS / port-level / app-layer filtering | Behavioural rules + segmentation enforcement |
| 15.1 / 15.4 | Service provider mgmt (technical lens) | Vendor-egress observation + reconciliation |
| 17.1–17.8 | Incident response management | Six-artefact reconstruction bundle |
| 18.1 / 18.5 | Penetration testing | Pre/post reachability + activity reconstruction |

---

## NIST Cybersecurity Framework 2.0 (Govern + 5 Functions)

> **Scope.** CSF 2.0 (Feb 2024) added **Govern (GV)** above the
> existing Identify / Protect / Detect / Respond / Recover. CSF
> wraps control catalogues; this section maps the **technical
> Subcategories** where CSW supplies evidence. Direct on ID / PR
> / DE / RS technical Subcategories; supporting on GV (evidence
> pack) and RC (post-incident diff). Out of scope on physical/
> environmental, backup/recovery execution, and training/HR
> Subcategories.

Source: [`NIST-CSF-2/CSW-CSF-Technical-Runbook.md`](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md)

| Subcategory | Topic | CSW can support evidence for |
|---|---|---|
| GV.OV-01 / 02 / 03 | Cybersecurity strategy oversight | Quarterly evidence pack to management body |
| GV.SC-04 / 07 / 09 / 10 | Cybersecurity supply chain (CSCRM) | Vendor-egress observation + reconciliation + EOL register |
| ID.AM-01 / 02 / 03 | Hardware / software / flow inventory | Continuous workload + ADM dependency + observed-flow inventory |
| ID.AM-04 | Supplier service inventory | Vendor-egress + register reconciliation |
| ID.AM-05 / 07 | Asset / data prioritisation and classification | `crit_band` + `data_class` labels per workload |
| ID.AM-08 | Asset lifecycle | Vendor-EOL flags in software inventory |
| ID.RA-01 / 05 / 06 | Vulnerabilities + risk + response | CVE inventory + reachability prioritisation + remediation tracking |
| ID.RA-07 | Changes & exceptions | Drift report + change-ticket attribution |
| PR.AA-01 / 05 | Identity-aware access enforcement | Workload-side enforcement (identity upstream) |
| PR.DS-02 | Data-in-transit | Plaintext-protocol DENY enforcement |
| PR.IR-01 | Network protected from unauthorised access | Workload-level deny-by-default segmentation |
| PR.IR-03 | Resilience requirements | Quarantine policy + segmentation under change control |
| PR.PS-01 | Configuration management | Daily baseline + drift detection |
| PR.PS-02 | Software maintained | Per-workload software inventory + EOL tagging |
| PR.PS-04 | Log records generated | Per-flow + per-process telemetry to SIEM |
| PR.PS-05 | Unauthorised software prevented | Behavioural rules + (IG3) block |
| PR.PS-06 | Secure software development | CVE inventory feeds SDLC |
| DE.CM-01 | Networks monitored | CSW flow telemetry + behavioural rules + SIEM |
| DE.CM-03 | Personnel activity monitored | Process telemetry + identity-aware policy |
| DE.CM-06 | External service provider activities monitored | Vendor-egress observation + drift alerting |
| DE.CM-09 | Computing hardware/software monitored | Per-workload telemetry retention |
| DE.AE-02 / 03 / 04 / 06 / 07 / 08 | Adverse event analysis | Forensic timeline + SIEM correlation + threat intel + impact + ticket routing |
| RS.MA-01 to 05 | Incident management | Six-artefact dossier + severity routing |
| RS.AN-03 / 06 / 07 / 08 | Incident analysis (root cause, magnitude, integrity) | Process + flow timeline + dossier with timestamped exports |
| RS.MI-01 / 02 | Incident mitigation | Quarantine policy + compensating-control register |
| RC.RP-04 / 05 / 06 | Recovery actions (evidence side) | Post-recovery segmentation diff + re-baseline |

---

## CMMC 2.0 (Cybersecurity Maturity Model Certification — DoD/DIB)

> **Scope.** Default depth is **Level 2** (110 controls = NIST SP
> 800-171 Rev 2). Level 1 (FAR 52.204-21, 15 safeguards) and Level
> 3 (Level 2 + selected NIST 800-172 enhancements) are called out
> in the runbook. CSW is direct on AC, AU, CM, RA, SC, SI families;
> supporting on CA, IA, IR (evidence), MA; out of scope on AT, MP,
> PE, PS. **CMMC L2 assessment is performed by a C3PAO** — nothing
> here substitutes for the SSP, POA&M, or the C3PAO engagement.

Source: [`CMMC-2/CSW-CMMC-Technical-Runbook.md`](./CMMC-2/CSW-CMMC-Technical-Runbook.md)

| Practice | Topic | CSW can support evidence for |
|---|---|---|
| AC.L1/L2-3.1.1 | Limit system access | Per-enclave deny-by-default segmentation |
| AC.L2-3.1.2 | Limit access to authorised functions | Allow-list per documented system function |
| AC.L2-3.1.3 | Control flow of CUI | Inter-enclave flow allow-list + reconciliation against SSP |
| AC.L2-3.1.20 | Verify external connections | Egress allowlist + alert on net-new external destinations |
| AC.L2-3.1.22 | CUI on publicly-accessible systems | Internet-reachability query + scope review |
| AU.L2-3.3.1 | Audit records | Per-flow + per-process telemetry to SIEM |
| AU.L2-3.3.2 | Action traceability to individual users | Process attribution + SIEM identity correlation |
| AU.L2-3.3.4 / 3.3.5 / 3.3.8 | Alert / correlate / protect logs | Forwarder health alert + SIEM correlation + RBAC |
| AU.L2-3.3.9 | Limit audit-log mgmt functionality | CSW RBAC for audit-management roles |
| CM.L2-3.4.1 | Establish baseline configurations | Daily snapshot per workload (OS, packages, ports, processes) |
| CM.L2-3.4.3 / 3.4.4 | Track and approve changes | Daily diff + change-ticket attribution |
| CM.L2-3.4.6 | Least functionality | Listening-port + service inventory + 90-day-no-flow review |
| CM.L2-3.4.7 | Restrict nonessential programs | Software allow-list + (L3) behavioural block |
| RA.L2-3.11.2 | Vulnerability scanning | Continuous CVE inventory per CUI workload |
| RA.L2-3.11.3 | Remediate vulnerabilities | Patch SLA + compensating-control register + POA&M linkage |
| SC.L2-3.13.1 | Boundary protection | Per-enclave segmentation enforcement |
| SC.L2-3.13.2 | Architectural designs | ADM-derived as-observed architecture |
| SC.L2-3.13.5 | Subnetworks for publicly-accessible components | Public-component scope isolation |
| SC.L2-3.13.6 | Deny by default; permit by exception | Workload-level deny-by-default (native CSW posture) |
| SC.L2-3.13.7 | Prevent split tunneling | Detective alert on split-tunnel patterns |
| SI.L2-3.14.1 | Identify, report, correct system flaws | CVE inventory + drift + SIEM routing |
| SI.L2-3.14.2 | Malicious code protection | Behavioural rules layered with endpoint AV |
| SI.L2-3.14.3 | Monitor security advisories | Threat-intel-enriched CVE prioritisation |
| SI.L2-3.14.6 | Monitor communications | Flow telemetry + behavioural rules + anomaly detection |
| SI.L2-3.14.7 | Identify unauthorised use | Process telemetry + identity-aware policy |
| IR.L2-3.6.1 / 3.6.2 / 3.6.3 | Incident response process | Six-artefact dossier per CUI-scope incident |

---

## Reverse Lookup — common CSW capabilities → frameworks

| CSW capability | Frameworks it often supports (apply judgment per deployment) |
|---|---|
| Workload inventory views | HIPAA §164.308(a)(1)(ii)(A) · PCI Req 2 · NIST CM-8 · ISO A.8.1 · CISA ZTMM Devices · 800-207 Tenet 1 · DORA Art. 8 · NIS2 Art. 21(2)(i) · NERC CIP-002 R1 · TSA SD Section II · CIS Safeguard 1.1 · CSF ID.AM-01 · CMMC CM.L2-3.4.1 |
| Workload-level segmentation (allow-list / deny-by-default) | HIPAA §164.312(a)(1) · SOC 2 CC6.1 · PCI Req 1, 7 · NIST AC-3, AC-4, SC-7 · ISO A.8.20–A.8.22 · CISA ZTMM Networks · 800-207 Tenets 3, 6 · 800-207A PEP · DORA Art. 9 · NIS2 Art. 21(2)(a), (j) · NERC CIP-005 R1 · TSA SD Section III.A · CIS Safeguards 4.4, 13.4 · CSF PR.IR-01 · CMMC AC.L2-3.1.1, SC.L2-3.13.1 / 3.13.6 |
| Identity-aware least-privilege between zones (e.g. IT-to-OT-adjacent) | NIST AC-3, AC-6 · 800-207 Tenets 3, 6 · NERC CIP-005 R1 (IT-side) · TSA SD Section III.A / III.B · CIS Safeguard 6.1 · CSF PR.AA-05 · CMMC AC.L2-3.1.2 / 3.1.3 |
| Interactive remote access termination evidence | NERC CIP-005 R2 · NIST AC-17 · DORA Art. 9 (telework) · CIS Safeguard 13.5 · CMMC AC.L2-3.1.13 |
| ADM (application dependency mapping) | PCI Req 1.2.1 · NIST CA-7, CM-2 · ISO A.8.16 · DORA Art. 8(6) · NIS2 Art. 21(2)(a) · NERC CIP-010 R1.1 · TSA SD Section III.A (documented flows) · CIS Safeguard 12.4 · CSF ID.AM-03 · CMMC SC.L2-3.13.2 |
| Per-workload listening-port inventory + last-flow timestamp | PCI Req 1.2.6, 2.2.4 · NIST CM-7 · NERC CIP-007 R1 · TSA SD Section III.B · CIS Safeguards 4.6, 2.6 · CMMC CM.L2-3.4.6 |
| Exposure / vulnerability views + conversational reachability | PCI Req 6.3.3, 11.3 · NIST RA-5, SI-5 · ISO A.8.8 · DORA Art. 25(1) · NIS2 Art. 21(2)(e) · NERC CIP-010 R3 · TSA SD Section III.D · CIS Safeguards 7.1–7.7 · CSF ID.RA-01 / ID.RA-05 · CMMC RA.L2-3.11.2 / 3.11.3 |
| Configuration baseline + unauthorised-change detection | NIST CM-2, CM-3, CM-6 · ISO A.8.9 · NERC CIP-010 R1, R1.5 · CIS Safeguard 4.1 · CSF PR.PS-01 / ID.RA-07 · CMMC CM.L2-3.4.1 / 3.4.3 |
| Process + flow telemetry into SIEM | HIPAA §164.312(b) · SOC 2 CC7.2 · PCI Req 10 · NIST AU-2, AU-12, SI-4 · ISO A.8.16 · DORA Art. 10 · NIS2 Art. 21(2)(b) · NERC CIP-007 R4 · TSA SD Section III.C · CIS Safeguards 8.2 / 8.5 / 13.6 · CSF DE.CM-01 / DE.CM-09 / PR.PS-04 · CMMC AU.L2-3.3.1 / 3.3.2 / SI.L2-3.14.6 |
| Quarantine policy + forensic export | HIPAA §164.308(a)(6) · SOC 2 CC7.3, CC7.4 · NIST IR-4 · DORA Art. 11 · NIS2 Art. 21(2)(b) · NERC CIP-008 · TSA CIRP / 24-hour CISA · CIS Control 17 · CSF RS.MI-01 / RS.AN-07 · CMMC IR.L2-3.6.x |
| Egress observation + supplier reconciliation | ISO A.5.19–A.5.22 · NIST SR-3, SR-6 · DORA Art. 28 · NIS2 Art. 21(2)(d) · NERC CIP-013 R1 (vendor remote access on the IT side) · CIS Safeguards 15.1 / 15.4 · CSF GV.SC-04 / GV.SC-07 / GV.SC-09 · CMMC AC.L2-3.1.20 |
| Plaintext-protocol DENY enforcement | HIPAA §164.312(e)(1) · NIST SC-7, SC-13 (programme support) · ISO A.8.24 · 800-207 Tenet 2 · NIS2 Art. 21(2)(h) · FIPS 140 (programme support) · CIS Safeguard 12.2 · CSF PR.DS-02 |
| Quarterly evidence pack to management body / Senior Officer | DORA Art. 5 · NIS2 Art. 20 · ISO Clause 9.3 (management review input) · SOC 2 CC4.1 · NERC CIP-003 R1 · TSA Cybersecurity Coordinator role · CSF GV.OV-01 / 02 / 03 · CMMC supports the SSP/POA&M cycle |
| Annual self-assessment evidence pack | NIST CA-2 · ISO Clause 9.2 · TSA Cybersecurity Assessment Plan (CAP) · CIS IG self-assessment · CMMC L2 self-assessment (where contract permits) |
| Behavioural detection + anomaly detection | NIST SI-4 · DORA Art. 10(2) · NIS2 Art. 21(2)(b) · CIS Safeguards 13.2 / 13.3 · CSF DE.AE-02 / DE.AE-07 · CMMC SI.L2-3.14.2 / 3.14.6 |
| CUI / regulated-data scope labelling | HIPAA ePHI tagging · PCI CDE labelling · DORA ICT-asset criticality (Art. 8) · CSF ID.AM-05 · CMMC CUI scope (foundational) |

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
