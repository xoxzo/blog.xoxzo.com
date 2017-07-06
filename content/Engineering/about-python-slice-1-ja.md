Title: スライス記法を理解するために
Date: 2017/07/03
Author: Akira Nonaka
Tags: python; slice; list; learning python series;
Slug: about-python-slice
Lang: ja
Summary:
 
Pythonのリストには、スライス記法という要素の指定方法があります。

```
>>> my_list = ['a','b','c','d','e']
>>> my_list[0:3]
['a', 'b', 'c']
```

`[0:3]`という指定をすると、0番から2番の要素が取り出されます。(要素の先頭は0番であることに注意)
ちょっと意外なのが3番の要素 `'d'` が含まれないということ。

これを理解するのに良い方法が [Python Tutorial](https://docs.python.jp/3/tutorial/index.html) の中で紹介されています。
具体的には[この部分](https://docs.python.jp/3/tutorial/introduction.html#strings)

スライス記法のインデックスは、要素そのものに振られているのでなく、要素の境界に対して振られているのと考えるのです。
つまり、リストの左端が0で、右にいくに従って1つずつ増え、右端がリストの長さと同じになります。
```
 +---+---+---+---+---+
 | a | b | c | d | e |
 +---+---+---+---+---+
 0   1   2   3   4   5
```
リストは変更可能なオブジェクトですので、スライス記法を使った代入も可能です。
以下の例は、リストの先頭の3つの要素を置き換える例です。
```
>>> my_list[0:3] = 'X'
>>> my_list
['X', 'd', 'e']
```
この考え方を進めれば、リストの先頭への挿入は
```
>>> my_list[0:0] = 'Y'
>>> my_list
['Y', 'X', 'd', 'e']
```
とすれば良いことや、リストの終わりへの追加が
```
>>> my_list[len(my_list):len(my_list)] = 'Z'
>>> my_list
['Y', 'X', 'd', 'e', 'Z']
```
でできることが容易にわかるのではないでしょうか？

蛇足ですが、`n:m`というスライス記法に関して、n、mは省略することが可能で、nが省略された場合にはn=0、mが省略された場合にはm=リストの長さ(終端)が指定されたとみなされます。
従って、
```
my_list[0:0] -> my_list[:0]

my_list[len(my_list):len(my_list)] -> my_list[len(my_list):]
```
と書くことも可能です。
