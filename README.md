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

### Use them to start a different conversation

Most compliance conversations focus on checkbox status. Use these
documents to escalate the conversation past "do you have a firewall?"
toward questions that genuinely separate posture from theater:

- *Can you enumerate, right now, every process on every workload that talks
  to your cardholder data environment — and prove the list hasn't drifted
  in the last 30 days?* (PCI DSS 1.2, 11.5)
- *When a CVE drops on a library inside a container, how long until you
  know which production workloads are exposed and which paths attackers
  could traverse to reach them?* (NIST RA-5, CM-7, ISO A.8.8)
- *If an auditor asks you to demonstrate least-privilege between two
  applications, what artifact do you hand them?* (SOC 2 CC6.1, 800-53 AC-3)
- *Your zero-trust architecture diagram shows a Policy Decision Point and
  a Policy Enforcement Point — where do they actually live in your stack
  today, and what data feeds them?* (NIST 800-207 §3.2, 800-207A PDP/PEP)
- *Could you withstand a lateral-movement-based ransomware event without
  network reorchitecture, or only with it?* (CISA ZTMM "Optimal" tier)

CSW is built specifically to give defensible answers to these questions
because it operates at the workload itself — every process, every flow,
every package — rather than inferring posture from network telemetry or
periodic scans. The frameworks are how regulators describe the goal;
CSW is one of the few engines that produces continuous, machine-verifiable
evidence that the goal is being met.

### Audience guide

| Audience | Lead with | Key takeaway |
|---|---|---|
| **CISO / Security leadership** | The PDF report's executive summary and the *Compliance Posture Summary* table | CSW collapses several manual evidence-gathering programs (segmentation reviews, change attestation, drift tracking) into continuous, query-able state. |
| **Security architect** | The full PDF report's control-by-control mapping | Where each control is satisfied (agent telemetry, policy enforcement, conversation graph, forensic flows) and what gaps remain to be designed around. |
| **Compliance / GRC team** | The *Audit Evidence* and *Gap Analysis* sections in the PDF | Which CSW reports, exports, and dashboards are auditor-ready as-is, and what supplementary attestation language to use. |
| **Operations / SRE / DevSecOps** | The Markdown technical runbook | Concrete configuration steps, policy patterns, and "what to show the auditor on day 1" playbooks. |
| **The customer's incumbent firewall / EDR vendor** | The runbooks and the 800-207 / 207A reports | Why workload-resident telemetry and identity-based segmentation are not duplicative of perimeter or endpoint controls — they answer questions those tools structurally cannot. |

### Suggested customer-engagement flow

1. **Start with their highest-pressure framework** (the one tied to a real
   audit or a contractual obligation). Hand them only that PDF.
2. **Walk the executive summary together** to align on what CSW
   demonstrably covers vs. what still requires complementary controls.
   Honesty here builds far more trust than over-claiming.
3. **Pivot to NIST 800-207 / 207A** once compliance language is
   established. This reframes the discussion from *"what do we have to
   do?"* to *"what would a defensible architecture look like?"* — and
   positions CSW as the workload-tier component of a zero-trust design,
   not just a control checkbox.
4. **Finish with a concrete artifact ask**: "Could we run a 30-day
   discovery in your environment and produce the same evidence tables we
   just looked at, populated with your real workloads?" That converts
   abstract mappings into a defensible PoV scope.

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
├── HIPAA/
├── SOC2/
├── PCI-DSS-v4/
├── NIST-800-53/
├── ISO-27001-2022/
├── CISA-ZeroTrust/
├── FIPS-140/
├── NIST-800-207/
└── NIST-800-207A/
```

## Disclaimer

The compliance mappings in this repository are derived from public
standards and regulatory framework documents (HIPAA, SOC 2, PCI DSS,
NIST SP 800-series, ISO/IEC 27001, CISA ZTMM, and FIPS 140) cross-
referenced against documented Cisco Secure Workload (CSW) product
capabilities at the time of authoring.

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
