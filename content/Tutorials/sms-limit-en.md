Title: How to deal with text-count limit on SMS messages
Date: 2017-12-28 17:00:00
Modified: 2018-5-24 15:00:00
Slug: sms-limit
Lang: en
Tags: SMS; 
Author: Aiko Yokoyama
Summary: SMS is a great friend fo marketing as it has higher opening rates and simple and easy to send. A little concern is there is a limit in body text. Here we can introduce some tips to use SMS more convenient.


Using Xoxzo's [SMSAPI](https://www.xoxzo.com/en/about/sms-api/) and/or [EZSMS](https://www.ezsms.biz/en/) and/or [DialSMS](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/what-is-dialsms/), you can send SMS messages by sending SMS messages from your PC instead of typing recipients numbers or body text on your phone. This makes it easier to send SMS in bulk to a large number of people.  

SMS is utilized for many purposes including business and marketing, as it is simple and easy to send and has higher open rates than emails. For example:

+ Notification of password confirmation for an online registration
+ Payment reminders to unpaid invoices
+ Notify past visitors about upcoming events.
+ Request for returning to the customers/patients who left the waiting room
+ Emergency notifications about disasters without internet connection
+ Meeting minutes and reminders of changes within large organizations
+ Corporate notifications and reminders

The list goes on.

But it is not easy to write the text for your SMS message.. Because SMS can include only up to 160 ASCII characters. It is unexpectedly difficult to summarize the well-noticeable contents within that limitation.

_First, whom you talk to_

__To XXX　（7 - 10 letters）__

_Introduction_

__Thank you for shopping at Xoxzo.（30 - 40 letters）__

_and the message_

__Please contact us for any questions you may have during the use.（70 - 80 characters）__

_Contact_

__Phone: 0123-456-789 (20 characters)__

_who you are_

__by Xoxzo sales dept (10 letters)__

This makes almost 160 characters, almost the limit.

It might be a fun to consider this as your summarize lesson, look up dictionaries and try to find a better wording. But it will be impossible to fit all in if you want to write a lot of content in your SMS message. Taking into account the usage rate of smartphones nowadays, it will be better to write the details on your website, and send the URL link of this page in the SMS message so customers can read more about it if they want to.

Firstly, keep in mind what kind of message you want to convey. For example a marketing message should create a sense of urgency and prompt the customer to visit their website. 

- 'Brand name' 40% off! Black Friday starts now: URL

A booking confirmation should be short, polite and to the point. 

- 'Hotel name' Thanks for booking a room at 'hotel name' for 'date'. Visit URL to read more.

Well though, the link URL is not always as short and clear as `https://www.xoxzo.com/ja/` it can go over 160 characters sometimes.

So how can we shorten a link that is too long? 
Xoxzo has an optional service for the SMS API called link tracking which was released in 2020.
By using link tracking your URL will be shortened automatically making it easier to fit within the limits of an SMS message.
In addition, you’re able to track who, and how many people clicked your link and at what time which can be useful for marketing purposes and improving your messaging even further next time.  
For example you can create an AB test, 2 types of SMS messages, each sent to half of your customers and track which of the messages had a higher open rate, and which message was clicked on faster. 
The optional parameter link tracking can easily be enabled when using the Xoxzo SMS API. 


It is all up to you and your idea to make the most of 160 characters, using [SMS](https://www.xoxzo.com/en/about/sms-api/).





