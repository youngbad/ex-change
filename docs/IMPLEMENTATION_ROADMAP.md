# Implementation roadmap

This roadmap is staged because the repository has no existing application or
data model. A stage is not complete until its acceptance checks, tests,
authorization, audit, and documentation are reviewed. Keep production claims
limited to verified features.

## Stage 1 — Discovery and foundations

- [x] Inventory repository; record that only a README exists and no in-repo
  application data needs migration.
- [x] Document target boundaries, regulatory validation needs, security
  requirements, proposed data model, and initial architecture decision.
- [x] Add an exact-decimal money value object and focused standard-library tests.
- [ ] Confirm legal/compliance, branch operations, identity, document-number,
  retention, rounding, and deployment decisions with accountable owners.

## Stage 2 — Platform and persistence

- [ ] Select supported dependency versions after compatibility and advisory
  review; establish FastAPI, strict TypeScript/React, PostgreSQL, Alembic,
  configuration, CI, and local development environment.
- [ ] Implement authentication, MFA integration, branch-scoped RBAC, audit
  events, and migration/recovery procedures.
- [ ] Add PostgreSQL integration tests and database-level financial invariants.

## Stage 3 — Exchange operations

- [ ] Implement currency catalog/configuration and approved rate lifecycle.
- [ ] Implement branches, register sessions, inventory ledger, and cash moves.
- [ ] Implement idempotent atomic exchange transactions, sequential documents,
  receipts, reversals, and regulatory register.
- [ ] Verify contention, duplicate requests, insufficient inventory, and
  register-close races.

## Stage 4 — Customers and compliance

- [ ] Implement minimized, protected customer identity and lifecycle.
- [ ] Build versioned, human-reviewed AML rules and traceable decisions after
  legal validation; do not encode unverified threshold behavior.
- [ ] Add restricted alert/case workflows, approvals, and controlled exports.

## Stage 5 — User experience and reporting

- [ ] Build permission-aware operational dashboard and transaction/register
  workflows.
- [ ] Add Polish and English translations, accessibility, responsive layouts,
  localized formatting, and light/dark theme.
- [ ] Define and test reporting/document formulas and export permissions.

## Stage 6 — Analytics and operations

- [ ] Provision isolated analytics database, minimized outbox ETL, reconciled
  idempotent loads, and approved KPI definitions.
- [ ] Add monitoring, alerting, backup/restore drills, retention controls, and
  operational runbooks.
- [ ] Add reviewed container/deployment pipeline and staging-to-production
  approval/rollback process.

## Stage 7 — Release assurance

- [ ] Complete integration, concurrency, authorization, accessibility,
  dependency/container, and security testing.
- [ ] Complete legal, AML, privacy, accounting, and operational review.
- [ ] Reconcile migration/import outcomes and sign off production readiness.

## Exit criteria

No stage implies legal compliance or production readiness by itself. Each
feature must be explicitly marked implemented, tested, and reviewed in
`IMPLEMENTATION_STATUS.md`.
