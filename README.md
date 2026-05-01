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

- **PDF reports** — Render natively in the GitHub web UI. Generated from
  the DOCX sources via LibreOffice; treat the DOCX as the editable master
  and re-generate the PDF after any edits.
- **DOCX reports** — Customer-facing editable master. Replace
  `[Customer Name]` and `[Month Year]` placeholders before sharing
  externally.
- **MD runbooks** — Internal SA/SE reference. Includes deployment
  playbooks, CSW configuration steps, and auditor response guidance.

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

## Contact

Created by the CSW Incubation Team. Questions or feedback → reach out via
Webex.

---
*Cisco Confidential — Internal Use. Customer-facing documents require
`[Customer Name]` substitution before external sharing.*
