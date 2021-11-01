Title: Voice authentication using Text To Speech (TTS)
Date: 2021-11-01 10:00
Author: Miko-chan
Tags: voice api; text to speech tts; mikochan; 2fa; 2018;
Slug: making-a-voice-authentication-call-with-tts
Thumbnail: images/xoxtan.png
Lang: en
Summary: This tutorial shows you how to read your auth code using TTS via a single API call

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>

Hello everyone! Miko-chan took a short break from writing tutorials. We're busy
improving and fixing our APIs to make it better for you, but now I am back so
let us get started with a new tutorial!

In our previous tutorial, we've [learned how to make a Simple Playback Call]({filename}./making-a-simple-playback-call-en.md) which just makes an outbound call to a certain number and plays an mp3
file that you specify. 

In this tutorial, I am going to show to you how to make a voice call while
specifying what you want to say using Text To Speech (TTS). 

By using TTS, you can dynamically change what you say when the call is answered. 
Because the message can dynamically be changed, a common use case is to read out
authentication codes to the recipient of the call, instead of sending the code via SMS.

Some of the biggest services on the internet like Google and Facebook use this
method to authenticate that you actually have physical possession of the phone.

<div style="clear:both;"></div>

## What Do I Need? ##

- You will need a valid caller and recipient phone number using the
[E.164 number format](https://en.wikipedia.org/wiki/E.164), which means the numbers
must have country code with a + before it.
- You will also need an API User to use the API. You can refer to my earlier
[tutorial on how to create your first API user]({filename}./create-your-first-apiuser-en.md) on
how to create one if you don't have one yet.
- Xoxzo's API does not create your auth code for you, so you will need the auth code
that you want to pass to the recipient.

## Let's make that call! ##

Let's say your service is called "My super service" and you want to pass the
auth code "1234" (one two three four) to the recipient. You will want to greet the recipient so they
know who you are before you read out the auth code, so this might be the message
that you want to say: 

"Hello, this is my super service. Your auth code is 1234".

It is good user experience to repeat the auth code twice, so your users will
have time to remember or write it down, so we will repeat the auth code part:

"Hello, this is my super service. Your auth code is 1234. I repeat. Your auth
code is 1234".

The URL to make a simple playback call is `https://api.xoxzo.com/voice/simple/playbacks/`.
So using curl, the typical command to make a call would be:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
--data-urlencode 'caller=thecallerphonenumber' \
--data-urlencode 'recipient=yourphonenumber' \
--data-urlencode 'tts_lang=en' \
--data-urlencode 'tts_message="Hello, this is my super service. Your auth code
is 1234. I repeat. Your auth code is 1234"' \
https://api.xoxzo.com/voice/simple/playbacks/
```

You should get a callid response in return: `[{"callid":"YoUr-5ucc355fuL-c4lL-Uu1D"}]` which you
can use to [check the status of the call later, as shown in our
docs](http://docs.xoxzo.com/en/voice.html#checking-call-status)

If you tried the example above, you may notice that your auth code is spoken as
"one thousand two hundred and thirty four" instead of "one two three four" as
expected. You might want to make the speed when reading out the auth code
slower. In order to do this, you can add some punctuations like so in your
`tts_message`:

`
tts_message="Hello, this is my super service. Your auth code is 1,,2,,3,,4. I
repeat. Your auth code is 1,,2,,3,,4"
`

And that's it!

Your user can now use the auth code you just told her over the phone and access
your super service. You also now know that the phone number you called to tell
her the code exists, and she is *probably* a real person!

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our API.

Until next time! Miko out!
