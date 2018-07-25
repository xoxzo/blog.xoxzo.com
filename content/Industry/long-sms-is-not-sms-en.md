Title: long-bodytext SMS = E-mail 
Date: 2018-07-26 17:00 
Slug: long-sms-is-not-sms 
Lang: en 
Tags: 2018; sms; long-message; SMS; email; 
Author: Iqbal Abdullah 
Summary: Why do we send the messages longer than SMS standard still as SMS?


"Corporation XXX provides long-bodytext SMS service up to 700 letters, how about you?"
Recently we often receive this kind of inquiries.
Taking this chance, I want to deep dive into **Why we send _LONG_ messages using _Short_ message service**.

To begin with, SMS (_Short Messaging Services_) can send only up to 160 ASCII (70 non-ASCII) letters no matter who is your recipient.
Some services provide function to allow you sending longer than that standard as one message, 
_One Message Up to 160 ASCII (70 non-ASCII)_ is a golden rule.

Using Xoxzo's SMS-APIs, long messages can be sent (delivers divided multiple message) like one message.

I wonder whether we should do or not, when it is technically possible.

I would say **No**.

開封率が高いと言えども
前回のブログ投稿「ビジネス・コミュニケーションにSMSを取り入れる理由」 にも
掲載をしていますが、電子メールに比べ、SMSの開封率は高いです。着信３秒後、ほとんどの人はメッセージを開封して読みます。

開封率が高いと聞いて、伸び悩みの電子メールからSMSへのマーケテイングに力を入れて切り替えよう、というビジネスは少なくありません。

しかし、SMSはその規格によって英数字以外の文字で送ると、最大1つのSMSに70文字しか入りません。この規格は、どこの国でも、どのサービス でも代わりはありません。お使いになっているベンダーの送信画面で70文字以上のメッセージを送信できるとなっても、メッセージ は必ず分割されて、その分の通数が課金されます。 分割されてしまったメッセージは、受信側の機種によって送った順に届く保証もありません。

SMSは、短い文字数で、伝えたいメッセージを伝えて直感的に何かのアクションを起こさせる有効なツールです。 メールのように、たくさんの文字が届いて、下手したら複数のバラバラのSMSで届いてしまうとむしろ カスタマー・エクスペリエンス (UX) が低下すると同時に、二度とその配信者からのメッセージを読みたくなくなる恐れがあります。

価格は800倍の差
相場としてそこそこ実績がある程度のところならはメールは１通あたり 0.025円 というぐらいのコストに対して、SMSは 1通あたり10円から20円になります。

単純に200文字のメールマガをSMSで送るとしてしまうと、1通が0.025円から30円になります。1000人のお客様に送るとしたら メールで送ると25円のところ3万円になります。

開封率が高いからと言って、 メールで伝えようとしていたことを、そのままSMSに送ろうということは、ないです。

パーソナライズできるからこそ、開封率が高いSMSなので、メールマーケテイング感覚でSMSを送ると、お客様は離れていく。 もちろんエンドユーザのお客様によりますが、月に４通程度のマーケテイングSMSはすでに多すぎると言われています。

で、どうすればいいでしょうか。
繰り返しになりますが、 SMSは、短い文字数で、伝えたいメッセージを伝えて直感的にアクションを起こさせるツールです。 この「アクション」というのは、一般的にあるリンクをクリックすることか、ある電話番号に電話をかけてもらうことです。

誰が読んでも何かしら欲しがる情報が載っているだろう、というメールの大量配信と違って、 読む側に短い文書で直感的にアクションを起こしてもらうなら、読む側は何がほしいななのか、知ることが一番大事です。 当たり前のようなことですが、実際にとても難しいことで、細かく顧客管理システム (CRM) などを運用していなければ、なかなかできないことです。

まとめ
ショートメッセージは、その名のとおり、短文を送るサービスです。

どうしてもたくさんのお得の情報を伝えたいなら、スマホ対応サイトに情報を載せ、SMSの中に誘導するリンクを埋め込めましょう。 リンクを載せることさえ70文字の制限にも入ることを忘れなく、URL短縮サービスなどを使って簡潔な文章を作りましょう。

誘導リンクを使うとことで、簡潔に短いSMSを送ることができる他、リンク解析ツールなどを使うと、 SMSの配信効果（開封率など）も分析することが可能になります。

SMSとメールは、どちらか一方がより優れている連絡手段ではなく、それぞれのメリットとデメリットがあることから、 それを理解することと、使い分けることがとても重要です。
