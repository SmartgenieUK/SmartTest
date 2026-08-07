# Adopting SmartTest

SmartTest is DevGenie's portable testing discipline for AI-assisted development. It is a set of Markdown practices and agent skills, not a test runner or DevGenie product dependency.

## Choose the smallest useful starting point

| Situation | Start with | Expected result |
|---|---|---|
| A change is not yet implemented | [`test-plan`](../skills/test-plan/SKILL.md) and the [test-plan template](../templates/TEST_PLAN_TEMPLATE.md) | Verification obligations derived from intent before code shapes the answer |
| A change already exists | [`test-impact`](../skills/test-impact/SKILL.md), then [`test-review`](../skills/test-review/SKILL.md) | A blast-radius assessment and evidence-based review |
| A non-trivial defect is under investigation | [`debug-causal`](../skills/debug-causal/SKILL.md) | A causal diagnosis with an explicit proof status |
| A release decision is due | [AI Code Release Checklist](../checklists/AI_CODE_RELEASE_CHECKLIST.md) | A decision tied to evidence, gaps, waivers, and risk |
| A team is setting policy | [Testing Doctrine](../doctrine/TESTING_DOCTRINE.md) | Shared principles and vocabulary |

Do not adopt every artefact at once. A team can begin with one skill and one template in an existing pull-request workflow.

## A bounded trial

After installation, the first planning workflow can take only a few minutes for a small, clear requirement. The complete sequence below continues as the change is implemented and reviewed; it is not a promise that cold setup, implementation and assurance all fit into ten minutes.

1. Pick a real, bounded change that has an acceptance criterion.
2. Give your coding agent repository access.
3. Ask it to read [`skills/test-plan/SKILL.md`](../skills/test-plan/SKILL.md) and follow it before implementing the change.
4. Write the output with the [test-plan template](../templates/TEST_PLAN_TEMPLATE.md).
5. Challenge one scenario: could the proposed test pass while the requirement is still wrong?
6. After implementation, run `test-impact` and `test-review` against the actual diff and evidence.
7. Keep, adapt, or reject the workflow based on whether it exposed a useful obligation—not on how polished the prose looked.

Use the [agent setup guide](AGENT_SETUP.md) for native Codex, Claude Code, Cursor, and GitHub Copilot locations.

## Team rollout

### 1. Define local meaning

Record what your team considers:

- a material change;
- production-affecting work;
- authoritative test ownership;
- acceptable independent verification;
- evidence needed for each risk tier;
- who may approve waivers or accept residual risk.

Keep those decisions near the repository, ideally in `AGENTS.md` or a short engineering guide.

### 2. Integrate with existing work

SmartTest should enrich the workflow you already use:

- link requirements or acceptance criteria in the pull request;
- place new tests with the authoritative existing suite;
- attach commands, results, logs, or traces as evidence;
- use explicit N/A decisions when a check genuinely does not apply;
- name evidence gaps rather than converting them into a green status.

The included [pull-request template](../.github/pull_request_template.md) is a starting point. Trim it only after observing which prompts are low-value in your context.

### 3. Calibrate by risk

Low-risk documentation or formatting changes may need only link, render, or structure verification. A change to authorization, money movement, migration, concurrency, or an external contract normally needs stronger boundary, failure, integration, and operational evidence. The doctrine requires testing to be addressed for every material change; it does not require the same tests for every change.

### 4. Review outcomes

After several changes, ask:

- Which obligations did the method uncover before release?
- Which prompts produced ceremony without evidence?
- Were requirements and tests independently derived where consequence warranted it?
- Did regressions protect behaviour rather than implementation detail?
- Did operational signals reveal anything the test environment could not?

Change local mechanics freely. Preserve the doctrine's evidence obligations and record deliberate deviations.

## What good use looks like

Good SmartTest use leaves a reviewer able to answer:

1. What behaviour was intended?
2. What could fail, including boundaries and failure paths?
3. Which tests or other evidence address each material obligation?
4. Were the checks capable of exposing the important defect?
5. What remains uncertain, waived, or operationally monitored?

A long document, high coverage percentage, or green pipeline is not a substitute for those answers.

## Worked material

- [Documented payment-approval example](../examples/payment-approval/README.md): the full requirement-to-evidence chain.
- [Executable Python example](../examples/payment-approval-python/README.md): a zero-dependency test suite and a boundary mutant that demonstrates whether a test can fail.

## Boundaries

SmartTest v0.1 does not install tools, run CI, store evidence, enforce gates, or implement DevGenie. Teams remain responsible for their product decisions, test infrastructure, security controls, and release authority.
