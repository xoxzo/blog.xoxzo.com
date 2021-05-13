Title: Amazon Linux 2AMIを使用してAWSElasticbeanstalkにDjangoChannels2.xをデプロイする方法
Date: 2020-07-17 08:00
Author: Jules Capacillo
Tags: django-channels; tutorial; elasticbeanstalk;
Slug: deploy-django-channels-in-elasticbeanstalk
Lang: ja
Summary: Django Channels 2.x を Amazon Linux 2 Amisを使って、Elasticbeanstalk にデプロイする方法を解説します。 

アマゾンウェブサービス（AWS）Elasticbeanstalk（EB）にアプリケーションをデプロイする際に難しいのは、クラスター内にある、それぞれのインスタンスで実行されるプロセスを処理することが挙げられます。私の場合、どのように、ロードバランサーを介してElasticbeanstalkにDjangoChannels 2をデプロイするか、でした。

ネット上には、チュートリアルやガイドがたくさんあるのですが、実際に役に立つものがありませんでした。というのも、AWSの最新の環境プラットフォームは、以前のチュートリアルが使えない、異なる設定とディレクトリ構造を持つAmazon Linux （AMI 2）インスタンスを使用しているというのに、ほとんどのチュートリアルがAmazon Linux AMIインスタンス用の構成ファイルを使用したものだったからです。AMI 2への移行方法について詳しくは、<a href="https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/using-features.migration-al.html" target="_blank">こちら</a>をご覧ください。

このチュートリアルは、3つのパートに分かれています。興味のあるところを自由に選んで読んでください。

- <a href="#assumptions">下準備</a>
- <a href="#deployment">アプリケーションのデプロイ</a>
- <a href="#using_https">Https を使う</a>


<h3 id="assumptions" class="anchor-link">下準備</h3>
このチュートリアルが有効なものとなるよう、基本的な下準備を下記に記しておきます。

1. アプリケーションロードバランサー（ALB）ルーティングセットアップを使用中。ということは、すべてのトラフィックがALBによって処理されているということです。このチュートリアルではネットワークロードバランサーは使用していませんが、従来のロードバランサーはWebSocketをサポートしていません。

2. DjangoChannels2をすでに実行しているDjangoアプリケーションがローカルで稼働中です。

3. 外部Redisインスタンスがあります（EBインスタンスからアクセスできれば、何でもかまいません）。

4. 最後に、すでにEBコマンドラインインターフェイス（CLI）がインストールされています。インストールされていない場合は、<a href="https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/eb-cli3-install.html" target="_blank">こちら</a> の手順に従ってください。


<h3 id="deployment" class="anchor-link">アプリケーションのデプロイ</h3>
セットアップを確認したら、デプロイしましょう！.ebextensionsフォルダーがまだない場合は、ルートディレクトリに作成してください。
その中に `01_<your_custom_name>.config` という構成ファイルを作成し、下記のテキストを貼り付けてください。

    option_settings:
        aws:elbv2:listener:80:
            DefaultProcess: http
            ListenerEnabled: 'true'
            Protocol: HTTP
            Rules: ws
        aws:elbv2:listenerrule:ws:
            PathPatterns: /ws/*
            Process: websocket
            Priority: 1
        aws:elasticbeanstalk:environment:process:http:
            Port: '80'
            Protocol: HTTP
        aws:elasticbeanstalk:environment:process:websocket:
            Port: '5000'
            Protocol: HTTP


これで、ALBにポート80に従うように指示 し、パスが `/ws/*` のパターンで入ってくる場合に、EB下のインスタンスのポート5000に要求を渡すことになります。
ここでのポート5000はオプションであり、任意のポートを使用できますので、ご注意ください。
<a href="https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/command-options-general.html" target="_blank">ここで</a> で他のルールを検索することもできます。


次に、`Procfile`を使用し て プロセスを実行します。`Procfile`という名前のファイルを作成し、ルートディレクトリに保存して、以下のコードを貼り付けます。


    web: gunicorn --bind :8000 --workers 3 --threads 2 <your_app>.wsgi:application
    websocket: daphne -b 0.0.0.0 -p 5000 <your_app>.asgi:application


`<your_app>`が、ご自分のアプリケーションを指すように変更してください。
また、上記で行った構成ファイルではなく、ここで wsgi エントリポイントを構成していることにご注意ください。
最後に、バインドする daphne サーバーポートは、WebSocketからのリクエストを受信しますので、ALB構成ファイルで指定したポートにしてください。

Procfilesを使用したり、その他の方法にて、EBLinuxプラットフォームを拡張するには <a href="https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/platforms-linux-extend.html" target="_blank">こちら</a> や <a href="https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/python-configuration-procfile.html" target="_blank">こちら</a> も、参考になるでしょう。


<h3 id="using_https" class="anchor-link">https を使う</h3>
アプリケーションでhttpsを有効にしたら、`wss` 接続に従い、それに応じて渡すよう、構成ファイルを微調整してください。上記で作成した構成ファイルを、次のようにコード編集するだけです。


    option_settings:
        aws:elbv2:listener:80:
            DefaultProcess: http
            ListenerEnabled: 'true'
            Protocol: HTTP
            Rules: ws
        aws:elbv2:listener:443:
            ListenerEnabled: 'true'
            Protocol: HTTPS
            SSLCertificateArns: <YOUR ARN FROM AWS CERTIFICATES MANAGER>
            SSLPolicy: ELBSecurityPolicy-2016-08
            Rules: ws
        aws:elbv2:listenerrule:ws:
            PathPatterns: /ws/*
            Process: websocket
            Priority: 1
        aws:elasticbeanstalk:environment:process:http:
            Port: '80'
            Protocol: HTTP
        aws:elasticbeanstalk:environment:process:websocket:
            Port: '5000'
            Protocol: HTTP


これで、ポート443をまず採り上げてから、これまでと同様にEB内のインスタンスにWebSocket関連のパスを渡すようになりました。`<YOUR ARN FROM AWS CERTIFICATES MANAGER>` の部分は、必ず、承認済み証明書の、実際のarnリソースと置き換えてください。

これで完了です。このガイドがお役に立てば幸いです。


参考:

（英語サイト）[https://medium.com/@elspanishgeek/how-to-deploy-django-channels-2-x-on-aws-elastic-beanstalk-8621771d4ff0](https://medium.com/@elspanishgeek/how-to-deploy-django-channels-2-x-on-aws-elastic-beanstalk-8621771d4ff0)

[Elastic Beanstalk Linux アプリケーションを Amazon Linux 2 に移行する](https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/using-features.migration-al.html)

[EB CLI のインストール](https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/eb-cli3-install.html)

[すべての環境に対する汎用オプション](https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/command-options-general.html)

[Elastic Beanstalk Linux プラットフォームの拡張](https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/platforms-linux-extend.html)

[Procfile を使用した WSGI サーバーの設定](https://docs.aws.amazon.com/ja_jp/elasticbeanstalk/latest/dg/python-configuration-procfile.html)
