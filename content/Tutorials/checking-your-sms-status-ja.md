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
 これが返されていれば、SMSがちゃんと送信された、ってことです。そうでなければ、<a href="http://docs.xoxzo.com/ja/sms.html#response-data">別のメッセージ</a>が返されていたはず。
 でも、<b>送信</b>したメッセージが、ちゃんと<b>受信</b>されたかどうかって、どうやって確認するんでしょう？
</div>
<div style="clear:both;"></div>

## SMS送信をチェックするコマンド

SMSメッセージの_送信ステータスの確認_にも、送信に使ったみたいに、やっぱりCURLを使いま〜す。
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
Xoxzo APIサービスの[SMS送信料金](https://www.xoxzo.com/ja/about/pricing/sms)を見て、確認してね！

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

Mikoシリーズ：
- [最初のAPIユーザーを作ろう](https://blog.xoxzo.com/ja/2017/10/13/create-your-first-apiuser/)
- [はじめてのSMSを送ってみよう！](https://blog.xoxzo.com/ja/2017/10/31/sending-your-first-sms/)
- [SMSの送信ステータスを確認しよう](https://blog.xoxzo.com/ja/2017/11/15/checking-your-sms-status/)
- [音声案内を発信しましょう！](https://blog.xoxzo.com/ja/2021/11/08/making-a-simple-playback-call/)
- [テキスト読み上げ機能を使って、電話で認証してみましょう!](https://blog.xoxzo.com/ja/2021/11/01/making-a-voice-authentication-call-with-tts/)

他のXoxzo tutorials:
- [ダイアルインナンバーを使ってみよう](https://blog.xoxzo.com/ja/2017/07/01/dialinnumbers-tutorial/)
- [SMSを使った二要素認証のやり方](https://blog.xoxzo.com/ja/2021/11/22/introduction-2fa-sms/)
- [音声電話を使った二要素認証のやり方](https://blog.xoxzo.com/ja/2018/05/14/introduction-2fa-voice/)
- [かけるほうは通話料無料のフリーダイヤルは、0120だけじゃない！！](https://blog.xoxzo.com/ja/2021/10/28/freecall-numbers-introduction/)
- [「自分専用」のボイスメールを設定してみる](https://blog.xoxzo.com/ja/2020/10/23/setting-up-my-first-online-voicemail/)
- [Xoxzo APIのユーザーエクスペリエンス（第1回）](https://blog.xoxzo.com/ja/2018/06/27/user-experience-on-xoxzo-api-part-1/)
- [Xoxzo APIのユーザーエクスペリエンス（第2回）](https://blog.xoxzo.com/ja/2018/07/03/user-experience-on-xoxzo-api-part-2/)
- [SMS文面の字数制限について](https://blog.xoxzo.com/ja/2017/12/28/sms-limit/)



SMSメッセージを送信するためのさらに簡単なオプションをお探しですか？ PCから顧客にSMSメッセージを送信方法を探しですか？ そして、コーディングせずにすぐに送信始めたいですか？smsアプリの代わりにパソコンからショートメール送信プログラムの おすすめはXoxzoの他のサービス[EZSMS](https://www.ezsms.biz/)はどうでしょう？
利用した分のみのお支払いからsms の送信、受信 料金心配せず！、月額費用も初期費用もかかりません。
・プログラムをインストールしたりすることなく簡単にPCからSMSを送信できます。
・顧客ごとにカスタマイズされたメッセージを送信できます。
無料登録後、即時にご利用のウェブブラウザーから、SMS(ショートメール)の配信機能をご利用いただいたり、ダイヤル・イン・ナンバーをご利用いただくことができます。 - 170カ国以上への送信も対応しています。 
- 複数の宛先への一斉送信や、メッセージをカスタマイズして大量配信可能なCSVファイルを使った配信にも対応しています。 
- いつでも、どこでもSMS送信が可能です。 すべてオンラインで完結できます - ダイヤルSMSでビジネスもイベントも大成功に導きましょう！

{% include "tutorial-footer.html" %}
