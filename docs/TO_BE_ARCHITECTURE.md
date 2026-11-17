# Target architecture

## Status and boundaries

This is a proposed architecture, not a description of implemented software.
Start with a modular monolith and explicit domain interfaces; extract services
only when operational evidence justifies doing so. Financial consistency and
traceability take precedence over service decomposition.

## Proposed stack

- **Web:** React, strict TypeScript, Vite, Tailwind CSS, accessible component
  system, TanStack Query, React Router, React Hook Form, Zod, i18next, Recharts,
  and Lucide.
- **API:** supported Python, FastAPI, Pydantic v2, SQLAlchemy 2, and Alembic.
- **Operational data:** PostgreSQL with transactional constraints and immutable
  financial journal records.
- **Async work:** Redis with a worker framework selected during implementation;
  reliable event publication through a transactional outbox.
- **Analytics:** physically separate PostgreSQL database and controlled,
  idempotent incremental data pipeline; BI tool selection is pending.
- **Delivery:** Docker/Compose for development, environment-specific
  configuration, CI, health checks, and documented backup/restore procedures.

No dependencies or infrastructure have been selected by installation or
deployment yet. Compatibility, supported versions, and security advisories must
be checked before adding them.

## Bounded contexts

1. Identity and access (authentication, users, roles, branch scopes).
2. Branch and cash-register operations.
3. Currency catalog and versioned exchange-rate configuration.
4. Transaction execution and document issuance.
5. Cash, bank, and foreign-currency movement ledger.
6. Customer records and data lifecycle.
7. AML alerting and restricted case management.
8. Audit, reporting, and regulatory exports.
9. Notifications and operational integrations.
10. Analytics ingestion and read-only BI.

Each context owns its application/domain rules and exposes explicit interfaces.
Cross-context updates use application services and, where asynchronous,
versioned outbox events; no module may silently edit another context's ledger.

## Financial invariants

- Represent amounts and rates with `Decimal`/database `NUMERIC`; reject binary
  floating-point inputs.
- Persist the exact rate, currency configuration version, and rounding policy
  used by a completed operation.
- Make transaction posting and its balanced journal movements atomic.
- Use database uniqueness, constraints, idempotency keys, and appropriate row
  locks to prevent duplicate execution and overselling.
- Treat posted movements and completed transactions as immutable; corrections
  are separately authorized reversal/correction operations.
- Generate sequential regulatory/document numbers transactionally, with
  concurrency behavior and gap policy reviewed against applicable rules.

## Request and event flow

The versioned API validates and authorizes a command, delegates to an
application service, then commits the transaction, ledger movements, audit
record, and outbox record together. Workers publish/process outbox events
idempotently. Analytics reads only its own database and receives minimized,
appropriately pseudonymized events.

## Deployment and operations

Production topology, identity provider, MFA method, secrets manager, worker,
reverse proxy, monitoring, retention, backups, and recovery objectives require
operational decisions before production deployment. Health/readiness checks
must not disclose secrets or sensitive customer/compliance data.

## Current implementation

The repository currently has no deployed API, UI, database, or infrastructure.
The first code increment is a pure, exact-decimal `Money` value object. See
`IMPLEMENTATION_STATUS.md` for verified scope and open work.
