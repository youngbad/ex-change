# Security requirements

## Status

There is no authentication, authorization, application, database, or
deployment configuration in the repository. The controls below are target
requirements, not implemented protections.

## Identity and authorization

- Use an established OIDC provider or a reviewed authentication service;
  require MFA for privileged and compliance roles.
- Hash local passwords with Argon2id if local credentials are approved. Protect
  refresh-token/session rotation, revocation, secure cookies, and recovery flows.
- Enforce least privilege with granular role and branch scope on every API
  operation and data query; deny by default.
- Separate cashier, branch manager, accountant, compliance officer, auditor,
  and administrator duties. Read-only auditors must not mutate financial data.
- Apply rate limits, login-attempt monitoring, lockout/recovery controls, and
  session expiration without leaking account existence.

## Financial and sensitive data

- Validate all input at the API boundary and again at business-rule boundaries.
- Use parameterized ORM/database operations, output encoding, secure headers,
  and CSRF controls for cookie-authenticated requests.
- Encrypt transport and sensitive data at rest using managed keys; define
  rotation, backup protection, masking, and key access separation.
- Mask sensitive identifiers in ordinary screens and logs. Record and restrict
  sensitive-data access and AML case access.
- Do not log passwords, tokens, full payment credentials, or unnecessary
  customer identity data.
- Make posted financial records append-only in application permissions and
  database controls; record corrections as auditable operations.

## Audit and secrets

Audit authentication events, authorization changes, transaction posting and
reversal, rate approvals, cash adjustments, AML decisions, sensitive-data
access, and configuration changes. Record actor, UTC time, action, entity,
correlation ID, reason when required, and minimized before/after values.
Protect logs from tampering and unauthorized access.

Load secrets only through environment-specific secret management; never commit
credentials. Restrict service/database accounts and separate operational and
analytics access. Review dependencies and container images before release.

## Operational assurance

Define threat model, security review cadence, incident response, vulnerability
handling, backup/restore tests, retention, and production access procedures.
Expose health checks without sensitive details. Security testing and legal
privacy review are release gates; this requirements document is not a
certification.
