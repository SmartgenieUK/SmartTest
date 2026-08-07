# Requirement-to-Test Traceability

Use one row per acceptance criterion and test/evaluation combination when multiple checks provide distinct evidence. Record missing evidence explicitly; do not use an unexplained boolean.

## Context

- **Change / release:**
- **Version / commit:**
- **Authoritative requirement / design decision:**
- **Environment / configuration:**
- **Evidence date:**
- **Evidence owner / reviewer:**

## Traceability matrix

| Requirement | Acceptance criterion | Design decision | Implementation area | Test / evaluation | Result | Evidence provider | Evidence record |
|---|---|---|---|---|---|---|---|
| REQ-000 | Observable criterion | Decision or rationale reference | `path/or/component` | TEST-000 — scenario and level | PASS / FAIL / NOT RUN / WAIVED | CI, test runner, reviewer, scanner, or service | Command, timestamp, environment, immutable URL/path, digest, commit, or signed record |

## Compact example

| Requirement | Acceptance criterion | Design decision | Implementation area | Test / evaluation | Result | Evidence provider | Evidence record |
|---|---|---|---|---|---|---|---|
| REQ-PAY-017 | £10,000 triggers secondary approval | Inclusive threshold, ADR-017 | Payment approval policy | PAY-BOUNDARY-02 — component | PASS | CI test runner | `payment-policy` run, 2026-08-07T10:15Z, commit `abc123`, report digest `sha256:...` |
| REQ-PAY-017 | Approval service failure prevents execution | Fail closed, ADR-017 | Payment orchestration | PAY-FAIL-01 — integration | NOT RUN | Release reviewer | Environment unavailable; release blocked; decision record `REL-442` |

## Gaps, exceptions, and waivers

| Requirement / criterion | Missing or failed evidence | Consequence | Decision and authority | Compensating control / remediation |
|---|---|---|---|---|
| | | | | |
