Title: Sending your first SMS
Date: 2017-10-31 12:00
Author: Miko-chan
Tags: sms; api user; api; tutorial; mikochan;
Slug: sending-your-first-sms
Thumbnail: images/xoxtan.png
Lang: en
Summary: Let's send your first SMS!

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>
<div class="lg-padding-top50 md-padding0">Now that you've created your API User, we can go ahead and explore what the Xoxzo web API can do. At its simplest function, you can use the Xoxzo web API to do what a phone can do: which is SMS and voice call. We'll go ahead and send an SMS for you to try it out!</div>
<div style="clear:both;"></div>

## What do I need?

What you really need is your computer's command prompt (cmd). In Linux environments and Mac, this is called the terminal or shell instead. For this tutorial, we'll be referring to this as the shell.

![shell](/images/Tutorial/send-sms/shell.png)

Next, you'll need something to send an HTTP request to Xoxzo's API server for it to process your commands to send an SMS. It goes without saying that you need Internet access as well.

Finally, you'll need your API User's API SID and Auth Token.

## How do I find my API SID and Auth Token again?

Log into your account, and you can see the API SID column for your first API User is already filled with jumbled text. Your entire API SID is not shown in full, so to get it, just double click on the text and copy it via Ctrl-C. Paste it in your notepad for easy reference.

Click on the "Show Token" button and copy the text in the Auth Token column as well.

![SID and token](/images/Tutorial/send-sms/sidtoken.png)

Now that you have your API SID and Auth Token texts, put them together like this:

APiSiDtext:AUthT0k3ntext

Remember to put the colon ':' between the API SID and Auth Token and that they're written in a single line.

## Now let's send an SMS!

Let's try sending an SMS to your own phone first to see it in action. Sending SMS messages from your PC through this web API saves a lot of time Note that you need to put down your phone number complete with the country code, with a '+' in front of it.

Type this in your shell prompt:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
--data-urlencode 'sender=XoxzoTest' \
--data-urlencode 'recipient=putyourphonenumberhere' \
--data-urlencode 'message=Hallo hello!' \
https://api.xoxzo.com/sms/messages/
```

You should be getting something like this message in return right after you type that: 
`[{"msgid":"tHi5i5y0urMsGIdt3xT"}]`
Which normally means that everything went well. You can also type the command in a single line without typing the '\' as well if you wish.

You should be receiving the message on your phone shortly. Your local carrier might not allow something like 'XoxzoTest' to appear as the sender, so another private number might appear instead.

And that's it! You've sent your first SMS through the Xoxzo web API! If you check your profile page, you'll also notice credits have been deducted after you sent the SMS.

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our API.

Are you looking for an even simpler option to send SMS messages from your PC to customers and do you want to get started right away without coding? Check out our other service EZSMS! 

With EZSMS you can start sending bulk SMS messages from the web right away. There are no initial or monthly fees: you only pay for what you use. You can also send customized messages to cater to each customer. 

EZSMS supports SMS sending to 170 countries and it supports simultaneous sending to multiple destinations and delivery using CSV files that can be customized and mass-delivered.
You can send SMS anytime, anywhere. Complete it all online-Dial SMS to make your business or event a huge success!

