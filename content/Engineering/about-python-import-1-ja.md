Title: Pythonのimportについて
Date: 2017/06/19 14:00
Author: Akira Nonaka
Tags: python; import
Slug: about-python-import
Lang: ja
Summary: Pythonでimportを行ったとき、ModuleNotFoundErrorに出会ったときの調べ方について

Pythonプログラマがしばしば遭遇する問題に、import したときにモジュールやパッケージが見つからないというものがあります。

```
>>> import foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'foo'
```
この問題の解決の第一歩は、Pythonインタプリタが
Pythonインタプリタがインポートするモジュールやパッケージを探す場所は `sys.path` という変数に
リストとして格納されています。

例えば、手元の `Ubuntu 14.04` では
```
$ /usr/bin/python3
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
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
['', '/usr/lib/python3.4/', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload']
>>> print(len(sys.path))
4
>>> import site
>>> print(len(sys.path))
7
```

