Title: The Game of Deployment
Date: 2017-07-26
Slug: the-game-of-deployment
Lang: en
Tags: 2017; tip;
Author: Shauryadeep Chaudhuri
Summary: With the growing need of managing application deployment, these are some of the ways we found to setup an in-house deployment management system for web applications.

Web Application Deployment is one of the important parts in application development. Once an application is developed, you are required to serve it to your users, and if it is not served right it would impact your customer base.  Over the years the procedures required in deployment have grown complex, and management cumbersome. 
Due to these factors, we have decided to setup a system in-house that would help us deploy more easily. As part of our research, I looked into various approaches on how to setup an in-house application deployment management system, I have come across various deployment strategies and today would like to give my views on why this is necessary going forward and a couple of strategies I have found viable.

###Growing need of Application Deployment Management
-----
After developing an application, the application needs to be available on a public facing server which should ideally have 100% uptime. Serving the application from your desktop/laptop does not guarantee that. The strategy of how to make the application available has also changed over the years.

If we go back just 10 years during the web 2.0 era, web application deployment was not as complex as today for a couple of reasons.

*   Implementations of web applications were mainly limited to PHP, ASP or Java Servlets.
*   The user base used to be limited, so "WebMasters" just upgraded to a higher end server. Generally, only a single instance was used to serve their website.

Today, there are more people on the internet which mean,  your website is available to more people. Because of this, we need to be prepared to do rapid changes to our application and we need to be prepared to handle more traffic. There are certain factors we face today for deployment management.

1.   *Scalability* :  An application should be scalable, means that it should be easy for the developers to increase the machine specifications as the traffic to the application grows. The application shouldn't be hosted on a server with a high configuration on its first day because then you are just wasting resources. On the other hand, if the traffic suddenly grows it should take the time to increase the specifications, in order to avoid downtime. So the bottom line is the transition of the specifications should take the least time as possible.

2.   *Rapid Deployment* : Due to the nature demand today, issues are fixed and features are developed at a fast pace. There can be instances where every day one issue is fixed on five consecutive days, and to provide better customer satisfaction we may need to deploy every day. This process also should take the least amount of developer effort.


3.   *Clustering* :  An application should be deployed to several instances so that when the traffic/load increases or an instance fails for some reason, the application does not face downtime. 

4.   *Isolation* :  Small changes to an environment can cause "The Butterfly Effect". The environment the application exists should not contain anything more than it needs.

Many cloud services like AWS, Heroku, Azure do provide certain solutions to these issues, but you will face a number of issues if one day you decide to migrate from one cloud provider to another. For Example, if you decide to move from AWS to Heroku, the way they function are completely different. So it is better to have an in-house or a third party deployment strategy.


###Convox
-----
Convox is a deployment management tool that takes care of deployment, management & maintenance of deployed applications.
Convox tries to replicate the deployment process to that of Heroku. It uses docker images to understand application configuration, it automagically creates isolated environments which are called Racks.These contain applications which are in turn have isolated environments. One of the things I disliked about Convox is that it is only currently available for AWS.

Analyzing it on the points previously mentioned.

1.   *Scalability*:  Convox allows to scale applications through its CLI and provides an easy interface to perform resource management. It basically acts as a wrapper to AWS in this context.

2.   *Rapid Deployment*:  It is fairly easy to deploy using convox. It would automatically create the necessary endpoints that for each process that are mentioned in the docker configuration file. One of the things I liked about Convox here is that it takes a snapshot of each deployment. So if you want to roll back to a previous state, you need not perform the complete deployment process with a previous version of the codebase. You can just select which deployment you want to make available and choose it from the list.


3.   *Isolation*:  The Convox infrastructure provides 2 level isolation.
	*   *Network Isolation* : Applications in a particular Rack can only talk to another application in the same Rack. They term themselves as a virtual private cloud implementation as most of the communication is done through internally opened ports and very few ports are opened on the public domain. Under the wraps required AWS infrastructure is created including AWS VPC, Subnets etc.

	*   *Environment Isolation* : Convox provides environment isolation to its applications using docker containers.


4.   *Clustering*:  Convox implicitly provides clustering using ECS Clusters. The user need not worry about managing nodes and setting up the cluster themselves.




*Upsides*: 

* Good Deployment Management.

* Autoscaled Clusters.

*Downsides*: 

* Even Though Open Source Cannot set it up for in-house deployment management.

* Currently, only available for AWS, application migration to another cloud would be easy since it is managed using docker but you would need to choose another deployment management technique.

###Flynn
-----
Flynn is an open source project which allows you to deploy an in-house deployment management system, on your server. Flynn internally uses Docker Containers to setup its environment but the user need not worry about docker configuration file and uses Heroku's open source build packs to build the application. The Deployment procedure is identical to that of Heroku.

Analyzing it on the points previously mentioned.

1. *Scalability*:  The scalability part in Flynn has to be manual. The user needs to setup Flynn on every node/instance of a cluster. The resources allocated to Flynn is same as the resource allocated to the particular instance.

2. *Rapid Deployment*:  If an application is deployed on Flynn Manually, it does not take a snapshot of each build deployed. On the other hand, if the application is deployed directly from GitHub, it keeps track of each commit and the application can be deployed from any state/state after a commit.  Unfortunately, it only supports GitHub. There is a plan on their roadmap to implement support for any git repo(ex: Flynn- BitBucket)

3. *Isolation*: Flynn is setup on a node, it would setup docker containers internally to provide environment isolation. 

4. *Clustering*:  Since Flynn acts as an in-house deployment management system, it needs to be manually setup on each node of the cluster. The installation procedure is not very complex and can be done easily. The instances can be scaled from the selected clouds console easily. Once setup, an application can be scaled to any number of instances available.

*Upsides*: 

* In House Deployment Management.

* Deploy Straight from Github.

* Not a lot of special configuration needed to deploy.

* Applications can be migrated without any change.

*Downsides*: 

* The setup procedure on each node can be cumbersome if a lot of nodes are selected.

* Only supports Github for a snapshot-like feature is needed.

###How They Compare
-----
Depending on the needs I personally would go prefer using Flynn as it gives more
freedom on managing the system, it is opensource and free to use if you can do it
yourself. Although if you do not wish to handle setting up yourself and want another
team to manage your deployments, then Convox would be the cheaper alternative.
