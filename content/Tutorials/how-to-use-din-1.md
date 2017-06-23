Title: ダイアルインナンバーを使ってみよう
Date: 2017/07/01
Author: Akira Nonaka
Tags: 
Slug: 
Lang: ja
Summary: 電話の着信を制御するダイアルインナンバーAPIの概要を解説します

## 概要

### ダイアルインナンバーとは?

ダイアルインナンバー(Dial in number;以降DINと書きます)はXOXZOの
テレフォニーAPIで、電話の着信を制御する機能です。ユーザーは、電話番号を
契約し、その電話に着信があった場合、転送やメッセージの再生するシステムを
APIを使って構築することができます。

利用するまでの大まかな流れは以下のようになります。

1. 空き番号を検索する
1. その中から、希望の電話番号を選び契約する
1. アクションサーバーを作る
1. アクションサーバーのURLを設定する

### アクションサーバーと電話着信時の動作
 
契約した電話番号に着信があったとき、XOXZOクラウドシステムはAPIで指定されたWebサーバ（以降、アクションサーバと呼ぶ）のアクションURLに対してHTTPリクエストを発行します。
DINを使うユーザは、XOXZOクラウドからのHTTPリクエストに応答するアクションサーバを設置しなければいけません。

![着信時の動作の図]({filename}/images/Tutorial/din-get-call-ja.jpeg)

アクションは、着信した電話をどのように処理するかをXOXZOクラウドシステムに対して指示するもので、次の３つの種類があります。

<dl>
    <dt>playback
    <dd>指定されたMP3ファイルを再生
    <dt>transfer
    <dd>指定された電話番号へ転送する
    <dt>say
    <dd>指定されたテキストを読み上げる
</dl>

それでは、以下順を追って、DINシステムをどのように構築していくか、解説します。

## 空き番号を検索する

DINで利用可能な電話番号はXOXZOクラウドシステムがプールしていて、ユーザーはこの中から自分の好きな電話番号を
選ぶことができます。利用可能な電話番号の一覧を得るには次のAPIを使います。

[DIN検索API](http://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)

このAPIでは、電話番号に１対１で対応する`din_uid`(DINに対応する、ユニークな識別子）が返されます。
以下に列挙するAPIでは、この `din_uid` が重要なパラメータとして使われますので、しっかり覚えておきましょう。

## 着信用電話番号を契約する

使いたい電話番号が決まったら、その番号を契約します。
契約にするには

[DIN契約API](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)

を使います。URLには検索APIで取得した `din_uid` を指定しましょう。

契約が成功したら

[DIN契約確認API](http://docs.xoxzo.com/ja/din.html#getting-the-list-of-subscribed-dial-in-numbers-via-api)

を使って、正しく契約されているかを確認しましょう。

## アクションサーバーをつくる

電話着信時にアクションサーバへ発行されるHTTPリクエストのメソッドは`GET`で２つのパラメータが付いています。

|パラメータ|意味|
|---------|------------------|
|caller |電話の発信者番号   |
|recipient|着信したDINの電話番号|


応答のアクションは１行のプレーンテキストで返します。
アクションの詳細については[ここを参照してください](http://docs.xoxzo.com/ja/din.html#available-actions)

## アクションURLを設定する

アクションサーバーの設置が完了したならばら、そのサーバーをXOXZOクラウドシステムが呼び出せるように、
アクションサーバーのURLをXOXZOクラウドに教えてあげる必要があります。
このURLの設定には以下のAPIを使います。

[アクションURL設定API](http://docs.xoxzo.com/ja/din.html#attach-an-action-to-the-dial-in-number-via-api)

## 電話番号を解約する

DINの解約をするには次のAPIを使います。

[DIN解約API](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)

## トラブルシュート

DINがうまく動かないときは次の点をチェックしてみましょう

- アクションURLは設定されているか？
- アクションURLは正しく、アクションサーバを指しているか？
- アクションサーバーは、アクセス可能な状態か？
- 再生するサウンドのmp3ファイルは、アクセス可能な状態か？
- アクションの応答テキストに間違いはないか? コマンドのスペル、引数の数、引数の内容は正しいか？
- クレジットは十分にあるか?
