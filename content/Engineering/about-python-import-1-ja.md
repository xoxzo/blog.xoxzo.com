Title: Pythonのimportについて
Date: 2017/06/19 14:00
Author: Akira Nonaka
Tags: python; import
Slug: about-python-import
Lang: ja
Summary: Pythonのimportのサーチパスに関する話題

Pythonプログラマがしばしば遭遇する問題に、`import` したいモジュールやパッケージが見つからないというものがあります。

```
>>> import foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'foo'
```
この問題の解決の第一歩は、Pythonインタプリタが
Pythonインタプリタがインポートするモジュールやパッケージを探す場所は `sys.path` という変数に
格納されているということを理解することです。
この変数の形式はリストです。

例えば、私の手元にある `Ubuntu 14.04` では
```
$ /usr/bin/python3
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', 
    '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages',
     '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
>>> print(len(sys.path))
7
```
となります。`sys.path` に含まれるパスは デフォルトでロードされる `site` というパッケージに大きく影響されます。
Pythonインタプリタ起動時に、`-S`というオプションを付けると、`site` パッケージをロードしないようにできます。
手動で `site` を `import` してみると `sys.path` の中身が増えているのがわかります。

```
$ /usr/bin/python3 -S
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python3.4/', '/usr/lib/python3.4/plat-x86_64-linux-gnu', 
    '/usr/lib/python3.4/lib-dynload']
>>> print(len(sys.path))
4
>>> import site
>>> print(len(sys.path))
7
```

sys.path[0]、つまりこのリストの先頭にはPythonインタプリタを起動するときに与えられたPythonスクリプト
のディレクトリが入ります。つまり起動したスクリプトのあるディレクトリは、`import`の検索対象になります。
Pythonインタプリタが対話的に起動された場合、sys.path[0]は空です。これはカレントディレクトリを意味します。

環境変数 `PYTHONPATH` の値は、起動時に sys.path に挿入されます。
ただし、挿入される場所は sys.path[0] の直後である点に注意しましょう。

```
$ export PYTHONPATH="/foo/bar/baz"
$ /usr/bin/python3
>> import sys
>>> print(sys.path)
['', '/foo/bar/baz', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', 
    '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', 
    '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
```

sys.pathは変更可能です。たとえば以下のようにして、Pythonスクリプトの中から、
任意のディレクトリを、importのサーチパスに追加することができます。

```
sys.path[0:0]=['/my/python/dir']
 print(sys.path)
['/my/python/dir', '', '/foo/bar/baz', '/usr/lib/python3.4', ...
```

[参考URL](https://docs.python.org/3/library/sys.html?highlight=sys.path#sys.path)