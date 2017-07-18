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
 
So for each of the arguments, you need to check first if the argument was prefixed with a `--` character and treat it differently. 
At this point, you realize that you have start to write a command line parser !

On most unix like environment, like Linux, there's a little command called `getopts`. There's also similar command which exists earlier 
called `getopt` (notice what is the difference ?), but you should just assume there's `getopts` and forget that `getopt` ever existed.
 While better than `getopt`, parsing cli arguments with `getopts` still not a fun exercise. Example of `getopts` is like below:-

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

At this point, we know that parsing command line arguments using traditional tool like `getopts` is not fun at all. And as I don't write much shell script these days, I prefer to start looking into how parsing command line in Python look like. It turn out that Python also has a module named [getopt][2]. It look slightly easier than the unix tools, you can try it if you want.

Other than `getopt` module, Python also has a module called `optparse`. Parsing command line arguments with `optparse` look like this (taken from the [docs][3]):-

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

The file optional argument then can be accessed as `options.file`, and the `-q` parameter can be accessed as `options.quiet`, which would default to `False`. It way much better now. But `optparse` was deprecated since Python 3.2, so it's not a viable alternative anymore. In python 3, a new module was introduced called `argparse`. There's some debates on `optparse` vs `argparse` but I don't want to get into that.

What more interesting here is that we might has come to realization, that to write a cli program in much saner way, we need more high level tools than just `getopt`, `optparse` or `argparse`. This is where cli framework came into picture. Imagine if we can have a python program like this:-

```python
def do_something(param1, param2, flag=False):
    pass

if __name__ == '__main__':
    make_command(do_something)
```
And then automagically, we can have a cli like this:-

    ./myprogram param1 param2
    ./myprogram param1 param2 --flag
    ./myprogram --help
    Usage: <myprogram> [options]

    Options:
      -h, --help                show this help message and exit
      -f FLAG, --flag=Boolean   Default to False

And if we have more than one functions in the script, like:-

```python
def do_something(param1, param2, flag=False):
    pass

def do_another_thing(param1):
    pass

if __name__ == '__main__':
    make_command(do_something, do_another_thing)
```

And have a program like:-

    ./myprogram do_something param1 param2 --flag
    ./myprogram do_another_thing param1

That would be great, right ?

So the tools that I'm using most of the time is a package called [Baker][Baker], you can get it from PyPI. It might not be the best but at that time when I'm looking for this kind of tools (7 years ago), it seem the most suitable for what I need. If starting again at present day, I might choose [click][click].

Google also has similar tools called [Fire][Fire]. I used it for a while as it seem to be more powerful than Baker and also solve some issue I have with Baker. But then I realized it just doing too much. For example it automatically print out the return value from your command, and no option to disable it.

There are more tools available in Python and I think you can find some more I didn't mention here by just googling "python cli tools". Hopefully now you understand the need of these tools when writing your python script.

[1]:https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
[2]:https://docs.python.org/3.1/library/getopt.html
[3]:https://docs.python.org/3.4/library/optparse.html
[Baker]:https://pypi.python.org/pypi/Baker
[click]:http://click.pocoo.org/5/
[Fire]:https://github.com/google/python-fire
