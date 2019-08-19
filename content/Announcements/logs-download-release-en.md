Title: New release: Logs download feature
Date: 2019-08-13
Slug: logs-download-feature-new-release
Lang: en
Tags: download logs; new release; 2019;
Thumbnail: images/freepik/young-females-download-icon.jpg
Author: Iqbal Abdullah
Summary: You can now download your usage logs from the dashboard directly.

We're excited to announce a small but significant new release today: You can now
download your usage logs directly from the dashboard, instead of only from the
API.

## What and why?

This is one feature which has been asked from our customers many times. Up until
now, you can only retrieve past sent messages data from the
**[Check SMS status API](https://docs.xoxzo.com/en/sms.html#check-sms-status-api)**

The Check SMS status API has limitations: The main intention of the Check SMS status
API was to allow you to check the status of specific messages quickly. It does allow you
to get message statuses within a period of time, but there is a limit of message statuses
that you can access in a single request.

Our customers makes tens of thousands of requests in a day, so they hit that
limit pretty easily. They wanted a way to easily see their usage logs for
an extended period of time for analytics purposes, which be as much hundreds of thousands
of messages. Other similar platforms only allow a maximum of a few days of logs
history to be downloaded, and that was not enough for our customers.

Due to technical limitations on our infrastructure, it was a challenge to build
something that allows our customers to retrieve their huge usage logs in a simple and
quick manner. It took us time but we've finally figured it out and you now can
download your usage logs directly from the dashboard in CSV format.

The csv file will contain the following data:

- sender
- url
- msgid
- tags
- sent_time
- recipient
- status
- cost
- apiuser

You can download logs for requests **up to 42 days in the past.**

## So how do I download my logs?

Simple! Just click on the _Download Usage Logs_ link on the left side of your
Dashboard:

![Download dashboard](/images/logs-download-feature-screenshot.png)

You can choose specific dates to download or a preset timeframe such
as the _last 7 days_, or the _last 30 days_.

Your download process will start as a background process, and you can come back later if your
download takes some time to finish.

## What's next?

For now, only the SMS messaging logs are available. We plan to add other logs
into the download logs feature, so that you can get all your usage logs from one
place.

Thank you to rawpixel.com for the thumbnail:
[Background photo created by rawpixel.com - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
