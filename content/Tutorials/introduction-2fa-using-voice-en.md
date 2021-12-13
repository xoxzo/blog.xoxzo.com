Title: How to set up Two-Factor Authentication using VOICE
Date: 2018-05-14 10:00
Author: Akira Nonaka
Tags: 2FA; Tutorial; Voice; API;
Slug: introduction-2fa-voice
Lang: en
Summary: Learn how to add Two-Factor Authentication using VOICE on your Web-applications!


[Last tutorial was to show you how to introduce two-factor authentication using SMS.](https://blog.xoxzo.com/en/2021/11/22/introduction-2fa-sms/)
But we have some situation that we cannot use SMS.
For example, the case that the recipient's phone is a landline, not a mobile phone.
Do not worry, we can still deliver the PIN using [VOICE API](https://www.xoxzo.com/en/about/voice-api/).

There needs some attention on formatting the message, when you use VOICE API, as we want the recipients to be able to properly hear the PIN.

1. Repeat the PIN readouts at least twice
1. Add an appropriate pausing before starting the PIN readouts after the call is picked.

This kind care of your heart will give a good extra space to the recipients to perhaps parepare for their jotting down.

This is the message example.
```
Hello This is Xoxzo. Please do not disclose the Pin number that you are going to hear.
Your Pin number is number nine, number seven, number two and number nine.
I repeat.
Your Pin number is number nine, number seven, number two and number nine.
Thank you for using, good bye.
```

Please find the sample code with Python[^1]. Although the basic structure is the same as sending by SMS, you will see a tiny wisdom at the message generation procedure.

```
import os
import secrets
from xoxzo.cloudpy import XoxzoClient


def two_fa_voice():
    """ two-factor authentication by VOICE　"""
    # Generating random PIN
    secret_key = secrets.randbelow(10000)
    message = gen_voice_msg(secret_key)
    # Assume that the secret key to call API is saved as an environment variable
    # Please retrieve your SID and TOKEN from your signed in account on https://www.xoxzo.com/
    sid = os.getenv('XOXZO_API_SID')
    auth_token = os.getenv('XOXZO_API_AUTH_TOKEN')

    # Calling recipient phone
    xc = XoxzoClient(sid=sid, auth_token=auth_token)
    result = xc.call_tts_playback(caller="0801234567", recipient="+818054695209", tts_message=message, tts_lang="ja")


def gen_voice_msg(secret_key, key_length=4):
    prefix_str = "Hello This is Xoxzo. Please do not disclose the Pin number that you are going to hear.
Your Pin number is"
    mid_str = "I repeat, your Pin number is"
    postfix_str = "Thank you for using, good bye."
    fmt_str = "%%0%dd" % key_length
    num_str = fmt_str % secret_key

    key_str = ""
    for st in num_str:
        key_str += "Number %s," % st
    return prefix_str + key_str + mid_str + key_str + postfix_str
```
 
#Summary

This is how you can execute two-factor authentication using VOICE. 
Different from the text sending SMS, there requirs some heartful care 
to create a message that is easy to listen.

[^1]:It is assumed to use Python 3.6 or later. There is no *secrets* package by default in Python before that ver., so you will need to use the appropriate random number generation library.
