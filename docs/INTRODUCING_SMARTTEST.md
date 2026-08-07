# What If You Could Get Your Hands on a Full-Blown Testing Doctrine for Your Entire Repository - for Free?

What would change if every developer and every coding agent working in your repository followed the same testing principles?

Not simply the same test runner. Not a target coverage percentage. A proper doctrine: one shared way to turn requirements, risk and uncertainty into evidence.

Now imagine that doctrine was already written, practical to adopt, able to work with the coding agent you already use and completely free.

That is the idea behind SmartTest.

But before I tell you what it contains, it is worth asking why a testing doctrine is suddenly so important.

## Code engineering has changed

AI has rapidly changed how software is built.

We have moved beyond autocomplete. Coding agents can inspect a repository, plan a change, edit several files, run commands, fix failures and prepare a pull request.

This is the beginning of Agentic Code Engineering: people set direction and remain accountable, while agents carry out more of the engineering workflow.

The change is real, but it should not be exaggerated. Current agents are not reliable substitutes for experienced engineers on every task. They are, however, producing code faster and taking on more complete pieces of work.

[DORA's research into AI-assisted software development](https://dora.dev/insights/balancing-ai-tensions/) found widespread AI adoption, increased development velocity and a significant verification cost. Time saved during creation is often spent auditing the result. Higher adoption was associated with greater throughput, but also greater delivery instability.

Code generation has accelerated. Confidence has not arrived automatically with it.

## The part of engineering that does not attract a queue

Let us be honest: writing tests can be boring.

That does not mean testing is unimportant or that nobody enjoys it. Many developers care deeply about quality and take real satisfaction from a strong test suite.

But compared with making a feature work, test writing can feel repetitive and less visible. The interesting implementation problem appears to be solved. What remains is setup, fixtures, mocks, awkward dependencies, edge cases and assertions.

A [survey of 284 professional developers](https://arxiv.org/abs/2309.01154) found both sides of this. Developers were motivated by quality and personal satisfaction, but also perceived testing as mundane and tended to prioritise other tasks.

That is a more useful truth than saying developers do not care about tests.

They care about the outcome. The work required to get there competes with features, incidents and deadlines.

AI makes the obvious shortcut irresistible:

> Write tests for this change.

A few moments later, the suite is green.

## More tests do not necessarily mean better evidence

There is a problem with asking the same agent to write the code and then test it.

If the agent misunderstood the requirement, its implementation and tests can share the same mistake. They agree with each other, but neither agrees with what the user actually needed.

Coverage does not solve that problem. Coverage tells us which code ran. It does not tell us whether we selected the right behaviour, boundary or failure mode.

A [2025 study of LLM-based unit-test generation](https://arxiv.org/abs/2506.02954) reported evaluated suites that achieved 100 percent code coverage but only a 4 percent mutation score. That result belongs to a particular study and benchmark, not every codebase, but the lesson is useful: executing code and detecting faults are not the same thing.

Even when a developer genuinely wants to write a good test, the hard part is not usually the syntax.

The hard part is deciding:

- what the requirement actually means;
- where the important boundaries are;
- which failures carry the greatest consequence;
- what happens across permissions, storage and integrations;
- which evidence is proportionate;
- whether the test could detect the defect that matters.

Those decisions vary between people and change under pressure.

That is why we need more than automated test generation.

## What a testing doctrine gives you

A testing doctrine is a shared set of principles for deciding what needs to be verified and what counts as credible evidence.

A useful doctrine should answer questions such as:

- Does verification begin with the requirement or the finished implementation?
- How should testing depth change with risk and consequence?
- Which positive, negative, boundary, permission, integration and operational cases must be considered?
- How is each important claim traced to evidence?
- How do we show that an important test can detect a relevant defect?
- What must happen before a suspected root cause can be called proven?
- How should missing evidence, waivers and uncertainty be reported?

There is no single perfect answer for every organisation. A medical system and a marketing site carry different consequences.

But the foundations do not need to be reinvented for every repository. A strong baseline can be adapted to the product while keeping the underlying engineering obligations intact.

Most importantly, the doctrine needs to appear during the work. If it sits in a wiki waiting to be remembered, it will disappear when the deadline gets close.

## One principle from the doctrine

A full doctrine contains several connected principles. Here is one that can be tried immediately:

> For an important behaviour, demonstrate that the relevant test fails when that behaviour is deliberately broken.

Suppose the requirement says:

> Payments of GBP 10,000 or more require secondary approval.

An agent implements approval only for values greater than GBP 10,000. It writes tests for GBP 9,999 and GBP 10,001. Both pass. The code is covered.

But the exact boundary is wrong.

Now create a test for GBP 10,000 and run it against the faulty rule. It should fail. Restore the correct rule and it should pass.

We can now make a precise claim:

> This test can detect the loss of secondary approval at the GBP 10,000 boundary.

It does not prove the whole payment system is correct. It proves one useful thing against one relevant defect.

That is test sensitivity. It is stronger evidence than a green status alone.

You would not do this for every line of every application. Apply it proportionately where failure matters: money movement, authorisation, data loss, migrations, external contracts, concurrency, safety controls and regressions that have already reached users.

The aim is not the largest number of tests. The aim is better evidence.

## What if the doctrine worked across your repository?

A doctrine becomes much more useful when it is translated into instructions that a coding agent can follow.

When the agent plans a change, it should derive verification obligations from intent. When it reviews the diff, it should examine impact beyond the edited files. When it investigates a defect, it should separate observation from inference and require evidence before declaring a root cause.

With compatible agents, repository instructions can be loaded automatically when work begins. Focused skills can guide test planning, impact analysis, test review and causal debugging. Agents without a native skill system can follow the same portable Markdown directly.

This is not automatic correctness. It is automatic access to a consistent engineering discipline at the moments when it is needed.

That is the gap SmartTest is designed to fill.

## What you get with SmartTest

SmartTest is DevGenie's free, open-source testing doctrine for AI-assisted software development.

It is a ready-made repository containing:

- the complete testing doctrine;
- repository-level guidance for coding agents;
- workflows for test planning, change impact, test review and causal debugging;
- requirement-to-evidence templates;
- an evidence-based Definition of Done;
- a release checklist;
- documented and executable examples;
- setup guidance for several coding agents.

It is portable Markdown, not another test framework, hosted platform or paid dashboard. It works alongside the test runners, scanners, review tools and CI systems a team already uses.

It is licensed under Apache 2.0. You can inspect it, adapt it and use it across your repositories.

Does that sound almost too good to be true?

There is no magic and no claim of guaranteed correctness. What you get is a serious body of testing discipline that has already been turned into practical agent instructions, templates and workflows.

You do not need a transformation programme to evaluate it. Start with one real, bounded change. Within a few minutes, your agent can be using the first workflow. Then judge SmartTest by the evidence it helps you uncover.

If it reveals a risk or uncertainty you would otherwise have missed, keep the useful part. If it creates ceremony without better evidence, reject that part.

Evidence over assertion applies to SmartTest too.

## Get the complete doctrine

> Send me a connection request and add **SMARTTEST** to the note. Once connected, I'll send you the repository and quick-start guide. You can try the first workflow on a real change within minutes.
