Title: 【Xoxzo】callbackurl パラメーターのリリース
Date: 2017/10/17
Author: Aiko Yokoyama
Tags: dlr; tutorial;
Slug: dlr-parameter-tutorial
Lang: ja
Summary: 行ったアクションに対するステータス確認に使えるパラメーター「callbackurl」がリリースされました。こちらでは、サンプルコードと併せて、ご案内します。
Series: Xoxzo API Tutorial
Series_index: 3

いつも、[Xoxzoークラウドテレフォニープラットフォーム](https://www.xoxzo.com/ja/)をご利用いただき、誠に有難うございます。

この度Xoxzoでは、[SMS配信](http://docs.xoxzo.com/ja/sms.html)と[音声通話VOICE](http://docs.xoxzo.com/ja/voice.html)の両方で、アクションに対するステータス確認にお使いいただける、パラメーター「callbackurl」をリリースいたしました。

このパラメータ（省略可能）をお使いいただくと、ご希望のURLにてhttpのPOSTメソッドを使い、コールバックを行い、
* SMS配信時には、キャリアからのステータス
* Voiceの利用時には、通話終了時に、通話のステータス
各アクションのステータスをお知らせします。

ご利用には、下記のサンプルコードをお試しください。

#SMS送信確認
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
#VOICE通話結果確認
```javascript
#!/bin/sh
# You should get SID and AUTH_TOKEN from XOXZO console
curl -v -u $SID:$AUTH_TOKEN \
     --data-urlencode 'caller=+818011112222' \
     --data-urlencode 'recipient=+818033334444' \
     --data-urlencode 'tts_message=おはよう' \
     --data-urlencode 'tts_lang=ja' \
     --data-urlencode 'callbackurl=http://example.com/receive_dlr/' \
     https://api.xoxzo.com/voice/simple/playback/
```

ご不明な点は、下記URLよりAPIドキュメンテーションをご参照ください。

[SMS配信用callbackurl パラメータについて](http://docs.xoxzo.com/ja/sms.html)
[VOICE音声通話用callbackurlパラメータについて](http://docs.xoxzo.com/ja/voice.html)

---
**📚 チュートリアルシリーズ**

<div class="tutorial-footer">
  <p><a href="/prev-url">← PREV_TITLE</a> · <a href="/tutorial-index-ja.html">目次へ戻る</a> · <a href="/next-url">NEXT_TITLE →</a></p>
  <p><strong>おすすめ:</strong> <a href="/send-your-first-sms">最初のSMS送信</a> ｜ <a href="/try-voice-api">音声APIを試す</a></p>
</div>

