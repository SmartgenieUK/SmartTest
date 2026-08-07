# Your AI-Generated Tests Are Green. What Did They Prove?

AI can write an implementation and its tests in minutes. That is useful—but it creates an assurance problem that a green pipeline cannot answer.

If the same context misunderstands a requirement, it can generate the wrong behaviour and tests that faithfully confirm the same mistake. Everything passes. The defect remains.

That is why we built [SmartTest](https://github.com/SmartgenieUK/SmartTest), DevGenie's portable, evidence-first testing discipline for AI-assisted software development.

SmartTest is not another test framework, hosted platform, or quality score. It is a small open-source repository of engineering rules, agent skills, templates, checklists, and worked examples that help developers answer a harder question:

> What evidence would make this change safe enough to trust?

## Green is a result, not an argument

A passing test tells you that the exercised path produced the asserted result in that environment. It does not, by itself, establish that:

- the requirement was interpreted correctly;
- important boundaries and failure paths were included;
- the test could detect the defect that matters;
- the right integration or operational behaviour was exercised;
- a regression elsewhere was considered;
- missing evidence was identified honestly.

Code coverage has the same limitation. It tells you which code ran. It does not tell you whether you tested what you were supposed to build.

SmartTest treats coverage, test results, static analysis, review comments, logs, and production signals as evidence inputs—not automatic truth.

## Start from intent, not implementation

The central workflow is deliberately simple:

1. Establish the intended behaviour and acceptance criteria.
2. Derive verification obligations before implementation shapes the answer.
3. Inspect authoritative existing tests and ownership.
4. Consider positive, negative, boundary, failure, permission, integration, and operational cases according to risk.
5. Map each important claim to evidence.
6. Demonstrate that important tests are capable of failing.
7. Record gaps, waivers, and residual uncertainty instead of hiding them behind a status.

This is not a demand for more tests everywhere. A documentation change may need link and structure checks. Authorization, money movement, data migration, concurrency, or an external contract usually warrants stronger evidence. The obligation is to address testing explicitly and proportionately.

## Four focused workflows for coding agents

SmartTest packages the method into four portable skills:

- `test-plan` derives verification obligations from requirements before implementation.
- `test-impact` traces a change beyond edited files into consumers, contracts, persistence, security, and operations.
- `test-review` judges whether the available tests actually support the claims being made.
- `debug-causal` prevents a plausible patch from being mistaken for proof of root cause.

The skills are Markdown, not a proprietary runtime. The repository includes setup instructions for Codex, Claude Code, Cursor, GitHub Copilot, and agents with no native skill mechanism.

## A ten-minute experiment

You do not need to transform your delivery process to find out whether SmartTest is useful.

Choose one real, bounded change with an acceptance criterion. Ask your coding agent to read `skills/test-plan/SKILL.md` before writing code. Review the proposed boundaries and failure paths. After implementation, run `test-impact` and `test-review` against the actual diff and evidence.

Then ask one question:

> Did this expose an obligation or uncertainty we would otherwise have missed?

If the answer is no, do not keep the ceremony. If the answer is yes, adapt the smallest useful part to your normal pull-request workflow.

## Tests should prove they can fail

The repository includes a small Python payment-approval example built around one requirement:

> Payments of £10,000 or more require secondary approval.

The correct implementation passes all six tests. A deliberate mutant changes `>=` to `>`. The exact-boundary test fails while the other five still pass.

That result does not prove the whole system is correct. It proves something narrower and useful: the named boundary test can expose that specific defect. SmartTest encourages that level of precision in every evidence claim.

## Debugging needs a proof threshold

AI is particularly good at producing persuasive causal stories. Persuasive is not the same as proven.

SmartTest's causal-debugging workflow separates observation from inference, requires a falsifiable hypothesis, and records an independent prediction before observing its result. If that prediction fails, a replacement hypothesis needs a new prospective prediction. Existing evidence cannot be relabelled as independent proof after the fact.

A root cause reaches `PROVEN` only when the causal chain, independent prediction, pre-correction failing regression, smallest mechanism-level correction, and focused and broader verification all support it. Otherwise, the honest result is `PARTIALLY SUPPORTED`, `NOT PROVEN`, or `ESCALATE`.

That distinction matters more as agents become better at writing confident explanations.

## Where evidence providers fit

Enterprises already use test runners, CI systems, static analyzers, security scanners, coverage tools, review services, observability platforms, and change-management systems. SmartTest does not compete with those systems.

First, the team must decide what needs to be proven. Then evidence providers can contribute relevant signals. A provider's badge is useful only when its scope, configuration, freshness, limitations, and relationship to the requirement are understood.

This is the longer-term DevGenie direction: establish engineering obligations first, then make evidence from multiple providers traceable, reviewable, and decision-ready. The public SmartTest repository is the methodology foundation, not a DevGenie product implementation.

## Try it, challenge it, improve it

SmartTest v0.1 is intentionally small. It is licensed under Apache-2.0 and includes:

- the complete testing doctrine;
- a release checklist;
- test-plan, traceability, and Definition of Done templates;
- four portable coding-agent skills;
- documented and executable worked examples;
- adoption and contribution guidance;
- behavioural evaluation results, including a weakness found and corrected during forward testing.

Start with the [SmartTest repository](https://github.com/SmartgenieUK/SmartTest). Try it on one real change. If it finds a useful gap, tell us what happened. If it produces ceremony without evidence, tell us that too.

Evidence over assertion applies to SmartTest itself.
