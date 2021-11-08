Title: 音声案内を発信しましょう！
Date: 2021-11-08 08:00
Author: Miko-chan
Tags: 音声; 通話; recording; api; チュートリアル; ミコちゃん;
Slug: making-a-simple-playback-call
Thumbnail: images/xoxtan.png
Lang: ja
Summary: 音声APIの、はじめての冒険へ出発！

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>

こんにちワ〜！
もう、 [SMS送信]({filename}./sending-your-first-sms-ja.md) 、もできちゃったし [そのステータス確認]({filename}./checking-your-sms-status-ja.md) もできちゃった、というあなたは、今度はXoxzoの [音声API](https://www.xoxzo.com/ja/about/voice-api/) (音声電話API)の冒険にでかける時ですよぉ〜！

今回は、シンプルな音声通話：録音済み音声ファイルの再生の使い方から初めちゃうね。この音声ファイル再生APIを使うと、留守電のように、こちらから電話をかけて、相手が出たら準備しておいたmp3ファイルを再生することができるのよ。そうしたら、留守電アプリが必要はない！まずは、自分の電話にかけて、テストしてみてね！

<div style="clear:both;"></div>

## 必要なものは？ ##

始める前に、mp3 音声ファイルを準備して、オンラインに保存してください。リンクを使うので、メモしておいてね！このリンク、webサービス apiが使うから、誰でもアクセス出来るようにしておいてね。あと、このURLに、通常の半角アルファベットや```- _ $ . * ' ( ) ! ?```　等の、使用に支障のない文字種のみが使われていることも、ちゃんと確認するのを、忘れないようにね。

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

XoxzoのウェブAPIの [ドキュメンテーション](https://docs.xoxzo.com/ja/) で、XoxzoのAPIでできる、すごいこと、もっともっと、チェックしてみてくださいね！
[EZSMS](https://www.ezsms.biz/)というsms配信サービス（sms送信サービス）で簡単にsms 一括送信・sms pcから送信ことができます。是非みてくださいね！

[ミコちゃんのチュートリアル・シリーズ](https://blog.xoxzo.com/ja/tag/mikochiyan/)好評不定期連載中
