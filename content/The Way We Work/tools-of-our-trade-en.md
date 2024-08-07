Title: Tools of our trade
Date: 2017-10-12 15:00
Author: Iqbal Abdullah
Tags: people; remote work; tool; 2017;
Slug: tools-of-our-trade
Thumbnail: images/tools-of-our-trade/twitter-screenshot.png
Lang: en
Summary: SaaS that we use to manage our business in Japan and abroad as a 100% remote team

Since 2007 we have been working remotely, from all over the planet. Due to the
unique nature of how we work, the tools that we use are doubly important to make
sure we can effectively carry out our daily tasks and support our customers.

Another requirement that we have is that the tools need to be able to process
Japanese other than English, as our Japanese customers mainly speak Japanese.

# Communication

Communication tools are especially important for us, as it requires to replace
the many types of non-text and nuanced office communication that you will
normally have in a physical office.

## Slack

For real-time discussion and conversation, we use Slack. Slack is good when you
want to have a conversation right now in real-time, and also it has simple tools
like reminders which are easy to use. We also actively use Slack's call feature
to have voice and video calls with our team members.

![Slack screenshot]({filename}/images/tools-of-our-trade/slack-screenshot.png)

But if you want to have a more in-depth discussion that spans across time, Slack
might not be the best tool for that. With contextual conversation that is
asynchronous (i.e please send in your monthly project targets, which you check
at the end of the day and questions and answers go back and forth) we just use
plain email.

## Bonusly

In a physical office, you can show appreciation to your team members by saying
thank you and maybe buying them some coffee or bagels when they lend you a
helping hand. We try to reproduce this by using Bonusly, an employee recognition
service.

![Bonusly screenshot]({filename}/images/tools-of-our-trade/bonusly-screenshot.png)

Other than allowing you to give so-called _micro bonuses_ to your team members,
Bonusly also gives us the opportunity to increase communication between members,
by making their contribution visible. We do this by connecting Bonusly to our
Slack all-hands channel, and when a bonus is given out, everyone knows.

Bonusly doesn't have a Japanese UI, but since we only use it internally, it's
not really an issue for us.

## Confluence by Atlassian

Confluence is a great tool for you to keep and share knowledge among your team
members. It also has a comment functionality which you can use to point out and
talk about a specific item on the page.

![Confluence screenshot]({filename}/images/tools-of-our-trade/confluence-screenshot.png)

Other than a place to share information, Confluence is also great for
long-winded asynchronous discussion within a specific context. Confluence works
well with JIRA in a way that it adds more context to specific tasks that we
have.

You can have multiple so-called _workspaces_ that can hold different topics. For
us, we have a separate workspace for each product, role and also ad-hoc items
like team camps, where we discuss the agenda and output from the camp.

Personally, I use the English UI of Confluence, but it has multiple languages
which can be set on a per user account. Japanese input is not an issue.

# Customer support and satisfaction

Customer support and satisfaction tools are especially important as they are the
communication lines of us and our customers.

## Help Scout

Our customers mainly talk to us via email, and it's important for us to have
these conversations in the right context, and sharable across the team.

Previously we have been using JIRA Service Desk, Desk.com by Salesforce, and
before that Zendesk, but the conclusion is that these SaaS are too bloated for
our own straightforward requirements. We wanted to control the UX and UI of our
help center, but it is difficult to control the look and feel of the online help
center functionalities which came with these tools.

JIRA Service Desk was especially difficult to use, requiring end users to
register to _their_ help desk software to access their tickets. Of course, you
might be able to change all these via their settings, but understanding JIRA
settings is a challenge in itself.

The email **From** was also difficult to set on all of the tools that we try, with
the exception of Help Scout.

![Help Scout screenshot]({filename}/images/tools-of-our-trade/helpscout-screenshot.png)

We use the English UI of Help Scout, but receiving and replying Japanese email
works just as well.

## Drip

Drip is a wonderful tool that aims to automate email marketing, but for us, it is
more relevant in the context of how we want to increase customer satisfaction and
communication. 

![Drip screenshot]({filename}/images/tools-of-our-trade/drip-screenshot.png)

By setting a few rules and integrating with our system, we can
make Drip send customized and well-crafted email to help our customers move from
different stages of their usage of our product, and send resources
information to them in a timely manner.

Drip's UI is in English, but you can create Japanese emails as well. There are
certain fixed data which can only be written in English, like the requirement
for writing your business address at the bottom of each email: You only have one
space to set that and it's used in _all_ of your outgoing emails regardless.

There is also a slight learning curve as you need to understand the different
functionalities like Workflows, Rules, Forms but once you go through the
tutorial and help pages and get grips on those, it's pretty easy to use and powerful.

I've personally met with Drip's Rob Walling during MicroConf 2017 in Las Vegas.
He's a great guy!

# Public relations

Some of the tools that we use to cultivate relationships and images with the
general public.

## Twitter

A staple now for nearly all organizations, our Twitter account
[@xoxzocom](https://twitter.com/xoxzocom/) is used to send
out short and quick information on our products, general market news, and what
we believe are important to our customers and us. 

![Twitter screenshot]({filename}/images/tools-of-our-trade/twitter-screenshot.png)

## Instagram

Because our product is APIs for the web developer, it is something not tangible.
Instagram puts colors and visual impact on our overall company and product. It
also allows our customers and the general public to see and know the people
behind Xoxzo.

# Development and developer tools

I'll introduce you to some of the SaaS that we use within the engineering team.
As these tools are used only internally, Japanese UI is not a priority.

## JIRA

Previously we were using GitHub with its issues tracker, and before that
Unfuddle but both prove to have been lacking in tracking issues within different
projects and connecting them together.

GitHub revolves around repositories and for our use case, we'll have different
repositories under a single project, which makes it difficult to track issues.

A big requirement for an issue tracker is to have a bird's eye overview of the
different open issues, who are responsible for them and any deadlines which have
passed. JIRA allows us to do that with its powerful issue search functionality.

![JIRA screenshot]({filename}/images/tools-of-our-trade/jira-screenshot.png)

One drawback of JIRA is that the settings are very complicated and not
intuitive. There is a steep learning curve you'll need to overcome, but to their
credit, JIRA's support people have been very responsive and helpful.

## Bitbucket

Bitbucket is part of the Atlassian suite, so after trying out GitHub while
trying to make use of the issues functionality, we've decided to move to
BitBucket which has good integration with JIRA.

You can create a branch straight from the JIRA ticket page, and that branch will
be tracked as part of the ticket. This allows you to see the status of the code
from the JIRA page (i.e is it merged, or is there a pull request?), instead of
having to go back and forth from the ticket page to BitBucket.

## GitHub

We use GitHub to host our public libraries for different languages like
[Python](https://github.com/xoxzo/xoxzo.cloudpy),
[Ruby](https://github.com/xoxzo/xoxzo.cloudruby) or
[PHP](https://github.com/xoxzo/xoxzo.cloudphp) for our [Xoxzo Cloud
Telephony](https://www.xoxzo.com/en/) product. 

![GitHub screenshot]({filename}/images/tools-of-our-trade/github-screenshot.png)

We also use GitHub to host our [blog](https://blog.xoxzo.com/en/)
and [Help Center](http://help.xoxzo.com/en/) pages. These pages are created
using markdown and generated with Pelican.

# Conclusion

There are many SaaS available for the common issues that your business will
face. For us, we needed to have something simple that will fit with the workflow
of our small team, but at the same time will be able to handle different
languages.

Of course, this list is not set in stone. As new requirements come out and new
SaaS becomes available, we'll continue to reiterate with different services to
fit our current workflow of the day.

For nearly all SaaS out there, if your Japanese team can move beyond the English
only UI, there will be many more choices powerful (and much cheaper) choices for
you out there.

