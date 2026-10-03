# CAF IGP Maturity Scorer — CSW-driven

**Purpose.** Translate CSW KPIs into CAF maturity tiers — **Achieved**,
**Partially Achieved**, or **Not Achieved** — per principle. Lets a CAF
Lead Assessor turn "our enforcement coverage is 88%" into a defensible
IGP position.

**Status:** Draft v1 — SME review required. Thresholds are starting
points, not NCSC-endorsed cut-offs. Your Competent Authority may apply
stricter criteria.

**Scope caveat.** CSW drives tiering only where CSW is the primary or
supporting evidence source. Principles marked ⚪ Out-of-scope in
[caf-mapping.md](./caf-mapping.md) (B2, B6) are not scored here —
their maturity is set by the paired IdP / training platform.

---

## How to use

1. Pull the latest CSW metrics via `generate_executive_report.py`.
2. For each CSW-relevant principle, read the rubric row below and pick
   the maturity tier that matches your current KPI value.
3. Record the maturity + the underlying metric + the evidence artefact in
   your CAF submission.
4. Where CSW alone cannot push a principle to Achieved (B3, D1), the
   rubric names the complementary control(s) required.

---

## Rubric

### A2 Risk Management

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No regular CSW snapshots; no blast-radius score; CVE inventory not tied to workloads. |
| **Partially Achieved** | Monthly `cluster_snapshot.py` running; blast-radius score produced but not reviewed by risk owner; CVE inventory produced but not prioritised by CVM intel. |
| **Achieved** | Monthly snapshot + exec report **reviewed and signed off** by risk owner; CVM-prioritised CVE register; `cluster_delta` showing quarter-over-quarter trend; risk decisions traced back to CSW evidence. |

### A3 Asset Management

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | <80% of in-scope workloads have CSW agent installed. |
| **Partially Achieved** | 80–94% agent coverage; agent census not reconciled against CMDB. |
| **Achieved** | ≥95% agent coverage on in-scope workloads; monthly reconciliation against CMDB with gaps triaged; package inventory present for all agents. |

### A4 Supply Chain

| Tier | CSW-observable criteria *(CSW is supporting)* |
|---|---|
| **Not Achieved** | No vendor-package inventory; no vendor-egress visibility. |
| **Partially Achieved** | Vendor packages discoverable via CSW; vendor-tagged egress flows exist but not reconciled against TPRM contracts. |
| **Achieved** | Vendor-package register maintained; vendor egress reconciled quarterly against TPRM contract list; deviations flagged into TPRM workflow. |

### B1 Policies & Processes

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | Policies on paper only; CSW in observe-only mode. |
| **Partially Achieved** | Policies authored in CSW workspaces; simulated but not enforced; no change log tied to tickets. |
| **Achieved** | Policies enforced in-kernel on all in-scope workloads; ADM version history linked to change tickets; rejected-flow log reviewed on a defined cadence. |

### B3 Data Security

| Tier | CSW-observable criteria *(CSW is supporting; pair required for Achieved)* |
|---|---|
| **Not Achieved** | No segmentation around data tiers; plaintext protocols allowed. |
| **Partially Achieved** | Data-tier segmentation enforced for some essential functions; insecure-cipher count flagged but not remediated; KMS/DLP evidence not produced alongside. |
| **Achieved** | **Requires CSW + KMS + DLP + classification.** CSW shows: data-tier segmentation enforced across all CAF scopes; plaintext-protocol deny policies active for PII/ePHI classes; insecure-cipher count = 0 or on a remediation plan. |

### B4 System Security

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No CSW vuln inventory; no agent-version tracking. |
| **Partially Achieved** | Monthly `generate_vuln_report.py` produced; vuln list exists but no prioritisation by exploit intel; agent-version drift not actively managed. |
| **Achieved** | CVM-prioritised CVE queue tied to patch SLAs (Critical ≤30d, High ≤60d); patch-after metric trending down; agent-version drift ≤1 minor version across fleet; policy denies known-vulnerable service ports. |

### B5 Resilient Networks & Systems *(CSW core; strongest row)*

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No microsegmentation enforced; blast-radius score ≤30. |
| **Partially Achieved** | Microsegmentation enforced on some CAF scopes but not all; blast-radius 31–74; IT/OT boundary not explicitly scored. |
| **Achieved** | Microsegmentation enforced across all CAF essential-function scopes; blast-radius ≥75; explicit scope-isolation attestation between IT and OT scopes (pair with Cyber Vision for OT tier); ADM-approved baselines in production. |

### C1 Security Monitoring

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No CSW flow telemetry retained; no SIEM egress. |
| **Partially Achieved** | Flow telemetry retained ≤30d; SIEM egress exists but not consumed in SOC playbooks. |
| **Achieved** | Flow + policy-decision + process telemetry retained for Competent Authority-required duration (sector-dependent; often 12 months); SIEM egress feeds documented SOC playbooks; cluster NTP synchronised; agent health monitored. |

### C2 Proactive Event Discovery

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No forensics profiles active; no MITRE coverage tracking. |
| **Partially Achieved** | Forensics profiles active on some agents; MITRE coverage map exists but gaps not triaged. |
| **Achieved** | Forensics profiles active on all in-scope agents; MITRE coverage map reviewed quarterly with targeted rule additions; rejected-flow anomalies drive SOC investigations; vuln scanning + threat intel integrated. |

### D1 Response & Recovery

| Tier | CSW-observable criteria *(CSW is supporting; backup/DR pair required for Achieved)* |
|---|---|
| **Not Achieved** | No IR playbooks reference CSW; no flow archive. |
| **Partially Achieved** | IR playbooks reference CSW flow archive for timeline reconstruction; ADM rollback tested; **but backup/DR pair not demonstrated**. |
| **Achieved** | **Requires CSW + backup/DR + tested IR runbooks.** CSW shows: blast-radius containment demonstrated in tabletop exercise; flow archive retrieved under IR within SLA; ADM version rollback rehearsed. Must pair with a backup/DR Achieved. |

### D2 Improvements

| Tier | CSW-observable criteria |
|---|---|
| **Not Achieved** | No CSW metrics tracked over time. |
| **Partially Achieved** | `cluster_delta.py` run between some snapshots but not fed into formal lessons-learned. |
| **Achieved** | Quarterly `cluster_delta.py` + exec-summary trends fed into formal lessons-learned / post-incident-review process; policy changes traced to specific findings. |

### A1 Governance

| Tier | CSW-observable criteria *(CSW is supporting; governance pair required)* |
|---|---|
| **Not Achieved** | No CSW metrics reach exec level. |
| **Partially Achieved** | Executive summary produced but not consumed by board/CISO reporting. |
| **Achieved** | **Requires CSW metrics + defined governance structure.** CSW shows: exec summary consumed in defined cadence (monthly/quarterly) by named governance body; metrics tied to risk-appetite statements. |

---

## Composite CAF maturity dashboard

A one-glance view suitable for an exec readout. Pull the current CSW
metric column from `summarize_cluster_posture` (CSW MCP server) or
`generate_executive_report.py`.

| Principle | CSW metric driving tier | Current value | Current tier | Target tier | Gap owner |
|---|---|---|---|---|---|
| A2 | Monthly snapshot + exec review | *(e.g. in place, signed off)* | *(fill)* | Achieved | Risk Owner |
| A3 | % workloads with agent | *(e.g. 97%)* | *(fill)* | Achieved | Platform Eng |
| A4 | TPRM reconciliation cadence | *(e.g. quarterly)* | *(fill)* | Achieved | TPRM Lead |
| B1 | Enforcement % + change-log cadence | *(e.g. 88% enforced)* | *(fill)* | Achieved | SecOps |
| B3 | Insecure-cipher count + KMS pair | *(e.g. 12 hosts; KMS: yes)* | *(fill)* | Achieved | DataSec |
| B4 | CVM-prioritised patch SLA attainment | *(e.g. 92%)* | *(fill)* | Achieved | Patch Mgmt |
| B5 | Blast-radius score | *(e.g. 78)* | *(fill)* | Achieved (≥75) | NetSec + App Owners |
| C1 | Flow retention + SIEM playbook | *(e.g. 180d retention)* | *(fill)* | Achieved | SOC |
| C2 | MITRE coverage review cadence | *(e.g. quarterly)* | *(fill)* | Achieved | SOC |
| D1 | IR tabletop + backup pair | *(e.g. tabletop Q2; backup Achieved)* | *(fill)* | Achieved | IR Lead |
| D2 | Quarterly delta into PIR | *(e.g. in place)* | *(fill)* | Achieved | SecOps |
| A1 | Exec summary consumption | *(e.g. monthly to CISO)* | *(fill)* | Achieved | Governance |

B2 and B6 are blank by design — fill them with the IdP and training-platform
tier from their respective pair.

---

## Disclaimer

Draft v1. Thresholds are proposed starting points and are not endorsed by
NCSC, Competent Authorities, or the Cabinet Office GSG. Validate with your
assessor before relying on them in a formal submission. See
[repository disclaimer](../README.md#disclaimer).
