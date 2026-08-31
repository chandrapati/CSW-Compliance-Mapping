# Cisco Secure Workload — IEC 62443 Compliance Framework
## Technical Runbook | Industrial Automation & Control Systems (IACS)

**Version:** 1.1  
**Use Case:** Fresh Install, Hybrid Environment (On-Prem + Cloud)  
**Standards anchor:** IEC 62443-3-3 (System security requirements and security levels); IEC 62443-2-1 (Security program requirements for IACS asset owners); IEC 62443-4-1 (Secure product development lifecycle requirements — supplier-side alignment for CSW as a product; see **Section 14**) — consult your SL-T target and zone/conduit documentation for authoritative control text.

---

## Reader's Guide

**Who this is for.** IACS asset owners, OT/IT security architects, plant
or operations cybersecurity teams, and integrators preparing for
IEC 62443-aligned assessments, customer security requirements, or
internal security management system (SMS) evidence for industrial
environments. **Section 14 additionally serves procurement, third-party
risk management (TPRM), and vendor-assurance reviewers** who need
evidence that CSW itself is developed under an IEC 62443-4-1-aligned
secure development lifecycle.

**Scope boundary you must understand before reading further.** Cisco
Secure Workload (CSW) enforces segmentation, discovers dependencies,
and produces forensic telemetry on **servers, virtual machines,
containers, and cloud workloads** — the **IT side of the IT/OT
boundary** and the systems that **support** IACS (jump hosts,
engineering workstations, historians, MES interfaces, DMZ brokers,
identity services, patch servers, vendor remote-access concentrators).
CSW does **not** replace dedicated OT visibility for Level 0–2 devices
(PLCs, RTUs, IEDs, drives, field instruments). Pair CSW at the IT
layer with **Cisco Cyber Vision**, **Claroty**, **Nozomi**, or
equivalent for asset discovery, ICS protocol analytics, and
device-level integrity signals.

**Questions this runbook helps you answer:**

- *SR 5.1–5.4 (restricted data flow / zones & conduits): Can I prove
  that only documented conduits carry traffic between OT-support
  tiers and corporate/cloud, and that lateral movement outside those
  conduits is structurally denied or logged?*
- *SR 1.1–1.13 (identification / authentication / access control):
  Can I show identity-aligned allow rules and deny-by-default paths
  for systems that administer or bridge into IACS zones?*
- *SR 3.1–3.9 (data / system integrity): Can I baseline inventory
  (processes, binaries, listening services) and detect unexpected
  change or unauthorized software on IACS-adjacent IT workloads?*
- *SR 6.1–6.2 (event monitoring & timely response): Can I reconstruct
  a timeline of flows and processes during an OT-adjacent incident?*
- *SR 7.1–7.8 (resource availability): Can I detect volumetric or
  connection storms indicative of denial-of-service against critical
  IT services that underpin OT availability?*
- *IEC 62443-2-1 (security program / operations): Can I produce
  continuous monitoring dashboards and exports that feed our SMS
  without manual spreadsheet reconciliation?*
- *IEC 62443-4-1 (secure development lifecycle for CSW as a product):
  For procurement / TPRM review — can Cisco demonstrate that Secure
  Workload is developed under an SDL aligned to the 4-1 practice areas
  (SM, SR, SD, SI, SVV, DM, SUM, SG), even where formal SDLA
  certification is not currently claimed?*

**What you'll need.** Your zone & conduit model (per IEC 62443-3-2 or
customer ZCRD), Security Level Target (SL-T) per zone, inventory of
IACS-adjacent IT systems (EWS, jump hosts, AD/PKI, historians), change
management approval for sensor install, and naming alignment between
your PAS/OT tools and CMDB labels.

**Where to start.** Sections 1–2 while scoping; 3–5 during pilot
sensor and baseline; 6–8 when designing enforcement; 9–10 for control
mapping and SMS reporting; section **Boundaries** before promising CSW
coverage to integrators or auditors.

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

- Zones & conduits segmentation on IT-side OT boundaries
- SR control evidence; pair with Cyber Vision/Claroty for device layer
- Jump host and historian path visibility

**Compared to manual programmes:** static diagrams and annual firewall samples age immediately; CSW ties evidence to **live workload behaviour** and produces queryable exports on demand — supporting "operating effectively" language in PCI v4.0, SOC 2 CC7, and HIPAA risk analysis.

---

## 1. Overview

IEC 62443 provides a lifecycle-oriented security framework for
industrial automation and control systems. **IEC 62443-3-3** specifies
foundational requirements (FRs) and associated **system requirements
(SRs)** for IACS components and systems. **IEC 62443-2-1** defines
requirements for an IACS **security management system** operated by the
asset owner. CSW contributes **technical evidence** for restricted data
flow, access enforcement, integrity-related visibility, detection
support, and availability-oriented anomaly awareness on the **IT
workloads** that border or support IACS — not as a substitute for OT
protocol inspection or safety-instrumented logic.

### IEC 62443 structure mapped to CSW capabilities

| IEC 62443 topic | Typical artifacts | Relevant CSW capabilities |
|---|---|---|
| **FR 5 / SR 5.1–5.4** — Restricted data flow (zones & conduits) | Zone diagrams, conduit allowlists, firewall/ACL rules | Microsegmentation workspaces; scope hierarchy mirroring zones; default-deny with explicit conduits |
| **FR 1 / SR 1.1–1.13** — Identification, authentication, access control | Account lifecycle, RBAC, remote access paths | Identity-aware policies (where integrated); least-privilege allowlists; jump-host-only admin paths |
| **FR 3 / SR 3.1–3.9** — System & data integrity | Software inventory, patch posture, change detection | Process/binary inventory; listening-port baseline; vulnerability context; drift alerts |
| **FR 6 / SR 6.1–6.2** — Event monitoring & timely response | SOC runbooks, timelines, ticket exports | Flow + process forensics; alert correlation inputs to SIEM |
| **FR 7 / SR 7.1–7.8** — Resource availability | SLAs, capacity plans, DoS playbooks | Flow anomaly detection (connection/session volume spikes); early warning on saturation patterns |
| **62443-2-1** — Security management / operations | KPIs, dashboards, management review | Continuous inventory/policy dashboards; scheduled evidence export |
| **62443-4-1** — Supplier secure development lifecycle (for CSW as a product) | SDLA questionnaires, SBOM, PSIRT process, CVD policy, patch/vulnerability advisories | Cisco CSDL alignment evidence — see **Section 14** for practice-by-practice mapping and vendor due-diligence checklist |

**Regional or contractual note:** Many asset owners implement 62443
requirements through customer purchase specifications or national
interpretations. Map this runbook’s **SR** references to *your*
contractual clauses and audit questionnaires; numbering alone is not
sufficient for certification evidence without your target SL and scope.

---

## 2. Pre-Deployment Checklist

Before deploying CSW sensors on IACS-adjacent IT estates, confirm:

- [ ] CSW cluster (SaaS or on-prem) is provisioned; **air-gap / data
  residency** rules reviewed if telemetry leaves the plant DMZ
- [ ] Network path from workloads to CSW cluster (typically **443
  outbound**); proxy exceptions documented
- [ ] Linux/Windows agent compatibility verified for **engineering
  workstations, jump servers, historians, AD/PKI**, and cloud broker VMs
- [ ] Cloud connectors configured where plant data lands in **AWS /
  Azure / GCP** (historian mirrors, IoT hubs, analytics lakes)
- [ ] Stakeholders engaged: **OT security lead**, **plant IT**,
  **integrator**, **SOC**, and **SMS owner** (62443-2-1)
- [ ] **Maintenance window** approved; **OT change freeze** rules
  respected — start in **Monitoring Only**
- [ ] **PAS / OT tool** (Cyber Vision, Claroty, Nozomi) inventory
  export available for cross-walk of hostnames / VLANs / cell IDs

---

## 3. Phase 1 — Sensor Deployment (Days 1–5)

### 3.1 On-premises IT adjacent to IACS

**Install software sensors on representative tiers:** EWS images, jump
hosts, historian/MES application servers, AD connectors, vendor VPN
concentrators — *never* on safety PLCs or real-time controllers if
those run unsupported or prohibited agent OSes.

```bash
# Linux (RHEL/CentOS/Ubuntu family)
sudo rpm -ivh tet-sensor-<version>.rpm    # RHEL/CentOS-compatible
sudo dpkg -i tet-sensor-<version>.deb    # Debian/Ubuntu

# Verify sensor service
sudo systemctl status csw-agent
sudo systemctl enable --now csw-agent
```

**Windows (engineering workstation build):**

```powershell
# Example: install from staged MSI (version/path per release)
msiexec /i "C:\Deploy\tet-sensor-<version>.msi" /qn
Get-Service | Where-Object { $_.Name -like "*tet*" -or $_.Name -like "*csw*" }
```

**Initial posture:**

- Enforcement: **Monitoring Only** (no blocks until ADM + simulation
  complete)
- Collection: **process hash**, **network flow**, **listening
  services**, **vulnerability exposure** (where licensed)
- Tags from day one: `zone:<cell>`, `conduit:<id>`, `iqs:iacs-adj`,
  `sl-target:SL2` (example)

### 3.2 Cloud & hybrid IACS data paths

Use **cloud connectors** when historian/analytics or IT control plane
lives in public cloud:

```
CSW UI → Platform → External Orchestrators
  → Add AWS / Azure / GCP connector
  → Least-privilege IAM / service principal
  → Enable flow visibility (VPC/VNet flow ingestion where supported)
```

### 3.3 Sensor validation

```
CSW UI → Manage → Agents
  → Status: Active for all pilot hosts
  → Confirm telemetry (flow/process) within 15–30 minutes of install
  → Record agent build in baseline export (62443-3 SR 3 / change mgmt input)
```

---

## 4. Phase 2 — Scope & Inventory Design — Zones, Conduits, SL (Days 6–12)

### 4.1 Map CSW scopes to IEC zones & conduits

Model scopes to mirror **62443-3-2** zone definitions without renaming
your-certified drawings — use **labels** that reference drawing IDs.

```
Root: Industrial-Enterprise
├── Plant-<Site>-OT-Support        # IT that touches OT (EWS, jump, historian app tier)
│   ├── Cell-A-Conduit-IT-OT       # Scoped to hosts in conduit endpoints only
│   ├── Cell-B-Conduit-IT-OT
│   └── Shared-Services-IACS       # AD, PKI, patch, backup — constrained to conduits
├── Plant-DMZ-Brokers              # Data diodes / OPC brokers / MQTT gateways (VM-based)
├── Corporate-IT                   # Default no direct path to OT-support
└── Vendor-Remote-Access           # Termination servers for integrator VPN
```

**Conduit rule of thumb:** One CSW policy workspace per **documented
conduit** (or group of symmetric conduits) so evidence maps 1:1 to
the ZCRD.

### 4.2 Discovery filters for IACS-adjacent candidates

```
Filter: Historian-MES-Tier
  - Process name contains: historian, mes, opc*, scada, "wonderware"
  - Ports: 1433, 1521, 5432, 135, 502 (context-dependent — validate in YOUR env)
  - Tag pas:ot-adjacent (if synchronized from PAS)

Filter: Jump-EWS
  - Hostname regex: (?i)(ews|eng|hmi-jump|vendor-jump)
  - User workload tag: role=engineering
```

Validate every automated filter with **OT SME sign-off** — **SR 5**
evidence must match the *as-engineered* conduit list, not a guessed list.

### 4.3 Label strategy (SMS-friendly)

| Label key | Examples | Purpose |
|---|---|---|
| `zone` | `cell-a`, `line-3` | Aligns to 62443 zone ID |
| `conduit` | `c-ot-to-mes-01` | Audit trail for restricted data flow |
| `sl-target` | `SL2`, `SL3` | Drive rule strictness / monitoring cadence |
| `ics-role` | `ews`, `jump`, `historian`, `broker` | Policy grouping |
| `owner` | `ot-sec`, `plant-it` | Accountability in exports |

---

## 5. Phase 3 — Application Dependency Mapping & Baseline (Days 13–28)

### 5.1 ADM workspace

ADM establishes **observed** vs **designed** conduits — essential for
**SR 5** and access **SR 1** reviews.

```
CSW UI → Investigate → Application Dependency Mapping
  → New Workspace
  → Name: IACS-Conduit-Baseline-<Site>
  → Scope: Plant-<Site>-OT-Support + DMZ brokers
  → Window: minimum 2–4 weeks (capture patch Tuesday, recipe changes, campaigns)
  → Enable process context; retain ≥ 30 days if storage policy allows
```

### 5.2 ADM review checklist (62443-oriented)

| Investigation question | SR / FR linkage |
|---|---|
| Which corporate subnets talk to historians or OPC brokers? | **SR 5** — restricted data flow |
| Are there HTTPS/LD/RDP paths bypassing EWS/jump? | **SR 1** — access paths |
| Do EWS images reach the internet directly? | **SR 5**, **SR 1** |
| New binary or service on jump host? | **SR 3** — integrity |
| Sudden east-west fan-out from a broker VM? | **SR 6** — detection; **SR 7** — availability stress |

### 5.3 Baselining for integrity (SR 3 inputs)

Export **inventory snapshots** after accepted build state:

```
CSW UI → Investigate → Inventory (or equivalent workload inventory view)
  → Filter: scope = Plant-<Site>-OT-Support
  → Export: processes, packages, listening ports, hashes (as available)
  → Store in secure evidence library with version + timestamp
```

Repeat on **known-good** patch cycles to update baseline registers.

---

## 6. Phase 4 — Policy Design & Enforcement (Days 29–45)

### 6.1 Conduit-aligned policy framework

Translate **allowlisted conduits** into CSW rules. **Example pattern**
— adjust ports, scopes, and identities to your ZCRD.

**Absolute denies (illustrative):**

```
DENY: Corporate-IT → Plant-<Site>-OT-Support (all)
  EXCEPTION: documented Intermediary / jump subnet only

DENY: Vendor-Remote-Access → any except Plant-DMZ-Brokers & Jump hosts

DENY: Plant-<Site>-OT-Support → Internet (0.0.0.0/0)
  EXCEPTION: explicit patch/CDN allowlist + CSW SaaS egress if required
```

**Conduit allows (illustrative):**

```
ALLOW: Plant-DMZ-Brokers ↔ Historian-MES-Tier
  - TCP 135, 49320–49330 (DCOM range — validate), OPC-UA 4840 (if used)

ALLOW: Jump-EWS → Plant-<Site>-OT-Support
  - RDP 3389 / SSH 22 only from Jump-EWS scope

ALLOW: Plant-<Site>-OT-Support → AD-PKI
  - LDAPS 636, Kerberos 88, DNS 53 — block cleartext LDAP 389 where possible
```

**Audit unmatched:**

```
LOG + ALERT: any flow not matching explicit conduit rules
```

### 6.2 Policy workspace

```
CSW UI → Defend → Segmentation
  → New Workspace: IEC62443-Conduits-<Site>
  → Import ADM-suggested rules → reconcile with ZCRD
  → Mode: Simulation (minimum 2 weeks typical) → Enforcement by conduit tier
```

### 6.3 Enforcement progression

| Step | Mode | Objective |
|---|---|---|
| 1 | Simulation | Prove OTSupport apps still function; tune OPC/RPC ranges |
| 2 | Selective enforcement | Lock down highest-risk corporate lateral paths first |
| 3 | Full enforcement on IT border | Default deny except conduits; maintain break-glass procedure |

**Integrator coordination:** Provide **simulation reports** before
enabling blocks on lines under warranty support.

---

## 7. Phase 5 — Monitoring, Availability Signals & SMS Feeds

### 7.1 Alerts aligned to 62443 operations

| Alert | Example trigger | SR mapping |
|---|---|---|
| Undocumented conduit attempt | New src→dst across OT-support boundary | **SR 5** |
| Cleartext admin | LDAP/HTTP to AD from EWS | **SR 1**, **SR 3** |
| New listening service on jump | Port opens not in baseline | **SR 3** |
| Flow anomaly / storm | Connection rate >> baseline | **SR 6** (detect), **SR 7** (availability) |
| Critical CVE on historian tier | CVSS ≥ threshold | **SR 3**, **62443-2-1** risk treatment |
| Sensor offline | Loss of heartbeats | **SR 6** — visibility gap |

### 7.2 IEC 62443-2-1 continuous monitoring dashboard

Schedule **weekly** management-visible tiles (exact UI path may vary
by release):

- **Scope coverage** — % of IACS-adjacent IT with active agent
- **Policy drift** — rules changed since last approval export
- **Open simulation violations** — unreviewed would-block flows
- **Top talkers** across conduits — compare to PAS asset roles

Export snapshots into your SMS review record **monthly** minimum.

---

## 8. Control-by-control mapping — Framework requirement → CSW → evidence

Use this table to **start** questionnaire mapping. Official conformity
assessment requires your **SL-T**, **scope statement**, and **test
methods** from the certification body or customer spec.

### 8.1 SR 5 — Restricted data flow (zones & conduits)

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 5.1** — Segmentation / zones | Scope hierarchy; segmentation workspaces; labels `zone`, `conduit` | Scope export; diagram cross-walk memo |
| **SR 5.2** — Segmentation for zones of differing security requirements | Tiered scopes by SL labels; stricter workspaces for higher SL | Policy diff between SL scopes |
| **SR 5.3** — Conduit control | Allowlist rules per conduit; default deny | Policy JSON/export + simulation/enforcement logs |
| **SR 5.4** — Covert channel mitigation (as applicable at IT layer) | Egress restrictions; anomaly detection on volume | Flow anomaly reports + change tickets |

### 8.2 SR 1 — Identification, authentication, and access control

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 1.1–1.13** (human / process / service access paths) | Identity-aware policies (when integrated); admin path lock-down; least privilege allowlists | Flow logs with user/process context; policy allow/deny history |
| **Remote access** paths via jump | Rules limiting src to jump scope; deny corporate→OTSupport direct | ADM + enforcement hit logs |

### 8.3 SR 3 — System integrity

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 3.1–3.9** (software integrity, malware deterrence inputs, etc.) | Process & binary inventory; package visibility; vulnerability data | Inventory export; drift alerts; VA connectors / built-in reports |
| **Unauthorized software** indicators | New process / listener alerts vs baseline | Ticket + before/after inventory |

### 8.4 SR 6 — Event monitoring & timely response

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 6.1** — Audit logging support | Flow + process retention; export APIs / UI exports | Raw & summary logs with UTC stamps |
| **SR 6.2** — Continuous monitoring inputs | Alerts; SIEM forwarders | Alert rule catalog; SOC ingest proof |

### 8.5 SR 7 — Resource availability

| IEC 62443-3-3 requirement (summary) | CSW capability | Evidence produced |
|---|---|---|
| **SR 7.1–7.8** (DoS considerations at system level) | Flow volumetrics; session rate anomalies; saturation precursors | Time-series anomaly exports + IR narrative |

### 8.6 IEC 62443-2-1 — Security management system (technical contributors only)

| 62443-2-1 theme (summary) | CSW capability | Evidence produced |
|---|---|---|
| Operations monitoring & KPIs | Dashboards; scheduled exports | Monthly PDF/CSV appendices to SMS review |
| Incident response support | Forensic drill exports | Tabletop package — flow + process trace |

---

## 9. Vulnerability, patch & compensating controls

### 9.1 Vulnerability visibility

```
CSW UI → Investigate → Vulnerability Report
  → Scope: Plant-<Site>-OT-Support
  → Filter: CVSS ≥ 7.0 (example)
  → Export CSV for SMS risk register linkage
```

### 9.2 Compensating controls when patching waits for outage

- Narrow allow rules to **known peer scopes** only
- Raise **alert severity** on vulnerable process names
- Capture **full flow logs** to affected workload until patched

---

## 10. Forensics & incident reconstruction

```
CSW UI → Investigate → Flow Search
  → Time range: incident window (extend for long-running OT campaigns)
  → Source/Destination: suspected broker or EWS
  → Export: CSV/JSON with process + user context

CSW UI → Investigate → Process Search
  → Parent/child chain for suspicious binaries on jump hosts
```

Retain exports per **your** SMS / legal hold policy; correlate with **PAS**
PCAP or ICS alerts for full OT picture.

---

## 11. Audit preparation & evidence export

### 11.1 Quarterly evidence pack (adjust to customer cadence)

| Evidence item | CSW source | Typical IEC mapping |
|---|---|---|
| Conduit policy export | Defend → workspace export | **SR 5.x** |
| Simulation vs enforcement history | Policy lifecycle / audit log | **SR 5**, **SR 1** |
| ADM cluster report | ADM workspace | **SR 5**, **SR 1** |
| Inventory baseline delta | Inventory exports | **SR 3.x** |
| Vulnerability exposure | Vulnerability report | **SR 3**, **62443-2-1** |
| Alert & flow excerpts | Flow Search, Alerts | **SR 6**, incident packs |
| Coverage report | Agent inventory | **62443-2-1** monitoring scope |

### 11.2 Bash helper examples (on analysis workstation)

After UI export to `/evidence/csw/`:

```bash
# Verify exported policy archive integrity (after UI download)
shasum -a 256 /evidence/csw/iec62443-policy-export-YYYYMMDD.zip | tee /evidence/csw/SHA256SUMS

# Redact non-production subnets before sharing with integrator
perl -pe 's/\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/10.REDACTED.0.0/g' \
  /evidence/csw/flows-incident-window.csv > /evidence/csw/flows-incident-window-redacted.csv
```

---

## 12. Boundaries — what CSW does **not** cover

- **Level 0–2 OT devices** (PLCs, IEDs, devices without supported agents) —
  use PAS/OT security tools; CSW does not inspect proprietary fieldbus
  payloads at wire speed.
- **Safety instrumented functions** — CSW is not a SIL-rated safety
  device; engineering lifecycle evidence stays with SIS vendor tools.
- **Physical security & personnel screening** — access badges, gates,
  contractor vetting — outside CSW.
- **Cryptographic key management policy** — CSW may enforce **paths**
  (e.g., TLS-only) but does not replace PKI governance or HSM decisions.
- **62443-2-1 organizational processes** — CSW supplies **telemetry and
  policy exports**; it does not author your procedures, training roster,
  or supplier security clauses.

---

## 13. Common pitfalls

| Pitfall | Mitigation |
|---|---|
| Mis-mapping CSW scopes to **electrical zones** instead of **cyber zones** | Anchor labels to approved cyber ZCRD IDs |
| Blocking **dynamic RPC/OPC** ranges without ADM | Long simulation + integrator test scripts |
| Deploying only on corporate IT | **OT-adjacent** IT is the compliance-critical tier |
| Ignoring cloud **shadow IT** paths to plant data | Enable cloud connectors for mirrored historians |
| Expecting CSW to **replace** OT IDS | Maintain Cyber Vision / Claroty / Nozomi for ICS context |

---

## 14. IEC 62443-4-1 — Cisco's Secure Product Development Lifecycle (CSW as a product)

**Audience shift.** Sections 1–13 help *asset owners* deploy CSW to
evidence 62443-3-3 / 2-1 controls in their plant. **Section 14 is for
your procurement, TPRM, and vendor-assurance reviewers** who need to
understand how the CSW *product* is built — mapping Cisco's Secure
Development Lifecycle (CSDL) to the eight IEC 62443-4-1 practice areas.

**Alignment, not certification.** Cisco Secure Workload is not currently
listed with an IEC 62443-4-1 **SDLA** or 62443-4-2 **SSA**
certification. This mapping demonstrates that CSDL — Cisco's
enterprise-wide secure development programme — *aligns to the intent
and practice structure* of 62443-4-1. Where a customer contract or SL-T
demands a certification claim, escalate to the Cisco account team for
formal supplier attestation letters or a customer-specific security
requirements (CSR) response.

### 14.1 SM — Security Management

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SM-1** Development process | Documented CSDL programme applied across Cisco engineering; product-level tailoring for CSW | CSDL programme overview; product security plan reference |
| **SM-2** Identification of responsibilities | Product Security Engineering Team (PSET) + PSIRT roles defined for CSW | Org chart / RACI for CSW security roles (under NDA) |
| **SM-3** Identification of applicability | CSDL scope explicitly covers CSW components (agents, cluster software, cloud connectors) | Scope statement referencing CSW SKUs / release trains |
| **SM-4** Security expertise | Trained secure-code reviewers, threat modelers, and pen-testers embedded in CSW BU | Training records summary; certification list |
| **SM-5** Process scoping | Release-gate integration of CSDL steps in CI/CD | Release checklist evidence (redacted) |
| **SM-6** File integrity | Signed builds, protected artifact repos, chain-of-custody | Code-signing certificate policy summary |
| **SM-7** Development environment security | Hardened build infrastructure, MFA-gated repos, segmented build networks | Build environment security policy (under NDA) |
| **SM-8** Continuous improvement | Post-release security retrospectives; PSIRT feedback loop into CSDL | CSDL change log / annual programme review |
| **SM-9** Controls on private keys | Cisco PKI + HSM-backed signing keys | Key management policy summary |
| **SM-10** Security-related issue disclosure | Coordinated Vulnerability Disclosure (CVD) via Cisco PSIRT | Link to Cisco PSIRT policy; sample advisory |
| **SM-11** Process verification | Internal audit of CSDL adherence per release | Most recent internal audit summary (under NDA) |
| **SM-12** Continuous improvement (metrics) | Vulnerability-density, MTTP, escape-rate KPIs tracked per release train | KPI dashboard extract (aggregate, under NDA) |
| **SM-13** Supplier-related issues | Third-party component monitoring; SBOM-driven CVE alerts | SBOM sample + monitoring workflow |

### 14.2 SR — Specification of Security Requirements

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SR-1** Product security context | Documented deployment topology, threat surface, trust boundaries for CSW | CSW deployment-model diagram; boundary description |
| **SR-2** Threat model | STRIDE-style threat models produced per major release / material change | Threat-model existence attestation (details under NDA) |
| **SR-3** Product security requirements | Security requirements traceable to threats + regulatory drivers (FIPS, Common Criteria, etc.) | Requirements matrix summary |
| **SR-4** Product security requirements content | Access control, data protection, session, error handling, resiliency requirements documented | Redacted requirements excerpt |
| **SR-5** Security requirements review | Reviewed by PSET at each release gate | Gate sign-off template |

### 14.3 SD — Secure by Design

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SD-1** Secure design principles | Defense in depth, least privilege, secure defaults, fail-secure documented in CSDL | Design principle policy |
| **SD-2** Defense in depth design | Multi-layer controls: agent → cluster → RBAC → transport → audit | Architecture overview / whitepaper |
| **SD-3** Security design review | Design review checklist gate; PSET sign-off before implementation | Review checklist template |
| **SD-4** Secure design best practices | Language-specific secure coding guidance (memory-safe, input validation, crypto libraries) | Secure coding standard reference |

### 14.4 SI — Secure Implementation

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SI-1** Secure implementation review | Peer review + PSET review of security-critical code paths | Review policy |
| **SI-2** Secure coding standards | Cisco-wide secure coding standards enforced (per language) | Standard document (under NDA) |
|  | Static analysis in CI (Coverity, semgrep, or equivalent) with security-severity gating | Tool inventory (aggregate) |
|  | Approved cryptographic libraries only (FIPS-validated where required) | Approved libraries list summary |

### 14.5 SVV — Security Verification & Validation Testing

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SVV-1** Security requirements testing | Test cases traced back to SR-3 requirements | Test-plan structure |
| **SVV-2** Threat mitigation testing | Test cases derived from SR-2 threat model | Threat-driven test summary |
| **SVV-3** Vulnerability testing | Fuzzing, SAST, DAST, SCA at build/release cadence | Tooling summary + cadence |
| **SVV-4** Penetration testing | Internal red-team + third-party pen tests per major release | Pen-test attestation (under NDA) |
| **SVV-5** Independence of testers | PSET testers are independent of feature-dev team; third-party testers external | Independence statement |

### 14.6 DM — Management of Security-Related Issues

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **DM-1** Receiving notifications | Cisco PSIRT — public intake (psirt@cisco.com), researcher liaison, CVD | Link to PSIRT process |
| **DM-2** Reviewing security-related issues | PSIRT triage + product BU joint assessment | Triage workflow overview |
| **DM-3** Assessing security-related issues | CVSSv3.1 scoring; exploitability + customer-context factors | Sample advisory showing scoring |
| **DM-4** Addressing security-related issues | Fix in patch train aligned to severity SLA | Patch cadence + SLA table |
| **DM-5** Disclosing security-related issues | Cisco Security Advisories published on tools.cisco.com | Sample CSW advisory URL |
| **DM-6** Periodic review | Portfolio-level trend review by PSIRT | Aggregate KPI summary |

### 14.7 SUM — Security Update Management

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SUM-1** Security update qualification | Regression + security regression tests before release | Regression suite summary |
| **SUM-2** Security update documentation | Release notes + advisories describe security fixes | Sample release notes |
| **SUM-3** Dependent component or OS security update documentation | SBOM + third-party CVE advisories referenced | SBOM sample |
| **SUM-4** Security update delivery | Cisco Software Central; signed packages | Delivery-mechanism description |
| **SUM-5** Timely delivery of security patches | Severity-driven SLA (Critical / High / Medium) | SLA table |

### 14.8 SG — Security Guidelines

| 62443-4-1 practice element (summary) | Cisco CSDL alignment | Reviewer can request |
|---|---|---|
| **SG-1** Product defense-in-depth | Hardening guides in CSW docs (agent, cluster, connector) | Links to hardening docs |
| **SG-2** Defense in depth measures expected in the environment | Deployment guides specify required network segmentation, IAM, PKI dependencies | Deployment prerequisites section |
| **SG-3** Security hardening guidelines | Baseline hardening in installer defaults; documented tuning for high-assurance environments | Hardening guide reference |
| **SG-4** Secure disposal guidelines | Decommission procedure includes credential rotation, agent removal, cluster wipe | Decommission SOP |
| **SG-5** Secure operation guidelines | Operator guides (RBAC, audit, backup) | Operator/admin guide links |
| **SG-6** Account management guidelines | Local + SSO/SAML admin account guidance | SSO integration doc |
| **SG-7** Documentation review | Docs versioned per release, reviewed by PSET for security-relevant changes | Doc-review checklist |

### 14.9 Recommended vendor due-diligence checklist

Give this list verbatim to your procurement / TPRM analyst. They should
raise it with the Cisco account team, not with the operations engineer
who deployed CSW.

- [ ] Cisco statement of CSDL applicability to CSW (product security plan reference)
- [ ] Cisco PSIRT policy link + sample CSW security advisory (public URL)
- [ ] Cisco Coordinated Vulnerability Disclosure (CVD) policy
- [ ] SBOM sample for the CSW release under evaluation
- [ ] Third-party pen-test attestation letter (under NDA)
- [ ] Signed-build / code-signing policy summary
- [ ] FIPS 140 validation status for cryptographic modules used by CSW
- [ ] Cisco supplier-attestation letter referencing 62443-4-1 practice
      alignment (if customer contract requires 4-1 language)
- [ ] Written statement on any current or planned SDLA / SSA
      certification programme for CSW
- [ ] Escalation path for customer-specific security requirements (CSR)
      not covered by standard documentation

### 14.10 Coverage at a glance

| 62443-4-1 practice area | Practice count | CSDL alignment | Public evidence | Under-NDA evidence |
|---|---|---|---|---|
| SM — Security Management | 13 | ✅ Full | Partial (policy summaries) | Full (audit + KPI) |
| SR — Specification of Security Requirements | 5 | ✅ Full | Diagrams only | Full |
| SD — Secure by Design | 4 | ✅ Full | Architecture whitepaper | Full |
| SI — Secure Implementation | 2+ | ✅ Full | Coding standard reference | Full |
| SVV — Security Verification & Validation | 5 | ✅ Full | Testing overview | Attestation letters |
| DM — Management of Security-Related Issues | 6 | ✅ Full | **Public** (PSIRT + advisories) | Aggregate metrics |
| SUM — Security Update Management | 5 | ✅ Full | **Public** (Software Central + release notes) | Delivery internals |
| SG — Security Guidelines | 7 | ✅ Full | **Public** (product docs) | Doc-review process |

**Certification note.** ✅ = practice-level alignment demonstrable via
CSDL. This is **not** an SDLA certification claim — see the disclaimer
on the companion Compliance Report.

---

## Related Frameworks

- [NERC CIP](../NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md) —
  analogous IT/OT boundary evidence pattern for BES entities.
- [NIST SP 800-82](https://csrc.nist.gov/publications/detail/sp/800-82/rev-3/final) —
  operational technology companion guidance (external).
- [ISO/IEC 27001:2022](../ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md) —
  when plants pair 62443 with enterprise ISMS audits.
- [NIST SP 800-207](../NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) —
  zero trust patterns for conduit enforcement narratives.

---

### Appendix A — Sample segmentation policy fragment (illustrative YAML-style)

> **Do not paste verbatim into production.** Replace scopes, addresses,
> and L4 tuples with values from your ZCRD. Syntax mirrors conceptual
> CSW rule metadata; exact API/UI format follows product version.

```yaml
workspace: IEC62443-Conduits-Site01
mode: simulation          # change to enforcement after sign-off
default_action: deny
rules:
  - name: conduit-opcua-historian
    action: allow
    src_scope: Plant-DMZ-Brokers
    dst_scope: Historian-MES-Tier
    services:
      - tcp/4840
  - name: admin-via-jump-only
    action: allow
    src_scope: Jump-EWS
    dst_scope: Plant-Site01-OT-Support
    services:
      - tcp/22
      - tcp/3389
  - name: log-unknown-east-west
    action: alert
    src_scope: Plant-Site01-OT-Support
    dst_scope: Plant-Site01-OT-Support
    match: not_in_conduit_allowlist
```

### Appendix B — PAS correlation workflow

1. Export **asset list** from Cyber Vision / Claroty / Nozomi (IP,
   MAC, VLAN, firmware).
2. Join on **IP or hostname** with CSW inventory.
3. Flag **CSW-only** or **PAS-only** assets — resolve before **SR 5**
   attestation.
4. For discrepancies, **field-verify** with plant engineering.

---

*Document prepared for industrial account engagements. Replace site
names, drawing references, and SL targets with customer-specific
values before delivery.*
