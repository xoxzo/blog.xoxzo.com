Title: SMSの送信ステータスを確認しよう
Date: 2017-11-15 11:00
Author: Miko-chan
Tags: sms; api ユーザー; api; チュートリアル; ミコちゃん;
Slug: checking-your-sms-status
Thumbnail: images/xoxtan.png
Lang: ja
Summary: SMSを送信したら、その結果を知りたいよね？　ミコちゃんのチュートリアル、今回は送信ステータスの確認方法をご案内しま〜す！

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>
<div class="lg-padding-top50 md-padding0">

<a href="https://blog.xoxzo.com/ja/2017/10/31/sending-your-first-sms/">前回のチュートリアル</a>では、SMSを送信しましたよね。
CURL コマンドを実行した後に、msgid という文字列が返されたのに気が付きましたか？ こんな感じですよ〜。
 <code>[{"msgid":"tHi5i5y0urMsGIdt3xT"}]</code>
 これが返されていれば、SMSがちゃんと送られた、ってことです。そうでなければ、<a href="http://docs.xoxzo.com/ja/sms.html#response-data">別のメッセージ</a>が返されていたはず。
 でも、<b>送信</b>したメッセージが、ちゃんと<b>受信</b>されたかどうかって、どうやって確認するんでしょう？
</div>
<div style="clear:both;"></div>

## SMS送信をチェックするコマンド

SMSの_送信ステータスの確認_にも、送信に使ったみたいに、やっぱりCURLを使いま〜す。
違うのは、つけるパラメーターと、URLだけですよ！


SMSの送信ステータスを確認するには、これを実行してみてね！


```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/tHi5i5y0urMsGIdt3xT/
```

ちゃんと送信できていたら、JSONレスポンスが返されるはず。こんな感じ。

```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "DELIVERED",
    "sent_time":"2015-08-27 09:22:32",
    "cost": 10,
    "sender": "your_number",
    "recipient": "your_recipientnumber",
    "url": "https://api.xoxzo.com/sms/messages/tHi5i5y0urMsGIdt3xT/",
    "msgid": "tHi5i5y0urMsGIdt3xT"
}
```

もちろん、`cost`の部分は、送信したメッセージの数によるわね。
Xoxzoの[SMS送信料金](https://www.xoxzo.com/ja/about/pricing/sms)を見て、確認してね！

送信したメッセージのステータスは、`DELIVERED（配信成功）`ばかりじゃないわよ。
下のリストにまとめてみたから、参考にしてね。

<table class="table table-striped">
  <thead>
    <tr>
      <td> メッセージステータス </td>
      <td> 詳細 </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> QUEUED </td>
      <td> メッセージは配信待ち </td>
    </tr>
    <tr>
      <td> DELIVERED </td>
      <td> メッセージは配信成功 </td>
    </tr>
    <tr>
      <td> DELIVERING </td>
      <td> メッセージは配信中 </td>
    </tr>
    <tr>
      <td> FAIL </td>
      <td> メッセージは配信失敗 </td>
    </tr>
  </tbody>
</table>

## msgidを加えずに、確認したら?

こんな感じで実行しちゃうと、

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/
```

過去90日間にあなたが送ったSMSゼンブのステータスを表示しま〜す！


## スクリーンがいっぱいに！ 日付ごとのステータスって確認できる？

もっちろん！日付をパラメーターに含めたら、その日付のSMS送信ステータスを見れるわよ！
日付のフォーマットは、`year-month-day` つまり `西暦年-月-日` でお願いね。実行するには、こういう風になりま〜す。

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/?sent_date=2017-10-31
```

もし、その日付にSMS送信がなかったら、`200 OK レスポンス` が返されるけど、中身は空っぽのはずよ。


```
HTTP/1.0 200 OK
Content-Type: application/json

[]
```

送信ステータスの確認ができるのは、過去90日まで。それ以外の日付を設定しちゃうと、こういうレスポンスが返りま〜す。

```
HTTP/1.0 400 Bad Request
Content-Type: application/json

{
    "sent_date": [
        "Invalid sent_date"
    ]
}
```

パラメーターが間違っているときも、`400 Bad Request レスポンス`が返りますよ〜。

お疲れさま、今回のチュートリアルは、ここまで！
[XoxzoのSMS送信ドキュメンテーション](http://docs.xoxzo.com/ja/sms.html#check-sms-status-api)で、もっと詳しいところを確認してね！


ほかにも、Xoxzoでできる、すごいこと、たくさんあるから、[その他のドキュメンテーション](http://docs.xoxzo.com/ja/readme.html)も、読んでみてね。質問があったら、連絡してね。

ではまた次回！

[ミコちゃんのチュートリアル・シリーズ](https://blog.xoxzo.com/ja/tag/mikochiyan/)好評不定期連載中
