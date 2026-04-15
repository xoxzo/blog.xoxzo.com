Title: Systems Should Assume Failure
Slug: systems-assume-failure
Lang: en
Date: 2026-04-15
Tags: SMS, Voice API, API-design, redundancy, system-design, transmission, reliability
Author: Aiko Yokoyama
Thumbnail: images/systems-assume-failure-en.jpg
Summary: Communication does not always succeed. SMS delivery depends on multiple layers including networks and filtering systems. Designing for retries and fallback mechanisms is essential for building reliable systems.

No matter how simple a system looks,
communication does not always succeed.

In fact,

>failure is the default state.

### There is no single reason why SMS fails

SMS may look simple, but in reality it passes through multiple layers:

- sender systems
- API infrastructure
- carrier networks
- recipient networks
- user devices

Each of these layers includes its own safeguards:

- spam filtering
- rate limiting
- security controls

So when a message is not delivered,

>there is always a reason—and rarely just one.

### Perfect delivery does not exist

Networks are unstable.
User environments are unpredictable.
System integrations can fail.

Designing under the assumption of success is risky.

### Designing for failure

Reliable systems are designed with failure in mind.

This includes:

- retry logic
- timeout handling
- status tracking

These are not optional features.
They are essential.

### The role of fallback

Even more important is fallback design.

If SMS fails, another method should take over.

### Voice as an alternative

Voice communication is a strong fallback option.

It works when:

- SMS cannot be delivered
- users do not have smartphones
- only landline phones are available

### Redundancy creates reliability

Combining SMS with voice:

- reduces delivery risk
- expands user reach
- increases system reliability

### Conclusion

Communication systems must assume failure.

- retry
- timeout
- fallback

These are the foundations of reliability.

>Reliable systems are not defined by success,
>but by how they handle failure.