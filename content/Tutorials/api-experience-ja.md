Title: Xoxzo APIのユーザーエクスペリエンス（第1回）
Date: 2018-06-27 12:00
Author: Ai Sin Chan
Tags: sms; api ユーザー; api; tutorial; UI; 体験;
Slug: user-experience-on-xoxzo-api-part-1
Thumbnail: images/apiexp1.jpg
Lang: ja
Summary: XoxzoのAPI　利用体験レポート

今日、Xoxzo APIを使ってSMSを送信し、テキスト読み上げや電話会議などの電話をかけ、テレフォニーユーティリティ機能のひとつ、キャリア検索を試してみました。
まずはじめに、私は試用 に [Xoxzo アカウント](https://www.xoxzo.com/ja/accounts/signup/)に登録し、そこへお試し用、おまけ50クレジットが付与されました。

![apiexp1](/images/XoxzoAPI_01_ja.png)

私は[最初のAPIユーザー](https://blog.xoxzo.com/ja/2017/10/13/create-your-first-apiuser/)を作成し、
以下のコマンドで使用する「API SID」と「認証トークン」を取得しました。

![apiexp2](/images/XoxzoAPI_02_ja.png)
![apiexp3](/images/XoxzoAPI_03_ja.png)

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
私は、[Xoxzo チュートリアル](https://blog.xoxzo.com/ja/2017/11/28/making-a-simple-playback-call/)のコマンドを 、私の環境に合わせて調整しました。私のコマンドは、こんな感じです。スクリーンショットも続いて御覧ください。

```
curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "recording_url=http://www.hubharp.com/web_sound/WalloonLilliShort.mp3" https://api.xoxzo.com/voice/simple/playbacks/
```

![apiexp4](/images/XoxzoAPI_04_ja.png) 

コマンドプロンプトにCallIDが表示されました。その後、私の電話が鳴り始めました。電話に出ると、ハープシコードの音楽が流れました。

音声コールの成功直後に、コマンドプロンプトに表示されたCallIDを指定し、コールステータスチェックAPIにてコールステータスをチェックしました。こちらが私のコマンドと、スクリーンショットです。

```
curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/calls/41c181b6-1817-4f91-8a4f-5e0cf5105092/
```

![apiexp5](/images/apiexp5.jpg)

私は自分のアカウントをチェックし、16クレジットが差し引かれ、34クレジットが残っているのを確認しました。こちらが、スクリーンショットです。

![apiexp6](/images/apiexp6.jpg)

テキスト読み上げ機能機能や電話会議APIなどの、他のVoice APIをテストするのに必要なクレジットが足りなくなってしまいました。40クレジットが、最低でも必要です。私は、テキスト読み上げ機能を使い、音声通話を試みたとき、失敗をしました。

curl -u <API SID>:<Auth Token> https://api.xoxzo.com/sms/messages/

![apiexp7](/images/apiexp7.jpg)

ですから、次に、[SMSの送信](https://blog.xoxzo.com/ja/2017/10/31/sending-your-first-sms/) を試したのです。こちらが、私の使ったコマンドで、続いてコマンドプロンプトのスクリーンショットです：

```
curl -u <API SID>:<Auth Token> --data-urlencode "sender=XoxzoBlog" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "message=これは初めてのSMSです。Xoxzoプラットフォームから送っています。" https://api.xoxzo.com/sms/messages/
```

![apiexp8](/images/apiexp8.jpg)

コマンドの後、メッセージIDが表示されました。その後、私は
[SMSのステータスを確認する](https://blog.xoxzo.com/ja/2017/11/15/checking-your-sms-status/)ため、このコマンドを実行しました。

![apiexp9](/images/apiexp9.jpg)

一方、SMS通知着信音が、私の携帯電話から聞こえました。私は[ウェブから送信されたSMS](https://www.xoxzo.com/ja/about/sms-api/)を受信したのです：

![apiexp10](/images/apiexp10.jpg)

50クレジットもかけず、私は、[テレフォニーユーティリティAPI](https://www.xoxzo.com/ja/about/utilities-api/)
- キャリア検索API を試してみることができました。私は日本の携帯電話番号とマレーシアの携帯電話番号を使ってこの機能を試しました。
私が実行したコマンドとスクリーンショット：

```
curl -u <API SID>:<Auth Token>  --data-urlencode "recipient=+81yyyyyyyy" https://api.xoxzo.com/utilities/carrierlookup/
```

![apiexp11](/images/apiexp11.jpg)
 
私が入力した日本の電話番号は、MVNOのAsahi Netから購読しました。MVNOは表示されず、実際のキャリア（この場合はNTT Docomo）が表示されました。私が入力したマレーシアの番号は、別のキャリア（Celcom）に変更したものでした。今回、変更前のキャリアであったMaxisが表示されました。私はナンバーポータビリティ（Mobile Number Portability）がベストエフォートベースでサポートされており、エンドキャリアに依存していることを認識しており、私の場合は反映されていないということです。

固定電話の番号を入力すると、返されるパラメータはすべて「null」でした。この機能は、携帯電話番号のみを対象としています。この機能は、使用されているかどうかにかかわらず、携帯電話番号の有効性をチェックするために使用できます。


![apiexp12](/images/apiexp12.jpg)
 
どの国の携帯電話番号もサポートされています。電話帳からさまざまな大陸の携帯電話番号を試しましたが、すべてに結果が返されました。スクリーンショットは、簡潔さ、明確さ、機密性の目的で省略します。

[(次回へ続く)](https://blog.xoxzo.com/ja/2018/07/03/user-experience-on-xoxzo-api-part-2/)
