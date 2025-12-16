Title: Start Small, Protect Properly: Introducing SMS Authentication for “Light Usage”
Date: 2025-12-16
Slug: small-usage
Lang: en
Tags: sms api; 2025; otp api; voice api; light usage;
Author: Aiko Yokoyama
Thumbnail: images/small-usage-en.jpg
Summary: SMS authentication is not just for large-scale services. Even with a small number of users, security should never be compromised. Xoxzo has long supported small businesses and individual developers by meeting the need for “light usage” SMS authentication.

### Start Small, Protect Properly  
### Why Xoxzo Has Continued to Support “Light Usage” SMS Authentication

Xoxzo has been in the industry for many years, but we are not a large company.
We operate fully remotely with a minimal team, and we do not have a particularly “strong” corporate culture.
One of the reasons we have been able to continue for so long is that we have consistently met the needs of customers who want to **“use just a little.”**

---

### The Primary Role of Commercial SMS: Authentication

Today, the most important use of commercial SMS is authentication.
Online banking, insurance services, e-commerce platforms, and various online services all rely on it.
As digital services expand, preventing account takeovers and impersonation has become essential.

In modern society, most people carry their mobile phones at all times.
From an adoption-rate perspective, a mobile phone number may now serve as a more practical identifier of an individual than national ID systems in some regions.

---

### Implementing SMS Authentication Requires an API

To integrate SMS authentication into a service, an **SMS sending API** is typically used.

For large enterprises, this is relatively straightforward:
- They have IT departments
- Dedicated engineers
- Predictable high-volume SMS usage

However, the situation is very different for small businesses, startups, and individual developers.

- The service may not yet be live
- User numbers are uncertain
- Monthly SMS volume cannot be estimated

Under these conditions, it is difficult to even begin discussions that assume large-scale SMS usage.


### Should Small Projects Give Up on SMS Authentication?

Implementing SMS authentication in-house requires more than just writing code.

- Contracts with mobile carriers
- Technical integration
- Administrative procedures

These requirements often make SMS authentication impractical for small projects.

Yet, postponing security measures undermines user trust.
If you have 100 users, you need 100 authentication messages.
Finding a way to handle these “just 100 messages” is a challenge many small projects face.

---

### Xoxzo APIs: Fully Online and Ready to Use

Xoxzo’s API services are fully online and available 24/7.
Anyone can create an account and start using the APIs immediately.

This makes Xoxzo especially suitable for individual developers who build services at night after daytime work.
There are no time constraints or sales processes involved.

Xoxzo uses a prepaid credit system.
You can test the service using the free credits provided upon account creation, then purchase credits starting from JPY 1,000 (excluding tax).
**For corporate customers, invoice-based postpaid contracts are also available upon request.**

Purchased credits are valid for 90 days.
This means that even small-scale usage allows you to implement SMS authentication for approximately three months at a minimal cost.
Credits can be recharged at any time as usage increases, without any sales negotiations or contract paperwork.

---

### An Even Simpler Option: OTP API

In addition to the SMS Sending API, Xoxzo also offers an **OTP API**.

By simply registering your service’s URL, you can easily implement SMS-based one-time password authentication through
[SMS Absolute Authentication](https://www.xoxzo.com/sms-otp/).

The cost is just **JPY 3 per message**, making it one of the most affordable options available.
This is especially well suited for small services and testing environments.

---

### A Backup Plan When SMS Does Not Arrive

One common issue with SMS authentication is when messages fail to arrive.

- Network conditions
- Device settings
- Users who only have landline phones

To address these cases, Xoxzo provides a **Voice API**.

By preparing voice-based authentication as a backup, you can prevent user drop-off when SMS delivery fails.
Both SMS and voice authentication use the same prepaid credits, offering additional convenience.

---

### Supporting Continuous “Light Usage”

Prepaid credits decrease as SMS and voice authentication are used.
If the balance runs out, authentication stops.

To avoid this, Xoxzo allows users to configure **low-balance notifications**.
Each user can set their preferred notification threshold based on their usage pace.

This makes it easy to continue using the service efficiently and without waste.

---

### To Start Small and Protect Properly

OTP API, SMS Sending API, and Voice API.
All of these are designed not only for high-volume usage, but also for **starting small**.

Even when starting small, security should never be compromised.
Xoxzo will continue to support projects that choose to protect their users from day one.
