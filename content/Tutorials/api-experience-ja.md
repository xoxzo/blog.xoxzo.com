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
実際には、CD（ディレクトリの変更）にはほんの少しコマンドを使って練習するだけで十分です。

私は [音声通話API](https://www.xoxzo.com/ja/about/voice-api/) - オーディオファイル再生API から始めることにしました。
私は[ハープシコードの音楽を再生するMP3オーディオファイル](http://www.hubharp.com/web_sound/WalloonLilliShort.mp3)を見つけました。
それを指すURLが、APIを実行するための前提条件です。
私は、[Xoxzo チュートリアル](https://blog.xoxzo.com/2017/11/28/making-a-simple-playback-call/)のコマンドを 、私の環境に合わせて調整しました。私のコマンドは、こんな感じです。スクリーンショットも続いて御覧ください。

```
curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "recording_url=http://www.hubharp.com/web_sound/WalloonLilliShort.mp3" https://api.xoxzo.com/voice/simple/playbacks/
```

![apiexp4](/images/apiexp4.jpg) 

コマンドプロンプトにCallIDが表示されました。その後、私の電話が鳴り始めました。電話に出ると、ハープシコードの音楽が流れました。

音声コールの成功直後に、コマンドプロンプトに表示されたCallIDを指定し、コールステータスチェックAPIにてコールステータスをチェックしました。こちらが私のコマンドと、スクリーンショットです。

```
curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/calls/41c181b6-1817-4f91-8a4f-5e0cf5105092/
```

![apiexp5](/images/apiexp5.jpg)

私は自分のアカウントをチェックし、16クレジットが差し引かれ、34クレジットが残っているのを確認しました。こちらが、スクリーンショットです。

![apiexp6](/images/apiexp6.jpg)

テキスト読み上げ機能機能や電話会議APIなどの、他のVoice APIをテストするのに必要なクレジットが足りなくなってしまいました。40クレジットが、最低でも必要です。私は、テキスト読み上げ機能を使い、音声通話を試みたとき、失敗をしました。

![apiexp7](/images/apiexp7.jpg)

ですから、次に、[SMSの送信](https://blog.xoxzo.com/ja/2017/10/31/sending-your-first-sms/) を試したのです。こちらが、私の使ったコマンドで、続いてコマンドプロンプトのスクリーンショットです：

```
curl -u <API SID>:<Auth Token> --data-urlencode "sender=XoxzoBlog" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "message=これは初めてのSMSです。Xoxzoプラットフォームから送っています。" https://api.xoxzo.com/sms/messages/
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
