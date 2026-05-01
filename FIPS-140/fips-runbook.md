# Cisco Secure Workload — FIPS 140-2/3 Compliance Framework
## Technical Runbook | Federal & Regulated Accounts

**Version:** 1.0 | **Standard:** FIPS 140-2 / FIPS 140-3 (CSW-Relevant Scope)

---

## 1. Overview & CSW Role

FIPS 140-2/3 is a US federal standard for cryptographic module validation. **CSW is not itself a cryptographic module** — it does not encrypt data at rest or in transit. However, CSW plays a critical **enforcement and detection** role in FIPS compliance programs by:

1. **Detecting non-FIPS-compliant cryptographic protocols** in workload communications
2. **Enforcing FIPS-compliant communication paths** via micro-segmentation policy
3. **Auditing all cryptographic service access** through flow and process telemetry
4. **Identifying workloads using non-approved algorithms** through port/protocol analysis

---

## 2. FIPS-Relevant CSW Capabilities

### 2.1 Non-FIPS Protocol Detection

CSW ADM and flow telemetry identify the following non-FIPS-compliant communications:

| Protocol / Service | Non-FIPS Indicator | CSW Detection Method |
|---|---|---|
| TLS 1.0 / 1.1 | Non-approved TLS version | Port 443 flow + process context analysis |
| SSLv2 / SSLv3 | Deprecated, non-FIPS | Flow telemetry protocol identification |
| MD5-based connections | Non-approved hash | Process + connection pattern analysis |
| Plain HTTP (port 80) | No encryption | Flow telemetry protocol filter |
| Plain FTP (port 21) | No encryption | Flow telemetry port filter |
| Telnet (port 23) | No encryption | Flow telemetry port filter |
| LDAP plain (port 389) | Non-encrypted directory | Flow telemetry port filter |
| SNMPv1/v2 (port 161) | Non-encrypted management | Flow telemetry port filter |

### 2.2 Enforcement of FIPS-Compliant Paths

CSW policy can **block non-compliant protocols** and **enforce approved alternatives**:

```
CSW Policy: FIPS-Protocol-Enforcement
  DENY: Any → Any (port 80)     # Block plain HTTP
  DENY: Any → Any (port 21)     # Block plain FTP
  DENY: Any → Any (port 23)     # Block Telnet
  DENY: Any → Any (port 389)    # Block plain LDAP
  DENY: Any → Any (port 161)    # Block SNMPv1/v2

  ALLOW: Any → Any (port 443)   # HTTPS (enforce TLS 1.2+ at app level)
  ALLOW: Any → Any (port 22)    # SSH (FIPS-compliant cipher suites)
  ALLOW: Any → Any (port 636)   # LDAPS
  ALLOW: Any → Any (port 162)   # SNMPv3
  ALLOW: Any → Any (port 990)   # FTPS
```

### 2.3 Cryptographic Service Access Auditing

For workloads using FIPS-validated HSMs or crypto libraries:

```
CSW UI → Investigate → Flow Search
  → Destination: HSM IP / crypto service endpoint
  → Process context: identifies which app is accessing crypto service
  → Log: full access audit for FIPS boundary documentation
```

---

## 3. FIPS Boundary Documentation

FIPS 140-2/3 requires precise definition of the cryptographic module boundary. CSW supports this through:

### 3.1 Crypto Service Scope

Define a CSW scope for FIPS-validated cryptographic infrastructure:

```
Root Scope
└── FIPS-Boundary
    ├── HSM-Cluster (validated hardware)
    ├── Crypto-Services (validated software libraries)
    └── Key-Management (KMS endpoints)
```

**Policy for FIPS-Boundary scope:**
- Default DENY all inbound
- ALLOW only explicitly approved workloads to access HSM/KMS
- LOG all connections to FIPS-Boundary scope (full audit trail)
- ALERT on any unapproved access attempt

### 3.2 Algorithm Identification via Process Telemetry

CSW process monitoring identifies workloads using non-FIPS-approved crypto libraries:

```
CSW UI → Investigate → Process Search
  → Filter: process name contains "openssl", "libssl", "nss"
  → Review: version number indicates FIPS-validated status
  → Flag: workloads using pre-FIPS OpenSSL versions
```

---

## 4. FIPS 140-3 Transition Support

FIPS 140-3 (based on ISO/IEC 19790:2012) replaces 140-2. CSW supports the transition by:

- **Inventorying** all workloads accessing cryptographic services (ADM map)
- **Flagging** workloads still using FIPS 140-2-only validated modules
- **Tracking** rollout of FIPS 140-3 validated replacements via ADM comparison
- **Enforcing** updated protocol requirements as crypto standards evolve

---

## 5. Evidence Package for FIPS Compliance

| Evidence Item | CSW Source | FIPS Relevance | Frequency |
|---|---|---|---|
| Non-FIPS protocol flow report | Investigate → Flow Search (port filter) | Module boundary | Weekly |
| FIPS-Boundary access log | Investigate → Flow Search (scope filter) | Access control | Continuous |
| Crypto service process audit | Investigate → Process Search | Module usage | Monthly |
| Policy enforcement log (FIPS policy) | Defend → Policy Analysis | Protocol enforcement | Monthly |
| HSM/KMS access audit | Flow Search → FIPS-Boundary scope | Key management | Continuous |

---

## 6. What CSW Does NOT Cover

| FIPS Requirement | Outside CSW Scope | Recommended Solution |
|---|---|---|
| Cryptographic module validation | CSW is not a crypto module | Use FIPS 140-3 validated libraries (OpenSSL FIPS, BouncyCastle) |
| Algorithm implementation testing | Hardware/software crypto validation | NIST CMVP testing laboratory |
| Key generation & storage | Key lifecycle management | FIPS-validated HSM (Thales, Entrust) |
| Self-tests at module boundary | Module-level testing | Crypto library self-test procedures |

---

*Replace [Customer Name] and bracketed fields before customer delivery.*
