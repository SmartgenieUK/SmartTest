# Requirement-to-Test Traceability

Use one row per acceptance criterion and test/evaluation combination when multiple checks provide distinct evidence. Record missing evidence explicitly; do not use an unexplained boolean.

## Context

- **Change / release:**
- **Version / commit:**
- **Environment / configuration:**
- **Evidence date:**

## Traceability matrix

| Requirement | Acceptance criterion | Implementation area | Test / evaluation | Result | Evidence |
|---|---|---|---|---|---|
| REQ-000 | Observable criterion | `path/or/component` | TEST-000 — scenario and level | PASS / FAIL / NOT RUN / WAIVED | Command, report, log, commit, or record |

## Compact example

| Requirement | Acceptance criterion | Implementation area | Test / evaluation | Result | Evidence |
|---|---|---|---|---|---|
| REQ-PAY-017 | £10,000 triggers secondary approval | Payment approval policy | PAY-BOUNDARY-02 — component | PASS | `payment-policy` run, commit `abc123`, 2026-08-07 |
| REQ-PAY-017 | Approval service failure prevents execution | Payment orchestration | PAY-FAIL-01 — integration | NOT RUN | Environment unavailable; release blocked |

## Gaps, exceptions, and waivers

| Requirement / criterion | Missing or failed evidence | Consequence | Decision and authority | Compensating control / remediation |
|---|---|---|---|---|
| | | | | |
