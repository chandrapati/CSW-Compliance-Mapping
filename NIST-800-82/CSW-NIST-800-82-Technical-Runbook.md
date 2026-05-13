# Cisco Secure Workload — NIST SP 800-82
## Technical Runbook | OT-Adjacent IT and Industrial Control System Support

**Version:** 1.0  
**Framework:** NIST SP 800-82, Guide to Operational Technology (OT) Security  
**Use Case:** IT-side systems supporting OT environments, jump hosts, historians, patch repositories, identity services, and vendor access

---

## Reader's Guide

**Who this is for.** Security architects, plant IT/OT teams, industrial asset owners, and SOC teams using NIST SP 800-82 guidance to improve OT-adjacent security.

**Scope boundary.** CSW applies to servers, VMs, cloud workloads, and supported connectors. It does not inspect PLC/RTU/IED/HMI fieldbus behavior or replace passive OT visibility. Use it for the IT-side systems that support or bridge to OT.

**Questions this runbook helps you answer:**

- *Can I map and restrict communication between corporate IT and OT-supporting systems?*
- *Can I prove jump hosts, historians, patch repositories, identity services, and vendor systems have constrained paths?*
- *Can I produce incident evidence for OT-adjacent Windows/Linux workloads?*

**What you'll need.** OT zone/conduit model, Purdue-level architecture, OT-supporting IT inventory, vendor access list, maintenance-window constraints, passive OT monitoring coverage, and change-approval process.

---

## 1. Overview

NIST SP 800-82 provides OT security guidance, including segmentation, remote access, monitoring, vulnerability management, and incident response considerations. CSW can support the IT workload layer adjacent to OT. It should be paired with Cisco Cyber Vision or equivalent OT visibility for Level 0-2 device and protocol coverage.

## 2. NIST 800-82 Topic Map

| 800-82 topic | CSW can support evidence for | Boundary |
|---|---|---|
| Network segmentation | Workload policy for OT-facing IT, DMZ brokers, jump hosts, historians | OT firewall / conduit architecture remains authoritative |
| Remote access | Vendor/jump-host dependency mapping and allowlists | PAM/MFA/session recording remain complementary |
| Asset inventory | OT-supporting Windows/Linux workload inventory | PLC/RTU/IED inventory requires OT tools |
| Vulnerability management | CVE/package context for IT workloads supporting OT | Safety constraints and OT patch governance remain customer-owned |
| Monitoring and detection | Flow/process telemetry and SIEM export for OT-adjacent workloads | OT protocol DPI requires Cyber Vision/Claroty/Nozomi/Dragos |
| Incident response | Communication timeline and containment evidence for IT-side systems | Safety and operational response remain OT-owned |

## 3. Suggested Scope Pattern

```text
NIST-800-82
├── OT-Facing-IT
│   ├── Jump-Hosts
│   ├── Historians
│   ├── Patch-Repositories
│   ├── Backup
│   ├── Identity-PKI
│   └── Vendor-Access
├── Industrial-DMZ
├── Site-Specific-Systems
└── Cannot-Instrument
```

## 4. POV Steps

- [ ] Start with OT-supporting IT, not PLCs or safety systems.
- [ ] Confirm which workloads can safely run CSW sensors.
- [ ] Label by `site`, `function`, `purdue_level`, `owner`, `criticality`, and `ot_facing`.
- [ ] Observe normal maintenance and vendor-access windows.
- [ ] Validate flows with plant operations and OT security.
- [ ] Generate policy candidates for jump hosts, patch repositories, and historians.
- [ ] Document systems requiring passive-only monitoring.

## 5. Evidence Package

- OT-adjacent workload inventory.
- Scope map by site/function/Purdue layer.
- Vendor and remote-access flow summary.
- Jump host / historian / patch-repo dependency maps.
- High-risk port and plaintext protocol findings.
- Cannot-instrument register.
- Policy candidate and rollback notes.

## 6. Complementary Controls

Pair CSW with Cisco Cyber Vision, OT firewalls, PAM/MFA, SIEM/SOAR, passive OT monitoring, maintenance procedures, backup/restore validation, and plant change-management controls.

## 7. Safety Caveat

Do not infer CSW support for OT field devices unless explicitly validated. Industrial safety, process availability, and integrator-approved change control take precedence over enforcement.
