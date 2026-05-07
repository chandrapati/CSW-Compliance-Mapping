# Cisco Secure Workload — Framework Scope Design Guide

Customer-facing scope and label patterns for Cisco Secure Workload (CSW)
compliance mapping workshops.

Use this guide before a proof-of-value, deployment planning workshop, or
evidence-readiness discussion. It helps teams translate framework language
into practical CSW scopes, labels, and evidence boundaries. These patterns
are starting points: validate final scope with the customer's architecture,
asset owners, compliance team, and assessor.

## Scope Design Principles

1. **Start from the protected service, not the tool.** Define the system,
   business function, data boundary, or regulated environment first; then
   map CSW scopes to that boundary.
2. **Separate regulatory scope from operational ownership.** A PCI CDE,
   HIPAA ePHI zone, CUI enclave, or DORA important business function may
   cross teams, clouds, and platforms.
3. **Use labels for policy and evidence.** Scopes should be generated from
   stable labels where possible so inventory, ADM, flow search, policy
   workspaces, and reports use the same vocabulary.
4. **Reconcile CSW coverage.** CSW evidence covers instrumented workloads
   and supported connector visibility. Reconcile gaps with the CMDB, cloud
   inventory, OT inventory, IAM, SIEM, vulnerability scanner, and GRC tools.
5. **Keep out-of-scope explicit.** Physical controls, legal obligations,
   cryptographic module validation, IAM/MFA, endpoint malware controls, and
   OT device enforcement usually require complementary controls.

## Framework Scope Design Table

| Framework | Customer scope anchor | Suggested CSW scope pattern | Primary evidence focus | Boundaries and complementary controls |
|---|---|---|---|---|
| HIPAA Security Rule | ePHI applications, databases, clinical integrations, and business associate connections | `Healthcare-Org` > `ePHI-Zone` > app/service scopes such as `EHR`, `Billing`, `PACS`, `HL7`; separate `BAA-Partners` egress scope | ePHI workload isolation, access-path evidence, audit-control telemetry, risk-analysis inputs | HIPAA administrative, physical, legal, and BAA obligations remain outside CSW; validate PHI classification with privacy/compliance owners |
| SOC 2 Type II | The service organization's system boundary and selected Trust Services Criteria | `SOC2-System` > `Production`, `Supporting-Infra`, `Admin-Access`, `Vendor-Integrations`; align scope to system description | Operating-effectiveness evidence for segmentation, monitoring, change drift, incident investigation | SOC 2 criteria depend on the auditor's system description and control design; CSW augments IAM, change management, SIEM, and availability controls |
| PCI DSS v4.0 | Cardholder Data Environment (CDE), CDE-connected systems, and security-impacting systems | `PCI-Environment` > `CDE`, `CDE-Connected`, `Security-Services`, `Third-Party-Processors`, `Out-of-Scope-Validation` | CDE flow documentation, segmentation simulation/enforcement, policy exceptions, vulnerability exposure context | CSW does not replace QSA judgment, ASV scans, penetration testing, network security controls, or PCI governance requirements |
| NIST SP 800-53 Rev. 5 | FISMA/FedRAMP system boundary and SSP control implementation | `System-Boundary` > impact-level or component scopes such as `Moderate`, `High`, `Data-Store`, `App-Tier`, `Management` | AC, AU, CM, IR, RA, SC, and SI evidence for covered workloads | Full 800-53 scope includes many controls outside CSW: identity, personnel, physical, contingency, privacy, and governance controls |
| ISO/IEC 27001:2022 | ISMS scope, information assets, and Annex A control applicability | `ISMS-Boundary` > `Confidential-Data`, `Business-Critical-Apps`, `Cloud-Services`, `Supplier-Connections` | Annex A.8 monitoring, network security, segregation, vulnerability, and supplier-egress evidence | Certification depends on ISMS design, SoA, risk treatment, internal audit, and management review; CSW is a technical evidence source |
| CISA Zero Trust Maturity Model | Agency/enterprise zero-trust initiative by pillar and use case | `ZT-Workloads` > `Sensitive-Apps`, `Privileged-Admin`, `Inter-App-Flows`, `External-Dependencies` | Workload-layer evidence for networks and applications/workloads pillars, plus visibility and analytics | ZTMM maturity is organizational; pair CSW with IdP, MFA, device posture, data governance, SIEM/SOAR, and policy orchestration |
| FIPS 140 | Systems handling regulated cryptographic use or plaintext-protocol risk | `Crypto-Review` > `Sensitive-Transport`, `Plaintext-Protocol-Candidates`, `FIPS-Required-Systems` | Detection/blocking of obvious plaintext transports and inventory support for cryptographic usage review | CSW is not a FIPS-validated cryptographic module; validation, key management, and module selection belong to FIPS-validated libraries/HSMs |
| NIST SP 800-207 | Zero Trust Architecture tenets for workload-to-workload access | `ZTA-Resources` > `Protected-Resources`, `Policy-Enforced-Flows`, `Observed-Dependencies`, `Exceptions` | Resource inventory, per-connection flow evidence, dynamic scoping, workload enforcement as one possible PEP placement | NIST ZTA also requires identity, device posture, policy decision architecture, and enterprise-wide telemetry beyond CSW |
| NIST SP 800-207A | PDP/PEP/PA/PIP component mapping for a cloud-native ZTA discussion | `ZTA-Components` > `PEP-Analogue`, `Policy-Workspace`, `Telemetry-PIP`, `SOAR-Integrated` | Illustrative traceability from CSW policy, enforcement, and telemetry to 207A-style logical components | Treat PDP/PEP/PA/PIP mapping as an analogue for workload segmentation, not a complete enterprise ZTA architecture |
| DORA | Important business functions (IBFs), supporting ICT assets, and third-party dependencies | `DORA-IBF` > one scope per IBF, with nested `Critical`, `Supporting`, `Third-Party-Egress`, `Incident-Dossier` scopes | Article 8 inventory inputs, Article 9 segmentation, Article 10 detection, Article 19 incident evidence, Article 28 technical egress | DORA governance, register of information, contracts, testing programme, and authority reporting remain customer-owned |
| NIS2 | Essential/important entity services and Article 21 risk-management measures | `NIS2-Service` > `Essential-Service`, `Important-Service`, `Supplier-Egress`, `Incident-Reporting`, `High-Risk-Workloads` | Risk-policy enforcement evidence, incident dossier, supply-chain egress, vulnerability exposure, secured workload paths | MFA, training, governance, cryptography, secured voice/video, and national transposition specifics require complementary programmes |
| NERC CIP | IT-side systems supporting BES Cyber System functions | `BES-Supporting-IT` > `EACMS`, `Jump-Hosts`, `Vendor-Access`, `BCSI-Hosts`, `Identity-PKI`, `Patch-Repos` | IT-side ESP boundary evidence, interactive remote access paths, ports/services baseline, vulnerability and change evidence | CSW is not an EAP and does not enforce on PLCs/RTUs/IEDs/HMIs; pair with boundary firewalls and OT-aware monitoring |
| TSA Pipeline Security Directive | IT-side systems supporting Critical Cyber Systems and IT/OT segmentation | `Pipeline-IT-Estate` > `OT-Facing-IT`, `CCS-Supporting-IT`, `Vendor-Access`, `Patch-Repositories`, `Corporate-IT` | IT-side segmentation, documented IT-to-OT flows, access control, monitoring, unpatched-system risk evidence | CSW does not replace the Cybersecurity Coordinator, CAP/CIRP, architecture review, boundary firewall, or OT DPI/monitoring tools |
| CIS Controls v8.1 | Enterprise assets and software in the customer's Implementation Group scope | `CIS-IG2` > `Enterprise-Assets`, `Software-Inventory`, `Secure-Config`, `Vuln-Exposure`, `Network-Monitoring` | Controls 1, 2, 4, 7, 8, 13, and 17 evidence for covered workloads | Reconcile CSW inventory with enterprise source of truth; endpoint, email, awareness, backup, and data controls are broader than CSW |
| NIST CSF 2.0 | CSF Profile outcomes, target tier, and management reporting needs | `CSF-Profile` > `Govern-Evidence`, `Identify-Assets`, `Protect-Segmentation`, `Detect-Monitoring`, `Respond-Dossier`, `Recover-Diff` | Technical evidence that feeds GV, ID, PR, DE, RS, and RC outcomes | CSF is an outcomes framework; CSW does not author the Profile or replace governance, risk appetite, or enterprise policy decisions |
| CMMC 2.0 | FCI/CUI enclave and CMMC assessment boundary | `CMMC-Scope` > `CUI-Enclave`, `FCI-Systems`, `CUI-Connected`, `Admin-Access`, `External-Services`, `Out-of-Scope-Validation` | AC, AU, CM, RA, SC, and SI technical evidence for CUI-scope workloads | CMMC requires SSP, POA&M, CUI scoping, and C3PAO/government assessment as applicable; CSW supports evidence but does not certify compliance |

## Label / Tag Recommendations

### Baseline Labels for Every Customer

Use a small, consistent baseline across all frameworks. Keep values stable
and controlled; avoid free-form spelling differences that split evidence.

| Label key | Example values | Why it matters |
|---|---|---|
| `app` | `payments-api`, `ehr-core`, `identity` | Groups workloads into application scopes and ADM workspaces |
| `env` | `prod`, `stage`, `dev`, `test` | Separates production evidence from non-production noise |
| `owner` | `team-payments`, `clinical-apps`, `platform` | Connects policy exceptions and remediation to accountable teams |
| `data_class` | `public`, `internal`, `confidential`, `phi`, `pci`, `cui` | Drives regulated data boundaries and evidence queries |
| `compliance` | `hipaa`, `pci`, `soc2`, `dora`, `cmmc`, `none` | Enables framework-specific scopes without duplicating inventory |
| `criticality` | `critical`, `high`, `medium`, `low` | Supports prioritization, segmentation strictness, and incident response |
| `internet_exposed` | `true`, `false` | Helps identify boundary and attack-surface review candidates |
| `third_party` | `none`, `supplier-name`, `processor-name` | Supports supplier egress and business associate / processor reviews |
| `region` | `us-east`, `eu-west`, `site-001` | Supports residency, operational ownership, and sector/site reporting |
| `lifecycle` | `active`, `exception`, `decommissioning` | Keeps stale workloads and temporary exceptions visible |

### Framework-Specific Labels

| Framework | Additional label keys | Example values | Scope-design use |
|---|---|---|---|
| HIPAA | `phi_scope`, `clinical_system`, `baa_partner`, `ehr_app` | `in-scope`, `epic`, `clearinghouse-a`, `true` | Build ePHI and partner-egress scopes |
| SOC 2 | `soc2_boundary`, `trust_service`, `system_component` | `in-scope`, `security`, `database` | Align workloads to the SOC 2 system description |
| PCI DSS v4.0 | `pci_scope`, `cde_zone`, `card_data_role`, `qsa_exception` | `cde`, `cde-connected`, `pan-storage`, `none` | Separate CDE, connected, and out-of-scope validation populations |
| NIST 800-53 | `system_id`, `impact_level`, `control_family`, `ssp_component` | `sys-001`, `moderate`, `ac`, `app-tier` | Tie workloads to SSP components and impact-level evidence |
| ISO 27001:2022 | `isms_scope`, `soa_control`, `asset_type`, `supplier_related` | `in-scope`, `a.8.22`, `database`, `true` | Align CSW evidence with the SoA and asset inventory |
| CISA ZTMM | `zt_pillar`, `zt_stage_target`, `zt_use_case` | `networks`, `advanced`, `east-west` | Organize evidence by maturity pillar and use case |
| FIPS 140 | `fips_required`, `crypto_review`, `plaintext_risk`, `module_owner` | `true`, `transport`, `high`, `platform` | Identify workloads needing crypto posture review |
| NIST 800-207 | `zta_resource`, `pep_candidate`, `policy_source`, `access_pattern` | `protected`, `csw-workload`, `adm`, `inter-app` | Trace workload resources and enforcement patterns |
| NIST 800-207A | `zta_component`, `pdp_analogue`, `pip_signal`, `pa_workspace` | `pep`, `csw-policy`, `vuln-context`, `zta-prod` | Support logical-component discussion and traceability |
| DORA | `dora_ibf`, `ibf_name`, `ibf_criticality`, `ict_third_party` | `true`, `sepa-transfer`, `critical`, `provider-a` | Build IBF and third-party exposure scopes |
| NIS2 | `nis2_entity_type`, `nis2_service`, `article21_measure`, `csirt_reportable` | `essential`, `health-service`, `21-2-b`, `true` | Structure service, measure, and incident evidence |
| NERC CIP | `cip_scope`, `bes_support_role`, `eacms`, `bcsi`, `ot_facing` | `it-side`, `jump-host`, `true`, `false`, `true` | Isolate IT-side BES-supporting systems and access paths |
| TSA Pipeline | `tsa_scope`, `ccs_function`, `site`, `ot_facing`, `vendor_access` | `it-side`, `historian`, `site-001`, `true`, `true` | Build site-specific IT/OT and vendor access scopes |
| CIS Controls v8.1 | `cis_control`, `implementation_group`, `asset_inventory_source` | `control-1`, `ig2`, `cmdb` | Organize evidence by Safeguard and Implementation Group |
| NIST CSF 2.0 | `csf_function`, `csf_category`, `profile_scope`, `target_tier` | `protect`, `pr.ir`, `core-platform`, `tier-3` | Align evidence with CSF Profile outcomes |
| CMMC 2.0 | `cmmc_level`, `cui_scope`, `fci_scope`, `assessment_boundary`, `poam_item` | `l2`, `in-scope`, `false`, `cui-enclave`, `poam-123` | Build CUI/FCI boundaries and C3PAO evidence sets |

## Workshop Output Checklist

By the end of a scope-design workshop, capture:

- The customer-owned authoritative inventory source and reconciliation owner.
- The CSW scope hierarchy for the selected framework.
- Required baseline labels and framework-specific labels.
- Initial values for regulated data, criticality, owner, and environment.
- Known gaps: unsupported workloads, missing connectors, uninstrumented OT,
  unmanaged SaaS, IAM-only controls, physical controls, or legal obligations.
- The first ADM / flow-search window and evidence export cadence.
- A named owner for label hygiene and exception review.

## Customer Conversation Prompt

The practical question is not "can CSW map to this framework?" It is:

> Which workloads, flows, owners, and labels must be correct before the
> mapping becomes evidence a customer can validate with their assessor?

Use this guide to answer that question before building dashboards or
collecting audit packets.
