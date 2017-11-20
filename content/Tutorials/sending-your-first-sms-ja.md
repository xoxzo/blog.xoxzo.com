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

アカウントにログインしたら、API SIDの欄と、Auth Token欄にある、ごちゃまぜテキストが、そのAPIユーザーのキーとトークン情報よ。見えてる部分はゼンブじゃないから、ダブルクリックしたりして、全体をコピーしてね。ノートパッドなんかを使うと、見やすいわね！

トークンも、「トークン表示」ボタンをクリックして表示させてから、コピーしてね。

![SID and token](/images/Tutorial/send-sms/sidtoken.png)

できたら、あなたの API SID と Auth Token を、コロン(:)をはさんで、サンドしちゃってください！こんなふうにね！

APiSiDtext:AUthT0k3ntext

大事なポイントは、間のコロンを 忘れないこと、と、全体を１行に書いてね、ってことかな。

## では、おくっちゃいましょう！

まずは、あなたの携帯に、実際の送信を確かめるために、送ってみちゃおうね。 あなたの携帯電話番号を、国コード（日本は『81』でーす）の前に『＋』を付けて、書き出しておいてね。

そして、シェルプロンプトに、下の通り、書いてみてね。

```
curl -u あなたのAPI SID:あなたのAuth Token \
--data-urlencode 'sender=XoxzoTest(送り主として表示されます)' \
--data-urlencode 'recipient=『+81』を付けたあなたの携帯電話番号' \
--data-urlencode 'message=Hallo hello!（ご希望のメッセージ）' \
https://api.xoxzo.com/sms/messages/
```

そうしたら、すぐに、答えが下のように返ってくるはず: 
`[{"msgid":"tHi5i5y0urMsGIdt3xT"}]`
そして、それが、送信がうまく行ったという印よ。
バックスラッシュ『\』を使わずに、上記のコマンドをゼンブ、１行に書いてしまっても、オッケー！

ちょっと待っている間に、あなたの携帯に、メッセージが届くはず。キャリアによっては、送信主をあなたの設定通りには表示してくれないから、別の番号に置き換えられて届くことも、あるけどね。

SMSの送信は、これで完了！はじめてのSMS送信は、どうだった？送信後に、アカウントのプロフィールページをチェックしてね。送信に使った分、クレジットもちゃんと、減ってるはずよ。 

XoxzoのAPIを使ってできる、カッコイイこと [ドキュメンテーション](https://docs.xoxzo.com/ja/) を読んで
XoxzoのAPIを使ってできる、カッコイイこと [ドキュメンテーション](https://docs.xoxzo.com/ja/) を読んで、
XoxzoのAPIを使ってできる、カッコイイこと [ドキュメンテーション](https://docs.xoxzo.com/ja/) を読んで
XoxzoのAPIを使ってできる、カッコイイこと [ドキュメンテーション](https://docs.xoxzo.com/ja/) を読んで、チェックしてみてね
curl -u あなたのAPI SID:あなたのAuth Token \
