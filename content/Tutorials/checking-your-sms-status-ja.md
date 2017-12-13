Title: SMSの送信ステータスを確認しよう
Date: 2017-11-15 11:00
Author: Miko-chan
Tags: sms; api ユーザー; api; チュートリアル; みこちゃん;
Slug: checking-your-sms-status
Thumbnail: images/xoxtan.png
Lang: ja
Summary: SMSを送信したら、その結果を知りたいよね？　ミコちゃんのチュートリアル、今回は送信ステータスの確認方法をご案内しま〜す！

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>
<div class="lg-padding-top50 md-padding0">

[前回のチュートリアル](https://blog.xoxzo.com/ja/2017/10/31/sending-your-first-sms/)では、SMSを送信しちゃいました。
CURL コマンドを実行した後に、msgid という文字列が返されたのに気が付きましたか？ こんな感じですよ〜。
 <code>[{"msgid":"tHi5i5y0urMsGIdt3xT"}]</code>
 これが返されていれば、SMSがちゃんと送られた、ってことです。そうでなければ、[別のメッセージ](http://docs.xoxzo.com/ja/sms.html#response-data)が返されていたはず。
 でも、送信したメッセージが、ちゃんと受信されたかどうかって、どうやって確認するんでしょうね？
</div>
<div style="clear:both;"></div>

## SMS送信をチェックするコマンド

SMSの送信ステータスの確認にも、送信に使ったみたいに、やっぱりCURLを使いま〜す。
違うのは、つけるパラメーターと、URLだけですよ！


SMSの送信ステータスTo check on the status of your SMS, run this:


```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/tHi5i5y0urMsGIdt3xT/
```

If everything is OK, you should be getting a JSON response like so:

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

Of course, the cost will depend on which number you are sending too. You can get the pricing details here: [SMS Pricing](https://www.xoxzo.com/en/about/pricing/#sms)

The SMS statuses are in this list:
<table class="table table-striped">
  <thead>
    <tr>
      <td> Status </td>
      <td> Details </td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> QUEUED </td>
      <td> Message put into queue and will be delivered shortly </td>
    </tr>
    <tr>
      <td> DELIVERED </td>
      <td> Message successfully delivered </td>
    </tr>
    <tr>
      <td> DELIVERING </td>
      <td> Sending message in progress </td>
    </tr>
    <tr>
      <td> FAIL </td>
      <td> Failed to send message </td>
    </tr>
  </tbody>
</table>

## What if I didn't put in my msgid?

Sending something like this:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/
```

Would give you the status of all the SMS that you sent within 90 days.

## There's a lot of stuff on my screen! Can I get statuses by date?

Sure! You can include a date parameter to get your SMS statuses on the day (date format is year-month-day), something like this:

```
curl -u th3ApISiDt3xtTh4tyoUcoPied:Th3aUthT0k3nth4tY0uCopi3D \
https://api.xoxzo.com/sms/messages/?sent_date=2017-10-31
```

If you didn't send an SMS during that period, it will still return a 200 OK response, but it'll be empty:

```
HTTP/1.0 200 OK
Content-Type: application/json

[]
```

You only can get statuses within 90 days of the current date. Otherwise, you will get this response:

```
HTTP/1.0 400 Bad Request
Content-Type: application/json

{
    "sent_date": [
        "Invalid sent_date"
    ]
}
```

You'll also get a 400 Bad Request response if your parameters are incorrect.

And that's it! There are more details in our [SMS documentation](http://docs.xoxzo.com/en/sms.html#check-sms-status-api) which you can check out as well!

Check out our [docs](https://docs.xoxzo.com/en/) to see what cool things you can do with our API. 

Until next time!
