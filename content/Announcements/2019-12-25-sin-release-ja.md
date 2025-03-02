Title: 【Xoxzo】SMS受信API リリースのお知らせ
Date: 2019-12-25
Slug: x4-sin-release
Lang: ja
Tags: x4; new release; 2019;
Thumbnail: images/sin.png
Author: Aiko Yokoyama
Summary: ご要望を受け、ついにXoxzoにSMS受信APIが登場しました。

![SIN](/images/sin.png)

平素は、[Xoxzo-クラウドテレフォニープラットフォーム](https://www.xoxzo.com/ja/)をご利用いただき、誠に有難うございます。

2019年12月20日、**SMS受信API**がリリースとなりました。

## SMS受信APIとは？
SMS受信APIでは、APIを使って電話番号を契約することにより、
SMS受信のための携帯電話・スマホ・その他のデバイスがなくてもインターネット上でSMSの受信が可能になります。

## SMS受信APIを使うメリットは？
+ SMSの送信者の電話番号を自動でリストに追加したい
+ SMSの送信者に自動で決まった返信を送信できるようにしたい
+ 複数の電話番号に届くSMSを一括して管理したい
+ 届いたSMSの内容に応じて、受信したメッセージを自動で振り分けたい

など、SMS受信APIを使ってできることは、無限大です。

## SMS受信APIの使い方は？
[ドキュメンテーション](https://docs.xoxzo.com/ja/sms.html#receive-sms-messages-api)
および[ヘルプページ](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/what-is-sin/)をご参照ください。

概要としては、

1. 受信用の番号を契約する

2. 契約した番号へWebhookを関連付ける

これで、受信の準備は完了です。

SMSを受信すると、Webhookへメッセージの送信者、受信した契約中の番号、メッセージの内容と受信時刻が送られます。

着信したSMSに対する使い方は、ユーザー様のアイディア次第です。
ご活用ください。


## SMS受信APIの料金は？

SMS受信APIのご利用には、

1. 初期導入料金（初回のみ・一律）

2. 番号のご利用契約料金（30日ごと）

3. メッセージの受信料金（SMS受信ごと）

が必要です。

詳しくは、[料金ページ](https://www.xoxzo.com/ja/about/pricing/sms)にてご確認ください。

ご不明な点がございましたら、ヘルプデスク (help@xoxzo.com)までご連絡ください。


