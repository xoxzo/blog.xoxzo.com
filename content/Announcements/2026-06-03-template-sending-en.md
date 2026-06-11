Title: Introducing SMS Templates
Date: 2026-06-03
Slug: template-sending
Lang: en
Tags: template; xoxzo; releases; 2026;
Author: Aiko Yokoyama
Summary: Xoxzo now offers SMS Templates, allowing users to create and manage reusable SMS content with dynamic variables. The feature helps improve operational efficiency while supporting reliable and consistent messaging workflows.


# Introducing SMS Templates

We are pleased to announce the release of SMS Templates, a new feature designed to make SMS messaging more efficient and reliable.

With SMS Templates, frequently used message content can be registered in advance and reused whenever needed.

## What are SMS Templates?

SMS Templates allow you to create reusable message formats for common communication workflows, including:

* One-time passwords (OTP)
* Appointment reminders
* Delivery notifications
* System alerts

Templates may contain variables that are replaced with dynamic values when messages are sent.

Example:

```text
Hello {{name}},

Your appointment is scheduled for {{date}}.

Thank you.
```

## Approval Workflow

Newly created templates are initially placed in a Pending status.

After review by the Xoxzo team, approved templates become available for message delivery.

If an approved template is modified, it will automatically return to Pending status and require re-approval.

## Why are we introducing this feature?

SMS remains one of the most effective communication channels available today. At the same time, maintaining service quality and preventing misuse are essential responsibilities for any messaging platform.

The SMS Templates feature helps us provide:

* Better message consistency
* Improved operational efficiency
* More reliable service delivery

while continuing to support legitimate messaging use cases.

## Availability

The feature will be rolled out gradually to eligible users.

### Additional note: Impact on Existing Users (2026-06-11)

The introduction of SMS Templates does not affect approved users who are already sending SMS messages through Xoxzo.

Users whose use cases have already been reviewed and approved may continue to send free-form SMS messages using the existing API, just as before.

New users are encouraged to use SMS Templates for sending messages, while approved users can continue using their existing workflows (Freeform SMS sending) without changes.

For more information about SMS Templates and the sending API, please refer to the documentation below.

[SMS Templates Documentation](https://docs.xoxzo.com/en/smstemplates)

If you have any questions regarding your account or sending options, please feel free to contact our support team.

