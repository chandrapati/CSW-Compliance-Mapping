# Cisco Secure Workload — UK NCSC CAF Mapping

**Framework:** UK NCSC Cyber Assessment Framework (CAF) v3.2
**Applies to:** NIS Regulations (OES) assessments conducted by UK Competent
Authorities (Ofgem, Ofcom, DWI, CAA, DfT, DHSC) and GovAssure assessments
administered by the Cabinet Office / Government Security Group (GSG).
**Status:** Draft v1 — SME review required against the current CAF text
and your assessor's expectations.

> **Companion assets.** This file is the 14-principle crosswalk only. For
> engineering steps, see the
> [Technical Runbook](./CSW-UK-NCSC-CAF-Technical-Runbook.md). For the
> customer-facing narrative, see the
> [Compliance Report](./CSW-UK-NCSC-CAF-Compliance-Report.md). For maturity
> scoring, see the [IGP Maturity Scorer](./caf-igp-maturity-scorer.md). For
> what to export per principle, see the
> [Evidence Pack Template](./caf-evidence-pack-template.md).

---

## How to use this document

The CAF describes **outcomes** across 4 Objectives (A/B/C/D) and 14
Principles. Assessors score each principle against granular Indicators of
Good Practice (IGPs) using three statuses — **Achieved**,
**Partially Achieved**, or **Not Achieved**. CSW does not satisfy any
principle by itself; it is an **evidence source** for a subset of the
technical IGPs.

For each principle below, this document identifies:

1. **CSW contribution tier** — ✅ Primary (CSW is a leading evidence source),
   🟡 Supporting (CSW supplements other controls), ⚪ Out of scope.
2. **Primary existing runbook** inside this repository that already contains
   the relevant engineering detail and control-ID mapping.
3. **Specific CSW evidence** that an assessor can inspect.
4. **Pairings needed** — other controls / tools that must sit alongside CSW
   to close the principle.

The goal is to reuse evidence already produced for sister frameworks
(NIS2, NIST CSF 2.0, ISO 27001:2022, CIS Controls v8.1, NIST 800-53,
IEC 62443) rather than duplicate it.

---

## Quick-scan table

| CAF | Objective / Principle | Tier | Reuse primarily from |
|---|---|---|---|
| **A1** | Governance | 🟡 Supporting | [NIST CSF GV.OV / GV.SC](../NIST-CSF-2/), [COBIT APO13](../COBIT-2019/), [ISO 27001 A.5](../ISO-27001-2022/) |
| **A2** | Risk Management | ✅ Primary | [NIS2 Art. 21(2)(a)](../NIS2/), [NIST CSF ID.RA](../NIST-CSF-2/), [NIST 800-53 RA family](../NIST-800-53/) |
| **A3** | Asset Management | ✅ Primary | [CIS Controls 1, 2](../CIS-Controls-v8/), [NIST CSF ID.AM](../NIST-CSF-2/), [NIST 800-53 CM-8](../NIST-800-53/) |
| **A4** | Supply Chain | 🟡 Supporting | [NIS2 Art. 21(2)(d)](../NIS2/), [ISO A.5.19–A.5.22](../ISO-27001-2022/), [DORA Art. 28](../DORA/) |
| **B1** | Policies & Processes | ✅ Primary | [NIST 800-53 PL family](../NIST-800-53/), [NIST CSF PR.PS](../NIST-CSF-2/), [ISO A.5](../ISO-27001-2022/) |
| **B2** | Identity & Access | ⚪ Out of scope | — (pair with Cisco ISE / identity platform) |
| **B3** | Data Security | 🟡 Supporting | [NIST CSF PR.DS](../NIST-CSF-2/), [NIST 800-53 SC family](../NIST-800-53/), [FIPS 140](../FIPS-140/) |
| **B4** | System Security | ✅ Primary | [CIS Controls 4, 7, 8](../CIS-Controls-v8/), [AU Essential Eight E2/E6](../AU-Essential-Eight/) |
| **B5** | Resilient Networks & Systems | ✅ **Primary — CSW core** | [NIST 800-53 SC-7/AC-4](../NIST-800-53/), [NIST CSF PR.IR](../NIST-CSF-2/), [CIS Control 13](../CIS-Controls-v8/), [ISO A.8.20–A.8.22](../ISO-27001-2022/), [**IEC 62443 Zones & Conduits**](../IEC-62443/), [NIST 800-82](../NIST-800-82/) |
| **B6** | Staff Awareness & Training | ⚪ Out of scope | — |
| **C1** | Security Monitoring | ✅ Primary | [NIST CSF DE.CM / DE.AE](../NIST-CSF-2/), [CIS Control 13](../CIS-Controls-v8/), [NIST 800-53 AU, SI-4](../NIST-800-53/) |
| **C2** | Proactive Event Discovery | ✅ Primary | [**MITRE ATT&CK runbook**](../MITRE-ATTACK/), [NIST CSF DE.AE](../NIST-CSF-2/), [NIST 800-53 SI-4, RA-5](../NIST-800-53/) |
| **D1** | Response & Recovery | 🟡 Supporting | [NIST CSF RS / RC](../NIST-CSF-2/), [NIST 800-53 IR, CP families](../NIST-800-53/), [DORA Art. 19](../DORA/) |
| **D2** | Improvements | 🟡 Supporting | [NIST CSF ID.IM](../NIST-CSF-2/), [NIST 800-53 PM-14](../NIST-800-53/) |

---

## Deep crosswalk

### Objective A — Managing Security Risk

#### A1 Governance

> *Clear organisational leadership, board-level accountability, defined
> security roles, and adequate resourcing for cyber resilience.*

- **CSW tier:** 🟡 Supporting
- **CSW evidence:** Executive posture summary feeding board/CISO reporting
  (blast-radius score, enforcement coverage %, policy maturity score,
  Critical CVE count, cluster-wide trend across months). This is governance
  **telemetry**, not governance **structure**.
- **Primary runbook to cite:** [NIST CSF GV.OV / GV.SC](../NIST-CSF-2/) for
  outcomes-based governance language; [COBIT 2019 APO13](../COBIT-2019/)
  for managed-security governance structure.
- **Pairings needed:** Documented security roles & resourcing (HR/finance),
  board/exec reporting cadence, risk appetite statement.

#### A2 Risk Management

> *Continuous identification and mitigation of threats targeting essential
> functions, moving away from static annual audits to dynamic threat modelling.*

- **CSW tier:** ✅ Primary
- **CSW evidence:** Dynamic (not annual) blast-radius scoring; enforcement
  gap % trend; exploitable-CVE counts with CVM intelligence (not raw CVSS);
  per-workload reachability analysis; `cluster_delta` change log between
  snapshots.
- **Primary runbooks:** [NIS2 Art. 21(2)(a)](../NIS2/) risk-analysis mapping;
  [NIST CSF ID.RA](../NIST-CSF-2/); [NIST 800-53 RA family](../NIST-800-53/).
- **Pairings needed:** Threat intelligence feeds, risk register, risk-tolerance
  decisions, business-impact analysis.

#### A3 Asset Management

> *Comprehensive, real-time inventory of all physical devices, software
> packages, firmware, network circuits, cloud services, and external
> dependencies supporting essential services.*

- **CSW tier:** ✅ Primary
- **CSW evidence:** Real-time sensor census (hostname, OS, agent version,
  interfaces, scope membership); installed-package inventory per workload;
  cluster snapshot JSON retained as point-in-time attestation.
- **Primary runbooks:** [CIS Controls 1 & 2](../CIS-Controls-v8/);
  [NIST CSF ID.AM](../NIST-CSF-2/); [NIST 800-53 CM-8](../NIST-800-53/).
- **Pairings needed:** CMDB authoritative source (ServiceNow via
  [CSW ServiceNow Integration](https://github.com/chandrapati/csw-servicenow-integration));
  IPAM/DNS inventory ([Infoblox integration](https://github.com/chandrapati/csw-infoblox-integration));
  cloud-provider asset APIs ([AWS](https://github.com/chandrapati/csw-aws-connector) /
  [Azure](https://github.com/chandrapati/csw-azure-connector) /
  [GCP](https://github.com/chandrapati/csw-gcp-connector) connectors).

#### A4 Supply Chain

> *Managing third-party and vendor risk, ensuring suppliers with access to
> critical systems adhere to equivalent security controls.*

- **CSW tier:** 🟡 Supporting
- **CSW evidence:** Vendor-code presence (installed packages per workload
  filtered by vendor); vendor-tagged egress reconciliation using scope-based
  flow analysis (what *actually* talks to vendor endpoints vs what the
  contract allows).
- **Primary runbooks:** [NIS2 Art. 21(2)(d)](../NIS2/);
  [ISO 27001 A.5.19–A.5.22](../ISO-27001-2022/);
  [DORA Art. 28](../DORA/) ICT third-party risk;
  [NIST CSF GV.SC](../NIST-CSF-2/).
- **Pairings needed:** Third-party risk management (TPRM) programme,
  contractual security clauses, assurance questionnaires, SBOM pipeline.

### Objective B — Protecting Against Cyber Attack

#### B1 Service Protection Policies & Processes

> *Defined, enforced, and continuously tested security policies.*

- **CSW tier:** ✅ Primary
- **CSW evidence:** Workspace policies defined and version-controlled in CSW;
  continuous enforcement at the host firewall (nftables on Linux, WFP on
  Windows); every flow decision is a de-facto policy test; ADM version
  history as change log.
- **Primary runbooks:** [NIST 800-53 PL family](../NIST-800-53/);
  [NIST CSF PR.PS](../NIST-CSF-2/); [ISO 27001 A.5](../ISO-27001-2022/).
- **Pairings needed:** Policy governance body, change-approval process,
  exception-management workflow.

#### B2 Identity & Access Control

> *Strict MFA, role-based least privilege (RBAC), privileged access
> management (PAM), and automated revocation of inactive accounts.*

- **CSW tier:** ⚪ Out of scope
- **Reason:** CSW is not an identity platform. CSW does not authenticate
  users, enforce MFA, manage RBAC, or operate PAM.
- **Pair with:** Enterprise IdP (Entra ID / Okta / Ping) for MFA + lifecycle;
  PAM tool (CyberArk / Delinea / BeyondTrust); SSO.
- **Where CSW *touches* B2:** User-identity–aware microsegmentation via
  [Cisco ISE / pxGrid integration](https://github.com/chandrapati/csw-ise-integration)
  — the identity assertion comes from ISE, not from CSW.

#### B3 Data Security

> *Protection of data at rest, in transit, and in use; robust cryptographic
> key management; prevention of unauthorised data exfiltration.*

- **CSW tier:** 🟡 Supporting (data in transit + exfiltration)
- **CSW evidence:** East-west flow visibility across every workload-to-workload
  pair; segmentation policy preventing unauthorised data paths; insecure-cipher
  agent count (TLS hygiene signal); plaintext-protocol deny policies (see
  [FIPS 140 runbook](../FIPS-140/)).
- **CSW does not do:** Data classification, data-at-rest encryption, key
  management (KMS/HSM), DLP content inspection.
- **Primary runbooks:** [NIST CSF PR.DS](../NIST-CSF-2/);
  [NIST 800-53 SC family](../NIST-800-53/);
  [NIS2 Art. 21(2)(h)](../NIS2/); [FIPS 140](../FIPS-140/).
- **Pairings needed:** DLP, KMS/HSM, data classification tool, database
  activity monitoring.

#### B4 System Security

> *Configuration hardening, timely vulnerability management/patching,
> removal of default credentials, and prevention of unauthorised code
> execution.*

- **CSW tier:** ✅ Primary (vuln management + config visibility)
- **CSW evidence:** Per-workload CVE inventory with CVM exploit-intelligence
  enrichment; package inventory for patch targeting; agent-version drift as
  config-baseline signal; process allowlist / policy enforcement blocks
  unauthorised code paths at the network layer.
- **Primary runbooks:** [CIS Controls 4, 7, 8](../CIS-Controls-v8/);
  [NIST CSF PR.PS](../NIST-CSF-2/);
  [AU Essential Eight E2/E6](../AU-Essential-Eight/) for patch cadence.
- **Pairings needed:** Patch management platform (SCCM/BigFix/Red Hat
  Satellite); config-baseline tool (CIS Benchmarks via scanner); EDR for
  process-level allow-listing.

#### B5 Resilient Networks & Systems *(CSW core value prop)*

> *Strict network segmentation and microsegmentation (especially separating
> IT corporate networks from OT/SCADA process control networks via the
> Purdue Model / IEC 62443), DDoS mitigation, and high-availability
> architecture.*

- **CSW tier:** ✅ **Primary — this is the strongest row in the entire repo**
- **CSW evidence:**
  - Workload-level microsegmentation enforced in-kernel (nftables Linux,
    WFP Windows) — matches the CAF's "host firewall orchestration, eBPF
    in-kernel filtering" language verbatim.
  - Per-scope policies with ADM-suggested baselines, simulation before
    enforcement, and continuous verification via rejected-flow logs.
  - IT-side separation from OT zones (IT-tier of IT/OT boundary; pair with
    Cisco Cyber Vision / Claroty for the OT tier).
  - Blast-radius score as a before/after metric for segmentation projects.
- **Primary runbooks:** [NIST 800-53 SC-7 / AC-4](../NIST-800-53/);
  [NIST CSF PR.IR](../NIST-CSF-2/); [CIS Control 13](../CIS-Controls-v8/);
  [ISO 27001 A.8.20–A.8.22](../ISO-27001-2022/);
  [IEC 62443 Zones & Conduits](../IEC-62443/) *(the specific one CAF B5
  Section 5 cites)*; [NIST 800-82](../NIST-800-82/).
- **Pairings needed:** Perimeter / DDoS layer (not CSW); OT-aware DPI
  (Cyber Vision / Claroty / Nozomi / Dragos); HA / BCP architecture.

#### B6 Staff Awareness & Training

> *Tailored, role-based security training (e.g., specialised awareness for
> OT operators and systems administrators).*

- **CSW tier:** ⚪ Out of scope
- **Pair with:** Security awareness platform (KnowBe4 / Proofpoint /
  SANS); role-based training programme.

### Objective C — Detecting Cyber Security Events

#### C1 Security Monitoring

> *Continuous logging and monitoring of endpoints, network flows
> (NetFlow/IPFIX/eBPF), firewalls, and authentication events with
> synchronised network time (NTP).*

- **CSW tier:** ✅ Primary (endpoints + flows)
- **CSW evidence:** Continuous per-connection flow telemetry (NetFlow-grade +
  process context + policy decision); agent heartbeats and health; forensics
  event stream; synchronised via cluster NTP; SIEM egress via
  [Splunk integration](https://github.com/chandrapati/csw-splunk-integration).
- **Primary runbooks:** [NIST CSF DE.CM, DE.AE](../NIST-CSF-2/);
  [CIS Control 13](../CIS-Controls-v8/);
  [NIST 800-53 AU, SI-4](../NIST-800-53/);
  [NIS2 Art. 21(2)(c)](../NIS2/).
- **Pairings needed:** SIEM/SOAR, authentication log sources (IdP), firewall
  logs, UBA.

#### C2 Proactive Event Discovery

> *Proactive threat hunting, anomaly detection, vulnerability scanning,
> and threat intelligence ingestion to identify undetected compromises.*

- **CSW tier:** ✅ Primary
- **CSW evidence:** MITRE ATT&CK technique coverage via forensics rules
  (see [MITRE ATT&CK runbook](../MITRE-ATTACK/)); vulnerability scanning via
  CVE inventory + CVM exploit intel; policy-violation anomaly detection
  (rejected flows report); process-level behavioural baselines via ADM.
- **Primary runbooks:** [MITRE ATT&CK runbook](../MITRE-ATTACK/);
  [NIST CSF DE.AE](../NIST-CSF-2/);
  [NIST 800-53 SI-4, RA-5](../NIST-800-53/).
- **Pairings needed:** External threat-intel feeds, EDR / XDR for host-level
  behavioural analytics, SOC playbooks.

### Objective D — Minimising the Impact of Incidents

#### D1 Response & Recovery Planning

> *Documented, tested disaster recovery and incident response plans;
> air-gapped/immutable backups; defined recovery time objectives (RTO) and
> recovery point objectives (RPO).*

- **CSW tier:** 🟡 Supporting
- **CSW evidence:** Blast-radius containment reduces incident scope;
  ADM policy versions enable rapid rollback of segmentation state;
  per-workload forensic flow history supports IR timeline reconstruction.
- **CSW does not do:** Backup, restore, immutable storage, DR orchestration,
  BCP site switchover.
- **Primary runbooks:** [NIST CSF RS / RC pillars](../NIST-CSF-2/);
  [NIST 800-53 IR, CP families](../NIST-800-53/);
  [NIS2 Art. 21(2)(b)](../NIS2/); [DORA Art. 19](../DORA/).
- **Pairings needed:** Backup/DR platform (Veeam/Rubrik/Cohesity);
  IR orchestration (SOAR); runbook library; tabletop exercise cadence.

#### D2 Improvements

> *Systematic post-incident root-cause analysis and lessons-learned
> mechanisms to continuously harden defences.*

- **CSW tier:** 🟡 Supporting
- **CSW evidence:** Snapshot history and `cluster_delta` change tracking feed
  "what changed between pre-incident and incident" reconstruction; blast-radius
  and policy-maturity trends over quarters show improvement cadence.
- **Primary runbooks:** [NIST CSF ID.IM](../NIST-CSF-2/);
  [NIST 800-53 PM-14](../NIST-800-53/).
- **Pairings needed:** Formal lessons-learned / post-incident-review process;
  risk-register integration; policy-update workflow.

---

## What this mapping does **not** cover

Honest about scope so assessors don't form false expectations:

| Area | Why not | Where to look instead |
|---|---|---|
| **B2 Identity & Access entirely** | CSW is not an IAM tool. | IdP + PAM. CSW can consume ISE identity assertions for policy via [ISE integration](https://github.com/chandrapati/csw-ise-integration), but the authentication/authorisation decision lives in ISE. |
| **B6 Staff training entirely** | Not applicable. | Security awareness platform. |
| **Data at rest + KMS (B3)** | CSW doesn't touch stored data or keys. | KMS/HSM + storage encryption. |
| **Backup/restore (D1)** | CSW does not operate backup. | Backup/DR platform. |
| **A1 Governance structure** | CSW produces metrics, not org charts or role definitions. | HR + CISO office. |
| **Perimeter / DDoS** | CSW is east-west, not north-south edge defence. | Secure Firewall / DDoS service. |
| **OT device tier of B5** | CSW agents run on servers, not PLCs/RTUs. | Cyber Vision / Claroty / Nozomi / Dragos. |

---

## Related documents in this folder

- **[CSW-UK-NCSC-CAF-Technical-Runbook.md](./CSW-UK-NCSC-CAF-Technical-Runbook.md)** —
  engineering view: scope design, labels, policy authoring per principle,
  evidence collection steps.
- **[CSW-UK-NCSC-CAF-Compliance-Report.md](./CSW-UK-NCSC-CAF-Compliance-Report.md)** —
  customer-facing narrative for CISO / exec audiences.
- **[caf-igp-maturity-scorer.md](./caf-igp-maturity-scorer.md)** — IGP rubric
  translating CSW KPIs to Achieved / Partially Achieved / Not Achieved per
  principle.
- **[caf-evidence-pack-template.md](./caf-evidence-pack-template.md)** — what
  to export from CSW per principle for a GovAssure / OES submission.

## Disclaimer

Draft v1. Mapping derived from the UK NCSC Cyber Assessment Framework v3.2
and cross-referenced against documented Cisco Secure Workload product
capabilities. Requires SME review against your Competent Authority's current
expectations before relied upon in a formal assessment. See the
[repository-level disclaimer](../README.md#disclaimer) for the full
informational-only clause.
