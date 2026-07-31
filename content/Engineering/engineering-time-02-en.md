Title: Don't Reinvent the Wheel
Date: 2026-07-31
Category: Engineering
Tags: engineering, system-design, api, software-development
Slug: dont-reinvent-the-wheel
Thumbnail: images/engineering-time-02-en.jpg
Authors: Aiko Yokoyama
Summary: Building everything yourself isn't always the best approach. By combining proven, well-maintained building blocks, engineers can spend more time creating the parts of a service that truly make it unique. That's also part of good system design.

## The Age of Composable Building Blocks

When developing a system, it's easy to think,

*"It would be nice if we had this feature."*
*"Maybe we should build this ourselves."*

Of course, that's technically possible.

But is that feature really something your team should spend time building, operating, and continuously improving?

## A System Is Never Finished

A feature isn't "done" the day it's is released.

As your user base grows, you'll need to improve performance.

Security requirements evolve.

New technologies appear.

Regulations change.

Monitoring, maintenance, and incident response all become part of everyday operations.

Systems continue to evolve over time.

And as your service grows, maintaining every single component at the same level of quality becomes increasingly difficult.

## Where Does Your Value Come From?

Think about services such as:

- A restaurant reservation platform, where the value lies in making reservations simple and convenient.
- An e-commerce site, where the shopping experience matters most.
- A workforce management system, where supporting employees efficiently is the real goal.

Those experiences are the **unique value** each service provides.

On the other hand, many functions are common across countless applications:

- SMS delivery
- Voice calls
- One-Time Passwords (OTP)
- Email delivery
- Payment processing
- Maps
- File storage

Of course, you can build them yourself.

But these are also areas that have been refined and improved by thousands of engineers over many years.

## Designing by Composing

Modern software development isn't about building everything from scratch.

Good design often means using mature, reliable building blocks where appropriate, while focusing your own engineering effort on what makes your service different.

That's also an important architectural decision.

The SMS API, Voice API, and One-Time Password (OTP) API provided by Xoxzo are examples of these shared building blocks.

And they're certainly not the only ones.

Today, developers can choose from countless services, including:

- Payment APIs
- Mapping APIs
- Translation APIs
- AI APIs
- Cloud storage services

By combining proven technologies, you can build faster, reduce operational burden, and spend more time creating the parts of your service that truly matter.

## You Don't Need to Reinvent the Wheel

The goal isn't to build a better wheel.

The goal is deciding where that wheel will take your users, how smoothly they'll get there, and what kind of journey they'll have along the way.

That's where the real joy of system design begins.

---

### Engineering Time

Engineering time is limited.

That's why we should spend it where it creates the greatest value.

Good design isn't only about deciding **what to build**.

It's also about deciding **what doesn't need to be built**.

That, too, is part of good engineering.

In our next article, we'll explore **"Spend Time on Design, Not Features."**
