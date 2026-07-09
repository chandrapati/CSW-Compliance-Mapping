# Cisco Secure Workload — Compliance Mapping Assets

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=chandrapati.CSW-Compliance-Mapping&left_text=visitors)

Customer-facing reports and matching technical runbooks that map Cisco
Secure Workload (CSW) controls to **thirty-four** compliance, sector, and
zero-trust frameworks. Every framework folder ships the same set of
assets: a Markdown technical runbook (the engineering view), a DOCX
report (the editable customer master), a PDF render of that report,
and HTML versions of both for browser/mobile reading.

> **New here?** Read [Background — What is Cisco Secure Workload?](./docs/about-csw.md)
> for a one-page intro to the platform itself, then come back to pick a
> framework.

## Executive overview — 60-second read

> **For a CISO / CIO skimming this for the first time.**

- **What this is.** A reference library that maps Cisco Secure Workload
  (CSW) capabilities to **34 security, regulatory, and zero-trust
  frameworks** — so you can see *which* controls CSW helps you evidence,
  and *how*, before committing budget or audit hours.
- **What you get per framework.** Two paired documents — a **technical
  runbook** (the engineering view: configuration steps, sample policies,
  exact evidence exports) and a **customer-facing report** (the narrative
  built on that work) — each in Markdown, DOCX, PDF, and HTML.
- **The core idea.** CSW turns live workload behaviour — *who talks to
  whom, on which port, via which process, and what changed* — into
  micro-segmentation, drift tracking, and forensic-grade flow evidence.
  The same evidence answers the **auditor** ("prove the control still
  holds, not just on audit day") and the **incident responder** ("what
  moved laterally, and what changed"). That overlap is why segmentation
  shows up across PCI, HIPAA, NIST, DORA, NIS2, and the zero-trust models.
- **Where to start.** New to CSW → [compliance evidence
  playbook](./docs/compliance-evidence-playbook.md). Hunting a specific
  control → [`INDEX.md`](./INDEX.md). Choosing a framework → the
  [asset library](#asset-library) table below.
- **Read this before relying on it.** These mappings are **informational
  reference only** — not legal, audit, or completeness advice. They
  require **SME review** against current official sources and your
  assessors. Note the explicitly-labelled drafts and proposals: **HIPAA
  2025 NPRM** is a *proposed* rule; **CIS / CSF 2.0 / CMMC 2.0** and
  **NERC CIP / TSA Pipeline** are *draft v1* cross-framework or
  IT-side sector overlays. See the full [Disclaimer](#disclaimer).

## Why these mappings exist

Compliance frameworks were written by humans trying to describe what
"good security" looks like for a class of risk. They are *outcomes*,
not products. The hardest question a customer faces is not *"what does
the standard require?"* — it's *"for the workloads I actually defend,
can I actually prove — with evidence that survives scrutiny — that the
control still holds tomorrow, not just on audit day?"*

These mappings exist to close that gap. For each framework, they trace
specific controls (e.g. PCI DSS Req 1.2.1, HIPAA §164.312(a)(1), NIST
AC-4) to concrete CSW capabilities — micro-segmentation, process-level
telemetry, software inventory, vulnerability awareness, forensic flow
data, and authored workload policy — and explain how those capabilities
can contribute evidence for assessor review when deployed in scope.

The same workload-resident evidence that can support an auditor's review also
shortens the questions defenders ask under pressure: *what was talking
to what, on which port, via which process, and what changed?* That
overlap is not a coincidence — it's why segmentation, lateral-movement
visibility, and patching priority show up across PCI Req 1, HIPAA
§164.312, NIST AC-4, ISO A.8.22, DORA Art. 9, NIS2 Art. 21(2)(j) and the
zero-trust frameworks. Standards writers captured the failure modes
people keep living through; treating those obligations as audit
busywork forfeits blast-radius containment while still paying for the
programme.

For the longer argument — including the five conversation-starter
questions worth walking through against your own environment — see
[Why these mappings matter](./docs/why-these-mappings-matter.md).

## Customer design aids

| Asset | Use it for | Formats |
|---|---|---|
| **Compliance evidence playbook** | Step-by-step CSW operations for newcomers — coverage, ADM, simulation, enforce, quarterly export pack | [MD](./docs/compliance-evidence-playbook.md) · [PDF](./docs/compliance-evidence-playbook.pdf) · [DOCX](./docs/compliance-evidence-playbook.docx) · [HTML](./docs/compliance-evidence-playbook.html) |
| Framework Scope Design Guide | Translating each compliance framework into practical CSW scope patterns, customer workshop questions, and label/tag recommendations | [MD](./docs/framework-scope-design.md) · [PDF](./docs/framework-scope-design.pdf) |
| **SE compliance & cyber-insurance role-play** | A first discovery-conversation rehearsal aid for SEs/SAs and partners — open by asking compliance needs, map pain to CSW, frame in the customer's framework, and answer the cyber-insurance / ransomware supplemental control questions honestly (what CSW covers vs. what to pair) | [MD](./docs/se-compliance-cyber-insurance-roleplay.md) · [PDF](./docs/se-compliance-cyber-insurance-roleplay.pdf) · [DOCX](./docs/se-compliance-cyber-insurance-roleplay.docx) · [HTML](./docs/se-compliance-cyber-insurance-roleplay.html) |

## Asset library

**Coverage** highlights what each framework section addresses so the
whole library can be scanned in one view. The **Runbook** column comes
first because the runbook is what proves the mapping is real and not
marketing — it shows the actual configuration steps, sample policies,
and evidence collection. The **Report** column is the customer-facing
narrative built on top of that work. Format links open the asset
directly; pick whichever fits the conversation you're in (see the
[audience and usage guide](./docs/audience-and-usage.md) for when to
reach for the runbook vs. the report).

| Framework | Coverage | Runbook | Report |
|---|---|---|---|
| HIPAA Security Rule | ePHI workload isolation; investigation-supporting telemetry; BAA technical boundary evidence | [MD](./HIPAA/CSW-HIPAA-Technical-Runbook.md) · [PDF](./HIPAA/CSW-HIPAA-Technical-Runbook.pdf) · [DOCX](./HIPAA/CSW-HIPAA-Technical-Runbook.docx) · [HTML](./HIPAA/CSW-HIPAA-Technical-Runbook.html) | [PDF](./HIPAA/CSW-HIPAA-Compliance-Report.pdf) · [DOCX](./HIPAA/CSW-HIPAA-Compliance-Report.docx) · [HTML](./HIPAA/CSW-HIPAA-Compliance-Report.html) |
| SOC 2 Type II | Continuous CC6.x evidence (vs point-in-time samples); CC7 incident artefacts; customer due-diligence proofs | [MD](./SOC2/CSW-SOC2-Technical-Runbook.md) · [PDF](./SOC2/CSW-SOC2-Technical-Runbook.pdf) · [DOCX](./SOC2/CSW-SOC2-Technical-Runbook.docx) · [HTML](./SOC2/CSW-SOC2-Technical-Runbook.html) | [PDF](./SOC2/CSW-SOC2-Compliance-Report.pdf) · [DOCX](./SOC2/CSW-SOC2-Compliance-Report.docx) · [HTML](./SOC2/CSW-SOC2-Compliance-Report.html) |
| PCI DSS v4.0 | CDE segmentation simulation→enforce; Req 1/11 evidence inputs to validate with your QSA; CVE + EPSS + reachability prioritisation | [MD](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md) · [PDF](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.pdf) · [DOCX](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.docx) · [HTML](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.html) | [PDF](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.pdf) · [DOCX](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.docx) · [HTML](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.html) |
| NIST SP 800-53 Rev 5 | AC-4 information-flow enforcement; CA-7 continuous monitoring; CM-2/3/8 baseline + change tracking | [MD](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md) · [PDF](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.pdf) · [DOCX](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.docx) · [HTML](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.html) | [PDF](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.pdf) · [DOCX](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.docx) · [HTML](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.html) |
| ISO/IEC 27001:2022 | A.8.20–A.8.22 network segregation; A.5.19–A.5.22 supplier egress reconciliation; A.8.16 monitoring evidence | [MD](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md) · [PDF](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.pdf) · [DOCX](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.docx) · [HTML](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.html) | [PDF](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.pdf) · [DOCX](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.docx) · [HTML](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.html) |
| CISA Zero Trust Maturity Model | Networks pillar Initial→Advanced path; Applications & Workloads policy enforcement; observable maturity progression | [MD](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.md) · [PDF](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.pdf) · [DOCX](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.docx) · [HTML](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.html) | [PDF](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.pdf) · [DOCX](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.docx) · [HTML](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.html) |
| FIPS 140 | Plaintext-protocol DENY enforcement; programme-level FIPS posture (cryptographic modules out of scope); 140-2→140-3 transition visibility | [MD](./FIPS-140/CSW-FIPS-Technical-Runbook.md) · [PDF](./FIPS-140/CSW-FIPS-Technical-Runbook.pdf) · [DOCX](./FIPS-140/CSW-FIPS-Technical-Runbook.docx) · [HTML](./FIPS-140/CSW-FIPS-Technical-Runbook.html) | [PDF](./FIPS-140/CSW-FIPS-Compliance-Report.pdf) · [DOCX](./FIPS-140/CSW-FIPS-Compliance-Report.docx) · [HTML](./FIPS-140/CSW-FIPS-Compliance-Report.html) |
| NIST SP 800-207 (ZTA Seven Tenets) | Workload-side evidence for Tenets 2/3/5/6; ZTA architecture mapping; workload-level enforcement as one possible PEP placement | [MD](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) · [PDF](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.pdf) · [DOCX](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.docx) · [HTML](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.html) | [PDF](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.pdf) · [DOCX](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.docx) · [HTML](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.html) |
| NIST SP 800-207A (PDP/PEP/PA/PIP, draft-derived) | CSW Defend as PDP/PEP; telemetry as PIP; logical-component traceability for cloud-native ZTA | [MD](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md) · [PDF](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.pdf) · [DOCX](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.docx) · [HTML](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.html) | [PDF](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.pdf) · [DOCX](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.docx) · [HTML](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.html) |
| DORA (EU 2022/2554) | Art. 8/9 segmentation + inventory; Art. 19 incident dossier templates; Art. 28 third-party egress reconciliation | [MD](./DORA/CSW-DORA-Technical-Runbook.md) · [PDF](./DORA/CSW-DORA-Technical-Runbook.pdf) · [DOCX](./DORA/CSW-DORA-Technical-Runbook.docx) · [HTML](./DORA/CSW-DORA-Technical-Runbook.html) | [PDF](./DORA/CSW-DORA-Compliance-Report.pdf) · [DOCX](./DORA/CSW-DORA-Compliance-Report.docx) · [HTML](./DORA/CSW-DORA-Compliance-Report.html) |
| NIS2 (EU 2022/2555) | Art. 21(2)(a–j) risk-management mapping; Art. 23 24 h / 72 h / 1-month dossier; Art. 21(2)(d) supply-chain egress | [MD](./NIS2/CSW-NIS2-Technical-Runbook.md) · [PDF](./NIS2/CSW-NIS2-Technical-Runbook.pdf) · [DOCX](./NIS2/CSW-NIS2-Technical-Runbook.docx) · [HTML](./NIS2/CSW-NIS2-Technical-Runbook.html) | [PDF](./NIS2/CSW-NIS2-Compliance-Report.pdf) · [DOCX](./NIS2/CSW-NIS2-Compliance-Report.docx) · [HTML](./NIS2/CSW-NIS2-Compliance-Report.html) |
| NERC CIP (Bulk Electric System) | IT-side ESP boundary hardening (CIP-005 R1); IRA evidence (CIP-005 R2); CIP-007/010 ports + baseline + VA evidence; CIP-013 vendor-egress reconciliation. *IT-side scope; OT device layer out of scope.* | [MD](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md) · [PDF](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.pdf) · [DOCX](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.docx) · [HTML](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.html) | [PDF](./NERC-CIP/CSW-NERC-CIP-Compliance-Report.pdf) · [DOCX](./NERC-CIP/CSW-NERC-CIP-Compliance-Report.docx) · [HTML](./NERC-CIP/CSW-NERC-CIP-Compliance-Report.html) |
| TSA Pipeline Security Directive | IT-side IT/OT segmentation (Section III.A); access control + monitoring (III.B/III.C); unpatched-system risk reduction (III.D); CIRP + CAP evidence packs. *IT-side scope; OT device layer out of scope.* | [MD](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md) · [PDF](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.pdf) · [DOCX](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.docx) · [HTML](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.html) | [PDF](./TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report.pdf) · [DOCX](./TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report.docx) · [HTML](./TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report.html) |
| CIS Critical Security Controls v8.1 | Direct on Controls 1, 2, 4, 7, 8, 13 (asset & software inventory, secure config, vuln mgmt, audit logs, network monitoring); IG2 lead with IG1/IG3 deltas called out | [MD](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md) · [PDF](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.pdf) · [DOCX](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.docx) · [HTML](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.html) | [PDF](./CIS-Controls-v8/CSW-CIS-Compliance-Report.pdf) · [DOCX](./CIS-Controls-v8/CSW-CIS-Compliance-Report.docx) · [HTML](./CIS-Controls-v8/CSW-CIS-Compliance-Report.html) |
| NIST Cybersecurity Framework 2.0 | Govern (GV.OV/GV.SC) evidence pack; direct coverage of ID.AM, ID.RA, PR.IR, PR.PS, DE.CM, DE.AE, RS.AN, RS.MI Subcategories | [MD](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md) · [PDF](./NIST-CSF-2/CSW-CSF-Technical-Runbook.pdf) · [DOCX](./NIST-CSF-2/CSW-CSF-Technical-Runbook.docx) · [HTML](./NIST-CSF-2/CSW-CSF-Technical-Runbook.html) | [PDF](./NIST-CSF-2/CSW-CSF-Compliance-Report.pdf) · [DOCX](./NIST-CSF-2/CSW-CSF-Compliance-Report.docx) · [HTML](./NIST-CSF-2/CSW-CSF-Compliance-Report.html) |
| CMMC 2.0 (DoD / DIB) | Level 2 lead (110 controls = NIST 800-171 Rev 2): direct on AC, AU, CM, RA, SC, SI families; CUI-scope labelling pattern; L1 (FCI) and L3 (800-172) deltas | [MD](./CMMC-2/CSW-CMMC-Technical-Runbook.md) · [PDF](./CMMC-2/CSW-CMMC-Technical-Runbook.pdf) · [DOCX](./CMMC-2/CSW-CMMC-Technical-Runbook.docx) · [HTML](./CMMC-2/CSW-CMMC-Technical-Runbook.html) | [PDF](./CMMC-2/CSW-CMMC-Compliance-Report.pdf) · [DOCX](./CMMC-2/CSW-CMMC-Compliance-Report.docx) · [HTML](./CMMC-2/CSW-CMMC-Compliance-Report.html) |
| IEC 62443 (IACS) | Zones & conduits segmentation; IT-side OT boundary hardening; SR control evidence; pair with Cyber Vision/Claroty for OT device layer | [MD](./IEC-62443/CSW-IEC62443-Technical-Runbook.md) · [PDF](./IEC-62443/CSW-IEC62443-Technical-Runbook.pdf) · [DOCX](./IEC-62443/CSW-IEC62443-Technical-Runbook.docx) · [HTML](./IEC-62443/CSW-IEC62443-Technical-Runbook.html) | [PDF](./IEC-62443/CSW-IEC62443-Compliance-Report.pdf) · [DOCX](./IEC-62443/CSW-IEC62443-Compliance-Report.docx) · [HTML](./IEC-62443/CSW-IEC62443-Compliance-Report.html) |
| GDPR (EU 2016/679) | Art. 32 security-of-processing evidence; data-flow mapping for Art. 30 RoPA; breach timeline for Art. 33/34; processor egress for Art. 28 | [MD](./GDPR/CSW-GDPR-Technical-Runbook.md) · [PDF](./GDPR/CSW-GDPR-Technical-Runbook.pdf) · [DOCX](./GDPR/CSW-GDPR-Technical-Runbook.docx) · [HTML](./GDPR/CSW-GDPR-Technical-Runbook.html) | [PDF](./GDPR/CSW-GDPR-Compliance-Report.pdf) · [DOCX](./GDPR/CSW-GDPR-Compliance-Report.docx) · [HTML](./GDPR/CSW-GDPR-Compliance-Report.html) |
| MITRE ATT&CK (Enterprise) | Tactic-by-tactic detection/prevention mapping (TA0001–TA0011, TA0040); technique-level forensic rule alignment; SOC integration guidance | [MD](./MITRE-ATTACK/CSW-MITRE-ATTACK-Technical-Runbook.md) · [PDF](./MITRE-ATTACK/CSW-MITRE-ATTACK-Technical-Runbook.pdf) · [DOCX](./MITRE-ATTACK/CSW-MITRE-ATTACK-Technical-Runbook.docx) · [HTML](./MITRE-ATTACK/CSW-MITRE-ATTACK-Technical-Runbook.html) | [PDF](./MITRE-ATTACK/CSW-MITRE-ATTACK-Compliance-Report.pdf) · [DOCX](./MITRE-ATTACK/CSW-MITRE-ATTACK-Compliance-Report.docx) · [HTML](./MITRE-ATTACK/CSW-MITRE-ATTACK-Compliance-Report.html) |
| FedRAMP (Moderate) | Moderate baseline overlay on NIST 800-53; ConMon evidence; POA&M inputs; 3PAO assessment preparation; AC-4/SC-7/CA-7/SI-4 FedRAMP parameters | [MD](./FedRAMP/CSW-FedRAMP-Technical-Runbook.md) · [PDF](./FedRAMP/CSW-FedRAMP-Technical-Runbook.pdf) · [DOCX](./FedRAMP/CSW-FedRAMP-Technical-Runbook.docx) · [HTML](./FedRAMP/CSW-FedRAMP-Technical-Runbook.html) | [PDF](./FedRAMP/CSW-FedRAMP-Compliance-Report.pdf) · [DOCX](./FedRAMP/CSW-FedRAMP-Compliance-Report.docx) · [HTML](./FedRAMP/CSW-FedRAMP-Compliance-Report.html) |
| SWIFT CSCF (v2024) | SWIFT secure zone isolation; mandatory/advisory control mapping; operator session integrity; Internet access restriction; SWIFT-specific logging | [MD](./SWIFT-CSCF/CSW-SWIFT-CSCF-Technical-Runbook.md) · [PDF](./SWIFT-CSCF/CSW-SWIFT-CSCF-Technical-Runbook.pdf) · [DOCX](./SWIFT-CSCF/CSW-SWIFT-CSCF-Technical-Runbook.docx) · [HTML](./SWIFT-CSCF/CSW-SWIFT-CSCF-Technical-Runbook.html) | [PDF](./SWIFT-CSCF/CSW-SWIFT-CSCF-Compliance-Report.pdf) · [DOCX](./SWIFT-CSCF/CSW-SWIFT-CSCF-Compliance-Report.docx) · [HTML](./SWIFT-CSCF/CSW-SWIFT-CSCF-Compliance-Report.html) |
| HITRUST CSF (v11) | Harmonized control mapping (HIPAA+ISO+NIST+PCI); e1/i1/r2 assessment level guidance; network segregation; vulnerability management; incident evidence | [MD](./HITRUST-CSF/CSW-HITRUST-Technical-Runbook.md) · [PDF](./HITRUST-CSF/CSW-HITRUST-Technical-Runbook.pdf) · [DOCX](./HITRUST-CSF/CSW-HITRUST-Technical-Runbook.docx) · [HTML](./HITRUST-CSF/CSW-HITRUST-Technical-Runbook.html) | [PDF](./HITRUST-CSF/CSW-HITRUST-Compliance-Report.pdf) · [DOCX](./HITRUST-CSF/CSW-HITRUST-Compliance-Report.docx) · [HTML](./HITRUST-CSF/CSW-HITRUST-Compliance-Report.html) |
| NIST SP 800-171 Rev. 3 | CUI enclave isolation; 03.01/03.13 flow enforcement; Rev 3 family alignment with 800-53; CMMC L2 underpinning evidence | [MD](./NIST-800-171/CSW-NIST-800-171-Technical-Runbook.md) · [PDF](./NIST-800-171/CSW-NIST-800-171-Technical-Runbook.pdf) · [DOCX](./NIST-800-171/CSW-NIST-800-171-Technical-Runbook.docx) · [HTML](./NIST-800-171/CSW-NIST-800-171-Technical-Runbook.html) | [PDF](./NIST-800-171/CSW-NIST-800-171-Compliance-Report.pdf) · [DOCX](./NIST-800-171/CSW-NIST-800-171-Compliance-Report.docx) · [HTML](./NIST-800-171/CSW-NIST-800-171-Compliance-Report.html) |
| CSA CCM v4 | Cloud workload segmentation; IVS-09 network security; DSP data isolation; TVM reachability; STAR certification evidence support | [MD](./CSA-CCM/CSW-CSA-CCM-Technical-Runbook.md) · [PDF](./CSA-CCM/CSW-CSA-CCM-Technical-Runbook.pdf) · [DOCX](./CSA-CCM/CSW-CSA-CCM-Technical-Runbook.docx) · [HTML](./CSA-CCM/CSW-CSA-CCM-Technical-Runbook.html) | [PDF](./CSA-CCM/CSW-CSA-CCM-Compliance-Report.pdf) · [DOCX](./CSA-CCM/CSW-CSA-CCM-Compliance-Report.docx) · [HTML](./CSA-CCM/CSW-CSA-CCM-Compliance-Report.html) |
| COBIT 2019 | DSS05.02 network security; APO13 managed security; MEA01/02 conformance monitoring; BAI06/10 change and configuration evidence | [MD](./COBIT-2019/CSW-COBIT-Technical-Runbook.md) · [PDF](./COBIT-2019/CSW-COBIT-Technical-Runbook.pdf) · [DOCX](./COBIT-2019/CSW-COBIT-Technical-Runbook.docx) · [HTML](./COBIT-2019/CSW-COBIT-Technical-Runbook.html) | [PDF](./COBIT-2019/CSW-COBIT-Compliance-Report.pdf) · [DOCX](./COBIT-2019/CSW-COBIT-Compliance-Report.docx) · [HTML](./COBIT-2019/CSW-COBIT-Compliance-Report.html) |
| Australian Essential Eight | ML1–ML3 maturity evidence; E2/E6 patch prioritisation via CVE+EPSS; E5 admin privilege path restriction; E1 application control support | [MD](./AU-Essential-Eight/CSW-Essential-Eight-Technical-Runbook.md) · [PDF](./AU-Essential-Eight/CSW-Essential-Eight-Technical-Runbook.pdf) · [DOCX](./AU-Essential-Eight/CSW-Essential-Eight-Technical-Runbook.docx) · [HTML](./AU-Essential-Eight/CSW-Essential-Eight-Technical-Runbook.html) | [PDF](./AU-Essential-Eight/CSW-Essential-Eight-Compliance-Report.pdf) · [DOCX](./AU-Essential-Eight/CSW-Essential-Eight-Compliance-Report.docx) · [HTML](./AU-Essential-Eight/CSW-Essential-Eight-Compliance-Report.html) |
| UK Cyber Essentials Plus | CE1 workload-level firewall; CE2 secure configuration baseline; CE5 patch management evidence; Plus technical verification support | [MD](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Technical-Runbook.md) · [PDF](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Technical-Runbook.pdf) · [DOCX](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Technical-Runbook.docx) · [HTML](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Technical-Runbook.html) | [PDF](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Compliance-Report.pdf) · [DOCX](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Compliance-Report.docx) · [HTML](./UK-Cyber-Essentials/CSW-Cyber-Essentials-Compliance-Report.html) |
| HIPAA 2025 NPRM | Mandatory network segmentation (§164.312(a)(2)(vi)); technology asset inventory; 24-month log retention architecture; 72-hour breach timeline; annual assessment evidence | [MD](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Technical-Runbook.md) · [PDF](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Technical-Runbook.pdf) · [DOCX](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Technical-Runbook.docx) · [HTML](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Technical-Runbook.html) | [PDF](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Compliance-Report.pdf) · [DOCX](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Compliance-Report.docx) · [HTML](./HIPAA-2025-NPRM/CSW-HIPAA-NPRM-Compliance-Report.html) |
| MAS TRM | Singapore financial-sector technology risk evidence; critical-system segmentation; outsourcing / third-party egress; incident investigation support | [MD](./MAS-TRM/CSW-MAS-TRM-Technical-Runbook.md) · [PDF](./MAS-TRM/CSW-MAS-TRM-Technical-Runbook.pdf) · [DOCX](./MAS-TRM/CSW-MAS-TRM-Technical-Runbook.docx) · [HTML](./MAS-TRM/CSW-MAS-TRM-Technical-Runbook.html) | [PDF](./MAS-TRM/CSW-MAS-TRM-Compliance-Report.pdf) · [DOCX](./MAS-TRM/CSW-MAS-TRM-Compliance-Report.docx) · [HTML](./MAS-TRM/CSW-MAS-TRM-Compliance-Report.html) |
| APRA CPS 234 | Australian prudential information security; critical information assets; control testing; service-provider dependency visibility | [MD](./APRA-CPS-234/CSW-APRA-CPS234-Technical-Runbook.md) · [PDF](./APRA-CPS-234/CSW-APRA-CPS234-Technical-Runbook.pdf) · [DOCX](./APRA-CPS-234/CSW-APRA-CPS234-Technical-Runbook.docx) · [HTML](./APRA-CPS-234/CSW-APRA-CPS234-Technical-Runbook.html) | [PDF](./APRA-CPS-234/CSW-APRA-CPS234-Compliance-Report.pdf) · [DOCX](./APRA-CPS-234/CSW-APRA-CPS234-Compliance-Report.docx) · [HTML](./APRA-CPS-234/CSW-APRA-CPS234-Compliance-Report.html) |
| NY DFS 23 NYCRR Part 500 | Covered-system workload visibility; NPI application scope; vulnerability context; third-party service-provider egress; incident support | [MD](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Technical-Runbook.md) · [PDF](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Technical-Runbook.pdf) · [DOCX](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Technical-Runbook.docx) · [HTML](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Technical-Runbook.html) | [PDF](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Compliance-Report.pdf) · [DOCX](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Compliance-Report.docx) · [HTML](./NY-DFS-23-NYCRR-500/CSW-NYDFS-Compliance-Report.html) |
| TISAX / VDA ISA | Automotive prototype and confidential engineering workload segmentation; supplier/customer egress; assessment evidence support | [MD](./TISAX/CSW-TISAX-Technical-Runbook.md) · [PDF](./TISAX/CSW-TISAX-Technical-Runbook.pdf) · [DOCX](./TISAX/CSW-TISAX-Technical-Runbook.docx) · [HTML](./TISAX/CSW-TISAX-Technical-Runbook.html) | [PDF](./TISAX/CSW-TISAX-Compliance-Report.pdf) · [DOCX](./TISAX/CSW-TISAX-Compliance-Report.docx) · [HTML](./TISAX/CSW-TISAX-Compliance-Report.html) |
| NIST SP 800-82 | OT-adjacent IT segmentation; jump hosts, historians, patch repositories, identity services, vendor access; pair with OT visibility | [MD](./NIST-800-82/CSW-NIST-800-82-Technical-Runbook.md) · [PDF](./NIST-800-82/CSW-NIST-800-82-Technical-Runbook.pdf) · [DOCX](./NIST-800-82/CSW-NIST-800-82-Technical-Runbook.docx) · [HTML](./NIST-800-82/CSW-NIST-800-82-Technical-Runbook.html) | [PDF](./NIST-800-82/CSW-NIST-800-82-Compliance-Report.pdf) · [DOCX](./NIST-800-82/CSW-NIST-800-82-Compliance-Report.docx) · [HTML](./NIST-800-82/CSW-NIST-800-82-Compliance-Report.html) |
| BSI C5 | Cloud service assurance; tenant/shared-service workload boundaries; cloud communication security; vulnerability and incident evidence | [MD](./BSI-C5/CSW-BSI-C5-Technical-Runbook.md) · [PDF](./BSI-C5/CSW-BSI-C5-Technical-Runbook.pdf) · [DOCX](./BSI-C5/CSW-BSI-C5-Technical-Runbook.docx) · [HTML](./BSI-C5/CSW-BSI-C5-Technical-Runbook.html) | [PDF](./BSI-C5/CSW-BSI-C5-Compliance-Report.pdf) · [DOCX](./BSI-C5/CSW-BSI-C5-Compliance-Report.docx) · [HTML](./BSI-C5/CSW-BSI-C5-Compliance-Report.html) |

> **Quickly find a control?** See [`INDEX.md`](./INDEX.md) for a
> control-ID-keyed index across all thirty-four frameworks (e.g. *PCI Req
> 1.2*, *HIPAA §164.312(a)(1)*, *DORA Art. 9*, *NIS2 Art. 21(2)(d)*,
> *NIST AC-4*, *NERC CIP-005 R1*, *TSA SD Section III.A*, *IEC 62443 SR 5.3*,
> *GDPR Art. 32*, *FedRAMP AC-4*, *SWIFT CSCF 1.4*, *HITRUST 01.m*, *MITRE TA0008*,
> *CIS Safeguard 13.4*, *CSF PR.IR-01*, *CMMC AC.L2-3.1.1*, *NIST 800-171 03.13.06*,
> *CSA IVS-09*, *COBIT DSS05.02*, *E8 E5*, *UK CE1*, *HIPAA NPRM §164.312(a)(2)(vi)*,
> *MAS TRM*, *APRA CPS 234*, *NY DFS 500.03*, *TISAX ISA*, *NIST 800-82*, *BSI C5*).

> **Cross-cutting frameworks scope note (CIS, CSF, CMMC).** These three
> frameworks are *cross-mapping* / certification frameworks that
> intentionally overlap with the underlying NIST families already in
> this library. CIS Controls v8.1 is a prioritised subset of NIST
> 800-53; CSF 2.0 is an outcomes wrapper that cites 800-53 (and others)
> as Informative References; CMMC 2.0 Level 2 *is* NIST 800-171, which
> is itself a tailored subset of 800-53. Read the standalone runbook
> when you need the framework-native narrative (assessor language,
> IG/Level/Profile structure, format evidence comes in);
> cross-reference the [800-53](./NIST-800-53/) and
> [800-207](./NIST-800-207/) runbooks for the deeper control rationale.
> All three are **draft v1** and require SME review before being relied
> upon in a formal compliance engagement (CMMC L2 specifically requires
> a C3PAO assessment regardless).

> **Sector frameworks scope note (NERC CIP, TSA Pipeline).** Both
> frameworks are sector overlays whose substantive controls overlap
> heavily with the NIST families already in this library. The CSW
> mapping is on the **IT side** of the IT/OT boundary — EACMS, jump
> hosts, vendor-access servers, engineering workstations, historians,
> identity/PKI, and the corporate IT systems that touch BES Cyber
> System Information or pipeline Critical Cyber Systems. CSW does
> **not** enforce on PLCs/RTUs/IEDs/HMIs and is not certified as an
> Electronic Access Point (NERC) or as an OT-protocol DPI tool; pair
> with your boundary firewall and your OT-aware monitoring stack
> (Cisco Cyber Vision, Claroty, Nozomi, Dragos) for end-to-end
> coverage. Both runbooks and reports are **draft v1** and require SME
> review before being relied upon in a formal compliance engagement.

## Read next

- **[Compliance evidence playbook](./docs/compliance-evidence-playbook.md)** —
  **start here if you are new to CSW** — universal 4-phase evidence programme,
  console map, quarterly export pack, and CSW effectiveness vs. manual audits.
- **[Background — What is Cisco Secure Workload?](./docs/about-csw.md)** —
  one-page intro to the platform, its agent + connector model, and the
  ML capabilities relevant to this repository.
- **[Why these mappings matter](./docs/why-these-mappings-matter.md)** —
  five conversation-starter questions to ask about your own environment,
  plus the case for evaluating CSW alongside what you already run.
- **[Framework Scope Design Guide](./docs/framework-scope-design.md)** —
  customer workshop aid for translating framework obligations into CSW
  scopes, labels, and evidence boundaries.
- **[SE compliance & cyber-insurance role-play](./docs/se-compliance-cyber-insurance-roleplay.md)** —
  a discovery-conversation rehearsal aid: open by asking compliance needs,
  map pain to CSW, frame it in the customer's framework, and answer the
  cyber-insurance / ransomware supplemental honestly (what CSW covers vs.
  what to pair).
- **[Audience and usage guide](./docs/audience-and-usage.md)** — who
  should lead with which document, runbook-vs-report guidance, file
  format guidance, and the full folder layout.
- **[`INDEX.md`](./INDEX.md)** — control-ID lookup across all thirty-four
  frameworks.
- **[CSW Epic EHR Microsegmentation Guide](https://github.com/chandrapati/CSW-Epic-Microsegmentation-Guide)** —
  step-by-step practitioner runbook for Epic tier scopes, ADM, Interconnect/HL7
  policy, enforcement, and HIPAA quarterly evidence — pairs directly with the
  HIPAA and HITRUST runbooks in this repo.

Once GitHub Pages is enabled, the same content is also browseable at
`https://chandrapati.github.io/CSW-Compliance-Mapping/` (landing page
[`index.html`](./index.html)).

## Licensing

This repository ships with Cisco's standard terms in
[`LICENSE`](./LICENSE) at the repo root — read before redistributing,
forking commercially, or building derivative artefacts outside your
organisation.

## Disclaimer

The compliance mappings in this repository are derived from public
standards and regulatory framework documents (HIPAA, SOC 2, PCI DSS,
NIST SP 800-series, ISO/IEC 27001, CISA ZTMM, FIPS 140, EU DORA,
EU NIS2, NERC CIP, TSA Pipeline Security Directives, CIS Critical
Security Controls v8.1, NIST Cybersecurity Framework 2.0, CMMC 2.0,
IEC 62443, GDPR, MITRE ATT&CK, FedRAMP, SWIFT CSCF, HITRUST CSF,
NIST SP 800-171 Rev. 3, CSA Cloud Controls Matrix v4, COBIT 2019,
ACSC Essential Eight, UK Cyber Essentials Plus, the HIPAA Security
Rule 2025 Notice of Proposed Rulemaking (NPRM), MAS Technology Risk
Management Guidelines, APRA CPS 234, NY DFS 23 NYCRR Part 500, TISAX /
VDA ISA, NIST SP 800-82, and BSI C5
cross-referenced against documented Cisco Secure Workload (CSW)
product capabilities at the time of authoring.

The **HIPAA 2025 NPRM** technical mapping interprets a **proposed**
Security Rule update and must be reconciled against **final** regulatory
text before formal reliance; continue parallel compliance with the
**current** Security Rule until amendments are effective.

The **NERC CIP** and **TSA Pipeline** mappings are explicitly scoped
to the **IT side of the IT/OT boundary** and are issued as **draft
v1**. Treat them as sector overlays on the underlying NIST family
rather than as standalone audit references.

The **CIS Controls v8.1**, **NIST CSF 2.0**, and **CMMC 2.0**
mappings are issued as **draft v1** and are *cross-mapping*
frameworks that intentionally overlap with the underlying NIST
families already in this library. CMMC Level 2 assessment is
performed by a Certified Third-Party Assessor Organisation (C3PAO);
nothing in this repository substitutes for the System Security Plan
(SSP), Plan of Action & Milestones (POA&M), or the C3PAO engagement.

All mappings require subject-matter-expert review for both
regulatory / framework accuracy and current Cisco product capability
before being relied upon in a formal compliance engagement.

These materials are provided for **informational and reference purposes
only**. They do not constitute legal, regulatory, or audit advice, are
not warranted to be complete, current, or fit for any specific
compliance program, and should not be relied upon as a substitute for
review by your own qualified compliance, legal, and audit professionals.

Standards evolve, product capabilities change, and the applicability of
any specific control depends on each organization's environment,
deployment, and risk posture. Always validate against the latest
official source documents before formal use.

**Guidelines.** The capability bullets in
[Background — What is Cisco Secure Workload?](./docs/about-csw.md)
describe how teams commonly use Cisco Secure Workload. They are not a
completeness check for your estate — apply professional judgment, align
with your assessors, and tailor to how you run operations.

For questions, scoping discussions, or to validate how these mappings
apply to your environment, please contact your **Cisco account team**.

---

## Step-by-Step Guides

Hands-on integration and deployment guides — follow these top to bottom to build out a deployment:

| Guide | Description | Best for |
|-------|-------------|---------|
| [Agent Installation](https://github.com/chandrapati/CSW-Agent-Installation-Guide) | Deploy CSW agents on Linux / Windows / cloud | Day-1 sensor deployment |
| [Policy Lifecycle](https://github.com/chandrapati/CSW-Policy-Lifecycle) | Policy discovery → enforcement workflow | Policy management |
| [ISE / pxGrid](https://github.com/chandrapati/csw-ise-integration) | ISE/pxGrid: user-identity–aware microsegmentation | Identity & Zero Trust |
| [AnyConnect NVM](https://github.com/chandrapati/csw-anyconnect-nvm) | Endpoint process flows + user identity via NVM | Endpoint telemetry |
| [ServiceNow CMDB](https://github.com/chandrapati/csw-servicenow-integration) | ServiceNow CMDB label enrichment for workload scopes | CMDB-driven policy |
| [Infoblox](https://github.com/chandrapati/csw-infoblox-integration) | Infoblox IPAM/DNS extensible-attribute label enrichment | IPAM/DNS-driven policy |
| [F5 BIG-IP](https://github.com/chandrapati/csw-f5-integration) | F5 virtual-server labels, policy enforcement, IPFIX flow visibility | Load balancer segmentation |
| [AWS Connector](https://github.com/chandrapati/csw-aws-connector) | EC2 tag ingestion + VPC flow logs + Security Group enforcement | AWS workloads |
| [Azure Connector](https://github.com/chandrapati/csw-azure-connector) | Azure VM tag ingestion + VNet flow logs + NSG enforcement | Azure workloads |
| [GCP Connector](https://github.com/chandrapati/csw-gcp-connector) | GCE label ingestion + VPC flow logs + firewall enforcement | GCP workloads |
| [NetFlow](https://github.com/chandrapati/csw-netflow-integration) | NetFlow v9/IPFIX agentless flow ingestion from switches | Network fabric visibility |
| [ERSPAN](https://github.com/chandrapati/csw-erspan-integration) | Agentless packet mirroring for legacy / OT / IoT devices | Deep agentless visibility |
| [Secure Firewall](https://github.com/chandrapati/CSW-Secure-Firewall-Integration-Guide) | NSEL flow ingestion from Cisco Secure Firewall (FTD/ASA) | Firewall flow visibility |
| [Splunk Integration](https://github.com/chandrapati/csw-splunk-integration) | CSW syslog alerts → Splunk SIEM | SecOps / SIEM teams |

## Resources

Learning paths, reference material, and day-2 tooling:

| Resource | Description | Best for |
|----------|-------------|---------|
| [User Education](https://github.com/chandrapati/CSW-User-Education) | Onboarding guides, concept explainers, and curated video library | New CSW users |
| [Compliance Mapping](https://github.com/chandrapati/CSW-Compliance-Mapping) | Map CSW controls to NIST, PCI-DSS, HIPAA, CIS | Compliance & audit |
| [Tenant Insights](https://github.com/chandrapati/CSW-Tenant-Insights) | Tenant-level reporting and analytics | Visibility metrics |
| [Operations Toolkit](https://github.com/chandrapati/CSW-Operations-Toolkit) | Day-2 ops scripts: health checks, reporting, policy analysis | Ongoing operations |

> **Suggested customer journey:**
> User Education → Agent Installation → Policy Lifecycle → ISE/pxGrid → ServiceNow CMDB → Infoblox → F5 BIG-IP → Splunk Integration → Compliance Mapping → Operations Toolkit
