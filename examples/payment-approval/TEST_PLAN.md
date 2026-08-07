# Test Plan: REQ-PAY-017

## Scope and ownership

- **Intended behaviour:** Require distinct authorized secondary approval for every GBP payment at or above £10,000 and fail closed.
- **Risk:** High — financial authorization boundary.
- **Existing verification:** The fictional system's authoritative `payment-policy` component suite owns threshold decisions; `payment-approval-integration` owns approval orchestration. Strengthen these suites rather than creating a parallel threshold suite.
- **Out of scope:** Non-GBP conversion, fraud, balance, sanctions, and UI styling. Those controls remain subject to their own regression suites.

## Assumptions to verify

| Assumption | Verification |
|---|---|
| Amount uses exact decimal minor units | Inspect money type and add exact-boundary component assertions |
| Execution cannot bypass approval state | Integration test observes the execution dependency |
| Identity policy distinguishes initiator and approver | Authorization integration uses real policy evaluation |
| Duplicate commands are idempotent | Retry the same request and decision with one idempotency key |

## Test obligations

| ID | Given / when / then | Category | Level | Expected evidence |
|---|---|---|---|---|
| PAY-C-01 | Given £9,999.99, when eligibility is evaluated, then secondary approval is not required by this rule | Below boundary | Component | Policy result `approvalRequired=false` |
| PAY-C-02 | Given £10,000.00, when eligibility is evaluated, then secondary approval is required | Exact boundary | Component | Policy result `approvalRequired=true` |
| PAY-C-03 | Given £10,000.01, when eligibility is evaluated, then secondary approval is required | Above boundary | Component | Policy result `approvalRequired=true` |
| PAY-C-04 | Given a malformed, negative, or missing amount, when eligibility is evaluated, then input is rejected rather than treated as below threshold | Invalid input | Component | Explicit validation error |
| PAY-I-01 | Given £10,000 and a distinct authorized approver, when approval is recorded, then the payment executes once | Happy path | Integration | Approval, audit, and single execution observed |
| PAY-I-02 | Given £10,000 awaiting approval, when the initiator or unauthorized actor attempts approval, then approval is rejected and execution is not invoked | Authorization | Integration | Denial, unchanged state, audit record, zero execution calls |
| PAY-I-03 | Given a payment requiring approval, when the approval dependency is unavailable, then state remains `approval_pending` and execution is not invoked | Dependency failure | Integration | Dependency error, retained state, zero execution calls |
| PAY-I-04 | Given a successful approval request or decision, when the same idempotency key is repeated, then no duplicate request, decision, audit outcome, or execution occurs | Duplicate / retry | Integration | Stable identifiers and one execution |
| PAY-I-05 | Given an unapproved £10,000 payment, when an execution command is sent directly, then execution is rejected | Bypass attempt | Integration | Policy denial and audit record |
| PAY-R-01 | Given representative below-threshold and approved payments, when the change is deployed, then existing payment execution and settlement behaviour remains valid | Regression | System | Existing payment journey suite passes |

## Test effectiveness

Mutate the comparison from `>=` to `>`. PAY-C-02 must fail while PAY-C-01 and PAY-C-03 retain their expected outcomes. Remove the approval-state guard from execution; PAY-I-05 must fail. These checks demonstrate that the suite can detect the two central defects.

## Security and non-functional considerations

- Authorization and idempotency are material and covered above.
- Performance testing is N/A for this isolated policy comparison, but approval-service latency remains covered by the service's existing objective.
- Privacy testing is N/A because no new personal data is introduced.
- Audit completeness is required because rejected and accepted approval decisions are security-relevant.

## Operational validation contract

- **Healthy:** threshold-decision counts align with payment amounts; approved high-value payments execute once; no unapproved high-value execution event occurs.
- **Failure:** any `high_value_execution_without_approval` event, elevated approval errors, duplicate executions, or payments stuck beyond the approval service objective.
- **Validation period:** first 60 minutes after deployment and the next business-day payment peak.
- **Rollback/remediation trigger:** immediately disable the changed policy path and stop high-value execution if any unapproved execution is detected; rollback if threshold or duplicate anomalies are confirmed.

## Entry and exit criteria

- **Entry:** requirement approved; authoritative suites identified; exact-money representation confirmed; integration environment available.
- **Exit:** all scenarios pass; both deliberate mutations are detected; traceability is complete; no blocker defect or unexplained missing evidence remains.
- **Independent review:** derive threshold, failure, authorization, and duplicate scenarios from REQ-PAY-017 in a separate review context from implementation.
