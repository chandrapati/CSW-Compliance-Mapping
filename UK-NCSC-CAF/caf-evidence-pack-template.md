# CAF Evidence Pack Template

Per-principle template for a quarterly CSW evidence pack suitable for a
UK Competent Authority (NIS OES) or Cabinet Office GSG (GovAssure)
submission.

**Status:** Draft v1 — SME review required.

---

## Pack-level conventions

- **One pack per cluster per quarter.** Naming:
  `caf-evidence-pack-<yyyy>-Q<n>/`.
- **Overview + disclaimer at the pack root.** Reviewers read these first.
- **Fourteen principle folders** (A1 … D2), in CAF order.
- **No real credentials, no secrets, no API keys.** CSW evidence is
  configuration + telemetry snapshots, not credentials.
- **Chain of custody.** Each file carries metadata (who exported it,
  when, which CSW tenant, which cluster snapshot JSON it derived from).
  Capture via the companion `evidence-package-manifest.yaml` pattern
  already in [this repository's templates](../templates/evidence-package-manifest.yaml).
- **Integrity.** Every file in the pack is SHA-256 hashed and listed in
  a top-level `MANIFEST.sha256` so reviewers can verify no post-export
  edits occurred.

---

## Pack structure

```
caf-evidence-pack-<yyyy>-Q<n>/
├── 00_overview.md
├── MANIFEST.sha256
├── manifest.yaml                      ← uses evidence-package-manifest.yaml schema
├── A1_Governance/
├── A2_Risk_Management/
├── A3_Asset_Management/
├── A4_Supply_Chain/
├── B1_Policies_Processes/
├── B2_Identity_Access/
├── B3_Data_Security/
├── B4_System_Security/
├── B5_Resilient_Networks/
├── B6_Staff_Awareness/
├── C1_Security_Monitoring/
├── C2_Proactive_Discovery/
├── D1_Response_Recovery/
├── D2_Improvements/
└── 99_disclaimers_and_pairings.md
```

---

## What to put in each folder

### 00_overview.md

```markdown
# CAF Evidence Pack — <Essential Function Name>

- Reporting period: <YYYY-MM-DD> to <YYYY-MM-DD>
- Essential function: <name>
- CSW cluster: <cluster_label>
- Pack owner (CSW side): <name, title, team>
- Pack owner (CAF side): <name, title, team>
- Competent Authority: <Ofgem | Ofcom | DWI | CAA | DfT | DHSC | GovAssure>
- Prior pack reference: <path or Q-id>
- Significant changes since prior pack: <summary>
- Known limitations: <summary — e.g. B2 evidence sits with IdP team>
```

### MANIFEST.sha256

Standard shasum file — generate with:
```bash
cd caf-evidence-pack-<yyyy>-Q<n>
find . -type f ! -name MANIFEST.sha256 -exec shasum -a 256 {} \; > MANIFEST.sha256
```

### A1_Governance/
- `executive-summary-<date>.html` — latest CISO/board posture summary.
- `executive-summary-<date>.md` — same, Markdown version.
- `governance-attestation.md` — one-page statement signed by named
  governance owner confirming cadence and consumption.

### A2_Risk_Management/
- `snapshot-<date>.json` (latest) + `snapshot-<prev>.json` (prior-quarter).
- `cluster-delta-<prev-to-current>.md`.
- `vulnerabilities-<date>.csv`.
- `risk-register-mapping.md` — short note tying CSW metrics to risk-register entries.

### A3_Asset_Management/
- `snapshot-<date>.json` (reference — same file as A2; link rather than duplicate if your pack supports it).
- `scope-workloads.json`.
- `cmdb-reconciliation-<date>.md` — asset count vs CMDB; gaps triaged.
- `agent-coverage-attestation.md` — % coverage statement signed by Platform Eng lead.

### A4_Supply_Chain/
- `vendor-package-inventory-<date>.csv` — filtered from `vulnerabilities-*.csv` by vendor.
- `vendor-egress-reconciliation-<date>.md` — flows to vendor endpoints vs contracted vendor list.
- Pointer: `../../tprm-evidence/` or equivalent (TPRM lives outside this pack).

### B1_Policies_Processes/
- `policies-all-<date>.json`.
- `policy-change-log-<quarter>.md` — ADM version diffs with ticket references.
- `simulation-reports/` — pre-enforcement simulation outputs for any policy changes this quarter.
- `rejected-flows-review-<quarter>.md` — periodic review of denied flows and triage outcomes.

### B2_Identity_Access/
- `README.md` — explicit statement that CSW does not satisfy B2; pointer to IdP + PAM evidence.
- Optional: `ise-integration-posture.md` if ISE identity-aware segmentation is in use.

### B3_Data_Security/
- `flows-<date>-data-tier.csv` — east-west flows into data-tier scopes.
- `insecure-cipher-hosts-<date>.csv` — hosts flagged with deprecated TLS; remediation plan annotations.
- `plaintext-protocol-deny-policies.md` — list of deny policies for plaintext protocols on sensitive data classes.
- Pointer: `../../kms-and-dlp-evidence/` for data-at-rest + DLP (not CSW).

### B4_System_Security/
- `vulnerabilities-<date>.csv` — primary artefact (same as A2; link if dedup allowed).
- `patch-sla-attainment-<quarter>.md` — Critical ≤30d, High ≤60d attainment %.
- `agent-version-drift-<date>.md` — fleet version distribution.
- `vulnerable-service-port-deny-policies.md` — summary of CSW policies denying known-vulnerable ports.

### B5_Resilient_Networks/ *(the primary CSW folder)*
- `policies-all-<date>.json` — enforcement set per scope.
- `blast-radius-trend-<quarter>.md` — score over quarter, with before/after if a project landed.
- `scope-isolation-attestation-<date>.md` — explicit "IT scopes X,Y,Z are isolated from OT scopes P,Q,R" statement with supporting flow evidence.
- `it-ot-boundary-evidence.md` — Purdue / IEC 62443 narrative.
- `enforcement-coverage-report-<date>.html` — % of in-scope workloads in enforcement mode.
- Pointer: `../../ot-visibility-evidence/` for OT device-tier evidence (Cyber Vision / equivalent).

### B6_Staff_Awareness/
- `README.md` — explicit statement that CSW does not satisfy B6; pointer to training-platform evidence.

### C1_Security_Monitoring/
- `flow-retention-attestation.md` — statement of retention duration + storage location.
- `siem-integration-attestation.md` — SIEM destination + SOC playbook references.
- `agent-health-report-<date>.html` — agent heartbeat and health across fleet.
- `ntp-synchronisation-attestation.md` — cluster NTP source + agent sync confirmation.

### C2_Proactive_Discovery/
- `forensics-posture-<date>.html` — MITRE technique coverage across cluster.
- `forensics-config-<date>.json` — raw config dump.
- `mitre-coverage-gaps-<quarter>.md` — gaps identified + new rules added this quarter.
- `anomaly-review-<quarter>.md` — rejected-flow or forensic-event anomalies that triggered SOC investigation.

### D1_Response_Recovery/
- `blast-radius-containment-case-studies/` — any real or tabletop incidents where CSW segmentation limited scope.
- `adm-rollback-rehearsal-<date>.md` — evidence that ADM version rollback was exercised.
- `ir-flow-timeline-<incident-id>.md` — if a real incident happened this quarter.
- Pointer: `../../backup-dr-evidence/` for backup/DR (not CSW).

### D2_Improvements/
- `cluster-delta-<quarter>.md` — same artefact as A2; link if dedup allowed.
- `pir-input-<quarter>.md` — summary of lessons-learned fed back into CSW policy / process from PIR cycles.
- `policy-changes-attributed-to-pir.md` — specific policy edits traced to PIR findings.

### 99_disclaimers_and_pairings.md

- Explicit list of what this pack does **not** cover and where that
  evidence lives (IdP for B2, training platform for B6, KMS/DLP for B3,
  backup/DR for D1, perimeter/DDoS for B5, OT visibility for B5).
- Pairings matrix: for each paired control, named owner + attestation
  reference.
- Repository disclaimer and SME-review notice.

---

## Automation hint

A `build-caf-pack.sh` wrapper can:

```bash
#!/usr/bin/env bash
# Build a quarterly CAF evidence pack.
set -euo pipefail
QUARTER="${1:?usage: build-caf-pack.sh YYYY-Qn}"
OUT="caf-evidence-pack-${QUARTER}"
mkdir -p "$OUT"/{A1_Governance,A2_Risk_Management,A3_Asset_Management,A4_Supply_Chain,B1_Policies_Processes,B2_Identity_Access,B3_Data_Security,B4_System_Security,B5_Resilient_Networks,B6_Staff_Awareness,C1_Security_Monitoring,C2_Proactive_Discovery,D1_Response_Recovery,D2_Improvements}

# Pull latest CSW artefacts
python3 cluster_snapshot.py
python3 generate_vuln_report.py
python3 generate_forensics_report.py
python3 generate_executive_report.py --snapshot-latest
# ... etc

# Copy into the right principle folders (symlinks reduce duplication)
cp snapshots/snapshot-*.json           "$OUT/A2_Risk_Management/"
cp -r snapshots/snapshot-*.json        "$OUT/A3_Asset_Management/"
cp reports/executive-summary-*.{html,md} "$OUT/A1_Governance/"
# ... etc

# Generate manifest
cd "$OUT"
find . -type f ! -name MANIFEST.sha256 -exec shasum -a 256 {} \; > MANIFEST.sha256
```

Full wrapper left as a Phase 5 deliverable once the content is validated
with your first Competent Authority / 3PAO cycle.

---

## Disclaimer

Draft v1. See [repository disclaimer](../README.md#disclaimer).
