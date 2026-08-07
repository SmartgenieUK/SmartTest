# Executable Payment-Approval Example

This standard-library-only Python example turns the documented payment requirement into executable evidence. It is teaching code, not DevGenie product code or a real payment integration.

Requirement: payments of £10,000 or more require approval by a distinct authorized person before execution. The suite covers the inclusive boundary, exact decimal validation, initiator and unauthorized rejection, retained pending state, audit evidence, blocked execution, dependency failure, and request and decision idempotency.

## Prerequisite

Use Python 3.8 or later. The example has no third-party package dependency.

```powershell
python --version
```

On Windows, use `py -3` instead of `python` in the commands below when the Python launcher is installed but `python` is not on `PATH`.

## Run the correct implementation

From this directory:

```powershell
python -m unittest -v
```

Expected result: ten tests pass.

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

Expected result: `test_exact_threshold_waits_for_distinct_authorized_approval` fails because the mutant executes the payment at exactly £10,000. The other nine tests pass. This is narrow mutation evidence that the exact-boundary test can expose the intended defect; it is not proof that the whole system is correct.

## Trace it back to intent

The fuller, language-neutral evidence chain remains in the [documented payment-approval example](../payment-approval/README.md). Compare its [requirement](../payment-approval/REQUIREMENT.md) and [test plan](../payment-approval/TEST_PLAN.md) with this suite's [real traceability record](TRACEABILITY.md) and [verification evidence](VERIFICATION.md).
