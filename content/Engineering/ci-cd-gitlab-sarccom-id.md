Title: Workshop CI/CD on gitlab by SARCCOM Indonesia
Lang: en
Date: 2019-05-31
Author: Zaki Akhmad
Tags: ci, cd, gitlab, sarccom, id
Slug: workshop-ci-cd-on-gitlab 
Summary: Automate as early as possible with CI/CD.

First, let's start with the abbreviations. CI stands for Continuous
Integration while CD stands for Continuos Delivery/Deployment.

Last month, I attended a [workshop on](https://www.meetup.com/Software-Architect-Indonesia/events/260847142/)
implementing CI/CD which hosted by SARCCOM (Software Architect Community) Indonesia.

![CI/CD Workshop]({filename}/images/ci-cd-workshop.jpeg)

It was a nice workshop! In around 2 hours, with hands-on experience, I get
to know how to implement CI/CD on gitlab. The workshop started with a basic
explanation on what is CI/CD and how we see this CI/CD in the whole process
of software development. CI/CD focuses on software-defined life cycles.

The room was a bit small but the nice thing is it was fully packed! There were
around 20-25 attendees, although the workshop location was a bit far from the
city center.

The instructor was [Freddy](https://twitter.com/FredEatWorld), which I think
I never met him before. Freddy explained everything clearly and also responded
to the attendees questions. We were using node.js application and since I don't
have any experience on node.js, Freddy gave me a hint when I was getting an error.

With CI in our development pipeline, we can know in short time if there's something
wrong in our code. For example the most simple error like assigning to a non-exist
variable and also syntax error. While for CD, we will know whether we can deploy
our code to development or production environment or not. And in some cases we can
automate to deploy to development environment once we commit it.

On gitlab, we define the configuration in `.gitlab-ci.yml` file. First, we define
the environment. Then we can also define the prerequisite before run the test such as
doing packages upgrade etc. Finally we define the tests that we're going to execute.
Starting from sytle checker (lint) and also run the test code. Once everything is OK,
we can ask CI/CD to deploy to development environment by running the deployment script.
