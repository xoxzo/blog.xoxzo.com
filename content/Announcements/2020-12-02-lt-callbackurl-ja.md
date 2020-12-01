Title: リンクトラッキングが追加パラメータにより、便利になりました
Date: 2020-12-02
Slug: lt-callbackurl-release
Lang: ja
Tags: xoxzo; 新規リリース; 2020; リンクトラッキング;
Thumbnail: images/link-tracking.png
Author: Aiko Yokoyama
Summary: 顧客行動分析や顧客リストの清浄化に役立つ、SMS配信時のリンクトラッキング機能。クリック即時に通知を受ける callback URL指定のパラメータが加わりました。

平素は、[Xoxzo API](https://www.xoxzo.com/ja/)をご利用いただき、ありがとうございます。

SMS配信時にご利用いただける、リンクトラッキング機能に、追加パラメータ _lt_callbackurl_ がリリースとなりましたので、お知らせいたします。


参照記事：[リンクトラッキング機能リリース](https://blog.xoxzo.com/ja/2020/10/15/link-tracking-release/)


### 使い方
使い方は、とっても簡単。リンクトラッキングの送信時に、追加のパラメータ _lt_callbackurl_ でコールバックを受けるURLを指定するだけです。
詳しくは、[ヘルプセンター](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/what-is-link-tracking/)をご参照ください。

### 仕組み
**リンクトラッキング送信**
- _track_link_ パラメータ付きのリクエストを受け取ると、本文中に最初に出てくるURLまたはドメイン名が、独自の短縮URLへ置き換えられます。<br>
- メッセージの受信者がURLをクリックすると、クリックした履歴がクリックした日時とともに記録されます。<br>
**リンクトラッキング通知用 URLを指定した送信**
- リンクトラッキング送信時に、クリック通知のコールバックを受けるURLを指定するパラメータ _lt_callbackurl_ を付けてください。<br>
- XOXZOクラウドシステムがこのURLをPOSTメソッドで呼び出します。<br>

クリックの記録は、[SMSの配信状態を確認するAPI](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api)にて確認することができます。

### 料金
リンクトラッキング機能のご利用には、追加料金がSMS通常配信に上乗せされます。
[SMS配信料金ページ](https://www.xoxzo.com/ja/about/pricing/#send-sms)をご参照ください。

リンクトラッキング機能は、ユーザー様の声から生まれました。<br>
その他、追加機能などのご希望がございましたら、[ヘルプデスク](mailto:help@xoxzo.com)までご連絡ください。
