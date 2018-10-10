Title: Pychonでインスタンスからクラス属性へアクセスするには？
Date: 2018/10/10
Author: Akira Nonaka
Tags: python; class; instance; attribute
Slug: access-class-attributes
Lang: ja
Summary: Pythonで、インスタンスメソッドからクラス属性へアクセスする方法を解説します

インスタンスメソッドからクラス属性へアクセスする時の注意点を解説します。
インスタンスが作られるたびに、クラス属性 `coungter` を１つ増やしたいとします。
以下のようなコードを書いてみました。

```
class Foo:

    counter = 1000

    def __init__(self):
        print("Old counter:", self.counter)
        self.counter += 1
        print("New counter:", self.counter)


f = Foo()
print("Updated counter:", f.counter)

f = Foo()
print("Updated counter:", f.counter)

```

これを実行してみると以下のような出力が出ます。
```
Old counter: 1000
New counter: 1001
Updated counter: 1001
Old counter: 1000
New counter: 1001
Updated counter: 1001
```
期待していた結果と違います。
確かに、1000 が 1001 に更新されていますが、更新が蓄積されず新しいインスタンスが作られても、相変わらず Old counter の値は1000のままです。なぜこのようになるのでしょうか？

Pythonの言語仕様には次のように書かれています。
```
Class instances
(...)
A class instance has a namespace implemented as a dictionary which is 
the first place in which attribute references are searched.When an 
attribute is not found there, and the instance’s class has an attribute
by that name,the search continues with the class attributes.
(...)
``` 
つまり、インスタンスの属性を探して見つからなかった場合は、クラス属性が探されるというわけです。

`self.counter += 1`という文は `self.counter = self.counter + 1` の意味ですが、右辺ではクラス属性が参照され
ていますが、左辺では新しいインスタンス属性が定義されていることになります。
一見同じようなものに見えますが、実は違うものであったというわけですね。

インスタンスメソッドからクラス属性へアクセス（代入）するには `__class__` を経由することで可能になります。

```
        self.__class__.counter += 1
```
このように変更して実行すると
```
Old counter: 1000
New counter: 1001
Updated counter: 1001
Old counter: 1001
New counter: 1002
Updated counter: 1002
```
となり、期待していた結果が得られました。
