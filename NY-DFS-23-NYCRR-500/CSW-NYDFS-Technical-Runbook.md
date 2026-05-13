# Cisco Secure Workload — NY DFS 23 NYCRR Part 500
## Technical Runbook | Covered Entities

**Version:** 1.0  
**Framework:** New York Department of Financial Services Cybersecurity Regulation, 23 NYCRR Part 500  
**Use Case:** Covered-entity workload visibility, segmentation, vulnerability context, monitoring, and incident support

---

## Reader's Guide

**Who this is for.** Financial services covered entities subject to NY DFS 23 NYCRR Part 500, including banks, insurers, and other regulated firms.

**Questions this runbook helps you answer:**

- *Can I produce technical evidence for access limitation, network monitoring, vulnerability management, and incident investigation?*
- *Can I define and protect nonpublic-information workloads and critical systems?*
- *Can I show that third-party and external connections are understood and monitored?*

**What you'll need.** Covered systems inventory, nonpublic information (NPI) data-flow understanding, vulnerability management process, incident-response plan, SIEM retention plan, third-party service provider inventory, and application ownership data.

---

## 1. Overview

23 NYCRR Part 500 requires covered entities to maintain a cybersecurity program and policies appropriate to risk. CSW can support the technical evidence layer for covered workloads: inventory, segmentation, vulnerability context, flow/process telemetry, incident investigation, and third-party egress visibility. It does not replace the CISO function, written policies, annual certification, governance, MFA/IAM, encryption programme, or DFS notification decisions.

## 2. NY DFS Topic Map

| Part 500 topic | CSW can support evidence for | Boundary |
|---|---|---|
| Cybersecurity program | Workload telemetry and segmentation evidence | Program governance remains customer-owned |
| Asset inventory | Workload and application-scope inventory | Official asset register remains authoritative |
| Access privileges | Workload communication allowlists and least-privilege policy | IAM/PAM/MFA remain complementary |
| Vulnerability management | CVE/package exposure and reachability context | Scanners and remediation workflow remain customer-owned |
| Monitoring and testing | Flow/process telemetry, policy simulation, drift review | SIEM/SOC operations remain complementary |
| Incident response | Affected-workload and communication timeline | Regulatory notice decisions remain legal/compliance-owned |
| Third-party service providers | External dependency and supplier egress summary | Contractual risk management remains GRC-owned |

## 3. Suggested Scope Pattern

```text
NYDFS-500
├── Covered-Systems
│   ├── NPI-Applications
│   ├── Customer-Portals
│   ├── Data-Stores
│   └── Security-Services
├── Critical-Operations
├── Third-Party-Service-Providers
└── Incident-Evidence
```

## 4. POV Steps

- [ ] Select one NPI-bearing application or critical system.
- [ ] Apply labels: `npi_scope`, `app`, `env`, `owner`, `criticality`, `third_party`.
- [ ] Build scopes around covered systems and service-provider egress.
- [ ] Run an observation window and validate dependencies.
- [ ] Identify unauthorized paths, excessive east-west access, high-risk ports, and plaintext protocols.
- [ ] Generate ADM policy and simulate.
- [ ] Package evidence for monitoring, vulnerability, and incident-response discussions.

## 5. Evidence Package

- Covered workload inventory.
- NPI and critical-system scope map.
- Observed communication paths.
- Third-party service provider egress summary.
- Vulnerability exposure summary.
- Policy candidate and exception register.
- Incident timeline sample.

## 6. Complementary Controls

Pair CSW with IAM/MFA/PAM, endpoint security, vulnerability scanners, SIEM/SOAR, encryption/key-management evidence, GRC workflow, and written policies required by the regulation.

## 7. Regulatory Caveat

NY DFS requirements and amendment effective dates should be validated against the current official text and counsel. CSW supports evidence; it does not certify compliance or replace required governance and filings.
