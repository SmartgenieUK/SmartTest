# Traceability: REQ-PAY-017

This is an illustrative record for a fictional release.

| Requirement / criterion | Implementation area | Test / evaluation | Result | Evidence |
|---|---|---|---|---|
| Rule 1: below £10,000 does not require approval | Payment policy | PAY-C-01 — £9,999.99 | PASS | EV-COMP-204, fictional commit `7c81e2a` |
| Rule 2: exactly £10,000 requires approval | Payment policy | PAY-C-02 — £10,000.00 | PASS | EV-COMP-204; `>=` to `>` mutation killed by PAY-C-02 |
| Rule 3: above £10,000 requires approval | Payment policy | PAY-C-03 — £10,000.01 | PASS | EV-COMP-204 |
| Invalid values cannot fail open | Money validation / payment policy | PAY-C-04 — malformed, negative, missing | PASS | EV-COMP-204 |
| Rule 4: distinct authorized approval precedes one execution | Approval orchestration / execution guard | PAY-I-01 and PAY-I-05 | PASS | EV-INT-088 |
| Rule 5: unauthorized approval is rejected and audited | Access policy / approval orchestration | PAY-I-02 | PASS | EV-INT-088 |
| Rule 6: dependency failure leaves payment pending and unexecuted | Approval orchestration | PAY-I-03 | PASS | EV-INT-088 |
| Rule 7: duplicate requests and decisions are idempotent | Approval API / idempotency store | PAY-I-04 | PASS | EV-INT-088 |
| Existing payment journeys remain valid | Payment system | PAY-R-01 | PASS | EV-SYS-041 |
| Tests detect material defects | Test suites | Comparison and execution-guard mutations | PASS | EV-MUT-012 |
| Operational validation is defined | Release configuration | Contract review | PASS | EV-OPS-017 |

## Gaps and waivers

None in this fictional release record. A real release would identify unavailable environments, failed evidence, N/A decisions, and waiver authority here.
