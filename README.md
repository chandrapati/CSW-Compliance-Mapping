# Cisco Secure Workload — Compliance Mapping Assets

Customer-facing reports and matching technical runbooks that map Cisco
Secure Workload (CSW) controls to **sixteen** compliance, sector, and
zero-trust frameworks. Every framework folder ships the same set of
assets: a Markdown technical runbook (the engineering view), a DOCX
report (the editable customer master), a PDF render of that report,
and HTML versions of both for browser/mobile reading.

> **New here?** Read [Background — What is Cisco Secure Workload?](./docs/about-csw.md)
> for a one-page intro to the platform itself, then come back to pick a
> framework.

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
data, and policy-as-code enforcement — and explain how that capability
produces auditor-grade evidence.

The same workload-resident evidence that satisfies an auditor also
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
| HIPAA Security Rule | ePHI workload isolation; OCR-investigation audit trail; BAA technical boundary evidence | [MD](./HIPAA/CSW-HIPAA-Technical-Runbook.md) · [HTML](./HIPAA/CSW-HIPAA-Technical-Runbook.html) | [PDF](./HIPAA/CSW-HIPAA-Compliance-Report.pdf) · [DOCX](./HIPAA/CSW-HIPAA-Compliance-Report.docx) · [HTML](./HIPAA/CSW-HIPAA-Compliance-Report.html) |
| SOC 2 Type II | Continuous CC6.x evidence (vs point-in-time samples); CC7 incident artefacts; customer due-diligence proofs | [MD](./SOC2/CSW-SOC2-Technical-Runbook.md) · [HTML](./SOC2/CSW-SOC2-Technical-Runbook.html) | [PDF](./SOC2/CSW-SOC2-Compliance-Report.pdf) · [DOCX](./SOC2/CSW-SOC2-Compliance-Report.docx) · [HTML](./SOC2/CSW-SOC2-Compliance-Report.html) |
| PCI DSS v4.0 | CDE segmentation simulation→enforce; QSA-ready Req 1/11 evidence; CVE + EPSS + reachability prioritisation | [MD](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md) · [HTML](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.html) | [PDF](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.pdf) · [DOCX](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.docx) · [HTML](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.html) |
| NIST SP 800-53 Rev 5 | AC-4 information-flow enforcement; CA-7 continuous monitoring; CM-2/3/8 baseline + change tracking | [MD](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md) · [HTML](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.html) | [PDF](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.pdf) · [DOCX](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.docx) · [HTML](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.html) |
| ISO/IEC 27001:2022 | A.8.20–A.8.22 network segregation; A.5.19–A.5.22 supplier egress reconciliation; A.8.16 monitoring evidence | [MD](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md) · [HTML](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.html) | [PDF](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.pdf) · [DOCX](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.docx) · [HTML](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.html) |
| CISA Zero Trust Maturity Model | Networks pillar Initial→Advanced path; Applications & Workloads policy enforcement; observable maturity progression | [MD](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.md) · [HTML](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.html) | [PDF](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.pdf) · [DOCX](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.docx) · [HTML](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.html) |
| FIPS 140 | Plaintext-protocol DENY enforcement; programme-level FIPS posture (cryptographic modules out of scope); 140-2→140-3 transition visibility | [MD](./FIPS-140/CSW-FIPS-Technical-Runbook.md) · [HTML](./FIPS-140/CSW-FIPS-Technical-Runbook.html) | [PDF](./FIPS-140/CSW-FIPS-Compliance-Report.pdf) · [DOCX](./FIPS-140/CSW-FIPS-Compliance-Report.docx) · [HTML](./FIPS-140/CSW-FIPS-Compliance-Report.html) |
| NIST SP 800-207 (ZTA Seven Tenets) | Workload-side evidence for Tenets 2/3/5/6; ZTA architecture mapping; clear PEP placement at the workload | [MD](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) · [HTML](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.html) | [PDF](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.pdf) · [DOCX](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.docx) · [HTML](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.html) |
| NIST SP 800-207A (PDP/PEP/PA/PIP, draft-derived) | CSW Defend as PDP/PEP; telemetry as PIP; logical-component traceability for cloud-native ZTA | [MD](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md) · [HTML](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.html) | [PDF](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.pdf) · [DOCX](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.docx) · [HTML](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.html) |
| DORA (EU 2022/2554) | Art. 8/9 segmentation + inventory; Art. 19 incident dossier templates; Art. 28 third-party egress reconciliation | [MD](./DORA/CSW-DORA-Technical-Runbook.md) · [HTML](./DORA/CSW-DORA-Technical-Runbook.html) | [PDF](./DORA/CSW-DORA-Compliance-Report.pdf) · [DOCX](./DORA/CSW-DORA-Compliance-Report.docx) · [HTML](./DORA/CSW-DORA-Compliance-Report.html) |
| NIS2 (EU 2022/2555) | Art. 21(2)(a–j) risk-management mapping; Art. 23 24 h / 72 h / 1-month dossier; Art. 21(2)(d) supply-chain egress | [MD](./NIS2/CSW-NIS2-Technical-Runbook.md) · [HTML](./NIS2/CSW-NIS2-Technical-Runbook.html) | [PDF](./NIS2/CSW-NIS2-Compliance-Report.pdf) · [DOCX](./NIS2/CSW-NIS2-Compliance-Report.docx) · [HTML](./NIS2/CSW-NIS2-Compliance-Report.html) |
| NERC CIP (Bulk Electric System) | IT-side ESP boundary hardening (CIP-005 R1); IRA evidence (CIP-005 R2); CIP-007/010 ports + baseline + VA evidence; CIP-013 vendor-egress reconciliation. *IT-side scope; OT device layer out of scope.* | [MD](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.md) · [HTML](./NERC-CIP/CSW-NERC-CIP-Technical-Runbook.html) | [PDF](./NERC-CIP/CSW-NERC-CIP-Compliance-Report.pdf) · [DOCX](./NERC-CIP/CSW-NERC-CIP-Compliance-Report.docx) · [HTML](./NERC-CIP/CSW-NERC-CIP-Compliance-Report.html) |
| TSA Pipeline Security Directive | IT-side IT/OT segmentation (Section III.A); access control + monitoring (III.B/III.C); unpatched-system risk reduction (III.D); CIRP + CAP evidence packs. *IT-side scope; OT device layer out of scope.* | [MD](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md) · [HTML](./TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.html) | [PDF](./TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report.pdf) · [DOCX](./TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report.docx) · [HTML](./TSA-Pipeline/CSW-TSA-Pipeline-Compliance-Report.html) |
| CIS Critical Security Controls v8.1 | Direct on Controls 1, 2, 4, 7, 8, 13 (asset & software inventory, secure config, vuln mgmt, audit logs, network monitoring); IG2 lead with IG1/IG3 deltas called out | [MD](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.md) · [HTML](./CIS-Controls-v8/CSW-CIS-Technical-Runbook.html) | [PDF](./CIS-Controls-v8/CSW-CIS-Compliance-Report.pdf) · [DOCX](./CIS-Controls-v8/CSW-CIS-Compliance-Report.docx) · [HTML](./CIS-Controls-v8/CSW-CIS-Compliance-Report.html) |
| NIST Cybersecurity Framework 2.0 | Govern (GV.OV/GV.SC) evidence pack; direct coverage of ID.AM, ID.RA, PR.IR, PR.PS, DE.CM, DE.AE, RS.AN, RS.MI Subcategories | [MD](./NIST-CSF-2/CSW-CSF-Technical-Runbook.md) · [HTML](./NIST-CSF-2/CSW-CSF-Technical-Runbook.html) | [PDF](./NIST-CSF-2/CSW-CSF-Compliance-Report.pdf) · [DOCX](./NIST-CSF-2/CSW-CSF-Compliance-Report.docx) · [HTML](./NIST-CSF-2/CSW-CSF-Compliance-Report.html) |
| CMMC 2.0 (DoD / DIB) | Level 2 lead (110 controls = NIST 800-171 Rev 2): direct on AC, AU, CM, RA, SC, SI families; CUI-scope labelling pattern; L1 (FCI) and L3 (800-172) deltas | [MD](./CMMC-2/CSW-CMMC-Technical-Runbook.md) · [HTML](./CMMC-2/CSW-CMMC-Technical-Runbook.html) | [PDF](./CMMC-2/CSW-CMMC-Compliance-Report.pdf) · [DOCX](./CMMC-2/CSW-CMMC-Compliance-Report.docx) · [HTML](./CMMC-2/CSW-CMMC-Compliance-Report.html) |

> **Quickly find a control?** See [`INDEX.md`](./INDEX.md) for a
> control-ID-keyed index across all sixteen frameworks (e.g. *PCI Req
> 1.2*, *HIPAA §164.312(a)(1)*, *DORA Art. 9*, *NIS2 Art. 21(2)(d)*,
> *NIST AC-4*, *NERC CIP-005 R1*, *TSA SD Section III.A*, *CIS
> Safeguard 13.4*, *CSF PR.IR-01*, *CMMC AC.L2-3.1.1*).

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

- **[Background — What is Cisco Secure Workload?](./docs/about-csw.md)** —
  one-page intro to the platform, its agent + connector model, and the
  ML capabilities relevant to this repository.
- **[Why these mappings matter](./docs/why-these-mappings-matter.md)** —
  five conversation-starter questions to ask about your own environment,
  plus the case for evaluating CSW alongside what you already run.
- **[Audience and usage guide](./docs/audience-and-usage.md)** — who
  should lead with which document, runbook-vs-report guidance, file
  format guidance, and the full folder layout.
- **[`INDEX.md`](./INDEX.md)** — control-ID lookup across all sixteen
  frameworks.

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
Security Controls v8.1, NIST Cybersecurity Framework 2.0, and CMMC
2.0) cross-referenced against documented Cisco Secure Workload (CSW)
product capabilities at the time of authoring.

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
