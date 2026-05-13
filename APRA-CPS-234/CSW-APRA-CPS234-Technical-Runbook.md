# Cisco Secure Workload — APRA CPS 234
## Technical Runbook | Australian Prudentially Regulated Entities

**Version:** 1.0  
**Framework:** APRA Prudential Standard CPS 234 — Information Security  
**Use Case:** Critical information asset segmentation, control testing, incident evidence, third-party dependency visibility

---

## Reader's Guide

**Who this is for.** Australian banks, insurers, superannuation trustees, and other APRA-regulated entities aligning workload controls to CPS 234.

**Questions this runbook helps you answer:**

- *Can I identify and protect workloads that support critical or sensitive information assets?*
- *Can I show that segmentation controls operate as designed and are tested?*
- *Can I produce investigation evidence for material information security incidents?*
- *Can I see service-provider communication paths that support critical operations?*

**What you'll need.** Information asset classification, materiality / criticality ratings, supplier register, control-testing cadence, incident-response workflow, CMDB/cloud inventory, and application ownership data.

---

## 1. Overview

APRA CPS 234 requires regulated entities to maintain information security capabilities commensurate with threats and vulnerabilities, protect information assets, test controls, and notify APRA of material incidents. CSW can support the technical evidence layer for workloads and cloud/server assets in scope. It does not replace board accountability, information-security governance, supplier assurance, IAM/PAM, endpoint protection, or regulatory notification decisions.

## 2. CPS 234 Requirement Map

| CPS 234 area | CSW can support evidence for | Boundary |
|---|---|---|
| Information asset identification | Workload inventory, labels, application scopes | Official asset register remains authoritative |
| Control implementation | Segmentation policy, deny-by-default allowlists, scope-based enforcement | IAM, endpoint, physical, and process controls remain complementary |
| Control testing | Policy simulation, flow drift review, evidence exports | Formal test plan and sign-off remain customer-owned |
| Incident management | Flow/process timeline and affected workload scoping | APRA notification decision remains governance/legal-owned |
| Service provider management | Third-party egress and dependency visibility | Contractual assurance remains supplier-risk-owned |

## 3. Suggested Scope Pattern

```text
APRA-CPS234
├── Critical-Information-Assets
│   ├── Customer-Data
│   ├── Payments
│   ├── Core-Systems
│   └── Analytics
├── Material-Operations
│   ├── Digital-Channels
│   ├── Identity
│   └── Monitoring
├── Service-Providers
└── Incident-Evidence
```

## 4. POV Steps

- [ ] Select one critical information asset or material operation.
- [ ] Install CSW sensors / connectors for representative workloads.
- [ ] Apply labels: `asset_class`, `criticality`, `owner`, `env`, `service_provider`, `data_class`.
- [ ] Run observation window and validate dependencies with application owners.
- [ ] Identify unexpected access, high-risk ports, and supplier egress.
- [ ] Generate policy candidate and run simulation.
- [ ] Package evidence against CPS 234 control testing and incident-response needs.

## 5. Evidence Package

- Critical information asset workload inventory.
- Scope and label hierarchy.
- Dependency map and third-party egress summary.
- Control testing export: observed vs allowed flows.
- Policy simulation result.
- Vulnerability exposure and high-risk communication findings.
- Incident scoping example: affected workloads, processes, and flows.

## 6. Complementary Controls

Use CSW with IAM/MFA, PAM, EDR, vulnerability scanners, SIEM/SOAR, ServiceNow/GRC, supplier-risk management, backup/DR, and APRA reporting procedures.

## 7. Assessor Caveat

CPS 234 is an APRA prudential standard. Validate evidence sufficiency with risk, compliance, internal audit, legal, and any appointed assessors.
