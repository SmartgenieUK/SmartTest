# Worked Example: Payment Approval Threshold

This language-neutral example applies SmartTest to one fictional requirement:

> Payments of £10,000 or more require secondary approval.

It demonstrates the chain from intent to release evidence:

1. [Requirement](REQUIREMENT.md)
2. [Test plan](TEST_PLAN.md)
3. [Requirement-to-test traceability](TRACEABILITY.md)
4. [Release evidence](RELEASE_EVIDENCE.md)

The evidence identifiers and execution records here are illustrative records for the fictional system. A separate [teaching implementation and test suite](../payment-approval-python/README.md) makes the central policy executable; it does not turn the illustrative release record into an actual payment-system run.

The example deliberately covers the inclusive boundary, approval dependency failure, authorization, duplicates, regression, and operational validation. It remains small enough to copy and adapt.
