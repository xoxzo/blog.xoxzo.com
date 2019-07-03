Title: 【Xoxzo】ログのウェブダウンロード リリース！！
Date: 2019-7-4
Slug: 201907-logdownload-release
Lang: ja
Tags: xoxzo; new release; 2019; logs;
Thumbnail: images/xoxzo-square-logo.png
Author: Aiko Yokoyama
Summary: 多くのリクエストを受けまして、ウェブダウンロード機能がご利用可能となりました！

Xoxzoの APIでは、 [SMSの配信](https://www.xoxzo.com/ja/about/sms-api/)や
[音声通話](https://www.xoxzo.com/ja/about/voice-api/)、そして
[ダイヤルインナンバーを使った音声通話受信](https://www.xoxzo.com/en/about/dial-in-api/)などをご利用いただけます。

ユーザーの方々は、SMSや通話の配信・受信後に、もちろんログの確認を行うものですので、 
Xoxzoでも [**SMSのステータス確認API**](https://docs.xoxzo.com/en/sms.html#check-sms-status-api) であるとか、
[**通話発信ステータス確認API**](https://docs.xoxzo.com/en/voice.html#checking-call-status) などをご用意しております。

今回のリリースでは、このステータス確認が、csv形式ファイルでウェブよりダウンロードできるようになり、
大変簡単で便利になりましたので、お知らせいたします。

どのくらい簡単で便利になったのでしょうか。

1. [Log in to your account](https://www.xoxzo.com/en/accounts/login/)
1. Find _Download Usage Logs_ from the top-right pulldown labeled _Account_
1. Select desired dates and the type of log you need before clicking `GENERATE` button

Your .csv file will be ready for download in a while.

* Please note that we store your logs for only 90 days.

Would you have any questions, please contact help@xoxzo.com

_this web-download feature has been valued as a handy-function at [EZSMS](https://www.ezsms.biz/en/), our web-based SMS sending service and former platform of Xoxzo. We are glad to have received such many hot-demand of reproduction and to be available to respond to the requests._
