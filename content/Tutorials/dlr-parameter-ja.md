
Title: 【Xoxzo】callbackurl パラメーターのリリース
Date: 2017/10/17
Author: Aiko Yokoyama
Tags: din; did; tutorial;
Slug: dlr-parameter-tutorial
Lang: ja
Summary: 行ったアクションに対するステータス確認に使えるパラメーター「callbackurl」がリリースされました。こちらでは、サンプルコードと併せて、ご案内します。

いつも、Xoxzoークラウドテレフォニープラットフォームをご利用いただき、誠に有難うございます。

この度Xoxzoでは、SMS配信と音声通話VOICEの両方で、アクションに対するステータス確認にお使いいただける、パラメーター「callbackurl」をリリースいたしました。

このパラメータ（省略可能）をお使いいただくと、ご希望のURLにてhttpのPOSTメソッドを使い、コールバックを行い、
* SMS配信時には、キャリアからのステータス
* Voiceの利用時には、通話終了時に、通話のステータス
各アクションのステータスをお知らせします。

ご利用には、下記のサンプルコードをお試しください。
```javascript
#!/bin/sh
# You should get SID and AUTH_TOKEN from XOXZO console
curl -u $SID:$AUTH_TOKEN \
     --data-urlencode 'sender=+818011112222' \
     --data-urlencode 'recipient=+818033334444' \
     --data-urlencode 'message=おはよう' \
     --data-urlencode 'callbackurl=http://example.com/receive_dlr/' \
     https://api.xoxzo.com/sms/messages/
```

ご不明な点は、下記URLよりAPIドキュメンテーションをご参照ください。

[SMS配信用callbackurl パラメータについて](http://docs.xoxzo.com/ja/sms.html)
[VOICE音声通話用callbackurlパラメータについて](http://docs.xoxzo.com/ja/voice.html)
