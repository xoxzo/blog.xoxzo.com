Title: Asizeof モジュールの使い方
Date: 2018-08-08 06:00
Author: Arthur Sultanbekov
Tags: asizeof; memory; tools; python; pympler;
Slug: asizeof-usage
Lang: ja
Summary: メモリの漏れを調べるために、asizeof を使います。

あなたのプログラムがメモリを食い始め、どこに問題があるかを調べようとすることがあります。
こんなとき役に立つ、さまざまなツールがあります。ここでは、 [Pympler](https://pythonhosted.org/Pympler/) lib
の、`asizeof` というシンプルなツールをご紹介したいと思います。

Pympler has 2 trackers to measure, monitor and analyze the memory behavior of
Python objects. These trackers are `muppy` and `Class Tracker`.
Pymplerには、Pythonオブジェクトのメモリ動作を測定、監視、分析するための2つのトラッカーがあります。 
 `muppy`と` Class Tracker`です。
これが、メモリの漏れを調べるのに、役立つのです。

純粋なPythonオブジェクトのサイズだけを返す、組み込みの `sys.getsizeof（）`というメソッドがあります。
例えば、このように使います。

```python
>>> import sys
>>> sys.getsizeof(None)
16
>>> sys.getsizeof([])
64
>>> sys.getsizeof('a')
50
>>> sys.getsizeof(['a'])
72
>>> sys.getsizeof(['avadakedavra'])
72
```

対照的に、 `asizeof.asizeof（）`は内部的な値を再帰的に検索し、
内部項目のサイズを含むオブジェクトの全体サイズを数えます。

```python
>>> from pympler import asizeof
>>> asizeof.asizeof(None)
16
>>> asizeof.asizeof([])
64
>>> asizeof.asizeof('a')
56
>>> asizeof.asizeof(['a'])
128
>>> asizeof.asizeof(['avadakedavra'])
136
```

スクリプト内の値の大きさを調べることで、 `asizeof`を使ってボトルネックを見つけることができるというわけです。
複雑で入り組んだスクリプトでは、もっと便利なツールが必要になるかもしれませんが、小さなスクリプトでは `asizeof`が便利です。


Asizeofは、どの変数が問題になるかを直感的に推測し、そのサイズを確認し、直感を確認するときに使用できます。
しかし、問題がどこにあるのか分からず、問題のあるコードが数十から数百行に及ぶ場合は、
すべての変数に `print（asizeof（）)`を書くことはできないので、メモリプロファイラを使うのが良いでしょう。

例:

```python
from pympler import asizeof

class Empty(object):
    pass

class Dummy(object):
    def __init__(self):
        self.a = ['apple', 'banana', ['foo', 'bar', ['tiger', 'leo']]]
        self.b = {'key1': 'val1', 'key2': 'val2'}
        self.c = bytearray(1024*1024*4)
        self.d = self


def investigated_function():
    sometuple = (4, 10, -2,)
    for i in range(1000):
        empty = Empty()
        dummy = Dummy()
        # do_something_with(dummy)
        
```


`investigated_function（）`を実行すると、メモリが消費され、問題がどこにあるか調べることになります。 
そうすると、値をチェックするだけです。例えば:

```python
print( asizeof.asizeof(sometuple) )
print( asizeof.asizeof(empty) )
print( asizeof.asizeof(dummy) )
168
152
4195944
```

and you can see that problem is in `dummy` instance, which is 4,195,944 bytes,
which is around 4Mb. Also you can use `asizeof.asizesof` function
(plural, "A Sizes Of"):
その問題が、4,195,944バイト（約4Mb）の`dummy`インスタンスにあることがわかります。 
また、 `asizeof.asizesof`(plural, "A Sizes Of") 関数を使うこともできます。

```python
print( asizeof.asizesof(dummy.a, dummy.b, dummy.c, dummy.d) )
# returns sizes of individual values
(592, 512, 4194368, 472)
```

上のコマンドから、 Dummyクラスの属性 `dummy.c`が、多くのメモリを使っていることがわかります。
is an attribute of Dummy class:

```python
self.c = bytearray(1024*1024*4)
```
