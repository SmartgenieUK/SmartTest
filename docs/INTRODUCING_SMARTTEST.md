# What If You Could Get Your Hands on a Full-Blown Testing Doctrine for Your Entire Repository - for Free?

## First things first - Get SmartTest

SmartTest is public and completely free.

Comment **SMARTTEST** below and send me a connection request. Once connected, I'll DM you the repository and quick-start guide. You can try the first workflow on a real change within minutes.


## AI can now change a repository in minutes.

But most teams still decide what to test in the same inconsistent way: developer by developer, change by change and deadline by deadline.

What if every developer and coding agent in your repository could follow one full-blown testing doctrine - already written, practical to implement and completely free?

## Code engineering changed. Testing needs to keep up too.

We have moved beyond autocomplete. Coding agents can inspect a repository, plan a change, edit several files, run commands and prepare a pull request.

This is agentic software engineering: people set direction and remain accountable while agents carry out more of the workflow.

The speed is real. So is the verification problem.

[DORA's research into AI-assisted software development](https://dora.dev/insights/balancing-ai-tensions/) found increased development velocity alongside a significant verification cost. Time saved creating code is often spent auditing it. More output does not automatically create more confidence.

And testing has a human problem too.

Writing tests is rarely the work people queue up to do. The feature is visible. The test setup, fixtures, mocks, awkward dependencies and boundary cases are not.

That does not mean developers do not care about quality. A [survey of 284 professional developers](https://arxiv.org/abs/2309.01154) found that developers were motivated by quality and personal satisfaction, but also found testing mundane and often prioritised other work.

Then AI offers the perfect shortcut:

> Write tests for this change.

A few moments later, everything is green.

But what did those tests prove?

## A green test can protect the wrong behaviour

Imagine this requirement:

> Payments of GBP 10,000 or more require secondary approval.

An agent implements approval for values greater than GBP 10,000. It then writes tests for GBP 9,999 and GBP 10,001.

Both tests pass. The code is covered. The exact boundary is still wrong.

This is the uncomfortable part: if the same agent misunderstands the requirement, writes the implementation and writes the tests, all three can agree with each other.

Coverage does not solve that. Coverage tells us which code ran. It does not tell us whether we chose the right behaviour, boundary or failure.

A [2025 study of LLM-based unit-test generation](https://arxiv.org/abs/2506.02954) reported evaluated suites with 100 percent code coverage but only a 4 percent mutation score. That result belongs to one study and benchmark, but the lesson is useful: executing code and detecting faults are different things.

Even if you want to write a good test, the difficult part is not the syntax. It is deciding:

- what the requirement really means;
- which boundaries and failures matter;
- what could break outside the edited file;
- what mocks cannot prove;
- how much evidence is proportionate to the risk; and
- when a release claim is genuinely supported.

That is not a test-generation problem. It is a testing doctrine problem.

## What a testing doctrine should do

A testing doctrine is a shared way to turn intent, risk and uncertainty into evidence.

It should guide the work before coding starts, while the change is being made, before it is merged and when something goes wrong.

A useful doctrine should make a team answer questions such as:

- What observable evidence would prove this requirement?
- Which positive, negative, boundary, permission and failure cases apply?
- Where does the behaviour already have authoritative tests?
- Which consumers, contracts, data and operations sit beyond the local diff?
- Can an important test detect a relevant defect?
- What is observed, what is inferred and what is still unknown?
- Who can accept missing evidence, and with what consequence?

The answers will differ between a medical system and a marketing site. The underlying discipline does not need to be reinvented in every repository.

Most importantly, the doctrine has to appear during the work. A document hidden in a wiki will disappear when the deadline gets close.

## One principle you can use immediately

Take the payment boundary again.

Add a test for exactly GBP 10,000. Run it against the faulty greater-than rule. It should fail. Restore the correct greater-than-or-equal rule. It should pass.

Now you can make a precise claim:

> This test detects the loss of secondary approval at the GBP 10,000 boundary.

It does not prove the payment system is correct. It proves one useful thing against one relevant defect.

That is test sensitivity. It is stronger than saying the suite is green.

You would not mutate every line of every application. Apply this in proportion to consequence: money movement, authorisation, data loss, migrations, external contracts, concurrency and regressions that have already reached users.

The aim is not more test theatre. It is better evidence.

## The ready-made implementation

This is why I built SmartTest.

SmartTest is DevGenie's free, open-source testing doctrine for AI-assisted software development. It turns the principles into portable repository instructions, focused agent workflows, templates, release checks and worked examples.

The useful part is what it changes in the engineering workflow:

- Before coding, the agent derives what must be proven from the requirement.
- During implementation, it traces risk beyond the files it edited.
- Before merging, it judges the evidence instead of trusting test count or coverage.
- During debugging, it stops a plausible explanation being promoted to a proven cause without a prediction and regression evidence.
- At release, missing proof and waivers stay visible.

"Repository-wide" means the same guidance is available across work in the repository. It does not mean every behaviour is automatically covered.

"Automatic" means compatible coding agents can load the instructions at the relevant moment. It does not mean automatic correctness.

SmartTest works alongside the test runners, CI systems, scanners and review tools you already use. It is portable Markdown, licensed under Apache 2.0, not a test framework, hosted platform or DevGenie product implementation.

And because evidence over assertion must apply to SmartTest too, the repository includes an adversarial report card. It shows the scores, the defects the review found, what was fixed and what remains unproven. One early evaluation found that the causal-debugging workflow could promote a replacement explanation using evidence already observed. We tightened it to require a new, prospectively recorded prediction before a root cause can be called proven. You can run the deterministic checks yourself.

No magic. No guarantee of correctness. No transformation programme.

Try it on one real, bounded change. You can have the first workflow running within a few minutes after installation. If it reveals a risk or uncertainty you would otherwise have missed, keep it. If it adds ceremony without better evidence, challenge it.


