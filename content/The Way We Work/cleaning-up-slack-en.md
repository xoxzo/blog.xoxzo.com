Title: Cleaning up Slack: Regaining back our sanity
Date: 2019-04-17 10:00
Author: Iqbal Abdullah
Tags: slack; cleanup; remotework; 2019;
Slug: cleaning-up-slack-and-regaining-our-sanity
Lang: en
Thumbnail: images/library-clutter.jpg
Summary: If you're starting to get overwhelmed using Slack alongside your usual project management tools, you might get some ideas from our experience cleaning it up. 

For a remote and distributed team like us, Slack is important for real-time
information sharing and communication and helps us make decisions in a fairly
timely manner compared to if we exclusively used email. It's basically like IRC
on steriods, if you're old enough to know what IRC is.

If you're also using Slack to communicate with your team members, and start to
find yourself overwhelmed with too many channels, and have been thinking of
doing something about it, this post might be for you.

# Our setup

We have five main tools that we use to communicate and manage our work. One is
Google Suite, (which includes emails, spreadsheets and the word processing). Next is
JIRA, Confluence and Bitbucket for project management and source control, and finally Slack
for online and realtime communication.

# Context based channels and JIRA

When we started using Slack, the most obvious thing to do was to use the channels
feature to separate our conversation within context. You'd talk about devops in
_devops_ , or talk about technical books in _library_ or engineering stuff in
_engineering_ . Things get pretty wild quickly, as we talked about different
stuff each day.

## Come JIRA

We also use JIRA to manage tasks. Now, when we want to talk about the task or
want a quick update, we ask through Slack. It was not long before discussions on
a specific ticket was all over the place: Some in Slack, some in the comments
section of the JIRA ticket. At least we did not use email for these. It was
driving us crazy. We're only a team of eleven people and it was driving us nuts.
I couldn't imagine what will happen if it was double our team size.

## Too many channels

Not long into using Slack, we're getting up to over twenty channels which are
mostly with the same people talking about different things. Some of these
channels stay quiet for weeks at a time.

It was not long before we find ourselves in a clutter of channels and
information lying in different platforms here and there.

![Clutter of books]({filename}/images/library-clutter.jpg)
Photo by Darwin Vegher on [Unsplash](https://unsplash.com/)

# Cleaning them up

So we decided to clean things up and try to make sense of it all.

First we need to step back and think back why we're use something in the first
place and then from there decide what goes where.

## JIRA and Confluence

Confluence is sort of like a intranet wiki page. This is where information which
seldom change, like company adminstrative procedures, or overall business plans
for the year are placed. We also use Confluence to lay down high level
requirements of a particular project, which then will be divided into several
tickets in JIRA to worked upon.

JIRA is a task manager that allows you to define the tasks, who will do it and
any time contraints it has. JIRA also has tools to allow you to easily pull
quantative data of your team's tasks to manage it easier.

Discussions on a particular ticket sometimes go to the Comments section of that
ticket in JIRA, or sometimes to a channel in Slack. This makes it difficult for
us to follow the discussion track for decisions, because it's all over the place.

## Slack

The basic plan is to have lesser channels. Lesser channels reduces context switching
and also clutter in our minds.

Currently, many of our channels are divided according to context which overlaps,
i.e _#tech_ and _#development_ where the same people partake in the conversations,
where the contents are about technology, but only separated based on where the
technology is being used.

There are also task related channels which are seldom used and are participated by
the same people but are separated just for better context, like _#xoxzoblog_, _#xoxzohelpcenter_
and _#xoxzocorpsite_. These are where we send out requests and responses for a paricular task
within that channel's context. 

We also use Slack for ops alerts: When a server goes down or when a certain
error goes beyond a certain threshold. These get sent to a single channel where
the ops team listen to.

Finally we have guests users on Slack which are mostly contractors, which can only access a channel.

# Cleaning up

So after discussions, we've decided on a few basic rules:

- **Rule 1** Not all data are created equal: Information (tasks, requirements, chat data, etc.)
  will be evaluated based on how useful they are 6 months from now. Based on this, the platform
  that we chose to host them will change.

- **Rule 2** Slack channels should be treated as an ephemeral medium: Your work
  should not be vastly effected if Slack goes away tomorrow. Instead of using it
  as a replacement for email or a storage device, we refocus Slack as a means of
  realtime communication.
  This means that the lesser channels that you have on Slack, the better.

- **Rule 3** We're paying good money for JIRA, so it should be leveraged more to manage tasks.
  JIRA tickets should be the single-point-of-truth if you wanted to know what
  happened to a particular ticket, its progress and _most importantly_ why a particular
  decision was made concerning specifics of that task.

- **Rule 4** Anything more permanent with lesser updates will go to Confluence.
  These usually will be high-level stuff like requirements, design decisions
  SOPs or internal company processes like how to do your reimbursements or buy a
  plane ticket for a conference.

- **Rule 5** Emails are a medium for external communications. Emails are still
  useful even for internal communications if what you're going to write is long
  (needs to be saved to draft halfway) and has attachements.

- **Rule 6** No one is expected to read their emails and everyone must be able to turn off their Slack
  notifications during their downtime. But incidents happen, and we need the team that's responsible
  to be able to catch these and ask for help from anyone else if needed.

## Making Slack and JIRA complement each other

We have decided that all discussions which does not equal to a decision or is a
significant update to a particular task in JIRA will be done through its own Slack channel.
We're using a connector called [Slack Connector for Jira Cloud](https://marketplace.atlassian.com/apps/1216107/slack-connector-for-jira-cloud?hosting=cloud&tab=overview) that allows us to connect with Slack from JIRA tickets.

Short, "right here, right now" question-and-answer pairs are done on the Slack
channels.

When a discussion in the Slack channels reach a decision or significantly
updates the ticket, it is then summarized in the Comments section of the ticket.

When the ticket is resolved, the corresponding channel will automatically be
archived. What this means is that the more open tickets that you have, the more
channels you will have on Slack, but as you resolve them the amount of channels
gets less.

When you create a channel from a ticket, you can choose who do invite into that
channel. We leave it to the individual to change their preferences on Slack to
only show on their sidebar channels (read: tickets) that they are actively part of
if they prefer. This allows you to see just what tickets are pending or
requiring your input on Slack too.

## Normalize Slack channels

The final part in all of these is to normalize and get to parity the Slack
channels that we currently have.

First is to get parity on the name of the channels: We renamed #random to
\#watercooler to be in line with a program that we have called _watercooler
chats_ where you get online and talk about random stuff unrelated to work.

A new channel we call #alerts was created. This is the only channel that the
engineering team doesn't turn off their notifications for. It is only used to
alert everyone on the engineering team when incidents happen. 

Next we moved on to reduce the actual number of channels. As written above, the
rule of thumb is to normalize the channels according to the context _and_ the
people participating in them. For example, channels like #tech, #engineering and #aws are all 
combined into a single #engineering channel.

This managed to bring down our channels number to just a managable eleven, from twenty over
channels, for our small team of eleven people.

Equally important, we've made the process above transparent to the team, and
based on the decisions we've made, now we have a set of guidelines to answer the
question _"do we need a new channel for this?"_ was built. 

The use of channel description is also made mandatory: It should be clear and concise
enough that anyone new to the team will understand the purpose of the channel.

We've added a new thing called _temporary channels_ too: These are clearly
marked channels that starts with an underscore. These channels are only expected
to last one month before it is archived. We use these channels when training new
hires or when testing something.

# In conclusion

Using Slack, JIRA and other tools to manage and communicate in your work is
really great and helpful. It is usually overkill though, and might even be
counterproductive to start of with a bunch of rules on how and when to use them.

It is best to just start using your tools right away, and try to fit them to
your worklfow processes.

Take a flexible path but understand the processes that you can't
compromise. As you use the tools, you will make small changes here and there, but if you
come to a point when it doesn't make sense anymore, you'll need to be brave and
get back to the drawing board and redesign your flow and processes based
on the experience you had.

Of course, not all teams and work are created equal, so your milage will vary. The important
part is that you need to understand _why_ you're using a particular tool in the
first place. But hopefully after reading this post, you've gotten some ideas to start with.
