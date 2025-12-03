Title: SMSが届かない？音声通話による認証という選択肢
Slug: sms-vs-voice-auth
Lang: ja
Date: 2025-11-21
Tags: SMS, 音声API, 認証, 代替手段, Xoxzo
Author: Aiko Yokoyama
Thumbnail: images/smsvsvoice-ja.jpg
Summary: SMSが届かない場合の代替手段として、音声通話によるコード読み上げ認証を解説します。固定電話しか使えない環境やSMS受信が不安定な端末でも利用可能な柔軟な認証方式です。

- - -

<img src="https://blog.xoxzo.com/images/smsvsvoice-ja.jpg" width="200" height="200" style="margin: 0;">

## SMS認証が難しいときの「音声通話による認証」という選択肢

本人確認で最も広く使われているのはSMS認証ですが、
**「SMSが届かない」「SMSが確認できない」** という状況は少なからず発生します。

* 受信端末の設定で海外SMSがブロックされている
* キャリア網の混雑・遅延
* ＋メッセージなど専用アプリの影響
* 固定電話のみ利用している高齢者・法人窓口がある

このような状況で有効な代替手段が、
**音声通話**（Voice API）**によるテキスト読み上げ認証** です。

- - -

## どういう仕組み？

音声認証は、ユーザーの電話番号に発信し、
自動音声（TTS）で認証コードを読み上げる仕組みです。

「こちらは認証サービスです。認証コードは 1 2 3 4 です。」

* 通話を取るだけでコードが確認できる
* スマホでなくても、固定電話でもOK
* SMSが不安定な地域でも確実に伝わる
* システム側はSMS認証とほぼ同じフローで導入可能

- - -

## 音声認証が向いているケース

### ① SMSが安定しない地域・端末

海外SMSブロックや＋メッセージの影響で
SMSが届きにくい環境でも確実にコードを伝達できます。

### ② 固定電話しか使えないユーザー

企業の受付番号や高齢者の固定電話など、
**スマホ以外の電話** にも対応できます。

### ③ 視覚的な理由でSMSの確認が難しいユーザー

音声で認証コードが聞けるため、アクセシビリティの面でも優れています。

- - -

## コストと実装の手軽さ

Xoxzoの **Voice API** を利用した音声通話認証は：

* **約10円/1通話**（国内）
* SMSの代替として負担にならない価格帯
* 既存の認証フローに簡単に追加可能

詳しくはドキュメントをご覧ください
https://docs.xoxzo.com/ja/voice/

- - -

## SMS認証との比較表

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid #ccc; padding: 8px;">項目</th>
      <th style="border: 1px solid #ccc; padding: 8px;">SMS認証</th>
      <th style="border: 1px solid #ccc; padding: 8px;">音声通話認証</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">受信方法</td>
      <td style="border: 1px solid #ccc; padding: 8px;">SMSアプリ</td>
      <td style="border: 1px solid #ccc; padding: 8px;">電話を受けるだけ</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">固定電話対応</td>
      <td style="border: 1px solid #ccc; padding: 8px;">✕</td>
      <td style="border: 1px solid #ccc; padding: 8px;">◯</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">海外SMSブロックの影響</td>
      <td style="border: 1px solid #ccc; padding: 8px;">受ける</td>
      <td style="border: 1px solid #ccc; padding: 8px;">受けない</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">キャリア遅延の影響</td>
      <td style="border: 1px solid #ccc; padding: 8px;">受ける</td>
      <td style="border: 1px solid #ccc; padding: 8px;">受けにくい</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">アクセシビリティ</td>
      <td style="border: 1px solid #ccc; padding: 8px;">画面確認が必要</td>
      <td style="border: 1px solid #ccc; padding: 8px;">音声で伝達</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">コスト</td>
      <td style="border: 1px solid #ccc; padding: 8px;">約10円（Xoxzo 絶対認証は3円より）</td>
      <td style="border: 1px solid #ccc; padding: 8px;">約10円（<a href="https://www.xoxzo.com/ja/about/pricing/voice/#outbound-call" target="_blank">料金ページ</a>）</td>
    </tr>
  </tbody>
</table>

- - -

## 導入アイデア

* **初回認証はSMS、失敗したら音声通話で再チャレンジ**
* 固定電話ユーザーが多いサービスでは
**最初から音声通話を選択肢として表示**

認証失敗率の低減につながり、結果として
**ユーザーの離脱防止** にも役立ちます。

- - -

## まとめ

* SMS認証が届きにくい環境は一定数存在する
* 音声通話認証は固定電話でも利用でき、非常に安定した代替手段
* コストはSMSと同等で、導入の負担も小さい

- - -

## 関連リンク

* [Xoxzo SMS API ドキュメンテーション](https://docs.xoxzo.com/ja/sms/)
* [Xoxzo Voice API（音声API）](https://docs.xoxzo.com/ja/voice/)
* [認証専用 OTP API（3円/SMS）](https://docs.xoxzo.com/ja/otp/)

## 関連記事
[SMSが届かない？まず確認したい3つのポイント](https://blog.xoxzo.com/ja/2025/11/14/sms-not-received-checkpoints/)<br>
[SMS認証 vs SNS認証：どちらが本人確認に向いている？](https://blog.xoxzo.com/ja/2025/12/03/sms-vs-social-auth/)
