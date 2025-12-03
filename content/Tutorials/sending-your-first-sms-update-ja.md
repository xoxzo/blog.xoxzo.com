Title: はじめてのSMSを送ってみよう！
Date: 2025-08-20 12:00
Author: Xoxzo Team
Tags: sms; api; tutorial
Slug: sending-your-first-sms-update
Thumbnail: images/xoxtan.png
Lang: ja
Summary: コマンドラインから最初のSMSを送る手順を解説します。APIキーを用意して、実際にメッセージ送信を試してみましょう。
Series: Xoxzo API Tutorial
Series_index: 4

---

<div>
  <img src="https://blog.xoxzo.com/images/xoxtan.png" class="float-lg-right lg-width200 md-width300" style="margin: 0;">
</div>


## はじめに

前回のチュートリアルでは、最初のAPIユーザーを作成しました。  
今回はいよいよ、**Xoxzo Web APIを使ってSMSを送信**してみます。  

Xoxzo APIの最もシンプルな機能はSMS送信です。この記事では、必要な準備から実際の送信までをステップごとに解説します。

---

## 1. 準備するもの

- **シェル環境**  
  Windowsではコマンドプロンプト、MacやLinuxではターミナルを使用します。  
  ここでは「シェル」と呼びます。

- **APIユーザーのSIDとAuth Token**  
  アカウントにログインし、ダッシュボードの「APIユーザー管理」から確認できます。  
  - `API SID` と `Auth Token` のペアが必要です。  
  - Auth Tokenは「トークン表示」ボタンを押してコピーしてください。  

![SID and token](/images/Tutorial/send-sms/sidtoken-ja.jpg)

- **インターネット接続**

---

## 2. API認証情報のフォーマット

API SID と Auth Token は次のように **コロン（:）でつないで1行**にします。

APiSiD:AUthT0k3n


- コロンを忘れないこと  
- 改行せず1行で書くこと  

この認証情報を使ってリクエストを送ります。

---

## 3. 実際にSMSを送ってみる

あなたの携帯電話番号を **国番号付き（E.164形式）** で準備してください。  
日本の場合は `+81` を先頭につけ、最初の0を省きます。

例: `+819012345678`

### cURLコマンド例
以下をシェルに入力して実行してください。

```bash
curl -u あなたのAPI SID:あなたのAuth Token \
--data-urlencode 'sender=XoxzoTest(送り主として表示されます)' \
--data-urlencode 'recipient=+819012345678' \
--data-urlencode 'message=Hello from Xoxzo!' \
https://api.xoxzo.com/sms/messages/
```
改行を使わず、1行でまとめて書いても動作します。

---

## 4. 実行結果を確認

送信に成功すると、次のようなレスポンスが返ってきます。

```
[{"msgid":"tHi5i5y0urMsGIdt3xT"}]
```

msgid が返ってくれば送信成功です。

数秒後にはあなたの携帯にSMSが届くはずです。

キャリアによっては送信者名が変わる場合があります。

送信後はアカウントのダッシュボードからクレジット残高も確認してみましょう。

## 5. まとめ

これで最初のSMS送信が完了しました！
シンプルな1コマンドでメッセージを届けられるのが、Xoxzo APIの強みです。

さらに詳しい使い方や他の機能（音声通話、ユーティリティAPIなど）は、ドキュメントをご覧ください。

補足：ノーコードでSMSを試すならEZSMS

もしプログラミングをせずにPCからSMSを送りたい場合は、XoxzoのEZSMSサービスもおすすめです。
月額費用や初期費用は不要で、使った分だけのお支払い。ブラウザからすぐに利用できます。

- 複数宛先への一斉送信やカスタマイズ送信に対応

- CSVファイルを使った大量配信も可能

- 170カ国以上への送信対応

**更新履歴**

2025-08: チュートリアル全体を更新。最新UIに合わせた説明と補足を追加。

---
<div class="tutorial-footer">
  <p><a href="/prev-url">← PREV_TITLE</a> · <a href="/tutorial-index-ja.html">チュートリアルシリーズ</a> · <a href="/next-url">NEXT_TITLE →</a></p>
  <p><strong>おすすめ:</strong> <a href="/send-your-first-sms">最初のSMS送信</a> ｜ <a href="/try-voice-api">音声APIを試す</a></p>
</div>
---