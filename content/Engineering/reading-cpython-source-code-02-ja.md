Title: CPythonの構文解析入門 -- CPythonのソースコードを読む(2)
Date: 2021-06-10
Author: Akira Nonaka
Tags: CPython, python, C
Slug: reading-cpython-source-code-02
Lang: ja
Summary: CPythonのソースコードを読むの２回目。構文解析のしくみを調べてみます。

##最初の一歩

CPythonのソースコード[^1]を読むの２回目です。今回は構文解析の部分を読んでみます。
Pythonのプログラムが実行されるまでには、ざっくりと次のような処理が走ります。

- ソースプログラムのテキストがトークンという単位に分解される（字句解析）
- トークンの並びが、抽象構文木に変換される（構文解析）
- 抽象構文木がバイトコードに変換される（コンパイル）
- バイトコードが実行される

CPythonの構文解析は `Parser/parser.c` というプログラムが行っていますが、これは実は、人が書いたプログラムではありません。このファイルの先頭行は以下のようにコメントが書かれています。

```
// @generated by pegen.py from ./Grammar/python.gram
```
つまり`pegen`というプログラムが`python.gram`という、Pythonの文法を定義したファイルを読み込んで、
それを元に、構文解析をして抽象構文木を生成するプログラム `parser.c` を生成したという事になります。
以下にgithub上のソースコードへのリンクを張っておきます。

- [構文解析生成器 pegenパッケージ](https://github.com/python/cpython/tree/3.10/Tools/peg_generator/pegen)
- [入力ファイル python.gram](https://github.com/python/cpython/blob/3.10/Grammar/python.gram)
- [出力ファイル parser.c](https://github.com/python/cpython/blob/3.10/Parser/parser.c)

##ちょっとした実験

ここで簡単な実験をしてみましょう。`python.gram`を編集して、１行追加します。
```
sum[expr_ty]:
    | a=sum '+' b=term { _PyAST_BinOp(a, Add, b, EXTRA) }
    | a=sum 'akira' b=term { _PyAST_BinOp(a, Add, b, EXTRA) } <---この行を追加
```
文法定義に `akira` というキーワードを追加して、それに `+`（足し算）と同じ抽象構文構文要素を割り当てています。

次に `parser.c` を再生成します。
```
$ make regen-pegen
PYTHONPATH=./Tools/peg_generator python3 -m pegen -q c \
		./Grammar/python.gram \
		./Grammar/Tokens \
		-o ./Parser/parser.new.c
python3 ./Tools/scripts/update_file.py ./Parser/parser.c ./Parser/parser.new.c
```
最後に新しい構文解析器をインタプリタに組み込みます。
```
$ make
```
出来上がった pythonを実行して、確かに文法が変わったかチェックしてみましょう。
```
$ ./python.exe

Python 3.10.0a7+ (heads/fix-comment-in-parser-dot-c-dirty:3fe21444e7, Jun  8 2021, 15:18:08) [Clang 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 10 akira 20
30
>>> 10 akira 20 akira 30
60
>>> 10 akira 3 * 2
16
>>> akira = 99
  File "<stdin>", line 1
    akira = 99  <--- akiraはキーワードなので代入できない
    ^^^^^
SyntaxError: invalid syntax
```
このように、Pythonに新しいキーワード `akira` が追加され、２項演算子 `+` と同じ動作をしているのがわかります。

##この先へ

この例では、既存の文法要素に関する、新たなキーワードを追加してみただけなので、簡単にできましたが、本格的に文法を拡張しようとすると、もう少し手を動かさないといけません。すなわち

- 具象構文の定義
- 新しいトークンの追加
- 対応する抽象構文要素の変更
- コンパイラの変更（抽象構文をどのようなバイトコードにコンパイルするか）

などです。[デベロッパーガイド](https://devguide.python.org/grammar/)
はここにありますので参考にしてみてください。

[^1]: この記事ではCPythonのバージョン3.10のソースコードを前提にしています。構文解析の部分は3.9で大幅に書き換えられました。3.9では新旧の構文解析器が共存していて、コマンドラインスイッチで切り替えることができます。このためソースコードがごちゃごちゃしていて、ちょっと読みにくいです。3.10では古い構文解析器のソースコードは綺麗に消されているので、ずっと読みやすくなりました。
