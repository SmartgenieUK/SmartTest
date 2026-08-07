# SmartTest

**DevGenie's portable testing discipline for AI-assisted software development.**

SmartTest is a small, portable toolkit combining a testing doctrine, agent skills, practical templates, a release checklist, and worked examples. It does not require the DevGenie product or any particular AI vendor.

> **AI may accelerate implementation. It does not lower the burden of proof.**

AI can produce implementation and tests from the same mistaken interpretation, then report a green result. This toolkit starts from intent, derives verification obligations before test generation, and asks for traceable evidence rather than confidence statements.

Read the launch article: [What If You Could Get Your Hands on a Full-Blown Testing Doctrine for Your Entire Repository - for Free?](docs/INTRODUCING_SMARTTEST.md)

Before trusting the pitch, read the [v0.1 report card](REPORT_CARD.md). Two adversarial reviews scored the pre-remediation repository at 6.7–6.8/10, exposed material defects, and drove fixes. The current B / 7.7 assessment names what is verified and what is still unproven.

> **Code coverage tells you what code your tests executed. Requirement coverage tells you whether you tested what you were supposed to build.**

The toolkit improves testing discipline; it does not guarantee correctness.

## Who it is for

- Developers using Claude, Codex, Copilot, Cursor, or another coding agent.
- Reviewers assessing AI-assisted changes and their evidence.
- Technical leads adopting a lightweight, tool-independent assurance method.
- Teams that want more rigour without introducing a testing platform.

## First workflow

1. Read the [adoption guide](docs/ADOPTION_GUIDE.md) and choose one real, bounded change.
2. Follow the [agent setup](docs/AGENT_SETUP.md) for Codex, Claude Code, Cursor, Copilot, or a generic agent.
3. Before implementation, copy the [Test Plan Template](templates/TEST_PLAN_TEMPLATE.md) and run [`test-plan`](skills/test-plan/SKILL.md).
4. After implementation, run [`test-impact`](skills/test-impact/SKILL.md), then [`test-review`](skills/test-review/SKILL.md).
5. For a non-trivial defect, use [`debug-causal`](skills/debug-causal/SKILL.md). For a release, use the [AI Code Release Checklist](checklists/AI_CODE_RELEASE_CHECKLIST.md).

See the [documented payment-approval example](examples/payment-approval/README.md) for the complete intent-to-evidence chain, then run the [executable Python example](examples/payment-approval-python/README.md) to observe a boundary test kill a deliberate mutant.

## What you can use immediately

| Need | Start here | Outcome |
|---|---|---|
| Plan verification before implementation | [Test Plan Template](templates/TEST_PLAN_TEMPLATE.md) | Risk-based scenarios and expected evidence |
| Connect intent to evidence | [Traceability Template](templates/REQUIREMENT_TEST_TRACEABILITY_TEMPLATE.md) | Requirement-to-result mapping |
| Decide whether an AI-assisted change is done | [Definition of Done](templates/AI_CODE_DEFINITION_OF_DONE.md) | An explainable completion decision |
| Review release readiness | [Release Checklist](checklists/AI_CODE_RELEASE_CHECKLIST.md) | High-signal release review |
| Guide a coding agent | [Skills](#using-the-skills) | Focused, repeatable agent workflows |
| Adopt with a team | [Adoption Guide](docs/ADOPTION_GUIDE.md) | A low-ceremony rollout path |

## Using the skills

Each skill has one primary job and is written as portable Markdown. Native discovery paths differ by agent; use the [verified setup guide](docs/AGENT_SETUP.md) to install them. If your agent has no skill mechanism, give it repository access and instruct it directly, for example:

```text
Read .smarttest/skills/test-plan/SKILL.md and follow it for this requirement.
Write the result using .smarttest/templates/TEST_PLAN_TEMPLATE.md.
Do not implement the change yet.
```

The four skills are:

- [`test-plan`](skills/test-plan/SKILL.md): derive verification obligations from intent.
- [`test-impact`](skills/test-impact/SKILL.md): assess blast radius and regression scope.
- [`test-review`](skills/test-review/SKILL.md): judge whether tests provide adequate evidence.
- [`debug-causal`](skills/debug-causal/SKILL.md): establish and verify defect causality before correction.

`AGENTS.md` contains the compact repository-level rules that a compatible coding agent can load automatically.

## Adapting the method

Keep the doctrine's obligations intact, then tailor the mechanics:

1. Define what counts as a material or production-affecting change in your context.
2. Map the templates to your requirement, pull-request, test, and release records.
3. Select test levels and independent evidence in proportion to consequence.
4. Name the tools that can supply required evidence, without making a tool's green status the method.
5. Record explicit N/A decisions and waivers; do not silently delete inconvenient checks.

Start with Markdown in the normal development workflow. Automate only after the method proves useful.

## Repository identity and DevGenie

**SmartTest** is the public repository and toolkit name. **DevGenie** is the originating brand and remains part of the methodology's identity. DevGenie is an intended AI-native software delivery system; SmartTest stands independently of that product. A future DevGenie product may make the method easier to follow and evidence, but it is not required here.

## Scope and boundaries

SmartTest v0.1 is not a test framework, DevGenie product implementation, evidence database, dashboard, IDE extension, agent installer, or commercial-tool integration. Its CI verifies this repository's deterministic evidence; it is not a general CI product. SmartTest provides no correctness guarantee and mandates no vendor.

Contributions are welcome under the constraints in [CONTRIBUTING.md](CONTRIBUTING.md). SmartTest is licensed under the [Apache License 2.0](LICENSE). See the [report card](REPORT_CARD.md), [behavioural evaluation](EVALUATION_REPORT.md), and [build report](BUILD_REPORT.md) for evidence and limitations.
