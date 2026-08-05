# Cisco Secure Workload — PCI DSS v4.0 Compliance Framework
## Technical Runbook | Payment Card Industry Accounts

**Version:** 1.1 | **Standard:** PCI DSS v4.0.1 (June 2024) — the current errata of PCI DSS v4.0 (March 2022). All future-dated v4.0 requirements are now **effective and mandatory** (as of 31 March 2025).

---

## Reader's Guide

**Who this is for.** Merchants and service providers with a Cardholder
Data Environment (CDE) preparing for QSA assessment, AOCs, or
self-assessment under PCI DSS v4.0; and QSAs cross-checking technical
evidence.

**Questions this runbook helps you answer:**

- *Can I prove every system component currently "in scope" for PCI is
  actually in scope today, with no scope drift since last assessment?*
  (Req 12.5.2)
- *Reqs 1.2.3 and 1.2.4 call for current, accurate network and
  account-data-flow diagrams of the CDE. What is the live,
  machine-generated artifact form of those diagrams?*
- *Req 11.5.2 (change-detection on critical files) — what is my signal
  that nothing was added to the CDE between assessments?*
- *Req 10.2 logging — am I capturing audit-relevant events at the
  workload tier, not just at the network or SIEM layer?*
- *PCI DSS v4.0 introduced "in place and operating effectively"
  language and the customized approach. What does my continuous
  evidence story look like, vs. annual snapshots?* (Req 12.4.2)

**What you'll need.** A defined and documented CDE, your current PCI
scope document, and your QSA's evidence request template (or last
year's RoC sections).

**Where to start.** Sections 1–2 if scope is in motion; section 3 to
walk requirement-by-requirement; sections 4–5 if you're inside the
assessment window or assembling evidence for the now-mandatory
future-dated v4.0 requirements.

---

<!-- CSW-RUNBOOK-PRIMER:v1 -->

## CSW primer — if you are new to Cisco Secure Workload

Cisco Secure Workload (CSW) is a **workload protection platform**. A lightweight **agent** on each server/VM/container observes processes and network flows; **cloud connectors** add AWS/Azure/GCP inventory where agents are not deployed.

| CSW term | Meaning | Why compliance teams care |
|----------|---------|---------------------------|
| **Scope** | Logical boundary (CDE, PHI zone, CUI enclave) | Defines the systems you must prove are isolated |
| **Label / filter** | Tag or query assigning workloads to scopes | Automates scope membership — reduces drift |
| **ADM** | Application Dependency Mapping from observed traffic | **Live** network/data-flow diagram for assessors |
| **Workspace** | Policy container for one scope or application | Where allow/deny rules are authored |
| **Monitor → Simulation → Enforce** | Safe rollout sequence | Simulation = change-board evidence before blocking traffic |
| **Denied Connections** | Log of flows blocked by policy | Primary proof that enforcement **operates** |

**Console areas:** Investigate (inventory, flows, vulns) · Defend/Segmentation (policy) · Manage (agents) · Platform (connectors) · Administration (audit log)

**Read next:** [Compliance evidence playbook](../docs/compliance-evidence-playbook.md) (full step-by-step) · [About CSW](../docs/about-csw.md) (platform intro)

---

## Universal evidence workflow

Execute these phases for **this framework's** compliance boundary. Map exports to control IDs in the **Reporting & Evidence** section below.

| Phase | Goal | Key CSW actions | Typical duration |
|-------|------|-----------------|------------------|
| **1 — Coverage** | Every in-scope workload in CSW | Install agents/connectors; apply compliance labels; create scope | Days 1–10 |
| **2 — Baseline** | Machine-generated flow map | Run ADM ≥2 weeks; export clusters; app-owner signoff | Days 11–28 |
| **3 — Policy** | Designed isolation before enforce | Build workspace; Simulation mode; fix false positives | Days 29–45 |
| **4 — Operate** | Continuous proof between audits | Enforce; quarterly export pack; ADM refresh every 90 days | Ongoing |

### Phase 1 checklist (coverage)

- [ ] In-scope host list reconciled to CSW Inventory (100% or documented exceptions)
- [ ] Labels applied: `compliance:<framework>`, `data:<classification>`, `env:<tier>`
- [ ] CSW scope created matching compliance boundary
- [ ] **Export:** inventory CSV + agent status screenshot

### Phase 2 checklist (baseline)

- [ ] ADM running on compliance scope for full business cycle (≥2 weeks)
- [ ] Unexpected flows documented (shadow IT, vendor egress, scope creep)
- [ ] App owners signed cluster-to-application mapping
- [ ] **Export:** ADM diagram + flow samples with process context

### Phase 3 checklist (policy)

- [ ] Default-deny posture defined for sensitive scope
- [ ] ADM-imported rules refined; Simulation run ≥1 week
- [ ] Change tickets for false-positive fixes; exception register updated
- [ ] **Export:** policy export + simulation report

### Phase 4 checklist (operate)

- [ ] Enforcement enabled on pilot scope; negative test recorded in Denied Connections
- [ ] Quarterly pack: inventory, policy, denies, vulns, audit log (see playbook)
- [ ] SIEM integration verified (sample events)
- [ ] **Export:** enforcement screenshot + quarterly binder

### What CSW evidence does not replace

Physical access, HR/training records, encryption key management, signed BAAs/vendor contracts, formal pen tests, and assessor attestation still require separate programmes. CSW addresses the **workload-resident** slice: segmentation, flows, process context, vuln reachability, and change drift.

---

## CSW effectiveness for this framework

- CDE isolation with simulation→enforce — Req 1 evidence at workload tier
- Live CDE flow map (Req 1.2.1) from ADM, not annual Visio
- CVE + reachability prioritisation for Req 6.3.3

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---

## 1. Overview

PCI DSS v4.0 introduces the customized approach and strengthens network segmentation requirements; **v4.0.1 (June 2024)** is the current errata, and the future-dated v4.0 requirements are now **in force** (mandatory since 31 March 2025). CSW can support evidence for aspects of PCI DSS Requirements 1 (network security controls), 6 (vulnerability management), 10 (logging/monitoring), 11 (security testing, including **segmentation penetration-test** support), and 12 (**scope validation**) where workload-level visibility and enforcement apply; confirm final scope and evidence sufficiency with your QSA.

### PCI DSS Requirement → CSW Capability Map

| PCI Requirement | CSW Capability |
|---|---|
| Req 1 — Network Security Controls | Micro-segmentation, CDE isolation, live network/data-flow diagrams (ADM) |
| Req 2 — Secure Configurations | Vulnerability detection, process monitoring |
| Req 6 — Vulnerability Management | Continuous vulnerability exposure visibility, CVSS prioritization |
| Req 7 — Access Control | Workload-level allowlist enforcement |
| Req 10 — Logging & Monitoring | Full flow + process telemetry; supports automated log review (10.4.1.1) |
| Req 11 — Security Testing | ADM baseline deviation detection; segmentation-isolation evidence for 11.4.5 / 11.4.6; IDS/IPS context (11.5.1) |
| Req 12 — Scope Management | ADM/flow evidence for CDE scope validation (12.5.2 / 12.5.2.1) |

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

**1.2.3 / 1.2.4 — Accurate network and account-data-flow diagrams**
- CSW ADM generates a **live application-dependency / data-flow map** of the CDE from observed traffic — the machine-generated form of the network diagram (1.2.3) and account-data-flow diagram (1.2.4), refreshed on demand rather than redrawn annually
- Export the ADM diagram and flow inventory as assessor evidence that the diagrams reflect **current** CDE connectivity

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
- Workload-level enforcement can catch gaps beneath or between network-security-control views; it complements, not replaces, PCI network security controls
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

**10.4.1.1 — Automated audit log review (future-dated; now mandatory)**
- CSW streams flow, process, and policy-violation events to the SIEM via the Data Tap / syslog connector, enabling **automated** log-review mechanisms rather than manual inspection
- Baseline-deviation and denied-connection alerts give the automated review concrete CDE signals to key on

### Requirement 11 — Security Testing

**11.3.1 — External vulnerability scans quarterly**
- CSW provides continuous vulnerability exposure context for workloads it observes
- Use CSW reports as supplementary evidence; they do not replace required PCI external ASV scans or other mandated testing unless explicitly accepted by your QSA for a documented customized approach

**11.4.1 — Penetration testing methodology**
- ADM baseline used as pre-pentest reference
- Post-pentest ADM comparison detects any new paths discovered
- Forensic telemetry captures all pentest activity for review

**11.4.5 — Segmentation controls penetration-tested (all entities, ≥ every 12 months)**
- Where segmentation isolates the CDE, CSW provides strong **supporting** evidence that the isolation holds: ADM shows zero CDE ↔ out-of-scope flows, enforced policy blocks cross-boundary attempts, and Denied Connections logs the blocks
- Run this evidence **before and after** the required segmentation penetration test; the test itself must still be performed by a qualified tester and validated by your QSA

**11.4.6 — Segmentation controls penetration-tested (service providers, ≥ every 6 months)**
- Service providers repeat the 11.4.5 evidence on the six-month cadence and after any change to segmentation controls/methods
- CSW change tracking (ADM refresh + policy version history) flags the "after any change" trigger between scheduled tests

**11.5.1 — Intrusion detection/prevention at the CDE perimeter and critical points**
- CSW forensic rules and network-anomaly detection add **workload-tier** intrusion signals that complement (do not replace) network IDS/IPS at the CDE boundary
- Denied Connections and anomaly alerts feed the SOC/SIEM for detection and response

### Requirement 12 — Scope Management & Risk

**12.5.2 — PCI DSS scope validated (≥ every 12 months)**
- CSW ADM/flow evidence confirms which system components actually communicate with the CDE, helping validate the documented scope and surface **scope creep** since the last assessment
- Export inventory + flow map as the machine-generated basis for the annual scope confirmation

**12.5.2.1 — Scope validated (service providers, ≥ every 6 months)**
- Service providers repeat scope validation every six months and after significant changes to the CDE; CSW change tracking highlights new or removed CDE-connected workloads between reviews

### Appendix A1 — Multi-Tenant Service Providers

**A1.1 — Logical separation between customers**
- CSW per-customer **scopes** and enforced policy isolate each tenant's workloads; ADM + Denied Connections evidence that one customer's environment cannot reach another's

---

## 4. Evidence Package for QSA

| Evidence Item | CSW Source | PCI Requirement | Frequency |
|---|---|---|---|
| CDE network policy export | Defend → Policy Workspaces | Req 1 | Per assessment |
| CDE inbound/outbound flow log | Investigate → Flow Search | Req 1, Req 10 | Continuous |
| Policy violation report | Alerts → Triggered Events | Req 10 | Monthly |
| Vulnerability exposure report (CDE) | Investigate → Vulnerability | Req 6, Req 11 | Weekly |
| CDE scope membership snapshot | Inventory → Export | Req 1, Req 7 | Monthly |
| Anomaly detection log | Alerts → Dashboard | Req 10, Req 11 | Monthly |
| ADM dependency map (CDE) | Investigate → ADM | Req 1 | Quarterly |
| Segmentation isolation evidence (no CDE↔out-of-scope flows + denies) | Investigate → ADM · Defend → Denied Connections | Req 11.4.5 / 11.4.6 | Per segmentation test |
| CDE scope validation pack (inventory + flow map) | Inventory → Export · Investigate → ADM | Req 12.5.2 / 12.5.2.1 | Annually / SP semi-annually |
| Process audit log (CDE) | Investigate → Process Search | Req 10 | On-demand |

---

## 5. PCI DSS v4.0 New Requirements CSW Addresses

*The future-dated v4.0 requirements below are now **mandatory** (effective 31 March 2025) and are carried forward unchanged in v4.0.1.*

| New in v4.0 | CSW Response |
|---|---|
| 12.3.2 — Targeted risk analysis for each requirement | CSW vulnerability + ADM data feeds risk analysis |
| 1.2.4 — Account-data-flow diagram kept current | ADM produces observed-flow documentation for CSW-instrumented paths; human approval and non-CSW paths remain part of CDE documentation |
| 6.3.3 — All vulnerabilities addressed per risk ranking | Continuous vulnerability exposure view with CVSS-ranked remediation inputs |
| 10.4.1.1 — Automated audit log review | Flow/process/policy events streamed to the SIEM enable automated review |
| 10.7.2 — Failures of critical security controls detected | Sensor offline alerts, policy enforcement gap detection |
| 11.4.6 — SP segmentation pen-test every 6 months | ADM + enforce + Denied Connections isolation evidence on the SP cadence |
| 12.5.2.1 — SP scope validation every 6 months | Inventory + flow evidence to confirm CDE scope semi-annually |

---

## Related Frameworks

- [ISO/IEC 27001:2022](../ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md) — most PCI-attested organisations also operate an ISO 27001 ISMS.
- [NIST SP 800-53 Rev 5](../NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md) — useful when PCI evidence is being reused across a federal control programme.
- [DORA (EU 2022/2554)](../DORA/CSW-DORA-Technical-Runbook.md) — for EU payment-services entities, PCI scope and DORA Pillar 1 share substantial evidence.
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) — the segmentation pattern underneath PCI Reqs 1, 7, 11.

---

*Replace [Customer Name] and bracketed fields before customer delivery.*
