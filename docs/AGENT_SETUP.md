# Coding Agent Setup

SmartTest's canonical skills live in [`skills/`](../skills/). They use the open `SKILL.md` convention and remain readable as ordinary Markdown. Native discovery locations differ by agent, so install only the skills you need in the target code repository.

The examples below use copies for portability. Symlinks are also reasonable when your operating system, source-control policy, and agent support them.

## OpenAI Codex

Codex discovers repository skills under `.agents/skills/<skill-name>/SKILL.md` from the repository root. Copy the desired SmartTest skill directories into that location:

```powershell
$smartTestPath = "C:\path\to\SmartTest"
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse "$smartTestPath\skills\test-plan" .agents\skills\test-plan
Copy-Item -Recurse "$smartTestPath\skills\test-impact" .agents\skills\test-impact
Copy-Item -Recurse "$smartTestPath\skills\test-review" .agents\skills\test-review
Copy-Item -Recurse "$smartTestPath\skills\debug-causal" .agents\skills\debug-causal
```

Then invoke a skill explicitly, for example `$test-plan`, or let Codex select it when the request matches its description. Put the repository-wide non-negotiables from [`AGENTS.md`](../AGENTS.md) in the target repository's root `AGENTS.md` if they should apply automatically.

Official references: [Codex skills](https://learn.chatgpt.com/docs/build-skills) and [AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

## Claude Code

Claude Code discovers project skills under `.claude/skills/<skill-name>/SKILL.md`:

```powershell
$smartTestPath = "C:\path\to\SmartTest"
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Copy-Item -Recurse "$smartTestPath\skills\test-plan" .claude\skills\test-plan
Copy-Item -Recurse "$smartTestPath\skills\test-impact" .claude\skills\test-impact
Copy-Item -Recurse "$smartTestPath\skills\test-review" .claude\skills\test-review
Copy-Item -Recurse "$smartTestPath\skills\debug-causal" .claude\skills\debug-causal
```

Invoke a skill with `/test-plan`, `/test-impact`, `/test-review`, or `/debug-causal`. Claude may also load a skill automatically from its description. If the `.claude/skills` directory is created during an active session and is not detected, restart that session; edits inside an already detected skill are live.

Official reference: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Cursor

Cursor project rules use `.cursor/rules/*.mdc`. Copy [`adapters/cursor/smarttest.mdc`](../adapters/cursor/smarttest.mdc) into the target repository as `.cursor/rules/smarttest.mdc`, then keep the canonical SmartTest `skills/` directory available in that repository or adjust the paths in the adapter.

```powershell
$smartTestPath = "C:\path\to\SmartTest"
New-Item -ItemType Directory -Force .cursor\rules | Out-Null
Copy-Item "$smartTestPath\adapters\cursor\smarttest.mdc" .cursor\rules\smarttest.mdc
Copy-Item -Recurse "$smartTestPath\skills" .\skills
```

In chat, ask Cursor to use the relevant SmartTest workflow and name the requirement, diff, or defect. You can also reference the rule explicitly with `@Cursor Rules`. The adapter points Cursor to the canonical skill files instead of duplicating their contents.

Official reference: [Cursor rules](https://docs.cursor.com/context/rules-for-ai).

## GitHub Copilot

GitHub Copilot supports repository-wide instructions in `.github/copilot-instructions.md`. Copy [`adapters/copilot/copilot-instructions.md`](../adapters/copilot/copilot-instructions.md) there and keep the canonical SmartTest `skills/` directory available:

```powershell
$smartTestPath = "C:\path\to\SmartTest"
New-Item -ItemType Directory -Force .github | Out-Null
Copy-Item "$smartTestPath\adapters\copilot\copilot-instructions.md" .github\copilot-instructions.md
Copy-Item -Recurse "$smartTestPath\skills" .\skills
```

Ask Copilot coding agent or chat to read the relevant `skills/<name>/SKILL.md` before acting. Copilot coding agent can also use `AGENTS.md`; the nearest applicable file takes precedence, so copy SmartTest's compact rules into the target repository only when they match local policy.

Official reference: [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions).

## POSIX copy equivalents

On macOS or Linux, set the source once and copy only the integration you use:

```sh
SMARTTEST_PATH=/path/to/SmartTest

# Codex
mkdir -p .agents/skills
for skill in test-plan test-impact test-review debug-causal; do
  cp -R "$SMARTTEST_PATH/skills/$skill" .agents/skills/
done

# Claude Code
mkdir -p .claude/skills
for skill in test-plan test-impact test-review debug-causal; do
  cp -R "$SMARTTEST_PATH/skills/$skill" .claude/skills/
done

# Cursor
mkdir -p .cursor/rules
cp "$SMARTTEST_PATH/adapters/cursor/smarttest.mdc" .cursor/rules/smarttest.mdc
cp -R "$SMARTTEST_PATH/skills" ./skills

# GitHub Copilot
mkdir -p .github
cp "$SMARTTEST_PATH/adapters/copilot/copilot-instructions.md" .github/copilot-instructions.md
cp -R "$SMARTTEST_PATH/skills" ./skills
```

These commands assume the destination does not already contain a SmartTest installation. Review and merge existing rules or skills instead of overwriting local policy.

## Generic coding agents

No native skill mechanism is required. Use a direct prompt:

```text
Read skills/test-impact/SKILL.md in full and follow it for the current diff.
Treat repository requirements and existing tests as authoritative inputs.
Do not implement unrelated changes. Report missing evidence honestly.
```

## Confirm the setup

Run a small behavioural check after installation. A successful discovery banner alone is weak evidence.

1. Ask the agent to plan tests for an inclusive boundary such as “£10,000 or more”.
2. Confirm it includes values below, exactly at, and above the boundary.
3. Give it a green suite with an obvious missing requirement and ask for `test-review`.
4. Confirm it does not equate green status or code coverage with adequacy.
5. Give `debug-causal` a failed prediction and confirm it refuses to label a replacement hypothesis `PROVEN` until a new independent prediction and failing regression exist.

If those behaviours are absent, check that the agent read the canonical skill—not merely the adapter—and that no nearer repository instruction overrides it.
