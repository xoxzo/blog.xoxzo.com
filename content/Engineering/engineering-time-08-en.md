Title: The Happy Path Is Only the Beginning
Lang: en
Date: 2026-10-05
Category: Engineering
Tags: engineering, system-design, error-handling, user-experience, resilience
Slug: engineering-time-08
Thumbnail: images/engineering-time-08-en.jpg
Authors: Aiko Yokoyama
Summary: When designing a system, we often begin with the ideal flow. But in systems used by real people, connections drop, inputs are incorrect, and external services sometimes fail to respond. Let's think about design that includes what happens when things don't go as planned.

# The Happy Path Is Only the Beginning

Press a button.

The process starts.

The result appears.

When we design a system, we often begin with this kind of ideal flow—the system we want to build working exactly as intended.

Place an order.  
Make a payment.  
Receive a confirmation email.

Enter a phone number.  
Receive an authentication code.  
Enter the code and log in.

Each step proceeds as expected.

Of course, designing this flow properly is important.

But systems used by real people do not always go according to plan.

## What If It Doesn't Arrive?

Let's take a system that sends an authentication code by SMS.

The user enters a phone number.

The system sends an SMS.

The user enters the authentication code.

Authentication succeeds.

That's the expected flow.

But what if the SMS doesn't arrive?

What if the user entered the wrong phone number?

What if the code has expired?

What if the connection drops halfway through?

What if an API doesn't return the expected response?

What happens next is still part of the system.

Do we simply tell the user that something went wrong and stop there?

Do we let them try again?

Do we ask them to check what they entered?

Do we offer another method?

Do we suggest trying again later?

If necessary, can they contact a person for help?

**What happens after something goes wrong is also part of the user's experience of the system.**

## An Error Isn't Necessarily "Exceptional" to the User

From a developer's perspective, an error may be an exception.

For the person using the system, however, it is simply what the system is doing at that moment.

"An error has occurred."

The message appears, and they can go no further.

What matters to the user is not only what went wrong inside the system.

It is also:

**"So, what do I do next?"**

When everything works normally, the system guides the user to the next step.

When something doesn't work, it should still be able to show them what they can do next.

## Preventing Failure and Designing for Failure

Of course, we should work to reduce errors in the first place.

Build stable systems.

Test them thoroughly.

Monitor for problems.

Fix bugs when they appear.

Even so, we cannot eliminate every failure.

Some factors exist outside the system itself.

Network conditions change.

External services can become temporarily unavailable.

And people sometimes enter the wrong information or get confused about what to do.

So perhaps good design is not only about:

**"Building a system that doesn't fail."**

It is also about:

**"Building a system that helps people move forward when something does fail."**

## Draw One More Line Beside the Happy Path

When designing a system, we ask:

"What happens next when the user does this?"

Now put one more question beside it:

**"What if that doesn't happen?"**

What if it can't be sent?

What if it doesn't arrive?

What if there is no response?

What if the input is incorrect?

What if the user stops halfway through?

What if they come back later?

Simply asking this question reveals another line beside the happy path.

That line does not always require a complicated solution.

It might be a button that lets the user try again.

A clear explanation of what happened.

Another communication method.

Or perhaps a path that says:

"From here, a person can help."

The important thing is not to leave the user at a dead end.

## Design Becomes Visible When Things Don't Go as Planned

When a system works exactly as expected, users may never notice its design.

That's probably a good thing.

But when something doesn't go as planned, the design becomes much easier to see.

Does the system show another way forward?

Does it explain what happened?

Can the user try again?

Can they reach a person if necessary?

Moments like these reveal how much thought has gone into the people who actually use the system.

**Designing the happy path is where system design begins.**

But:

**The happy path is not where system design ends.**

## From Xoxzo

Send an SMS.

Make a phone call.

Deliver an authentication code.

APIs make it possible to add these capabilities to a system.

But calling a function is not the end of the design.

What if the message doesn't arrive?

What if the method isn't available?

What if the situation changes?

Only when we think about those possibilities does the capability truly become part of the service.

And there is one more thing worth considering.

A path we don't need today may become necessary in the future.

The number of users may grow.

The service itself may change.

New options may become available.

So how do we build systems that can adapt to those future changes?

Next time, we'll think about:

**"Choose APIs for the Future."**