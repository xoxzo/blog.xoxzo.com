Title: supを使って、複数のサーバでコマンドを実行する
Date: 2018-08-27
Author: Kamal Mustafa
Tags: golang, deploy
Slug: running-command-multiple-servers-sup
Lang: ja
Summary: supと呼ばれるツールを、複数のサーバーにおいて、リモートでコマンドを実行するのに使ってみました。

supは、Golang (https://github.com/pressly/sup)で書かれたツールです。
Fabricや、特定の側面においては Ansible によく似ていますが、Fabricより柔軟で、Ansibleよりシンプルだと思いました。
もし、もう [Golang environment on your computer](https://github.com/devkini/notes/wiki/Go)があれば、コトは簡単。
ただ下記のように：-


```
go get -u github.com/pressly/sup/cmd/sup
```

次に Supfile を定義します。こんな感じです:-

```
networks:
    web:
        hosts:
            - web-01.site.com:22
            - web-01.site.com:22
    db:
        hosts:
            - db-01.site.com:10022

commands:
    tailf:
        desc: Tailf local1
        run: tailf /var/log/local1
    bash:
        desc: Interactive commands on all hosts
        stdin: true
        run: bash
```

それから、コマンドを実行。例えば web サーバー上の talif :-

```
sup web tailf
```

すべてのサーバーでコマンドを対話形式で実行することだって、できます。 上記のsupファイルでは、対話モードで実行するコマンド、bashを定義しました。

```
sup web bash
```

今は、プロンプトは表示されませんが、実際の入力を開始してEnterを押すことができます。 
たとえば :-


grep ERROR /var/log/local1
You'll get output:-

```
grep ERROR /var/log/local1
kamal@web-01.site.com:22 | kamal@web-01:~$ Jan 12 21:21:06 web-01 messaging.Sender.send(): ERROR: Sending failed for xxx0 user1: -2 HTTPSConnectionPool(host='sender2.local', port=443): Max retries exceeded with url: /h/send (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7ff769fe2c50>, 'Connection to sender2.local timed out. (connect timeout=10)'))
```

終了するには、exit と入力するだけ:-

```
exit
kamal@web-01:50022 | kamal@web-01:~$ exit
kamal@web-01:22 | kamal@web-01:~$ kamal@web-01:~$ exit
kamal@web-02:22 | kamal@web-02:~$ kamal@web-02:~$ exit
kamal@web-02:22 | Process exited with status 1
```

対話式にしなくても、コマンドがパイプにもなってくれるわけです:-

```
echo 'grep ERROR /var/log/local1' | sup x4 bash
```

## 問題点
1. インタラクティブコマンドをしばらくアイドル状態にすると応答がなくなり、強制終了することになります。
2. コマンド編集時、カーソルを移動できないので、それまでに入力したものを削除することになります。
3. コマンド履歴がない
