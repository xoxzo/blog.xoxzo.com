Title: Pythonでのインポート方法を理解する
Date: 2011-11-22 16:32
Author: Kamal Mustafa
Tags: python; インポート; 
Slug: understanding-python-import
Lang: ja
Summary: Pythonでのインポート方法の理解については、既に色々と書かれているため、本稿がお悩みの解消に役立つか、増大させるかは良く分からないが、前者であることを願う。


Pythonでのインポート方法の理解については、既に色々と書かれているため、本稿がお悩みの解消に役立つか、
増大させるかは良く分からないが、前者であることを願う。
Xoxzoでは、Pythonが初めての新入社員によって、これが再び問題となったのである。

Pythonには、他のモジュールをインポートする方法がいくつかあり、これらは effbot の
[Importing Python Modules](http://effbot.org/zone/import-confusion.htm)という記事(英文)で詳しく取り上げられている。
Python上のモジュールは、拡張子が.pyのファイル すべてである。このファイルを何らかの方法でPythonのインポート・パス上で利用可能にすれば
（これについては後述する）インポートすることができる。
モジュールの直近の概念として、パッケージがある。これは、モジュールの集合体であると考えることができるが、もっと簡単な定義がある。
つまり、`__init__.py` と名付けられたファイル（中身が空でもよい）を含むディレクトリは、パッケージである。

さて、pythonにおける最初のインポート方法は、`import`文であるが、これはモジュールまたはパッケージしかインポートすることができない。
例えば、`sugar` と名付けたモジュールがあるとしよう。

    $ touch sugar.py
    $ python
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sugar
    >>> sugar

これはかなり分かりやすいと思う。
`sugar.py` と名付けたファイルがあり、これを同じディレクトリ内で実行されたpython インタプリタからインポートすることができる。
もし、`sugar.py` 内に`is_sweet()`という関数があれば、これによって`sugar.is_sweet()`と参照することができる。
すると、次のようなことを試みたくなるかもしれない。

    >>> import sugar.is_sweet
    Traceback (most recent call last):
    File "<console>", line 1, in <module>
    ImportError: No module named is_sweet

エラーメッセージの通り、is_sweetと名付けられたモジュールは存在しない。
インポートできるのは、モジュール（またはパッケージ？）に限られていることを忘れてはならない。
一方、 `is_sweet` は関数なので、今のところかなり明確であることを願う。
でも何らかの理由により、モジュール全体ではなく、特定のオブジェクトだけインポートしたいこともあるだろう。
pythonで認められないとすれば、これで終わりなのだろうか？
幸い、pythonには、`from ... import` （個人的には、`from module|package import object`と説明するのが好きだが）という別のインポートの方法がある。
そこで、先ほどの例をそのまま利用すると、

    >>> from sugar import is_sweet
    >>> is_sweet
    <function is_sweet at 0xb731de9c>

こうすれば、`sugar` モジュールから`is_sweet` 関数をインポートすることができる。
つまり、`from module|package import object` の方法を利用すれば、モジュールから特定のオブジェクトをインポートすることができる。
なお、ここで「オブジェクト」という用語を利用したのは、pythonでは全てがオブジェクトであるからである。
モジュールも、パッケージも、関数も、クラスも、何でもオブジェクトである。
さて、ここで先ほどのsugar モジュールをパッケージとして再編してみよう。

    $ mkdir sugar
    $ touch sugar/__init__.py
    $ touch sugar/white.py

ここでは、`sugar` パッケージに`white` と名付けたモジュールを新たに追加した。このwhite モジュールのみインポートするためには、次のような方法がある。

    >>> import sugar.white
    >>> sugar.white
    <module 'sugar.white' from 'sugar/white.pyc'>

もしくは

    >>> from sugar import white
    >>> white
    <module 'sugar.white' from 'sugar/white.pyc'>

次のフレーズを頭の中で何回か繰り返してみよう。`from module|package import object` 
（英語では、モジュールまたはパッケージから（from）、オブジェクトをインポートできる）。
繰り返しになるが、Pythonでは何でもオブジェクトである。


Importパス
-----------

importの仕組みを（願わくば）理解できた所で、別の疑問が出てきた。
これらのモジュールをどこで探せばいいかPythonはどうしたら分かるか？
モジュールをインポートしようとする時、Pythonはパスのリストを調べる。
リストは `sys` モジュールの下に置かれ、`sys.path`として参照できる。

    >>> import sys
    >>> sys.path
    ['',
    '/home/kamal/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg',
    '/home/kamal/lib/python2.6/site-packages/pip-1.0.1-py2.6.egg',
    '/home/kamal/lib/python2.6/site-packages/patu-0.1-py2.6.egg',
    '/home/kamal/lib/python2.6/site-packages/lxml-2.3-py2.6-linux-i686.egg',
    ......

Pythonは、意図するモジュールが見つけられるようにするためのパスのリストを修正する方法を、いくつも提供している。
PYTHONPATHという名の環境変数を指定するのはその一つである。

    PYTHONPATH=/home/kamal/my-python-lib

今後はその環境からPythonを実行すれば `/home/kamal/my-python-lib` 下のどの `*.py` ファイルもインポートされることができる。
もう一つの方法は直接  `sys.path` を修正することだが、アプリケーションの最初のブートストラップコードで行えるため、この方が便利である。


[続きはこちらからお読みいただけます](https://blog.xoxzo.com/ja/2017/06/21/understanding-python-import-1/)

[関連記事もどうぞ](https://blog.xoxzo.com/ja/2017/06/19/about-python-import/)
