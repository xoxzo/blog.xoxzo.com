Title: ジブン専用のボイスメールを設定してみる
Date: 2020-10-23 10:00
Authors: Iqbal Abdullah, Josef Monje
Tags: コロナ禍; リモートワーク; 2020; ボイスメール;
Slug: setting-up-my-first-online-voicemail
Thumbnail: images/Voicemail.png
Lang: ja
Summary: Xoxzoでジブン専用のボイスメールを設定してみました。その方法を記しておきます。

このコロナ禍で、多くの人が同じことをしていると思いますが、わたしも外出を控えて様々なショッピングサイトから、注文して配達を頼んでいました。
ショッピングサイトの登録時には、たいてい電話番号も入力するよう求められていました。

悲しいことに、しばらくするとわたしの電話にセールスの電話がかかってきたり、SMSが届いたりするようになりました。

# ダイヤルインナンバー(DIN)とボイスメール

そこで、Xoxzoの [リリースしたボイスメール機能]({filename}/Announcements/2020-10-20-voicemail-release-en.md)を使い、
ショッピングサイトの登録用に使う番号をあっさり入手することができました。
これまでは、Xoxzoでは入電に対し、転送を行ったり、テキスト読み上げ機能やオーディオファイルを使って応答することしか
できませんでした。しかしボイスメール機能がくわわったことで、相手からのメッセージを保管しておけるようになったのです。

伝言を聞いておいてもらえる機能というのが、わたしにとっては重要でした。
というのも、ショップからの電話はやむを得ず電話連絡している場合もあるかもしれないからです。
ですから、留守録したメッセージを保管しておいてくれて、そのメッセージの着信を連絡してくれる、そういう方法を探していたのです。

どうやってこれを設定するのか、というところは、下記をお読みください。

## APIユーザーを作る

[アカウントの作成](https://www.xoxzo.com/ja/accounts/signup/)後、電話番号の取得に必要な認証情報を得るために、
APIユーザーを作ります。you'll need
[アカウントの作成](https://www.xoxzo.com/ja/accounts/signup/)後、電話番号の取得に必要な認証情報を得るために、you'll need
[アカウントの作成](https://www.xoxzo.com/ja/accounts/signup/)後、電話番号の取得に必要な認証情報を得るために、you'll need
to create an API User to get the credentials needed for subscribing to a number. This will be the
phone number which you'll give to the shops.

- After [logging in](https://www.xoxzo.com/en/accounts/login/), you'll be shown your "API Users" dashboard. Click on
  the "**Add API User**" button on the right side to start creating your API User.
- You'll be shown a screen to set the nickname of your API User. Set an easy to
  understand nickname like "Amazon" so you can easily remember what the API User is used for.
- You'll be shown back to the dashboard. What you need now is the **API SID** and **Auth Token** of your newly
  created API User. Copy these two, as we'll need them later.

## Setup action URL

You'll need to tell the Xoxzo platform what it should do when it receives a call
to your number. We need to set this up before getting a number for your
voicemail.

The Xoxzo platform makes a request to a particular URL which we call
`action_url`. This URL is set up by you, and you specify this URL when you
subscribe to a number. Because you need to set up a URL, it has to be hosted
somewhere.

You can of course host this URL on your own, but what your `action_url` will be
returning when the Xoxzo platforms make it request is only a bunch of text. If
you can programmatically change the text that you send back when Xoxzo makes its
request, it will be a powerful way for you to change how you handle the call that you
receive.

But for this exercise, we're only interested in storing incoming voice calls to
our voicemail, so there is only a simple need to host this text somewhere
without any fancy logics.

Some of us at Xoxzo use Github Gists for this. Signing up
for an account at github.com is free and it's a quick way to put text files online
for an `action_url`. At a later step, you'll configure the `action_url` with some text.
That text will be the content of the gist. You can save the gist and view it as plain text
by clicking the **raw** button. You can find it on the right side while viewing your gist.
While viewing the raw gist, take note of its URL. This will be the URL of your `action_url`.

## Subscribe to a number

The first thing you need to do is to subscribe to a DIN. To find numbers, send a
request to the Xoxzo API with your user's API SID and Auth Token. If you have the
`curl` program installed, the request looks like this:

```
curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/dins/
```

You can use any program or even programming language to make the request but we'll use
`curl` in the examples, since it's a common way to make requests in the command-line.

This request returns a list of available DINs you can choose from.
Once you've selected a DIN, take note of its `din_uid` because you need this to subscribe,
which is what we'll do next. You'll also need this later when we attach the `action_url` to the DIN.

To subscribe to a DIN, send a `POST` request to the API:

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
