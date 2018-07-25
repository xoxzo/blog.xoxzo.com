Title: 緊急情報の通知への活用
Date: 2018-07-25 
Author: Akira Nonaka
Tags: telephony; sms; alert; notification
Slug: alert-notification
Lang: ja
Summary: XOXZO APIの緊急情報の通知への活用について解説します

XOXZOのテレフォニーAPIの活用法として考えられものに「緊急情報の通知」が考えられます。

+ 災害発生の危機がある
+ 事故や犯罪が発生した
+ 安否の確認をしたい
+ システムに障害が発生している

このような通知は、見逃されると重大な結果を招きます。
できるだけ、多くの手段を使って通知をする必要があるでしょう。

例えば、[XOXZO APIのPythonライブラリ](https://github.com/xoxzo/xoxzo.cloudpy)を使えば、
緊急SMS通知を、このように書くことができます。

```
   xc = XoxzoClient(sid="<your xoxzo sid>", auth_token="<your xoxzo auth_token>")
   result = xc.send_sms(
       message = "XOXZO緊急情報センターです。XXX付近で突発的な豪雨が発生する可能性があります。注意して下さい",
       recipient = "+818012345678",
       sender = "818011112222"
   )
```

電話やSMSを使った通知は、このような目的に、最適なメディアと考えられます。
また、このような機会は稀ですので月々の、固定費等が発生しないことも運用上の重大なポイントとなります。
XOXZOのAPIは完全に従量制なので、使わなければ全く費用は発生しません。