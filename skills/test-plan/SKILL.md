---
name: test-plan
description: Derive risk-based verification obligations from requirements before implementation or material behavioural change. Use when planning a feature, change, migration, or fix; when acceptance criteria need test scenarios; or before generating tests.
---

# Test Plan

## Purpose

Derive verification obligations from intent before implementation or before a material behavioural change. Produce a plan that challenges the requirement rather than tests that merely agree with a proposed implementation.

## Use when

- Planning a feature, rule change, migration, or material configuration change.
- Turning requirements or acceptance criteria into test scenarios.
- Deciding whether existing verification should be strengthened.
- Establishing evidence obligations before asking an agent to implement tests.

Do not use this skill to judge an already-written test suite; use [test-review](../test-review/SKILL.md).

## Inspect

Read, in this order:

1. Requirement, user outcome, acceptance criteria, and relevant design decisions.
2. Repository instructions and risk or release policies.
3. Existing tests, test helpers, fixtures, and ownership conventions for the behaviour.
4. Relevant implementation and contracts only to understand boundaries and consumers, not to redefine intent.
5. Integration, security, operational, and historical defect evidence where applicable.

State what could not be inspected.

## Procedure

1. Restate the intended observable behaviour without implementation detail.
2. Identify ambiguities, assumptions, and acceptance criteria. Stop if a material ambiguity prevents a reliable expected result.
3. Locate authoritative existing verification. Prefer strengthening it over creating overlapping test ownership.
4. Derive happy-path scenarios.
5. Derive exact, below, above, empty, missing, malformed, and extreme boundaries as applicable.
6. Derive invalid, unauthorized, duplicate, repeated, cancellation, and state-transition scenarios as applicable.
7. Derive dependency failure, timeout, retry, partial-failure, ordering, concurrency, recovery, and rollback scenarios as applicable.
8. Identify permissions, privacy, abuse, and other security obligations.
9. Identify real integration assumptions that mocks cannot prove.
10. Trace plausible regression impact through consumers, contracts, persistence, configuration, and operations.
11. Consider proportionate non-functional and production validation obligations.
12. Assign the lowest effective test level to each scenario; add higher-level evidence only where it proves a distinct boundary or outcome.
13. Define expected, reproducible evidence and any required independent derivation or review.
14. Record exclusions and N/A decisions with rationale.

Use the [Test Plan Template](../../templates/TEST_PLAN_TEMPLATE.md) when writing a repository artefact.

## Required output

Return:

- scope, intended behaviour, acceptance criteria, and risk;
- existing verification located and its ownership;
- assumptions and unresolved ambiguities;
- test obligations with scenario ID, expected observable outcome, category, test level, and evidence;
- integration, security, regression, non-functional, and operational obligations as applicable;
- explicit exclusions or N/A decisions with rationale;
- unavailable evidence and independent review needs.

Do not implement code or tests unless separately asked.

## Stop or escalate

Escalate when:

- acceptance criteria materially conflict or do not define a decidable expected result;
- required evidence depends on unavailable access, data, environment, or authority;
- security, regulatory, financial, or safety consequence requires a risk decision outside the task;
- no authoritative owner can be determined and adding tests would create conflicting suites;
- the requested plan would knowingly omit a plausible high-consequence failure mode.

## Anti-patterns

- Generate tests before deriving scenarios.
- Treat every conceivable case as mandatory regardless of risk.
- Duplicate tests without locating existing ownership.
- Treat code coverage, test count, or a green pipeline as requirement evidence.
- Test implementation details when observable behaviour is available.
- Use mocks as proof of a real integration.
- Hide exclusions behind silence or unexplained N/A labels.

## Compact example

For “payments of £10,000 or more require secondary approval”:

| ID | Scenario | Level | Expected evidence |
|---|---|---|---|
| PAY-01 | £9,999.99 does not require secondary approval | Component | Policy assertion passes |
| PAY-02 | £10,000 requires secondary approval | Component | Inclusive-boundary assertion passes |
| PAY-03 | Approval service unavailable prevents execution | Integration | Real failure response leaves payment unexecuted |
| PAY-04 | Unauthorized approver is rejected | Integration | Authorization decision and audit record verified |

Also establish duplicate-request behaviour, regression consumers, healthy production signals, and rollback triggers if this policy will affect production.
