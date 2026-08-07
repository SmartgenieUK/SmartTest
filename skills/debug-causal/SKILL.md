---
name: debug-causal
description: Diagnose non-trivial defects by reproducing the failure, tracing causality, testing an independent prediction, and protecting the smallest root-cause correction. Use when a bug spans components, has an uncertain cause, recurs, is timing- or state-dependent, or when a working patch could be only a symptom fix.
---

# Causal Debugging

## Purpose

Diagnose non-trivial defects without confusing a working patch with proof of root cause.

## Use when

- A defect's cause is uncertain, indirect, intermittent, or cross-component.
- A previous correction addressed symptoms or the defect recurred.
- State, concurrency, ordering, caching, configuration, or integration may be causal.
- A proposed patch appears to work but lacks explanatory evidence.

For an obvious isolated typo with direct evidence, use proportionate judgement; do not manufacture ceremony.

## Inspect

Inspect:

1. Expected behaviour, requirement, and observed failure.
2. Reproduction steps, data, environment, configuration, logs, traces, and timing.
3. Relevant code path, state transitions, contracts, dependencies, and recent changes.
4. Existing tests and defect history for the behaviour.
5. Consumers and blast radius of a potential correction.

Preserve observations separately from interpretations.

## Procedure

Follow this sequence:

1. **Reproduce.** Establish a repeatable failure or document why reproduction is constrained. Record exact inputs, version, configuration, environment, and observation.
2. **Trace the causal chain.** Follow the failing outcome backwards through data, state, calls, events, and decisions to the earliest evidenced divergence.
3. **Audit assumptions.** List assumptions about contracts, order, timing, identity, state, configuration, and dependencies. Test the material ones.
4. **Form a falsifiable hypothesis.** State the proposed cause and mechanism, not merely the faulty line.
5. **Make an independent prediction.** Before observing its result, record an observable outcome that follows from the hypothesis and goes beyond “the patch makes the failure disappear,” preferably without changing production code. Evidence already known may support a hypothesis, but it cannot count as its independent prediction.
6. **Verify the prediction.** Attempt to falsify it. If it fails, reject or revise the hypothesis and return to step 4. A replacement hypothesis needs a new, prospectively recorded prediction; do not reuse already-observed evidence as retrospective proof.
7. **Create or strengthen a failing regression.** Prefer authoritative existing ownership. Ensure it fails for the observed defect and protects expected behaviour.
8. **Apply the smallest root-cause correction.** Avoid unrelated cleanup.
9. **Run focused verification.** Confirm the regression and relevant assumption checks pass.
10. **Run broader regression.** Use a blast-radius analysis to choose proportionate integration and system evidence.
11. **Review evidence.** Distinguish proven cause, supporting evidence, residual uncertainty, and operational follow-up.

Hard rules:

- If a hypothesis's independent prediction is false, do not claim that hypothesis is proven merely because a patch appears to work.
- Do not label a replacement hypothesis `PROVEN` from the same observations that suggested it. Record and verify a new discriminating prediction first.
- Do not label a cause `PROVEN` unless an authoritative regression failed before correction and passed afterward. When reproducing safely is impossible, report the limitation and use `PARTIALLY SUPPORTED` or `ESCALATE`, not `PROVEN`.

## Root-cause status gate

Use the strongest status supported by the evidence:

- **PROVEN:** the failure is reproducible, or equivalently constrained evidence is available; the causal chain reaches the earliest evidenced divergence; a prospectively recorded independent prediction was verified; an authoritative regression failed before correction; and the smallest mechanism-level correction passes focused and proportionate broader verification.
- **PARTIALLY SUPPORTED:** the explanation fits material evidence but one or more proof obligations remain, such as a new independent prediction, a pre-correction failing regression, safe reproduction, or broader verification.
- **NOT PROVEN:** a material prediction failed, competing explanations remain, or evidence does not establish the proposed mechanism.
- **ESCALATE:** the next discriminating step needs unavailable evidence, access, authority, or a material external decision.

State missing proof obligations explicitly. Never upgrade status because a plausible correction, green suite, or persuasive narrative exists.

## Required output

Return:

- expected versus observed behaviour;
- reproduction evidence and constraints;
- causal chain with observations separated from inference;
- audited assumptions and results;
- hypothesis, independent prediction, and prediction result;
- regression-test ownership and evidence that it failed before correction;
- smallest correction and why it addresses the mechanism;
- focused and broader verification results;
- blast radius, residual uncertainty, and missing evidence;
- root-cause status: PROVEN / PARTIALLY SUPPORTED / NOT PROVEN / ESCALATE.

## Stop or escalate

Escalate when:

- the failure cannot be safely reproduced and available production evidence is insufficient;
- required logs, data, systems, or access are unavailable;
- evidence indicates security compromise, data loss, safety impact, or an active production incident outside task authority;
- multiple hypotheses remain plausible and the next discriminating experiment requires a material external change;
- a proposed correction needs a product, architecture, migration, or risk-acceptance decision.

## Anti-patterns

- Patch first and explain afterward.
- Treat correlation, temporal proximity, or changed lines as causation.
- Repackage already-observed evidence as a new prediction.
- Promote a replacement explanation directly to `PROVEN` after the original hypothesis fails.
- Change several variables during the discriminating experiment.
- Rewrite a weak test to agree with current implementation.
- Claim root cause after an independent prediction fails.
- Add only a test of the chosen implementation detail.
- Skip broader regression because the focused test passes.

## Compact example

Failure: exactly £10,000 bypasses approval. Hypothesis: the policy uses an exclusive comparison. Independent prediction: £10,000.01 requires approval while £10,000 does not, and the same divergence appears before the approval service is called. If observed, strengthen the existing policy test with the exact boundary, confirm it fails, change `>` to `>=`, then verify approval integration and payment-execution blocking. If the prediction is false, the comparison hypothesis is not proven even if that edit happens to make one reproduction pass.
