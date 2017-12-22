Title: Pythonでのインポート方法を理解する(其の二)
Date: 2017/06/21 09:52
Author: Kamal Mustafa
Tags: python; import; sys.path;
Slug: understanding-python-import-1
Lang: ja
Summary: Python インポートに使う search path について、もう少し説明します。

モジュールやパッケージにおけるインポートの失敗が、Pythonプログラマーが直面する一番の問題です。
非常によく見られるので、Pythonのエキスパートになるために必要な知識の80%は、Pythonのこの部分を理解することであると言えます。

Pythonのインポートのメカニズムは実のところとてもシンプルなものです（[黒魔術][lucumr]を伴うからではありません）。
とりあえず、黒魔術なんて存在しないつもりになりましょう。Pythonにおけるインポートに影響するのはたった２つしかありません。


```
PYTHONPATH
sys.path
```

後者は前者の上に構築されています。なので、あなたが一部のモジュールまたはパッケージをインポートできない時
（モジュールとパッケージの違いはご存知ですよね？）この2箇所をチェックしてください。
または、もしインポートの振舞いを変更したい場合、これもあなたがいじりたい2ヶ所です。

デフォルトで、 `sys.path`は一連のエントリーで埋められています。例えば、ubuntu 14.04上では

```
>>> import sys
>>> sys.path
['', '/home/kamal/.local/lib/python3.4/site-packages/Baker-1.3-py3.4.egg', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/home/kamal/.local/lib/python3.4/site-packages', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
>>> len(sys.path)
9
```

どのパスがsys.pathに追加されるかは、あなたがPythonを立ち上げる時に自動でインポートされる `site` モジュールによって大きく影響されます。
`python -S` を使うことで私達はこれを抑圧することができます。こちらがこのフラグを使用した時の画面です

```
>>> import sys
>>> sys.path
['', '/usr/lib/python3.4/', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload']
```

最初のよりかなりを見て取れます。この sys.pathのデフォルトのエントリーは通常スタンダードライブラリーの場所です。
これこそが `import os`, `import json` が動作する理由です。
スタンダードライブラリーへのパスはバイナリにハードコードされているように見受けられ、 sys.prefix + 'lib' + sys.versionという組み合わせを利用しているのかも知れません。

なので、繰り返しますが、何らかのモジュール（またはパッケージ）をインポートできない時チェックすべき場所はここです。 
buildoutを利用して、更に一歩先に行く事ができます。 
[buildout]はsys.pathを再構築し、全てのパスをeggsディレクトリに追加するので、あなたがインポートしたいパッケージがそこにあるかどうかが確実にわかり、
インポートできない原因が明らかにできるのです。

願わくば、本記事を読んだ後、あなたがもうPythonでのモジュールのインポートに苦慮することがなければ良いと思います。
あるいはまだ問題がある場合、少なくともどこを当たればいいか、分かっているといいですよね。

[参照 URL](https://docs.python.org/3/library/sys.html?highlight=sys.path#sys.path)
[lucumr]:http://lucumr.pocoo.org/2011/9/21/python-import-blackbox/
[buildout]:http://www.buildout.org/
