# Executable Traceability: REQ-PAY-017

This record maps the published Python teaching implementation to real test identifiers. It does not claim that in-memory stubs prove production integration.

| Acceptance rule | Implementation area | Executable evidence | Result |
|---|---|---|---|
| Below GBP 10,000 needs no secondary approval | `submit` threshold branch | `test_below_threshold_executes_without_approval_request` | PASS |
| Exactly GBP 10,000 needs approval before execution | Inclusive threshold and execution guard | `test_exact_threshold_waits_for_distinct_authorized_approval` | PASS; deliberate `>=` to `>` mutant detected |
| Above GBP 10,000 needs approval | Approval rejection path | `test_above_threshold_gateway_rejection_does_not_execute` | PASS |
| Approver must be distinct from initiator | Identity check and audit sink | `test_initiator_approval_is_rejected_audited_and_left_pending` | PASS |
| Approver must be authorized | Authorization check and audit sink | `test_unauthorized_approval_is_rejected_audited_and_left_pending` | PASS |
| Dependency failure retains pending state and blocks execution | Exception path, state store and execution spy | `test_dependency_failure_is_audited_pending_and_never_executed` | PASS |
| Repeated request is idempotent | Submit idempotency record | `test_repeated_submit_key_creates_one_approval_request` | PASS |
| Repeated decision is idempotent | Approval idempotency record | `test_repeated_approval_key_creates_one_decision_and_execution` | PASS |
| Invalid amounts cannot fail open | Exact decimal parser | `test_invalid_amounts_cannot_fail_open` | PASS |
| Reused key cannot mask a different request | Idempotency fingerprint | `test_reused_idempotency_key_with_different_payload_is_rejected` | PASS |

## Evidence boundary

The store, gateways and audit sink are in-memory test doubles. These tests prove the service's observable orchestration against those interfaces. They do not prove database durability, identity-provider policy, network contracts, audit retention, or real payment execution behaviour. A production implementation would require separate integration and operational evidence.
