Title: 音声案内を発信しましょう！
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
こんにちワ〜！
もう、 <a href="https://blog.xoxzo.com/ja/2017/10/31/sending-your-first-sms/">SMSの送信、</a> もできちゃったし <a href="https://blog.xoxzo.com/ja/2017/11/15/checking-your-sms-status/">そのステータス確認</a>もできちゃった、というあなたは、今度はXoxzoの<a href="https://www.xoxzo.com/ja/about/voice-api/">音声API</a>の冒険にでかける時ですよぉ〜！
</div>
<div style="clear:both;"></div>

今回は、シンプルな音声通話：録音済み音声ファイルの再生の使い方から初めちゃうね。このAPIを使うと、こちらから電話をかけて、相手が出たら準備しておいたmp3ファイルを再生することができるのよ。まずは、自分の電話にかけて、テストしてみてね！

## 必要なものは？ ##

始める前に、mp3 音声ファイルを準備して、オンラインに保存してください。リンクを使うので、メモしておいてね！このリンク、APIが使うから、誰でもアクセス出来るようにしておいてね。あと、このURLに、通常の半角アルファベットや```- _ $ . * ' ( ) ! ?```　等の、使用に支障のない文字種のみが使われていることも、ちゃんと確認するのを、忘れないようにね。

あと、通話のできる電話番号を、[E.164](https://ja.wikipedia.org/wiki/E.164)フォーマットで、準備してねっ！
このフォーマットは、つまり、先頭に + のついた、```国番号``` 付きの電話番号ってことです！

## 電話をかけてみましょう！ ##

音声ファイル再生APIを使うときの、URLは `https://api.xoxzo.com/voice/simple/playbacks/`です。だから、CURLを使うと、音声通話を使う基本のコマンドは、こんな感じです。

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
--data-urlencode 'caller=thecallerphonenumber' \
--data-urlencode 'recipient=yourphonenumber' \
--data-urlencode 'recording_url=theURLofyourmp3file' \
https://api.xoxzo.com/voice/simple/playbacks/
```

レスポンスは、callid が返ってきまぁす。

`[{"callid":"YoUr-5ucc355fuL-c4lL-Uu1D"}]`

使い方は、これだけです！
でも、このAPIを使ってできることは、たっくさんあります。お客様へのご挨拶コール、プロモーションのご案内にはもちろん、ミーティングのリマインダーにも応用できちゃうんです。使うあなたの想像力次第で、可能性は無限ですね！

Xoxzoの [ドキュメンテーション](https://docs.xoxzo.com/ja/) で、XoxzoのAPIでできる、すごいこと、もっともっと、チェックしてみてくださいね！

[ミコちゃんのチュートリアル・シリーズ](https://blog.xoxzo.com/ja/tag/mikochiyan/)好評不定期連載中
