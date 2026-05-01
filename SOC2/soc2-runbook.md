# Cisco Secure Workload — SOC 2 Compliance Framework
## Technical Runbook | Enterprise Accounts

**Version:** 1.0 | **Standard:** SOC 2 Type II (AICPA Trust Services Criteria)

---

## Reader's Guide

**Who this is for.** Service organizations preparing for or maintaining
an annual SOC 2 Type II attestation, the security/GRC teams who own
the report, and Cisco SAs supporting them.

**Questions this runbook helps you answer:**

- *Which Common Criteria controls can I evidence with continuous data
  rather than point-in-time samples? Type II auditors increasingly
  prefer the former.* (CC6.1, CC6.6, CC7.2)
- *When my auditor asks me to prove a segmentation control "operated
  effectively throughout the period", what does the artifact look
  like?* (CC6.1, CC6.6)
- *When a customer in due diligence asks "is workload X isolated from
  workload Y?", can I prove it from live data instead of a network
  diagram?* (CC6.1, CC6.7)
- *Are my privileged access changes producing the artifact format my
  auditor's evidence template expects?* (CC6.2, CC6.3)
- *For my Availability or Confidentiality TSC additions, what do I gain
  from workload-level telemetry that I don't get today?*

**What you'll need.** A defined trust boundary (system description),
your current TSC selection, and your auditor's evidence request list
or last year's PBC list.

**Where to start.** Section 1 for the TSC↔CSW capability map; sections
2–3 to design evidence collection; sections 4–5 if you're inside the
audit window.

---

## 1. Overview

SOC 2 Type II audits evaluate whether security controls operated effectively over a defined period (typically 6–12 months). Cisco Secure Workload (CSW) directly addresses the **Security** Trust Services Criteria (TSC) and contributes to **Availability**, **Confidentiality**, and **Processing Integrity** criteria through workload visibility, micro-segmentation, vulnerability detection, and forensic telemetry.

### SOC 2 TSC to CSW Capability Map

| Trust Services Criteria | CSW Capability |
|---|---|
| CC6 — Logical & Physical Access | Micro-segmentation, scope-based access enforcement |
| CC7 — System Operations | Anomaly detection, vulnerability scanning, alerting |
| CC8 — Change Management | Policy workspace versioning, ADM drift detection |
| CC9 — Risk Mitigation | Vulnerability prioritization, compensating controls |
| A1 — Availability | Workload health monitoring, sensor telemetry |
| C1 — Confidentiality | PHI/PII zone isolation, encryption enforcement |

---

## 2. SOC 2 Audit Preparation with CSW

### 2.1 Evidence Collection Timeline

SOC 2 Type II requires evidence across the **entire audit period**. Configure CSW from Day 1:

- Enable full flow telemetry retention (minimum 12 months)
- Enable policy workspace audit logging
- Schedule monthly vulnerability scan exports
- Configure alert export to SIEM for centralized evidence collection

### 2.2 Key Control Areas

**CC6.1 — Logical Access Controls**
- CSW enforces workload-level allowlist policies
- Every inbound connection to sensitive workloads requires explicit policy approval
- Policy violations logged with source, destination, process, and timestamp

**CC6.6 — Network and Infrastructure Controls**
- ADM discovers all communication paths — no undocumented flows
- Micro-segmentation enforces least-privilege network access
- External access paths (third-party, partner) isolated in dedicated CSW scopes

**CC6.7 — Transmission of Confidential Information**
- CSW detects unencrypted transmission (HTTP, FTP, plain LDAP)
- Alerts trigger on any plaintext flow from confidential data scopes
- Encryption compliance report available for auditor evidence package

**CC7.1 — Detection of Vulnerabilities**
- Continuous CVE scanning on all in-scope workloads
- CVSS-scored reports with workload-level attribution
- Remediation tracking via policy compensating controls

**CC7.2 — Monitoring of System Components**
- Full process and network telemetry across all monitored workloads
- Anomaly detection alerts on baseline deviation
- Sensor health monitoring — alerts on agent offline events

**CC7.3 — Evaluation of Security Events**
- Forensic telemetry supports security event investigation
- Process-level audit trail: what ran, when, what it connected to
- Flow search enables retrospective query across audit period

---

## 3. CSW Deployment for SOC 2

### 3.1 Scope Definition

Define CSW scopes aligned to SOC 2 system boundaries:

```
Root Scope
└── SOC2-Boundary (audit scope)
    ├── Production-Systems (primary controls)
    │   ├── Application-Servers
    │   ├── Databases
    │   └── APIs
    ├── Supporting-Infrastructure
    │   ├── Auth-Systems (LDAP/SSO)
    │   └── Monitoring-Stack
    └── Third-Party-Integrations
        └── Vendor-Connections
```

### 3.2 Policy Requirements per CC Control

| CC Control | CSW Policy Requirement |
|---|---|
| CC6.1 | Default-deny inbound to Production-Systems scope |
| CC6.6 | Explicit allowlist for all inter-service communication |
| CC6.7 | Block HTTP/FTP from Production-Systems; enforce HTTPS |
| CC7.1 | Vulnerability scan enabled on all SOC2-Boundary workloads |
| CC7.2 | Anomaly detection alert on all Production-Systems |
| CC8.1 | Policy changes require approval workflow; audit logged |

### 3.3 Continuous Monitoring Setup

```
CSW UI → Defend → Alerts
  → New Alert Policy
  → Scope: SOC2-Boundary
  → Triggers:
    - Policy violation (any)
    - New vulnerability CVSS ≥ 7.0
    - Sensor offline > 5 minutes
    - Anomalous flow (ADM baseline deviation)
  → Notify: SIEM webhook + email to security team
```

---

## 4. Evidence Package for SOC 2 Auditors

| Evidence Item | CSW Source | CC Control | Frequency |
|---|---|---|---|
| Access control policy export | Defend → Policy Workspaces | CC6.1 | Per audit request |
| Policy violation log | Alerts → Triggered Events | CC6.1, CC6.6 | Monthly export |
| Vulnerability scan report | Investigate → Vulnerability | CC7.1, CC9.1 | Weekly |
| Network flow audit log | Investigate → Flow Search | CC6.7, CC7.2 | Continuous |
| Anomaly alert log | Alerts → Dashboard | CC7.2, CC7.3 | Monthly |
| ADM application map | Investigate → ADM | CC6.6, CC8.1 | Quarterly |
| Sensor health report | Manage → Agents | CC7.2, A1.1 | Monthly |
| Policy change audit trail | Policy workspace history | CC8.1 | Per change |

---

## 5. Common SOC 2 Audit Findings CSW Addresses

| Auditor Finding | CSW Remediation |
|---|---|
| Undocumented network access paths | ADM generates complete dependency map as evidence |
| No workload-level access controls | Micro-segmentation enforces and logs all access |
| Undetected lateral movement | Anomaly detection + forensic telemetry |
| No evidence of encryption enforcement | Protocol-level flow analysis + block policy |
| Vulnerability management gaps | Continuous CVE scan with CVSS prioritization |
| Insufficient logging | Full process + network telemetry across audit period |

---

## Related Frameworks

- [ISO/IEC 27001:2022](../ISO-27001-2022/iso27001-runbook.md) — the international ISMS counterpart; many organisations pursue SOC 2 + ISO 27001 jointly.
- [NIST SP 800-53 Rev 5](../NIST-800-53/nist-runbook.md) — for cross-mapping CC-series criteria to a federal control catalogue.
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) — the ZTA pattern underneath CC6 logical access and CC7 system operations.

---

*Replace [Customer Name] and bracketed fields before customer delivery.*
