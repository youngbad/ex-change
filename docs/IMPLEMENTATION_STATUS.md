# Implementation status

Last updated: 2026-11-17

This repository began as an empty scaffold. A checkbox means only the stated
scope is present and locally verified; it does not imply overall system
readiness or legal compliance.

## Stage 1 — Discovery and foundations

- [x] Repository inventory documented: README only; no application, schema,
  external data source, dependency setup, build, or test infrastructure found.
- [x] Proposed architecture, logical database design, regulatory validation
  caveats, security requirements, roadmap, and initial ADR documented.
- [x] Added immutable `Money` value object using `Decimal`, with exact
  same-currency addition/subtraction, currency compatibility checks, and
  rejection of float/non-finite amounts.
- [x] Added focused standard-library unit tests for the value object.
- [ ] Legal, accounting, rounding, document numbering, operational, and
  deployment policies reviewed by accountable professionals.

## Not implemented

No API, UI, persistence, authentication/RBAC, database migrations, exchange
transaction workflow, inventory ledger, rates, branches, register management,
customers, AML case management, document generation, audit service, analytics,
CI/CD, monitoring, backups, or deployment exists yet. The initial domain
primitive does not perform currency conversion, decide currency precision, or
establish regulatory policy.

## Verification

- `python -m unittest discover -s tests -v` — 6 focused `Money` tests pass,
  including a large-value precision regression.
- No baseline repository build, linter, or CI test command exists.
