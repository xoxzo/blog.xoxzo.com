Title: Xoxzoの働き方と環境をご紹介
Date: 2018-09-28 14:00
Author: Zaki Akhmad
Tags: 環境; 仕事; ツール; python; zsh; vscode; チームキャンプ;
Slug: sharing-our-working-environment
Lang: ja
Summary: 生産力向上のため、チームキャンプでメンバーの仕事環境を覗いてみました。

2018年7月、[チームキャンプ](https://blog.xoxzo.com/tag/team-camp/)がありました。
今回は、クアラルンプールです。Xoxzoは、[100％リモートワーク](https://info.xoxzo.com/ja/aboutus/)の会社なので、
同僚と一緒の場所で顔を合わせて仕事ができる時間は、いつも面白くて盛り上がります。

![KL team camp 2018](/images/kl-team-camp-2018.jpg)

Xoxzoでは、自分のローカル環境へソースコードをダウンロードしない、というポリシーがあります。
このポリシーに従えば、どのように働くか、という決まりはまったくなく、自由に仕事をしていいのです。

みな、働き方が違います。私達の中でも、テキストエディタで仕事をするのを好む人、
もう、ターミナルでは生きていけなくなった、という人もいます。

チームキャンプ中のあるセションで、働き方の共有をしました。
仕事場はどんな風か、生産性向上のために、ツールの設定をどうしているのか、などです。

例えば、私は、自分の vim 上で、[PEP8](https://www.python.org/dev/peps/pep-0008/) コンプライアンス用のコードを
どのように [vim-flake8](https://github.com/nvie/vim-flake8) を使って
自動的にチェックしているかを共有しました。Pythonのファイルを保存するたびに、flake8 が自動的に下記の事柄をチェックするのです。

* 不使用だが重要なモジュール
* 不使用の変数
* シンタックス・エラー
* スペースの提案
* 改行の提案

例を挙げると、私がこんなPython ソースコードを書きます。
```
1 #!/usr/bin/python
2
3 from datetime import datetime
4
5 import django
6
7
8 now = datetime.now()
9 yesterday = timedelta(days=1)
10
11
```

そして、 :wq とタイプします。（保存して vim を終了する) すると vim は、警告を出します。
```
1 example.py|5 col 1| F401 'django' imported but unused
2 example.py|9 col 13| F821 undefined name 'timedelta'
3 example.py|11 col 1| W391 blank line at end of file
```

一行一行、目を凝らし、手動で上記のエラーのチェックをする必要がない分、
これは全くの生産性向上だと思っています。

そうしたら、友人たちは、Microsoft Visual Studio のコードを使ってできることを、
例えば、違いの比較だとか、commits する方法とか、シンタックスエラーをチェックすること
なんかを、たくさん教えてくれました。
最近では、[GNU/Linux](https://code.visualstudio.com/docs/setup/linux)　を含む、Windowsでない環境下でも、
 VS コードが使えるんです。
 
シェルに関しては、チームの一人が、zsh を見せてくれました。
私は、従来の bash shell から zsh へ変えようか、と興味を持っていたところでした。
zsh には、[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)と呼ばれる、人気のフレームワークがあるんです。

プラグインのコレクションも、たくさんあります。
気づいたのは、zsh では、ブランチ名を全部タイプしなくても、ブランチをチェックアウトできる
ということでした。
キーワードをタイプするだけで、zsh が探してきてくれるんです。
例えば、

```
$ git checkout -b PROJECT-123-update-readme
$ git checkout master

# Just type the keyword of the branch name and press tab
$ git checkout 123
# zsh will find it for you

$ git checkout PROJECT-123-update-readme
```

フロントエンドの仕事ぶりを見る機会もありました。
私が日々やっている仕事とは、全く違いました。アイコン、ワイヤーフレームを作成して、それをコードを使って
実行するツールなど、バックエンドエンジニアとして、私が見たことも触ったこともないところを、
見せてくれました。

これまで、私はかなり長い間、テキストエディタと、bash を使ってきました。
そこで今、考えています。IDEテキストエディタと zsh を使ってみようかな、と。
_いつだって、新しいことにチャレンジする余地はあるものです、よね？_
