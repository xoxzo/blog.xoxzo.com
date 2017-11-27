Title: 【Xoxzo】APIエンドポイント変更のお知らせ
Date: 2017-11-24 
Slug: endpoint-nouns-change
Lang: ja
Tags: endpoint, nouns
Author: Aikra Nonaka
Summary: APIの呼び出しエンドポイント(URL)変更のお知らせ

XOXZOでは、利便性向上のために、
[音声プレーバックAPI](http://docs.xoxzo.com/ja/voice.html#simple-playback-api)および
[プレーバック発信ステータス確認API](http://docs.xoxzo.com/ja/voice.html#checking-call-status)
の呼び出しエンドポイントを以下の通り変更しましたのでお知らせします。

*音声プレーバックAPI*

* 旧　`POST /voice/simple/playback/`
* 新　`POST /voice/simple/playbacks/`

*プレーバック発信ステータス確認API*

* 旧　`GET /voice/simple/playback/<callid>`
* 新　`GET /voice/calls/<callid>/`

旧来のエンドポイントは、2018/2/28まではお使いになれますが、それ以降は削除されますのでご注意下さい。