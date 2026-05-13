# Cisco Secure Workload — BSI C5
## Technical Runbook | Cloud Computing Compliance Criteria Catalogue

**Version:** 1.0  
**Framework:** BSI C5 — Cloud Computing Compliance Criteria Catalogue  
**Use Case:** Cloud service provider and cloud customer workload segmentation, cloud tenant evidence, monitoring, and vulnerability context

---

## Reader's Guide

**Who this is for.** Cloud service providers, SaaS operators, and cloud customers using BSI C5 as a cloud assurance baseline, especially in German or EU-aligned assurance contexts.

**Questions this runbook helps you answer:**

- *Can I produce workload-level evidence for cloud network segmentation and tenant/service isolation?*
- *Can I reconcile cloud inventory, application scopes, vulnerability context, and monitoring evidence?*
- *Can I show supplier/customer communication paths and incident investigation artifacts?*

**What you'll need.** Cloud architecture, C5 scope statement, tenant/service boundary definition, cloud account inventory, CMDB or tag model, SIEM retention, vulnerability process, and shared-responsibility model.

---

## 1. Overview

BSI C5 provides cloud assurance criteria across organization, security policies, asset management, cryptography, operations, communication security, vulnerability handling, incident management, and portability/interoperability. CSW can support technical evidence for cloud/server workloads where visibility, segmentation, vulnerability context, telemetry, and policy evidence apply. It does not replace the auditor's attestation, cloud provider controls, IAM, cryptography, backup/DR, or governance requirements.

## 2. C5 Topic Map

| C5 topic | CSW can support evidence for | Boundary |
|---|---|---|
| Asset management | Workload inventory, cloud connector context, labels | Official asset register remains authoritative |
| Communication security | Workload segmentation and approved service paths | Perimeter/SASE/cloud-native controls remain complementary |
| Operations | Baseline dependencies, drift detection, policy reports | Operational process evidence remains customer-owned |
| Vulnerability handling | Package/CVE exposure and reachability context | Scanner and remediation workflow remain complementary |
| Incident management | Flow/process timelines and affected workload scoping | Legal/customer notification remains customer-owned |
| Supplier/customer boundaries | Tenant/service egress and shared-service communication | Contractual assurance and CSP controls remain separate |

## 3. Suggested Scope Pattern

```text
BSI-C5
├── Cloud-Service-Scope
│   ├── Production-Service
│   ├── Tenant-Shared-Services
│   ├── Customer-Data-Stores
│   └── Management-Plane-Adjacent
├── Cloud-Accounts
│   ├── AWS
│   ├── Azure
│   └── GCP
├── Supplier-Egress
└── Incident-Evidence
```

## 4. POV Steps

- [ ] Select one cloud service or SaaS production boundary.
- [ ] Connect supported cloud accounts or deploy sensors on representative workloads.
- [ ] Normalize labels from cloud tags: `app`, `env`, `owner`, `tenant`, `data_class`, `criticality`, `region`.
- [ ] Observe flows across the agreed business cycle.
- [ ] Identify shared-service, management, and customer-data communication paths.
- [ ] Generate ADM candidate policy and run simulation.
- [ ] Export evidence for the C5 criteria owner.

## 5. Evidence Package

- Cloud workload inventory.
- Scope tree and tag/label mapping.
- Tenant/shared-service flow summary.
- Supplier egress summary.
- Vulnerability exposure and high-risk communication report.
- Policy candidate and exceptions.
- Incident evidence sample.

## 6. Complementary Controls

Use CSW with cloud-native CSPM/CWPP, IAM, KMS/HSM, SIEM/SOAR, vulnerability scanners, backup/DR, GRC, customer notification workflows, and cloud provider assurance reports.

## 7. Assurance Caveat

BSI C5 evidence depends on the exact audit scope and shared-responsibility model. Validate CSW evidence mapping with the C5 audit owner and assessor.
