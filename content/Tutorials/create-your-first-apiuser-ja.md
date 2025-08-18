Title: 最初のAPIユーザーを作ろう
Date: 2017-10-13 12:00
Author: Miko-chan
Tags: api user; api; tutorial; ミコちゃん;
Slug: create-your-first-apiuser
Thumbnail: images/xoxtan.png
Lang: ja
Summary: まずは、あなたの最初のAPIユーザーを作ってみてね！
Series: Xoxzo API Tutorial
Series_index: 2

<div class="lg-padding-top50 md-padding0">
Xoxzoへようこそ！わたしたちのAPIを使うと、SMSを送ったり、電話をかけたり、もっといろいろ、できちゃうんです。でも、その前に。APIキーとトークンを手に入れてね！
え？どうやって、やるかって？</div>
<div style="clear:both;"></div>

## APIユーザーって?

APIキーとトークンのセットには、ひとりのAPIユーザーが必要なの。

この、APIユーザー、っていうのは、あなたのアカウントを使って、SMS送信とかをする時の、バーチャルユーザーだって、考えてね。

Xoxzoのアカウントでは、APIユーザーはひとつだけじゃなくて、必要に応じて、もっとAPIユーザーを登録することができるのよ。

## それでは、APIユーザーを、作ってみましょう！

APIユーザーを作るのは、とても簡単よ。まずは、ログインしてね。

そして、プロフィールページで、*『APIユーザーの追加』*っていうボタンを探してみて。

![apiuserpage](/images/apiuser_page-ja.png)

見つかったらクリックして、あなたのAPIユーザーの名前を入力！

それだけ！できあがり！

ハイライトして、簡単にコピペできちゃうAPIキーが、わかるかな？

デフォルトでは、トークンは *かくれんぼ *してるから、 *『トークン表示』* をクリックして、表示させてみてね！

## でも、他に何ができるかって？

鉛筆のアイコンをクリックすると、APIユーザーの名前を変更できちゃうのよ。

それに、『許可IPアドレス』に、IPやCIDRレンジを入力して、利用制限をかけることもできちゃいまーす。

制限を解除したくなったらいつでも、このリストから削除してねっ。

![editpage](/images/edit_page-ja.png)

わたしたちXoxzoのAPIの使い方は、[こちら](https://docs.xoxzo.com/ja/) ！
どうぞ、よろしくね！

[ミコちゃんのチュートリアル・シリーズ](https://blog.xoxzo.com/ja/tag/mikochiyan/)好評不定期連載中


Title: APIユーザーを作成してみましょう
Date: 2017-10-13 12:00
Author: Miko-chan
Tags: api user, api, tutorial
Slug: create-your-first-apiuser
Thumbnail: images/xoxtan.png
Lang: ja
Summary: APIを使うための第一歩として、APIユーザーを作成してみましょう。

## はじめに

Xoxzoへようこそ！
APIを使えば、SMSを送ったり、電話をかけたりと、さまざまな機能を活用できます。
そのために必要なのが APIキーとトークン。そして、それを取得するには、まず APIユーザー を作成する必要があります。

今回は、その最初のステップを一緒に確認していきましょう。

## APIユーザーとは？

APIユーザーは、XoxzoアカウントからAPIを利用するときに必要となる「仮想ユーザー」です。
複数作成することもできるので、利用目的ごとに分けて管理することが可能です。

## APIユーザーを作成する手順

では実際に、APIユーザーを作ってみましょう。

まずはXoxzoにログインします。

プロフィールページを開き、「APIユーザーの追加」 ボタンをクリックします。

任意の名前を入力すれば、すぐに作成完了です。

作成後は、APIキーが表示されます。コピーして保存しておきましょう。
なお、トークンはデフォルトでは非表示になっているため、「トークン表示」 をクリックして確認してください。

## APIユーザーを編集する

作成したAPIユーザーは、あとから管理することもできます。

名前を変更：鉛筆アイコンをクリック

利用制限を追加：許可するIPアドレスやCIDRレンジを登録

制限解除：不要になった制限を削除

状況に合わせて調整できるので安心です。

## まとめ

これで、APIユーザーの作成と基本的な管理方法がわかりました。
次のステップでは、このユーザーを使って実際にAPIを呼び出してみましょう。

👉 APIの詳細は [公式ドキュメント](https://docs.xoxzo.com/ja/) をご覧ください。
👉 シリーズ記事一覧は [こちら](/tutorial-index-ja.html)


{% include "tutorial-footer.html" %}
