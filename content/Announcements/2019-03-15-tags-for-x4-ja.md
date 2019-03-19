Title: 新規パラメーター tags リリース！
Date: 2019-03-15
Slug: tags-with-xoxzo-api
Lang: ja
Tags: xoxzo; 新規リリース; 2019; tags;
Author: Iqbal Abdullah
Summary: tags パラメーターを使って、APIコールをカテゴリー分けできるようになりました。

ご要望いただいておりました、**APIコールのカテゴリー分け**が可能になりました。


簡単にAPIコールのカテゴリー分けができる、新機能がリリースされました。
**tags** パラメーターをAPIコールに加えるだけです。

ひとつのAPIコールに複数のタグをつけることも、可能です。

例:

    #!/bin/sh
    # You should get SID and AUTH_TOKEN from XOXZO console
    curl -u $SID:$AUTH_TOKEN \
         --data-urlencode 'sender=+818011112222' \
         --data-urlencode 'recipient=<recipient>' \
         --data-urlencode 'message=Hello world' \
         --data-urlencode 'tags=tag1,tag2,tag3' \
         https://api.xoxzo.com/sms/messages/

ご利用のSMS配信およびVoiceのAPIコールに、この **tags** がご利用いただけます。

この **tags** は、[SMSの配信状態を確認するAPI](https://docs.xoxzo.com/ja/sms.html#check-sms-status-api) や、
[プレーバック発信ステータス確認](https://docs.xoxzo.com/ja/voice.html#checking-call-status) にて、それぞれ取得することができます。

例:

    #!/bin/sh
    # You should get SID and AUTH_TOKEN from XOXZO console
    curl -u $SID:$AUTH_TOKEN \
        https://api.xoxzo.com/sms/messages/7sBZmVznoXJap2wkMIlihgPKqjdOGS1f/

レスポンスデータ :

     {
        "sender": "8011112222",
        "msgid": "7sBZmVznoXJap2wkMIlihgPKqjdOGS1f",
        "status": "DELIVERED",
        "cost": 10,
        "sent_time": "2019-03-15 08:29:09",
        "tags": [
            "tag1",
            "tag2",
            "tag3"
        ],
        "url": "https://api.xoxzo.com/sms/messages/7sBZmVznoXJap2wkMIlihgPKqjdOGS1f/",
        "recipient": "<recipient>"
    }

このタグデータを、XoxzoのAPIのご利用をカテゴリー分けするのにご活用いただけます。
例えば、マーケティングキャンペーン毎に違ったタグをご利用いただいたり、メッセージを送信したり電話をかけたりする
顧客をグループ分けしたり、異なるメッセージごとに異なるタグを設定したりするのにも便利です。

将来的には、このタグデータを使い、それぞれのメッセージや通話がどの程度効果を上げたかを、
ご自身で手軽に可視化できるようにすることも考えています。

この **tags** パラメーターについて、詳しくは[SMSメッセージ送信API](https://docs.xoxzo.com/ja/sms.html#send-sms-messages-api) 
及び[音声プレーバックAPI](https://docs.xoxzo.com/en/voice.html#simple-playback-api)をご参照ください。
