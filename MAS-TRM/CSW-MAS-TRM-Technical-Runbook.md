# Cisco Secure Workload — MAS Technology Risk Management Guidelines
## Technical Runbook | Singapore Financial Institutions

**Version:** 1.0  
**Framework:** Monetary Authority of Singapore Technology Risk Management (TRM) Guidelines  
**Use Case:** Financial-services workload segmentation, outsourcing / third-party visibility, cyber resilience evidence

---

## Reader's Guide

**Who this is for.** Singapore financial institutions and regulated financial-services providers using MAS TRM as a technology risk management baseline.

**Questions this runbook helps you answer:**

- *Can I demonstrate controlled workload connectivity for critical systems and customer-data environments?*
- *Can I produce evidence for technology asset inventory, network security, vulnerability management, and incident investigation?*
- *Can I reconcile third-party / outsourced service communication paths against approved technology risk boundaries?*

**What you'll need.** Critical system inventory, outsourcing / third-party register, CMDB or cloud inventory, network diagrams, vulnerability-management process, SIEM retention requirements, and application owner validation.

---

## 1. Overview

MAS TRM is a supervisory guideline for financial institutions' technology risk management. CSW can support technical evidence where workload visibility, microsegmentation, flow telemetry, vulnerability context, process/package inventory, and incident investigation are relevant. CSW does not replace MAS governance, board / senior management accountability, outsourcing due diligence, BCP/DR, IAM, cryptographic architecture, or regulatory notification decisions.

## 2. MAS TRM Topic Map

| MAS TRM topic | CSW can support evidence for | Boundary |
|---|---|---|
| Technology asset inventory | Workload inventory, labels, application scopes, cloud connector context | Reconcile with official CMDB / asset register |
| Network security | Workload-level segmentation, deny-by-default policy, approved-flow baselines | Perimeter / internet controls remain firewall/SASE-owned |
| Vulnerability management | CVE / package exposure context, reachability-informed prioritization | Scanner ownership and SLA governance remain customer-owned |
| Security monitoring | Flow/process telemetry and SIEM export | SOC process and alert adjudication remain customer-owned |
| Incident response | Flow timeline, process context, quarantine / containment evidence | Legal/regulatory notification remains customer-owned |
| Outsourcing / third-party risk | Supplier egress visibility and approved endpoint mapping | Contractual controls and supplier assurance remain GRC-owned |

## 3. Suggested Scope Pattern

```text
MAS-TRM
├── Critical-Systems
│   ├── Digital-Banking
│   ├── Payments
│   ├── Trading
│   └── Core-Platforms
├── Customer-Data
│   ├── Data-Stores
│   └── Analytics
├── Security-Services
│   ├── Identity
│   ├── Monitoring
│   └── Patch-Management
└── Outsourced-Third-Parties
```

## 4. Deployment Checklist

- [ ] Identify one critical system or customer-data application for the pilot.
- [ ] Confirm workloads can be instrumented or discovered through supported connectors.
- [ ] Align labels to business service, environment, owner, data class, and criticality.
- [ ] Define a normal observation window that captures month-end or batch processing if relevant.
- [ ] Export observed flows and validate dependencies with the application owner.
- [ ] Generate candidate policy through ADM and review before enforcement.

## 5. Evidence Package

- Critical-system workload inventory.
- Scope and label export.
- Approved and observed flow comparison.
- Third-party / outsourced egress summary.
- High-risk port and plaintext protocol findings.
- Vulnerability exposure summary.
- ADM policy candidate and exception register.
- Incident-response timeline sample from flow/process telemetry.

## 6. Complementary Controls

Pair CSW evidence with IAM/MFA, PAM, SIEM/SOAR, vulnerability scanners, GRC/outsourcing workflow, firewall/SASE controls, backup/DR testing, and cryptographic key-management evidence.

## 7. Assessor / Regulator Caveat

MAS TRM is principle- and outcome-oriented. Validate final evidence format and supervisory expectations with the institution's risk, compliance, legal, and audit teams.
