# Your AI-Generated Tests Are Green. What Did They Prove?

There is a reassuring moment in AI-assisted development.

The agent finishes the change, writes the tests and runs the suite. Everything is green. The report looks tidy, the coverage number is respectable and it feels as though the work is done.

But there is a question we do not ask often enough:

> What did those tests actually prove?

The uncomfortable answer is sometimes: much less than we think.

If the same agent reads the requirement, writes the implementation and creates the tests, all three can share the same misunderstanding. The code does the wrong thing. The tests confirm that it does the wrong thing consistently. The pipeline stays green.

That is the problem SmartTest is designed to tackle.

## A green pipeline can still be wrong

Imagine a simple requirement:

> Payments of GBP 10,000 or more require secondary approval.

An implementation checks for payments greater than GBP 10,000. The agent also writes tests for GBP 9,999 and GBP 10,001, but misses the exact boundary.

Both tests pass. The changed code is covered. The rule is still wrong for a payment of exactly GBP 10,000.

Nothing is wrong with the test runner. It ran the tests it was given. The problem is that nobody turned the words "or more" into an explicit verification obligation.

This is where a lot of AI testing goes wrong. We ask an agent to test the code it has just written instead of first asking what must be true, where the boundaries are and how the result could fail.

## Start with the requirement

SmartTest is a small, open-source testing discipline from DevGenie. It is not another test framework and it does not replace the tools already in your pipeline.

It changes the order of the conversation.

Before implementation begins, SmartTest asks:

- What behaviour has actually been requested?
- Which boundaries and failure paths matter?
- What could go wrong outside the edited file?
- What evidence would support each important claim?
- Could the proposed test detect the defect we care about?
- What will still be uncertain after the tests pass?

That sounds like ordinary good engineering, because it is. The difficulty is applying it consistently when an AI agent can produce plausible code and plausible tests faster than a person can properly challenge the assumptions behind them.

SmartTest gives the agent a repeatable way to do that work without forcing a new platform or a heavyweight process onto the team.

## Four practical jobs

The repository contains four focused workflows.

Test Plan turns a requirement into verification obligations before the implementation shapes the answer.

Test Impact looks beyond the files in the diff. It asks about consumers, contracts, stored data, permissions, integrations and operational behaviour.

Test Review checks whether the available tests support the claims being made. A test count or coverage percentage is not accepted as proof on its own.

Causal Debugging slows down one of the most tempting AI failure modes: finding a plausible fix and immediately calling it the root cause.

These workflows are written as portable Markdown instructions. They can be used with Codex, Claude Code, Cursor, GitHub Copilot or another coding agent. There is no proprietary runtime.

## A test should show that it can fail

The SmartTest repository includes the payment example above as executable Python code.

The correct implementation passes six tests. We then make one deliberate change: the exact boundary is excluded. Five tests continue to pass, while the GBP 10,000 boundary test fails.

That does not prove the entire payment system is correct. It proves something smaller and more useful: this particular test can detect this particular defect.

That level of precision matters. "The tests pass" is a status update. "This test fails when the required boundary is removed" is evidence.

## A working fix is not proof of root cause

The same discipline applies to debugging.

An agent sees a failure, produces a convincing explanation, changes the code and gets a green test. It is very easy to describe the original explanation as proven.

But perhaps the change affected several things. Perhaps the test never reproduced the production failure. Perhaps the explanation was simply one of several stories that fitted the evidence.

SmartTest asks for a falsifiable hypothesis and a prediction recorded before its result is known. It also asks for a failing regression before the correction is applied. If the prediction fails, the hypothesis is not quietly rewritten to match what happened.

Sometimes the honest conclusion is "partially supported" or "not proven". That is not weakness. It is better engineering than a confident story the evidence cannot support.

## Your existing tools still matter

Test runners, static analysis, security scanners, code review, coverage tools and production monitoring all provide valuable signals. SmartTest does not compete with them.

It helps the team decide which questions those tools need to answer.

A green badge is useful when we understand its scope, configuration, freshness and relationship to the requirement. Without that context, it is easy to treat a signal as a conclusion.

This is also where the longer-term DevGenie direction fits. SmartTest establishes what should be proven. Evidence providers supply relevant signals. DevGenie can eventually help make that evidence traceable, reviewable and ready for a decision.

The public repository is the methodology. It is not a DevGenie product implementation.

## Try it on one real change

You do not need a transformation programme to find out whether SmartTest is useful.

Choose one bounded change with a clear acceptance criterion. Before writing code, ask your coding agent to derive the verification obligations. Look at the boundaries, failure paths and assumptions it identifies. Then compare those obligations with the tests and evidence produced after implementation.

Ask one question at the end:

> Did this reveal a risk or uncertainty we would otherwise have missed?

If the answer is no, do not keep the ceremony. If the answer is yes, adopt the smallest useful part of the workflow.

SmartTest is deliberately small, practical and licensed under Apache 2.0. We want developers to challenge it with real work, not simply agree with the idea.

If it finds a gap, tell us what happened. If it creates paperwork without better evidence, tell us that too.

Evidence over assertion applies to SmartTest itself.

Want to try it?

> Comment **SMARTTEST** and send me a connection request. Once connected, I'll DM you the repository and starting workflow.
