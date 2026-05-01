# Cisco Secure Workload — SOC 2 Compliance Framework
## Technical Runbook | Enterprise Accounts

**Version:** 1.0 | **Standard:** SOC 2 Type II (AICPA Trust Services Criteria)

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

*Replace [Customer Name] and bracketed fields before customer delivery.*
