# Contributing to SmartTest

Thank you for improving SmartTest, DevGenie's portable testing discipline.

## Before proposing a change

1. Read the [testing doctrine](doctrine/TESTING_DOCTRINE.md). It is normative.
2. Check the [v0.1 scope](README.md#scope-and-boundaries). SmartTest is not a DevGenie product implementation or testing framework.
3. Open an issue first when a proposal changes doctrine meaning, adds a dependency or agent-specific integration, or expands scope materially.

## Make a focused change

- Preserve vendor and language portability in canonical artefacts.
- Put agent-specific mechanics in adapters or setup guidance, not in the doctrine.
- Prefer a small example with verifiable evidence over broad claims.
- Keep templates usable without hidden context.
- Do not add a mandatory commercial service.
- Record deliberate N/A decisions and limitations.

## Verify the contribution

Use the pull-request template and address testing explicitly. At minimum:

- verify every changed relative Markdown link;
- check heading hierarchy and balanced code fences;
- run affected executable examples;
- forward-test changed skill behaviour with a fresh agent context when practical;
- confirm names, commands, and discovery locations against primary vendor documentation when changing an adapter;
- inspect the diff for doctrine contradictions and unrelated scope.

For a changed skill, test the behaviour that motivated the edit, not only the frontmatter or file shape. Record prompts, observed outcomes, remaining weaknesses, and any correction made after evaluation.

## Pull requests

Explain the intent, risk, affected artefacts, verification evidence, and residual uncertainty. A green pipeline or high coverage number is not, by itself, evidence that the change meets its requirement.

## Licence

SmartTest is licensed under the [Apache License 2.0](LICENSE). Unless explicitly stated otherwise, contributions intentionally submitted for inclusion are provided under the same licence.
