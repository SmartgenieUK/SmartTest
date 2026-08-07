# Your AI-Generated Tests Are Green. What Did They Prove?

AI has radically changed how code is engineered.

We have moved well beyond faster autocomplete. Coding agents can now read a requirement, inspect a repository, plan a change, write the code, run commands, fix errors and prepare the pull request.

This is Agentic Code Engineering. It is not perfect, but it is already changing what one developer can produce and how quickly a team can move.

Testing has not necessarily made the same leap.

Yes, an agent can generate test files. It can add mocks, increase coverage and return a satisfying green result. But generating more tests is not the same as improving the way we decide what should be tested.

In many teams, the code is being engineered in a new way while the thinking behind testing is still largely unchanged.

That gap matters.

## Let's be honest: writing tests can be boring

Most developers enjoy making something work. There is a visible result. A feature appears, a problem disappears or a user can do something they could not do yesterday.

Writing tests often feels different.

It can be repetitive. The interesting implementation problem has already been solved. Now there are fixtures to create, dependencies to fake, edge cases to imagine and assertions to maintain.

Good tests are valuable, but writing them is not always the part of the job people are excited to start.

Under time pressure, that makes testing easy to reduce to a routine:

- add a happy-path test;
- cover the new lines;
- make the pipeline green;
- move on to the next change.

AI makes the shortcut even more tempting. We can ask the same agent that wrote the code to "add tests" and receive a polished suite a few seconds later.

Job done. Or so it appears.

## Generating tests is not independent verification

If the agent misunderstands the requirement, it can write the wrong behaviour and then write tests that confirm the same misunderstanding.

The implementation and the tests agree. The pipeline is green. The defect remains.

This is not a rare or exotic kind of failure. It follows naturally from giving one context responsibility for interpreting the requirement, implementing it and judging whether the result is correct.

The danger is not only a test that fails.

The more dangerous test may be the wrong test that passes.

## Even when you care, a good test is hard to write

Suppose you genuinely want to test a change properly. Where do you begin?

You need to understand the requirement, identify the source of truth and decide which outcomes matter. You need to think about boundaries, invalid input, permissions, failure recovery, integrations, stored data, concurrency and operational behaviour.

You also need to decide how much evidence is proportionate. A wording change and a payment-authorisation rule should not receive the same treatment.

Then there is the hardest question of all:

> Would this test actually detect the defect we care about?

Test syntax is usually the easy part. Choosing the right test is an engineering judgement.

That judgement varies between people, teams and deadlines. Give the same change to two developers and you may get two completely different levels of evidence, even when both are acting in good faith.

So asking AI to produce tests faster does not solve the deeper problem. We first need a consistent way to decide what good testing looks like.

## What we need is a testing doctrine

A testing doctrine is a shared set of principles for turning intent and risk into evidence.

It should not be tied to one language, framework, test runner or coding agent. Those will change. The principles should survive the tool change.

A useful doctrine should answer questions such as:

- Does verification begin with the requirement or with the finished implementation?
- How does the required evidence change with risk and consequence?
- Which positive, negative, boundary, permission, integration and operational cases must be considered?
- How is each important claim traced to evidence?
- How do we show that an important test can detect a relevant defect?
- What must happen before a suspected root cause can be called proven?
- How do we report missing evidence and uncertainty honestly?

There may not be one perfect doctrine for every organisation. But teams should not have to invent the foundations from a blank page.

The ideal starting point would be rigorous enough to improve decisions, light enough for developers to use and practical enough for a coding agent to apply consistently.

Most importantly, it should not sit unread in a wiki.

## One principle: prove that an important test can fail

A complete doctrine contains several connected principles. Let us take just one.

> For an important behaviour, demonstrate that the relevant test fails when that behaviour is deliberately broken.

Consider this requirement:

> Payments of GBP 10,000 or more require secondary approval.

An agent implements the rule so that approval is required only when the payment is greater than GBP 10,000.

It writes one test for GBP 9,999 and another for GBP 10,001. Both pass. The changed code is exercised. Coverage looks healthy.

But nobody checks exactly GBP 10,000.

The words "or more" created a boundary obligation. Because the obligation was not made explicit before the code and tests were written, both share the same mistake.

Now add an exact-boundary test and deliberately run it against the faulty rule. It should fail. Restore the correct rule and it should pass.

That gives us a precise evidence statement:

> This test can detect the loss of secondary approval at the GBP 10,000 boundary.

It does not prove that the whole payment system is correct. It proves one useful thing against one relevant defect.

That is stronger than simply saying that all the tests are green.

You do not need to mutate every line of every application. Use the principle where failure matters: money movement, authorisation, data loss, migrations, external contracts, concurrency, safety controls and regressions that have already reached users.

The aim is not more tests. The aim is better evidence.

## The doctrine should appear automatically

A doctrine will not make testing consistent if developers have to remember a long document every time they touch code.

It needs to appear at the point of work.

When an agent plans a change, the doctrine should prompt it to examine intent, risk and boundaries. When the agent reviews a diff, it should look beyond the edited files and connect claims to evidence. When it investigates a defect, it should distinguish a plausible story from a proven cause.

With a compatible coding agent, repository instructions can be loaded automatically when work begins. Focused skills can guide planning, impact analysis, test review and causal debugging. If an agent does not support skills, the same instructions can still be followed as ordinary Markdown.

This does not remove engineering judgement or guarantee correctness. It makes the good questions much harder to forget.

Wouldn't it be useful if the team could choose a sound doctrine once and have it applied consistently as part of everyday Agentic Code Engineering?

## Meet SmartTest

SmartTest is DevGenie's ready-made, open-source implementation of that idea.

It packages a complete testing doctrine into practical repository instructions, coding-agent skills, templates, checklists and worked examples.

It includes workflows for:

- deriving test obligations before implementation;
- assessing the wider impact of a code change;
- reviewing whether tests genuinely support the claims being made;
- debugging with a real causal proof threshold;
- tracing requirements to evidence;
- making an evidence-based release decision.

It is not another test runner or a hosted quality dashboard. It works alongside the tools a team already uses.

It may sound almost too convenient: take a ready-made doctrine, connect it to your coding agent and start using it on a real change within minutes.

There is no magic involved. SmartTest is a small set of explicit engineering rules made easy for humans and agents to follow. You can inspect every part, keep what improves the work and reject anything that creates ceremony without evidence.

That is exactly how it should be judged.

Want to try SmartTest?

> Send me a connection request and add **SMARTTEST** to the note. Once connected, I'll send it directly to you. Within a few minutes, you should be up and running on your first real change.
