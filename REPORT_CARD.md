# SmartTest v0.1 Report Card

**Assessment date:** 2026-08-07  
**Current verdict:** **B / 7.7 out of 10 — strong, inspectable beta**  
**Pre-remediation baseline:** 6.7–6.8 out of 10 across two adversarial reviews

SmartTest is a serious, usable methodology toolkit with automated deterministic checks. It is not independently certified, and it does not yet have enough multi-team field evidence to claim proven adoption at scale.

## How this was assessed

Two fresh-context AI reviewers were commissioned to attack different claims:

- [Adoption audit](evidence/audits/ADOPTION_AUDIT.md): could a developer install, understand and use the repository without maintainer help?
- [Doctrine audit](evidence/audits/DOCTRINE_AUDIT.md): does SmartTest satisfy its own evidence, traceability, sensitivity and gate standards?

The maintainers then reproduced the deterministic findings, fixed the material defects, strengthened the executable example, and added a one-command verifier plus CI. These are independent reasoning contexts, but they are still maintainer-commissioned AI reviews—not an external certification.

## Current scores

| Area | Grade | Evidence and limits |
|---|---:|---|
| Doctrine coherence | A- | Substantive normative baseline, clear hard rules, linked map and consistent hierarchy. It remains deliberately broad. |
| Practical workflow | B+ | Four bounded skills, templates, a release checklist and an adoption path. Real-world team usage is not yet measured. |
| Executable evidence | A- | Ten requirement-facing tests pass; one deliberate boundary mutant causes exactly the expected one failure. This proves one suite can detect one seeded defect, not full correctness. |
| Traceability | B+ | The example maps acceptance obligations to named executable tests and a verification record. Production evidence is represented, not integrated. |
| Portability | B | Native Codex and Claude paths plus namespaced Cursor, Copilot and generic-agent setup. Every vendor UI/version has not been exercised end to end. |
| Reproducibility | B- | Repository structure, local links, skill metadata, example tests and mutant expectation run in one command and CI. Behavioural agent probes still lack full replay bundles. |
| Gate governance | B+ | N/A and waiver semantics are explicit; agents cannot approve their own high-consequence exceptions. Enforcement remains procedural. |
| Adoption evidence | C | No published longitudinal evidence yet from independent repositories, teams or languages. |

## Reproduce the deterministic evidence

Prerequisite: Python 3.8 or later.

```sh
python scripts/verify_repo.py
```

The verifier fails unless:

- required v0.1 artefacts exist;
- local Markdown file and anchor links resolve;
- fenced code blocks are balanced;
- every skill has required frontmatter;
- all ten tests pass against the correct payment example; and
- the deliberate `>=` to `>` mutant causes exactly one failure in the exact-threshold test.

The same command runs in [GitHub Actions](.github/workflows/verify.yml).

## Important fixes made because of the review

- Replaced collision-prone portable installation paths with a `.smarttest/` namespace.
- Removed the copied-skill dependency on an absent template.
- Expanded the payment example from a boolean sketch to distinct authorization, audit, pending-state, no-premature-execution and idempotency behaviours.
- Connected acceptance obligations to actual test names and results.
- Made evidence provenance and design decisions first-class traceability fields.
- Prevented a waiver from masquerading as a passing release decision.
- Ratified and made the doctrine navigable.
- Added deterministic verification and CI.

## What this grade does not claim

SmartTest does not guarantee correct software. Its example does not exercise a real bank, identity provider, audit store or production environment. The behavioural agent evaluation is promising but too small and insufficiently archived to prove consistent outcomes across models. v0.1 should therefore be treated as a strong beta to inspect, try on a bounded change, and challenge—not as a certified assurance system.

If you adopt it, the most useful contribution is evidence: the agent and version used, the repository context, the workflow attempted, the output, what changed in developer behaviour, and any failure or friction you observed.
