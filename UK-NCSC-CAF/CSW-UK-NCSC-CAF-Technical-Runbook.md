# CSW — UK NCSC CAF Technical Runbook

Engineering runbook mapping Cisco Secure Workload (CSW) controls to the
**UK NCSC Cyber Assessment Framework (CAF) v3.2**, used by UK Competent
Authorities for NIS Regulations (OES) assessments and by the Cabinet Office
GSG for GovAssure.

**Audience:** CSW administrators, Cisco SEs/SAs, and compliance engineers
preparing CAF evidence for an OES Competent Authority or a GovAssure
3rd-party assessor.

**Companion documents.** See [caf-mapping.md](./caf-mapping.md) for the
principle-by-principle crosswalk against sister frameworks already in this
repo. See [CSW-UK-NCSC-CAF-Compliance-Report.md](./CSW-UK-NCSC-CAF-Compliance-Report.md)
for the customer-facing narrative. See
[caf-igp-maturity-scorer.md](./caf-igp-maturity-scorer.md) for the IGP rubric.

**Status:** Draft v1 — SME review required.

---

## 0. Prerequisites

- CSW cluster deployed and reachable; agents installed on all workloads in
  scope for the essential service.
- API key with capabilities: `sensor_management`, `app_policy_management`,
  `flow_inventory_query`, `software_inventory`, `user_data_upload`.
- Operations toolkit cloned
  ([CSW_POV_Template](https://github.com/chandrapati/CSW-Operations-Toolkit)
  or equivalent) — specifically `cluster_snapshot.py`,
  `generate_vuln_report.py`, `generate_forensics_report.py`,
  `generate_executive_report.py`.
- Scope hierarchy modelled with CAF scope in mind (see Phase 1 below).

---

## 1. Phase 1 — Scope definition

CAF applies to **essential functions** and the systems supporting them. The
first engineering job is to translate "essential functions" into a CSW scope
hierarchy an auditor can read.

### Recommended CSW scope pattern

```
root-scope
├── CAF:Essential-Function:<name>        ← one per essential function
│   ├── Tier:Web
│   ├── Tier:App
│   ├── Tier:Data
│   └── Tier:Support                      ← identity, patching, backup
├── CAF:Supporting:<name>                 ← systems supporting an EF but not the EF itself
└── CAF:Out-of-Scope                      ← explicitly carved out
```

Workloads inside `CAF:Essential-Function:*` are "in scope" for the CAF
assessment. The explicit `CAF:Out-of-Scope` scope exists so an assessor
can see what was deliberately excluded and why.

### Labels / tags to apply (per workload)

| Label | Example values | CAF principle this feeds |
|---|---|---|
| `caf_essential_function` | `electricity_distribution`, `patient_record_system` | A3, B5 |
| `caf_tier` | `web`, `app`, `data`, `support`, `ot_adjacent` | B5, B1 |
| `caf_data_classification` | `ePHI`, `PII`, `operational`, `public` | A3, B3 |
| `caf_criticality` | `critical`, `high`, `medium`, `low` | A2 |
| `caf_owner_team` | `payments_eng`, `clinical_apps` | A1, A3 |
| `caf_regulator` | `ofgem`, `ofcom`, `dwi`, `caa`, `dft`, `dhsc`, `govassure` | — |

Push these as annotations via `user_data_upload` from your CMDB.

### Deliverable from Phase 1

- `scope-model.md` — explains the scope tree and the labels, signed off by
  the CAF scoping SME.
- `scope-workloads.json` — snapshot of which workload lives in which CAF
  scope (produced via `cluster_snapshot.py`).

---

## 2. Phase 2 — Policy authoring per CAF principle

Policies live inside CSW workspaces. One workspace per essential function
is the recommended pattern.

### Policy design per principle

- **B5 (segmentation):** Default-deny between CAF essential-function scopes;
  explicit allows only for documented data flows; cross-tier flows
  restricted to the specific ports/processes ADM identified. For IT/OT
  separation, add an explicit `CAF:Essential-Function:*` → `CAF:OT-Zone:*`
  deny with narrow exceptions.
- **B1 (policies & processes):** Every policy carries a human-readable
  description; version tagged with change ticket; owner labelled.
- **B4 (system security):** Policies that deny known-vulnerable-service
  ports (telnet, old SMB, plaintext SNMP) across all CAF scopes.
- **B3 (data security — in transit):** FIPS-aligned deny of plaintext
  protocols for workloads tagged `caf_data_classification=PII` or stricter
  (see [FIPS 140 runbook](../FIPS-140/) for pattern).

### ADM → simulate → enforce workflow

1. Run ADM on each `CAF:Essential-Function:*` workspace to get a baseline
   policy proposal.
2. Review in CSW UI; adjust against the documented authorised data flows
   for the essential function.
3. **Simulate** for at least two full business cycles (typically 2 weeks)
   before enforcement. Simulation reports become evidence for A2
   ("continuous, not annual").
4. Enforce in staged rings: Tier:Support → Tier:Web → Tier:App → Tier:Data.
5. Keep ADM version history as change log — this is B1 evidence.

### Deliverable from Phase 2

- `policies-authored.json` (via `download_policies.py`) — the current policy
  set per workspace.
- `simulation-report-<yyyy-mm-dd>.html` per essential function — pre-enforcement
  evidence of what would be allowed vs rejected.
- `policy-change-log-<yyyy-mm-dd>.md` — ADM versions and the human-approved
  changes between them.

---

## 3. Phase 3 — Evidence collection per CAF Objective

Automate the following so evidence is produced on a cadence, not scrambled
for the audit.

### Monthly (per cluster)

```bash
python3 cluster_snapshot.py            # A3, A2, B4 (point-in-time inventory + posture)
python3 generate_vuln_report.py        # B4, A2 (CVE inventory with CVM intel)
python3 generate_forensics_report.py   # C2 (MITRE technique coverage)
python3 download_flows.py --hours 720  # C1 (30-day flow archive)
python3 generate_executive_report.py \
  --snapshot-latest \
  --prepared-for "<Essential Function Owner>" \
  --prepared-by "SecOps"               # A1, A2 governance telemetry
```

### Weekly (per cluster)

```bash
python3 cluster_delta.py \
  --from snapshots/snapshot-<prev-week>.json \
  --to   snapshots/snapshot-<this-week>.json   # D2 improvement evidence
```

### Per enforcement change

```bash
python3 download_policies.py           # B1 change log
```

### Mapping evidence artefacts to CAF Objectives

| CSW artefact | CAF Objectives served |
|---|---|
| `snapshot-*.json` | A2, A3, A4 (partial), B4 |
| `vulnerabilities-*.csv` | A2, B4 |
| `policies-all.json` + ADM version history | B1, B5 |
| `conversations-*.json` / `flows-*.csv` | C1, B5 (verification), D1 (IR timeline) |
| `forensics-posture-*.html` | C2 |
| `simulation-report-*.html` | A2, B1 |
| `executive-summary-*.html` / `.md` | A1, A2 |
| `cluster-delta-*.md` | D2 |

---

## 4. Phase 4 — Quarterly CAF evidence pack

A GovAssure or OES Competent Authority submission typically wants an
evidence pack covering each CAF principle. Pre-stage the files monthly;
assemble the pack quarterly.

### Pack structure

```
caf-evidence-pack-<yyyy-qq>/
├── 00_overview.md                      ← executive summary + scope attestation
├── A1_Governance/
├── A2_Risk_Management/
├── A3_Asset_Management/
├── A4_Supply_Chain/
├── B1_Policies_Processes/
├── B2_Identity_Access/                 ← pointer to IdP evidence (no CSW output)
├── B3_Data_Security/
├── B4_System_Security/
├── B5_Resilient_Networks/
├── B6_Staff_Awareness/                 ← pointer to training evidence
├── C1_Security_Monitoring/
├── C2_Proactive_Discovery/
├── D1_Response_Recovery/
├── D2_Improvements/
└── 99_disclaimers_and_pairings.md
```

See [caf-evidence-pack-template.md](./caf-evidence-pack-template.md) for
exactly what file goes in each folder.

---

## 5. Common assessor questions and the CSW answer

| Question | CSW evidence |
|---|---|
| *"Prove the control still held last Tuesday, not just today."* | Monthly `snapshot-*.json` and flow archive — point-in-time attestation. |
| *"How do you know you'd see an attacker moving laterally?"* | Flow telemetry + rejected-flows report + MITRE forensics coverage. |
| *"How do you measure improvement since the last assessment?"* | `cluster_delta.py` output + `executive-summary` trend. |
| *"What enforces the segmentation — is it just a firewall rule you hope stays?"* | Policies are enforced in-kernel on every host (nftables / WFP); CSW continuously verifies. |
| *"How do you handle supplier access?"* | Scope-tagged egress flows; vendor-package inventory; pair with TPRM. |
| *"What about identity?"* | Explicit: CSW is not an IAM tool. Point to IdP + PAM evidence. |

---

## 6. SE / SA conversation starters

Lift from the repo's
[SE compliance role-play](../docs/se-compliance-cyber-insurance-roleplay.md)
but tailored to a UK assessor conversation:

1. *"Which of your essential functions is being assessed first — and how
    many workloads sit inside its boundary?"* → scopes problem to real
    numbers.
2. *"Who is your Competent Authority for this programme (Ofgem? DWI? GSG?)
    and what have they flagged in prior assessments?"* → anchors conversation
    in regulator language.
3. *"Can you show me the current scope-isolation attestation between IT
    and OT today?"* → opens IEC 62443 / Purdue conversation; CSW is the
    IT side.
4. *"When you need to tell your Competent Authority that control X still
    held last Tuesday, where does that evidence come from?"* → surfaces
    continuous-vs-annual pain, where CSW shines.

---

## 7. Known limitations and pairings

- **B2 (Identity):** CSW cannot satisfy. Pair with IdP + PAM. Use
  [ISE integration](https://github.com/chandrapati/csw-ise-integration) for
  identity-aware segmentation (identity assertion from ISE).
- **B6 (Training):** Out of scope.
- **D1 (Backup/DR):** CSW contains blast radius; it does not restore
  services. Pair with backup/DR platform.
- **OT device tier:** CSW does not run on PLCs/RTUs/IEDs. Pair with
  Cyber Vision / Claroty / Nozomi / Dragos.
- **Perimeter / DDoS:** CSW is east-west only. Pair with Secure Firewall
  and DDoS service.

---

## Disclaimer

Draft v1. Requires SME review against the current CAF text (v3.2 at time
of authoring) and against your Competent Authority's expectations before
relied upon in a formal assessment. See
[repository disclaimer](../README.md#disclaimer).
