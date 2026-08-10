# Governance and evidence standards

This guide establishes the minimum governance standard for using Cisco Secure Workload (CSW) compliance mappings in a customer engagement. It is a reusable evidence-engineering aid—not an attestation, legal advice, certification opinion, or substitute for a customer's assessor.

## 1. Use each mapping as an evidence input

Every mapped control must have one of these applicability outcomes:

| Outcome | Meaning |
|---|---|
| **Direct evidence contribution** | CSW produces configuration, telemetry, policy, or audit evidence materially relevant to the control. |
| **Supporting evidence contribution** | CSW evidence supports a control whose complete implementation depends on customer processes or other technologies. |
| **Complementary control required** | CSW may help reduce risk, but another control owner or technology is required for the control objective. |
| **Out of scope** | CSW cannot provide relevant evidence for this control in the agreed deployment scope. |
| **Validate with SME / assessor** | Framework interpretation, product behavior, or scope requires current validation before reliance. |

Do not use “fully compliant,” “certified,” “guaranteed,” or equivalent language for a CSW mapping. Record the customer’s final applicability decision, evidence owner, and assessor feedback.

## 2. Shared responsibility

CSW is one evidence source within a broader control system. Capture responsibility for every mapped item.

| Party | Typical responsibility |
|---|---|
| Customer control owner | Defines scope, approves policy/change, retains evidence, accepts residual risk, and operates complementary controls. |
| Customer cloud/service provider | Provides platform-level identity, logging, physical, infrastructure, and service controls under the applicable shared-responsibility model. |
| Cisco Secure Workload | Produces supported workload visibility, policy, configuration, and audit evidence within the deployed scope. |
| Complementary tools | Supply CMDB, IAM, SIEM, vulnerability management, EDR, firewall, GRC, or OT-specific evidence where CSW does not. |

## 3. Evidence package standard

Use [`templates/evidence-package-manifest.yaml`](../templates/evidence-package-manifest.yaml) for every evidence package.

For each artifact, record:

1. The mapped framework/control ID and applicability outcome.
2. The customer scope, workloads, time window, and CSW product/version context.
3. Collector, collection time in UTC, evidence source, and SHA-256 checksum.
4. Classification, retention period, storage location, and access owner.
5. Any limitation: sensor offline, missing label, export delay, simulation-only result, or unsupported platform.

Store raw evidence in the customer-approved repository or evidence system—not in this reusable mapping repository.

## 4. Export, privacy, and secret handling

CSW flow, process, inventory, policy, and diagnostic exports can contain sensitive operational metadata, including hostnames, IP addresses, process paths, user-related context, and application topology.

- Classify exports under the customer’s information-handling policy before collection.
- Minimize fields and time range to the control objective; redact where external sharing is necessary.
- Encrypt evidence in transit and at rest using customer-approved mechanisms.
- Never commit API keys, API secrets, session tokens, credentials, raw diagnostic bundles, or unredacted customer exports to this repository.
- Use a customer-approved secret manager or runtime credential mechanism for automation.
- Record retention and deletion requirements in the evidence manifest.

## 5. Evidence integrity and failure handling

An export is not automatically defensible evidence. Before marking a control contribution as demonstrated, verify:

| Failure mode | Required response |
|---|---|
| Sensor offline or stale | Record the coverage gap; reconcile against the workload register/CMDB; do not imply continuous coverage. |
| Missing or drifted labels | Correct the label source, capture before/after evidence, and document affected policy scope. |
| Simulation-only policy | Mark as design validation, not enforcement proof. |
| Enforcement enabled but target version not applied | Capture the policy-application timestamp before functional testing. |
| Export lag, parsing error, or incomplete time window | Recollect or mark evidence partial; retain the limitation in the manifest. |
| Evidence altered for sharing | Preserve the original in approved customer storage and record the redaction/transformation. |

## 6. Exception and risk-acceptance register

Use this minimum record where a mapped control is partial, deferred, or compensated:

| Field | Required content |
|---|---|
| Exception ID | Stable identifier |
| Framework/control | Applicable framework and control ID |
| Scope and rationale | Affected workloads and reason |
| Risk owner | Accountable customer owner |
| Compensating control | Existing mitigation and evidence location |
| Expiry/review date | Time-bound reassessment date |
| Approval | Customer risk/change approver and reference |
| Status | Open, accepted, remediating, or closed |

## 7. Mapping lifecycle

Review a mapping when any of these changes:

- framework edition, regulator guidance, or assessor interpretation;
- CSW product release, supported-platform status, or connector behavior;
- customer deployment scope, cloud/provider model, or shared-responsibility boundary;
- evidence-source, retention, or data-classification requirement.

Record material changes in the repository changelog and regenerate derived artifacts. Every customer-facing report should identify the mapping version, framework edition, CSW version/validation context, review status, and disclaimer.

## 8. Standard customer-facing limitation statement

> This mapping identifies how Cisco Secure Workload may contribute evidence to the listed control objectives within the agreed deployment scope. It does not establish compliance, replace customer controls or assessor judgment, or constitute legal, regulatory, certification, or audit advice. Validate framework interpretation, product behavior, and final evidence sufficiency with qualified customer stakeholders and assessors.
