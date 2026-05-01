# Cisco Secure Workload — PCI DSS v4.0 Compliance Framework
## Technical Runbook | Payment Card Industry Accounts

**Version:** 1.0 | **Standard:** PCI DSS v4.0 (March 2022)

---

## 1. Overview

PCI DSS v4.0 introduces customized implementation approaches and strengthens network segmentation requirements. CSW is uniquely positioned to satisfy PCI DSS Requirements 1 (network controls), 6 (vulnerability management), 10 (logging/monitoring), and 11 (security testing) through workload-level visibility and enforcement.

### PCI DSS Requirement → CSW Capability Map

| PCI Requirement | CSW Capability |
|---|---|
| Req 1 — Network Security Controls | Micro-segmentation, CDE isolation |
| Req 2 — Secure Configurations | Vulnerability detection, process monitoring |
| Req 6 — Vulnerability Management | Continuous CVE scanning, CVSS prioritization |
| Req 7 — Access Control | Workload-level allowlist enforcement |
| Req 10 — Logging & Monitoring | Full flow + process telemetry |
| Req 11 — Security Testing | ADM baseline deviation detection |

---

## 2. Cardholder Data Environment (CDE) Scoping

### 2.1 CDE Scope Architecture

```
Root Scope
└── PCI-Environment
    ├── CDE (Cardholder Data Environment) — strictest controls
    │   ├── PAN-Storage (databases storing card data)
    │   ├── Payment-Processing (apps that process PANs)
    │   ├── Payment-Gateways
    │   └── HSM-Servers
    ├── CDE-Connected (systems that connect to CDE)
    │   ├── Web-Servers (front-end payment pages)
    │   ├── Auth-Servers
    │   └── Logging-Infra
    ├── Out-of-Scope (isolated from CDE)
    │   └── Corporate-Systems
    └── Third-Party-Processors (PCI-compliant vendors)
```

### 2.2 Scope Reduction Strategy

CSW helps reduce PCI scope by proving isolation:
- ADM confirms zero communication between CDE and out-of-scope systems
- Policy enforcement blocks any unapproved CDE connections
- Segment isolation evidence available for QSA (Qualified Security Assessor)

---

## 3. PCI DSS v4.0 Control Implementation

### Requirement 1 — Network Security Controls

**1.2.1 — Configuration standards for network controls**
```
CSW Policy: CDE-Isolation
  DENY: Any → CDE (default deny all inbound)
  ALLOW: Web-Servers → Payment-Processing (port 443 only)
  ALLOW: Payment-Processing → PAN-Storage (port 5432/1521 — encrypted)
  ALLOW: Auth-Servers → CDE (port 636 LDAPS only)
  DENY: CDE → Internet (no direct internet access)
  LOG: All policy violations with full context
```

**1.3.1 — Inbound traffic to CDE restricted**
- CSW enforces allowlist-only inbound to CDE scope
- Any unlisted source attempting CDE access triggers immediate alert

**1.3.2 — Outbound traffic from CDE restricted**
- CDE workloads blocked from initiating internet connections
- Only approved outbound paths (monitoring, logging) explicitly allowed

**1.4.1 — Network controls between CDE and untrusted networks**
- CSW micro-segmentation enforces at workload level — not just perimeter
- ADM provides continuous mapping of CDE communication paths

### Requirement 6 — Vulnerability Management

**6.3.3 — All software protected from known vulnerabilities**
```
CSW UI → Investigate → Vulnerability Report
  → Scope: CDE
  → Filter CVSS ≥ 4.0
  → Export: CSV for tracking

Remediation SLAs:
  Critical (CVSS 9.0+): 24 hours
  High (CVSS 7.0-8.9): 7 days
  Medium (CVSS 4.0-6.9): 30 days
```

**6.4.1 — Web-facing applications protected**
- CSW monitors all inbound flows to web-facing CDE workloads
- Anomalous request patterns surfaced via forensic telemetry

### Requirement 7 — Access Control

**7.2.1 — Access to system components and cardholder data restricted**
- CSW scope-based policy: only approved workload identities access CDE
- Policy enforced at OS level — bypasses firewall rule gaps
- Process-level access audit: which process on which workload touched CDE

**7.2.5 — Default and unnecessary accounts removed**
- CSW process monitoring detects unexpected processes on CDE workloads
- Alert on new process hash not seen in ADM baseline

### Requirement 10 — Logging & Monitoring

**10.2.1 — Audit logs capture required events**
```
CSW captures per CDE workload:
  - All inbound/outbound network connections (source, dest, port, protocol)
  - Process activity (name, hash, parent process, user context)
  - Policy violations (blocked connections with full 5-tuple)
  - Anomaly events (baseline deviations)
```

**10.3.1 — Audit logs protected from destruction**
- CSW telemetry stored in tamper-resistant cluster storage
- Export pipeline to immutable SIEM/SYSLOG for long-term retention
- PCI DSS requires 12-month retention (3 months immediately available)

**10.4.1 — Audit logs reviewed daily**
- CSW dashboard provides daily summary of CDE events
- Automated alert export to SOC/SIEM eliminates manual review burden

### Requirement 11 — Security Testing

**11.3.1 — External vulnerability scans quarterly**
- CSW provides continuous (not just quarterly) vulnerability assessment
- Exceeds PCI DSS requirement; use CSW reports as supplementary evidence

**11.4.1 — Penetration testing methodology**
- ADM baseline used as pre-pentest reference
- Post-pentest ADM comparison detects any new paths discovered
- Forensic telemetry captures all pentest activity for review

---

## 4. Evidence Package for QSA

| Evidence Item | CSW Source | PCI Requirement | Frequency |
|---|---|---|---|
| CDE network policy export | Defend → Policy Workspaces | Req 1 | Per assessment |
| CDE inbound/outbound flow log | Investigate → Flow Search | Req 1, Req 10 | Continuous |
| Policy violation report | Alerts → Triggered Events | Req 10 | Monthly |
| Vulnerability scan (CDE) | Investigate → Vulnerability | Req 6, Req 11 | Weekly |
| CDE scope membership snapshot | Inventory → Export | Req 1, Req 7 | Monthly |
| Anomaly detection log | Alerts → Dashboard | Req 10, Req 11 | Monthly |
| ADM dependency map (CDE) | Investigate → ADM | Req 1 | Quarterly |
| Process audit log (CDE) | Investigate → Process Search | Req 10 | On-demand |

---

## 5. PCI DSS v4.0 New Requirements CSW Addresses

| New in v4.0 | CSW Response |
|---|---|
| 12.3.2 — Targeted risk analysis for each requirement | CSW vulnerability + ADM data feeds risk analysis |
| 1.2.1 — All traffic flows documented and approved | ADM generates complete approved flow documentation |
| 6.3.3 — All vulnerabilities addressed per risk ranking | Continuous CVE scan with CVSS-ranked remediation |
| 10.7.2 — Failures of critical security controls detected | Sensor offline alerts, policy enforcement gap detection |

---

*Replace [Customer Name] and bracketed fields before customer delivery.*
