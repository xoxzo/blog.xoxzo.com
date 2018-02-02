Title: Making a Simple Playback Call
Date: 2017-11-28 08:00
Author: Miko-chan
Tags: 音声; 通話; recording; api; チュートリアル; ミコちゃん;
Slug: making-a-simple-playback-call
Thumbnail: images/xoxtan.png
Lang: ja
Summary: 音声APIの、はじめての冒険へ出発！

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>
<div class="lg-padding-top50 md-padding0">
Now that we've <a href="https://blog.xoxzo.com/2017/10/31/sending-your-first-sms/">sent an SMS</a> and learned how to <a href="https://blog.xoxzo.com/2017/11/15/checking-your-sms-status/">check its status</a>, it's time we start exploring the Voice API of Xoxzo!
</div>
<div style="clear:both;"></div>

For this tutorial, we're going to start off with a simple implementation of voice: recording playback, or what we call simple playback. We're going to make a call and when the recipient picks up the phone, they will hear an mp3 file being played on the other end. Let's try it out on your own number so you can experience it firsthand!

## What Do I Need? ##

To start off, you will need to have an mp3 file stored somewhere online and a URL that links to it. Make sure that the link is public so that the API can use it. Keep in mind that the mp3 URL must only have safe characters, which are alphanumeric and these:
```- _ $ . * ' ( ) ! ?```

You'll also need a valid caller and recipient phone number using the [E.164 number format](https://en.wikipedia.org/wiki/E.164), which means the numbers must have country code with a + before it.

## Let's make that call! ##

The URL to make a simple playback call is `https://api.xoxzo.com/voice/simple/playbacks/`. So using CURL, the typical command to make a call would be:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
--data-urlencode 'caller=thecallerphonenumber' \
--data-urlencode 'recipient=yourphonenumber' \
--data-urlencode 'recording_url=theURLofyourmp3file' \
https://api.xoxzo.com/voice/simple/playbacks/
```

You should get a callid response in return: `[{"callid":"YoUr-5ucc355fuL-c4lL-Uu1D"}]`.

And that's it! There's a lot of uses you can get out of this, like sending a greeting/promotion call to your customers, or even as a reminder for a meeting. The possibility is as unlimited as your imagination.

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our API.

Until next time! Miko out!
