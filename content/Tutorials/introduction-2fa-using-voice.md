Title: 音声電話を使った二要素認証のやり方
Date: 2018-05-14 10:00
Author: Akira Nonaka
Tags: 二要素認証; チュートリアル;音声
Slug: introduction-2fa-voice
Lang: ja
Summary: Webアプリに音声電話を使った二要素認証を導入する方法の紹介です。

さて前回は、SMSを使った二要素認証の導入方法をご紹介しました。
しかし、どうしてもSMSが利用できない場合もあります。
例えば、電話番号が固定電話の場合などです。
音声電話を使うと、このような場合でも暗証番号を目的の相手に届けることもできます！

音声電話では、暗証番号が聞き取り易いように、メッセージの形式に少し注意が必要です。

# 暗証番号は、最低でも2回繰り返す。
# 相手が電話に出ても、暗証番号の読み上げをはじめるまで、少しの間をおくようにする。

こういった注意をすることで、相手がメモを準備するなどの、余裕をあげることができるでしょう。

Python[^1]のサンプルコードを以下に示します。基本的にSMSのときと同じ構造ですが、メッセージを生成するところに、少し工夫がしてあります。

```
import os
import secrets
from xoxzo.cloudpy import XoxzoClient


def two_fa_voice():
    """ 2要素認証を音声電話で行う　"""
    # ランダムな暗証番号を生成します
    secret_key = secrets.randbelow(10000)
    message = gen_voice_msg(secret_key)
    # APIを呼び出すための秘密鍵は、環境変数に保存されているものとします
    # SIDとTOKENはhttps://www.xoxzo.com/からサインアップして入手してください
    sid = os.getenv('XOXZO_API_SID')
    auth_token = os.getenv('XOXZO_API_AUTH_TOKEN')

    # 音声電話の発信
    xc = XoxzoClient(sid=sid, auth_token=auth_token)
    result = xc.call_tts_playback(caller="0801234567", recipient="+818054695209", tts_message=message, tts_lang="ja")


def gen_voice_msg(secret_key, key_length=4):
    prefix_str = "こんにちは、ゾクゾーです。これからお伝えする暗証番号は誰にも教えないでください。あなたの暗証番号は、"
    mid_str = "です。繰り返します。あなたの暗証番号は、"
    postfix_str = "です。ご利用、どうもありがとうございました。"
    fmt_str = "%%0%dd" % key_length
    num_str = fmt_str % secret_key

    key_str = ""
    for st in num_str:
        key_str += "数字の%s," % st
    return prefix_str + key_str + mid_str + key_str + postfix_str


two_fa_voice()



```
 
#まとめ

音声電話による二要素認証の実現方法を紹介しました。SMSによるテキスト通信とは異なり、
音声電話では相手が内容を聞き取りやすいメッセージにすることが大切です。

[^1]:Python3.6以降の利用を想定しています。それよりも前のPythonには標準では *secrets* パッケージがないので、
適当な乱数生成ライブラリを使う必要があります。