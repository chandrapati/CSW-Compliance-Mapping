# Cisco Secure Workload — CISA Zero Trust Maturity Model
## Technical Runbook | Federal & Enterprise Accounts

**Version:** 1.0 | **Standard:** CISA Zero Trust Maturity Model v2.0 (2023)

---

## 1. Overview

The CISA Zero Trust Maturity Model (ZTMM) v2.0 defines maturity across **5 pillars**: Identity, Devices, Networks, Applications & Workloads, and Data. CSW is the primary Cisco platform addressing the **Networks** pillar and makes significant contributions to **Applications & Workloads** and **Data** pillars. Each pillar has 4 maturity stages: Traditional → Initial → Advanced → Optimal.

---

## 2. CSW Maturity Mapping — Networks Pillar (Primary)

The Networks pillar focuses on macro/micro-segmentation, encryption, and network traffic management.

| Maturity Stage | Networks Pillar Requirement | CSW Capability |
|---|---|---|
| **Traditional** | Coarse perimeter-based segmentation | CSW ADM reveals actual traffic — baseline for improvement |
| **Initial** | Basic internal segmentation; some visibility | CSW ADM deployed; monitoring mode; scopes defined |
| **Advanced** | Micro-segmentation enforced; encrypted traffic | CSW enforcement active; allowlist policies; encryption detection |
| **Optimal** | Dynamic policy; continuous validation; full automation | CSW ADM continuous re-run; API-driven policy updates; ML anomaly detection |

### Achieving Advanced Maturity (Networks)

```
Phase 1 — Initial (Weeks 1-4):
  ✓ Deploy CSW sensors across all workloads
  ✓ Run ADM — document all traffic flows
  ✓ Define scope hierarchy (environment, sensitivity, function)
  ✓ Enable flow telemetry and alerting

Phase 2 — Advanced (Weeks 5-12):
  ✓ Build allowlist policies from ADM baseline
  ✓ Enable enforcement mode on sensitive scopes
  ✓ Detect and block unencrypted flows (HTTP, Telnet, FTP)
  ✓ Isolate workloads into least-privilege network segments
  ✓ Configure anomaly detection on production scopes

Phase 3 — Optimal (Ongoing):
  ✓ Continuous ADM re-runs (90-day cycles)
  ✓ API integration with SOAR for automated policy response
  ✓ ML-based behavioral baseline deviation detection
  ✓ Dynamic policy adjustment based on workload risk score
```

---

## 3. CSW Maturity Mapping — Applications & Workloads Pillar

| Maturity Stage | Requirement | CSW Capability |
|---|---|---|
| **Traditional** | No workload-level visibility | ADM provides first-ever workload communication map |
| **Initial** | Basic application inventory; some access controls | CSW inventory + scope-based access policies |
| **Advanced** | Workload identity-based access; continuous monitoring | Process-level identity; policy enforcement; anomaly detection |
| **Optimal** | Automated workload security; continuous validation | API-driven policy; vulnerability-triggered policy updates |

**Key CSW Contributions:**
- **Workload Identity:** CSW uses process hash, OS fingerprint, and network identity — not just IP
- **Least Privilege Workload Access:** Each workload allowed only its documented communication paths
- **Continuous Validation:** ADM re-runs validate workloads haven't expanded their access footprint
- **Vulnerability-Aware Policy:** Critical CVEs on a workload can trigger automatic policy tightening

---

## 4. CSW Maturity Mapping — Data Pillar (Supporting)

| Maturity Stage | Requirement | CSW Capability |
|---|---|---|
| **Traditional** | No data flow visibility | ADM reveals all data movement paths |
| **Initial** | Data categorized; basic access controls | Scope-based isolation for sensitive data workloads |
| **Advanced** | Data access logged; encryption enforced | Full flow telemetry; encryption compliance enforcement |
| **Optimal** | Automated data protection response | Alert-triggered policy updates on data access violations |

---

## 5. CISA ZTMM Pillar Coverage Summary

| Pillar | CSW Role | Maturity Achievable |
|---|---|---|
| Identity | Supporting (enforces identity-verified access paths) | Initial → Advanced |
| Devices | Supporting (process + OS-level workload fingerprinting) | Initial → Advanced |
| Networks | **Primary** (micro-segmentation, encryption, monitoring) | Advanced → Optimal |
| Applications & Workloads | **Primary** (workload identity, policy, vulnerability) | Advanced → Optimal |
| Data | Supporting (data flow visibility, encryption enforcement) | Initial → Advanced |

---

## 6. CSW Deployment Phases for ZTMM

### Phase 1 — Establish Visibility (Traditional → Initial)
```
Week 1-2:   Deploy sensors (on-prem + cloud connectors)
Week 3-4:   Run ADM — generate traffic baseline
Week 4:     Define scope hierarchy
Week 4:     Enable flow telemetry retention (12 months)
```

### Phase 2 — Enforce Least Privilege (Initial → Advanced)
```
Week 5-6:   Build allowlist policies from ADM
Week 7-8:   Simulation mode — validate no false positives
Week 9-10:  Enforcement mode — sensitive scopes first
Week 11-12: Encryption enforcement; block non-compliant protocols
Week 12:    Full alerting and SIEM integration
```

### Phase 3 — Continuous Validation (Advanced → Optimal)
```
Month 4+:   90-day ADM re-run cycles
Month 4+:   Vulnerability-triggered policy review
Month 6+:   API integration with SOAR
Month 6+:   Automated policy tightening on critical CVEs
Ongoing:    Maturity assessment vs ZTMM scorecard
```

---

## 7. ZTMM Assessment Evidence Package

| Evidence Item | CSW Source | ZTMM Pillar | Maturity Stage |
|---|---|---|---|
| ADM traffic baseline | Investigate → ADM | Networks, Apps | Initial |
| Enforcement policy export | Defend → Policy Workspaces | Networks, Apps | Advanced |
| Encryption compliance report | Flow Search (protocol filter) | Networks, Data | Advanced |
| Anomaly detection log | Alerts → Dashboard | Networks | Advanced |
| Vulnerability report | Investigate → Vulnerability | Apps | Advanced |
| Continuous ADM comparison | ADM re-run vs baseline | Networks, Apps | Optimal |
| API policy automation evidence | CSW API audit log | Networks | Optimal |
| Workload inventory | Manage → Inventory | Devices, Apps | Initial |

---

## 8. ZTMM Scorecard Template

| Pillar | Current Stage | Target Stage | CSW Actions Required |
|---|---|---|---|
| Identity | Traditional | Advanced | Enforce identity-verified access paths via CSW |
| Devices | Initial | Advanced | Process-level workload fingerprinting; anomaly detection |
| Networks | Initial | Optimal | Full enforcement; encryption; continuous ADM |
| Applications | Traditional | Advanced | Workload-level policy; vulnerability management |
| Data | Traditional | Advanced | Data flow visibility; encryption enforcement |

---

*Replace [Customer Name] and bracketed fields before customer delivery.*
