# Cisco Secure Workload — TISAX
## Technical Runbook | Automotive Information Security Assessment

**Version:** 1.0  
**Framework:** TISAX / VDA ISA-aligned information security assessment  
**Use Case:** Automotive supplier workload segmentation, prototype / confidential data protection, supplier connectivity evidence

---

## Reader's Guide

**Who this is for.** Automotive OEMs, suppliers, engineering partners, and service providers preparing for TISAX assessment or customer security requirements based on VDA ISA.

**Questions this runbook helps you answer:**

- *Can I prove that prototype, engineering, and customer-confidential workloads are isolated from general corporate systems?*
- *Can I document supplier/customer connectivity and detect unexpected egress?*
- *Can I provide technical evidence for network segmentation, monitoring, vulnerability, and incident investigation controls?*

**What you'll need.** Assessment objective, VDA ISA scope, customer-specific protection needs, engineering / prototype system inventory, supplier connection list, application ownership, and evidence request expectations.

---

## 1. Overview

TISAX assessments use VDA ISA to evaluate information security controls in automotive ecosystems. CSW can support technical evidence for workload segmentation, dependency mapping, vulnerability context, process/flow telemetry, and supplier egress monitoring. CSW does not replace TISAX assessment, VDA ISA control ownership, physical prototype controls, HR/training controls, IAM/MFA, DLP, or supplier contractual assurance.

## 2. TISAX / VDA ISA Topic Map

| Assessment topic | CSW can support evidence for | Boundary |
|---|---|---|
| Information classification | Scope/label mapping to prototype, confidential, and customer data workloads | Classification policy remains customer-owned |
| Access control | Workload-level communication allowlists | IAM/PAM remains complementary |
| Network segregation | Engineering/prototype enclave segmentation and supplier egress | Campus/perimeter controls remain complementary |
| Vulnerability management | Workload package/CVE context and reachability | Scanner and remediation SLAs remain customer-owned |
| Logging and monitoring | Flow/process telemetry and SIEM export | SOC workflow remains complementary |
| Supplier connectivity | Approved customer/supplier endpoints and egress tracking | Contractual supplier assurance remains GRC-owned |

## 3. Suggested Scope Pattern

```text
TISAX
├── Assessment-Scope
│   ├── Prototype-Protection
│   ├── Engineering-Systems
│   ├── Customer-Confidential
│   └── Production-IT
├── Supplier-Customer-Egress
├── Shared-Services
└── Incident-Evidence
```

## 4. POV Steps

- [ ] Select one engineering, prototype, or customer-confidential workload group.
- [ ] Label workloads by `assessment_scope`, `data_class`, `customer`, `owner`, `env`, and `criticality`.
- [ ] Observe flows over a representative engineering cycle.
- [ ] Validate customer/supplier communication with business owners.
- [ ] Identify unexpected egress, high-risk ports, and excessive lateral paths.
- [ ] Generate candidate policy and simulate before enforcement.

## 5. Evidence Package

- TISAX scope workload inventory.
- Prototype / engineering / customer-confidential scope map.
- Supplier and customer egress summary.
- Flow and process telemetry summary.
- Vulnerability exposure summary.
- Policy candidate and exception register.
- Assessment evidence notes by VDA ISA topic.

## 6. Complementary Controls

Use CSW with IAM/MFA/PAM, DLP, endpoint security, SIEM, GRC, physical prototype controls, supplier contracts, and customer-specific evidence portals.

## 7. Assessment Caveat

TISAX labels and VDA ISA assessment objectives vary by customer and scope. Validate final evidence with the customer's assessment provider and OEM/customer requirements.
