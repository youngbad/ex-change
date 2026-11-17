# Regulatory and compliance requirements

## Important limitation

This document records engineering considerations derived from the project
requirements; it is not legal advice, an applicability assessment, or evidence
of compliance. Qualified Polish legal counsel and the obliged entity's
compliance officer must validate the current laws, regulations, GIIF guidance,
reporting procedures, document fields, thresholds, retention periods, and
effective dates before these rules are implemented or used operationally.

## Requirements to validate

- Foreign-exchange activity, office recordkeeping, transaction evidence, and
  record numbering under applicable Polish law and regulations.
- AML/CFT customer due diligence, beneficial-owner identification, monitoring,
  internal escalation, reporting, and confidentiality requirements.
- GDPR/RODO lawful basis, purpose limitation, data minimization, access,
  correction, retention, deletion restrictions, and data-subject workflows.
- Accounting, fiscal/document, evidentiary, and record-retention obligations.
- Branch and register controls, reconciliation, and audit evidence.

The legal sources and provisions cited in the project brief have not been
independently verified for current text or applicability. Maintain a source
register with the authoritative publication, provision, effective date,
reviewer, and implementation/version reference before encoding a legal rule.

## AML rule design constraints

- Distinguish customer due-diligence triggers from statutory reporting
  obligations; one must not be inferred from the other.
- Keep threshold amounts, currency conversion methodology, applicable-date
  rules, and rule versions configurable and approved.
- If an EUR threshold conversion is adopted, preserve the source, rate, date,
  rule version, and calculation with each decision; obtain legal approval for
  the applicable NBP rate and transaction-date interpretation.
- Do not aggregate unrelated operations to create a statutory reporting
  obligation unless the validated rule requires it. Related-operation patterns
  may separately trigger human suspicious-activity review.
- Permit suspicion- and circumstance-based escalation independently of a
  numeric threshold. The software must support, not replace, qualified
  decisions and internal procedures.
- Restrict AML cases and reporting information to explicitly authorized roles;
  avoid disclosure that could compromise an investigation.

## Documents and records

Document templates and required fields must be versioned and approved by
qualified reviewers. Preserve the exact data/rate used for a completed
transaction, document issue time, actor, and subsequent correction history.
Retention and legal holds must be configurable only under a reviewed policy;
never assume deletion is appropriate merely because a customer record is
inactive.

## Release gate

No feature should be labeled legally compliant or certified without formal
review and sign-off. Capture each rule's owner, authoritative source, effective
period, tests, and approval evidence in a controlled compliance register before
production use.
