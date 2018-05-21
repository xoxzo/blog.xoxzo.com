Title: サイバーセキュリティにおける、SMSと音声通話の役割
Date: 2018-5-22 12:00
Author: Ai Sin Chan
Tags: api; sms; voice api; サイバーセキュリティ; 2要素認証; 多要素認証; SMSコード; 
Slug: 2fa-cyber-security
Lang: ja
Thumbnail: images/2facybersecurity.jpg
Summary: サイバーセキュリティにおいて、なぜ2要素認証が、重要なのでしょうか？

これまで、企業や公共サービスで利用できる可能性のある、SMSや音声通話の利用方法について、たくさん議論してきました。
SMSと音声通話が、データ保護とサイバーセキュリティの役割を果たすことができる、今後拡大していきたい領域が、もう1つあります。

![2facybersecurity](/images/2facybersecurity.jpg)

## セキュリティ侵害の種類

よく見られる、目立ったセキュリティ侵害のトップ５はとして、下記があります。

* フィッシングとソーシャルエンジニアリング

* パスワード攻撃

* マルウェア

* [ランサムウェア](https://www.npa.go.jp/cyber/ransom/main1.html)

* [DoS攻撃](https://ja.wikipedia.org/wiki/DoS%E6%94%BB%E6%92%83)

## 知っておきたいセキュリティ侵害の例

企業における事件：史上最大のサイバーセキュリティ侵害事例を抱えるのは、ヤフー!で、ユーザーアカウントデータがハッカーに侵害される、大事件が２度も報告されています。2013年には10億ユーザーアカウントに、2014年には5億ユーザーに影響を与えています。

個人における事件: テクノロジージャーナリストのMat Honan氏は、Apple、Amazonの認証手続きの脆弱性のために、2012年にはGoogle、Twitter、Amazon、Appleのアカウントを、またMacBookやiPhoneへのアクセスを失いました。 ハッカーがソーシャルエンジニアリングを適用しし、Honan氏のアカウントへ侵入したのです。しかも、ハッカーたちは3文字のTwitterのハンドルネームを参照しただけだったのです。 なんとも痛い損失でした。Honan氏の一番の後悔は、データをバックアップしておらず、アカウントに2FAを使用していなかった、ということでした。


## 2FA(二要素認証、多要素認証）って何？

二要素認証は、ユーザーを特定するために、下記より２つを合わせた方法で認証を行うことです。

* ユーザーの知っていること (ログイン情報: ユーザーネームやパスワード)

* ユーザーの持っているもの (ハードウェア: キーフォブや携帯電話)

* ユーザーそのもの (生物的認識: 声紋、指紋、虹彩)

通常、ワンタイムパスワード（OTP）を生成・送信したり、「ユーザーが持っているもの」を適用することによって、2FAを実装する方法が用いられています。

* SMS or 音声通話

* ハードウェア (キーフォブ)

* オンラインアプリケーション

* オフラインアプリケーション

There is a weak point in cybersecurity in the account recovery process, the use of 2FA for logging in is bypassed. In designing the algorithm flow for account recovery such as in case of forgotten password, we highly recommend that a different set of 2FA is implemented before allowing passwords to be reset.
アカウント回復プロセスではサイバーセキュリティに弱点があり、ログインに2FAを使用することはバイパスされます。



## SMS in 2FA

One of the most convenient solutions is to send a OTP to the user’s mobile phone over SMS, which the user must enter on the portal to gain access to her account. Implementing 2FA for your users’ accounts over SMS offers effective protection against phishing and password attacks, the apparent advantages are:

* Protect against weak passwords;

* No key fob required;

* No 3rd party app (whether online or offline) required.

It is also important to note that 2FA over SMS is not immune against:

* Social engineering: where the hacker has convinced your service provider to redirect your phone number to the hacker’s SIM;

* Malware attacks: where SMS sent to an Android phone infected with malware is intercepted and redirected to the hacker’s device instead.

However, we can deduce that the risk of facing such an attack is comparatively low, as opposed to not implementing 2FA at all.

## Voice in 2FA

As a variation to sending an OTP over SMS, voice can be used instead. Applying text-to-speech functionality to the standard 2FA process, the system dials a voice call and sends an OTP via voice audio. This is particularly useful for the visually impaired users.

Using OTP sent to a mobile device via an SMS or a voice clip is user-friendly for your users, relatively cheap and easy to implement, and achieves the purpose of 2FA.

As with any security measure, 2FA is not foolproof, but it adds an effective extra layer of a protective barrier against unauthorized access to any user accounts. There is no reason not to implement it into your system. Our SMS API and Voice API are the perfect tools for you to get started and get it done quickly.
