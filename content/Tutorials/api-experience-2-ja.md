Title: Xoxzo APIのユーザーエクスペリエンス（第2回）
Date: 2018-07-03 12:00
Author: Ai Sin Chan
Tags: sms; api ユーザー; api; tutorial; お試し; 2018
Slug: user-experience-on-xoxzo-api-part-2
Thumbnail: images/apiexp21.jpg
Lang: ja
Summary: Xoxzo API の体験レポート

Xoxzo APIを使った [私のユーザーエクスペリエンス]
(https://blog.xoxzo.com/ja/2018/06/27/user-experience-on-xoxzo-api-part-1/) の第2回 です。

[オーディオファイルの再生](https://www.xoxzo.com/ja/about/voice-api/)、
[SMS配信](https://www.xoxzo.com/ja/about/sms-api/)、および [キャリア検索 API](https://www.xoxzo.com/ja/about/utilities-api/)
を試したあと、私は当初の50クレジットがほぼなくなっていました。
だから、私は、アカウントにクレジットを補って、他の機能を試し続けました。

まずは、[テキスト音声変換API](https://www.xoxzo.com/ja/about/voice-api/)。このAPIはあなたが入力したテキストを読み上げることになっており、
通話上では音声として聞こえます。
サポート可能な言語は、英語と日本語です。
これは私が実行したコマンドであり、続いてWindows OSでのコマンドプロンプトのスクリーンショットが続きます。

```
curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "tts_lang=en" --data-urlencode "tts_message='Hello world, this is my first attempt at Xoxzo text-to-speech call. Testing, 1,, 2,,,3.'" https://api.xoxzo.com/voice/simple/playbacks/
```

![apiexp2](/images/apiexp21.jpg)

コマンドプロンプトにCallIDが表示されました。
テキスト音声変換/TTS（Text-to-Speech）を使った電話にでると、
[快活で滑らかな女性の声](https://blog.xoxzo.com/ja/2018/05/23/ivrflow/)に挨拶されました。
上記のコマンドで入力したテキストを読み上げたものです。
私は、[TTSチュートリアル](https://blog.xoxzo.com/ja/2021/11/01/making-a-voice-authentication-call-with-tts/)
で提案されていた通り、数字と数字の間に、カンマをいくつか入れて、
実験しました。数同士の間がほんの少し開いたことに気づきました。

その後、提供されたCallIDを使用して、自分のテキスト音声変換を使った通話の、ステータスを確認しました。
以下が、私の使用したコマンドとスクリーンショットです。

```
curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/calls/7142d264-a945-41ed-8dcb-c28dc7a8c339/
```

![apiexp2](/images/apiexp22.jpg)

テキスト音声変換に満足した後、私は [会議APIウェブ](https://www.xoxzo.com/ja/about/voice-api/#conference)から発信する電話を2つの番号に発信しました。
両方の受信者が応答すると、その通話はブリッジされ、お互いに話すことができました。
以下が、私の使用したコマンドとスクリーンショットです。

```
curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "participants=+81yyyyyyyy,+81zzzzzzzz" https://api.xoxzo.com/voice/simple/conferences/
```

![apiexp2](/images/apiexp23.jpg)
 
コマンドが正常に入力されると、Conference IDが1つとCallIDが2つ返されます。
その間、私の電話が鳴り、私はそれに応答し、通常の電話のように、もうひとりの受信者と話すことができました。
私たちのどちらも、相手にダイヤルしていないのに、私たちはともかく電話を受けて通話ができました。

次に、Conference IDを入力して、会議通話のステータスを確認しました。こちらが私のコマンドと、スクリーンショットです。

```
curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/simple/conferences/b600722b-d1e0-4eaf-a4a9-ba33bfcc2560/
```

![apiexp2](/images/apiexp24.jpg)

[新規アカウント作成](https://www.xoxzo.com/ja/accounts/signup/)時に、無料で付与されるお試し用 50クレジットは、
1通話やSMS数通、キャリア検索を数回試すのにちょうどいい量です。
ですから、音声通話やオーディオファイルの再生、テキスト/音声通話、または会議通話のどれを試すのかを選んでください。
また、[毎分の通話料金](https://www.xoxzo.com/ja/about/pricing/voice/#outbound-call)は 40クレジット未満ですが、
音声通話の最小要件であるクレジットが40を超えている間に、行う必要があります。
これは、クレジットが足りなくなる前に、通話に少なくとも数分かかることは確実だとして、こうなっているのでしょう。
もちろん、クレジットを購入し、より多くの機能を使用し、より多くの通話を行うことができます。

私の感想ですか？[XoxzoのAPI](https://www.xoxzo.com/ja/) は、本当に使いやすかったです。私がインターネットに接続したコンピュータから、ウェブテレフォニーを使用して、SMSを送信したり、さまざまな音声通話を行うのは初めてのことです。APIを試すのに、開発者である必要はありません。基本的なコンピュータリテラシー、特に基本的なコマンドライン・インターフェイス（CLI）スキルで十分なのです。
