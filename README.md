# Cisco Secure Workload — Compliance Mapping Assets

## What is Cisco Secure Workload?

Cisco Secure Workload (CSW) is a workload-protection and micro-
segmentation platform that runs *on* your servers, virtual machines
and containers — wherever they live. A lightweight agent on each
workload, paired with agentless connectors for AWS, Azure, GCP and
Kubernetes, gives you four things continuously and from one place:

- **A complete, current inventory** across hosts and workloads—observed
  processes and packages where the platform surfaces them—and the network
  conversations those workloads participate in across on‑prem and
  supported cloud footprints. Best practice is to reconcile this view with
  your authoritative CMDB or cloud asset records.
- **An application dependency map** built from observed behaviour, not
  guessed from a network diagram, so you can see exactly which
  workloads talk to which, on which ports, with which processes.
- **Workload-level micro-segmentation** that enforces deny-by-default
  policy at the workload itself — close to the resource, identity-
  aware, and consistent across cloud providers.
- **Vulnerability and behavioural awareness** — CVE/exposure posture,
  behavioural signals, and drift versus baselines, with export paths into
  your SIEM and incident-response workflows designed the way your
  programme prefers.

**CSW makes extensive use of machine learning** alongside classical
signals (rules, baselines, graph edges you can inspect). Exactly which
models and features ship in a given release are documented in official
product materials and release notes — treat this repository as mapping
those capabilities to frameworks, **not** as the authoritative ML
architecture spec. Below is the *intent* practitioners care about:

- **Application discovery (ADM).** Observed processes and flows are
  grouped to propose application/service boundaries and *starting-point*
  policy candidates for human review — not carte-blanche automation that
  bypasses governance. Outputs should be iterated and gated like any
  other security change programme.
- **Behavioural detection.** Baselines over process execution and graph
  structure can highlight unusual workloads, workload-to-workload edges,
  and drift in conversational patterns; expect tuning to reduce noisy
  detections as with any behavioural product.
- **Vulnerability prioritisation.** Risk rankings can combine CVE
  metadata, exploit intelligence, topology/reachability context, and
  business metadata to focus remediation — they **prioritise** work;
  human validation still matters for irreversible containment decisions.

In practical terms, CSW collapses several things organisations
typically run as separate programmes — segmentation reviews, change
attestation, drift tracking, application-flow documentation,
vulnerability prioritisation, lateral-movement detection — into a
single, query-able, evidence-producing system. Because discovery and
detection reconcile against live workload behaviour rather than relying
purely on static diagrams, evidence can stay materially aligned with how
applications actually run — supporting both *audit-style questions*
(what changed, what's allowed?) and *incident-response questions* (what
was talking to what, across which process?) far more cleanly than periodic
reviews alone usually achieve.

This repository explains, framework-by-framework, exactly which
auditor questions and which incident-response questions that data
answers — and what artefact you'd hand over in each case.

## About this repository

Customer-facing reports and matching technical runbooks mapping
Cisco Secure Workload controls to eleven common compliance and
zero-trust frameworks. Each framework folder contains the same three
assets: a PDF report (for executive review), a DOCX report (the
editable master), and a Markdown technical runbook (concrete
configuration steps and the auditor-response playbook). A single
`INDEX.md` at the root lets you jump straight from any control ID
into the runbook section that addresses it.

**Licensing.** This repository ships with Cisco's standard terms in
[`LICENSE`](./LICENSE) at the repo root — read before redistributing,
forking commercially, or building derivative artefacts outside your
organisation.

## Asset Library

| Framework | Report (PDF) | Report (DOCX) | Report (HTML) | Runbook (Markdown) | Runbook (HTML) |
|---|---|---|---|---|---|
| HIPAA Security Rule | [pdf](./HIPAA/CSW-HIPAA-Compliance-Report.pdf) | [docx](./HIPAA/CSW-HIPAA-Compliance-Report.docx) | [html](./HIPAA/CSW-HIPAA-Compliance-Report.html) | [md](./HIPAA/CSW-HIPAA-Technical-Runbook.md) | [html](./HIPAA/CSW-HIPAA-Technical-Runbook.html) |
| SOC 2 Type II | [pdf](./SOC2/CSW-SOC2-Compliance-Report.pdf) | [docx](./SOC2/CSW-SOC2-Compliance-Report.docx) | [html](./SOC2/CSW-SOC2-Compliance-Report.html) | [md](./SOC2/CSW-SOC2-Technical-Runbook.md) | [html](./SOC2/CSW-SOC2-Technical-Runbook.html) |
| PCI DSS v4.0 | [pdf](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.pdf) | [docx](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.docx) | [html](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.html) | [md](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.md) | [html](./PCI-DSS-v4/CSW-PCI-DSS-Technical-Runbook.html) |
| NIST SP 800-53 Rev 5 | [pdf](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.pdf) | [docx](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.docx) | [html](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.html) | [md](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.md) | [html](./NIST-800-53/CSW-NIST-800-53-Technical-Runbook.html) |
| ISO/IEC 27001:2022 | [pdf](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.pdf) | [docx](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.docx) | [html](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.html) | [md](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.md) | [html](./ISO-27001-2022/CSW-ISO27001-Technical-Runbook.html) |
| CISA Zero Trust Maturity Model | [pdf](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.pdf) | [docx](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.docx) | [html](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.html) | [md](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.md) | [html](./CISA-ZeroTrust/CSW-CISA-ZTMM-Technical-Runbook.html) |
| FIPS 140 | [pdf](./FIPS-140/CSW-FIPS-Compliance-Report.pdf) | [docx](./FIPS-140/CSW-FIPS-Compliance-Report.docx) | [html](./FIPS-140/CSW-FIPS-Compliance-Report.html) | [md](./FIPS-140/CSW-FIPS-Technical-Runbook.md) | [html](./FIPS-140/CSW-FIPS-Technical-Runbook.html) |
| NIST SP 800-207 (ZTA Seven Tenets) | [pdf](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.pdf) | [docx](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.docx) | [html](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.html) | [md](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) | [html](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.html) |
| NIST SP 800-207A (PDP/PEP/PA/PIP, draft-derived) | [pdf](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.pdf) | [docx](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.docx) | [html](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.html) | [md](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md) | [html](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.html) |
| DORA (EU 2022/2554) | [pdf](./DORA/CSW-DORA-Compliance-Report.pdf) | [docx](./DORA/CSW-DORA-Compliance-Report.docx) | [html](./DORA/CSW-DORA-Compliance-Report.html) | [md](./DORA/CSW-DORA-Technical-Runbook.md) | [html](./DORA/CSW-DORA-Technical-Runbook.html) |
| NIS2 (EU 2022/2555) | [pdf](./NIS2/CSW-NIS2-Compliance-Report.pdf) | [docx](./NIS2/CSW-NIS2-Compliance-Report.docx) | [html](./NIS2/CSW-NIS2-Compliance-Report.html) | [md](./NIS2/CSW-NIS2-Technical-Runbook.md) | [html](./NIS2/CSW-NIS2-Technical-Runbook.html) |

The **HTML** column links host a browseable, mobile-friendly version of every
report and runbook. Once GitHub Pages is enabled for this repository, those
same files are also available at `https://chandrapati.github.io/CSW-Compliance-Mapping/`
(start at [`index.html`](./index.html) for a landing page).

> **Quickly find a control?** See [`INDEX.md`](./INDEX.md) for a
> control-ID-keyed index across all eleven frameworks (e.g. *PCI Req
> 1.2*, *HIPAA §164.312(a)(1)*, *DORA Art. 9*, *NIS2 Art. 21(2)(d)*,
> *NIST AC-4*).

## How to Use

### Why these mappings exist

Compliance frameworks were written by humans trying to describe what
"good security" looks like for a class of risk. They are *outcomes*, not
products. The hardest question a customer faces is not *"what does the
standard require?"* — it's *"for the workloads I actually defend, can I
actually prove — with evidence that survives scrutiny — that the control
still holds tomorrow, not just on audit day?"*

These mappings exist to close that gap. For each framework, they trace
specific controls (e.g. PCI DSS Req 1.2.1, HIPAA §164.312(a)(1), NIST AC-4)
to concrete Cisco Secure Workload (CSW) capabilities — micro-segmentation,
process-level telemetry, software inventory, vulnerability awareness,
forensic flow data, and policy-as-code enforcement — and explain how that
capability produces auditor-grade evidence.

### Use them to start a different conversation — with yourself

Compliance frameworks were originally written to capture lessons from
real breaches. Over time the conversation around them has narrowed to
checkbox status — *do you have a firewall, do you have an EDR, do you
have a SIEM* — and the connection back to actual loss prevention has
gotten thinner. Walk through the questions below about *your own*
environment and compare how each lands in compliance language versus
during an incident retrospective — organisations that triage breaches
almost always converge on segmentation, lateral movement, patching
priorities, visibility gaps, or drift across "what's supposed to happen"
versus "what's actually happening." They are overlapping views of similar
underlying risk.

- **Can you enumerate, right now—at the fidelity your monitoring stack
  actually provides—every process talking to your cardholder data
  environment, and reason about how that picture changed over roughly the
  last 30 days without a rebuild-the-world project?** *(PCI DSS Req 1.2,
  11.5)* Your QSA asks something in this neighbourhood once per assessment
  cycle.
  Immediately after credential theft or initial foothold, defenders ask a
  related question repeatedly: *what new paths opened from this pivot?*
  If assembling the authoritative answer reliably takes heroic effort,
  defenders are improvising faster than attackers during the decisive
  early hours.

- **When a CVE drops on a library inside one of your containers, how
  long until you know which production workloads are exposed and which
  paths attackers could traverse to reach them?** *(NIST RA-5, CM-7,
  ISO A.8.8)* Many vulnerability scanners and programmes answer *whether
  a CVE exists on an asset*. They often omit or under-weight the richer
  question CSW specialises in: given how this workload actually converses —
  ingress, egress and lateral paths — what's the practical blast radius?
  Separate tools partially answer pieces of this; assembling a coherent,
  repeatable picture organisation-wide commonly remains brittle without
  workload-resident conversational context.

- **If an auditor asks you to demonstrate least-privilege between two
  applications, what artefact do you hand them?** *(SOC 2 CC6.1,
  800-53 AC-3)* Now ask exactly the same question with different
  words: *if app A is compromised, what stops it from talking to app
  B?* — and notice the answer should be the same artefact. If your
  "least privilege" lives in a network-design document and not in
  something the workload actually enforces, then you have least-
  privilege as a policy, not as a property of your environment.

- **Your zero-trust architecture diagram shows a Policy Decision Point
  and a Policy Enforcement Point — where do they actually live in
  your stack today, and what data feeds them?** *(NIST 800-207 §3.2,
  800-207A PDP/PEP)* If you paused right now — without opening a wiki —
  where does an allow vs deny verdict *actually get applied* for lateral
  workload‑to‑workload flows you care most about defending, which engine
  emitted it last, what attributes did it ingest, and can you replay a
  decision historically? Architectural diagrams clarify intent; answering
  those factual questions cleanly for production traffic is harder for
  many organisations than decks suggest.

- **If a lateral-movement or ransomware tabletop asked *"how fast can we
  change who can talk to whom"* — would the answer be *continuous,
  policy-driven reachability* tied to live workload behaviour, or mainly
  *project-driven network redesigns*?** *(CISA ZTMM treats "Optimal"
  maturity as an aspiration; use it that way, not as a guarantee.)* Not
  every incident involves ransomware, yet exercises still surface the same
  axis: does blast-radius containment ride on everyday operations, or wait
  for the next big architectural push?

#### Notice the pattern

Each of those questions appears in a compliance framework *because*
the framework's authors knew it was the question that decides whether
a foothold becomes an incident, or an incident becomes a breach.
**Compliance is commonly the lagging indicator; blast‑radius containment
often becomes the unavoidable leading indicator when something breaks
badly.** At the workload layer—particularly where CSW enforces segmentation
policy—audit-oriented exports often overlap substantially with artefacts
incident responders reconstruct under pressure. Assessors revisit periodically; attackers probe reachable paths
far more impatiently — both perspectives stress‑test whether policy is real
property or aspiration.

That reframes what micro-segmentation is *for*. It is not a
compliance project that happens to limit blast radius as a side
effect — it is a blast-radius control that happens to satisfy the
compliance requirement at the same time. PCI Req 1, HIPAA §164.312,
NIST AC-4, ISO A.8.22, DORA Art. 9, NIS2 Art. 21(2)(j) — these controls are
where standards writers captured the idea that *unbounded lateral
reachability routinely turns small footholds into existential incidents.*
They are not cynical checkboxes; they encode failure modes people keep
living through. Treating segmentation only as audit busywork forfeits
blast‑radius containment while still paying for the programme.

CSW is designed to sharpen those answers wherever workload-resident
telemetry and enforcement overlap your scope — acknowledging that tooling
never replaces disciplined architecture, identity and access management,
patching, backups, and mature SOC processes.

### Audience guide

| Audience | Lead with | Key takeaway |
|---|---|---|
| **CISO / Security leadership** | The PDF report's executive summary and the *Compliance Posture Summary* table | CSW collapses several manual evidence-gathering programs (segmentation reviews, change attestation, drift tracking) into continuous, query-able state. |
| **Security architect** | The full PDF report's control-by-control mapping | Where each control is satisfied (agent telemetry, policy enforcement, conversation graph, forensic flows) and what gaps remain to be designed around. |
| **Compliance / GRC team** | The *Audit Evidence* and *Gap Analysis* sections in the PDF | Which CSW reports, exports, and dashboards are auditor-ready as-is, and what supplementary attestation language to use. |
| **Operations / SRE / DevSecOps** | The Markdown technical runbook | Concrete configuration steps, policy patterns, and "what to show the auditor on day 1" playbooks. |
| **You already have firewalls and EDR** | The runbooks and the 800-207 / 207A reports | Workload-resident telemetry and identity-aware segmentation address many evidence questions about *process-to-process* and *intra-host East–West* flows that perimeter and endpoint controls usually see only partially. The frameworks below spell out which obligations sit in that gap — and which still require other tools. |

### How to get the most out of this repo

Whether you found this from a search for a specific control, were
pointed here by your Cisco account team, or are doing a broader
evaluation, here's a way to navigate the material that respects your
time:

1. **Open the framework that's actually on your roadmap.** The one tied
   to a current audit, a customer contractual ask, or board-level
   pressure. Read only that PDF first — every report stands on its own,
   and skimming all eleven will dilute the signal.
2. **Read the executive summary, then jump to the *Compliance Posture
   Summary* table.** It tells you in one page which control families
   CSW addresses fully, which it addresses partially, and where you'll
   need complementary controls. If the table doesn't match your
   environment, you've already learned something useful — talk to your
   account team about scope.
3. **Then look at the matching technical runbook (`*-runbook.md` or
   `*-Technical-Runbook.md` in the same folder).** It shows the *how*:
   sensor deployment phases, policy patterns, evidence collection
   cadence, and what an auditor will actually accept as proof. If the
   runbook's level of detail looks plausible for your environment,
   that's the strongest signal that the mapping is real and not
   marketing.
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

### Why look at CSW at all?

Be honest about the question. There are many security tools competing
for attention; the case for evaluating CSW specifically rests on a few
things these mappings demonstrate concretely:

- **It operates where the workload lives.** Not solely at the perimeter or
  through an endpoint-console-only lens—the agent observes applications,
  processes, and flows directly on servers, VMs, and supported container
  hosts, alongside optional cloud inventory through authorised
  connectors. Many East–West and process-context questions land more
  naturally here **as part of** a layered control stack, alongside your
  existing tools—use judgment about where CSW fits.
- **Segmentation anchored in observed behaviour.** Teams often freeze
  diagrams long before production traffic changes. Where CSW's policy
  workflow is anchored in observed conversational reality (with appropriate
  human approvals), auditors increasingly see artefacts that resemble the
  *in place and operating effectively* framing in PCI DSS v4 and the intent
  of NIST CA-7-style continuous diagnostics — contingent on disciplined
  change management behind the knobs.
- **Hybrid / multi‑cloud cohesion.** Organisations operating across AWS,
  Azure, GCP, on‑prem, and containers often value a single segmentation
  and evidence vocabulary—CSW supports that posture where you standardise
  on it **as a deliberate programme choice**.
- **Operational leverage — not another silo.** Process‑level conversational
  graphs (where enabled), vulnerability posture, enriched flow history, and
  export paths into telemetry platforms can converge on fewer bespoke
  evidence pulls — freeing humans for judgement calls instead of
  archaeology.
- **It complements, not replaces, what you have.** CSW is built to live
  alongside firewalls, EDR, SIEM, and CSPM. The frameworks here show
  exactly which evidence questions land in the gap those tools leave —
  not as a replacement argument, but as a "here's what's still missing"
  argument.

If after reading any one framework you can answer *"yes, our current
controls already produce artefacts on page X at comparable fidelity
without undue manual effort"* — Cisco Secure Workload may add little beyond
marginal convenience for that obligation. Ambiguity—or heavy glue—to get
answers is generally the pragmatic signal to revisit the conversation with
your Cisco account team rather than accumulating more slideware diagrams.

### File formats

- **PDF reports** — Render natively in the GitHub web UI. Use these for
  customer review and audit conversations. Generated from the DOCX
  sources via LibreOffice; treat the DOCX as the editable master and
  re-generate the PDF after any edits.
- **DOCX reports** — Customer-facing editable master. Replace
  `[Customer Name]` and `[Month Year]` placeholders, and tailor the
  Compliance Posture Summary table to the customer's specific scope and
  deployment stage before sharing externally.
- **Markdown runbooks** — Technical reference for the security
  engineers and platform owners doing the work. Includes deployment
  playbooks, CSW configuration steps, sample policies, and the
  auditor-response guidance referenced from the report.

## Folder Structure

```
CSW-Compliance-Mapping/
├── INDEX.md             ← control-ID lookup across all frameworks
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
└── NIS2/                ← EU essential & important entities
```

## Disclaimer

The compliance mappings in this repository are derived from public
standards and regulatory framework documents (HIPAA, SOC 2, PCI DSS,
NIST SP 800-series, ISO/IEC 27001, CISA ZTMM, FIPS 140, EU DORA, and
EU NIS2) cross-referenced against documented Cisco Secure Workload
(CSW) product capabilities at the time of authoring.

These materials are provided for **informational and reference purposes
only**. They do not constitute legal, regulatory, or audit advice, are
not warranted to be complete, current, or fit for any specific
compliance program, and should not be relied upon as a substitute for
review by your own qualified compliance, legal, and audit professionals.

Standards evolve, product capabilities change, and the applicability of
any specific control depends on each organization's environment,
deployment, and risk posture. Always validate against the latest
official source documents before formal use.

**Guidelines.** The capability bullets earlier in **What is Cisco Secure
Workload?** describe how teams commonly use Cisco Secure Workload. They are
not a completeness check for your estate—apply professional judgment,
align with your assessors, and tailor to how you run operations.

For questions, scoping discussions, or to validate how these mappings
apply to your environment, please contact your **Cisco account team**.
