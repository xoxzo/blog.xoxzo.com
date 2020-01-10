Title: DevOps is a culture, not a role
Date: 2019-05-12 08:45
Author: Kamal Mustafa
Tags: 2019; devops;
Slug: devops-is-a-culture-not-a-role
Lang: en
Thumbnail: images/devops-culture.jpg
Summary: There's no specific DevOps role. Instead, we build a culture where Dev and Ops engineer work together to achieve the organization's objective. And that's what is DevOps.

The traditional problem between dev and ops is the conflicting goal that they have in order to achieve organization's objective. Dev need to build and release new features fast in order to support user's need, while Ops need to ensure system reliability by minimizing changes to the system.

DevOps culture intended to fix this so that both roles are working together instead of being odd at each other. To better understand the culture, we need to look first what are the responsibilities of both roles.

Software Engineering (SE) primary roles is to design, build, test and deploy application so that we can deliver it as a service to our customers.

While Operational Engineering (OE) roles can be described as below:-

1. OE primary roles is to ensure our services properly running in a reliable and secure way so that our customers will be able to use it to meet their business requirements.
    * Define and measure availability metrics.
1. OE also responsible for providing supportive environment for the SE team to accomplish their development tasks. This include:-
    * Providing efficient development and testing environment.
    * Providing a frictionless and continuous way of pushing application from dev to production.
1. Track outages and incidents, and their associated impact to the business. Make sure all outages and incident properly closed in timely manner with adequate reports of what, when, why and how it affecting our customers.

For more insight of what constitute an effective OE, can refer to this article - [8 Habits of Highly Successful Operations Practitioners][ops-habit]. In general, OE should be an expert in this 3 technical domains:-

1. Low-level systems knowledge.
    * Know how to debug low-level systems problems.
    * Understand the fundamentals of networking.
    * Know the intricacies of the Linux kernel and know every Linux command on this earth (ok, maybe not all but you get the point).
    * Cross OS knowledge and know the trade off and what they are more suited for.
1. High-level distributed systems knowledge.
    * Know how entire production systems fit and work together.
    * Know how to design for scalability and reliability.
    * Know how things should be deployed and monitored and logged.
1. Have solid programming skills.
    * Know multiple languages quite well, and can easily write applications and tools for developers to use.

I prefer to look at "devops" as a culture instead of specific roles. It's within this culture we define roles as software engineer and ops engineer that will fit into what the culture intended to. One of that culture can be seen from the responsibility of SE and OE.

As we can see above, SE role include deploying application to production. This is one difference with the traditional setup where deployment is an Operational role. But at the same time, OE role include “Providing a frictionless and continuous way of pushing application from dev to production”. So while it’s SE’s responsibility to deploy code to production, OE must provide the most efficient way to accomplish that. It's here we apply the 80/20 rule where every role will responsible to 80% + 20% of defined key areas.

## Conclusion
There's no specific DevOps role. Instead, we build a culture where Dev and Ops engineer work together to achieve the organization's objective. And that's what is DevOps.

[ops-habit]:https://blog.newrelic.com/2017/06/07/successful-operations-practitioners-habits/
