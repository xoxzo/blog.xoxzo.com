Title: 予約の確認を送る
Date: 2018-06-26
Author: Akira Nonaka
Tags: sms;api;リマインダー;チュートリアル
Slug: appointment-reminder
Lang: ja
Summary: 予約を忘れられないように、リマインダーを送りましょう

XOXZOのお客様の中には、レストランや宿泊施設の予約サービスのためのWebサイトを
運営されている方がいらっしゃいます。
それらの方が抱える悩みのひとつが「お待ちしていたお客さまが、予約したことを忘れて来なかった」
というものです。
これは、サービスを提供する側にとっても、お客様にとっても不幸なことです。

これを防止するのに効果的なのが、前日にお知らせ(リマインド)のSMSを送ることです。
もちろん電子メールで送っても良いのですが、迷惑メールと判断され、読んでもらえない可能性も大です。
SMSは大変目立ち、開封率も高いので、このような大切な連絡に最適です。

例えば、[XOXZO APIのPythonライブラリ](https://github.com/xoxzo/xoxzo.cloudpy)を使えば
こんな風に書くことができます。

```
   xc = XoxzoClient(sid="<your xoxzo sid>", auth_token="<your xoxzo auth_token>")
   result = xc.send_sms(
       message = "レストランXOXZOです。本日19時、２名様でご予約があります。ご来店お待ちしております。",
       recipient = "+818012345678",
       sender = "818011112222"
   )
```


