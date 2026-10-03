# Cisco Secure Workload — UK NCSC CAF Compliance Report

**Framework:** UK NCSC Cyber Assessment Framework (CAF) v3.2
**Audience:** CISO, Head of Compliance, CAF Lead Assessor, Competent
Authority relationship owner.
**Status:** Draft v1 — SME review required.

---

## Executive summary

The UK NCSC Cyber Assessment Framework (CAF) is the outcome-based security
assessment framework used by UK Competent Authorities (Ofgem, Ofcom, DWI,
CAA, DfT, DHSC) under the NIS Regulations and by the Cabinet Office
Government Security Group under GovAssure. It evaluates an organisation
against **14 Principles** grouped under **4 Objectives**, scored against
Indicators of Good Practice (IGPs) as **Achieved**, **Partially Achieved**,
or **Not Achieved**.

Cisco Secure Workload (CSW) is a workload-visibility, microsegmentation,
and east-west security platform. CSW does not satisfy any CAF principle
on its own — no single product does — but it is a **primary evidence
source for 6 of the 14 principles** (A2, A3, B1, B4, B5, C1, C2) and a
supporting source for several more. It is particularly strong for CAF
Objective B (Protect) and Objective C (Detect), which is exactly where
network segmentation, host-level visibility, and continuous telemetry
belong in the CAF model.

For a Competent Authority assessment, the practical consequence is that
CSW output can drive the **"Achieved" vs "Partially Achieved" distinction**
on technical IGPs because the evidence is **continuously verified**
(every connection, every day) rather than **sampled annually**.

---

## What CSW contributes per CAF Objective

### Objective A — Managing Security Risk

- **A2 Risk Management (Primary).** CSW produces a dynamic risk picture:
  blast-radius score (0–100), enforcement coverage %, exploitable-CVE
  counts filtered through CVM intelligence, and change deltas between
  snapshots. The CAF explicitly wants organisations to move "away from
  static annual audits to dynamic threat modelling" — CSW is on the right
  side of that transition.
- **A3 Asset Management (Primary).** Real-time inventory of workloads,
  installed packages, interface addresses, scope membership, and agent
  posture. Pairs with CMDB/IPAM/cloud-provider sources via CSW connectors.
- **A1 Governance / A4 Supply Chain (Supporting).** CSW produces
  governance telemetry (board-ready posture summaries) and vendor-code
  presence signals; it does not substitute for governance structure or
  TPRM programmes.

### Objective B — Protecting Against Cyber Attack

- **B5 Resilient Networks & Systems (Primary — CSW core).** This is where
  CSW is strongest. The CAF explicitly cites "Zero-Trust Microsegmentation
  (host firewall orchestration, eBPF in-kernel filtering)" and "software-
  defined perimeters, IT/OT DMZs" as the key technical controls for B5
  — this is a word-for-word description of CSW. For IT/OT separation
  under the Purdue Model / IEC 62443, CSW handles the IT tier; pair with
  Cisco Cyber Vision or equivalent for the OT device tier.
- **B1 Policies & Processes (Primary).** Workspace-based policy authoring
  with ADM-suggested baselines, pre-enforcement simulation, in-kernel
  enforcement, and ADM version history as change log.
- **B4 System Security (Primary).** Per-workload CVE inventory with
  exploit-intelligence prioritisation; package inventory for patch
  targeting; agent-version drift as config-baseline signal.
- **B3 Data Security (Supporting).** East-west segmentation prevents
  unauthorised data paths; insecure-cipher count flags TLS hygiene gaps.
  Pair with KMS, DLP, and data classification.
- **B2 Identity & Access (Out of scope).** CSW is not an IAM tool. Pair
  with your IdP and PAM; use ISE integration if identity-aware
  segmentation is required.
- **B6 Staff Awareness (Out of scope).**

### Objective C — Detecting Cyber Security Events

- **C1 Security Monitoring (Primary).** Continuous per-connection flow
  telemetry (NetFlow-grade with process context and policy decision);
  agent health heartbeats; forensics event stream; SIEM egress via Splunk
  (or equivalent). Covers the CAF's call for "endpoints, network flows
  (NetFlow/IPFIX/eBPF), firewalls, and authentication events".
- **C2 Proactive Event Discovery (Primary).** MITRE ATT&CK technique
  coverage through CSW forensics rules; vulnerability scanning with
  threat-intel enrichment; anomaly detection via policy-violation
  (rejected-flow) analysis.

### Objective D — Minimising the Impact of Incidents

- **D1 Response & Recovery (Supporting).** CSW contains blast radius
  (limits incident scope) and provides per-connection flow history for
  IR timeline reconstruction. CSW does not operate backup, restore, or
  DR orchestration — pair with your backup/DR platform.
- **D2 Improvements (Supporting).** Snapshot history and cluster-delta
  tracking feed quarter-over-quarter improvement narratives.

---

## IGP maturity narrative (how CSW moves the needle)

A representative CAF journey, year-over-year:

| Principle | Year 0 (baseline) | Year 1 (CSW adopted) | Year 2 (CSW mature) |
|---|---|---|---|
| A2 | Partially Achieved — annual risk register | Partially Achieved — monthly posture snapshot | Achieved — monthly dynamic risk picture tied to business impact |
| A3 | Partially Achieved — CMDB only | Achieved — CMDB + live sensor census reconciled |
| B1 | Partially Achieved — policies on paper | Partially Achieved — authored in CSW, simulated | Achieved — enforced + continuously tested via rejected-flow log |
| B4 | Partially Achieved — monthly vuln scan | Achieved — CVM-prioritised, workload-contextualised, trended |
| B5 | Not / Partially Achieved | Partially Achieved — segmentation designed & simulated | Achieved — microsegmentation enforced, blast-radius score ≥85 |
| C1 | Partially Achieved — firewall logs only | Achieved — endpoint + flow + policy decision telemetry |
| C2 | Partially Achieved | Achieved — MITRE technique coverage tracked |
| D1 | Partially Achieved | Partially Achieved — containment improves but DR unchanged |

The maturity scorer document (see
[caf-igp-maturity-scorer.md](./caf-igp-maturity-scorer.md)) gives the
specific CSW KPI thresholds behind each tier shift.

---

## What CSW explicitly does **not** satisfy

Being honest about scope is itself CAF-aligned (Principle A1 wants clear
accountability). The following CAF obligations are **not** addressable
by CSW alone and must be evidenced through pairings:

- **B2 Identity & Access** — IdP + PAM (CSW consumes identity, doesn't
  issue it).
- **B6 Staff Awareness & Training** — security awareness platform.
- **B3 Data at rest + key management** — KMS/HSM + storage encryption.
- **D1 Backup / restore / BCP** — backup/DR platform.
- **A1 Governance structure** — org-chart, roles, resourcing decisions.
- **Perimeter / DDoS** — Secure Firewall + DDoS service.
- **OT device tier (B5)** — Cyber Vision / Claroty / Nozomi / Dragos.

A credible CAF submission must address these pairings explicitly rather
than ignore them.

---

## Suggested next steps

1. **Scope workshop.** Translate essential functions into the CSW scope
   pattern described in the
   [Technical Runbook](./CSW-UK-NCSC-CAF-Technical-Runbook.md) Phase 1.
2. **Baseline snapshot.** Run `cluster_snapshot.py` and
   `generate_executive_report.py` to capture the current posture — this
   becomes "Year 0" in the maturity narrative.
3. **Policy authoring.** Author B5 segmentation per essential function
   with the ADM-suggested baseline; simulate for two full business cycles.
4. **Quarterly evidence pack.** Pre-stage CSW artefacts into the pack
   structure described in
   [caf-evidence-pack-template.md](./caf-evidence-pack-template.md).
5. **Pair-up matrix.** Document which pairings (IdP, PAM, DLP, backup,
   training, OT visibility, perimeter) will supply the non-CSW evidence.
6. **Pre-assessment dry run.** Walk the pack with the CAF Lead Assessor
   before the formal Competent Authority / 3PAO engagement.

---

## Disclaimer

Draft v1. Mapping derived from the UK NCSC CAF v3.2 and documented CSW
capabilities. For informational and reference purposes only — not legal,
regulatory, or audit advice. Requires SME review against the current CAF
text and your Competent Authority's expectations before relied upon in a
formal assessment. See the
[repository-level disclaimer](../README.md#disclaimer) for the full clause.
