Title: 【Xoxzo】ログのウェブダウンロード リリース！！
Date: 2019-7-4
Slug: 201907-logdownload-release
Lang: ja
Tags: xoxzo; new release; 2019; logs;
Thumbnail: images/xoxzo-logo-linkedin.png
Author: Aiko Yokoyama
Summary: 多くのリクエストを受けまして、ウェブダウンロード機能がご利用可能となりました！

Xoxzoの APIでは、 [SMSの配信](https://www.xoxzo.com/ja/about/sms-api/)や
[音声通話](https://www.xoxzo.com/ja/about/voice-api/)、そして
[ダイヤルインナンバーを使った音声通話受信](https://www.xoxzo.com/ja/about/dial-in-api/)などをご利用いただけます。

ユーザーの方々は、SMSや通話の配信・受信後に、もちろんログの確認を行うものですので、 
Xoxzoでも [**SMSのステータス確認API**](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api) であるとか、
[**通話発信ステータス確認API**](https://docs.xoxzo.com/ja/voice.html#checking-call-status) などをご用意しております。

今回のリリースでは、**SMSの配信状況ステータス確認が、csv形式ファイルでウェブよりダウンロードできる**ようになり、
大変簡単で便利になりましたので、お知らせいたします。

どのくらい簡単で便利になったのでしょうか。

1. [アカウントへログインする](https://www.xoxzo.com/ja/accounts/login/)
1. 画面右上の _アカウント_ プルダウンより _ご利用ログをダウンロードする_ を選ぶ
1. ご希望の期間を選んで _作成する_ をクリック

以上で、csvファイルのダウンロード準備が出来ます。ファイル内の項目は、

- sender
- url
- msgid
- tags
- sent_time
- recipient
- status
- cost
- apiuser
です。

**XoxzoのAPIご利用ログの保管期限は、90日間です。**

ご質問は、help@xoxzo.com までお寄せください。

_このウェブダウンロード機能は、弊社運営のウェブベースSMS配信サービスであり、Xoxzo APIプラットフォームの前進である [EZSMS](https://www.ezsms.biz/en/)にて、長年ご愛用いただいておりました。この度、多くのユーザー様からの熱いご要望を受け、それにお応えする形で Xoxzoでもご利用いただけるよう復刻できましたことを、大変嬉しく思っています。_
