Title: What Do Humans Design When AI Writes the Code?
Lang: en
Date: 2026-09-21
Category: Industry
Tags: ai, engineering, system-design, software-development, requirements
Slug: ai-coding-what-humans-design
Thumbnail: images/ai-coding-what-humans-design-en.jpeg
Authors: Aiko Yokoyama
Summary: As AI makes coding faster, deciding what to build and what success looks like may become even more important. What should humans design in the age of AI—and could AI help us with that earliest stage of design as well? Let's think about the "far left" of software development.


# What Do Humans Design When AI Writes the Code?

## Starting with "Shift Left"

Recently, I received an invitation to a webinar about a "shift-left approach to development in the AI era."

AI-assisted coding is dramatically increasing the speed at which code can be implemented.

But if we can create more code, faster, the burden of reviewing, testing, and finding problems in all that code later in the development process can also grow.

One response is to move quality checks earlier in the development process.

In other words:

**"Shift left."**

The webinar introduced approaches such as applying the same kinds of quality checks traditionally performed by human development teams to AI-generated work, and defining acceptance criteria for APIs as contracts before implementation begins.

That makes sense.

AI builds.

AI checks.

Development gets faster.

But as I read about it, another question came to mind.

**What is even further to the left?**


## Building Faster Is Not the Same as Building the Right Thing

Ask AI:

"Build this."

And sometimes, it can turn that request into something real with astonishing speed.

But:

**Building faster is not the same as building what we actually wanted.**

This is not unique to software development.

Imagine commissioning an illustration.

Even a highly skilled illustrator cannot necessarily create exactly what the client has in mind from an instruction as simple as:

"Please draw a cute girl."

How old is she?

What is she wearing?

Where is she?

What expression does she have?

What pose is she in?

What should the illustration emphasize most?

The more specific the instructions become, the closer the creator's and the client's ideas of "finished" become.

The same may be true for AI.

In fact, precisely because AI can work so quickly, if we start with an ambiguous request,

**it may produce something that is "not quite what we wanted" at astonishing speed—before we even have time to correct its course.**


## Who Decides What AI Should Build?

AI writes the code.

AI runs the tests.

But who decides:

**what should be built?**

Who will use it?

What should they be able to do?

In what order will they use it?

What should happen in different situations?

Who should be allowed to see what?

At what point can we call it "complete"?

What counts as a failure?

If these things have not been decided, AI cannot determine whether what it created is correct.

If testing is going to be automated, then before that happens, someone needs to define:

**what counts as passing.**

If AI continues to accelerate implementation and verification, perhaps the work that comes before all of it—

**deciding what to build and what success looks like—**

will become even more valuable.


## "I Want to Send SMS" Is Not Yet a Specification

Suppose someone says:

"I want a system that can send SMS messages."

Xoxzo's SMS API can send SMS messages.

But what is the person actually trying to accomplish?

Perhaps the real goal is:

**"I want to reduce missed appointments."**

That immediately raises more questions.

Who should receive the message?

When should it be sent?

How many days before the appointment?

At what time?

What should the message say?

Should it explain how to change the appointment?

What happens if the SMS cannot be delivered?

What happens if the appointment is rescheduled?

What happens if it is cancelled?

And:

**How will we know that we have successfully reduced missed appointments?**

What began as:

"I want to send SMS"

gradually becomes a description of the system we actually want to build.


## Could We Do That Work Together with AI?

That led me to another thought.

If clearly defining what we want to build becomes increasingly important,

**could AI help us with that work too?**

Imagine someone who knows nothing about programming saying:

"I want a system that reduces missed appointments."

AI asks:

"Who will use it?"

The person answers.

AI asks the next question:

"When would you like to notify them?"

The person answers.

"What should happen if the appointment changes?"

They answer.

"What if the SMS cannot be sent?"

"Would the system be complete if it could do all of this?"

Like turning over cards one at a time, the person simply has a conversation with AI in ordinary language.

They do not need to understand the technical details of requirements engineering.

But behind that conversation, information is gradually being structured into:

Requirements.

User flows.

Necessary data.

Permissions.

Exceptions.

Acceptance criteria.

Test cases.

If something is missing or contradictory, AI can ask:

**"What should happen in this case?"**

What if we could work that way?


## Opening Up the "Far Left" of Development

If we think about it that way, future development might begin with a very human thought:

**"I wish we had something like this."**

And then move through:

Human idea

↓

Conversation with AI

↓

Requirements

↓

Specifications and acceptance criteria

↓

Implementation by AI

↓

Verification by AI and CI

Of course, this does not mean humans no longer need to think.

Quite the opposite.

Whose problem are we trying to solve?

What matters to them?

What outcome would make things better?

The answers to those questions come from people.

But AI could help translate those answers into the language needed to build a system.

If that happens, more people may be able to participate in the earliest stages of software development—stages that have traditionally required specialized knowledge.


## The AI Era Takes Us Back to the Beginning

AI may continue to reduce the cost of:

"How do we build it?"

And that may make some very old questions even more important:

**"What should we build?"**

**"Why are we building it?"**

**"Who are we building it for?"**

**"What does success look like?"**

With new technology, it can feel as though we are moving toward the newest frontier of software development.

And yet, perhaps we are actually returning to its very beginning.

**Back to the first questions we needed to answer all along.**


## From Xoxzo

An API is a building block for accomplishing something.

Sending an SMS.

Making a phone call.

Authenticating a user.

Those actions are not necessarily the real goal.

Behind them, someone wants to:

Reduce missed appointments.

Deliver important information.

Make authentication easier to use.

Those human goals do not disappear when AI starts writing the code.

If anything, as building becomes easier,

**the time we spend deciding what should be built may become even more important.**

And perhaps AI can help us with that difficult first step too.

**What do humans design when AI writes the code?**

Maybe the answer lies somewhere before the code even begins.