# Build Report — SmartTest v0.1

## Outcome

SmartTest v0.1 provides DevGenie's tool-independent testing doctrine, a practical adoption path, verified setup guidance for four coding-agent families, a 28-check release checklist, three templates, four focused agent skills, a documented evidence chain, a zero-dependency executable example, and public launch material. No DevGenie product, hosted service, test framework, package, or automated installer was introduced.

## Source and scope decisions

- The supplied DevGenie Testing Doctrine v2 was treated as normative.
- No substantive conflict was found between the doctrine and build brief.
- The brief's fixed-size release checklist was reconciled with the doctrine's risk-based approach by requiring every item to be completed, marked N/A with rationale, or explicitly waived.
- The public repository name is **SmartTest**. DevGenie remains the originating brand in descriptions, doctrine context, and contribution guidance.
- The original language-neutral example remains the authoritative teaching evidence chain. A separate, minimal Python example was added because public adopters need to see a real passing suite and a deliberately failing boundary mutant.
- Apache License 2.0 was selected by the repository owner after the initial v0.1 build. The standard licence text is included without inventing a copyright-holder name or adding an optional `NOTICE` file.
- The public repository is [SmartgenieUK/SmartTest](https://github.com/SmartgenieUK/SmartTest) with `main` as its default branch. The local source directory remains `C:\localcode\devgenietesting` as directed.
- Owner-supplied seed inputs remain on disk but are excluded by `.gitignore` from the public repository tree.

## Artefacts created

```text
.
├── .github/
│   ├── copilot-instructions.md
│   └── pull_request_template.md
├── .gitignore
├── README.md
├── AGENTS.md
├── BUILD_REPORT.md
├── CONTRIBUTING.md
├── EVALUATION_REPORT.md
├── LICENSE
├── adapters/
│   ├── copilot/copilot-instructions.md
│   └── cursor/smarttest.mdc
├── docs/
│   ├── ADOPTION_GUIDE.md
│   ├── AGENT_SETUP.md
│   ├── INTRODUCING_SMARTTEST.md
│   └── LAUNCH_KIT.md
├── doctrine/
│   └── TESTING_DOCTRINE.md
├── checklists/
│   └── AI_CODE_RELEASE_CHECKLIST.md
├── templates/
│   ├── TEST_PLAN_TEMPLATE.md
│   ├── REQUIREMENT_TEST_TRACEABILITY_TEMPLATE.md
│   └── AI_CODE_DEFINITION_OF_DONE.md
├── skills/
│   ├── test-plan/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── test-impact/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── test-review/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── debug-causal/
│       ├── SKILL.md
│       └── agents/openai.yaml
└── examples/
    ├── payment-approval/
    │   ├── README.md
    │   ├── REQUIREMENT.md
    │   ├── TEST_PLAN.md
    │   ├── TRACEABILITY.md
    │   └── RELEASE_EVIDENCE.md
    └── payment-approval-python/
        ├── README.md
        ├── payment_approval.py
        ├── payment_approval_mutant.py
        └── test_payment_approval.py
```

The four `agents/openai.yaml` files are thin, optional discovery metadata created by the prescribed skill scaffolder. They add no tool dependency; each canonical `SKILL.md` remains usable as plain Markdown by any coding agent. Agent-specific mechanics otherwise remain in setup guidance and thin adapters so that the canonical method stays portable.

The repository root also retains the owner-supplied `DevGenie-Testing-Codex-Seed.zip` and standalone `DEVGENIE_TESTING_DOCTRINE_V2.md` source file locally. They are unmodified build inputs and are ignored for publication.

## Doctrine fidelity review

The repository preserves all 1,479 source lines. Fourteen formatting-only changes normalize principles T1–T14 from level-three to level-two headings, removing an H1-to-H3 hierarchy jump without changing wording.

| Distinctive concept | Preserved in doctrine | Operationalized in |
|---|---|---|
| Testing Addressed | Yes | Agent rules, checklist, test plan, Definition of Done |
| Verification vs validation | Yes | README journey, checklist, test-plan workflow |
| Requirements traceability | Yes | Traceability template and worked example |
| Existing test ownership | Yes | Agent rules, test plan, test-plan and debug skills |
| Positive, negative, boundary, and failure testing | Yes | Checklist, test plan, worked example |
| Independent verification | Yes | Checklist, Definition of Done, test-review skill |
| Tests must be capable of failing | Yes | Checklist, test-review skill, mutation example |
| Multi-dimensional coverage | Yes | Doctrine and README distinction |
| Risk-based assurance | Yes | All templates and skills use proportionate application |
| Change-impact verification | Yes | Agent rules, checklist, test-impact skill |
| Causal debugging | Yes | Agent rules and debug-causal skill |
| Operational validation | Yes | Test plan, checklist, Definition of Done, example |
| Evidence over assertion | Yes | Traceability, release evidence, skill outputs |
| Tool independence | Yes | Plain Markdown canonical artefacts; no required vendor |

## Usability review

A developer arriving without context can determine within five minutes:

1. **What it is:** the first README paragraph defines the toolkit and its independence.
2. **Where to start:** the numbered five-minute journey links to a ten-minute trial and actionable artefacts.
3. **How to create a test plan:** the journey links the template and `test-plan` skill.
4. **How to review a change:** the journey sequences `test-impact` and `test-review`.
5. **How to use a skill:** the setup guide gives exact locations and invocations for Codex, Claude Code, Cursor, GitHub Copilot, and generic agents.

The documented payment example demonstrates the complete requirement → plan → traceability → evidence journey. The Python companion demonstrates executable boundaries, dependency failure, authorization, duplication, and a deliberately detectable mutation without third-party dependencies.

Public-repository essentials now include contribution guidance, a pull-request template, agent adapters, source-input exclusions, explicit scope boundaries, and an honest licence notice.

## Internal consistency review

Repository-wide searches and manual review found no statement that:

- makes executable tests mandatory for literally every change;
- treats test count, code coverage, or a green pipeline as proof;
- requires a commercial tool;
- treats review by the same AI context as automatically independent;
- reduces a gate or release decision to an unexplained boolean.

N/A decisions and waivers require rationale. “PASS” is tied to criteria and evidence. The fictional release record remains clearly illustrative; the separate executable example is clearly labelled teaching code and does not imply that a payment system was exercised.

## Validation evidence

- Required brief paths: **16/16 present** before adding this report.
- Public repository candidate: **37 files**, excluding the two ignored owner-supplied build inputs and Python cache artefacts.
- Release checklist: **28 actionable checks**, within the required 20–30 range.
- Doctrine concepts checked: **16/16 present** in the normative document.
- Doctrine comparison: **1,479/1,479 lines retained**; exactly 14 differences, all verified heading-prefix normalization.
- Skills: all four contain valid hyphen-case names, descriptions, required workflow sections, outputs, escalation conditions, anti-patterns, and examples; no scaffold placeholder remains.
- Markdown: all **27** public Markdown files have H1 headings, balanced code fences, and valid heading hierarchy.
- Relative Markdown links: **61 checked, 0 unresolved** after final repository validation.
- Required payment cases: £9,999.99, £10,000, £10,000.01, dependency unavailable, unauthorized approval, and duplicate request/decision are all present.
- Executable example: **6/6 tests pass** against the correct implementation; the deliberate `>=` to `>` mutant exits non-zero with exactly the expected boundary test failure.
- Forward evaluation: `test-plan`, `test-impact`, `test-review`, and proportionate low-risk behaviour passed their representative probes. The initial causal-debug probe found a premature proof claim; after strengthening the proof gate, a fresh rerun correctly returned `PARTIALLY SUPPORTED` and named the missing obligations. See [EVALUATION_REPORT.md](EVALUATION_REPORT.md).
- GitHub publication: the public launch commit contains all **37** candidate files; README rendering, the launch article, Apache-2.0 licence, executable test source, repository description, and discovery topics were verified from GitHub after publication.
- Whitespace/structure: no newly authored trailing whitespace was found. Three source-preserved doctrine lines retain Markdown's intentional two-space line breaks.

The skill creator's supplied `quick_validate.py` was invoked but could not start because the bundled Python runtime does not include its `PyYAML` dependency. Its validation rules were inspected and reproduced locally: frontmatter delimiters and fields, allowed keys, hyphen-case names, length limits, and forbidden angle brackets all pass. The metadata generator itself completed for all four skills.

## Acceptance criteria

- [x] Required repository structure exists.
- [x] README provides a clear five-minute adoption path.
- [x] Doctrine v2 is preserved and navigable.
- [x] Release checklist contains 20–30 concrete checks.
- [x] Test Plan Template can be used without additional explanation.
- [x] Traceability template links intent to evidence.
- [x] Definition of Done is concise and tool-independent.
- [x] Four skills are independently usable.
- [x] AGENTS.md contains the minimum non-negotiable testing behaviour.
- [x] Worked example demonstrates the methodology end to end.
- [x] Public adoption and contribution guidance is present.
- [x] Codex, Claude Code, Cursor, and GitHub Copilot setup paths are documented from primary vendor guidance.
- [x] Executable teaching code demonstrates that an important test can fail.
- [x] Changed causal-debug behaviour was forward-tested in a fresh agent context.
- [x] A repository-linked launch article and platform-specific promotion kit are included without unsupported performance or adoption claims.
- [x] The public GitHub repository is published and its default-branch contents were verified remotely.
- [x] No commercial testing service is required.
- [x] All relative links resolve.
- [x] Required self-review is complete and findings were fixed.
- [x] BUILD_REPORT.md records the build and review.

## Testing Addressed decision

This release contains documentation, agent instructions, adapters, and a small executable teaching example—not executable DevGenie product behaviour. The teaching code was verified with six unit tests and an expected-failing boundary mutant. The remaining artefacts were verified through source-fidelity comparison, required-path checks, skill metadata validation, behavioural forward tests, checklist counting, scenario checks, contradiction searches, heading and fence checks, link resolution, and manual usability review.

## Unresolved questions

No question blocks the local v0.1 deliverable. A separate `NOTICE` or trademark-use policy can be added later if the owner wants more specific DevGenie attribution or brand guidance; neither is required to apply Apache-2.0.

## Restrained v0.2 recommendations

1. Expand forward tests across several real repositories and agent versions; refine only observed failure modes.
2. Package or automate skill installation only if copy-based adoption produces repeated friction; keep portable Markdown canonical.
3. Add a lightweight committed link and structure checker only if repeated releases make the current validation costly.
4. Gather adopter feedback before adding CI integrations, additional language examples, or product features.
## Post-build adversarial review and remediation

On 2026-08-07, two fresh-context AI coding agents were commissioned to challenge the repository rather than confirm it. One reviewed developer adoption and portability; the other tested the doctrine against its own standards. These were independent reasoning contexts, but they were maintainer-commissioned AI reviews, not external certification.

The pre-remediation assessments were B- / 6.8 for adoption and a conditional 6.7 for doctrine fidelity. Material findings included a copied-skill template path that could not resolve, incomplete generic-agent packaging, unreplayable behavioural evidence, weak waiver semantics, incomplete traceability provenance, and an executable example that did not implement several acceptance obligations it claimed to illustrate.

The remediation added:

- a namespaced `.smarttest/` portable installation for Cursor, Copilot, and generic agents;
- a safe copied-skill fallback when an optional template is absent;
- a ratified, navigable normative doctrine baseline;
- explicit design-decision and evidence-provenance traceability fields;
- non-waivable release obligations and independent human authority for high-consequence exceptions;
- a ten-test payment example covering the inclusive threshold, distinct authorized approval, audit records, retained pending state, dependency failure, no premature execution, idempotency, invalid amounts, and conflicting keys;
- executable traceability and verification records;
- two preserved adversarial audit records and a public report card; and
- a standard-library repository verifier plus GitHub Actions.

Final deterministic command:

```sh
python scripts/verify_repo.py
```

Observed result:

- 33 Markdown files checked for local links and fenced-code structure;
- four skill frontmatter blocks checked;
- correct payment example: 10/10 tests passed; and
- deliberate `>=` to `>` mutant: exactly one expected exact-threshold test failed.

The remaining limitations are explicit in [REPORT_CARD.md](REPORT_CARD.md): the behavioural agent probes do not have a complete replay bundle; vendor discovery has not been exercised across every UI/version; the executable example uses in-memory collaborators; and independent multi-repository adoption evidence is not yet available.

This post-build review does not expand SmartTest into a DevGenie product. It makes the v0.1 evidence more inspectable and the adoption path less fragile.
