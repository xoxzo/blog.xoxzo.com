Title: New parameter "tags" released
Date: 2019-03-15
Slug: tags-with-xoxzo-api
Lang: en
Tags: xoxzo; new release; 2019; tags;
Author: Iqbal Abdullah
Summary: You can now categorize your API calls with the tags parameter

One of the functionality requests that we get concerns the categorization of API calls.

We have released a new functionality which allows you to do just that: Now you can
categorize your API calls by adding an optional **tags** parameter to your API calls.
You can even attach multiple tags to a single API call:

Example:

    #!/bin/sh
    # You should get SID and AUTH_TOKEN from XOXZO console
    curl -u $SID:$AUTH_TOKEN \
         --data-urlencode 'sender=+818011112222' \
         --data-urlencode 'recipient=<recipient>' \
         --data-urlencode 'message=Hello world' \
         --data-urlencode 'tags=tag1,tag2,tag3' \
         https://api.xoxzo.com/sms/messages/

These tags data will be attached to your SMS and Voice API calls that you make,
and can be retrieved via the [Check SMS Status API](https://docs.xoxzo.com/en/sms.html#check-sms-status-api)
and the [Checking Call Status API](https://docs.xoxzo.com/en/voice.html#checking-call-status) respectively.

Example:

    #!/bin/sh
    # You should get SID and AUTH_TOKEN from XOXZO console
    curl -u $SID:$AUTH_TOKEN \
        https://api.xoxzo.com/sms/messages/7sBZmVznoXJap2wkMIlihgPKqjdOGS1f/

Returned data :

     {
        "sender": "8011112222",
        "msgid": "7sBZmVznoXJap2wkMIlihgPKqjdOGS1f",
        "status": "DELIVERED",
        "cost": 10,
        "sent_time": "2019-03-15 08:29:09",
        "tags": [
            "tag1",
            "tag2",
            "tag3"
        ],
        "url": "https://api.xoxzo.com/sms/messages/7sBZmVznoXJap2wkMIlihgPKqjdOGS1f/",
        "recipient": "<recipient>"
    }

You can use the tags data to categorize your usage of our API, for example,
using different tags for different marketing campaigns or block of customers to
differentiate between them and different messaging that you use.

In the future, we plan to make it easier for you to visualize how
effective the different types of your messages and calls are, using these tags data.

For more information on how to use the **tags** parameter, please refer to our [Send SMS
Messages API](https://docs.xoxzo.com/en/sms.html#send-sms-messages-api) and [Simple Playback Voice API](https://docs.xoxzo.com/en/voice.html#simple-playback-api)
