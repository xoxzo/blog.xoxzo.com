Title: 【Xoxzo】SMS送信文字数増量!!
Date: 2025-06-03
Slug: long-sms
Lang: ja
Tags: 長文SMS; 660文字; 2025;
Thumbnail: /images/longsms-ja.png
Author: Aiko Yokoyama
Summary: SMS1通の文字数はGSMの仕様により、1通あたり日本語70文字と決まっています。とはいえ、携帯電話番号がわかれば送信できる上、郵送DMに比較して単価の低いSMSで、伝えたいことは無限大。XoxzoのSMSAPIが、660文字に対応します。

![jpkp-price](/images/longsms-ja-1.png)

平素は、[Xoxzo−クラウドテレフォニープラットフォーム](https://www.xoxzo.com/ja/)のご利用ありがとうございます。<br>
XoxzoのSMS送信APIが、660文字の長文に対応しました。<br>
<br>
ユーザーの皆様は、SMS送信や音声通話APIは、どのような用途でご利用でしょうか。
<br>
主なSMSの用途として、大きく３つに分けられますが、<br>
* 認証<br>
* 緊急通知<br>
* マーケティング<br>
<br>
認証用SMSは、簡潔に、<br>
```Xoxzoです。認証コードは、３０３０です。```<br>
で十分ですね。<br>
<br>
緊急通知の場合も、要点だけ、<br>
```警戒レベル3『高齢者等避難』です。施設内高齢者の避難を開始してください。```<br>
などが、シンプルで伝わりやすいです。<br>
<br>
とはいえ、認証に使う、オンラインサービスのページを案内したり、避難場所をオンラインマップのURLで送信して誘導したりすることも、ありますよね。<br>
SMSメッセージは、携帯電話番号がわかれば送信できて即時性もある上、スマホユーザーの増加につれ、SMSからブラウザへの誘導がスムーズであることも、利用時の利点になっています。<br>
ただ、リンクは文字列が長い場合もあり、短縮URLツールを使っても、それなりの文字数を使いますので、１通の文字数が７０文字に限られた中で、文面の作成に苦労することも多いのが実情です。<br>
<br>
マーケティングメッセージを送信する場合は、なおさら。広告内容に加え、オプトアウトの方法や、ひとことご挨拶…を入れることはほぼ不可能ですよね。<br>
<br>
そこで、XoxzoのSMSAPIが、660文字に対応します。<br>
郵送DMに比較して単価の低いSMSで、詳細な情報も余さず届けられます。<br>
<br>
長文対応となった、XoxzoのSMS APIで扱う文字数については、[ヘルプページ](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/sms-api/articles/how-many-characters-would-fit-within-1-x-sms/)をご参照ください。<br>
ドキュメンテーションは、[こちら](https://docs.xoxzo.com/ja/sms#send-sms-messages-api)です。完結で使いやすいXoxzoのSMS APIの導入に、お役立てください。<br>
<br>
<br>
###　Mail2SMSでもご利用いただけます。
長文対応SMS API はもちろん、[Mail2SMS](https://www.xoxzo.com/ja/about/mail2sms-api/)でもご利用いただけます。<br>
![Mailsms_ja_042](/images/mailsms_ja_042.png)<br>
Eメールを送信するように、メーラーから送信可能なため、開発も不要ですので、簡単、お気軽にご利用いただくことができます。<br>
詳細は、[ヘルプページ](https://help.xoxzo.com/ja/xoxzo-cloud-telephony/sms-api/articles/how-to-send-via-mail2sms/)をご参照ください。<br>
<br>
**【ご注意】**<br>
1通のSMSに含めることのできる文字数は、GSMの仕様により日本語は70文字までです。XoxzoのAPIで受け付ける文字数は660文字まで広がりましたが『長くかける』=『コスパがいい』わけではありません。660文字最大のメッセージを送信すると、通常のSMSを10通送信したのと同じ料金が発生しますのでご注意ください。<br>
文字数により、受け取る側の印象も変わります。実務的には、SMSはショートメッセージですので、要点を明確にするほうが効果的です。下記に目安をご紹介します。<br>
<br>
70文字以内：通知・一言キャンペーン・短縮URL付きで誘導<br>
```【〇〇】明日のご来店予約を確認しました。ご不明点は https://xxx.jp```<br><br>
150〜200文字程度：簡単な説明 + アクション誘導（リンク等）<br>
```【〇〇ストア】本日限定セール開催中！人気アイテムが最大50%オフ！今すぐチェック：https://xxx.jp/sale```<br><br>
660文字近く：詳細説明が必要な場合やステップメール的な活用（稀）<br>
```【〇〇クリニック】健康診断の結果をお知らせします。今回の検査では血圧が高めとの結果が出ております。日常生活での注意点や、今後の通院についてのアドバイスを同封しておりますので、郵送物をご確認のうえ、不明点があればお電話ください。次回のご予約は https://xxx.jp より可能です。```<br>
<br>
読み物：[長文SMSというのは、Eメールのこと](https://blog.xoxzo.com/ja/2021/12/07/long-sms-is-not-sms/)<br>
<br>
ご不明な点や、ご相談は、[ヘルプデスク](mailto:help@xoxzo.coom)までご連絡ください。<br>
<br>
今後も[Xoxzo](https://www.xoxzo.com/ja/)をどうぞよろしくお願いします。
