# Executable Verification Evidence

## Tested snapshot

- Date: 2026-08-07
- Runtime: CPython 3.12.13
- Dependencies: Python standard library only
- Source version: SmartTest commit `7b40b8ba209ec82252c6af08c4ef93398b2c3b76`
- CI replay: [Verify SmartTest run 4](https://github.com/SmartgenieUK/SmartTest/actions/runs/31210732558), successful in 9 seconds on GitHub-hosted Ubuntu with Python 3.12

## Correct implementation

Command:

```powershell
python -m unittest -v
```

Observed result: 10 tests run, 10 passed.

## Deliberate boundary mutant

Command:

```powershell
$env:SMARTTEST_PAYMENT_MODULE = "payment_approval_mutant"
python -m unittest -v
```

Observed result: 10 tests run, exactly one expected failure:

```text
test_exact_threshold_waits_for_distinct_authorized_approval
Expected: APPROVAL_PENDING
Observed with mutant: EXECUTED
```

The other nine tests passed. This demonstrates sensitivity to the inclusive-boundary defect only.

## Independent audit finding addressed

Before this evidence run, the example asserted only returned status values and did not represent distinct approver identity, audit records, stored pending state, execution blocking or idempotency. The adversarial review classified that mismatch with the linked requirement as high severity. The implementation and tests were extended before these results were recorded.

## Remaining uncertainty

- No real database, identity provider, approval service, audit store or payment executor is used.
- No concurrency or process-restart durability is demonstrated.
- Behavioural agent evaluations are separate from this deterministic Python evidence.
