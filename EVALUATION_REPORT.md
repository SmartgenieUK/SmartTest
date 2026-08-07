# SmartTest Behavioural Evaluation

This report records forward tests run against the v0.1 skills. The purpose was to observe whether the instructions changed agent behaviour on representative cases, not merely whether the files parsed.

## Method

- Each case used a fresh agent context with access to one canonical `SKILL.md` and a bounded fixture.
- Agents were asked to produce the skill's required output without modifying files.
- Evaluation checked substantive behaviour against the doctrine's distinctive obligations.
- A failure prompted a skill correction and a fresh rerun of the same challenge.

The cases are scenario probes, not statistical evidence or a guarantee that every agent and repository will behave identically. The original raw prompts, full outputs, model versions and runner were not retained in a replay bundle, so this report should not be treated as independently reproducible behavioural evidence.

## Results

| Skill or path | Challenge | Expected discriminator | Result |
|---|---|---|---|
| `test-plan` | High-risk account lockout requirement | Derive boundaries, abuse/failure cases, operational signals, and independent evidence before implementation | Pass |
| `test-impact` | Tenant-key normalization diff | Trace impact beyond edited files into identity, persistence, consumers, security, and regression scope | Pass |
| `test-review` | Green suite with reported 100% coverage | Refuse to equate green status or coverage with adequate requirement evidence | Pass |
| Low-risk doctrine application | Documentation-only change | Select proportionate link/structure evidence without manufacturing executable tests | Pass |
| `debug-causal`, initial | Concurrent user creation produces two emails | Reject a failed event-bus retry prediction and avoid a premature root-cause claim | Partial: rejected the original hypothesis but promoted a replacement explanation to `PROVEN` using evidence already observed |
| `debug-causal`, after correction | Same fresh-context challenge | Require a new prospective prediction and pre-correction failing regression before `PROVEN` | Pass: replacement mechanism reported `PARTIALLY SUPPORTED` with missing proof obligations |

## Causal-debug correction

The initial skill correctly said that a false independent prediction invalidates the original hypothesis. It did not state strongly enough that a replacement hypothesis needs its own prospectively recorded discriminating prediction. The agent consequently reused existing observations to claim proof.

The skill now requires:

- recording the prediction before observing its result;
- rejecting or revising a hypothesis when that prediction fails;
- giving a replacement hypothesis a new prospective prediction;
- demonstrating an authoritative regression that fails before correction;
- withholding `PROVEN` when any proof obligation remains.

In the fresh rerun, the agent rejected the event-bus retry explanation, identified double publication as the leading mechanism, proposed a barrier-controlled concurrent prediction and regression, and assigned `PARTIALLY SUPPORTED` because neither had yet run. That is the intended evidence discipline.

## Executable sensitivity check

The [Python payment-approval example](examples/payment-approval-python/README.md) supplies an additional non-agent check:

- Correct implementation: ten of ten tests pass.
- Deliberate inclusive-boundary mutant (`>=` changed to `>`): the exact-threshold test fails; the other nine pass.

This demonstrates that the named boundary test can expose that specific defect. It does not prove full correctness or substitute for requirement, integration, and operational evidence.

## Residual uncertainty

- Four positive probes and one corrected probe are too small to establish reliability across all models, prompts, and codebases.
- The behavioural probes cannot be independently replayed from this repository because their full fixtures, prompts, outputs, model versions, and runner were not retained. This is a known evidence gap, not a passing result.
- Agent-native discovery was verified against current primary documentation, but behavioural probes loaded skills by explicit path rather than exercising every vendor UI.
- Teams should rerun representative probes in their chosen agent and repository context, particularly after changing a skill or adapter.

Repository structure, local Markdown links, skill metadata, the executable suite, and the deliberate mutant are separately reproducible with `python scripts/verify_repo.py` and in GitHub Actions. Those deterministic checks do not repair or replace the missing behavioural replay evidence.
