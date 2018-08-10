Title: Xoxzo APIのユーザーエクスペリエンス（第1回）
Date: 2018-08-10
Author: Ai Sin Chan
Tags: sms; api ユーザー; api; tutorial; UI; 体験;
Slug: User-experience-on-Xoxzo-API-Part-1
Thumbnail: images/apiexp1.jpg
Lang: ja
Summary: XoxzoのAPI　利用体験レポート

今日、Xoxzo APIを使ってSMSを送信し、テキスト読み上げや電話会議などの電話をかけ、テレフォニーユーティリティ機能のひとつ、キャリア検索を試してみました。
まずはじめに、私は試用 に [Xoxzo アカウント](https://www.xoxzo.com/ja/accounts/signup/)に登録し、そこへお試し用、おまけ50クレジットが付与されました。

![apiexp1](/images/apiexp1.jpg)

私は[最初のAPIユーザー](https://blog.xoxzo.com/ja/2017/10/13/create-your-first-apiuser/)を作成し、
以下のコマンドで使用する「API SID」と「認証トークン」を取得しました。

![apiexp2](/images/apiexp2.jpg)
![apiexp3](/images/apiexp3.jpg)

次にラップトップに[CURL](https://curl.haxx.se/dlwiz/?type=*) をダウンロードしました。
私はWindows OSを搭載したIntelプロセッサを使用しているので、
ノートパソコンの仕様と互換性のある、特定の実行可能ファイルを選択しました。
次に、CURL実行ファイルとライブラリファイルを格納するディレクトリ（フォルダ）にて、
Windowsコマンドプロンプトからすべてのコマンドを実行しました。

コマンドプロンプトに慣れている人は、ナビゲートには、CDコマンドが必要なだけです。
それ以外はCURL関数です。コマンドプロンプトを使用したことのない方は、ユーザーマニュアルをチェックし、
[コマンドプロンプトの使い方](https://techacademy.jp/magazine/5318)を小一時間ほど、勉強するといいかと思います。
実際には、CD（ディレクトリの変更）には少数のコマンドを使って練習するだけで十分です。


I decided to start with [Voice API](https://www.xoxzo.com/en/about/voice-api/) – Audio File Playback API. I found an MP3 audio file playing harpsichord music with a [URL pointing to it](http://www.hubharp.com/web_sound/WalloonLilliShort.mp3), this is a pre-requisite to run the API. I modified the commands from the [Xoxzo tutorial](https://blog.xoxzo.com/2017/11/28/making-a-simple-playback-call/) to suit my situation. Here’s the command I issued, followed by the screenshot from my Command Prompt: 

```
curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "recording_url=http://www.hubharp.com/web_sound/WalloonLilliShort.mp3" https://api.xoxzo.com/voice/simple/playbacks/
```

![apiexp4](/images/apiexp4.jpg) 

A Call ID was displayed on Command Prompt. Then my phone started to ring. I answered and heard the harpsichord music playing through my phone. 

Immediately after the successful voice call, I checked the call status using the Check Call Status API, by specifying the Call ID displayed on Command Prompt. Here was the command I issued, followed by the screenshot:

```
curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/calls/41c181b6-1817-4f91-8a4f-5e0cf5105092/
```

![apiexp5](/images/apiexp5.jpg)

I checked my Xoxzo account, my credits were deducted by 16, and I was left with 34 credits, here is the screenshot:

![apiexp6](/images/apiexp6.jpg)
 
I no longer have enough credits to test out other Voice APIs, such as Text-to-Speech and Conference. The minimum required credits is 40. When I attempted to make a Text-to-Speech voice call, it failed.

![apiexp7](/images/apiexp7.jpg)
 
So, I tried [sending SMS](https://blog.xoxzo.com/2017/10/31/sending-your-first-sms/) next. This was the command I issued, followed by the screenshot of the Command Prompt: 

```
curl -u <API SID>:<Auth Token> --data-urlencode "sender=XoxzoBlog" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "message=Hello world, this is my first SMS sent over the Xoxzo platform." https://api.xoxzo.com/sms/messages/
```

![apiexp8](/images/apiexp8.jpg)
 
The Message ID was displayed after my command. Subsequently I issued this command to [check the SMS status](https://blog.xoxzo.com/2017/11/15/checking-your-sms-status/). 

![apiexp9](/images/apiexp9.jpg)
 
Meanwhile the SMS notification ringtone was audible on my mobile phone. I received the [SMS sent from the web](https://www.xoxzo.com/en/about/sms-api/):

![apiexp10](/images/apiexp10.jpg)
 
With less than 50 credits, I was still able to try out [Telephony Utilities API](https://www.xoxzo.com/en/about/utilities-api/) – Carrier Lookup API. I used a Japan mobile number and a Malaysia mobile number to try out this function. The commands I issued and the screenshot:

```
curl -u <API SID>:<Auth Token>  --data-urlencode "recipient=+81yyyyyyyy" https://api.xoxzo.com/utilities/carrierlookup/
```

![apiexp11](/images/apiexp11.jpg)
 
The Japan number I entered was subscribed from Asahi Net, an MVNO. The MVNO was not displayed, instead the actual infrastructure owner was displayed, in this case, NTT Docomo. The Malaysia number I entered had been ported to a different carrier (Celcom), in this case Maxis was displayed which was the carrier before porting. I am aware that the MNP (Mobile Number Portability) is supported on a best effort basis and is dependent on the end carrier, so in my case it is not reflected. 

When I entered a fixed line number, all the parameters returned were ‘null’. This function is only meant for mobile numbers. This function can be used to check validity of a mobile number, whether it is still in use. 

![apiexp12](/images/apiexp12.jpg)
 
Mobile numbers from any country is supported, I tried out a few more mobile numbers in various continents from my phone book, they all returned results. Screenshots are omitted for brevity, clarity, and confidentiality purposes. 

(to be continued)
