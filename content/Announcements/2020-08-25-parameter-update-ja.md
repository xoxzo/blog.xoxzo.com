Title: Kプレミアムサービスにおけるパラメーター変更のお知らせ
Date: 2020-08-25
Slug: x4-jpkp-parameter-update
Lang: ja
Tags: xoxzo; release; 2020; jp-kp; update; parameter;
Author: Aiko Yokoyama
Summary: 独自の送信元IDを設定する「Kプレミアムサービス」でご利用のパラメーター表記に変更があります。

APIからのSMS配信で重要な要素のひとつとなるのが、送信元ID。
受信者にとって、SMSメッセージが誰から届いたのかの確認を取る手がかりになります。

[XoxzoのKプレミアムサービス](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-service/)では、
事前登録いただいた番号を送信時にパラメーターで引用して配信することで、送信時に使われる送信元IDを固定することができます。

この度、送信に使うパラメーターが変更されましたので、通知させていただきます。

旧パラメーター： `jp_kddi_sender`

新パラメーター： `jp_kp_sender`

[ドキュメンテーション](https://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters)にてご確認いただけます通り、

[Kプレミアムサービス](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-service/)では `jp_kp` 

[Kプレミアム Lite](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/the-k-premium-lite/)では、`jp_kpl` 

の各パラメーターと併せて、ご登録の番号を指定する際にお使いください。

** 旧パラメーターは、９月末日までお使いいただけます。

ご不明な点がございましたら、いつでもヘルプデスク help@xoxzo.com までご連絡ください。

## ご要望はございませんか？

**継続改善** は、Xoxzoのサービスの鍵となっています。そして、改善内容の多くは、ユーザー様の声にお応えすることとしています。
ご利用時にご不便を感じたことがございましたら、いつでもお気軽に、ご連絡ください。チーム一同、お待ち申し上げております。
