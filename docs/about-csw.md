# Background — What is Cisco Secure Workload?

> Background page for the
> [CSW Compliance Mapping repository](../README.md). Read this if you
> want context on the platform itself before working through the
> framework mappings.

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

## Machine learning, in practical terms

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

## Why that matters for compliance

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

The [main repository README](../README.md) explains, framework-by-framework,
exactly which auditor questions and which incident-response questions
that data answers — and what artefact you'd hand over in each case.

---

**See also**

- [Why these mappings matter](./why-these-mappings-matter.md) — the
  conversation prompts that explain why segmentation and workload
  evidence are leading indicators, not just compliance checkboxes.
- [Audience and usage guide](./audience-and-usage.md) — who should read
  what, file format choices, and folder layout.
- [Repository README](../README.md) — asset library, scope notes, and
  disclaimer.
