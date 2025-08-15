Title: OTP APIを使った最新の二要素認証（2FA）導入方法
Date: 2025-08-15 11:00
Author: miko-chan
Tags: 二要素認証; チュートリアル; sms; otp
Slug: otp-api-2fa-tutorial
Lang: ja
Thumbnail: /images/otp-api.jpg
Summary: Xoxzoの新しいOTP APIを使って、安全で簡単、そしてコスト効率の高い二要素認証を導入する方法を紹介します。

---

> **重要なお知らせ**  
> 本記事では、Xoxzoの最新OTP APIを利用した二要素認証の実装方法を紹介します。  
> 従来のSMS APIを使った実装方法については、[こちらの旧チュートリアル](https://blog.xoxzo.com/ja/2021/11/22/introduction-2fa-sms/)をご参照ください。

## 1. はじめに

オンラインアカウントのセキュリティを強化する方法の一つが二要素認証（2FA）です。  
パスワードだけに依存するのではなく、別の手段で本人確認を行うことで、不正アクセスのリスクを大幅に減らせます。

Xoxzoの新しい **OTP API** を使えば、SMSを利用したワンタイムパスワード認証を、より簡単・安全・低コストで実装できます。

---

## 2. OTP APIの基本フロー

1. **OTPを発行** — ユーザーの電話番号宛に一度きりの認証コードを送信
2. **ユーザーがコードを入力** — サービス側で受け取り、コードを検証
3. **認証成功または失敗の判定**

---

## 3. 実装例（Python）

以下の例では、`requests` を使用してOTPの発行と検証を行います。

### OTP発行
```python
import os
import requests

# APIキーとトークン（環境変数から取得）
api_sid = os.getenv("XOXZO_API_SID")
api_token = os.getenv("XOXZO_API_AUTH_TOKEN")

# OTPを発行
resp = requests.post(
    "https://api.xoxzo.com/otp/request/",
    auth=(api_sid, api_token),
    json={
        "website": "https://example.com",  # 認証元のサイト
        "phone_number": "+818012345678"    # ユーザーの電話番号（E.164形式）
    }
)

print(resp.json())
```

###　OTP検証
```
resp = requests.post(
    "https://api.xoxzo.com/otp/verify/",
    auth=(api_sid, api_token),
    json={
        "otp_id": "<上で取得したOTP ID>",
        "code": "123456"  # ユーザーが入力したコード
    }
)

print(resp.json())
```
---

## 4. アップデートするメリット

- セキュリティ強化
専用エンドポイントとAPI側のバリデーションにより、より安全な認証プロセスを実現します。

- シンプルな実装
旧方式に比べてコードが短くなり、メンテナンスも容易です。

- コスト効率の向上
最新のOTP APIは従来のSMS送信よりも料金が安く、ランニングコストを抑えられます。
詳細な料金は[料金ページ](https://www.xoxzo.com/ja/about/pricing/)をご確認ください。

- 管理の容易さ
OTPの発行・検証履歴をダッシュボードで一元管理できます。

---

## 5. まとめ

OTP APIを利用することで、二要素認証をより安全に、そして手軽に導入できます。
従来のSMS送信APIを利用している場合でも、コードの書き換えは最小限で済み、さらにコスト面のメリットも得られます。

詳細なAPI仕様や追加機能については、OTP API ドキュメントをご参照ください。

**更新履歴**

2025-08: 新しいOTP APIを利用した二要素認証チュートリアルを公開