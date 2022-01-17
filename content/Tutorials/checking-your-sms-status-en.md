Title: Checking your SMS status
Date: 2017-11-15 11:00
Author: Miko-chan
Tags: sms; api user; api; tutorial; mikochan;
Slug: checking-your-sms-status
Thumbnail: images/xoxtan.png
Lang: en
Summary: How to check the status of your SMS.

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>
<div class="lg-padding-top50 md-padding0">
  
Have you [created your Xoxzo API user](https://blog.xoxzo.com/en/2017/10/13/create-your-first-apiuser/) and have you [sent your first SMS](https://blog.xoxzo.com/2017/10/31/sending-your-first-sms/) using the Xoxzo web API? Follow this tutorial for the next step: checking your SMS status online!
 
If you have managed to send your first SMS, as we explained in the <a href="https://blog.xoxzo.com/2017/10/31/sending-your-first-sms/">previous article</a>, you'll notice that we get a msgid string in return after we run the CURL command, like this: <code>[{"msgid":"tHi5i5y0urMsGIdt3xT"}]</code>. If we get that, we sent the SMS correctly, otherwise the return message would've been different. But how do we know recipient actually received the SMS message?

</div>
<div style="clear:both;"></div>

## SMS checking command

We'll still use CURL to check the SMS status, similar to how we sent an SMS. The difference will be in the parameters we provide and the URL.

To check on the status of your SMS, run this:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/tHi5i5y0urMsGIdt3xT/
```

If everything is OK, you should be getting a JSON response like so:

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "DELIVERED",
    "sent_time":"2015-08-27 09:22:32",
    "cost": 10,
    "sender": "your_number",
    "recipient": "your_recipientnumber",
    "url": "https://api.xoxzo.com/sms/messages/tHi5i5y0urMsGIdt3xT/",
    "msgid": "tHi5i5y0urMsGIdt3xT"
}
```

Of course, the cost will depend on which number you are sending too. You can get the pricing details here: [SMS Pricing](https://www.xoxzo.com/en/about/pricing/sms)

The SMS statuses are in this list:
<table class="table table-striped">
  <thead>
    <tr>
      <td> Status </td>
      <td> Details </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> QUEUED </td>
      <td> Message put into queue and will be delivered shortly </td>
    </tr>
    <tr>
      <td> DELIVERED </td>
      <td> Message successfully delivered </td>
    </tr>
    <tr>
      <td> DELIVERING </td>
      <td> Sending message in progress </td>
    </tr>
    <tr>
      <td> FAIL </td>
      <td> Failed to send message </td>
    </tr>
  </tbody>
</table>

## What if I didn't put in my msgid?

Sending something like this:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/
```

Would give you the status of all the SMS that you sent within 90 days.

## There's a lot of stuff on my screen! Can I get statuses by date?

Sure! You can include a date parameter to get your SMS statuses on the day (date format is year-month-day), something like this:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/?sent_date=2017-10-31
```

If you didn't send an SMS message during that period, it will still return a 200 OK response, but it'll be empty:

```
HTTP/1.0 200 OK
Content-Type: application/json

[]
```

You only can get statuses within 90 days of the current date. Otherwise, you will get this response:

```
HTTP/1.0 400 Bad Request
Content-Type: application/json

{
    "sent_date": [
        "Invalid sent_date"
    ]
}
```

You'll also get a 400 Bad Request response if your parameters are incorrect.

And that's it! There are more details in our [SMS documentation](http://docs.xoxzo.com/en/sms.html#check-sms-status-api) which you can check out as well!

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our [Xoxzo web API](https://www.xoxzo.com/). 

Here you can find all the Xoxzo tutorials:

Xoxzo web API tutorials by Miko:

- [Create your first API user](https://blog.xoxzo.com/en/2017/10/13/create-your-first-apiuser/)
- [Sending your first SMS](https://blog.xoxzo.com/en/2017/10/31/sending-your-first-sms/)
- [Checking your SMS status](https://blog.xoxzo.com/en/2017/11/15/checking-your-sms-status/)
- [Making a Simple Playback Call](https://blog.xoxzo.com/en/2021/11/08/making-a-simple-playback-call/)
- [Voice authentication using Text To Speech (TTS)](https://blog.xoxzo.com/en/2021/11/01/making-a-voice-authentication-call-with-tts/)

Other Xoxzo tutorials:

- [Let's use the dial-in number](https://blog.xoxzo.com/en/2017/07/01/dialinnumbers-tutorial/)
- [How to set up two-factor authentication using SMS](https://blog.xoxzo.com/en/2021/11/22/introduction-2fa-sms/)
- [How to set up Two-Factor Authentication using VOICE](https://blog.xoxzo.com/en/2018/05/14/introduction-2fa-voice/)
- [0120 isn’t the only toll-free option for callers! (How to use a toll-free number)](https://blog.xoxzo.com/en/2021/10/28/freecall-numbers-introduction/)
- [Setting up my first online voicemail](https://blog.xoxzo.com/en/2020/10/23/setting-up-my-first-online-voicemail/)
- [User experience on Xoxzo API (Part 1)](https://blog.xoxzo.com/en/2018/06/27/user-experience-on-xoxzo-api-part-1/)
- [User experience on Xoxzo API (Part 2)](https://blog.xoxzo.com/en/2018/07/03/user-experience-on-xoxzo-api-part-2/)
- [How to deal with text-count limit on SMS messages](https://blog.xoxzo.com/en/2017/12/28/sms-limit/)
 
 
Are you looking for an even simpler option to send SMS messages from your PC to customers and do you want to get started right away without coding? Check out our other service: [EZSMS](https://www.ezsms.biz/)! 
With [EZSMS](https://www.ezsms.biz/) you can start sending bulk SMS messages from the web right away. There are no initial or monthly fees: you only pay for what you use. You can also send customized messages to cater to each customer. 
[EZSMS](https://www.ezsms.biz/) supports SMS sending to 170 countries and it supports simultaneous sending to multiple destinations and delivery using CSV files that can be customized and mass-delivered.
You can send SMS anytime, anywhere. Complete it all online-Dial SMS to make your business or event a huge success!
See you next time! 



