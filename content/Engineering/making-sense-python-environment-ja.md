Title: python 環境を 「なるほど」と理解する
Date: 2020-05-09 12:00
Slug: making-sense-python-environment
Lang: ja
Tags: python; venv; virtualenv; pyenv; conda
Author: Kamal Mustafa
Thumbnail: /images/python-env.png
Summary: python の開発環境の設定時に必要なツールを全て理解しましょう。 Venv、 pip、 pyenv について述べます。

python環境の設定に多数のツールを必要とすることは、pythonの初心者の間では[冗談](https://xkcd.com/1987/)のように言われています。 virtualenv、venv、pip、pyenv、condaなどについて聞いたことがあると思います。

個人的にはJSランドと比べると、それほど悪くはないと思っていますが、これが初心者にとって圧倒的である理由は、容易に察するところです!

実際、pythonでコーディングを始めたいだけなら、こういったツールが全部必要かというとそうではありません。
始める時には、pythonインタープリターさえあれば十分なのです。
しかしもちろん、標準ライブラリだけで完全な（または十分に楽しい）プログラミング言語なんてありません。
遅かれ早かれ、ホイールを再構築するのを避けるため、他人のコードを入手する必要に迫られるでしょう。

PYTHONPATH（pythonプログラマーは絶対 [知っておくべき](https://blog.xoxzo.com/2017/06/21/understanding-python-import-1/)だと思っています）を理解している限り、
単純なモジュールだとかパッケージの取得は、手動で行うことができますが、その他のパッケージをさらに取得するには、なんらかの自動化が必要になってきます。


pythonランドでは、サードパーティパッケージはほとんど、PyPI（Python Package Index）にあります。
PyPIからパッケージを見つけてインストールする時、標準ツールはpipですが、他のツールもあります。システムにpythonを取り入れる方法によっては、すでにプレインストールされていることもあります。しかし、pythonにない場合は、次の方法でインストールできます。

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

そうすれば、PyPIからのパッケージのインストールは次のように簡単なのです。

    pip install <packagename>

シンプルに見えますが、初心者はこの時点ですでに多くの問題に直面しています。
問題は、上記のpipをインストールするために使用されるコマンドの `python` は、どこかから来ている必要があるということです。
チュートリアルの多くは、`python` はそこに存在すると想定していて、ほとんどの場合、存在するものです。
しかし、そこにあるとしても、必ずしもあなたが必要な「python」であるとは限らないのです。

Linuxシステム上では、コマンド `python` （またはそれに関する任意のコマンド）を入力するとき、そのコマンドを実行するシェルは、どこだかを探す必要があります。
コマンドを探す場所は、`PATH`と呼ばれる環境変数で定義されます。これは基本的に、シェルが実行するコマンドを探すディレクトリのリストです。以下は私のシステムのPATH値の例です。

```
echo $PATH
/home/kamal/.poetry/bin:/home/kamal/.cargo/bin:/home/kamal/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/home/kamal/.local/share/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/var/lib/snapd/snap/bin
```

上記は、シェルが `/home/kamal/.poetry/bin/`から`/var/lib/snapd/snap/bin` まで検索を開始する、ということを意味します。
コマンドが見つかると、検索は停止します。
リストの最後のディレクトリまでコマンドが見つからない場合は、「command not found (コマンドが見つかりません)」というエラーまたは同等のエラーが表示されます。

では、python はどこから来るのでしょうか？それはシステムによって異なります。例えば、私のシステム上では

```
which python
/usr/bin/python
```

ということで、私の `python` プログラムは、実際には `/usr/bin/python`　から来ているのです。
`/usr/bin` が上記の私の `PATH` のディレクトリのリストにあったことがわかるでしょう。
私の `python` が `PATH` 内にあるのですから、単に `python` と入力すれば実行できることを意味しています。
ただし、`PATH` に含まれていなくても、任意のコマンドを実行できるのです。
その場合、次のようにコマンドへのフルパスを入力する必要があります。

    /opt/my-python-installed-manually/3.8/bin/python

しかし、毎度このように入力しなければならないなんて、おかしいですよね？そのため、誰もが　`python` のみのような短いバージョンを使用したいと考えています。

短いバージョンにおける問題は、それがどのように機能するかを理解していない人がほとんどで、忘れたり混乱したりしやすいことです。
実際には `/usr/bin`からのものであるのに、`/opt/my-python-installed-manually/3.8/bin` からのものであるかのように「python」と入力してしまうのです。

ということで、第一課 - あなたの python とそのルートを知る。後々、多くのトラブルを回避できるはずです。

上記のpipのインストールに戻りましょう。
`pythonget-pip.py`を実行すると、使用される `python` は`/usr/bin/python`　から来ている可能性があります。
デフォルトでは、pythonはパッケージをpythonインタープリター自体に関連するディレクトリに配置します。
この場合は `/usr/lib/python3.7/site-packages` になります。
バージョン番号は、`python3.7`ですが、あなたの使用する `python` のバージョンによって異なります。
問題は、`/usr/lib/` への書き込みには管理者権限が必要になることです。
コマンドを `sudo`で実行する提案する人もいるでしょう。実は、良くないアドバイスです。
インストールしようとしている pythonパッケージはどんな任意のコードでも実行でき、ある程度の検証が行われるOSパッケージとは異なり、PyPIにアップロードされたパッケージは、誰も検証していません。
誰でも、良くても悪くても、悪意があるかどうかにかかわらず、PyPIにコードをアップロードできるのです。

実際に、pythonコードを実行の際、絶対に `python` を使用しないでください。`python` は [あなたのためになりません](https://dev.to/k4ml/system-python-is-not-for-you-e4g)。
これはシステムpythonと呼ばれ、OSシステム（ここではUbuntuのようなLinuxについて話しています）も、pythonを頻繁に使用してシステムを管理しているためです。
たくさんのpythonプログラムがあるため、実行するには `python` が必要なのです。

## venv

python3には、`venv`というモジュールが デフォルト で含まれています。これは実際には、python2の時代に`virtualenv`と 呼ば れ たモジュールから来ています。
Ubuntuでは、`sudo apt install python3-venv`を使用してインストールする必要があります。これにより、別のpython環境を作成できるのです。

    python3 -mvenv myenv

ということは、基本的に、`myenv`ディレクトリに 新規 pythonのコピーを作成することになります。次のようなものを、ディレクトリに確認できるでしょう。

```
ls myenv/
bin  include  lib  lib64  pyvenv.cfg  share
```

必要に応じて、これを [手動で](https://dev.to/k4ml/python-diy-virtualenv-5e4j)作成することもできます。
`myenv/bin/python` に別の python があるでしょう。これが、あなたが使うべき "python" です。
"myenv/bin/python" として実行できるものです。また、pipもデフォルトで含まれているので、"myenv/bin/pip" として実行して新しいパッケージをインストールできます。
venv に関連するチュートリアルでは、たいてい、この後次のコマンドを実行することを勧めています。


```
source myenv/bin/activate
```
こうすると、基本的に "python" と入力するだけで、`myenv/bin/python` の方が使用されるのです。少なくとも最初のうちは、これには従わないように、アドバイスしたいと思います。

`myenv/bin/pip install requests` などのパッケージをインストールすると、パッケージは `myenv/lib/site-packages`というディレクトリに "インストール" されます。これは python コンソールから確認できます。

```
myenv/bin/python
>>> import requests
>>> requests
<module 'requests' from '/home/ubuntu/myenv/lib/python3.6/site-packages/requests/__init__.py'>
```
もちろん、実際のパスは 私のものとは異なっているでしょう。

ということで、第二課 - venvを常用し、プロジェクト用に別の環境を作成すること実際には、各プロジェクトには個別のvenvがあるものです。

実際にvenvを使用する場合、2つの状況が想定されます。

1.	ご自身のプログラミングプロジェクト用上記のように、プロジェクトごとに常に個別のvmを作成しましょう。進行するにつれて、こういったことすべてを手動で管理しなければならないのが面倒だと感じるかもしれません。そう感じても何もおかしくはありません。最近、私は プロジェクトのvenvを管理するのに、ほぼ常に [poetry](https://python-poetry.org/) を使用しています。うまくいけば、次の記事で poetry について掘り下げましょう。同じ場所に pipenv もあります。
2.	pythonで書かれたプログラム/アプリケーションのインストール用この場合、プログラムをインストールする前に必ずvenvを作成してください。たとえば、youtube-dlをインストールする場合は、次のようにします。

    python -mvenv venv
    venv/bin/pip install youtube-dl
    venv/bin/youtube-dl

プロジェクトでvenvを使用するのと同様に、新しいプログラムをインストールするたびに新しい venv を作成する必要がある、ということも、面倒になってくるでしょう。最近、私はこの処理に pipx を使用しています。

    pipx install youtube-dl

`pipx` は、実行可能な `youtube-dl`が `$HOME/.local/bin` に配置される`$HOME/.local` ディレクトリにインストールします。そのディレクトリが あなたの`$PATH`にあることを確認してください。

もう1つの方法は、`--user`フラグを `pip` に使用することです。これにより、パッケージを `$HOME/. local` ディレクトリにインストールしますが、pipx を使う現在では、使用しなくなりました。

## pyenv

venv はよしとして、pyenvはどうでしょうか？ほとんどの場合、これが必要になることはありません。pyenv が必要になるのは、次の状況です。

1. お使いのシステムに、使いたいバージョンの pythonがない場合たとえば、システムには python3.4しかありませんが、python3.7を使用したいとします。この場合、pyenvを介してpython3.7を取得できるのです。しかし、私はほとんどの場合Ubuntuを使用しているので、必要なpythonバージョンを取得する場合、deadsnake/ppaを代わりに使用するほうを好みます。
2. pythonの複数のバージョンを使用する必要がある場合。たとえば、あるプロジェクトで、python2.7、python3.4、python3.6、python3.7、および python3.8 に対してテストする必要があるとします。この場合、pyenv が役立ちます。

要するに、pyenv は異なるバージョンのpythonを提供してくれるのです。しかし、すでに pyenvを使用している場合でも、venv が必要でしょうか？まあ...一般的にはそうでしょう。上記のように、pyenv は異なるバージョンの python のみを提供します。第二課に戻ると、プロジェクトには常に個別の venv を使用する必要があります。違いは、venvを「おそらく」作成するために使用される pythonが、システムpythonではなくpyenvからのものになっていることです。この時点で、しっかり理解していただいている必要があるので、「おそらく」を引用符で囲んでいます。では、第一課に戻ってください。これが、多くの人がつまずくところなのです。pyenv の使用を開始してしまうと、使用している pythonが、よくわからなるのです。

## 概要
そろそろ終わりが近づいてきました。python環境を設定する方法について、より理解が深まってきていますか。これまでに学んだことをまとめてみましょう。

1. 使用中の python を常に確認しましょう。常に、確認し、再確認し、再度確認してください。エラーメッセージに記載されているパスをたどり、使用している pythonを探しましょう。
2. インストールするプロジェクトまたはアプリケーションごとに、常に個別のvenvを使用しましょう。
3. pythonの複数のバージョンを使用することがあるかもしれません。そんな時、pyenv、またはubuntuを使用している場合は deadsnake ppa を使用できます。

ではまた次回、 Happy coding!!

## 更新事項

現在、`get-pip.py` スクリプト がデフォルトでローカルディレクトリにインストールされることに気づきました。やった！

```
python get-pip.py
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Downloading pip-20.1-py2.py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 9.3 MB/s
Installing collected packages: pip
  WARNING: The scripts pip, pip2 and pip2.7 are installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```
