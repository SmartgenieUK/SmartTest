# Test Plan: `<change or requirement ID>`

Keep this plan proportional to consequence. Delete prompts only after answering them. Use **N/A — rationale** when a concern was considered but does not apply.

## 1. Intent and scope

- **Change / requirement:**
- **Owner:**
- **Version / change reference:**
- **Intended behaviour and user outcome:**
- **Acceptance criteria:**
- **In scope:**
- **Out of scope:**
- **Risk / consequence if wrong:** Low / Medium / High — rationale

## 2. Existing verification ownership

Identify where this behaviour is already authoritatively verified before adding tests.

| Existing test/evaluation | Behaviour owned | Strengthen, retain, replace, or N/A | Rationale |
|---|---|---|---|
| | | | |

## 3. Assumptions and dependencies

| Assumption or dependency | How it could be wrong | How it will be verified |
|---|---|---|
| | | |

## 4. Test obligations

Give each scenario a stable ID. Select the lowest test level that provides meaningful evidence; add higher-level evidence where real boundaries matter.

| ID | Scenario: given / when / then | Category | Test level | Expected evidence |
|---|---|---|---|---|
| TP-01 | | Happy path | | |
| TP-02 | | Boundary | | |
| TP-03 | | Negative / invalid | | |
| TP-04 | | Failure / recovery | | |

Consider, as applicable:

- exact, below, and above boundaries;
- missing, malformed, duplicate, repeated, unauthorized, and cancelled actions;
- dependency errors, timeouts, retries, partial failure, ordering, concurrency, and rollback;
- state transitions and invariants.

## 5. Permissions and security

- **Authentication / authorization scenarios:**
- **Input, secrets, data sensitivity, and privacy concerns:**
- **Threats or abuse cases requiring evidence:**
- **N/A rationale, if applicable:**

## 6. Integration and contracts

- **Real dependencies and interfaces affected:**
- **Schemas, protocols, transactions, events, compatibility, and idempotency:**
- **What cannot be proved with mocks:**
- **Required environment or test data:**

## 7. Regression blast radius

| Affected behaviour, consumer, or contract | Why plausibly affected | Required regression evidence |
|---|---|---|
| | | |

Include shared code, callbacks, middleware, observers, persistence, configuration, feature flags, deployment, security boundaries, and operational dependencies where relevant.

## 8. Non-functional and operational validation

- **Performance / scale:**
- **Resilience / recoverability:**
- **Accessibility / compatibility:**
- **Observability / operability / maintainability:**
- **Healthy production signals and validation period:**
- **Failure or degradation signals:**
- **Rollback or remediation trigger:**
- **N/A rationale, if applicable:**

## 9. Evidence and completion

- **Expected commands, reports, logs, traces, screenshots, or evaluation records:**
- **Version, configuration, data, and dependency context to retain:**
- **Independent derivation or review required:**
- **Entry criteria:**
- **Exit criteria:**
- **Explicit exclusions and rationale:**
- **Known evidence that cannot currently be obtained:**
