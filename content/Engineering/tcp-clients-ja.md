Title: TCP クライアントの対話
Lang: ja
Date: 2020-08-31 09:00
Author: Arthur Sultanbekov
Tags: tcp; tcpクライアント; http; websocket; keepalive; 2020;
Slug: tcp-clients-communication
Summary: TCP クライアントの対話を分析しました

ユーザーがデータを送信し、サーバーがレスポンスを返す、というクライアントとサーバーの機能を、私はたいてい理解できます。
しかし、それだけでは、あまりに浅いレベルです。そこで、そのあたりの機能が、どのように対話するかということに焦点を合わせて、より深く学んでみることに決めました。
ありがたいことに、そういった対話を表示できる `Wireshark` や `tcpdump` といったツールもあります。
私は主にWebテクノロジーを扱っているので、Webに関連するTCPクライアントを分析したいと思いました。
以下の実験は、すべて Ubuntu20.04 で行いました。

## 基本的な HTTPクライアントと 理論を少し

とても基本的な例から始めましょう。python の requests モジュールを使用して htmlページを取得します。
```python
>>> import requests
>>> r = requests.get('http://example.com/')
```
ダイアログを確認すると、次のようになっています。

*	`requests` が `Connection: keep-alive` ヘッダーをデフォルトで追加します。
*	gzip 圧縮されたレスポンスを、受け取りました。

基本的なHTTPクライアントは keepalive を使用しません。簡単にするために、gzipをオフにして続行します。

```python
>>> r = requests.get('http://example.com/', headers={'Accept-Encoding': 'identity', 'Connection': 'Close'})
```

次に出力を見てみましょう。

![http dialog]({filename}/images/tcp-clients-communication/2020-08-29_15-12.png)

または、概略ダイアログは次のようになります。

![schematic http dialog]({filename}/images/tcp-clients-communication/2020-08-29_16-26.png)

First, we can see that every TCP request or reply has some flags like SYN, ACK, they are named Control bits, and used for congestion notification. There's 6 such flags:

* URG: Urgent Pointer field significant
* ACK: Acknowledgment field significant
* PSH: Push Function
* RST: Reset the connection
* SYN: Synchronize sequence numbers
* FIN: No more data from sender

まず、すべてのTCP要求または応答には、制御ビットと呼ばれる SYN、ACKなどのフラグがあり、輻輳通知に使用されていることがわかります。この種のフラグは6つあります。

•	URG：緊急ポインタフィールド 重要
•	ACK：確認フィールド 重要
•	PSH：プッシュ機能
•	RST：接続をリセット
•	SYN：シーケンス番号を同期
•	FIN：送信者からのデータは以上

4つのフラグは有名で、次のことを示しています。
SYN - 接続を開始します<br>
ACK - 受信データを確認します<br>
FIN - 接続を閉じます<br>
RST - エラーに応答して接続を中止します<br>
その他2つのフラグ PSH（push）とURG （urgent）は、あまり知られていません。[ここ](https://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/)で詳細を参照することができます。

上記のクライアント（C）とサーバー（S）の間のダイアログを見ると、次のように読むことができます。
* CはSとの接続を確立したい（SYNを送信）
* SはACKで応答します-接続を許可します
* Cは再度ACKで応答します-接続が確立されます。
* CはGEThtmlページ（PSH、ACK）のリクエストを送信します
* SはACKで応答します*そしてリクエストされたページを送信します。
* Cはデータを受信したと応答し、ACKを送信します
* CはFIN、ACKを送信します-クライアントにはSに送信するデータがありません
* SもFIN、ACKで応答します
* 両側に交換するデータがないため、接続を閉じることができます。そして、そうしたわけです。CはACKを送信します
* Sは接続を閉じます。ACKを送信します。

上記のコードを再度実行すると (`requests.get('http://example.com/', headers={'Accept-Encoding': 'identity', 'Connection': 'Close'})`)クライアントは同じダイアログで再び接続を確立します。

## keepalive を備えた HTTP クライアント

`Connection` ヘッダー値を `keepalive` に変更したときの動作を確認しましょう。

この場合、クライアントがサーバーから最後のACKを取得しなかったことを除いて、ダイアログは前の例と同じであることがわかります。そのため、サーバーは接続を閉じません。keepalive の利点を確認するには、クライアントからサーバーへ、乗算リクエストを実行しなくてはなりません。セッションを使用するようにコードを変更し、乗算リクエストを行うことができます。しかし、私は、TCPクライアント自体であるブラウザーを使用することにしました。カンタンなウェブ検索で、[http://supervisord.org/](http://supervisord.org/) が見つかりました。 ブラウザで開くと、 `/` ページが読み込まれ、次にjs、cssファイル、画像などが読み込まれます。その場合のTCPダイアログの結果は次のとおりです。

![http with keepalive dialog]({filename}/images/tcp-clients-communication/2020-08-29_18-50.png)

クライアントは接続を1回だけ開き、サーバーからデータ （httpページ、静的ファイル、メディアファイル） を取得します。そして、タイムアウトに達し、サーバーは接続を閉じます（タイムアウトの値は、keepalive によって制御される場合があります：`timeout=X、max=Y ヘッダー`）。 もちろん、このようなアプローチはCPU使用率を最小限に抑え、Webサイトのパフォーマンスに役立ちます。 HTTPでのKeep-aliveの詳細については、1）[https://www.imperva.com/learn/performance/http-keep-alive/](https://www.imperva.com/learn/performance/http-keep-alive/) および 2）[https://www.oreilly.com/library/view/http-the-definitive/1565925092/ch04s05.html
](https://www.oreilly.com/library/view/http-the-definitive/1565925092/ch04s05.html) を参照してください。 


## Websocket

WebSocketがhttpリクエストとどのように異なるかを確認しましょう。[simple-websocket-server](https://github.com/dpallot/simple-websocket-server) にて、単純なWSサーバーを使用することにしました 。 
まず、 echo WS server を開始しました。


```python
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):
    def handleMessage(self):
        # メッセージをクライアントに　echo で返す
        self.sendMessage('resp: %s' % self.data)
    def handleConnected(self):
        print(self.address, 'connected')
    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('127.0.0.1', 8000, SimpleEcho)
server.serveforever()
```

そのリポジトリから `websocket.html`ファイルを開いて、ブラウザーを使用してWSをテストします。

![websocket dialog]({filename}/images/tcp-clients-communication/2020-08-29_19-49.png)

![websocket dialog]({filename}/images/tcp-clients-communication/2020-08-29_19-48.png)

ここで、クライアントとサーバーが接続を確立します。その後、両側ともが、接続を閉じないことがわかります。CはFINフラグセット付きのデータを送信し、SもFINで応答し、CはACKを送信します。`Connection：keep-alive`を使用したHTTPと比較すると、WSはタイムアウト後にも接続を閉じていません。WebSocketの動作に興味がある場合は、[この記事](https://lucumr.pocoo.org/2012/9/24/websockets-101/)を読むのも良いでしょう。


## HTTP2
HTTP2プロトコルの理解に興味をお持ちの場合、こちらの[記事](https://blog.lgohlke.de/docker/h2o/2016/03/01/dockerized-h2o-webserver.html) に基づいて次の設定をお勧めします。

1. 私は、セキュリティで保護されていない接続を許可するDockerコンテナを選択しました。

```
> docker run -p "9090:8080" -d lkwg82/h2o-http2-server
```

2. また、http2サポートで [curl](https://curl.haxx.se/docs/http2.html) を使用しました。
```
> curl --version
curl 7.68.0 ...
Release-Date: 2020-01-08
Protocols: ...
Features: AsynchDNS brotli GSS-API HTTP2 HTTPS-proxy ...
# リクエストする
> curl --head --http2 -H 'Accept-Encoding: identity' -v http://localhost:9090
# 応答として404 Not Foundとなりますが、問題ありません
```

そしてこちらがダイアログフローです。

![http2 dialog]({filename}/images/tcp-clients-communication/2020-08-30_11-23.png)

`Connection：Close`ヘッダーを 追加すると、プロトコルがHTTP2に切り替わらないの、面白いところです。上記の例では、 `Accept- Encoding： identity`ヘッダーを使用しましたが、プロトコルはデータ圧縮を使用し、プレーンテキストの代わりにバイトを送信するため、http2の場合に使用しても意味がないのです。


## まとめ
お気づきかもしれませんが、安全でないhttpとwsのリクエストを行い、httpsとwssは行いませんでした。安全なリクエストを行うと、暗号化された対話を見ることとなりますが、これは現在の私にとっては意味がありません。HTTPおよびWSリクエストに加えて、他にも興味深いものもあります。AJAXリクエスト、MySQL / PostgreSQLデータベースへの接続、ファイルのアップロードまたはダウンロードです。
