Title:遅延評価の威力
Date: 2017/12/25
Author: Akira Nonaka
Tags: python; lazy evaluation; delayed evaluation
Slug: about-lazy-evaluation
Lang: ja
Summary: 遅延評価の効能について紹介します

みなさん、遅延評価という言葉をお聞きになったことがあるでしょうか？

以下のコードを見てください。1億回のループですが、実際は i == 0 のときにループから抜け出しているので一回しかループは回りません。

```
$ cat lazy_evaluation.py

import time

start_time = time.time()

for i in range(0,10**8):
    if i == 0:
        break

end_time = time.time()

print end_time - start_time
```

これをpython2.7で実行してみます。

```
$ python2.7 lazy_evaluation.py
4.24918317795

```
私のMacBookでは４秒ほど時間がかかりました。

同じコードをPython3.6で実行してみます。(print文だけは直して下さいね)

```
$ python3.6 lazy_evaluation.py
5.0067901611328125e-06
```

こんどは一瞬(百万分の５秒)でおわりました。この差はどこから来るのでしょうか？

python2ではforループ内部の実行が行われる前に、range()が実行され、長さ１億の整数のリストがあらかじめメモリ上に作られます。
これはforループの実行前に行われるので、上に掲げた極端な例のような場合、range()が行なったしごとの大部分は、使われず無駄になってしまいます。

プログラムのシンプルさを保ちつつ、不要な計算をなるべく少なくしたいという要求を満たすため、コンピュータサイエンスの世界では遅延評価というしくみが考案されました。
Python3でのrange()関数にはこの思想が反映されています。
実際に値が必要となるまで、計算が行われないのです。
「遅延評価」「Python」というキーワードで検索してみると、色々面白い事が発見できると思います。
