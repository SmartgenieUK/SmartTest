# SmartTest Adversarial Adoption Audit

**Date:** 2026-08-07  
**Method:** Fresh-context adversarial review by an AI coding agent, commissioned by the maintainer.  
**Pre-remediation verdict:** B- / 6.8 out of 10.

This is an inspectable review record, not independent certification. The reviewer was asked to find reasons a competent developer might fail to install, trust, or adopt SmartTest.

## Material findings

| Severity | Finding | Disposition |
|---|---|---|
| High | Native skill copies left `test-plan` pointing to a template that was not installed. | Fixed: the skill degrades safely when the optional template is absent. |
| High | Generic-agent setup did not explain how SmartTest files become available. | Fixed: the setup now installs portable material under `.smarttest/` and gives an exact prompt path. |
| High | The behavioural evaluation lacked fixtures, raw outputs, model versions, and an executable harness. | Partly fixed: deterministic repository and example verification is now automated. The behavioural report is explicitly retained as limited, non-statistical evidence. |
| Medium | Cursor and Copilot copy commands could produce `skills/skills` and collide with application directories. | Fixed: both adapters use `.smarttest/skills`; commands assume and state a clean destination. |
| Medium | Five-minute language read like a universal cold-start promise. | Fixed in current guidance: the quick start is framed as trying one bounded workflow, not completing organisational adoption. |
| Medium | The doctrine was marked Draft while marketed as normative. | Fixed: the doctrine records its ratified SmartTest v0.1 status and provenance. |
| Medium | A 1,400-line doctrine with many top-level headings was hard to scan. | Fixed: one document title, a linked map, and a consistent section hierarchy. |
| Medium | The executable example omitted its Python prerequisite. | Fixed: the example states Python 3.8+ and provides version/run commands. |
| Medium | No one-command validation or CI existed. | Fixed: `python scripts/verify_repo.py` and GitHub Actions now enforce deterministic checks. |

## What already held up

- The doctrine was substantive rather than a list of generic testing slogans.
- Codex, Claude, Cursor and Copilot integration mechanisms were broadly credible.
- The old six-test example passed, and its deliberate inclusive-boundary mutant caused exactly one expected failure.
- All then-present relative Markdown links resolved in the source tree.

## Residual adoption uncertainty

- SmartTest has not yet published longitudinal adoption evidence from multiple independent repositories or teams.
- Native discovery has not been exercised end to end in every supported vendor UI and version.
- Copy-based installation requires adopters to decide how they will receive upstream updates.
- The behavioural probes remain too small and insufficiently archived to support reliability claims across agents.

These limitations are carried into the public [report card](../../REPORT_CARD.md), rather than hidden behind the remediation work.
