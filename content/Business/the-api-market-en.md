Title: API empowering developers: The API Market and Economy
Date: 2017-04-29 10:00
Lang: en
Author: Iqbal Abdullah
Tags: developer; japan; market; economy; twilio alternative; aws; 2017;
Slug: the-api-market-empowering-developers
Thumbnail: images/api-empowering.jpg
Summary: In this post, Iqbal writes about the growing API market which is more and more empowering developers everywhere.

The [Application Programming
Interface](https://en.wikipedia.org/wiki/Application_programming_interface) 
or API is a way for systems and programs to talk to each other. Different
systems will have different ways to store and process data, and using an API
with a publicly available instruction to retrieve this data will increase
interoperability and capability of other systems that rely on this data or
service.

As our business is providing a service via a paid API, I would like to take some
time during this long holiday in Japan to look into and share some thoughts 
concerning the API market.

The History of APIs
======================================

APIs have been around for a _very_ long time:

> "The concept of an API pre-dates even the advent of personal computing, let
> alone the Web, by a very long time! The principal of a well documented set of
> publicly addressable "entry points" that allow an application to interact with
> another system has been an essential part of software development since the
> earliest days of utility data processing. However, the advent of distributed
> systems, and then the web itself, has seen the importance and utility of these
> same basic concepts increase dramatically." - Martin Bartlett [^Ref1]

APIs are a source of innovation as it empowers developers with many different
data and services that they can mix and match to produce much more effective and
focused service to their own users.

With the prevalent of personal computing and the internet and with it the
number of engineers that can harness this technology, it is now much more
easier to share data or services via API which can be utilized using standard web
protocols and development tools. 

The Growth of APIs
======================================

[Salesforce.com release of it's publicaly available API at the IDG Demo
conference in 7th Feb
2000](http://www.prnewswire.com/news-releases/salesforcecom-to-debut-at-demo-2000-72352127.html)
kick started the web API market.

In "Tracking The Growth of the API Economy"[^Ref2] Art Anthony shows us that
public API grew from nearly an insignificant amount in 2006 to 15,000 in 2016.

Today [ProgrammableWeb](https://www.programmableweb.com/) lists over 17k of
available APIs.

Not only are there server side web APIs, there are also client side APIs like
native plug-in browser extensions.

There are now as many APIs as types of data or services that you can imagine.
Here are some examples:

Getting Social
--------------------------------------
del.icio.us which was founded in 2003 was a service for people to share
bookmarks on the web. It is a good example on how you'd harness the
standard way of calling for information on the web into a simple programmable
interface to retrieve information.

Of course, we can't leave out Facebook. Facebook released it's Developers
Platform in August 2006. It followed the same pattern of REst web APIs, with
responses in XML following the common pattern of web APIs at that time.

Mapping
--------------------------------------
Google Maps lauched it's API in June 2006, partly due to pressure from rogue
applications that was leveraging it's maps service to show information on the
maps. The API allows developers to show Google Maps on their own websites, with
specific data overlaid on the maps.

Entertainment
--------------------------------------
Netflix serves over 20 billion requests a month over it's API.[^Ref3] Netflix's
API serves all the devices that's hooked to it's platform consuming it's
contents. From the engineering point of view, Netflix is a good study case to
learn how they scale to cope with the increasing load and demands on their API.

Infrastructure-as-a-service Platforms
--------------------------------------
In 2007, Twilio launched as a API-as-a-product platform, which allows developers
to make and receive phone calls. The API was launched in 2008[^Ref4] and in 2010 Twilio
has added text messaging (SMS) to it's API.

Amazon's AWS is the behemoth infrastructure platform that we all know now. It
consists of among others S3 (a storage platform) and EC2 (a computing platform)
Even before it's web interface was avaialable to the public, it's functionalities 
can be accessed via an API. For S3, Amazon allowed developers to host files via an API and it
charges developers for the amount of data they stored in the cloud per month. In
2006 this was a new billing model and with the S3, Amazon brought in what we now
know as cloud coumputing.

With tens and thousands of APIs that will give you the service or data that you
need for your application, developers are spoilt to the choice that they have to
achieve their goals.

Monetizing models
======================================
Paid public APIs are common. Generally there are 4 big types of monetizing models
which the API can help the business earn[^Ref5]:

Free
--------------------------------------
Free APIs are like Facebook's Developer's Platform API. You can access and use the
APIs for free, which will add more contents on Facebook. Facebook then earns
from the more ads that get's onto it's platform which is boosted by more users
attracted to the increasing contents.

Developer Pays
--------------------------------------
This model is a straightforward model where the user of the API pays. [Xoxzo's
Cloud Telephony Platform API](https://www.xoxzo.com/en/) and Amazon's AWS APIs 
are examples. Paypal which takes a cut from the sales that you make when you use 
their APIs also fall into this model.

Developer gets paid
--------------------------------------
Google AdSense, Amazon Affiliates are examples of model which the developer gets
paid, while the business also earns from a different source, like the business
trying to sell merchandise on Amazon, or the owner of the ads in the case of
AdSense. These are usually revenue share setups. 

Expedia, which says that 90% of what they do is through their APIs, has around
USD2 billion per year of business going through it's Affiliate Network.

Indirect
--------------------------------------
3rd party applications built on the eBay open platform, and also 3rd party
Twitter clients are examples of the indirect model. These two are examples of
ways for the business to aquire contents, which leads to a better user
exeprience in their main businesses.

The New York Times utilizes APIs for contents syndication, which will pull
visitors to it's main site so that they can earn on ads revenue of subsciption
fees for their contents.

I think there is a fine line between the indirect and the free model, because
both are basically "free" to the user. I guess it will depend on the underlying
monetizing model that you have for your business. In these cases, usually you would consider the
API as an additional funnel that leads to your main business.

While in Japan...
======================================

In Japan, ITR states that the amount of revenue for the API market 
for 2015 was 80% more than 2014, and it predicts the between the year 2015 to 2020, the
average growth for the API economy is 41%, with revenue gained in 2020 a
whopping 5.6 times compared to 2015.[^Ref6]

ITR points to the reason of the increase was due to the implementation push by
big companies. But at least for the Japan market, it seems that these are not
public APIs but APIs which are only opened to partners.

Terrie Lloyd, a long time Japan resident of Japan and comments on the tech
industry has a different view. He believes unlike the rest of the world where 
APIs are used extensively, due to the controlling nature of Japanese businesses 
over business relationships and company internal data, not to mention the technical 
challenges for smaller companies, the opening up of APIs to the public is not as 
fast as the rest of the world.[^Ref7]

I believe it will be a matter of time that business in Japan will also be
providing public APIs readliy accessible to developers. Business models might be
different than for example Twilio which charges the developers directly per
usage, but might be more of indirect or partnership agreements where the
businesses themselves will have a stronger control on the relationship.

In Summary
======================================

The API economy and market will continue to grow, due to the pull factors such
as ease of computing resources (cloud computing), increase of mobile devices
which requires more and more real-time data and the growing number of engineers
which can handle and work with web technologies. The push for more efficiency
and need for faster time to market also contributes the growth of the API.

New industries such as big data processing and AI require data to function, and
these data will more and more be made avaialable via public APIs. 

The business models for APIs are pretty straightforward, and can be the main
revenue generator (like Xoxzo or Expedia) or an indirect channel to acquire contents
(like eBay). Either way, there still needs to have a specific and comprehensive
strategy for the business part of the API itself. It is not something that you
do as a "side" service. 

But APIs are never done. They grow and need to be refined based on actual data
used, who is using it and it's use cases.[^Ref8]


[^Ref1]:[History of APIs](http://history.apievangelist.com/)
[^Ref2]:[Tracking the Growth of the API Economy](http://nordicapis.com/tracking-the-growth-of-the-api-economy/)
[^Ref3]:[Netflix API Now Serving 20+ Billion Requests Per Month](https://www.programmableweb.com/news/netflix-api-now-serving-20-billion-requests-month/2011/03/29)
[^Ref4]:[Twilio: Powerful API For Phone Services That Can Recreate GrandCentral's Core Functionality In 15 Lines Of Code](https://techcrunch.com/2008/11/20/twilio-powerful-api-for-phone-services-that-can-recreate-grandcentral-in-15-lines-of-code/)
[^Ref5]:[API Business Models](https://www.slideshare.net/jmusser/j-musser-apibizmodels2013/35-API_Business_Models)
[^Ref6]:[2015年度のAPI管理市場は前年度比80.0％増の高成長、2016年度の市場規模は倍増を予測](https://codezine.jp/article/detail/9890)
[^Ref7]:[Terrie's Take 892](https://www.terrielloyd.com/terries-take/tt-892-tourism-edition-technology-birth-pains-new-definition-of-the-travel-api-a-path-to-irritation/)
[^Ref8]:[What Is The API Economy?](https://www.ibm.com/cloud-computing/learn-more/hybrid-integration/api-economy/)


