# Cisco Secure Workload — Compliance Mapping Assets

Customer-facing reports and SA/SE technical runbooks mapping Cisco Secure
Workload (CSW) controls to common compliance frameworks. Created by the
CSW Incubation Team.

## Asset Library

| Framework | PDF Report | DOCX Report | Technical Runbook |
|---|---|---|---|
| HIPAA Security Rule | [pdf](./HIPAA/CSW-HIPAA-Compliance-Report.pdf) | [docx](./HIPAA/CSW-HIPAA-Compliance-Report.docx) | [runbook](./HIPAA/CSW-HIPAA-Technical-Runbook.md) |
| SOC 2 Type II | [pdf](./SOC2/CSW-SOC2-Compliance-Report.pdf) | [docx](./SOC2/CSW-SOC2-Compliance-Report.docx) | [runbook](./SOC2/soc2-runbook.md) |
| PCI DSS v4.0 | [pdf](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.pdf) | [docx](./PCI-DSS-v4/CSW-PCI-DSS-Compliance-Report.docx) | [runbook](./PCI-DSS-v4/pci-runbook.md) |
| NIST SP 800-53 Rev 5 | [pdf](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.pdf) | [docx](./NIST-800-53/CSW-NIST-800-53-Compliance-Report.docx) | [runbook](./NIST-800-53/nist-runbook.md) |
| ISO/IEC 27001:2022 | [pdf](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.pdf) | [docx](./ISO-27001-2022/CSW-ISO27001-Compliance-Report.docx) | [runbook](./ISO-27001-2022/iso27001-runbook.md) |
| CISA Zero Trust Maturity Model | [pdf](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.pdf) | [docx](./CISA-ZeroTrust/CSW-CISA-ZTMM-Compliance-Report.docx) | [runbook](./CISA-ZeroTrust/cisa-ztmm-runbook.md) |
| FIPS 140 | [pdf](./FIPS-140/CSW-FIPS-Compliance-Report.pdf) | [docx](./FIPS-140/CSW-FIPS-Compliance-Report.docx) | [runbook](./FIPS-140/fips-runbook.md) |
| NIST SP 800-207 (ZTA Seven Tenets) | [pdf](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.pdf) | [docx](./NIST-800-207/CSW-NIST-800-207-Compliance-Report.docx) | [runbook](./NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) |
| NIST SP 800-207A (PDP/PEP/PA/PIP) | [pdf](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.pdf) | [docx](./NIST-800-207A/CSW-NIST-800-207A-Compliance-Report.docx) | [runbook](./NIST-800-207A/CSW-NIST-800-207A-Technical-Runbook.md) |
| DORA (EU 2022/2554) | [pdf](./DORA/CSW-DORA-Compliance-Report.pdf) | [docx](./DORA/CSW-DORA-Compliance-Report.docx) | [runbook](./DORA/CSW-DORA-Technical-Runbook.md) |
| NIS2 (EU 2022/2555) | [pdf](./NIS2/CSW-NIS2-Compliance-Report.pdf) | [docx](./NIS2/CSW-NIS2-Compliance-Report.docx) | [runbook](./NIS2/CSW-NIS2-Technical-Runbook.md) |

> **Quickly find a control?** See [`INDEX.md`](./INDEX.md) for a
> control-ID-keyed index across all eleven frameworks (e.g. *PCI Req
> 1.2*, *HIPAA §164.312(a)(1)*, *DORA Art. 9*, *NIS2 Art. 21(2)(d)*,
> *NIST AC-4*).

## How to Use

### Why these mappings exist

Compliance frameworks were written by humans trying to describe what
"good security" looks like for a class of risk. They are *outcomes*, not
products. The hardest question a customer faces is not *"what does the
standard require?"* — it's *"can I actually prove the control is in place,
on every workload, every day, in evidence an auditor will accept?"*

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
environment and notice that each one shows up in a compliance standard
**and** in nearly every major incident retrospective of the last five
years. They are the same questions, asked twice, by two very different
people.

- **Can you enumerate, right now, every process on every workload that
  talks to your cardholder data environment — and prove the list
  hasn't drifted in the last 30 days?** *(PCI DSS Req 1.2, 11.5)* Your
  QSA asks a version of this once a year. An attacker who has just
  landed an initial foothold asks a far more dangerous version every
  minute: *what else can I reach from here?* If the answer to the
  auditor takes a week of spreadsheet work to assemble, the answer to
  the attacker is *"everything you want."*

- **When a CVE drops on a library inside one of your containers, how
  long until you know which production workloads are exposed and which
  paths attackers could traverse to reach them?** *(NIST RA-5, CM-7,
  ISO A.8.8)* Your vulnerability scanner tells you *who is
  vulnerable*. It does not tell you *who is reachable from the
  internet*, *who can pivot to your crown jewels*, or *who would still
  be reachable if you isolated workload A*. That second question is
  what decides whether a CVE is a Tuesday-morning patch or a board
  call at 2 a.m.

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
  800-207A PDP/PEP)* For most organisations the honest answer is
  *"the PDP is a wiki page and the PEP is a firewall rule from 2021."*
  Zero trust isn't a slide; it's the question of which component, on
  which packet, makes which decision — and you should be able to
  point at it.

- **Could you withstand a lateral-movement-based ransomware event
  without network re-architecture, or only with it?** *(CISA ZTMM
  "Optimal" tier)* This is the question your CFO will ask the morning
  after the next high-profile incident in your industry. The honest
  answer for most organisations today is *"only with it"* — meaning,
  the controls that would have constrained the blast radius are the
  same controls that have been deferred as a six-month project for the
  last three years. The peers who can answer *"without it"* did not
  deploy magic; they deployed workload-resident segmentation before
  they needed it.

#### Notice the pattern

Each of those questions appears in a compliance framework *because*
the framework's authors knew it was the question that decides whether
a foothold becomes an incident, or an incident becomes a breach.
**Compliance is the lagging indicator; blast radius is the leading
one.** And micro-segmentation at the workload — every process, every
flow, every package — is one of the very few controls where the
artefact you hand the auditor is the same artefact that bounds your
worst day. A QSA inspects it once a year; an attacker tests it the
moment they land. Both should get the same answer.

That reframes what micro-segmentation is *for*. It is not a
compliance project that happens to limit blast radius as a side
effect — it is a blast-radius control that happens to satisfy the
compliance requirement at the same time. PCI Req 1, HIPAA §164.312,
NIST AC-4, ISO A.8.22, DORA Art. 9, NIS2 Art. 21(2)(j) — they all
exist because the regulator already knows that an unsegmented
workload is one phishing email away from front-page news. Treating
micro-segmentation purely as a checkbox is a fairly expensive way to
miss the point of why the checkbox is there.

CSW is built to give defensible answers to both readers continuously
— the auditor *and* the incident commander — because it operates at
the workload itself rather than inferring posture from network
telemetry or periodic scans. The frameworks below describe what
"good" looks like on paper. The runbooks show you how to get to a
state where your segmentation, your audit evidence, and your incident
response are all the same artefact — instead of three different
programmes doing 30% of each other's work.

### Audience guide

| Audience | Lead with | Key takeaway |
|---|---|---|
| **CISO / Security leadership** | The PDF report's executive summary and the *Compliance Posture Summary* table | CSW collapses several manual evidence-gathering programs (segmentation reviews, change attestation, drift tracking) into continuous, query-able state. |
| **Security architect** | The full PDF report's control-by-control mapping | Where each control is satisfied (agent telemetry, policy enforcement, conversation graph, forensic flows) and what gaps remain to be designed around. |
| **Compliance / GRC team** | The *Audit Evidence* and *Gap Analysis* sections in the PDF | Which CSW reports, exports, and dashboards are auditor-ready as-is, and what supplementary attestation language to use. |
| **Operations / SRE / DevSecOps** | The Markdown technical runbook | Concrete configuration steps, policy patterns, and "what to show the auditor on day 1" playbooks. |
| **You already have firewalls and EDR** | The runbooks and the 800-207 / 207A reports | Workload-resident telemetry and identity-based segmentation answer evidence questions that perimeter and endpoint tools structurally can't — process-to-process flows, intra-host conversations, drift over time. The frameworks below show you exactly which controls land in that gap. |

### How to get the most out of this repo

Whether you found this from a search for a specific control, were
pointed here by your Cisco account team, or are doing a broader
evaluation, here's a way to navigate the material that respects your
time:

1. **Open the framework that's actually on your roadmap.** The one tied
   to a current audit, a customer contractual ask, or board-level
   pressure. Read only that PDF first — every report stands on its own,
   and skimming all nine will dilute the signal.
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

- **It operates where the workload lives.** Not at the perimeter, not on
  the endpoint console — on every server, VM, and container, watching
  every process and every flow. Many compliance evidence questions
  ("prove this process never talks to that one") are *only* answerable
  with telemetry at that layer.
- **Segmentation that survives change.** Most environments have
  segmentation controls that were correct on the day they were designed
  and have drifted ever since. CSW's policy model is computed from
  observed application behavior and continuously verified, which is
  what auditors increasingly want to see (PCI DSS v4.0's "in place and
  operating effectively" language, NIST CA-7 continuous monitoring).
- **One source of truth across hybrid and multi-cloud.** AWS, Azure,
  GCP, on-prem, bare metal, containers — same agent, same policy
  language, same evidence format. Frameworks like NIST 800-53 and ISO
  27001 don't care where your workload runs; your evidence shouldn't
  either.
- **Forensic depth without a separate tool.** Process-level conversation
  graphs, package inventory, vulnerability exposure, and historical flow
  records are all in one platform — which collapses several manual
  evidence-gathering programs (segmentation reviews, change attestation,
  drift tracking) into continuous, query-able state.
- **It complements, not replaces, what you have.** CSW is built to live
  alongside firewalls, EDR, SIEM, and CSPM. The frameworks here show
  exactly which evidence questions land in the gap those tools leave —
  not as a replacement argument, but as a "here's what's still missing"
  argument.

If after reading any one framework you can answer *"yes, my current
stack already gives me the artifacts on page X with this much
fidelity, on every workload, every day"* — you may not need CSW for
that control. If the answer is *"I'm not sure"* or *"only with
significant manual effort"* — that's the conversation worth having
with your Cisco account team.

### File formats

- **PDF reports** — Render natively in the GitHub web UI. Use these for
  customer review and audit conversations. Generated from the DOCX
  sources via LibreOffice; treat the DOCX as the editable master and
  re-generate the PDF after any edits.
- **DOCX reports** — Customer-facing editable master. Replace
  `[Customer Name]` and `[Month Year]` placeholders, and tailor the
  Compliance Posture Summary table to the customer's specific scope and
  deployment stage before sharing externally.
- **Markdown runbooks** — Technical reference for SA/SE engineers and
  customer practitioners. Includes deployment playbooks, CSW
  configuration steps, sample policies, and auditor response guidance.

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

For questions, scoping discussions, or to validate how these mappings
apply to your environment, please contact your **Cisco account team**.
