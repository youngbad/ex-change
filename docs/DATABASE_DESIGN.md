# Operational and analytical database design

## Status

No database, schema, migration tool, or production data exists in the inspected
repository. This document is a proposed logical design; it is not an implemented
schema and requires review before migrations are authored.

## Operational database

Use PostgreSQL as the system of record. Store monetary values, rates, and
quantities with explicitly chosen `NUMERIC(precision, scale)` definitions; do
not use floating point. Store instants in UTC and retain explicit business date,
branch timezone, and the legal/rule/configuration version used for date-based
decisions.

Candidate entities and relationships:

- `branch` owns `cash_register` and branch-specific currency/rate settings.
- `user`, `role`, `permission`, and scoped assignments authorize actions by
  branch and operation.
- `currency` and versioned `currency_configuration` define code, names,
  precision, and active intervals; branch support is separately effective-dated.
- `exchange_rate` records pair, side, value, branch scope, validity interval,
  author, approval, and immutable history.
- `transaction` records parties/roles, branch, register, cashier, contract and
  settlement times, currencies, amounts, exact applied rate, settlement type,
  idempotency key, status, and references to reversal/correction operations.
- `document` stores unique sequential number, versioned template, issue time,
  and a transaction reference; minimize copies of personal data.
- `ledger_entry` is append-only and records each signed account/currency
  movement, operation, posting time, actor, and correction reference. The
  transaction and all entries commit atomically.
- `register_session` and `cash_movement` model open/active/closing/closed
  lifecycle, opening/closing counts, deposits, withdrawals, transfers, and
  adjustments as explicit ledger-backed operations.
- `customer` and restricted `customer_identity` separate minimal operational
  references from sensitive identity data, with encryption/access and retention
  policies to be defined.
- `aml_rule_version`, `aml_decision`, `aml_alert`, and `aml_case` preserve
  evaluation inputs and decisions with restricted access.
- `audit_event` and `outbox_event` are written in the same commit as the
  protected business change; consumers are idempotent.

## Integrity and concurrency

Use foreign keys, unique constraints for idempotency and document numbers,
check constraints for valid states/signs, and indexes aligned with authorized
branch/date searches. Transaction execution must lock the relevant inventory
accounts or use an equivalent serializable/optimistic strategy with retries.
Enforce sufficient-balance checks in the same database transaction as posting.
Application code alone must not be the only guard against overselling.

Posted ledger rows and completed transactions are not updated/deleted through
normal application paths. Reversals post offsetting entries and link to the
original operation. Document-number allocation and any permitted gaps require
legal/business approval.

## Migrations and data preservation

Use reviewed, versioned Alembic migrations with safe expand/contract sequencing
where applicable. Rehearse upgrades and rollback/restore against backups.
No destructive or data-transforming migration is currently proposed because no
source database exists. Any future import requires reconciliation and an
approved mapping/retention plan.

## Analytics database

Create a separate database and service account. Load minimized, pseudonymized,
versioned events from the outbox into dimensions (date, time, currency, branch,
employee, transaction type) and facts (transactions, cash movements,
inventory snapshots, rates, register sessions, AML metrics where authorized).
Do not copy raw customer identity, AML case notes, or unnecessary personal data.
Define freshness, deduplication keys, reconciliation, retention, and access
controls before enabling BI.

## Open design inputs

Precision and rounding policy by currency/operation, ledger account model,
transaction state machine, document-number rules, isolation/concurrency
strategy, retention/legal-hold policy, and analytical definitions must be
approved before schema implementation.
