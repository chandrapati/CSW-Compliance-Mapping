# Audience and usage guide

> Companion to the
> [CSW Compliance Mapping repository](../README.md). Everything in
> this page is about *how to navigate* the assets — who should lead
> with which document, when to pick the runbook vs the report, which
> file format to share, and where to find things in the folder tree.

## Audience guide

| Audience | Lead with | Key takeaway |
|---|---|---|
| **CISO / Security leadership** | The PDF report's executive summary and the *Compliance Posture Summary* table | CSW collapses several manual evidence-gathering programs (segmentation reviews, change attestation, drift tracking) into continuous, query-able state. |
| **Security architect** | The full PDF report's control-by-control mapping | Where each control is satisfied (agent telemetry, policy enforcement, conversation graph, forensic flows) and what gaps remain to be designed around. |
| **Compliance / GRC team** | The *Audit Evidence* and *Gap Analysis* sections in the PDF | Which CSW reports, exports, and dashboards are auditor-ready as-is, and what supplementary attestation language to use. |
| **Operations / SRE / DevSecOps** | The Markdown technical runbook | Concrete configuration steps, policy patterns, and "what to show the auditor on day 1" playbooks. |
| **You already have firewalls and EDR** | The runbooks and the 800-207 / 207A reports | Workload-resident telemetry and identity-aware segmentation address many evidence questions about *process-to-process* and *intra-host East–West* flows that perimeter and endpoint controls usually see only partially. The frameworks below spell out which obligations sit in that gap — and which still require other tools. |

## How to get the most out of this repo

Whether you found this from a search for a specific control, were
pointed here by your Cisco account team, or are doing a broader
evaluation, here's a way to navigate the material that respects your
time:

1. **Open the framework that's actually on your roadmap.** The one tied
   to a current audit, a customer contractual ask, or board-level
   pressure. Skimming all sixteen will dilute the signal — pick one
   and stay with it.
2. **Start with the technical runbook (`*-Technical-Runbook.md` in the
   same folder).** It shows the *how*: sensor deployment phases, policy
   patterns, evidence collection cadence, and what an auditor will
   actually accept as proof. If the runbook's level of detail looks
   plausible for your environment, that's the strongest signal that the
   mapping is real and not marketing — and it's the right place to
   stress-test scope before investing in a wider read.
3. **Then read the matching report.** Open the executive summary in the
   PDF and jump to the *Compliance Posture Summary* table. It tells you
   in one page which control families CSW addresses fully, which it
   addresses partially, and where you'll need complementary controls.
   With the runbook fresh in your head, the report reads as the
   evidence story for work you've already verified is real.
4. **Once you've grounded the conversation in compliance language, read
   the NIST 800-207 and 800-207A reports.** These shift the lens from
   *"what do we have to do?"* to *"what does a defensible zero-trust
   architecture actually look like at the workload tier?"* — useful
   even if zero trust isn't your stated initiative, because the same
   patterns underlie most modern compliance frameworks.
5. **When you're ready, ask your Cisco account team for a discovery
   exercise.** Specifically: a short engagement where CSW is deployed
   in a representative slice of your environment and the same evidence
   tables in these reports are populated with *your real workloads,
   your real flows, your real CVEs*. That converts these documents from
   abstract mappings into something you can actually defend in front of
   your auditors and your board.

## Runbook or report — when to use which

- **Runbook** is the technical foundation everything else rests on. It's
  written for the **security engineers and platform owners actually doing
  the work**: deployment playbooks, CSW configuration steps, sample
  policies, evidence-collection commands, and the auditor-response guidance
  the report cites. If a customer wants to know whether a mapping is real
  or just slideware, the runbook is where they look. Use **Markdown** when
  editing or diff-reviewing in a code editor, **HTML** when reading through
  it in a browser.
- **Report** is the customer-facing narrative built on top of the runbook.
  It's for **leaders, auditors, customers in due diligence, and
  procurement** — explaining how Cisco Secure Workload supports the
  framework, the artefacts produced, and where the boundaries are. Use
  **PDF** for review meetings, **DOCX** when you need to tailor placeholders
  before sharing externally, **HTML** for a link you can drop into
  Slack/email or read on a phone.

## File formats

- **Markdown runbooks** — The technical foundation. Reference for the
  security engineers and platform owners doing the work: deployment
  playbooks, CSW configuration steps, sample policies, and the
  auditor-response guidance the report cites. Markdown for editing or
  diff-reviewing in a code editor; HTML for reading in a browser.
- **DOCX reports** — Customer-facing editable master built on top of the
  runbook. Replace `[Customer Name]` and `[Month Year]` placeholders, and
  tailor the Compliance Posture Summary table to the customer's specific
  scope and deployment stage before sharing externally.
- **PDF reports** — Render of the DOCX for customer review and audit
  conversations; renders natively in the GitHub web UI. Generated from
  the DOCX via LibreOffice; treat the DOCX as the editable master and
  re-generate the PDF after any edits.
- **HTML** — Browseable, mobile-friendly view for both runbooks and
  reports. Once GitHub Pages is enabled, the same HTML is published at
  `https://chandrapati.github.io/CSW-Compliance-Mapping/` (landing page:
  [`index.html`](../index.html)).

## Folder structure

```
CSW-Compliance-Mapping/
├── README.md            ← compliance-mapping focus, asset library, scope notes
├── INDEX.md             ← control-ID lookup across all frameworks
├── docs/                ← background and navigation pages (this folder)
│   ├── about-csw.md     ← what Cisco Secure Workload actually is
│   ├── why-these-mappings-matter.md
│   └── audience-and-usage.md
├── HIPAA/
├── SOC2/
├── PCI-DSS-v4/
├── NIST-800-53/
├── ISO-27001-2022/
├── CISA-ZeroTrust/
├── FIPS-140/
├── NIST-800-207/
├── NIST-800-207A/
├── DORA/                ← EU financial sector
├── NIS2/                ← EU essential & important entities
├── NERC-CIP/            ← North American bulk electric system (IT side)
├── TSA-Pipeline/        ← TSA-designated natural gas / oil pipelines (IT side)
├── CIS-Controls-v8/     ← CIS Critical Security Controls v8.1 (IG2 lead)
├── NIST-CSF-2/          ← NIST Cybersecurity Framework 2.0 (Govern + 5 functions)
└── CMMC-2/              ← CMMC 2.0 (Level 2 lead, with L1 / L3 deltas)
```

Every framework folder follows the same shape: a Markdown technical
runbook, a DOCX (editable master) and PDF (review render) of the
customer-facing report, and HTML versions of both built by
[`.html-tools/build-html.py`](../.html-tools/build-html.py).

---

**See also**

- [Background — What is Cisco Secure Workload?](./about-csw.md)
- [Why these mappings matter](./why-these-mappings-matter.md)
- [Repository README](../README.md) — asset library, scope notes, and
  disclaimer.
