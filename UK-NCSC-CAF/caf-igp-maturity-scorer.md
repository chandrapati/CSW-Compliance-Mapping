# CAF IGP Maturity Scorer — CSW-driven

**Purpose.** Show which CSW observations can be attached to a CAF principle.
An assessor still scores the principle. A healthy CSW metric is not an
Achieved IGP.

**Status:** Draft v1 — SME review required. The checks below are working
aids. They are not NCSC cut-offs. Your Competent Authority may apply
stricter criteria.

**Scope caveat.** CSW drives tiering only where it can supply evidence.
Principles marked out of scope in
[caf-mapping.md](./caf-mapping.md) (B2, B6) are not scored here —
their maturity is set by the paired IdP / training platform. No row below
marks a whole principle Achieved from CSW alone.

---

## How to use

1. Pull the latest CSW metrics via `generate_executive_report.py`.
2. For each CSW-relevant principle, read the rubric row below and pick
   the maturity tier that matches your current KPI value.
3. Record the maturity + the underlying metric + the evidence artefact in
   your CAF submission.
4. Where the CSW slice is in good shape, the principle is still Achieved
   only when the pairings in the mapping are also evidenced.

---

## Rubric

### A2 Risk Management

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No regular snapshots; CVE inventory is not tied to workloads. |
| **Partially Achieved** | Snapshots exist, but a risk owner has not used them in the risk review. |
| **Achieved** | Not reached from CSW alone. Snapshots can support the review. A2 still needs the organisation's risk method, decision-makers, and an update when things change. |

### A3 Asset Management

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | In-scope workloads that should carry an agent do not. |
| **Partially Achieved** | Agent census exists but has not been reconciled to the asset register. |
| **Achieved** | Not reached from CSW alone. Agent and package inventory cover the workloads CSW can see. A3 also includes people, data, and supporting infrastructure such as power and cooling. |

### A4 Supply Chain

| Tier | CSW-observable criteria *(CSW is supporting)* |
|---|---|
| **Not Achieved** | No vendor-package inventory; no vendor-egress visibility. |
| **Partially Achieved** | Vendor packages discoverable via CSW; vendor-tagged egress flows exist but not reconciled against TPRM contracts. |
| **Achieved** | Not reached from CSW alone. Vendor packages and vendor egress can be compared with the supplier register. The supplier-risk programme remains outside CSW. |

### B1 Policies & Processes

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | Policies on paper only; CSW in observe-only mode. |
| **Partially Achieved** | Policies authored in CSW workspaces; simulated but not enforced; no change log tied to tickets. |
| **Achieved** | Not reached from CSW alone. In-scope workload policy can be enforced and versioned. B1 also covers the wider policies, processes, procedures, communication, and exception handling. |

### B3 Data Security

| Tier | CSW-observable criteria *(CSW is supporting; pair required for Achieved)* |
|---|---|
| **Not Achieved** | No segmentation around data tiers; plaintext protocols allowed. |
| **Partially Achieved** | Data-tier segmentation enforced for some essential functions; insecure-cipher count flagged but not remediated; KMS/DLP evidence not produced alongside. |
| **Achieved** | **Requires the data-protection controls as well as CSW.** CSW can show which workload paths are allowed and which plaintext protocols were denied. It does not encrypt data or manage keys. |

### B4 System Security

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No vulnerability inventory tied to workloads. |
| **Partially Achieved** | A CVE list exists, but it is not used to decide what to patch. |
| **Achieved** | Not reached from CSW alone. Inventory can show which workloads carry a CVE and who can reach them. Patching, secure design, and removal of default credentials sit with other controls. There is no CAF patch window of 30 or 60 days. |

### B5 Resilient Networks & Systems

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | Essential-function systems are not separated from other business systems in policy. |
| **Partially Achieved** | Segregation is designed or simulated, or enforced on only some essential-function scopes. Internet services may still be reachable from those systems. |
| **Achieved** | Not reached from CSW alone. CSW can show enforced segregation and denied connections. CAF Achieved for B5.b also requires separate infrastructure, independent administration, no browsing or email from those systems, and resource and geographic mitigations. B5.c backups are a separate control. |

### C1 Security Monitoring

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No connection record for the essential-function workloads. |
| **Partially Achieved** | Connection records exist, but they are not used by the monitoring team, or they cover only some of the essential function. |
| **Achieved** | Not reached from CSW alone. Host connection records can support C1.a. Log integrity, retention, access control, and a common time source (C1.b) stay with the logging platform. |

### C2 Proactive Event Discovery

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No record of which systems communicate, and no forensic events. |
| **Partially Achieved** | Communication records exist, but unexpected paths are not investigated. |
| **Achieved** | Not reached from CSW alone. The useful CSW input is which systems should and should not communicate. Hunting, threat intelligence, and signature detection stay with the detection programme. |

### D1 Response & Recovery

| Tier | CSW-observable criteria *(CSW is supporting; backup/DR pair required for Achieved)* |
|---|---|
| **Not Achieved** | No IR playbooks reference CSW; no flow archive. |
| **Partially Achieved** | IR playbooks reference CSW flow archive for timeline reconstruction; ADM rollback tested; **but backup/DR pair not demonstrated**. |
| **Achieved** | Not reached from CSW alone. A flow history can support the timeline, and a previous policy version can be restored in an exercise. The response plan, backups, and restore test sit outside CSW. |

### D2 Lessons Learned

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | Nothing is kept that would show what changed around an incident. |
| **Partially Achieved** | Snapshots exist but are not used in the post-incident review. |
| **Achieved** | Not reached from CSW alone. A snapshot delta can support the review. Root-cause analysis and the improvement actions sit with the incident process. |

### A1 Governance

| Tier | CSW-observable criteria *(CSW is supporting; governance pair required)* |
|---|---|
| **Not Achieved** | No CSW metrics reach exec level. |
| **Partially Achieved** | Executive summary produced but not consumed by board/CISO reporting. |
| **Achieved** | **Requires the governance structure as well as a CSW summary.** A posture summary in the board pack does not create roles, resourcing, or risk appetite. |

---

## Composite CAF maturity dashboard

A one-glance view suitable for an exec readout. Pull the current CSW
metric column from `summarize_cluster_posture` (CSW MCP server) or
`generate_executive_report.py`.

| Principle | What CSW can show | Current value | Current tier | Target for the CSW slice | Gap owner |
|---|---|---|---|---|---|
| A2 | Snapshots used in the risk review | *(fill)* | *(fill)* | Slice ready | Risk Owner |
| A3 | Agent census reconciled to the asset register | *(fill)* | *(fill)* | Slice ready | Platform Eng |
| A4 | Vendor egress compared with the supplier register | *(fill)* | *(fill)* | Slice ready | TPRM Lead |
| B1 | Versioned workload policy, enforced where intended | *(fill)* | *(fill)* | Slice ready | SecOps |
| B3 | Denied plaintext paths, alongside encryption evidence | *(fill)* | *(fill)* | Slice ready | DataSec |
| B4 | CVE inventory tied to workloads | *(fill)* | *(fill)* | Slice ready | Patch Mgmt |
| B5 | Enforced segregation and denied connections | *(fill)* | *(fill)* | B5.b slice ready | NetSec + App Owners |
| C1 | Host connection records used by monitoring | *(fill)* | *(fill)* | Slice ready | SOC |
| C2 | Unexpected communication reviewed | *(fill)* | *(fill)* | Slice ready | SOC |
| D1 | Flow history available to the incident team | *(fill)* | *(fill)* | Slice ready | IR Lead |
| D2 | Snapshot delta used in the post-incident review | *(fill)* | *(fill)* | Slice ready | SecOps |
| A1 | Posture summary attached to the governance pack | *(fill)* | *(fill)* | Slice ready | Governance |

B2 and B6 are blank by design — fill them with the IdP and training-platform
tier from their respective pair.

---

## Disclaimer

Draft v1. Thresholds are proposed starting points and are not endorsed by
NCSC, Competent Authorities, or the Cabinet Office GSG. Validate with your
assessor before relying on them in a formal submission. See
[repository disclaimer](../README.md#disclaimer).
