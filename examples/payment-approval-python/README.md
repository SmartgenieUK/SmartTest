# Executable Payment-Approval Example

This zero-dependency Python example turns the documented payment threshold into executable evidence. It is teaching code, not DevGenie product code.

Requirement: payments of £10,000 or more require authorized secondary approval. The suite covers below, exactly at, and above the inclusive boundary; dependency failure; unauthorized approval; and duplicate decisions.

## Run the correct implementation

From this directory:

```powershell
python -m unittest -v
```

Expected result: six tests pass.

## Demonstrate that the boundary test can fail

`payment_approval_mutant.py` deliberately changes `>=` to `>`. Run the same suite against it:

```powershell
$env:SMARTTEST_PAYMENT_MODULE = "payment_approval_mutant"
python -m unittest -v
Remove-Item Env:SMARTTEST_PAYMENT_MODULE
```

On a POSIX shell:

```sh
SMARTTEST_PAYMENT_MODULE=payment_approval_mutant python -m unittest -v
```

Expected result: `test_exact_threshold_requires_authorized_secondary_approval` fails because the mutant bypasses the approval gateway at exactly £10,000. The other five tests pass. This is narrow mutation evidence that the exact-boundary test can expose the intended defect; it is not proof that the whole system is correct.

## Trace it back to intent

The fuller, language-neutral evidence chain remains in the [documented payment-approval example](../payment-approval/README.md). Compare its [requirement](../payment-approval/REQUIREMENT.md), [test plan](../payment-approval/TEST_PLAN.md), and [traceability](../payment-approval/TRACEABILITY.md) with this suite.
