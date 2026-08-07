# SmartTest Adversarial Doctrine Audit

**Date:** 2026-08-07  
**Method:** Fresh-context adversarial review by an AI coding agent, commissioned by the maintainer.  
**Pre-remediation verdict:** Conditional pass as a methodology prototype / 6.7 out of 10.

This is not an external assurance opinion or certification. The reviewer tested whether SmartTest obeyed its own demands for traceability, sensitivity, causal reasoning, risk, gates, reproducibility and portability.

## Pre-remediation category scores

| Category | Score / 10 |
|---|---:|
| Doctrine coherence | 8.0 |
| Doctrine-to-artefact fidelity | 7.0 |
| Traceability | 5.0 |
| Test sensitivity evidence | 6.5 |
| Causal debugging discipline | 8.5 |
| Risk and gate discipline | 6.0 |
| Reproducibility | 4.0 |
| Portability | 7.5 |

## Material findings

| Severity | Finding | Disposition |
|---|---|---|
| High | Behavioural self-review was asserted without enough material to replay it independently. | Partly fixed: the limitation is explicit, while deterministic structure, link, example and mutation checks are executable in CI. Full behavioural replay artefacts remain future evidence, not a v0.1 claim. |
| High | The executable example did not implement several acceptance obligations it claimed to illustrate: distinct approval, authorization, audit, retained pending state, no premature execution, and idempotency. | Fixed: the example now implements those behaviours and tests them directly. |
| Medium | The documented traceability chain was fictional rather than tied to the executable checks. | Fixed: the executable example has a test-name-level traceability matrix and verification record. |
| Medium | Release N/A and waiver language could bypass controls without strong authority semantics. | Fixed: non-waivable obligations are named; N/A and waivers require rationale and evidence; high-consequence exceptions require a named accountable human independent from the coding agent. |
| Medium | The traceability template omitted design decision and evidence provenance. | Fixed: both are now first-class fields, including provider, timestamp, immutable location or digest, commit and reviewer. |
| Medium | Draft status conflicted with normative positioning. | Fixed: v0.1 status and provenance are explicit. |

## What already held up

- The doctrine was coherent and unusually explicit about evidence versus assertion.
- The causal-debugging proof gate resisted a plausible but unproven explanation.
- The old executable suite passed and the targeted mutant was killed by exactly one boundary test.
- Relative Markdown links had no observed broken targets.

## Residual assurance limits

- The payment example uses in-memory collaborators; it does not prove a real approval, audit, persistence or payment integration.
- One hand-authored mutant demonstrates sensitivity to one defect only.
- The independent reviews were AI-agent reviews commissioned inside the project, not external expert or user research.
- Production-scale operability, accessibility, security and multi-language adoption are not evidenced by v0.1.

The current, post-remediation assessment is summarised in the public [report card](../../REPORT_CARD.md).
