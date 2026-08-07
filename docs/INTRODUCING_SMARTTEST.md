# Your AI-Generated Tests Are Green. What Did They Prove?

Testing is meant to be repeatable. The way teams decide what to test often is not.

Give the same change to two developers and you may get two very different answers. One checks the happy path. Another thinks about boundaries, permissions and failure recovery. A third relies on coverage and a green pipeline because the deadline is close.

The variation is rarely caused by a lack of care. Most teams have never agreed a practical testing doctrine that says what good evidence looks like.

AI-assisted development makes that inconsistency faster. A coding agent can turn an unclear requirement into code and tests in minutes. If its interpretation is wrong, the implementation and the tests can still agree perfectly.

The pipeline is green. The software is wrong.

Wouldn't it be useful if a team could start with a strong testing doctrine, make it easy to adopt and have it brought into the development workflow automatically?

That is a more interesting goal than simply asking AI to generate more tests.

Every engineering team already has a testing doctrine, even if nobody has written it down. It lives in daily decisions: what counts as enough testing, which failures matter, when a green pipeline is good enough and what evidence a reviewer needs before approving a change.

When those decisions are explicit, developers, reviewers and coding agents can work from the same rules. When they are not, the doctrine becomes whatever the team happens to do under pressure.
## What should a testing doctrine contain?

There probably is not one perfect doctrine for every product. A medical system and a marketing website do not carry the same consequences. But teams should not have to invent the foundations from scratch.

A strong baseline doctrine should be clear, risk-based, evidence-led, portable across tools and simple enough to use on a real change. Most importantly, it should be operational. A document that nobody consults will not make testing more consistent.

It should answer questions such as:

- Does verification begin with the requirement or with the finished code?
- How should the depth of testing change with risk and consequence?
- Which positive, negative, boundary, permission, integration and operational cases must be considered?
- How is each important claim connected to evidence?
- How do we know that an important test can detect the defect it claims to cover?
- What is required before a suspected root cause can be called proven?
- How are missing evidence, waivers and uncertainty reported?

Those questions form a system. Starting from intent helps identify the right risks. Risk determines how much evidence is proportionate. Traceability shows which claims have support. Honest reporting stops a green status from hiding what has not been checked.

Trying to cover all of that in one article would turn it into a manual. So I want to focus on one principle that is easy to understand, easy to try and surprisingly powerful.

## An important test should prove that it can fail

A passing test does not automatically prove that the test is useful.

It may execute the code without checking the important outcome. It may assert the implementation's current behaviour rather than the requirement. It may miss the exact boundary where the defect lives. In some cases, it may continue to pass even after the intended rule has been removed.

So the principle is simple:

> For an important behaviour, demonstrate that the relevant test fails when that behaviour is deliberately broken.

This is test sensitivity. It asks whether the test is capable of detecting the defect it is supposed to guard against.

## A boundary example

Consider this requirement:

> Payments of GBP 10,000 or more require secondary approval.

Now imagine the implementation only requires approval when the value is greater than GBP 10,000.

The agent writes one test for GBP 9,999 and another for GBP 10,001. Both pass. The changed code is exercised. Coverage looks healthy. But nobody tests exactly GBP 10,000.

The words "or more" created a boundary obligation. Because that obligation was never made explicit, the implementation and the tests share the same mistake.

To check test sensitivity, deliberately replace the correct boundary with the faulty one. The exact-boundary test should fail. Restore the correct rule and it should pass.

That short experiment gives us a precise piece of evidence:

> The boundary test can detect the loss of secondary approval at exactly GBP 10,000.

Notice what it does not prove. It does not prove that the whole payment service is correct. It does not prove that permissions, persistence, integrations or production configuration are safe. It supports one named claim against one relevant defect.

That is much more useful than saying, "All the tests are green."

## How to use the principle

You do not need a full mutation-testing programme to apply this idea. For a material rule or regression, use five steps:

1. Name the behaviour the test is meant to protect.
2. Describe the smallest realistic defect that would violate it.
3. Introduce that defect temporarily, or run the test against the known faulty behaviour.
4. Confirm that the expected test fails for the expected reason.
5. Restore the correct implementation and confirm that the focused and relevant broader tests pass.

This also improves test review. Instead of asking only whether a test exists, the reviewer can ask which defect it would catch and what evidence shows that it can catch it.

It improves regression testing too. A regression test should fail before the correction and pass after it. If it never saw the faulty behaviour, its value is still an assumption.

## Proportion still matters

Not every test needs a deliberate mutant. That would create effort without enough benefit.

Apply the principle where failure has a meaningful consequence: money movement, authorisation, data loss, external contracts, migrations, concurrency, safety controls and defects that have already reached users.

For a spelling correction in documentation, link and structure checks may be enough. A doctrine should increase rigour with consequence, not demand maximum ceremony for every change.

The aim is not more tests. The aim is stronger evidence.

## Why this matters more with coding agents

Before coding agents, implementation and test mistakes could still share an assumption. AI makes the failure mode faster and more convincing.

The same context often produces the requirement interpretation, the code, the tests and the summary telling us that everything is complete. Internal consistency can look like independent verification when it is nothing of the kind.

A testing doctrine gives the agent a different job. It must derive obligations from intent, challenge its own implementation and state exactly what the evidence does and does not support.

That does not make AI-generated code trustworthy by default. It makes the route to a decision more visible and reviewable.

## A doctrine should turn up automatically

A testing doctrine will not improve consistency if developers have to remember a long document every time they change code.

It should appear at the point of work.

For AI-assisted development, that means turning principles into repository instructions and focused agent workflows. When the agent plans a change, it should ask about intent, risk and boundaries. When it reviews a diff, it should check impact and evidence. When it investigates a defect, it should distinguish a plausible explanation from a proven cause.

With compatible coding agents, repository instructions can be loaded automatically when work begins. Focused skills can then guide test planning, impact analysis, test review and causal debugging. Agents without a native skill system can still follow the same portable Markdown instructions directly.

The automation is in applying the doctrine consistently at the right moments. It does not remove engineering judgement, run every testing tool by itself or guarantee that a change is correct.

That boundary matters. The purpose is to make good questions difficult to forget, not to replace the people accountable for the answer.
## A ready-made implementation of the rest

Test sensitivity is only one part of a complete testing doctrine.

SmartTest is DevGenie's ready-made, open-source implementation of the wider discipline. It packages the principles as practical repository guidance, agent skills, templates and examples, so a team can start with a working baseline instead of writing its own doctrine from a blank page.

It includes:

- the full testing doctrine;
- a workflow for deriving test obligations before implementation;
- change-impact analysis that looks beyond the edited files;
- a review method for connecting claims to evidence;
- a causal-debugging workflow with a real proof threshold;
- requirement traceability and Definition of Done templates;
- a release checklist;
- worked and executable examples;
- setup guidance for several coding agents.

It is portable Markdown rather than a testing framework or hosted product. Once configured for a coding agent, it can bring the doctrine into normal planning, implementation, review and debugging work. Teams can use the whole method or adopt the smallest part that improves a real decision.

The best way to judge it is not to agree with the principles. Try it on one bounded change and see whether it exposes a risk or uncertainty that the normal workflow missed.

If it adds ceremony without better evidence, reject that part. Evidence over assertion applies to the doctrine itself.

Want the ready-made doctrine and implementation?

> Comment **SMARTTEST** and send me a connection request. Once connected, I'll DM you the repository and starting workflow.
