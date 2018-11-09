Title: メッセージや通話の受信者番号入力時のルール
Date: 2018-11-08 
Author: Miko-chan
Tags: ezsms; sms; xoxzo; international_call; phone_number;
Slug: recipient-number-rule
Lang: ja
Thumbnail: images/xoxtan.png
Summary: XoxzoやEZSMSの利用時、受信者の電話番号の入力には、ルールがあるんです。

こんにちは！お久しぶりです。ミコです!

![miko-chan](/images/xoxtan.png)

Xoxzoがご提供しているのは、</br>
- APIを使って自分のアプリやシステムからSMSを送ったり、電話をかけたり受けたりできるようにできちゃう [Xoxzo-クラウド・テレフォニー・プラットフォーム](https://www.xoxzo.com/ja/) </br>
- ウェブブラウザーを使って、サイトからSMSを送信できちゃう [EZSMS](https://www.ezsms.biz/ja/) </br>
なんですが、今、XoxzoでもEZSMSでも、新規のご利用者がとっても増えていますぅ。

でも、そもそも、SMSの送り先の電話番号の入力でつまづいてしまう方が、たくさんいらっしゃるんです！

…ということで。

今日はちょっと、初歩に戻って、「受信者の電話番号」の入力方法をご案内しちゃおっかな？って思ってます！

簡単に言うと「受信者の電話番号」の入力には、[E.164](https://ja.wikipedia.org/wiki/E.164)のフォーマットを使ってくださいねっ！
…って言うことなんですが、[E.164](https://ja.wikipedia.org/wiki/E.164)ってなんだろう、と思う方のために、ミコの特別レッスンです！

普段、日本国内で暮らしていると、ケータイへ電話をかけたりSMSを送信したりする時、`090` `080` `070` っていうような番号から始まる
電話番号を使いますよね？

でも、Xoxzoの提供しているサービスは、全世界が対象だから、たとえ日本国内から日本国内へ送信・発信するときでも、
相手は「世界の中の」日本の電話番号なんだ、っていうことを、忘れないでくださいねっ。

ということで、受信者の番号の入力は、</br>
**1.  `+` (プラス)から始めてね。**</br>
**2. そして「日本の番号だよっ」っていうために国番号 `81`を続けてくださいっ！** </br>
**3. その後、いよいよ電話番号なんだけど、最初の `0` は、はずしちゃってくれますか？ **</br>

例えば、`090-1234-5678`っていう番号へSMS送信や電話発信をしたい場合、`+819012345678` を入力するってことなんです！

難しかったり、海外への送信にはどうするか、がわからなかったら、<a href="mailto:help@xoxzo.com?subject=Xoxzoのブログより、質問です&body=お名前：">ヘルプデスクへ質問</a>を送ってね！

このルールは、[XoxzoのAPIドキュメンテーション](https://docs.xoxzo.com/ja/sms.html#send-sms-messages-api)とか、
[EZSMSの送信ページ](https://www.ezsms.biz/ja/member/sendsms/)でも、参照できるから、便利に使ってねっ！

ではまた次回。

ミコちゃんのチュートリアルで、お勉強しちゃう？
[こちら](https://blog.xoxzo.com/ja/tag/mikochiyan/)から、どうぞ。
