# Why these mappings matter

> Companion to the
> [CSW Compliance Mapping repository](../README.md). The README gives
> the short version of why these mappings exist; this page is the
> longer argument — the kind you'd walk a sceptical engineer or
> auditor through.

## Use them to start a different conversation — with yourself

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

### Notice the pattern

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

## Why look at CSW at all?

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

---

**See also**

- [Background — What is Cisco Secure Workload?](./about-csw.md)
- [Audience and usage guide](./audience-and-usage.md) — who should read
  what, file format choices, and folder layout.
- [Repository README](../README.md) — asset library, scope notes, and
  disclaimer.
