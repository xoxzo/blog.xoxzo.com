Title: Let's use the dial-in number
Date: 2017/07/01
Author: Akira Nonaka
Tags: din; did; tuborial;
Slug: dialinnumbers-tutorial
Lang: jne
Summary: I will outline the dial-in number API that controls incoming calls

## Overview

### What is dial in number?

The dial-in number (Dial in number, hereinafter referred to as DIN)
It is a function to control incoming calls using XOXZO's Telephony API.
The user contracts the telephone number,
If there is an incoming call on the phone, transfer system or system to play the message
You can build it using the API.

The rough flow until use is as follows.

1. Search for a free phone number
1. Choose the desired phone number from among them and sign up
1. Create an action server
1. Set the action server URL

### アクションサーバーと電話着信時の動作
 
契約した電話番号に着信があったとき、XOXZOクラウドシステムはAPIで指定されたWebサーバ（以降、アクションサーバと呼びます）のアクションURLに対して、HTTPリクエストを発行します。
DINを使うユーザは、XOXZOクラウドからのHTTPリクエストに応答する、アクションサーバを設置しなければいけません。

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

## 空き電話番号を検索する

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
これらのパラメータを使えば、誰から電話がかかってきたか？　何番へ電話がかかってきたか？　がわかります。
これらの情報をつかうことによって、より細かいアクションの制御が可能となります。

<dl>
    <dt>caller
    <dd>電話の発信者番号
    <dt>recipient
    <dd>着信したDINの電話番号
</dl>

応答のアクションは１行のプレーンテキストで返します。
アクションの詳細については[こちらを参照してください](http://docs.xoxzo.com/ja/din.html#available-actions)

[こちら](https://github.com/xoxzo/din-action-server-demo)には Djangoフレームワークを使って作成した
アクションサーバーのサンプルが置いてありあます。

## アクションURLを設定する

アクションサーバーの設置が完了したならば、そのサーバーをXOXZOクラウドシステムが呼び出せるように、
アクションサーバーのURLをXOXZOクラウドに教えてあげる必要があります。
このURLの設定には以下のAPIを使います。

[アクションURL設定API](http://docs.xoxzo.com/ja/din.html#attach-an-action-to-the-dial-in-number-via-api)

## 電話番号を解約する

DINの解約をするには次のAPIを使います。

[DIN解約API](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)

## 各言語用ライブリラリ

XOXZO APIを利用するために便利な Python, Ruby, PHP ライブラリが用意されています。これらはMITライセンスのオープンソースで、ユーザーは自由に利用することができます。

- [Python](https://github.com/xoxzo/xoxzo.cloudpy)
- [Ruby](https://github.com/xoxzo/xoxzo-cloudruby)
- [PHP](https://github.com/xoxzo/xoxzo.cloudphp)

## トラブルシュート

DINがうまく動かないときは次の点をチェックしてみましょう

- アクションURLは設定されているか？
- アクションURLは正しく、アクションサーバを指しているか？
- アクションサーバーは、アクセス可能な状態か？
- 再生するサウンドのmp3ファイルは、アクセス可能な状態か？
- アクションの応答テキストに間違いはないか? コマンドのスペル、引数の数、引数の内容は正しいか？
- クレジットは十分にあるか?
