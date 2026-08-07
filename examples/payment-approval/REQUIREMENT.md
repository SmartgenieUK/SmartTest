# Requirement: REQ-PAY-017

## Intent

Prevent a single actor from causing a payment of £10,000 or more to execute without a distinct authorized person approving it.

## Acceptance rules

1. A GBP payment below £10,000 does not require secondary approval under this rule.
2. A GBP payment of exactly £10,000 requires secondary approval.
3. A GBP payment above £10,000 requires secondary approval.
4. A payment requiring approval must not execute until a distinct, authorized approver records approval.
5. An approval attempt by the initiator or another unauthorized actor is rejected, leaves the payment unapproved and unexecuted, and creates an audit record.
6. If the approval dependency is unavailable or returns an error, the payment remains `approval_pending` and execution is not invoked.
7. Repeating an approval request or approval decision with the same idempotency key does not create a duplicate request, decision, or payment execution.

## Assumptions

- Amounts use exact decimal currency representation; floating-point rounding is not permitted.
- Currency conversion and thresholds for non-GBP payments are outside this requirement.
- Separate fraud, balance, and sanctions controls still apply.
- “Authorized” and “distinct” are supplied by the access-control policy and identity service.

## Failure consequence and risk

Incorrect threshold or fail-open behaviour could permit an unauthorized high-value payment. Risk is **High** because the change affects financial authorization and payment execution.
