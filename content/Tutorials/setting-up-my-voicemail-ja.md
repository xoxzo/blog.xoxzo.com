Title: 「自分専用」のボイスメールを設定してみる
Date: 2020-10-23 10:00
Authors: Iqbal Abdullah, Josef Monje
Tags: コロナ禍; リモートワーク; 2020; ボイスメール;
Slug: setting-up-my-first-online-voicemail
Thumbnail: images/Voicemail.png
Lang: ja
Summary: Xoxzoで自分専用のボイスメールを設定してみました。その方法を記しておきます。

このコロナ禍で、多くの人が同じことをしていると思いますが、わたしも外出を控えて様々なショッピングサイトから、注文して配達を頼んでいました。
ショッピングサイトの登録時には、たいてい電話番号も入力するよう求められていました。

悲しいことに、しばらくするとわたしの電話にセールスの電話がかかってきたり、SMSが届いたりするようになりました。

# ダイヤルインナンバー(DIN)とボイスメール

そこで、Xoxzoがリリースした [ボイスメール機能]({filename}/Announcements/2020-10-20-voicemail-release-en.md)を使い、
ショッピングサイトの登録用に使う番号をあっさり入手することができました。
これまでは、Xoxzoでは入電に対し、転送を行ったり、テキスト読み上げ機能やオーディオファイルを使って応答することしか
できませんでした。しかしボイスメール機能がくわわったことで、相手からのメッセージを保管しておけるようになったのです。

伝言を聞いておいてもらえる機能というのが、わたしにとっては重要でした。
というのも、ショップからの電話はやむを得ず電話連絡している場合もあるかもしれないからです。
ですから、留守録したメッセージを保管しておいてくれて、そのメッセージの着信を連絡してくれる、そういう方法を探していたのです。

どうやってこれを設定するのか、というところは、下記をお読みください。

## APIユーザーを作る

[アカウントの作成](https://www.xoxzo.com/ja/accounts/signup/)後、電話番号の取得に必要な認証情報を得るために、
APIユーザーを作ります。取得する電話番号が、ショッピングサイトの登録などに使う電話番号となります。

- [ログイン](https://www.xoxzo.com/ja/accounts/login/)したら、APIユーザ　ダッシュボードが表示されます。 右側の**APIユーザ追加** ボタンをクリックし、新規APIユーザを作りましょう
- APIユーザにつけるニックネームを設定する画面が表示されます。このAPIユーザを使う目的など、たとえば”Amazon”などわかりやすい名前を設定してください。
- ダッシュボードに戻ります。つぎに必要なのは、今作成した新規APIユーザの **API SID** と **Auth Token** です。後ほど必要になるので、コピーをとってください。

## アクションURLの設定

取得する電話番号への着信をXoxzoのシステムが受け取った時、システムに何をしてほしいのかをお知らせください。
ボイスメールを取得する前に、この準備を行ってください。

Xoxzoのシステムは、`action_url` という特定のURLへリクエストを出します。
このURLは、ご自身で設定してください。このURLを、ボイスメールを使いたい番号を取得する際、指定します。
ご自身で設定するURLですから、どこかでホストされているものでなくてはなりません。

このURLをご自分でホストしてもよいのですが、Xoxzoシステムがリクエストを出して この `action_url` がレスポンスを返すのは
ほんの少しのテキストのみとなります。Xoxzoからのリクエストに対するレスポンスをプログラム的に変更できれば、
かかってきた電話をどのように扱いたいのかを変更できる強力な方法となります。

今回のエクササイズでは、着信した電話をボイスメールに保管するというだけのことに焦点を当てています。
ですから、派手なロジックは必要なく、このテキストをホストできるだけのシンプルなもので良いのです。

Xoxzoの中には、Github Gist を使っている人もいます。
github.com へのサインアップは無料ですし、このテキストをオンラインにおいておく `action_url` としては、
手早い方法ですね。後ほど、この`action_url` と他のテキストを使って構成を行いますが、そのテキストが、gist のファイルの内容となります。
gist を保存し、**raw** ボタンでプレーンテキストとして確認することができます。自分の gist を見ているときには、
右側に表示されています。この raw gist を表示しているときの URL をコピーしておいてください。ご自分の `action_url` となります。

## 電話番号を取得する

まず、ダイヤルインナンバー（DIN）を取得しましょう。
取得可能な番号を探すには、XoxzoAPIに、ご自分の API SID と Auth Token を使ってリクエストを出します。
`curl` のプログラムがインストールされている場合、このような感じになります。

```
curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/dins/
```

このリクエストを出すには、どんなプログラムを使っても、またどんなプログラミング言語を使っていただいても大丈夫です。
ここでは、コマンドラインのリクエストとして一般的である `curl` を使った例をサンプルとして用いています。

このリクエストを出すと、取得可能なダイヤルインナンバーのリストが返されます。
どの電話番号を取得するか決まったら、次に行う取得に必要となりますので、その番号の `din_uid` を控えてください。
その後この番号に、`actiona_url` を併記する際にも使用します。

ダイヤルインナンバーの取得には、APIへ `POST` リクエストを出してください。

```
curl -u <SID>:<AUTH_TOKEN> -d'din_uid=<din_uid>' https://api.xoxzo.com/voice/dins/subscriptions/
```

When this request succeeds, your subscription starts immediately and your credits will be charged.
You can read more about this process in our [documentation](https://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api).

### Remember to attach the `action_url` to your number

At this point, the DIN doesn't do anything yet so the next step is to attach an `action_url`.
The voicemail system can be configured to use either **text-to-speech** or an **mp3** file hosted
somewhere for the voicemail greeting. In this example, we're using text-to-speech.

For a text-to-speech greeting, put `voicemail say` in your `action_url` followed by
the [language code](https://docs.xoxzo.com/en/utilsapi.html#tts-lang-label) and your message enclosed in quotes:

```
voicemail say en "Hello, you have reached my voicemail. I cannot answer the phone right now, but I will return your call as soon as I can..."
```

This is the content of the `action_url`. If you haven't created a GitHub gist mentioned earlier,
create one now with your preferred greeting. Get the URL of the **raw** gist and that will be the URL.
Once you have that URL, you can attach it to the DIN:

```
curl -u <SID>:<AUTH_TOKEN> -d'action_url=<url>' https://api.xoxzo.com/voice/dins/subscriptions/<din_uid>/
```
 
Once this is done, you're ready to receive voicemail messages.

## Receiving voicemails to your new number

It works just like any voicemail. When someone calls your DIN, they hear a greeting and they
can leave a message. The message gets recorded and all the recordings will be available for your use later.

### Listening to your voicemails

To listen to your voicemail messages, login to your Xoxzo account and you'll find a link to your 
`Voicemail Records` on the left. There you'll see a list of your recordings with information such as when it happened and who called.
You can download or delete recordings and, if you start getting a lot of messages, you can filter by date, caller, DIN, or API user.

# Your voicemail is setup

And that's it! Perhaps the most difficult part is figuring out how to host your
`action_url` but once that's done, it's a straightforward process all the way.

You can now use it as a contact phone number for non-important stuff.
Anyone can still get in touch with through it, but you won't be sharing
your real personal or work numbers with everyone that you need to interact with on the
internet.
