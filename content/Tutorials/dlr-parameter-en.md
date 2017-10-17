
Title: 【Xoxzo】New Released callbackurl parameter
Date: 2017/10/17
Author: Aiko Yokoyama
Tags: dlr; tutorial;
Slug: dlr-parameter-tutorial
Lang: en
Summary: Xoxzo has just released a parameter, "callbackurl" on both SMS/VOICE to check the status of actions being made. Here you can check how the sample codes are.

Thank you for using [Xoxzo - Cloud Telephony Platform](https://www.xoxzo.com/en/).

We are glad to announce a new feature release, “callbackurl” parameter to be used in both [SMS API](http://docs.xoxzo.com/en/sms.html) and [Voice API](http://docs.xoxzo.com/en/voice.html).

With this parameter, you will be able to receive the result of your action at your favorite URL. Status of SMS delivery will be called when the carrier network notifies Xoxzo of the SMS delivery status (DLR) and status of Voice will be called when the call ended.

Please refer these sample code below for how to use this parameter.

#SMS delivery status check
```javascript
#!/bin/sh
# You should get SID and AUTH_TOKEN from XOXZO console
curl -u $SID:$AUTH_TOKEN \
     --data-urlencode 'sender=+818011112222' \
     --data-urlencode 'recipient=+818033334444' \
     --data-urlencode 'message=おはよう' \
     --data-urlencode 'callbackurl=http://example.com/receive_dlr/' \
     https://api.xoxzo.com/sms/messages/
```
#VOICE result check
```javascript
#!/bin/sh
# You should get SID and AUTH_TOKEN from XOXZO console
curl -v -u $SID:$AUTH_TOKEN \
     --data-urlencode 'caller=+818011112222' \
     --data-urlencode 'recipient=+818033334444' \
     --data-urlencode 'tts_message=おはよう' \
     --data-urlencode 'tts_lang=ja' \
     --data-urlencode 'callbackurl=http://example.com/receive_dlr/' \
     https://api.xoxzo.com/voice/simple/playback/
```


You may refer more details from below:<br>
[Callbackurl for SMS delivery](http://docs.xoxzo.com/en/sms.html)<br>
[Callbackurl for Voice](http://docs.xoxzo.com/en/voice.html)
