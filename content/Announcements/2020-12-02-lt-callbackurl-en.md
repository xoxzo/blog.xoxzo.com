Title: Additional parameter made Link-Tracking even more convenient
Date: 2020-12-02
Slug: lt-callbackurl-release
Lang: en
Tags: xoxzo; release; 2020; link-tracking;
Thumbnail: images/link-tracking.png
Author: Aiko Yokoyama
Summary: Introducing an additional paramter to provide an URL to be called at the event of link clicked.


Thank you for using [Xoxzo API](https://www.xoxzo.com/).

Please let us announce an additional parameter _lt_callbackurl_ to be used together with _track_link_ for our SMS API.


Please also see [Link tracking release](https://blog.xoxzo.com/en/2020/10/15/link-tracking-release/)


### How to use
Very simple. Please add a paramter _lt_callbackurl_ to provide an URL to be called at the event of link clicked when you send SMS sending request.
For more details, please visit [Help Center](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/what-is-link-tracking/).

### How it works
**SMS Link Tracking**
- When the parameter _track_link_ is provided, link tracking function is enabled. 
The first URL/domain name in the message will be replaced with our private short url. <br> 
- The information of when the recipient clicks the link on the mobile terminal will be recorded. <br>
**SMS Link Tracking with callbackurl**
- Provide the URL to call when the link is clicked with the parameter _lt_callbackurl_. <br>
- XOXZO cloud will call the URL with http POST method<br>

Please check the link tracking details using [Check SMS status API](https://docs.xoxzo.com/en/sms.html#check-sms-status-api) as well.

### Pricing
The link-tracking feature needs an additional parameter cost on top of standard messaging.
Please visit our [SMS pricing page](https://www.xoxzo.com/en/about/pricing/#send-sms) for more details.

Link tracking feature was born by our user's voice.<br>
Please contact our helpdesk（help@xoxzo.com）with your requests too.
