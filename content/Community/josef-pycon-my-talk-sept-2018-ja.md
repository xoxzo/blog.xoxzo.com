Title: PyCon MY 2018 でのトーク – Pythonのトレーニングをどのようにスケールさせたか
Date: 2018-09-12 12:00 
Lang: ja
Author: Josef Monje
Tags: 2018; pycon; MY; training; jupyter;
Slug: python-talk-how-josef-made-trainings-scale
Summary: PyCon MY 2018 にて登壇し、Python のトレーニングを行った方法について話しました。

わたしが PyCon MY 2018で行ったトークに関してお話します。
[JennaのPyCon 2018 MY](https://blog.xoxzo.com/2018/09/05/pycon-my-2018/
)でも言及されていますが、役に立ちそうな補足となるといいと思っています。
PyCon MYでお話しした内容のいくつかを、ここでも読者の皆さんに共有しようと思います。

トークは技術的なものではなく、初心者にも分かりやすいものでした。
想定していた対象は教育者、技術グループや、トレーニングを運営している個人や組織などでした。
普段から仕事で使っていたり、交代要員や新規入社で一回トレーニングことがあるか、という感じでしょうか。
組織やコミュニティの一員として、だとすれば、知識共有のため、招かれたとか、参加権を振られたりしたのかもしれません。
誰しもが突然、何らかの理由で何かしらのトレーニングの必要に迫られることがあるでしょう。
参加者は無料か、自腹、または会社持ちの費用で来ているのかもしれません。
参加者がトレーニングに料金を支払う場合、人数が増える事はより多くの収益を意味します。
会社に大変革が起き、巨大な部屋に参加者を迎えて、なんてことがあるかもしれません。
準備しておくに越したことはありません。

何にせよ、柔軟性があることは参加者にとってよいことです。
より大きなグループでのチャレンジは、より問題が起こりやすい、と言うことです。
人が増えると質問も増え、エラーもより多く起きるということです。
中には、単に話について行くのにも時間がかかる、ということもあります。
そんな人がたまたま、あるイベントに沢山参加した、ということもあります。
グループが大きいほど管理は難しく、脱線しがちです。
これでは、大きなグループの参加者が質の高いトレーニングを受けられなくなるということです。
グループのサイズを大きくしたければ、届ける内容の価値にも同時に注意しなければならないのです。
スタートアップの世界や技術サークルなどで、いずれ誰かが「価値があるのか？」という疑問を持つことになります。

![Josef トーク]({filename}/images/pycon-my-2018/IMG_9595.JPG)

自分の経験から学んだことがあります。このことだけに限りませんが、
わたしはトレーニングのやり方を改善し、トレーニングの品質を保ちつつ、扱える参加者数を増やしていくことができました。
トレーニング経験から得た知見をまとめると、以下のようなものです。

•	より良いツール - その作業に適したツールを使うこと、という格言もあります
•	やり方を再考する - 利用するツールによって、作業方法を変えることが可能です
•	個人をエンパワーする - クラスを一つの単位で扱うかそれぞれの参加者単位で捉えるかで、違ってきます
•	双方向性は不可欠 - 社交的相互関係は、邪魔になるのではなく、助けになるのです


![Josef トーク]({filename}/images/pycon-my-2018/IMG_9612.JPG)

私の使うメインのツールはJupyter notebookです。これは教育用として素晴らしいと思います。多くの講演やデモに使われ、インタラクティブなコードスニペットと共に口述を行なっています。プログラミングを教えるのに使う場合には、最初から全てをタイプしたり、前の誰かの話を聞いたりする必要が無くなるので進行がスピーディーになります。参加者はコードをより快適に試すことができ、より早いフィードバックループが得られるのです。

クラスの運営の仕方という意味では、私のガイドに沿って、一歩一歩進められるnotebookのレポジトリを用意すること以外に、バグの取り扱いと問題の回避方法を参加者へ与える準備をします。こうするとより自信を持って学ぶことができるのです。私は簡単には壊れないけれど、もしものために、リセットボタンがあると言って安心させます。迷子になったり、何をすれば良いかわからないと彼らが感じることは無いようにします。ある時点で、参加者自身でnotebookの使い方を把握しているか確認します。私が前方で話すのを聞く代わりに、新しいnotebookを使って自分のペースで進めさせ、近くに行った時に彼らが質問できるよう、私は歩き回るのです。クラスは私の話を聞いているのではなく、頭を下げてnotebookに取り組む人々の集団となります。私は彼らのフロー状態を邪魔したり、私が前で話すのを待たせたりして妨害しません。この方法で、私は歩き回って個々の人への指導に集中することもできるのです。

この手法は個人をエンパワーすることに重点を置いています。クラスを一つの単位として捉えることも可能ですが、一日の終わりには皆家に帰って、参加したことで得られた価値というものを彼らがそれぞれで評価するのです。クラスを一つと捉えることと各々を個人と見ることの比較は、トレーナーに成長する機会を与えてくれます。デモをしながら講義をすることとは別で、コーチングの能力を向上させることもできます。両方のアプローチを持っていることで参加者にも多くのメリットがあるだけでなく、知識のより良い共有者となれるメリットもあります。
この手法は個人をエンパワーすることに重点を置いています。クラスを一つの単位として捉えることも可能ですが、一日の終わりには皆家に帰って、参加したことで得られた価値というものを彼らがそれぞれで評価するのです。クラスを一つと捉えることと各々を個人と見ることの比較は、トレーナーに成長する機会を与えてくれます。デモをしながら講義をすることとは別で、コーチングの能力を向上させることもできます。両方のアプローチを持っていることで参加者にも多くのメリットがあるだけでなく、知識のより良い共有者となれるメリットもあります。
This method focuses on empowering individuals. We can treat the class as one unit but at the end of the day, everyone goes home and makes their own evaluation about the value they gained from attending. Treating the class as one versus seeing each as an individual opens up an opportunity for the trainer to improve. Aside from delivering a lecture while running some demos, you can also improve out coaching ability. By having both approaches, there's a lot of benefits to the attendees but there's also the benefit of becoming a better knowledge sharer.

個人としては、双方向性は学習に不可欠なものです。仲間は私たちが行なっていることや知らないことの理解を助けると共に、より良い質問や解法の提示のやり方を学ぶことで、チームとして活動する心構えをさせてくれます。古典的なクラスで隣の人に質問することは授業の邪魔になりかねません。しかし個々人が彼らのnotebookで非同期に取り組んでいる場合、問題はすでに解決していたり、誰かが解決に繋がる洞察を得ていて、皆の助けになるかもしれません。もし誰かが邪魔をされたとしても、それはクラス全体ではありません。
As individuals, interaction is essential to learning. Our peers help us understand what we do or don't know and it also prepares us to work with a team by learning how to better ask questions or present solutions. In traditional classes, asking your seatmate can disrupt the class. But with individuals working on their own notebooks asynchronously, problems may have been solved by already or someone may have an insight that can lead to a solution that can help the rest. If ever someone does get disrupted, it's not the whole class.


これにはnotebookのセットアップを行い、使い方を学ぶ時間が必要であるというデメリットもあります。短いセッションではかなりの時間を食いつぶしてしまうかもしれません。初心者クラスでは実際に開始できる前に少し時間が必要でしょう。しかし私はデメリットを上回るメリットがあると信じていて、なぜならば彼らはnotebookを持ち歩き、残りを自分のペースで続けることができるからです。私は単に彼らを正しい方向に向けてあげて、彼ら自身で継続できるようにするだけです。何が誤りとなり、それで何ができるのかを垣間見せてくれるnotebookがあります。レッスンはすでにnotebookにあってセッション中の私の話の中には無いので、彼らがここから何を得られるかは彼らの努力にかかっているのです。彼らが急にクラスを出たとたん「Python-fuを理解した！」と言うことはあり得ませんが、その道は開いたのでどこまで行けるかは彼らの努力にかかっています。Jupyter notebookは様々な言語でも動作しますので、Python向けだけでは無いと言うことも言っておくべきでしょう。

There are disadvantates to this like the requirement to setup and the need to spend some time learning how to use notebooks. For short sessions, it may eat up a huge chunk of time. For a beginner class, it may take some time before they actually get started. But I believe the advantages outweigh the disadvantages since they can take the notebooks with them and continue with the rest at their own pace. I merely set them in the right direction and empower them to continue on their own. There are notebooks that give them a glimpse of what can go wrong and what they can do about it. Since the lessons are already in the notebooks and not in what I say during the session, what they get out of it depends on their effort. They can't suddenly say "I know Python-fu!" after stepping out of the class but the pave the path and how far they go is up to their effort. I also have to mention that Jupyter notebooks can also work with different languages so it's not just for Python.

授業のはじめには古典的な授業のような始まり方をしますが、しばらくしてnotebookの使い方を学ぶにつれて変化が起こり、彼らは各々で取り組むようになります。彼らは個人で取り組んでいますので、何人かは自然と他の人より早く進みます。私が注目した興味深い点の一つは、トレーニングのあと私が雇いたくなるであろうのは誰かがはっきりと分かったことです。何人かは他の人よりもまさに抜き出ていました。この手法で、私は最大ではプログラミング経験のない120人を超えるグループを扱うことができました。
At the beginning of class, it starts out more like a traditional class but after a while, we see them working individually with the transition happening as they learn how to use the notebooks. Since they'll be working individually, some people will naturally be faster than others. One interesting thing I realized was that after a training, I know exactly who I would want to hire. Some people would just be ahead of others. With this method, the largest group that I was able to handle was more than 120 people with no programming background.
