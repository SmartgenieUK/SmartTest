# AI Code Release Checklist

Use this for behaviour-bearing AI-assisted changes. Mark each item **done**, **N/A with rationale**, or **waived with approver, consequence, compensating control, and remediation condition**. Apply depth in proportion to risk; never omit a check silently.

## Intent

- [ ] The requirement and intended user or business outcome are identified.
- [ ] Acceptance criteria are explicit and observable enough to test.
- [ ] Material assumptions, dependencies, and ambiguous decisions are recorded.
- [ ] Verification and validation obligations are distinguished where relevant.

## Test design

- [ ] Existing authoritative tests were inspected before new tests were created.
- [ ] Testing has been explicitly addressed; “tests pass” is not vacuously true.
- [ ] Happy paths and exact acceptance behaviour are covered.
- [ ] Relevant boundaries, invalid inputs, missing inputs, and negative cases are covered.
- [ ] Dependency failures, timeouts, partial failures, retries, or recovery are considered where relevant.

## Implementation verification

- [ ] Required tests or evaluations exist at the lowest effective test level.
- [ ] Assertions check observable behaviour and are strong enough to detect a meaningful defect.
- [ ] Applicable build, compiler, type, lint, and static checks pass.
- [ ] Test evidence identifies the tested version, configuration, data, result, and execution context as needed for reproduction.

## Integration, security, and non-functional behaviour

- [ ] Material integration assumptions were verified beyond mocks.
- [ ] Contracts, schemas, persistence, transactions, and compatibility were checked where affected.
- [ ] Authentication, authorization, privacy, input handling, and other security concerns were tested where applicable.
- [ ] Relevant performance, resilience, accessibility, compatibility, observability, and operability obligations were addressed.

## Regression and change impact

- [ ] Blast radius was traced beyond edited lines to consumers, shared contracts, callbacks, middleware, observers, and events.
- [ ] Configuration, feature flags, migrations, deployment, and operational dependencies were considered.
- [ ] Focused tests and proportionate broader regression checks pass.
- [ ] Defect fixes include evidence that would have detected the defect and protects the corrected behaviour.

## Independent review

- [ ] Requirement interpretation, implementation, tests, and approval do not rely solely on one reasoning context where consequence warrants independence.
- [ ] Test quality was reviewed for missing scenarios, weak assertions, excessive mocking, false positives, and implementation coupling.
- [ ] Tests were shown capable of failing through review, mutation, fault injection, or another proportionate method where assurance warrants it.

## Release and operation

- [ ] Requirement-to-test traceability identifies results and supporting evidence.
- [ ] Blocking failures, missing evidence, accepted exceptions, and waivers are explicit.
- [ ] Healthy production signals and the intended validation period are defined for production-affecting changes.
- [ ] Degradation or failure signals and rollback or remediation triggers are known.

## Decision

**Decision:** PASS / FAIL / ESCALATE / WAIVED

**Evidence reviewed:**

**N/A decisions and rationale:**

**Waivers and authority:**

**Reviewer and date:**
