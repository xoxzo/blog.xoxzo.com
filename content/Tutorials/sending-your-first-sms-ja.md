Title: 最初のSMSを送ってみよう！
Date: 2017-10-31 12:00
Author: Miko-chan
Tags: sms; api ユーザー; api; チュートリアル; みこちゃん;
Slug: sending-your-first-sms
Thumbnail: images/xoxtan.png
Lang: ja
Summary: さぁ、最初のSMSを送る準備はOK?

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>
<div class="lg-padding-top50 md-padding0">前回のチュートリアルでは、最初のAPIユーザーを作ったわよね？じゃぁ、XoxzoのAPIを使って何ができるのかもっと探検してみましょ？　一番シンプルな機能として、XoxzoのAPIと電話でできること、つまり、SMS（ショートメッセージ）の送信と、音声通話なんだけど、まずはSMSをお試しで送るように、進めちゃうわね！</div>
<div style="clear:both;"></div>

## 何を準備したらいいの?

必要なのは、パソコンに入っている、コマンド・プロンプトっていうもの(cmd)。LinuxやMacだと、ターミナルとかシェルって呼ばれてまーす。このチュートリアルでは、統一して「シェル」って呼ぶことにするわねっ！

![shell](/images/Tutorial/send-sms/shell.png)

次は、XoxzoのAPIサーバーに接続して、SMS送信のコマンドを処理させるためにHTTPリクエストを送るもの、それが必要ね。インターネット接続が必要なことは、もちろん言うまでもないけどね。


そして仕上げに、この前のチュートリアルでつくった、APIユーザーのAPIキーとトークンが必要ですから、用意してね。

## え？APIユーザーキーとトークンって、どこで探すんだったっけ・・・って？

アカウントにログインしたら、API SIDの欄と、Auth Token欄にある、ごちゃまぜテキストが、そのAPIユーザーのキーとトークン情報よ。見えてる部分はゼンブじゃないから、ダブルクリックしたりして、ゼンブをコピーしてね。ノートパッドなんかを使うと、見やすいわね！

トークンも、「トークン表示」ボタンをクリックして表示させてから、コピーしてね。

![SID and token](/images/Tutorial/send-sms/sidtoken.png)

Now that you have your API SID and Auth Token texts, put them together like this:

APiSiDtext:AUthT0k3ntext

Remember to put the colon ':' between the API SID and Auth Token and that they're written in a single line.

## Now let's send an SMS!

Let's try sending an SMS to your own phone first to see it in action. Note that you need to put down your phone number complete with the country code, with a '+' in front of it.

Type this in your shell prompt:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
--data-urlencode 'sender=XoxzoTest' \
--data-urlencode 'recipient=putyourphonenumberhere' \
--data-urlencode 'message=Hallo hello!' \
https://api.xoxzo.com/sms/messages/
```

You should be getting something like this message in return right after you type that: 
`[{"msgid":"tHi5i5y0urMsGIdt3xT"}]`
Which normally means that everything went well. You can also type the command in a single line without typing the '\' as well if you wish.

You should be receiving the message on your phone shortly. Your local carrier might not allow something like 'XoxzoTest' to appear as the sender, so another private number might appear instead.

And that's it! You've sent your first SMS! If you check your profile page, you'll also notice credits have been deducted after you send the SMS.

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our API.
