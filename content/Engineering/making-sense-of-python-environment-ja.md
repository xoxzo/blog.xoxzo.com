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

So my `python` program actually coming from `/usr/bin/python`. You can see that `/usr/bin` was in the list of directories in my `PATH` above. Because my `python` is in the `PATH`, that mean I can simply type `python` to execute it. But you can still execute any command even though it's not in the PATH. In this case you have to type the full path to the command, such as:-
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

In practice, you should never use `python` to run your python code. That `python` is [not for you](https://dev.to/k4ml/system-python-is-not-for-you-e4g). It is called system python and that because your OS system (I'm talking about Linux like Ubuntu here) also use python a lot to manage the system. They have lot of python program so they need `python` to run it.
実際に、pythonコードを実行の際、絶対に `python` を使用しないでください。`python` は [あなたのためになりません](https://dev.to/k4ml/system-python-is-not-for-you-e4g)。
これはシステムpythonと呼ばれ、OSシステム（ここではUbuntuのようなLinuxについて話しています）も、pythonを頻繁に使用してシステムを管理しているためです。
たくさんのpythonプログラムがあるため、実行するには `python` が必要なのです。

## venv

In python3, a module called `venv` is included by default. This is actually coming from a module called `virtualenv` back in Python2 days. On Ubuntu you still need to install it with `sudo apt install python3-venv`. This allow you to create a separate python environment:-

    python3 -mvenv myenv

This basically create a new copy of python in `myenv` directory. You can see in the directory something like:-

```
ls myenv/
bin  include  lib  lib64  pyvenv.cfg  share
```

You can even create this [manually](https://dev.to/k4ml/python-diy-virtualenv-5e4j) if you want. You'll see there's another "python" in `myenv/bin/python`. This is the "python" that you should use. You can run it as "myenv/bin/python". You'll also notice pip also included by default, so you can run it as "myenv/bin/pip" to install new packages. Many tutorials related to venv will suggest that you run the following command next:-

```
source myenv/bin/activate
```
That basically allow you to just type "python" and it will use `myenv/bin/python`. I would advice against this, at least not in the beginning.

When you install some packages like `myenv/bin/pip install requests`, the packages will be "installed" to `myenv/lib/site-packages` directory. You can verify this from python console:-

```
myenv/bin/python
>>> import requests
>>> requests
<module 'requests' from '/home/ubuntu/myenv/lib/python3.6/site-packages/requests/__init__.py'>
```
Your actual path of course will look different than mine.

So that's the second lesson - always use venv to create a separate environment for your project. In practice, each project will have it's own venv.

There are 2 situations actually when you want to use venv:-

1. For your programming project. As mentioned above, always create separate vm for each project. As you're progressing, you might feel that having to manage all this manually is cumbersome. You're not wrong to feel that. These days, I'm using [poetry](https://python-poetry.org/) most of the time to manage my project's venv. Let's delve into poetry in the next article, hopefully. There's also pipenv in the same space.
2. For installing program/application written in python. In this situation, also always create venv before installing the program. For example, if you want to install youtube-dl, do:-

    python -mvenv venv
    venv/bin/pip install youtube-dl
    venv/bin/youtube-dl

Similar to using venv in project, having to create new venv everytime you want to install new program also will start becoming cumbersome. These days, I'm using pipx to handle this.

    pipx install youtube-dl

`pipx` will install it to `$HOME/.local` directory where the executable `youtube-dl` will be placed in `$HOME/.local/bin`. Just make sure that directory is in your `$PATH`.

Another alternative is to use `--user` flag to `pip` which will also install the package to `$HOME/.local` dir but with pipx I no longer use that.

## pyenv

So we have done  with venv, what about pyenv? Most of the time you don't really need this. You'll need pyenv in the following situation:-

1. Your system doesn't has python version that you want. For example, your system only has python3.4 but you want to use python3.7. In this case you can get python3.7 through pyenv. But as I'm on Ubuntu most of the time, I prefer to use deadsnake/ppa instead to get python version that I need.
2. You need to use multiple version of python. For example your project must be tested against python2.7, python3.4, python3.6, python3.7 and python3.8. In this situation, pyenv can be helpful.


In short, pyenv give you different version of python. But do you still need venv if you already use pyenv? In general yes. As we can see above, pyenv only give different version of python. Back to lesson #2 above, you should always use separate venv for your project. The different is that now the python that will be used to create the venv "probably" come from pyenv instead of the system python. I put "probably" in quote because you have to be very certain here. So go back to the first lesson. This is one area that trip many people off. They don't really know which python they're using, once they have started using pyenv.

## Summary
We have come to an end and hopefully you have better idea now how to setup your python environment. Let's recap what we have learned so far:-

1. Always make sure you know which python you're currently using. Check, re-check and double check again, always. Follow the path mentioned in the error message that should bring you to the actual python being used.
2. Always use separate venv for each of your project or application that you want to install.
3. You might want to use multiple versions of python. In this case you can use pyenv, or deadsnake ppa if you're on ubuntu.

Till we meet again, happy coding.

## Updates

I noticed that `get-pip.py` script now by default will install to your local dir. Yeay!

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
