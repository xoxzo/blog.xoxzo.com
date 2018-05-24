Title: How to set up Two-Factor Authentication using VOICE
Date: 2018-05-25 10:00
Author: Akira Nonaka
Tags: 2FA; Tutorial; Voice; API;
Slug: introduction-2fa-voice
Lang: en
Summary: Learn how to add Two-Factor Authentication using VOICE on your Web-applications!


[Last tutorial was to show you how to introduce two-factor authentication using SMS.](/introduction-2fa-en.md)
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
    # APIを呼び出すための秘密鍵は、環境変数に保存されているものとします
    # SIDとTOKENはhttps://www.xoxzo.com/からサインアップして入手してください
    sid = os.getenv('XOXZO_API_SID')
    auth_token = os.getenv('XOXZO_API_AUTH_TOKEN')

    # Calling recipient phone
    xc = XoxzoClient(sid=sid, auth_token=auth_token)
    result = xc.call_tts_playback(caller="0801234567", recipient="+818054695209", tts_message=message, tts_lang="ja")


def gen_voice_msg(secret_key, key_length=4):
    prefix_str = "こんにちは、ゾクゾーです。これからお伝えする暗証番号は誰にも教えないでください。あなたの暗証番号は、"
    mid_str = "です。繰り返します。あなたの暗証番号は、"
    postfix_str = "です。ご利用、どうもありがとうございました。"
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

[^1]:Python3.6以降の利用を想定しています。それよりも前のPythonには標準では *secrets* パッケージがないので、
適当な乱数生成ライブラリを使う必要があります。
