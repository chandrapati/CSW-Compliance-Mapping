# Cisco Secure Workload — NIST 800-53 Rev 5 Compliance Framework
## Technical Runbook | Federal & Enterprise Accounts

**Version:** 1.0 | **Standard:** NIST SP 800-53 Rev 5 (CSW-Relevant Control Families)

---

## Reader's Guide

**Who this is for.** Federal agencies (civilian and DoD), FedRAMP
applicants, and enterprises that have adopted 800-53 as a security
overlay, plus the assessors and Cisco SAs supporting them.

**Questions this runbook helps you answer:**

- *For my system's impact level (LOW / MODERATE / HIGH), which AC, AU,
  CM, and SC controls become continuous monitoring rather than
  periodic-assessment items?* (CA-7)
- *Can my POA&M be partially burned down through automated CSW
  evidence rather than manual remediation tracking?* (CA-5, RA-5)
- *For SC-7 boundary protection, what is my evidence at the workload
  tier — distinct from perimeter firewalls and CSPM?*
- *For SI-4 system monitoring, can I show end-to-end visibility from
  process initiation through network conversation to data store?*
- *If my assessor wants machine-readable artifacts (OSCAL-adjacent),
  what does CSW produce vs. what still requires narrative
  documentation?*

**What you'll need.** Your system's FIPS 199 categorization, a current
or draft System Security Plan (SSP), your control overlay if any
(e.g., HIGH baseline, FedRAMP Mod), and your assessor's evidence
format expectations.

**Where to start.** Section 2 walks the seven control families CSW
addresses most directly; section 3 maps coverage by impact level; go
to section 4 if you're building the evidence package now.

---

## 1. Overview

NIST SP 800-53 Rev 5 provides a comprehensive catalog of security and privacy controls for federal information systems. CSW directly addresses controls across seven key families: **AC** (Access Control), **AU** (Audit & Accountability), **CM** (Configuration Management), **IR** (Incident Response), **RA** (Risk Assessment), **SC** (System & Communications Protection), and **SI** (System & Information Integrity).

---

## 2. Control Family Mapping

### AC — Access Control

| Control | Name | CSW Implementation |
|---|---|---|
| AC-3 | Access Enforcement | Micro-segmentation enforces allowlist policies at workload level |
| AC-4 | Information Flow Enforcement | ADM maps all flows; policy blocks unauthorized paths |
| AC-6 | Least Privilege | Workload-scoped policies grant minimum required network access |
| AC-17 | Remote Access | Jump-host enforcement; remote admin paths explicitly defined and logged |
| AC-20 | Use of External Systems | External partner scope with restricted, audited access paths |

**CSW Implementation:**
```
CSW UI → Defend → Segmentation
  → Policy type: Allowlist (default deny)
  → Scope: target workload group
  → Document each allowed flow with business justification
  → Export policy for AC-3/AC-4 control evidence
```

### AU — Audit & Accountability

| Control | Name | CSW Implementation |
|---|---|---|
| AU-2 | Event Logging | Full network flow + process telemetry on all monitored workloads |
| AU-3 | Content of Audit Records | 5-tuple flows + process name + user context + timestamp |
| AU-6 | Audit Record Review | Alerts export to SIEM for automated review; anomaly detection |
| AU-9 | Protection of Audit Information | CSW telemetry stored in tamper-resistant cluster |
| AU-12 | Audit Record Generation | Continuous logging; configurable retention (recommend 3 years for federal) |

**Log Content per AU-3:**
- Source/destination IP and port
- Protocol and direction
- Process name and hash
- Parent process context
- User context (where OS supports)
- Policy action (allow/deny/alert)
- Timestamp (UTC, microsecond precision)

### CM — Configuration Management

| Control | Name | CSW Implementation |
|---|---|---|
| CM-2 | Baseline Configuration | ADM establishes approved communication baseline |
| CM-6 | Configuration Settings | Process monitoring detects configuration drift (new processes, new ports) |
| CM-7 | Least Functionality | Block non-approved services via port-level policy enforcement |
| CM-8 | System Component Inventory | CSW inventory provides real-time workload asset catalog |

**Baseline Drift Detection:**
```
CSW UI → Investigate → ADM
  → Re-run ADM quarterly
  → Compare to previous baseline
  → New flows = configuration change review required
  → Policy workspace updated to reflect approved changes
```

### IR — Incident Response

| Control | Name | CSW Implementation |
|---|---|---|
| IR-4 | Incident Handling | Forensic telemetry enables full incident reconstruction |
| IR-5 | Incident Monitoring | Real-time anomaly alerts; policy violation events |
| IR-6 | Incident Reporting | Alert export to SIEM/SOAR for automated incident ticket creation |
| IR-10 | Integrated Information Security Analysis | CSW correlates network + process + vulnerability context per incident |

**Forensic Investigation Workflow:**
```
1. Alert triggered → CSW alert with workload ID, time, flow context
2. Flow Search → reconstruct all connections from/to affected workload
3. Process Search → identify anomalous processes + parent chain
4. Vulnerability Report → identify exploited CVE if applicable
5. Export → full forensic package for IR team
```

### RA — Risk Assessment

| Control | Name | CSW Implementation |
|---|---|---|
| RA-3 | Risk Assessment | Vulnerability data + ADM attack surface = continuous risk posture |
| RA-5 | Vulnerability Monitoring | Continuous CVE scanning with CVSS scoring |
| RA-7 | Risk Response | Compensating controls via policy when patching delayed |
| RA-9 | Criticality Analysis | Scope-based tagging identifies high-criticality workloads |

### SC — System & Communications Protection

| Control | Name | CSW Implementation |
|---|---|---|
| SC-7 | Boundary Protection | Micro-segmentation enforces east-west boundaries |
| SC-8 | Transmission Confidentiality | Detect and block unencrypted sensitive data flows |
| SC-28 | Protection of Information at Rest | Identify workloads with unencrypted storage access paths |
| SC-39 | Process Isolation | Workload-level policy ensures process-to-process isolation |

### SI — System & Information Integrity

| Control | Name | CSW Implementation |
|---|---|---|
| SI-2 | Flaw Remediation | Continuous vulnerability scan; prioritized remediation guidance |
| SI-3 | Malicious Code Protection | Process hash monitoring detects unknown/malicious executables |
| SI-4 | System Monitoring | Full telemetry with anomaly detection and alerting |
| SI-7 | Software & Firmware Integrity | Process hash baseline from ADM; deviation triggers alert |

---

## 3. NIST Impact Level Guidance

| Impact Level | CSW Configuration |
|---|---|
| Low | ADM + monitoring only; simulation policies |
| Moderate | ADM + enforcement on sensitive scopes; full alerting |
| High | ADM + full enforcement; process-level monitoring; 3-year telemetry retention |

---

## 4. Evidence Package

| Evidence Item | CSW Source | Control Family | Frequency |
|---|---|---|---|
| Policy enforcement log | Defend → Policy Workspaces | AC | Per audit |
| Network flow audit log | Investigate → Flow Search | AU | Continuous |
| Vulnerability report | Investigate → Vulnerability | RA, SI | Weekly |
| ADM baseline map | Investigate → ADM | CM | Quarterly |
| Alert/incident log | Alerts → Dashboard | IR | Monthly |
| Workload inventory | Manage → Inventory | CM | Monthly |
| Process anomaly report | Investigate → Process Search | SI | On-demand |

---

## Related Frameworks

- [ISO/IEC 27001:2022](../ISO-27001-2022/iso27001-runbook.md) — the international counterpart for organisations cross-mapping 800-53 to ISO Annex A.
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) — the ZTA architectural overlay on top of the 800-53 control catalogue.
- [NIST SP 800-207A](../NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md) — the logical-component view that operationalises AC, SI, SC families.
- [FIPS 140](../FIPS-140/fips-runbook.md) — SC-13 cryptographic-protection requirement for the 800-53 baselines.
- [HIPAA](../HIPAA/CSW-HIPAA-Technical-Runbook.md) — for healthcare entities that satisfy §164.306 via 800-53 mapping.

---

*Replace [Customer Name] and bracketed fields before customer delivery.*
