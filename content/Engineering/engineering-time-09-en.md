Title: Choose APIs for the Future
Lang: en
Date: 2026-10-18
Category: Engineering
Tags: engineering, api, system-design, maintainability, architecture
Slug: engineering-time-09
Thumbnail: images/engineering-time-09-en.jpg
Authors: Aiko Yokoyama
Summary: Building the functionality you need today is important. But a system does not end when it is completed. Pricing changes. Services change. New authentication methods may be needed. Let's think about APIs and system design that leave room for future change.

# Choose APIs for the Future

**It is not enough for a system to work today.**

When building a system, the first question is often:

"What do we need to make this work now?"

We want to send SMS messages.

We want to make phone calls.

We want to authenticate users.

We want to accept payments.

We choose an API that provides the functionality we need and integrate it into the system.

Of course, that is important.

But a system does not end when it is completed.

In many ways, that is when the long life of the system begins.

## Today's "best choice" may not always be the best choice

As a service continues to operate, many things can change.

A telecom provider may change its services.

Pricing may change.

The specifications of a feature you rely on may change.

You may want to add a new authentication method.

As your user base grows, you may need to support use cases that did not exist before.

The approach you choose today may not be the same one you use three years from now.

Does that mean we should predict everything we might need three years from now and build it all today?

Not quite.

## You don't have to build the entire future today

Building every feature you might possibly need someday means spending engineering time on things that may never be used.

Earlier in [this series](https://blog.xoxzo.com/en/2026/07/31/engineering-time-02/), we asked:

"Do we really need to build this?"

The same question applies to the future.

We do not need to build everything today simply because we might need it someday.

What matters is this:

**Preparing for the future does not mean building the finished solution in advance. It means leaving options open.**

## Design things so they can be replaced

Suppose a system needs to send SMS messages.

If different parts of the application call a specific SMS service directly, logic related to that service can gradually spread throughout the system.

Then imagine that, someday, you need to use a different service.

Or the pricing model changes.

Or you want to add another communication channel.

The number of places you need to change may grow as well.

Instead, if you separate:

"send a message"

from:

"which service should send it"

you may be able to reduce the impact of future changes.

It is perfectly fine to use only one API today.

But you can still leave room to replace it or add another option later.

**One choice today does not have to mean one choice forever.**

That, too, is part of design.

## Authentication methods change, too

In [Episode 7](https://blog.xoxzo.com/en/2026/09/14/engineering-time-07/), we considered the idea that:

"There Is No Single Best Authentication Method."

SMS authentication may be enough today.

But someday, you may want to add passkeys.

You may need voice authentication as another path.

You may want to combine another identity verification method.

If that happens, the lesson is not:

"We should have built all of that from the beginning."

What matters is being able to add another option when it becomes necessary.

If one method can no longer be used, you should be able to consider another.

**Leave room for change in the original design.**

That room becomes preparation for the future.

## When choosing an API, look beyond its features

When choosing an API, it is natural to focus on questions such as:

"Does it have the feature we need?"

"How much does it cost?"

"Can we start using it right away?"

All of these are important.

But for a system that will be used for a long time, it is worth looking a little further ahead.

Can new functionality be added?

Can it work well with the rest of the system?

Can the impact of future changes be kept small?

Will the system remain manageable and maintainable?

And:

**Does using this API narrow our future options?**

An API is not only a way to implement the functionality we need today.

It is also a boundary between our system and the outside world.

How we design that boundary can shape how easily the system responds to future change.

## Design systems that can absorb change

Pricing changes.

Telecom providers change.

New authentication methods appear.

Users develop new needs.

Operational processes change.

We cannot eliminate change.

And we cannot predict every change that will happen in the future.

So perhaps the goal of good design should not be to create a system that never changes.

It should be to create:

**A system that can absorb change.**

Instead of rebuilding the entire system every time something changes:

Replace the part that changed.

Add what is needed.

Remove what is no longer needed.

Leave room for those choices.

## Don't predict the future. Leave options for it.

Good design is not about predicting the future perfectly.

What will we need three years from now?

What technologies will we be using?

Which services will we choose?

We cannot know all of that today.

And that is exactly why we should:

**Avoid deciding the future in advance.**

Build what is needed today while allowing the people of the future to make different choices.

That "future person" might be another engineer.

It might be someone responsible for operations.

It might be a user of the service.

Or it might be you, a few years from now.

The options preserved by today's design become choices those people are free to make.

Engineering time is not only for building today's functionality.

**It can also be invested in giving someone in the future the freedom to make a better choice.**

Next time, in the final episode of Engineering Time:

**"Good Design Gives People Freedom."**

We have explored what to build, what to automate, how to design for failure, and how to preserve choices.

In the final episode, we will ask who all of that design is ultimately for.