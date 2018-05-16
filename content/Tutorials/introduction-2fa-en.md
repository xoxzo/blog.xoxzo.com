Title: How to set up Two-Factor Authentication using SMS
Date: 2018-05-02 10:00
Author: Akira Nonaka
Tags: 2FA; Tutorial; SMS; API;
Slug: introduction-2fa-sms
Lang: en
Summary: Let's learn how to add Two-Factor Authentication on your Web-applications

いろいろなWebサービスで、ユーザIDとパスワードが流出し、アカウントが乗っ取られて不正に利用されるという問題が多発しています。
このような問題を防ぐ手段として、ユーザーの携帯番号を確認するのが一般的になってきました。
仮にIDとパスワードが盗まれても、それだけではアカウントは使えず、なにか追加の手段で、利用者が本当に登録した本当であるかどうか確認しようとするのが、
二要素認証の考え方です。XOXZOのテレフォニーAPIの使われ方の中で、最も多いものの一つも二要素認証です。

Webサービスで、SMSを使った二要素認証を導入するとすれば、その流れは、おおよそ次のようになるでしょう。

1. ユーザのアカウント登録時には、あらかじめ本人の携帯番号を登録してもらう。
1. Webサービスにユーザーがログインしようとする。
1. Webサービス内で、4桁から6桁程度のランダムな暗証番号を生成する。
1. ユーザーが登録している電話番号へSMSでその暗証番号を送る。
1. Webサービスで、暗証番号を入力してもらう。

暗証番号が一致すれば、たしかにログインしようとしているユーザーは、本人の携帯電話を所持していることになりますでの、ログインを許可することになります。
逆に、正しい暗証番号が入力されなければ、そのユーザーが本人であるか怪しいので、ログインを拒否することになります。

暗証番号をSMSで送信するPython[^1]のコード例を次に示します。

    import os
    import secrets
    from xoxzo.cloudpy import XoxzoClient
    
    # ２要素認証をSMSで行うためのサンプルコード
    
    # ４桁のランダムな暗証番号を生成します
    secret_key = secrets.randbelow(10000)
    message = "こちらはXOXZOです。あなたの暗証番号は %04d です" % secret_key
    
    # APIを呼び出すための秘密鍵は、環境変数に保存されているものとします
    # SIDとTOKENは https://www.xoxzo.com/ からサインアップして入手してください
    sid = os.getenv('XOXZO_API_SID')
    auth_token = os.getenv('XOXZO_API_AUTH_TOKEN')
    
    # SMSの送信
    xc = XoxzoClient(sid=sid, auth_token=auth_token)
    result = xc.send_sms(message=message, recipient="+818054695209", sender="XOXZO")

このコードを実行すると、次のようなSMSがユーザーの携帯電話に届くはずです。

<br>
***
<br>
![SMS PIN](/images/introduction-2fa-sms/sms-2fa-ja.jpg)
<br>
<br>

この後、ユーザーに暗証番号の入力を求めるフォームを表示して、それが *secret_key* と一致すれば認証成功です。
 
#まとめ

以上、簡単なSMS二要素認証の紹介をしました。
この方式を導入すると、例えば一人の人間が複数のアカウントを作り、目的に応じて使い分けるといった裏アカウントを防ぐこともできます。

[^1]:Python3.6以降の利用を想定しています。それよりも前のPythonには標準では *secrets* パッケージがないので、
適当な乱数生成ライブラリを使う必要があります。
