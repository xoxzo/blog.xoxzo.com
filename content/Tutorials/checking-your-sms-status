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
Now that we managed to send an SMS in the previous article: [Sending your first SMS](https://blog.xoxzo.com/2017/10/31/sending-your-first-sms/), you'll notice that we get a msgid string in return after we run the CURL command, like so:
`[{"msgid":"tHi5i5y0urMsGIdt3xT"}]`
We know that we sent the SMS correctly, otherwise the return message will be different. But how do we know if the SMS is actually received?
</div>
<div style="clear:both;"></div>

## SMS checking command

We'll still use CURL to check the SMS status, similar to how we sent an SMS. The difference will be in the parameters we provide and the url.

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
    "status": "OK",
    "sent_time":"2015-08-27 09:22:32",
    "cost": 10,
    "sender": "your_number",
    "recipient": "your_recipientnumber",
    "url": "https://api.xoxzo.com/sms/messages/tHi5i5y0urMsGIdt3xT/",
    "msgid": "tHi5i5y0urMsGIdt3xT"
}
```

Of course, the cost will depend on which number you are sending too. You can get the pricing details here: [SMS Pricing](https://www.xoxzo.com/en/about/pricing/#sms)

The SMS statuses is in this list:
|---|---|
| QUEUED | Message put into queue and will be delivered shortly |
| OK | Message successfully delivered |
| DELIVERING | Sending message in progress |
| FAIL | Failed to send message |

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

If you didn't send an SMS during that date, it will still return a 200 OK response, but it'll be empty:

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

And that's it! There's more details in our [SMS documentation](http://docs.xoxzo.com/en/sms.html#check-sms-status-api) which you can check out as well!

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our API. 

Until next time!
