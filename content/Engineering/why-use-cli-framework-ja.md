Title: なぜ、CLI フレームワークをつかうのか ?
Lang: ja
Date: 2017-07-18 12:00
Author: Kamal Mustafa
Tags: python, cli
Slug: why-use-cli-framework
Summary: コマンドラインアプリケーションをつくるための、いくつかのアプローチ方法の考察

コマンドラインスクリプトを作る時は、引数やパラメータをどのように処理する考えないといけません。
主な理由は、特定な値をスクリプトの中にハードコートすることは避けたいからです。
ディレクトリをまとめて削除するスクリプトを例に取ってみましょう。普通は次のように実行したいことでしょう

    ./delete-dirs.sh dir1 dir2 dir3 ...

このようにすれば、任意のディレクトリを削除することが可能です。
ディレクトリをスクリプトの中にハードコートしてしまうと、
別のディレクトリを消したい場合は、毎回スクリプトを編集しなければならなくなってしまいます。

上の例では、消したいディレクトリの数は３つでした。

一般的には、スクリプトへの引数は、値のリストとして渡されます。
一つ目の引数へアクセスする時は `$1` ２つ目は `$2` といった具合です。
数が決まっていない場合のために、 bash では `$@` という変数が用意されています。
ここではとてもシンプルです。しかし、例えば任意の数の引数に加えて、省略可能なフラグの処理を追加したい場合はどうすれば良いでしょうか？
次の例を見て下さい。

    ./delete-dirs.sh --confirm dir2 dir2 dir3 ...

それぞれの引数について、まず前に `--` が付いているかチェックし、もしそうであれば処理を分ける必要があります。
ここまで来ると、コマンドラインのパーサを書く必要性が理解できるでしょう。

大部分のUnixライクな環境には `getopts` という小さなコマンドがあります。
また、以前にはよく似たよコマンド　`getopt`　というものもありましたが、
（２つの違いに気が付きましたか？）
今となっては、`getopts` だけがあって、`getopt` がかつて存在していたことは忘れてしまっても良いでしょう。

 `getopts`は `getopt`より良くなったとは言え、コマンドラインパーサを書くのは、あまり楽しい作業ではありません。
 `getopts`　を使う例は次のようになります。
 
    while getopts "h?vf:" opt; do
        case "$opt" in
        h|\?)
            show_help
            exit 0
            ;;
        v)  verbose=1
            ;;
        f)  output_file=$OPTARG
            ;;
        esac
    done

詳しくは [Stackoverflow][1] を参照してください。

ここまでくると、伝統的な `getopts` のようなツールをつかって、コマンドライン引数を解析するのは、
全くもって、面白い作業ではないことがわかります。
最近は shell スクリプトを書く機会があまりないので、Python でコマンドラインを解析する方法に興味を持つようになりました。
Pythonには [getopt][2] というモジュールがあることがわかりました。これは Unix のツールをよりは少しだけ使いやすいので、
興味があれば試してみて下さい。

`getopt`モジュール以外にも、Pythonには` optparse`というモジュールがあります。
 `optparse`を使ってコマンドライン引数を解析すると、以下のようになります（[docs] [3]から引用）


```python
from optparse import OptionParser
[...]
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()
```
オプションパラメータ `file` は `options.file` で、`-q` パラメータは `options.quiet` （デフォルトの値は `False` ）でアクセスすることが可能です。
これでずっと良くなりましたが、`optparse`は　Python 3.2　から非推奨となりましたので、現在では有効な解決手段ではありません。
Python 3 から新しいモジュール　`argparse`　が導入されています。
 `optparse`と`argparse`のどちらがが良いかついては、議論があるのですが、ここではそこには立ち入りません。

ここまできて分かるのは、コマンドラインプログラムを、正しくつくるには
 `getopt` や `optparse` や `argparse`　よりもずっと高レベルのツールが必要だということです。
そこでコマンドラインフレームワークの登場です。
次のような Python プログラムを考えてみてください。
 

```python
def do_something(param1, param2, flag=False):
    pass

if __name__ == '__main__':
    make_command(do_something)
```

そして、それが魔法のように動きます。

And then automagically, we can have a cli like this:-

    ./myprogram param1 param2
    ./myprogram param1 param2 --flag
    ./myprogram --help
    Usage: <myprogram> [options]

    Options:
      -h, --help                show this help message and exit
      -f FLAG, --flag=Boolean   Default to False

そしてもし、スクリプトが２つ以上の機能をもつときは

```python
def do_something(param1, param2, flag=False):
    pass

def do_another_thing(param1):
    pass

if __name__ == '__main__':
    make_command(do_something, do_another_thing)
```

そして、そのプログラムは次のように使えまたら

    ./myprogram do_something param1 param2 --flag
    ./myprogram do_another_thing param1

とても凄いと思いませんか？

そこで私は、ほとんどの場合、[Baker][Baker]というパッケージを使っています。これはPyPIから入手可能です。これは現在では最良の選択ではないかもしれませんが、
私がこのようなツールを探していた時点（７年前）では、やりたい事にもっとも適したツールと思えました。
もし、今日の時点で探すなら、[click][click]を選ぶかもしれません。

Googleも似たようなツール[Fire][Fire]を持っています。これはしばらく使ってみましたが、Bakerより強力であり、Bakerが持っていた問題点が解決されていました。
しかし、コマンドの戻り値が自動的に表示されてしまい、またその機能を無効化するオプションが無いなど、少しやり過ぎの面も感じました。

世の中には、もっと沢山の Python ツールがあります。"python cli tools"でググってみれば、ここでで触れなかったツールがもっと見つかるでしょう。
Pythonスクリプトを書くときに、このようなツールの必要性がわかって頂ければ幸いです。

[1]:https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
[2]:https://docs.python.org/3.1/library/getopt.html
[3]:https://docs.python.org/3.4/library/optparse.html
[Baker]:https://pypi.python.org/pypi/Baker
[click]:http://click.pocoo.org/5/
[Fire]:https://github.com/google/python-fire
