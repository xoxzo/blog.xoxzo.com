Title: SMSマーケティングキャンペーンのROI(費用対効果)を測定する方法
Date: 2021-03-01 12:00
Author: Surya Banerjee
Tags: Tutorial; LinkTracking; 2021;
Slug: introduction-linktracking
Lang: ja
Summary: SMSマーケティングキャンペーンのROI(費用対効果)を測定する方法

## SMSマーケティングキャンペーンのROI(費用対効果)を測定する方法

世界中で毎日６０億のsmsメッセージが送信されていることを知っていますか？
現在、コミュニケーションツールが急増する中でも、テキストベースのマーケティングキャンペーンは２０２１年も人気です。

Mobile Marketerによると、SMSのエンゲージメント率が最も高いため、このダイレクトマーケティングチャネルにチューニングを合わせていく必要があります。
特に、SMSの開封率は98％と高く、わずか20％の電子メールの開封率を上回っています。 

SMS技術は長年に渡り軍を抜いてきましたが、欠点もあります。

よく耳にするのは、SMSマーケティングキャンペーンへ投資した際、そのパフォーマンスを追跡することができないことです。これは、実は完全に正解とはいえません。

SMSキャンペーンの効果を測定するための賢い方法がありますので、下記にご紹介します。

1.  **オンラインプレゼンスを持ち、そこにユーザーをリダイレクトする**<br />
見込み客がSMSメッセージを開いた場合、そのキャンペーンのコンテンツが乏しいと、顧客は積極的に食いついてこなくなるものです。
となると、ランディングページの出番です。驚くようなステキなサイトを作る必要はなく、シンプルなページにマーケティングの中身をできるだけ詳細に記載することをお勧めします。

SMSの本文には、URLを追加するだけです。SMSには文字制限があるため、ランディングページが、見込み客を引きつけるセールストークを行う機会となるのです。

2. **分析ツールを使用してランディングページへのトラフィックを測定する**<br />

SMSマーケティングキャンペーンのランディングページを設定したら、次のステップです。
ページを訪問しているユーザーの数を測定して識別するのには、Google Analyticsなどの、素敵で無料の分析ツールが役立ちます。SMSマーケティングキャンペーンのパフォーマンスを測定することができます。 

3. **URL短縮ツールの使用**<br />

SMSキャンペーンのパフォーマンスを把握するために、ランディングページや分析ツールを使用することはいい選択肢ですが、残念ながら、実際にランディングページにアクセスしているユーザーの数とトラフィックの量を完全に把握することはできません。
そこで、リンク短縮ツールが力を発揮します。こういったツールを使用すると、ページのURLを短くしてSMSの本文に占めるURLの文字数を制限したり、クリック数の分析ができます。
ただし、顧客がリンクをクリックしても、SMSマーケティングキャンペーンのターゲットリストの顧客を見分けることができないため、理想的な選択とは言えません。
かといって、手動で短縮リンクをいくつも作成して一つずつSMSのメッセージに挿入したりすれば、とんでもない時間がかかってしまいます。
（10,000人にマーケティングSMSを送信することを想像してみてください！）


4. **EZSMSとXoxzo SMS APIで リンクトラッキングを活用**<br />

Xoxzoでは、ユーザーからこの問題を聞いて、ソリューションを考えました。
そして、ウェブベースのSMS配信プラットフォーム・EZSMSとXoxzo APIで、送信したメッセージ内の[リンクを追跡](https://blog.xoxzo.com/ja/2020/10/15/link-tracking-release/)できるようになりました。
[SMS API](https://www.xoxzo.com/ja/about/sms-api/)は、各メッセージを個別に追跡できるようにする track_link というオプションパラメーターで、ランディングページのURLを指定するだけです。
システムが、各受信者のリンクを個別に作成しSMSを送信して、リンクをクリックしたかどうかを追跡します。

さらに、[lt_callbackurl](https://www.xoxzo.com/ja/about/voice-api/)と言う特別なパラメーターがあり、lt_callbackurlを使用すると、受信者がリンクをクリックした時に、指定したウェブフックにて、コールバックを受信するように設定できます。 
ユーザーが送信されたSMSメッセージを開いてリンクをクリックする度に、通知が届きます。

## [EZSMS](https://blog.xoxzo.com/ja/2021/01/28/ez-link-tracking-release/)でリンク追跡の使用 

ウェブベースのテレフォニープラットフォーム・EZSMSでは、[この機能](https://help.xoxzo.com/ja/ezsms-sms-delivery-service/articles/link-tracking-feature/)をどのように使用するかを見てみましょう。
ウェブベースのSMS機能を使用します。<br />

1. **EZSMSにログインし、『ウェブから送信』をクリックしましょう。**<br />
アカウントにサインインした後、右側のメニューの『SMS送信』から『ウェブから送信』をクリックしましょう。追跡したいURLを含むメッセージなどを、入力欄に入力します。

2. **[リンク追跡を有効にする]チェックボックスをクリックします。**<br />
送信するテキストを入力したら、『リンクトラッキングを有効にする』チェックボックスをクリックしましょう。

3. **メッセージを送る**<br />
『SMSを送信』ボタンをクリックしましょう。
受信者は、入力されたURLが [https://xoz.so/XYZ](https://xoz.so/XYZ) のような自動生成されたショートリンクに置き換えられた、SMSメッセージを受信します。
この機能をテストするために、受信したメッセージ内のリンクをクリックしてみましょう。 送信時に入力したメッセージにあった、元のURLにリダイレクトされます。

4. **リンクのステータスを確認しましょう。**<br />
まず、ご利用ログをダウンロードしてみましょう。トップバーのメニューをクリックして、ご利用ログページを見ましょう。
そこで、ご希望の送信日で日付範囲を選択し、ログをダウンロードしてください。送信したメッセージには、リンクトラッキングのステータスに0が表示されます。
<br />
これは、まだこのリンクがアクセスされていないことを意味します。機能をテストするために、受信したメッセージ内のリンクをクリックしてみましょう。
テキストメッセージに配置した元のURLにリダイレクトされます。それから、もう一回ご利用ログをダウンロードしてみてください。
リンクトラッキングのステータスが0から1に変更されていることをご確認いただけます。

## [Xoxzo SMS API](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/articles/what-is-link-tracking/)で リンクトラッキングを活用する

自分のサービスでこの機能を使用する場合、またはAPIを使用する場合は、これがXoxzoAPIでどのように機能するかを見てみましょう。手順を見ていきましょう。

1. **APIを使用してSMSメッセージを送信しましょう**<br />
[Xoxzo](http://www.xoxzo.com)に登録したらアカウントにログインして、新しいapiユーザーを作成すると、SIDとトークンにアクセスできるようになります。それができたら、curl コマンドラインツールを使用して下記のリクエストを作成します（でもまだ、Returnキーを押さないでください）<br />

 **_curl -u &lt;SID>:&lt;AUTH_TOKEN> --data-urlencode 'recipient=&lt;recipient>' --data-urlencode 'sender=&lt;sender>' --data-urlencode 'message=&lt;message>' https://api.xoxzo.com/sms/messages/_**
 
 2. **リンクトラッキングを有効にしましょう**<br />

curl コマンドの最後に**track_link=true**というパラメーターを追加しましょう。完成形の curlコマンドは次のようになります- <br />
 **_curl -u &lt;SID>:&lt;AUTH_TOKEN> --data-urlencode 'recipient=&lt;recipient>' --data-urlencode 'sender=&lt;sender>' --data-urlencode 'message=&lt;message>' --data-urlencode ‘track_link=true’ https://api.xoxzo.com/sms/messages/_**
 
 3. **StatusAPIで、SMSのステータスを確認しましょう**<br />

メッセージを送信すると、送信したSMSの識別子である **msgid** が返されます。
個々のメッセージのステータスを確認するには、次のようなcurlコマンドでステータスAPIを使用できます。- <br />

**_curl -u &lt;SID>:&lt;AUTH_TOKEN> https://api.xoxzo.com/sms/messages/&lt;msgid>/_**<br />

    _(このエンドポイントの最後尾の <msgid> を省略すると、複数のメッセージをチェックできます。_<br />
    **_curl -u &lt;SID>:&lt;AUTH_TOKEN> https://api.xoxzo.com/sms/messages/_**

このcurlのレスポンスにて、リンクトラッキングの詳細を次のように表示できます。- <br />

```
{
    "cost": 15.0,
    "link_tracking": {
        "accessed": true,
        "accessed_on": "2020-10-09 02:40:39",
        "link": "http://www.example.com",
        "shortlink": "https://xoz.so/dbNL4"
    },
    "msgid": "oxgyFO6tfwYkHLIMbURrz5smCv9QT423",
    "recipient": "+818012345678",
    "sender": "XOXZO",
    "sent_time": "2020-10-09 02:37:47",
    "status": "DELIVERED",
    "tags": [],
    "url": "https://api.xoxzo.com/sms/messages/oxgyFO6tfwYkHLIMbURrz5smCv9QT423/"
}
```

**リンクがクリックされたときに通知を受け取るためのコールバックURLを設定（オプション）：**<br />
メッセージ内のリンクがクリックされたら通知を受けられるように、コールバックURLを設定可能です。
実行するには、上記の curl に **「lt_callbackurl」** というパラメーターを追加して、リクエストを受信するカスタムエンドポイントを設定します。
テストするには、コールバックURLを作成する[「requestbin」](https://requestbin.com/)などの無料ツールを使用できます。<br />

**_curl -u &lt;SID>:&lt;AUTH_TOKEN> --data-urlencode 'recipient=&lt;recipient>' --data-urlencode 'sender=&lt;sender>' --data-urlencode 'message=&lt;message>' --data-urlencode ‘track_link=true’ --data-urlencode ‘lt_callbackurl=example.com/callback/’  https://api.xoxzo.com/sms/messages/_**

Xoxzo APIが、指定したエンドポイントに、リンクがクリックされた際の情報をすべて送信し、すぐに次のアクションを実行できるようになります。

この機能の詳細については、[APIドキュメント](https://docs.xoxzo.com/ja/sms.html#send-sms-messages-api)をご覧ください。 APIへのアクセスに問題がある場合は、遠慮なく[help@xoxzo.com](mailto:help@xoxzo.com)までご連絡ください。 皆様からのフィードバックをお待ちしております。
