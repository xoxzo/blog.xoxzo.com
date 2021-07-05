Title: How to measure Return On Investment of your SMS marketing campaign
Date: 2021-03-01 12:00
Author: Surya Banerjee
Tags: Tutorial; LinkTracking; 2021;
Slug: introduction-linktracking
Lang: en
Summary: Learn how to use linktracking on EZSMS and Xoxzo API


## How to measure Return On Investment of your SMS marketing campaign

With 6 billion SMS text messages sent every single day around the world it is no wonder that text based marketing campaigns are still the rage in 2021 even with all the new age communication tools that we have available today. 

According to [mobile marketer](https://www.marketingdive.com/ex/mobilemarketer/cms/opinion/columns/1944.html), SMS has the highest engagement rate and so it is a no brainer solution to invest on this channel of direct marketing to a highly targeted audience. Especially with [open rates](https://www.gartner.com/en/marketing/insights/articles/tap-into-the-marketing-power-of-sms) as high as 98% which far exceeds open rates of emails which stand at a mere 20%. 

Though having the advantage of SMS technology being around for a relatively long period of time, there are disadvantages to this too. 

The biggest concern we come across is when we see people mentioning the lack of ability to track the performance of their investment in SMS marketing campaigns. However this is not really true. 

There are smart ways to monitor the effectiveness of sms campaigns and here we mention a few below:



1. **Having an online presence and redirecting the users there**<br />
    When a text message is opened by a prospective customer, the retention of the content for the specific marketing campaign is much lower than when there is no active engagement from the customer. This where a landing page comes in. It doesn’t necessarily need to be a full blown website, but often a simple page with more details about whatever you are marketing is a good idea. You would just need to add the URL to the contents of the text message. With the character limitation on SMS, this landing page would be a great opportunity to make a more convincing pitch to the prospective customer.

2. **Using an analytics tool to measure traffic to the landing page**<br />
    This is the direct next step after setting up the landing page for the SMS campaign. There are amazing free analytics tools like [Google Analytics](https://analytics.google.com/analytics/web/provision/#/provision) which will help you measure and identify the number of people visiting the page and hence give you a good feel of how well your SMS marketing campaign is performing.

3. **Using URL shortening tools**<br />
    Using the landing page and the analytics tools is a great way to get a feel of how well your SMS campaign is performing but, unfortunately, that is not a full-proof measure of how many people are actually visiting your website and how much traffic is coming from elsewhere on the internet. This is where link shortening tools come in handy. These tools would help you shorten a link so that you can limit the number of characters taken up by the URL and at times even provide you with analytics of the number of clicks. However, even this is not the exact measure you might be looking for, since you are unable to distinguish between different customers in your SMS campaign target list clicking the link. And it is quite impractical to manually create many short links and insert them one by one in the text messages. (Imagine sending a marketing SMS to 10000 people!)

4. **Using link tracking on EZSMS and Xoxzo SMS API**<br />
    We heard about this issue from our clients and decided to do something about this problem. For this we came up with a solution. You can now [track links](https://blog.xoxzo.com/en/2020/10/15/link-tracking-release/) on our web-based telecommunication platform EZSMS or on our Xoxzo telephony API.
    
    Our [SMS API](https://www.xoxzo.com/en/about/sms-api/) now accepts a special parameter called **track_link** which enables you to track each message individually. All you have to do is put the URL to your landing page and we will do the rest. We create unique links for each recipient, send the SMS to people on your list and show you if they have clicked on the link or not. 

Even better, now we have another special parameter called **lt_callbackurl** which you can set to receive a [callback](https://www.xoxzo.com/en/about/voice-api/) when someone in your list clicks on the link. So in essence you get a notification every time someone opens a SMS message sent by you and clicks on the link.



## How does link tracking work in [EZSMS](https://blog.xoxzo.com/en/2021/01/28/ez-link-tracking-release/):

Let us see [how we use this feature](https://help.xoxzo.com/ezsms-sms-delivery-service/articles/link-tracking-feature/) on our EZSMS web based telephony platform. We are going to use the feature web based SMS feature for this. <br />


1. **Login to EZSMS and go to Web SMS Sending page:**<br />
After signing into the dashboard, on the right sidebar click on _From Web_ from the _SMS sending_ section. You will be able to fill the required fields including the message that contains the link you would like to track. 

2. **Click on Enable Link Tracking checkbox:**<br />
Once you have filled in the text you would like to send, click on the checkbox marked _Enable Link Tracking_

3. **Send message:**<br />
Click on _Send SMS_. Your recipient should receive a text message with the link replaced by an auto generated shortlink that looks something like this - _[https://xoz.so/XYZ](https://xoz.so/XYZ)_. Now for testing the feature, lets click on that link. It should redirect you to the original url you placed in the text message.

4. **Check the status of the Link, if it is accessed or not:**<br />
Lets first try to download the usage logs. For this go to the menu on the top bar and go to the usage logs page. Once there, select a custom date range and download the log. You will be able to see the message you just sent, and in the _Link Tracking Status_ you will be able to see 0 which means it hasn't yet been accessed.
<br />
Now for testing the feature, lets click on that link. It should redirect you to the original url you placed in the text message. Now download the usage logs again. You should see that the _Link Tracking Status_ should have changed from 0 to 1 now.



## How does link tracking work in [Xoxzo SMS API](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/what-is-link-tracking/):

In case you want to use this feature in your own product or use an API lets look exactly how this works with our Xoxzo API. Let's walk through the steps:


1. **Send a SMS message using the API:**<br />
    After registering on [Xoxzo](http://www.xoxzo.com), log in to your account and create a new api user. Once you have done that you will be able to access your SID and TOKEN. Once you have that, using the curl command line tool construct this request.(Do not press return to send this yet) <br />
    
    **_curl -u &lt;SID>:&lt;AUTH_TOKEN> --data-urlencode 'recipient=&lt;recipient>' --data-urlencode 'sender=&lt;sender>' --data-urlencode 'message=&lt;message>' https://api.xoxzo.com/sms/messages/_**

2. **Enable link tracking:**<br />
    Now is the time to enable link tracking. Add a new parameter at the end of this curl command called **track_link=true**. The final curl command would look like this - <br />
    
    **_curl -u &lt;SID>:&lt;AUTH_TOKEN> --data-urlencode 'recipient=&lt;recipient>' --data-urlencode 'sender=&lt;sender>' --data-urlencode 'message=&lt;message>' --data-urlencode ‘track_link=true’ https://api.xoxzo.com/sms/messages/_**

3. **Check status of the SMS using the Status API:**<br />
    Once you have sent the message you would receive a **msgid** which is a unique identifier of the SMS sent. If you want to check the status of the individual message, you can use our status api by a curl command like this - <br />
    
    **_curl -u &lt;SID>:&lt;AUTH_TOKEN> https://api.xoxzo.com/sms/messages/&lt;msgid>/_**<br />

    _(In case you want to check for multiple messages just drop the msgid at the end of this endpoint.)_<br />
    **_curl -u &lt;SID>:&lt;AUTH_TOKEN> https://api.xoxzo.com/sms/messages/_**


You will be able to observe the link tracking details in the response to this curl like this - <br />

```
{
    "cost": 15.0,
    "link_tracking": {
        "accessed": true,
        "accessed_on": "2020-10-09 02:40:39",
        "link": "http://www.example.com",
        "shortlink": "https://xoz.so/dbNL4"
    },
    "msgid": "oxgyFO6tfwYkHLIMbURrz5smCv9QT423",
    "recipient": "+818012345678",
    "sender": "XOXZO",
    "sent_time": "2020-10-09 02:37:47",
    "status": "DELIVERED",
    "tags": [],
    "url": "https://api.xoxzo.com/sms/messages/oxgyFO6tfwYkHLIMbURrz5smCv9QT423/"
}
```

**Set callback url for getting notification when someone clicks on the link(optional):**<br />
As mentioned above, you can also set a callback url for receiving a request when someone clicks on your link. This can be done by adding a parameter to the curl above called **lt_callbackurl** to set your custom endpoint to receive the requests. To test this, you can use free tools like [requestbin](https://requestbin.com/) which generates a callback url for you.<br />
    
**_curl -u &lt;SID>:&lt;AUTH_TOKEN> --data-urlencode 'recipient=&lt;recipient>' --data-urlencode 'sender=&lt;sender>' --data-urlencode 'message=&lt;message>' --data-urlencode ‘track_link=true’ --data-urlencode ‘lt_callbackurl=example.com/callback/’  https://api.xoxzo.com/sms/messages/_**


The Xoxzo API will send you all information about when someone clicked on a link on the endpoint you specify, and you get to take action on that immediately. 

More details about this feature can be found in our [API docs](https://docs.xoxzo.com/en/sms.html#send-sms-messages-api). Please do not hesitate to contact us at [help@xoxzo.com](mailto:help@xoxzo.com) in case you have any problem accessing our APIs. We look forward to hearing your feedback.
