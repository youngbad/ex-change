# ADR 0001: Start with a modular monolith

- **Status:** Proposed
- **Date:** 2026-11-17

## Context

The repository contains no application, deployment, or operational data from
which to justify distributed services. The target has tightly coupled
financial invariants: a transaction, its inventory movements, receipt number,
audit event, and outbox event must be committed consistently. Independent
services would add failure and reconciliation modes before scale or ownership
requirements are known.

## Decision

Start with a modular monolith and explicit domain/application interfaces for
identity, branch/register operations, currencies/rates, transactions/ledger,
customers, AML, audit/reporting, and analytics integration. Use PostgreSQL
transactions as the consistency boundary for operational postings. Add a
transactional outbox for reliable downstream events. Keep analytics physically
separate.

## Consequences

- Initial deployment and local development are simpler, with financial writes
  kept atomic.
- Domain ownership and APIs must still be enforced to prevent modules from
  depending on one another's internals.
- Extraction into services remains possible only after measured scaling,
  resilience, or team-ownership needs justify the operational cost.
- This ADR does not select authentication provider, worker/BI products,
  deployment host, or legal/accounting policy.

## Revisit when

Operational evidence shows an independently scalable or separately operated
context, and the team can preserve idempotency, ledger consistency, auditability,
and recovery guarantees across service boundaries.
