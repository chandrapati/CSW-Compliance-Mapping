#!/usr/bin/env python3
"""
Generate customer-facing DOCX, HTML, and PDF reports for the framework
runbooks that are Markdown-first in this repository.

The DOCX and HTML outputs use pandoc. The PDF output intentionally uses a small
stdlib-only writer so the repo does not require LaTeX, wkhtmltopdf, or reportlab.
"""

from __future__ import annotations

import html
import re
import subprocess
import tempfile
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / ".html-tools"
CSS = TOOLS / "style.css"


FRAMEWORKS = [
    {
        "folder": "MAS-TRM",
        "title": "Cisco Secure Workload - MAS TRM Compliance Report",
        "stem": "CSW-MAS-TRM-Compliance-Report",
        "standard": "MAS Technology Risk Management Guidelines",
        "audience": "Singapore financial institutions and regulated financial-services providers.",
        "driver": "Critical-system segmentation, technology risk evidence, outsourcing visibility, vulnerability context, and incident support.",
        "scope": "`MAS-TRM` > `Critical-Systems`, `Customer-Data`, `Security-Services`, `Outsourced-Third-Parties`",
        "outcomes": [
            "Inventory and label critical systems and customer-data workloads.",
            "Document approved and observed workload communication paths.",
            "Identify supplier / outsourced service egress for risk review.",
            "Package vulnerability, monitoring, and incident-response evidence.",
        ],
        "evidence": [
            "Critical-system workload inventory",
            "Approved-flow and observed-flow comparison",
            "Third-party egress summary",
            "Vulnerability exposure summary",
            "Incident timeline sample",
        ],
        "boundaries": "CSW does not replace MAS governance, outsourcing due diligence, BCP/DR, IAM, cryptography, or regulatory reporting decisions.",
    },
    {
        "folder": "APRA-CPS-234",
        "title": "Cisco Secure Workload - APRA CPS 234 Compliance Report",
        "stem": "CSW-APRA-CPS234-Compliance-Report",
        "standard": "APRA CPS 234 - Information Security",
        "audience": "Australian banks, insurers, superannuation trustees, and other APRA-regulated entities.",
        "driver": "Critical information asset visibility, control testing, service-provider dependency review, and incident scoping.",
        "scope": "`APRA-CPS234` > `Critical-Information-Assets`, `Material-Operations`, `Service-Providers`, `Incident-Evidence`",
        "outcomes": [
            "Map workloads to critical information assets and material operations.",
            "Use policy simulation and flow review as technical control-testing evidence.",
            "Identify third-party service-provider communication paths.",
            "Support incident scoping with flow and process telemetry.",
        ],
        "evidence": [
            "Critical information asset workload inventory",
            "Control-testing export",
            "Service-provider egress map",
            "Policy candidate and exception register",
            "Incident scoping example",
        ],
        "boundaries": "CSW does not replace APRA notification decisions, formal control ownership, supplier assurance, IAM, EDR, or GRC workflows.",
    },
    {
        "folder": "NY-DFS-23-NYCRR-500",
        "title": "Cisco Secure Workload - NY DFS Part 500 Compliance Report",
        "stem": "CSW-NYDFS-Compliance-Report",
        "standard": "NY DFS 23 NYCRR Part 500",
        "audience": "Covered entities such as banks, insurers, and financial-services organizations regulated by NY DFS.",
        "driver": "Covered-system visibility, nonpublic-information workload protection, monitoring, vulnerability context, and incident support.",
        "scope": "`NYDFS-500` > `Covered-Systems`, `NPI-Applications`, `Critical-Operations`, `Third-Party-Service-Providers`",
        "outcomes": [
            "Identify covered workloads and NPI-bearing applications.",
            "Build least-privilege workload communication policies.",
            "Identify third-party service-provider egress.",
            "Package monitoring, vulnerability, and incident evidence.",
        ],
        "evidence": [
            "Covered workload inventory",
            "NPI application scope map",
            "Observed communication paths",
            "Third-party provider egress summary",
            "Policy candidate and incident timeline sample",
        ],
        "boundaries": "CSW does not replace the CISO function, written policies, MFA/IAM, encryption programs, annual certification, or DFS notification decisions.",
    },
    {
        "folder": "TISAX",
        "title": "Cisco Secure Workload - TISAX Compliance Report",
        "stem": "CSW-TISAX-Compliance-Report",
        "standard": "TISAX / VDA ISA",
        "audience": "Automotive OEMs, suppliers, engineering partners, and providers preparing for TISAX assessment.",
        "driver": "Prototype protection, engineering-system segmentation, customer-confidential workload boundaries, and supplier/customer egress evidence.",
        "scope": "`TISAX` > `Prototype-Protection`, `Engineering-Systems`, `Customer-Confidential`, `Supplier-Customer-Egress`",
        "outcomes": [
            "Map prototype, engineering, and customer-confidential workloads.",
            "Document supplier and customer communication paths.",
            "Identify excessive lateral access or unexpected egress.",
            "Support VDA ISA assessment evidence with workload telemetry.",
        ],
        "evidence": [
            "TISAX scope workload inventory",
            "Supplier/customer egress summary",
            "Flow and process telemetry summary",
            "Vulnerability exposure report",
            "Policy candidate and exception register",
        ],
        "boundaries": "CSW does not replace physical prototype controls, DLP, IAM, supplier contracts, or TISAX assessor judgment.",
    },
    {
        "folder": "NIST-800-82",
        "title": "Cisco Secure Workload - NIST SP 800-82 Compliance Report",
        "stem": "CSW-NIST-800-82-Compliance-Report",
        "standard": "NIST SP 800-82 - Guide to Operational Technology Security",
        "audience": "Security architects, plant IT/OT teams, industrial asset owners, and SOC teams.",
        "driver": "OT-adjacent IT segmentation for jump hosts, historians, patch repositories, identity services, and vendor access.",
        "scope": "`NIST-800-82` > `OT-Facing-IT`, `Industrial-DMZ`, `Jump-Hosts`, `Historians`, `Patch-Repositories`, `Vendor-Access`",
        "outcomes": [
            "Map IT-side workloads that support OT operations.",
            "Constrain jump-host, vendor, historian, and patch-repository paths.",
            "Identify high-risk ports and unexpected IT-to-OT communication.",
            "Separate CSW-covered IT workloads from OT-native visibility requirements.",
        ],
        "evidence": [
            "OT-adjacent workload inventory",
            "Vendor and remote-access flow summary",
            "Jump-host / historian dependency maps",
            "Cannot-instrument register",
            "Policy candidate and rollback notes",
        ],
        "boundaries": "CSW does not inspect PLC/RTU/IED/HMI fieldbus behavior or replace Cyber Vision, Claroty, Nozomi, Dragos, OT firewalls, or plant change control.",
    },
    {
        "folder": "BSI-C5",
        "title": "Cisco Secure Workload - BSI C5 Compliance Report",
        "stem": "CSW-BSI-C5-Compliance-Report",
        "standard": "BSI C5 - Cloud Computing Compliance Criteria Catalogue",
        "audience": "Cloud service providers, SaaS operators, and cloud customers using BSI C5 as a cloud assurance baseline.",
        "driver": "Cloud workload segmentation, tenant/shared-service boundaries, vulnerability handling, monitoring, and incident evidence.",
        "scope": "`BSI-C5` > `Cloud-Service-Scope`, `Production-Service`, `Tenant-Shared-Services`, `Customer-Data-Stores`, `Supplier-Egress`",
        "outcomes": [
            "Map cloud service workloads and shared services.",
            "Document tenant, customer-data, and supplier communication boundaries.",
            "Use workload telemetry for communication security evidence.",
            "Package vulnerability and incident evidence for cloud assurance.",
        ],
        "evidence": [
            "Cloud workload inventory",
            "Scope tree and cloud tag mapping",
            "Tenant/shared-service flow summary",
            "Supplier egress summary",
            "Policy candidate and incident evidence sample",
        ],
        "boundaries": "CSW does not replace BSI C5 attestation, CSP controls, IAM/KMS, backup/DR, portability, or shared-responsibility decisions.",
    },
    {
        "folder": "IEC-62443",
        "title": "Cisco Secure Workload - IEC 62443 Compliance Report",
        "stem": "CSW-IEC62443-Compliance-Report",
        "standard": "IEC 62443 - Industrial Automation and Control Systems Security",
        "audience": "Industrial, manufacturing, energy, utilities, and OT security teams designing zones and conduits.",
        "driver": "Zones and conduits segmentation, IT-side OT boundary hardening, SR control evidence, and complementary OT device visibility.",
        "scope": "`IEC-62443` > `IT-OT-Boundary`, `Industrial-DMZ`, `Jump-Hosts`, `Engineering-Workstations`, `Historians`, `Vendor-Access`",
        "outcomes": [
            "Map IT-side workloads that participate in OT access paths.",
            "Document conduit-like communication between industrial support systems.",
            "Identify unexpected lateral movement paths near the OT boundary.",
            "Package SR-aligned segmentation and monitoring evidence.",
        ],
        "evidence": [
            "Zone and conduit workload inventory",
            "IT/OT boundary flow summary",
            "Jump host and vendor-access dependency map",
            "Policy candidate and exception register",
            "Cannot-instrument OT device layer notes",
        ],
        "boundaries": "CSW does not replace OT-native asset discovery or protocol inspection. Pair it with Cisco Cyber Vision, Claroty, Nozomi, Dragos, OT firewalls, and plant change control for PLC, RTU, IED, and fieldbus layers.",
    },
    {
        "folder": "GDPR",
        "title": "Cisco Secure Workload - GDPR Compliance Report",
        "stem": "CSW-GDPR-Compliance-Report",
        "standard": "General Data Protection Regulation (EU 2016/679)",
        "audience": "Privacy, security, data protection, and application teams responsible for personal-data processing systems.",
        "driver": "Article 32 security-of-processing evidence, Article 30 data-flow support, Article 33/34 breach timeline inputs, and processor egress review.",
        "scope": "`GDPR` > `Personal-Data-Systems`, `Special-Category-Data`, `Processors`, `Breach-Investigation`, `Security-Processing-Evidence`",
        "outcomes": [
            "Identify workloads that process or store personal data.",
            "Support RoPA discussions with observed application data flows.",
            "Review processor and third-country egress paths.",
            "Build incident timelines from workload communication telemetry.",
        ],
        "evidence": [
            "Personal-data workload inventory",
            "Observed data-flow map for application owners",
            "Processor / third-party egress summary",
            "Segmentation policy evidence for Article 32",
            "Incident timeline sample for breach response",
        ],
        "boundaries": "CSW does not determine lawful basis, consent, DPIA conclusions, data-subject rights handling, retention decisions, or legal breach-notification obligations.",
    },
    {
        "folder": "MITRE-ATTACK",
        "title": "Cisco Secure Workload - MITRE ATT&CK Compliance Report",
        "stem": "CSW-MITRE-ATTACK-Compliance-Report",
        "standard": "MITRE ATT&CK Enterprise",
        "audience": "SOC, detection engineering, threat hunting, and security architecture teams.",
        "driver": "Tactic-by-tactic detection and prevention mapping, technique-level forensic alignment, and SOC integration guidance.",
        "scope": "`MITRE-ATTACK` > `Initial-Access`, `Execution`, `Persistence`, `Privilege-Escalation`, `Defense-Evasion`, `Lateral-Movement`, `Command-Control`, `Exfiltration`, `Impact`",
        "outcomes": [
            "Map CSW telemetry and policy controls to ATT&CK tactics and techniques.",
            "Use workload process and flow evidence for forensic rule alignment.",
            "Identify lateral movement and command-and-control opportunities.",
            "Create SOC-ready evidence packages for investigation workflows.",
        ],
        "evidence": [
            "Technique-to-CSW capability matrix",
            "Observed flow and process telemetry examples",
            "Lateral movement candidate paths",
            "Policy deny / allow evidence",
            "SOC enrichment guidance",
        ],
        "boundaries": "ATT&CK is not a compliance standard. CSW does not replace EDR, SIEM, identity telemetry, malware analysis, endpoint response, or full detection engineering coverage.",
    },
    {
        "folder": "FedRAMP",
        "title": "Cisco Secure Workload - FedRAMP Moderate Compliance Report",
        "stem": "CSW-FedRAMP-Compliance-Report",
        "standard": "FedRAMP Moderate Baseline",
        "audience": "Cloud service providers, federal customers, 3PAOs, and security teams preparing FedRAMP evidence.",
        "driver": "Moderate baseline overlay on NIST 800-53, ConMon evidence, POA&M inputs, and AC-4 / SC-7 / CA-7 / SI-4 support.",
        "scope": "`FedRAMP` > `Moderate-Baseline`, `Boundary-Protection`, `Information-Flow-Enforcement`, `Continuous-Monitoring`, `POAM-Evidence`",
        "outcomes": [
            "Support information-flow enforcement and boundary protection evidence.",
            "Provide workload telemetry for continuous monitoring discussions.",
            "Identify segmentation and vulnerability findings that may inform POA&M entries.",
            "Prepare 3PAO review artifacts from observed and approved flow data.",
        ],
        "evidence": [
            "FedRAMP-scoped workload inventory",
            "AC-4 / SC-7 flow evidence package",
            "Continuous monitoring export",
            "Vulnerability and reachability summary",
            "Exception and remediation register",
        ],
        "boundaries": "CSW does not replace FedRAMP authorization, SSP ownership, 3PAO assessment, CSP platform controls, IAM, encryption, audit retention, or agency ATO decisions.",
    },
    {
        "folder": "SWIFT-CSCF",
        "title": "Cisco Secure Workload - SWIFT CSCF Compliance Report",
        "stem": "CSW-SWIFT-CSCF-Compliance-Report",
        "standard": "SWIFT Customer Security Controls Framework v2024",
        "audience": "Financial institutions, SWIFT operations teams, security teams, and assurance owners.",
        "driver": "SWIFT secure zone isolation, mandatory/advisory control mapping, operator session integrity context, Internet restriction, and SWIFT-specific logging support.",
        "scope": "`SWIFT-CSCF` > `Secure-Zone`, `SWIFT-Interfaces`, `Operator-Workstations`, `Jump-Hosts`, `Internet-Restricted-Systems`, `Third-Party-Connectivity`",
        "outcomes": [
            "Identify workloads within or connected to the SWIFT secure zone.",
            "Review Internet and third-party egress paths from SWIFT-related systems.",
            "Support segmentation evidence for mandatory and advisory controls.",
            "Package flow and process telemetry for operational review.",
        ],
        "evidence": [
            "SWIFT secure zone workload inventory",
            "Internet access restriction evidence",
            "Operator / jump-host flow summary",
            "Policy candidate and exception register",
            "Monitoring and incident timeline sample",
        ],
        "boundaries": "CSW does not replace SWIFT CSP attestation, endpoint hardening, operator authentication, transaction integrity, logging retention, or SWIFT-specific application controls.",
    },
    {
        "folder": "HITRUST-CSF",
        "title": "Cisco Secure Workload - HITRUST CSF Compliance Report",
        "stem": "CSW-HITRUST-Compliance-Report",
        "standard": "HITRUST CSF v11",
        "audience": "Healthcare, life sciences, payer, provider, and service-provider teams preparing HITRUST evidence.",
        "driver": "Harmonized HIPAA / ISO / NIST / PCI mapping, e1/i1/r2 assessment guidance, network segregation, vulnerability management, and incident evidence.",
        "scope": "`HITRUST-CSF` > `Regulated-Data-Systems`, `Network-Segmentation`, `Vulnerability-Management`, `Incident-Evidence`, `Third-Party-Egress`",
        "outcomes": [
            "Support HITRUST-aligned evidence for segmentation and network protection.",
            "Map workload controls to harmonized HIPAA, ISO, NIST, and PCI themes.",
            "Identify vulnerability exposure and reachable regulated workloads.",
            "Build incident and monitoring evidence for assessment review.",
        ],
        "evidence": [
            "HITRUST-scoped workload inventory",
            "Segmentation and network restriction evidence",
            "Vulnerability exposure summary",
            "Third-party egress summary",
            "Incident timeline and monitoring sample",
        ],
        "boundaries": "CSW does not replace HITRUST assessment methodology, control scoring, privacy governance, IAM, encryption, vendor management, or policy ownership.",
    },
    {
        "folder": "NIST-800-171",
        "title": "Cisco Secure Workload - NIST SP 800-171 Rev. 3 Compliance Report",
        "stem": "CSW-NIST-800-171-Compliance-Report",
        "standard": "NIST SP 800-171 Rev. 3",
        "audience": "Defense industrial base, CUI enclave owners, CMMC preparation teams, and security architects.",
        "driver": "CUI enclave isolation, 03.01 and 03.13 flow enforcement, Rev. 3 family alignment, and CMMC Level 2 underpinning evidence.",
        "scope": "`NIST-800-171` > `CUI-Enclave`, `CUI-Applications`, `Boundary-Services`, `Admin-Paths`, `External-Connections`",
        "outcomes": [
            "Identify CUI-related workloads and enclave boundaries.",
            "Support access control and system communication protection evidence.",
            "Document allowed and observed workload communication paths.",
            "Package evidence that can inform CMMC Level 2 preparation.",
        ],
        "evidence": [
            "CUI workload inventory",
            "Enclave flow and boundary map",
            "Policy candidate and exception register",
            "External connection summary",
            "Vulnerability and monitoring evidence",
        ],
        "boundaries": "CSW does not replace CUI marking, contracts, SSP/POA&M ownership, identity governance, encryption, media protection, or CMMC assessment decisions.",
    },
    {
        "folder": "CSA-CCM",
        "title": "Cisco Secure Workload - CSA CCM v4 Compliance Report",
        "stem": "CSW-CSA-CCM-Compliance-Report",
        "standard": "Cloud Security Alliance Cloud Controls Matrix v4",
        "audience": "Cloud security, SaaS, IaaS/PaaS, and STAR certification preparation teams.",
        "driver": "Cloud workload segmentation, IVS-09 network security, DSP data isolation, TVM reachability, and STAR evidence support.",
        "scope": "`CSA-CCM` > `Cloud-Workloads`, `Tenant-Boundaries`, `Data-Protection`, `Network-Security`, `Threat-Vulnerability-Management`",
        "outcomes": [
            "Map cloud workloads to tenant and data-boundary labels.",
            "Support infrastructure and virtualization security evidence.",
            "Identify reachability of vulnerable cloud workloads.",
            "Package segmentation and monitoring artifacts for STAR discussions.",
        ],
        "evidence": [
            "Cloud workload inventory",
            "Tenant and data-boundary flow summary",
            "IVS / DSP / TVM evidence package",
            "Vulnerability reachability summary",
            "Policy candidate and exception register",
        ],
        "boundaries": "CSW does not replace CSP native controls, IAM, KMS, logging retention, cloud posture management, STAR attestation, or shared-responsibility decisions.",
    },
    {
        "folder": "COBIT-2019",
        "title": "Cisco Secure Workload - COBIT 2019 Compliance Report",
        "stem": "CSW-COBIT-Compliance-Report",
        "standard": "COBIT 2019",
        "audience": "IT governance, risk, audit, security operations, and control owners.",
        "driver": "DSS05.02 network security, APO13 managed security, MEA01/02 conformance monitoring, and BAI06/10 change and configuration evidence.",
        "scope": "`COBIT-2019` > `Governance-Evidence`, `Managed-Security`, `Network-Security`, `Change-Configuration`, `Monitoring`",
        "outcomes": [
            "Provide workload-level evidence for governance and assurance conversations.",
            "Support network security and configuration monitoring objectives.",
            "Document policy changes, exceptions, and operational review points.",
            "Translate technical telemetry into management-system evidence.",
        ],
        "evidence": [
            "Governance scope workload inventory",
            "Network security flow summary",
            "Change / configuration evidence",
            "Monitoring and exception register",
            "Management review package",
        ],
        "boundaries": "CSW does not replace COBIT governance design, process ownership, risk appetite decisions, enterprise metrics, audit judgment, or GRC workflow.",
    },
    {
        "folder": "AU-Essential-Eight",
        "title": "Cisco Secure Workload - Australian Essential Eight Compliance Report",
        "stem": "CSW-Essential-Eight-Compliance-Report",
        "standard": "ACSC Essential Eight",
        "audience": "Australian public and private-sector security teams using Essential Eight maturity guidance.",
        "driver": "ML1-ML3 maturity evidence, patch prioritisation using CVE / EPSS and reachability, admin path restriction, and application control support.",
        "scope": "`Essential-Eight` > `Critical-Applications`, `Admin-Paths`, `Patch-Priority`, `Application-Control-Support`, `Monitoring`",
        "outcomes": [
            "Prioritize patching using vulnerability, exploitability, and reachability context.",
            "Restrict administrative workload communication paths.",
            "Support application control conversations with observed process telemetry.",
            "Package maturity-level evidence for segmentation and monitoring.",
        ],
        "evidence": [
            "Critical workload inventory",
            "Admin path flow summary",
            "Patch prioritization export",
            "Observed process and application evidence",
            "Policy candidate and exception register",
        ],
        "boundaries": "CSW does not replace application control enforcement, endpoint hardening, MFA, backup recovery, macro controls, or ACSC maturity assessment ownership.",
    },
    {
        "folder": "UK-Cyber-Essentials",
        "title": "Cisco Secure Workload - UK Cyber Essentials Plus Compliance Report",
        "stem": "CSW-Cyber-Essentials-Compliance-Report",
        "standard": "UK Cyber Essentials Plus",
        "audience": "UK organisations preparing Cyber Essentials or Cyber Essentials Plus technical verification.",
        "driver": "CE1 workload-level firewall evidence, CE2 secure configuration baseline, CE5 patch management evidence, and Plus verification support.",
        "scope": "`UK-Cyber-Essentials` > `Internet-Facing-Systems`, `Workload-Firewall`, `Secure-Configuration`, `Patch-Evidence`, `Verification-Sample`",
        "outcomes": [
            "Identify Internet-facing and sensitive workloads.",
            "Document workload-level firewall and segmentation posture.",
            "Support secure configuration and patch management evidence.",
            "Prepare technical verification evidence for Plus discussions.",
        ],
        "evidence": [
            "Cyber Essentials workload inventory",
            "Firewall / policy evidence",
            "Secure configuration support notes",
            "Patch exposure summary",
            "Verification sample pack",
        ],
        "boundaries": "CSW does not replace Cyber Essentials certification, endpoint configuration, malware protection, MFA, unsupported software governance, or assessor testing.",
    },
    {
        "folder": "HIPAA-2025-NPRM",
        "title": "Cisco Secure Workload - HIPAA 2025 NPRM Compliance Report",
        "stem": "CSW-HIPAA-NPRM-Compliance-Report",
        "standard": "HIPAA Security Rule 2025 NPRM",
        "audience": "Healthcare covered entities, business associates, compliance leaders, and security teams tracking the proposed rule.",
        "driver": "Mandatory network segmentation, technology asset inventory, 24-month log retention architecture, 72-hour breach timeline, and annual assessment evidence.",
        "scope": "`HIPAA-2025-NPRM` > `ePHI-Systems`, `Network-Segmentation`, `Technology-Assets`, `Log-Retention`, `Incident-Timeline`, `Annual-Assessment`",
        "outcomes": [
            "Map ePHI-related workloads and proposed segmentation boundaries.",
            "Support technology asset inventory with workload and software telemetry.",
            "Prepare incident timeline evidence for proposed 72-hour expectations.",
            "Document architecture considerations for longer log-retention requirements.",
        ],
        "evidence": [
            "ePHI workload inventory",
            "Segmentation policy and flow evidence",
            "Technology asset and software inventory",
            "Incident timeline sample",
            "Annual assessment evidence package",
        ],
        "boundaries": "This mapping is based on a proposed rule and must be revalidated after final rulemaking. CSW does not replace legal analysis, HIPAA policies, risk analysis, BAA management, IAM, encryption, or regulatory reporting.",
    },
]


def report_markdown(item: dict[str, object]) -> str:
    outcomes = "\n".join(f"- {entry}" for entry in item["outcomes"])
    evidence = "\n".join(f"- {entry}" for entry in item["evidence"])
    return f"""# {item['title']}

## Customer-Facing Compliance Report

**Framework:** {item['standard']}  
**Primary audience:** {item['audience']}  
**CSW positioning:** {item['driver']}

---

## Executive Summary

Cisco Secure Workload (CSW) can support this framework by producing workload-level evidence for inventory, application dependency mapping, segmentation design, policy simulation, vulnerability context, and incident investigation. The strongest customer story is not that CSW "certifies" compliance; it is that CSW turns workload communication into evidence that control owners, assessors, and technical teams can review.

## Suggested CSW Scope Pattern

{item['scope']}

This scope pattern should be validated with the customer's architecture, application owners, compliance team, and assessor before it is used for formal evidence.

## Outcomes CSW Can Support

{outcomes}

## Evidence Package

{evidence}

## POV / Workshop Approach

1. Select one business service, regulated boundary, or critical workload group.
2. Validate workload coverage and install sensors or configure supported connectors.
3. Apply labels for application, environment, owner, data class, criticality, compliance scope, and lifecycle.
4. Observe flows over a representative business window.
5. Use ADM to generate a candidate policy and review it with the application owner.
6. Package inventory, scope, flows, policy, exceptions, and known gaps as the evidence output.

## Boundaries and Complementary Controls

{item['boundaries']}

## Disclaimer

This report is for informational and planning purposes. It is not legal, regulatory, audit, or certification advice. Validate all mappings against the current official framework text, the customer's environment, and qualified compliance, legal, and audit professionals.
"""


def plain_text(markdown: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", markdown)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"^- ", "• ", text, flags=re.MULTILINE)
    text = text.replace("---", "")
    return text


def write_simple_pdf(text: str, output_path: Path) -> None:
    """Write a simple multi-page PDF using Helvetica and ASCII-compatible text."""
    lines: list[str] = []
    for paragraph in text.splitlines():
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        if paragraph.startswith("• "):
            wrapped = textwrap.wrap(paragraph, width=88, subsequent_indent="  ")
        else:
            wrapped = textwrap.wrap(paragraph, width=92)
        lines.extend(wrapped or [""])

    pages = [lines[i : i + 48] for i in range(0, len(lines), 48)] or [[]]
    objects: list[bytes] = []

    def pdf_escape(value: str) -> str:
        value = value.encode("latin-1", "replace").decode("latin-1")
        return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")

    # 1 catalog, 2 pages, then pairs of page/content objects.
    kids = []
    for idx, page_lines in enumerate(pages):
        page_obj_num = 3 + idx * 2
        content_obj_num = page_obj_num + 1
        kids.append(f"{page_obj_num} 0 R")
        stream_lines = ["BT", "/F1 10 Tf", "50 760 Td", "14 TL"]
        for line in page_lines:
            stream_lines.append(f"({pdf_escape(line)}) Tj")
            stream_lines.append("T*")
        stream_lines.append("ET")
        stream = "\n".join(stream_lines).encode("latin-1", "replace")
        objects.append(
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            f"/Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> >> >> "
            f"/Contents {content_obj_num} 0 R >>".encode("latin-1")
        )
        objects.append(b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream")

    all_objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        f"<< /Type /Pages /Kids [{' '.join(kids)}] /Count {len(pages)} >>".encode("latin-1"),
        *objects,
    ]

    output = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for number, obj in enumerate(all_objects, start=1):
        offsets.append(len(output))
        output.extend(f"{number} 0 obj\n".encode("ascii"))
        output.extend(obj)
        output.extend(b"\nendobj\n")
    xref_offset = len(output)
    output.extend(f"xref\n0 {len(all_objects) + 1}\n".encode("ascii"))
    output.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        output.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    output.extend(
        f"trailer\n<< /Size {len(all_objects) + 1} /Root 1 0 R >>\n"
        f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii")
    )
    output_path.write_bytes(bytes(output))


def run_pandoc(markdown: str, output_path: Path, to_format: str, title: str) -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as tmp:
        tmp.write(markdown)
        tmp_path = Path(tmp.name)
    try:
        cmd = [
            "pandoc",
            "--standalone",
            "--from",
            "markdown",
            "--to",
            to_format,
            "--metadata",
            f"title={title}",
            "-o",
            str(output_path),
            str(tmp_path),
        ]
        if to_format == "html5":
            header = tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False)
            header.write(f"<style>\n{CSS.read_text(encoding='utf-8')}\n</style>\n")
            header.close()
            cmd[2:2] = ["--embed-resources", "--toc", "--toc-depth=2", "--include-in-header", header.name]
        subprocess.run(cmd, check=True)
    finally:
        tmp_path.unlink(missing_ok=True)
        if to_format == "html5" and "header" in locals():
            Path(header.name).unlink(missing_ok=True)


def main() -> int:
    for item in FRAMEWORKS:
        folder = ROOT / str(item["folder"])
        folder.mkdir(parents=True, exist_ok=True)
        markdown = report_markdown(item)
        stem = folder / str(item["stem"])
        print(f"report -> {stem.relative_to(ROOT)}.docx/.html/.pdf")
        run_pandoc(markdown, stem.with_suffix(".docx"), "docx", str(item["title"]))
        run_pandoc(markdown, stem.with_suffix(".html"), "html5", str(item["title"]))
        write_simple_pdf(plain_text(markdown), stem.with_suffix(".pdf"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
