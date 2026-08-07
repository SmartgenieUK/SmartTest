---
name: test-impact
description: Determine the plausible blast radius of a code or configuration change and derive proportionate regression obligations. Use when reviewing a diff, planning verification for an implementation, changing shared contracts, or investigating downstream risk beyond edited lines.
---

# Test Impact

## Purpose

Determine what a change could affect beyond its edited lines and derive evidence needed to protect plausible downstream behaviour.

## Use when

- Reviewing a proposed or completed behaviour-bearing diff.
- Changing shared libraries, contracts, schemas, policies, or configuration.
- Selecting focused and broader regression scope.
- Checking whether local tests miss downstream consumers or operations.

## Inspect

Inspect:

1. Change intent, acceptance criteria, and the complete diff.
2. Repository architecture, ownership, and dependency conventions.
3. Changed symbols, behaviour, interfaces, configuration, and data shape.
4. Direct callers, consumers, existing tests, and test fixtures.
5. Shared contracts, schemas, events, callbacks, middleware, observers, and handlers.
6. Persistence, migrations, transactions, caching, permissions, and security boundaries.
7. Deployment, feature flags, jobs, monitoring, and external operational dependencies.

Report search limits and unavailable repositories or environments.

## Procedure

1. Separate changed behaviour from mechanical edits.
2. Identify direct consumers and the behaviour each relies on.
3. Follow shared or reused contracts across component and service boundaries.
4. Trace indirect activation through callbacks, middleware, observers, events, retries, jobs, and caches.
5. Inspect schema, persistence, transaction, and migration implications.
6. Inspect authentication, authorization, privacy, and trust-boundary implications.
7. Inspect configuration, feature flags, deployment order, observability, and rollback assumptions.
8. Rank plausible effects by consequence, likelihood, coupling, reversibility, and existing evidence.
9. Map each material risk to focused, integration, system, or operational regression evidence.
10. Stop tracing when architectural evidence makes further effects implausible; do not impose a fixed graph depth.
11. Distinguish verified effects from assumptions and unknowns.

## Required output

Return:

- changed behaviours, excluding mechanical noise;
- affected components and why;
- affected contracts, interfaces, data, and operational assumptions;
- risks, confidence, and supporting repository evidence;
- required focused and broader regression evidence;
- explicit unaffected areas when evidence supports that conclusion;
- items that could not be verified.

Do not claim an impact absent or present solely from filename proximity.

## Stop or escalate

Escalate when:

- change intent and observed diff materially disagree;
- a consumer, contract, schema, or deployment dependency cannot be inspected and could create high-consequence impact;
- migration, security, or release-order decisions require authority outside the task;
- the change crosses an unknown trust or data boundary.

## Anti-patterns

- Review only edited functions.
- Use a fixed number of dependency hops.
- List every repository file without explaining plausible behaviour impact.
- Infer safety from passing unit tests around the edited code.
- Treat mocks as proof of interface compatibility.
- Present assumptions as verified facts.
- Recommend the entire test suite without a risk-based reason.

## Compact example

A change from `amount > 10000` to `amount >= 10000` directly affects the payment policy. Plausible indirect effects include approval-request creation, authorization checks, duplicate-event handling, execution blocking, audit events, UI status, and monitoring at the threshold. Evidence should pair focused boundary tests with real approval integration and regression of payment execution; an unrelated reporting export is excluded only if it consumes settled payment state rather than approval eligibility.
