# DevGenie Testing Doctrine — Version 2

**Status:** Draft v2  
**Purpose:** Methodology-first testing doctrine for AI Code Engineering  
**Scope:** DevGenie methodology first; product enforcement second  
**Principle:** External testing tools strengthen our engineering discipline. They do not define it.

**Version 2 focus:** Preserve the original assurance model while making testing obligations harder to omit in day-to-day AI-assisted engineering. V2 adds explicit rules for testing-addressed decisions, existing-test ownership, change-impact verification, causal debugging, and operational validation.

---

# 1. Purpose

AI-assisted software development changes the speed and volume of code production, but it does not remove the engineering obligations that made disciplined software delivery reliable.

If anything, AI increases the need for them.

The DevGenie Testing Doctrine defines the minimum level of testing discipline expected throughout the software development lifecycle. It deliberately begins with established SDLC testing principles before introducing AI-specific controls.

The doctrine exists to ensure that:

- testing begins before code is written;
- every important requirement is demonstrably verified;
- tests are designed to find defects, not merely to produce green pipelines;
- verification and validation remain distinct;
- test evidence is traceable, reproducible, and reviewable;
- AI-generated code is not trusted simply because AI-generated tests agree with it;
- external tools supplement, rather than replace, engineering judgement and internal discipline;
- release decisions are based on evidence.

The objective is not maximum test volume.

The objective is **sufficient, relevant, independent evidence that the software is fit for its intended purpose**.

---

# 2. Core Doctrine

## 2.1 Quality is a lifecycle responsibility

Testing is not a phase performed after implementation.

Every stage of the lifecycle creates an engineering artefact that must be capable of being challenged and verified.

```text
Requirement
    ↓
Design
    ↓
Implementation
    ↓
Component
    ↓
Integration
    ↓
System
    ↓
Acceptance
    ↓
Release
    ↓
Operation
```

At every stage DevGenie asks:

> What could be wrong here, and what evidence would demonstrate that it is right?

---

## 2.2 A green pipeline is not proof of correctness

A system may:

- compile successfully;
- pass all unit tests;
- satisfy static analysis;
- contain no known vulnerabilities;
- pass code review;

and still implement the wrong behaviour.

DevGenie therefore distinguishes between:

### Verification

**Did we build the thing correctly?**

Examples:

- Does the implementation conform to the design?
- Does the function behave according to its contract?
- Does the API honour its schema?
- Does the component handle failures correctly?

### Validation

**Did we build the correct thing?**

Examples:

- Does the implemented behaviour satisfy the actual requirement?
- Does the workflow solve the intended user problem?
- Are the acceptance criteria met?
- Is the resulting system fit for its intended operational context?

Both are required.

---

# 3. Testing Begins With Requirements

A requirement that cannot be tested is not ready for implementation.

Before implementation begins, significant requirements should be examined for:

- clarity;
- observability;
- measurable acceptance criteria;
- boundary conditions;
- invalid conditions;
- failure behaviour;
- security implications;
- operational implications;
- dependencies and assumptions.

Where practical, requirements should identify the evidence required to prove their satisfaction.

Example:

```text
REQ-PAY-017

Payments of £10,000 or more require secondary approval.

Acceptance evidence:
- £9,999.99 does not trigger secondary approval
- £10,000 triggers secondary approval
- £10,000.01 triggers secondary approval
- approval failure prevents payment execution
```

This turns testing into a consequence of the requirement rather than an afterthought.

---

# 4. Traceability

For material behaviour, DevGenie should maintain traceability across the engineering chain.

```text
Requirement
    ↓
Design decision
    ↓
Implementation
    ↓
Test
    ↓
Execution result
    ↓
Evidence
```

A mature implementation should be able to answer questions such as:

- Which tests verify REQ-042?
- Which requirement justified this code?
- Which implementation components realise this requirement?
- Which requirements currently have no test evidence?
- Which tests failed after this change?
- Which release contained the verified implementation?
- What evidence supported the release decision?

Traceability is not documentation theatre.

It is how DevGenie distinguishes **tested code** from **verified intent**.

---

# 5. The Testing Pyramid Still Matters

AI does not repeal software economics.

The majority of behavioural verification should occur as low in the test stack as is reasonably possible.

```text
                 /\
                /  \
               / E2E\
              /------\
             / System \
            /----------\
           / Integration\
          /--------------\
         / Component/API  \
        /------------------\
       /     Unit Tests     \
      /______________________\
```

Lower-level tests should generally be:

- faster;
- more deterministic;
- easier to diagnose;
- cheaper to execute;
- narrower in scope.

Higher-level tests are necessary but should not become the primary mechanism for detecting basic implementation defects.

DevGenie should resist the common AI-generated-code failure mode of creating many expensive end-to-end tests while neglecting precise lower-level verification.

---

# 6. Required Test Levels

Not every change requires every test type.

However, every behaviour-bearing change must explicitly address testing. Silence is not evidence that no testing is required.

The required test scope should be proportional to the behaviour, risk, architecture, and impact of the change.

However, the methodology recognises the following distinct test levels.

## 6.0 Testing Must Be Addressed

For every material change, DevGenie must reach one of two explicit conclusions:

1. **Verification evidence is required**, and the required tests or other checks are identified; or
2. **No executable test is appropriate**, with a recorded rationale and an alternative verification method where necessary.

For behaviour-bearing changes, “no tests” is not a default and should be exceptional.

A gate such as:

```text
Tests pass
```

is insufficient because it can be vacuously true when no relevant tests exist.

The stronger gate is:

```text
Testing addressed
```

which requires the workflow to establish what evidence should exist and whether it exists.

Examples of changes that may legitimately require non-test verification include:

- documentation-only changes;
- formatting-only changes;
- some static configuration or scaffolding changes;
- generated metadata with deterministic validation elsewhere.

Even in such cases, the decision must be explicit.


## 6.1 Unit Testing

Verify the smallest meaningful units of behaviour in isolation.

Unit tests should cover, where relevant:

- expected behaviour;
- boundary conditions;
- invalid inputs;
- null or missing values;
- error paths;
- state transitions;
- exceptional conditions;
- calculation rules;
- authorization decisions;
- invariants.

Unit tests should not merely mirror implementation structure.

They should verify externally meaningful behaviour.

---

## 6.2 Component Testing

Verify a service, module, library, class cluster, or bounded component as a coherent unit.

Typical concerns:

- public contracts;
- persistence behaviour;
- internal collaboration;
- configuration;
- serialization;
- dependency handling;
- component-level failure behaviour.

---

## 6.3 Contract and API Testing

Interfaces must be tested independently of individual implementations.

Examples:

- request/response schemas;
- API status behaviour;
- version compatibility;
- event schemas;
- message contracts;
- database contracts;
- service boundaries.

Contract testing is particularly important in AI-assisted development because an agent may make a locally reasonable change that silently breaks a consumer.

---

## 6.4 Integration Testing

Verify that independently developed components behave correctly together.

Integration tests should specifically challenge assumptions about:

- data formats;
- protocols;
- authentication;
- authorization;
- retries;
- timeouts;
- transaction boundaries;
- ordering;
- idempotency;
- dependency failure;
- network behaviour;
- schema compatibility.

Mocks must not become a substitute for validating real integration behaviour.

---

## 6.5 System Testing

Verify the complete system against intended system behaviour.

System testing should cover:

- important user journeys;
- business workflows;
- cross-component behaviour;
- system-level failures;
- data integrity;
- authorization boundaries;
- externally visible behaviour.

---

## 6.6 Acceptance Testing

Acceptance testing establishes whether the system satisfies the intended business or user outcome.

It should be derived from requirements and acceptance criteria rather than implementation details.

Acceptance should answer:

> Would the intended stakeholder consider this requirement satisfied?

---

## 6.7 Regression Testing

Every defect fix and material behaviour change should consider regression protection.

A defect should normally result in:

1. reproduction;
2. diagnosis;
3. correction;
4. a test that would have detected the defect;
5. regression verification.

A defect that can silently return is not fully resolved.

---

# 7. Positive Tests Are Not Enough

Testing must actively attempt to invalidate assumptions.

For meaningful behaviours, test design should consider:

- happy path;
- lower boundary;
- upper boundary;
- just below boundary;
- exact boundary;
- just above boundary;
- invalid input;
- missing input;
- malformed input;
- unauthorized access;
- duplicate action;
- repeated action;
- dependency unavailable;
- dependency timeout;
- partial failure;
- retry behaviour;
- concurrency;
- ordering;
- recovery;
- cancellation;
- rollback;
- extreme volume;
- resource exhaustion where relevant.

The applicable set depends on the behaviour under test.

The doctrine does not require meaningless test multiplication.

It requires **deliberate consideration of failure space**.

---

# 8. Test Design Before Test Generation

AI can generate tests quickly.

That does not mean generated tests are good tests.

Before test implementation, DevGenie should reason about the required test design:

```text
Requirement
    ↓
Expected behaviour
    ↓
Failure modes
    ↓
Boundaries
    ↓
Test scenarios
    ↓
Test implementation
```

The scenario set matters more than the number of test functions.

For behaviour-bearing work, material test scenarios should be identified during planning rather than invented only after implementation. A useful scenario statement includes:

- the requirement or acceptance criterion being covered;
- relevant preconditions or input;
- the action or behaviour under test;
- the expected observable outcome;
- the appropriate test level;
- any required evidence or environment that makes the result meaningful.

A simple form is:

```text
Requirement / Acceptance Criterion
        ↓
Given / Input
        ↓
When / Action
        ↓
Then / Expected observable outcome
        ↓
Evidence
```

A hundred tests covering the same happy path provide less assurance than five well-designed tests covering materially different failure modes.

---

# 9. Existing Test Ownership

Before creating new tests for changed behaviour, DevGenie should first identify where that behaviour is already verified.

The preferred order is:

```text
Locate existing verification
        ↓
Can an authoritative existing test be strengthened?
        ↓
YES → strengthen it
NO  → add the smallest appropriate new test
```

Possible verification strategies include:

- reproduce through an existing failing test;
- strengthen an existing test whose assertion is too weak;
- add a focused new test where no suitable test exists;
- add characterisation coverage before changing poorly understood legacy behaviour;
- explicitly record why executable testing is unsuitable and what replacement evidence will be used.

This discipline prevents test-suite fragmentation and reduces the common AI-assisted failure mode of continuously adding overlapping test files without understanding existing test ownership.

The goal is not fewer tests.

The goal is a coherent, authoritative verification structure.

---

# 10. Independence of Verification

A system should not be considered independently verified merely because the same reasoning process produced:

- the requirement interpretation;
- the implementation;
- the tests;
- the review;
- the approval.

This is especially important with AI agents.

A dangerous pattern is:

```text
Agent reads requirement
    ↓
Agent writes implementation
    ↓
Agent writes tests for its implementation
    ↓
Agent reviews its own implementation
    ↓
Agent reports success
```

The implementation and tests may share the same misunderstanding.

Where assurance warrants it, DevGenie should introduce independent derivation.

For example:

```text
                   Contract
                  /   |    \
                 /    |     \
                ↓     ↓      ↓
Implementation   Test      Review
   Agent        Agent      Agent
                |
                ↓
        deterministic execution
```

Independence may be created using:

- separate agent contexts;
- independently derived test scenarios;
- deterministic tools;
- human review;
- external analysis tools;
- mutation testing;
- golden datasets;
- reference implementations.

Independence should be proportional to consequence.

---

# 11. Tests Must Be Capable of Failing

A test suite that cannot detect meaningful defects creates false assurance.

DevGenie should therefore assess test effectiveness, not merely test execution.

Useful techniques include:

- mutation testing;
- deliberate fault injection;
- negative test execution;
- test review;
- coverage analysis;
- boundary mutation;
- contract mutation.

Example:

Requirement:

```text
amount >= 10000 requires approval
```

Implementation mutation:

```text
>=
```

changed to:

```text
>
```

If the test suite still passes, the suite has failed to protect the requirement boundary.

This is stronger evidence than simply reporting that the existing tests passed.

---

# 12. Coverage Is Multi-Dimensional

Code coverage is useful but insufficient.

DevGenie should distinguish several forms of coverage.

## 12.1 Code Coverage

What implementation paths were executed?

Examples:

- line coverage;
- branch coverage;
- condition coverage.

## 12.2 Requirement Coverage

Which requirements have verification evidence?

```text
REQ-001 → PASS
REQ-002 → PASS
REQ-003 → NO TEST
REQ-004 → PASS
```

## 12.3 Scenario Coverage

Which expected and failure scenarios have been exercised?

## 12.4 Interface Coverage

Which contracts and integration boundaries have been tested?

## 12.5 Risk Coverage

Have the behaviours with the greatest potential impact received proportionate assurance?

DevGenie should avoid treating a single percentage as a proxy for quality.

---

# 13. Test Data Is an Engineering Asset

Test quality depends heavily on test data.

Test data should be:

- representative;
- deterministic where required;
- reproducible;
- privacy-safe;
- versioned where appropriate;
- capable of exercising boundary conditions;
- capable of exercising failure conditions.

For AI and data-intensive systems, important datasets may need explicit lineage and versioning.

Where production data is used or derived, privacy, confidentiality, regulatory, and masking requirements must be satisfied.

---

# 14. Entry and Exit Criteria

Testing stages should have explicit criteria.

Progression should not depend solely on subjective statements such as:

> It looks ready.

Example integration-test entry criteria:

```text
✓ build succeeds
✓ required unit tests pass
✓ critical component tests pass
✓ relevant contracts are defined
✓ required test environment is available
✓ blocking implementation defects are resolved
```

Example integration-test exit criteria:

```text
✓ required scenarios executed
✓ critical integration behaviours verified
✓ no unresolved blocker defects
✓ required regression tests pass
✓ evidence captured
```

DevGenie gates should ultimately operationalise these criteria.

---

# 15. Causal Debugging Discipline

For non-trivial defects, DevGenie should not treat a working patch as proof that the root cause is understood.

The preferred debugging sequence is:

```text
Reproduce
   ↓
Trace the causal chain
   ↓
Audit assumptions
   ↓
Form a hypothesis
   ↓
Make an independent prediction
   ↓
Verify the prediction
   ↓
Create or strengthen the failing regression test
   ↓
Apply the smallest root-cause correction
   ↓
Run focused verification
   ↓
Run broader regression
   ↓
Review the resulting evidence
```

A strong hypothesis should predict something observable beyond “this patch makes the failure disappear.”

If the proposed causal explanation makes an independent prediction and that prediction is false, the explanation is incomplete even if the patch appears to work.

This protects against symptom fixes, accidental fixes, and AI-generated explanations that merely rationalise the changed code after the fact.

The regression test should protect the corrected behaviour rather than merely preserve the chosen implementation.

---

# 16. Defects Have a Lifecycle

A failed test is not merely a red icon.

Material defects should be traceable engineering events.

A defect record may include:

```text
DEF-0029

Detected by: IT-041
Requirement: REQ-022
Change: CR-148
Severity: High
Failure mode: Boundary validation
Root cause: Incorrect interpretation of inclusive threshold
Correction: Validation operator corrected
Regression test: UT-097
Verification: PASS
```

Over time, defect data should enable engineering learning.

Examples:

```text
Ambiguous requirements              23%
Integration assumptions             17%
Boundary-condition errors           12%
Incorrect API usage                  9%
Concurrency defects                  6%
...
```

Testing should improve the development system, not merely the current release.

---

# 17. Non-Functional Testing Is First-Class

Functional correctness alone does not make software production-ready.

Depending on system context, DevGenie should explicitly consider:

- security;
- performance;
- scalability;
- resilience;
- reliability;
- recoverability;
- accessibility;
- compatibility;
- privacy;
- observability;
- operability;
- maintainability;
- deployment behaviour;
- upgrade and rollback behaviour.

These requirements should be testable where material.

---

# 18. Security Testing

Security must not depend on one scanner.

The methodology should combine appropriate layers such as:

- secure design review;
- threat modelling;
- authorization testing;
- authentication testing;
- input validation;
- secrets detection;
- dependency analysis;
- static application security testing;
- dynamic security testing;
- infrastructure configuration checks;
- adversarial testing where justified.

External tooling can provide powerful evidence.

Responsibility for security assurance remains internal.

---

# 19. Testing AI-Enabled Software

Traditional testing remains the foundation.

AI-enabled behaviour introduces additional concerns because outputs may be probabilistic, model-dependent, context-dependent, and difficult to specify as exact expected values.

Relevant techniques may include:

- golden datasets;
- behavioural evaluations;
- tolerance-based assertions;
- groundedness checks;
- provenance verification;
- prompt regression tests;
- model regression tests;
- tool-call verification;
- adversarial inputs;
- hallucination checks;
- safety evaluations;
- deterministic fallback tests;
- evaluation across repeated executions;
- human review for subjective criteria.

The presence of AI does not justify vague acceptance criteria.

It requires better-defined evaluation methods.

---

# 20. Testing AI-Generated Code

AI-generated code should be treated as untrusted implementation until verified.

The following assumptions are prohibited:

```text
AI generated it, therefore it is probably correct.
AI explained it, therefore it understands it.
AI wrote tests, therefore the behaviour is covered.
The tests passed, therefore the requirement is satisfied.
Another AI reviewed it, therefore the review is independent.
```

AI-generated code should be subject to the same or greater engineering scrutiny as human-generated code.

The appropriate assurance level depends on the consequence of failure, not on who or what wrote the code.

---

# 21. Evidence Over Assertion

DevGenie's core testing principle is:

> Engineering claims should be supported by evidence.

Examples:

Instead of:

```text
"The requirement is implemented."
```

prefer:

```text
REQ-042
Implementation: src/payment/approval.ts
Unit tests: UT-091, UT-092, UT-093
Integration test: IT-014
Acceptance test: AT-007
Latest execution: PASS
Evidence commit: 9fd7ab2
```

Instead of:

```text
"The code is secure."
```

prefer evidence such as:

- applicable security tests passed;
- security review completed;
- static analysis findings resolved;
- dependency findings reviewed;
- authorization scenarios passed;
- threat-model controls verified.

Evidence does not eliminate judgement.

It makes judgement auditable.

---

# 22. Reproducibility

Verification should be reproducible wherever practical.

Test evidence should retain sufficient context to answer:

- what was tested;
- which version was tested;
- with which configuration;
- using which test data;
- using which dependency versions;
- using which model and prompt where AI is involved;
- what result was observed;
- when the evidence was produced.

A result that cannot be reproduced has reduced assurance value.

---

# 23. Risk-Based Testing

Not all code deserves equal testing effort.

Testing depth should reflect consequence.

Factors may include:

- business criticality;
- financial impact;
- safety impact;
- security exposure;
- regulatory exposure;
- data sensitivity;
- blast radius;
- architectural centrality;
- reversibility;
- frequency of use;
- likelihood of failure;
- complexity;
- degree of AI autonomy.

A low-risk cosmetic change should not require the same assurance regime as a financial approval engine.

Conversely, critical behaviour should not escape deep testing because a code change appears small.

---

# 24. Change-Impact Verification

Every material change must prompt a deliberate blast-radius analysis.

The question is not merely:

> Which lines changed?

It is:

> Which behaviours, consumers, observers, interfaces, and operational assumptions could this change affect?

Testing scope should consider, as applicable:

```text
Changed behaviour
      ↓
Direct callers and consumers
      ↓
Shared libraries and reused contracts
      ↓
Callbacks / middleware / observers / event handlers
      ↓
Schemas and external interfaces
      ↓
Configuration and feature flags
      ↓
Persistence and migration implications
      ↓
Security and authorization boundaries
      ↓
Deployment and operational dependencies
      ↓
Required regression evidence
```

The depth of analysis should be proportional to architecture, coupling, blast radius, and consequence of failure.

AI agents are particularly prone to local reasoning around edited code. DevGenie must reason about change impact at system level.

A clean isolated unit test does not prove that surrounding layers still work together. Where integration assumptions are material, verification must extend beyond mocked boundaries.

---

# 25. Production Verification

Testing does not end at deployment.

Production engineering should validate assumptions through:

- health checks;
- deployment verification;
- canary behaviour where appropriate;
- smoke tests;
- telemetry;
- alerting;
- synthetic transactions;
- rollback validation;
- runtime policy checks;
- error-rate monitoring;
- performance monitoring.

Pre-production evidence and runtime evidence serve different purposes.

Both matter.

For every production-affecting change, the release evidence should explicitly identify:

- what healthy behaviour looks like;
- which logs, metrics, traces, or synthetic checks demonstrate health;
- which signals indicate degradation or failure;
- the rollback or remediation trigger;
- the intended validation period where relevant.

If a change has no meaningful production validation requirement, that conclusion should be recorded rather than silently assumed.

Operational validation is therefore part of the release contract, not optional release prose.

---

# 26. External Tools Are Evidence Providers

DevGenie should integrate external tools without outsourcing the methodology to them.

Examples may include:

```text
Native test runners
    Jest / Vitest / pytest / JUnit / xUnit / NUnit / Go test

Browser and system testing
    Playwright / Cypress / Selenium

Static and security analysis
    SonarQube / Snyk / Semgrep / CodeQL

AI-assisted review
    CodeRabbit / coding agents / review agents

Performance
    k6 / JMeter / Locust

Mutation testing
    Stryker / PIT / mutmut

Infrastructure validation
    policy engines / IaC scanners / cloud-native tooling
```

DevGenie should treat their outputs as **evidence inputs**.

The governing model remains:

```text
Methodology
    ↓
Required evidence
    ↓
Appropriate tools
    ↓
Collected results
    ↓
Gate decision
```

Not:

```text
Tool installed
    ↓
Tool passed
    ↓
Therefore software is good
```

---

# 27. Tool Independence

Where reasonable, the DevGenie testing methodology should avoid binding itself to a specific vendor.

For example:

```text
security.static_analysis = PASS
```

is a methodological requirement.

Whether the evidence comes from SonarQube, CodeQL, Semgrep, or another qualified provider is an implementation decision.

This keeps the doctrine stable while tooling evolves.

---

# 28. Evidence Normalisation

The product implementation should eventually normalise results from heterogeneous tools.

Example:

```json
{
  "evidenceType": "unit-test",
  "requirement": "REQ-CUST-004",
  "testId": "UT-CUST-017",
  "provider": "vitest",
  "result": "PASS",
  "commit": "ab12cd",
  "durationMs": 37,
  "timestamp": "2026-08-07T20:11:00Z"
}
```

The methodology defines the evidence needed.

The product defines how that evidence is harvested, normalised, stored, and evaluated.

---

# 29. Gates Are Engineering Decisions

A gate should represent an explicit engineering decision based on known criteria.

Examples:

```text
PASS
FAIL
ESCALATE
WAIVED
```

A gate should be able to explain:

- which criteria applied;
- which evidence was evaluated;
- which criteria passed;
- which criteria failed;
- which exceptions were accepted;
- who or what authorised any waiver.

A gate must never be reduced to an unexplained boolean.

---

# 30. Waivers Must Be Explicit

Engineering sometimes requires conscious acceptance of incomplete assurance.

That is legitimate.

Silent exceptions are not.

A waiver should record:

- failed or missing criterion;
- rationale;
- consequence;
- compensating control;
- approver;
- expiry or remediation condition where relevant.

This makes engineering pragmatism visible without pretending the evidence was stronger than it was.

---

# 31. Minimum Testing Discipline

Before advanced external testing capabilities are considered, DevGenie methodology should expect at least the following for meaningful production changes:

- requirements are sufficiently clear to test;
- acceptance criteria exist where needed;
- relevant unit tests exist;
- relevant boundary and negative conditions are considered;
- integration assumptions are tested where applicable;
- regression impact is considered;
- requirements can be traced to relevant verification;
- testing has been explicitly addressed for every material behaviour change;
- existing authoritative tests have been inspected before creating overlapping new tests;
- change impact and blast radius have been considered;
- tests execute deterministically where determinism is expected;
- failures block progression according to defined criteria;
- test evidence is retained;
- defects result in regression protection;
- non-trivial defect fixes are supported by causal reasoning rather than patch success alone;
- production-affecting releases identify healthy signals, failure signals, and rollback criteria;
- release decisions can be explained.

This is the internal engineering baseline.

---

# 32. Anti-Patterns

DevGenie should actively discourage the following.

## Test-count theatre

```text
"AI generated 1,200 tests."
```

The number is meaningless without understanding what they verify.

## Coverage theatre

```text
"Coverage is 95%, therefore quality is high."
```

Coverage measures execution, not correctness.

## Green-pipeline reasoning

```text
"CI passed, therefore the feature is correct."
```

CI only proves the configured checks passed.

## Mock everything

A system can achieve perfect mocked tests while failing against every real dependency.

## Same-agent assurance

Implementation, tests, review, and approval all produced from the same context should not automatically be considered independent evidence.

## Snapshot abuse

Tests that merely approve large generated outputs can easily preserve incorrect behaviour.

## Brittle implementation tests

Tests tied unnecessarily to internal implementation make refactoring expensive and encourage superficial maintenance.

## Test-after-the-fact only

Writing tests only after implementation encourages tests that rationalise what was built rather than challenge what should have been built.

## Tool-as-methodology

Installing SonarQube, CodeRabbit, Snyk, Playwright, or any other product does not constitute a testing strategy.

## Vacuous test gates

```text
"Tests pass."
```

is not sufficient when no relevant tests exist. The workflow must first establish that testing has been addressed.

## Test-suite fragmentation

Automatically creating a new test file for every change without locating the authoritative existing verification produces duplication and inconsistent behavioural ownership.

## Symptom-fix debugging

A patch that removes a failure does not by itself prove the root cause. Non-trivial fixes should be supported by causal explanation and regression evidence.

## Local-diff blindness

Testing only the edited function ignores downstream consumers, observers, middleware, shared contracts, and integration behaviour.

## Deploy-and-hope

Production deployment without defined healthy signals, failure signals, and rollback criteria is incomplete verification.

---

# 33. DevGenie Testing Principles

The doctrine can be condensed into the following principles.

## T1 — Testing starts with intent

If we do not know what correct behaviour means, execution cannot prove correctness.

## T2 — Every important claim requires evidence

Assertions about quality should be backed by reproducible engineering evidence.

## T3 — Verification and validation are different

We must prove both that the system was built correctly and that the correct system was built.

## T4 — Test design matters more than test volume

A small number of carefully chosen tests may provide more assurance than thousands of mechanically generated tests.

## T5 — Failure paths are first-class

We test how systems fail, recover, reject, retry, and degrade — not merely how they succeed.

## T6 — Independence increases assurance

The same reasoning process should not be the only authority for implementation, testing, review, and approval.

## T7 — Coverage has multiple dimensions

Code coverage alone is not sufficient. Requirement, scenario, interface, and risk coverage matter.

## T8 — Tests themselves must be tested

Where assurance warrants it, mutation, fault injection, review, and other techniques should demonstrate that tests can detect defects.

## T9 — External tools provide evidence, not truth

Tools strengthen the testing system. They do not replace engineering judgement.

## T10 — Testing is proportional to consequence

Assurance effort should scale with the impact and likelihood of failure.

## T11 — Defects improve the system

A defect should produce learning, regression protection, and where useful, methodology improvement.

## T12 — Release is an evidence-based decision

A release should be explainable in terms of satisfied criteria, available evidence, and explicitly accepted exceptions.

---

## T13 — Testing must be explicitly addressed

Every material change must establish what verification evidence is required. “No tests” is a reasoned conclusion, not an omission.

## T14 — A fix is not proof of a cause

For non-trivial defects, root-cause claims should survive causal tracing, assumption audit, and an independent prediction.

---

# 34. Relationship to the DevGenie Product

The methodology must exist independently of the product.

The product's job is to make the methodology easier to follow, harder to bypass accidentally, and cheaper to evidence.

The intended evolution is:

```text
Testing doctrine
      ↓
DevGenie methodology
      ↓
Test policies and contracts
      ↓
Evidence requirements
      ↓
Automation
      ↓
Tool integrations
      ↓
Gate enforcement
      ↓
Audit and learning
```

DevGenie should not invent engineering quality from scratch.

It should encode good engineering discipline into an AI-native software delivery system.

---

# 35. Product Capabilities Implied by the Doctrine

The doctrine suggests future DevGenie capabilities such as:

- requirement-to-test traceability;
- testing-addressed gates;
- plan-time test scenario obligations;
- existing-test ownership discovery;
- test obligation generation;
- boundary-case derivation;
- change-impact / blast-radius analysis;
- independent test-generation workflows;
- evidence harvesting from native test runners;
- evidence harvesting from external analysis tools;
- requirement coverage reporting;
- scenario coverage reporting;
- mutation-test integration;
- defect-to-regression linkage;
- causal-debugging evidence capture;
- configurable entry and exit criteria;
- risk-based assurance profiles;
- AI evaluation datasets;
- provenance capture;
- test evidence normalisation;
- release gates;
- operational validation contracts;
- waiver management;
- historical quality analytics.

These are product consequences of the doctrine, not substitutes for it.

---

# 36. Version 2 Hard Rules

Version 2 introduces five explicit operational rules that complement the original doctrine.

## V2-1 — Testing Addressed

Every material change must explicitly establish its verification obligation. For behaviour-bearing work, material test scenarios are identified during planning. A pipeline cannot pass simply because no relevant tests exist.

## V2-2 — Existing Test Ownership

Before adding new tests, locate and strengthen the authoritative existing verification where appropriate.

## V2-3 — Change-Impact Verification

Verification must consider the blast radius beyond the edited lines, including consumers, callbacks, middleware, interfaces, persistence, security boundaries, and operational dependencies.

## V2-4 — Causal Debugging

For non-trivial defects, reproduce the issue, trace the causal chain, audit assumptions, make and verify an independent prediction, then fix the root cause and protect it with regression evidence.

## V2-5 — Operational Validation Contract

Every production-affecting release must identify healthy signals, failure signals, and rollback or remediation criteria.

These rules do not replace the broader DevGenie assurance model.

They make it harder for sound testing doctrine to be lost during implementation.

---

# 37. Final Position

The speed of AI code generation must not become an excuse for reducing software engineering discipline.

The opposite should happen.

When implementation becomes cheap and abundant, **verification becomes more valuable**.

DevGenie's position should therefore be:

> AI may accelerate implementation. It does not lower the burden of proof.

And:

> We do not trust code because a developer wrote it, because an AI wrote it, because tests exist, or because a tool produced a green badge. We trust software to the extent that relevant engineering claims are supported by sufficient, traceable, reproducible evidence.

That is the foundation on which DevGenie's testing methodology — and later its testing product capabilities — should be built.
