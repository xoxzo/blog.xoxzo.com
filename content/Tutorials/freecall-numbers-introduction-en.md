Title: 0120 isn’t the only toll-free option for callers!
Date: 2017-11-02 12:00
Author: Aiko Yokoyama
Tags: APIuser; api; tutorial; mikochan; free-call; freephone; tall-free;
Slug: freecall-numbers-introduction
Thumbnail: ![free-dial-logo](/images/free-dial.png)
Lang: ja
Summary: 着信課金のフリーダイヤルは、0120で始まるものだけではありません。0800も全く同じ仕様でご利用いただけます。着信した電話を至便な番号へ転送したり、テキスト読み上げ機能を使って返答させたり、XoxzoのAPIなら、カスタマイズ可能で、着信利用データも取りやすくなっています。


## About toll-free calling

_Toll-free calling_ refers to a service where a person can call a designated phone number and any cost for calling are to be paid by the recipient of the call.  It is often used to contact customer service or place orders or complaints; even if you have to wait a little to be connected, you know they’re the ones covering the calling costs so it’s not as irritating; nowadays just about everyone knows about this service.

But no doubt people have a sense that **toll free = a number that starts with 0120.** There are in fact toll-free numbers that **start with 0800.**  There’s even a fairly long history behind this; 11-digit toll-free numbers starting with 0800 came into existence in July of 1999.  It may look like a cell phone number since it starts with 080, but note that the fourth digit is a 0 (zero) so you can tell the difference that way.

![free-dial-logo](/images/free-dial.png)

In the United States, the same service where the recipient bears the burden of costs is called **toll-free calling** (as opposed to “free dial” in Japan), and these numbers may start with 1-800, 1-888, 1-877 etc.  Be sure to keep in mind that the Japanese term “free dial” is an English term used only in Japanese.


## The crisis of 0120 toll-free numbers

The reality is that **0120 numbers are currently facing a crisis.**  Numbers starting with 0120 are only followed by 6 digits, meaning only 1 million (10 to the power of 6) 0120 numbers can be given out.  Given this depletion and the premium placed on 0120 numbers, 0800 numbers were introduced as a backup but they still have not received widespread acknowledgement.

Despite the lack of recognition, 0800 numbers function exactly the same as 0120 numbers and have potential for the future.  It’s relatively easy to obtain 0800 numbers that are easy for customers to remember, such as a play on words or round numbers, and since they are 7 digits long, there are 10 million possible numbers that can be used.  There is practically no concern of experiencing **a shortage** like 0120 numbers are currently facing.

現在、有名企業も含めて0800番号を採用している企業では、
**0800番号の表記の際、「発信料無料」であることを明記して** あります。
フリーダイヤルであるという認知度が低いため、番号と併記する必要があるのです。
0800の利用者が増え続ければ、時間の経過とともに、 **「フリーダイヤル=0800」** という認識も、
徐々に広まっていくこととおもわれます。
Companies currently using 0800 numbers, including some of the more well-known ones, when displaying their 0800 number, make it clear that they incur **no costs to the caller.**  Since not many people know that these are toll-free numbers, it is necessary to state this together with the phone number.   As more people start using 0800 numbers, the awareness that “0800 = toll-free calling” will no doubt gradually become more widespread.


## フリーダイヤル取得後の活用法

お客様に対し「いつでもお気軽にお問い合わせください」というオープンな態度を表すことができる、
フリーダイヤルですが、 **0120番号、0800番号を取得したら、** _どのように使いますか？_

- カスタマーサポート窓口⇒コールセンターへ接続

- イベントに関する問い合わせ⇒資料を送付

- 電話アンケート⇒アンケートの回答を取得

- 本人確認⇒発信者の情報取得

- 着信利用状況の確認⇒利用状況明細データ取得

**着信した電話に対するアクションを、「自分仕様」にカスタマイズできたらいいな** という時には
_**[Xoxzo VOICE API](https://www.xoxzo.com/ja/about/voice-api/)**_ をご利用ください。


- __テキスト読み上げ（TTS）機能を活用し、着信した電話に返答する__
    - 「はい。株式会社Xoxzoです。APIに関するお問い合わせは、１を…」（そして下記 _3.別の電話番号へ転送_で担当者の電話へとつなぐ）
    - 「お電話ありがとうございます。Xoxzo歯科医院です。ご予約お取り消しには３を押してください…」
    - 「Xoxzoキャンペーン事務局です。発信されたお電話へ、特別割引価格でお買い物をお楽しみいただけるウェブサイトのURLをお送りいたします…」（その後 _4.「伝えたい情報量が多いときには」で、SMSにて情報を送信）

- __準備しておいたMP3ファイルを再生して、発信者のほしい情報を音声でご案内__
    - 「次回のXoxzo API 説明会は、◯月◯日◯曜日　◯時より、Xoxzo会館第一会議室にて行います…」
    - 「本日のXoxzo球場での試合、SMS対VOICE の結果は、５対５で引き分けました。次回は◯月◯日…」

- __別の電話番号へ転送__
    - 休日にオフィスへかかる電話を、自分の携帯電話に転送設定すれば、大切な電話を逃すこともありません
    - 複数の電話番号を、ひとつの電話で受信したい場合も、XoxzoのAPIを使えば、簡単転送

- __伝えたい情報量が多いときには、_「クリック（タップ）すればアクセスできる、ご案内ウェブサイトへのURL」_を、電話をかけてきた相手にSMS送信する__

 _などなど、ユーザー様の想像力と創造力の限り、いろいろ_

なんてことも、できてしまいます。

その他、**[XoxzoのAPI](https://www.xoxzo.com/ja/)**は _**[SMS配信](https://www.xoxzo.com/ja/about/sms-api/)**_ や _**[発信電話](https://www.xoxzo.com/ja/about/voice-api/)**_ _複数で**電話会議**ができる_ _**[カンファレンスコール](http://docs.xoxzo.com/ja/voice.html#simple-conference-api)**_ の機能も充実しています。

_Xoxzo機能のデモのご希望にも、関東圏を中心に、お応えします。_

ご不明な点があれば、是非 help@xoxzo.com までご連絡ください。

