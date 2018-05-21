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

アカウント回復のプロセスではサイバーセキュリティに弱点があり、ログインに2FAを使用することで、回避されます。パスワードを忘れた場合、のようなアカウント回復のためのアルゴリズムフローを設計する際には、パスワードをリセットする前に、様々な組み合わせの2FAを実装することを強くお勧めします。



## 二要素認証におけるSMS

最も便利なソリューションの1つは、ユーザーの携帯電話にSMS経由でOTPを送信することです。ユーザーは、自分のアカウントにアクセスするため、受け取ったパスワードをポータルに入力する必要があります。SMS経由でユーザーのアカウントに2FAを実装することで、フィッシングやパスワードの攻撃に対し、効果的にアカウントを保護することができます。利点は次のとおりです。


* パスワードの脆弱性に対して守りを固める

* キーフォブが不要

* 他のアプリケーション（オンラインでもオフラインでも）が不要

SMSを使ったに要素認証は、下記にも影響を受けざるをえないということも、重要です。

* ソーシャルエンジニアリング: ハッカーがユーザーの電話番号を、ハッカーのSIMに転送するように、サービスプロバイダを征服した場合

* マルウェア攻撃: マルウェアに感染したAndroidの携帯電話に送信されたSMSが傍受され、代わりにハッカーのデバイスに転送されます。

しかし、2FAを絶対実装しないのではなく、そのような攻撃に直面するリスクが、比較的低いと推定します。

## 要素認証における、音声通話

As a variation to sending an OTP over SMS, voice can be used instead. Applying text-to-speech functionality to the standard 2FA process, the system dials a voice call and sends an OTP via voice audio. This is particularly useful for the visually impaired users.

Using OTP sent to a mobile device via an SMS or a voice clip is user-friendly for your users, relatively cheap and easy to implement, and achieves the purpose of 2FA.

As with any security measure, 2FA is not foolproof, but it adds an effective extra layer of a protective barrier against unauthorized access to any user accounts. There is no reason not to implement it into your system. Our SMS API and Voice API are the perfect tools for you to get started and get it done quickly.
