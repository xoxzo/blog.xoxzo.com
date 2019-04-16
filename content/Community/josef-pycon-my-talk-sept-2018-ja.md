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

トークは技術的なものではなく、初心者にも分かりやすいものです。
想定していた対象は教育者、技術グループや、トレーニングを運営している個人や組織などでした。
仕事で日常的に行なっているのかもしれませんし、誰かの交代要員や新しいチームメンバーを一度だけトレーニングことがあるか、という感じでしょうか。
組織やコミュニティの一員としてであれば、知識を共有するために、招かれたりタスクを振られたりしたのかもしれません。
誰しもが突然、何らかの理由で何かしらのトレーニングを実施する必要に迫られることがあります。
参加者は無料か、自腹、または会社持ちの費用で来ているのかもしれません。
参加者がトレーニングに料金を支払う場合、人数が増える事はより多くの収益を意味します。
会社に何らかの大きな変化が起きれば、巨大な部屋に参加者を迎えるなんてことがあるかもしれません。
準備しておくに越したことはありません。

何にせよ、柔軟性があることは参加者にとって有益です。
より大きなグループでのチャレンジは、より問題が起こりやすいと言うことです。
人が増えるとより多くの質問がなされますし、より多くのエラーが起きるということです。
誰かが単に話について行くのに時間がかかることもあります。
そんな人がたまたま、特定のイベントに沢山いるということもあります。
クラスが大きいほど、管理は難しく、物事は誤った方向に行きやすくなります。
これは、大きなクラスが得られる全体的な品質を低下させてしまいます。
クラスのサイズを大きくしたければ、届けられる価値にも同時に注意しなければなりません。
スタートアップの世界や技術サークルなどでいずれ誰かが「それはスケールするのか？」という疑問を持つことになります。

In any case, having flexibility will be beneficial to your attendees. 
The challenge with larger groups is that more problems can arise. 
More people means more questions are asked, and more errors happen. 
Sometimes, it just takes longer for someone to follow along. 
Sometimes, it just so happens that there's a lot of that kind of person in a particular event. 
The larger the class, the harder it is to manage and the bigger the chances of things going wrong. 
This lowers the overall quality received by larger classes. 
If we want to increase the size of the class, we sill want to maintain the value we deliver. 
In startup land or in our tech circles someone eventually asks the question "Does it scale?"

![Josef トーク]({filename}/images/pycon-my-2018/IMG_9595.JPG)

Here are some of the insights from my experience. 
They can be applied to other things but for my purpose, I improved how I conduct trainings, 
which allowed me to increase the number of attendees I can handle while maintaining the quality. 
The insights I gained from my training practice can be summed up into:

これらは私の経験から得られたいくつかの知見です。
これらは私の意図を別にすれば他のことにも応用できますが、私はトレーニングのやり方を改善し、
これにより品質を担保しながら扱える参加者数を増やしていくことができました。
私がトレーニングの経験から得た知見をまとめると、以下のようなものです。

* Better tools - there's a saying about using the right tool for the job
* Rethink methods - tools we use allow us to change the way we do our work
* Empower individuals - there's a different between treating the class as one unit vs each attendee as a unit
* Interaction is essential - make social interaction work for you, not disrupt you

•	より良いツール - 仕事に適した道具を使うことに関する格言があります
•	やり方を再考する - 利用するツールが仕事のやり方を変えます
•	個人をエンパワーする - クラスを一つの単位で扱うかそれぞれの参加者単位で捉えるかには違いがあります
•	双方向性は不可欠 - 社会的相互作用を利用して、邪魔はさせない


![Josef トーク]({filename}/images/pycon-my-2018/IMG_9612.JPG)

私の使うメインのツールはJupyter notebookです。これは教育用として素晴らしいと思います。多くの講演やデモがこれを利用し、インタラクティブなコードスニペットと共に口述を行なっています。プログラミングを教えるのに使う場合には、最初から全てをタイプしたり、前にいる誰かの話を聞いたりする必要が無くなるので進行がスピーディーになります。参加者はコードをより快適に試すことができ、より早いフィードバックループが得られます。
The main tool I use is the Jupyter notebook. I think it's great for teaching. Many talks and demos use it to tell a narrative together with interactive code snippets. When used to teach programming, it speeds things up by removing the need to type everything from scratch and the need to listen to someone in front. It also lets participants play with code more comfortably and let them have a faster feedback loop.

クラスの運営の仕方という意味では、私はステップバイステップでガイドに沿って進められるnotebookのレポジトリを用意すること以外に、バグの取り扱いと問題の回避方法を彼らに与える準備をします。こうすると彼らはより確信を持って学ぶことができるのです。私は簡単には壊れないといって安心させますが、もしものために、リセットボタンもつけます。迷子になったり、何をすれば良いかわからないと彼らが感じることは無いようにします。ある時点で、彼らは彼ら自身でnotebookの使い方を把握します。私が前方で話すのを聞く代わりに、新しいnotebookを使って自分のペースで進めるように奨励し、近くに行った時に彼らが質問できるよう私は歩き回ります。クラスは私の話を聞いているのではなく、頭を下げてnotebookに取り組む人々の集団となります。私は彼らのフロー状態を邪魔したり、私が前で話すのを待たせたりして妨害しません。この方法で、私は歩き回って個々人への指導に集中することもできます。
In terms of how I conduct the class, aside from preparing a repository of notebooks that let them progress step by step with my guidance, I prepare them by giving them ways to handle bugs and find their way around problems. This way, they have more confidence while learning. I assure them it won't be easy to break things, but just in case, there's a reset button. I just make sure that they don't feel like they're lost or don't know what to do. At some point, they get a good grasp of using the notebooks on their own. Instead of listening to me speaking in front, I encourage them to go ahead with the other notebooks at their own pace and I get to walk around, which becomes an opportunity for some people to ask me questions when I'm near. The class turns into a group of people with their heads down, working on noteoboks instead of listening to me. I don't hold them back by disrupting their flow or making them wait while I speak in front. This way I can also go around and focus on giving individual guidance.


この手法は個人をエンパワーすることにフォーカスしています。クラスを一つの単位として捉えることも可能ですが、一日の終わりには皆家に帰って、参加したことで得られた価値というものを彼らがそれぞれで評価するのです。クラスを一つと捉えることと各々を個人と見ることの比較は、トレーナーに成長する機会を与えてくれます。デモをしながら講義をすることとは別で、コーチングの能力を向上させることもできます。両方のアプローチを持っていることで参加者にも多くのメリットがあるだけでなく、知識のより良い共有者となれるメリットもあります。
This method focuses on empowering individuals. We can treat the class as one unit but at the end of the day, everyone goes home and makes their own evaluation about the value they gained from attending. Treating the class as one versus seeing each as an individual opens up an opportunity for the trainer to improve. Aside from delivering a lecture while running some demos, you can also improve out coaching ability. By having both approaches, there's a lot of benefits to the attendees but there's also the benefit of becoming a better knowledge sharer.

個人としては、双方向性は学習に不可欠なものです。仲間は私たちが行なっていることや知らないことの理解を助けると共に、より良い質問や解法の提示のやり方を学ぶことで、チームとして活動する心構えをさせてくれます。古典的なクラスで隣の人に質問することは授業の邪魔になりかねません。しかし個々人が彼らのnotebookで非同期に取り組んでいる場合、問題はすでに解決していたり、誰かが解決に繋がる洞察を得ていて、皆の助けになるかもしれません。もし誰かが邪魔をされたとしても、それはクラス全体ではありません。
As individuals, interaction is essential to learning. Our peers help us understand what we do or don't know and it also prepares us to work with a team by learning how to better ask questions or present solutions. In traditional classes, asking your seatmate can disrupt the class. But with individuals working on their own notebooks asynchronously, problems may have been solved by already or someone may have an insight that can lead to a solution that can help the rest. If ever someone does get disrupted, it's not the whole class.


これにはnotebookのセットアップを行い、使い方を学ぶ時間が必要であるというデメリットもあります。短いセッションではかなりの時間を食いつぶしてしまうかもしれません。初心者クラスでは実際に開始できる前に少し時間が必要でしょう。しかし私はデメリットを上回るメリットがあると信じていて、なぜならば彼らはnotebookを持ち歩き、残りを自分のペースで続けることができるからです。私は単に彼らを正しい方向に向けてあげて、彼ら自身で継続できるようにするだけです。何が誤りとなり、それで何ができるのかを垣間見せてくれるnotebookがあります。レッスンはすでにnotebookにあってセッション中の私の話の中には無いので、彼らがここから何を得られるかは彼らの努力にかかっているのです。彼らが急にクラスを出たとたん「Python-fuを理解した！」と言うことはあり得ませんが、その道は開いたのでどこまで行けるかは彼らの努力にかかっています。Jupyter notebookは様々な言語でも動作しますので、Python向けだけでは無いと言うことも言っておくべきでしょう。

There are disadvantates to this like the requirement to setup and the need to spend some time learning how to use notebooks. For short sessions, it may eat up a huge chunk of time. For a beginner class, it may take some time before they actually get started. But I believe the advantages outweigh the disadvantages since they can take the notebooks with them and continue with the rest at their own pace. I merely set them in the right direction and empower them to continue on their own. There are notebooks that give them a glimpse of what can go wrong and what they can do about it. Since the lessons are already in the notebooks and not in what I say during the session, what they get out of it depends on their effort. They can't suddenly say "I know Python-fu!" after stepping out of the class but the pave the path and how far they go is up to their effort. I also have to mention that Jupyter notebooks can also work with different languages so it's not just for Python.

授業のはじめには古典的な授業のような始まり方をしますが、しばらくしてnotebookの使い方を学ぶにつれて変化が起こり、彼らは各々で取り組むようになります。彼らは個人で取り組んでいますので、何人かは自然と他の人より早く進みます。私が注目した興味深い点の一つは、トレーニングのあと私が雇いたくなるであろうのは誰かがはっきりと分かったことです。何人かは他の人よりもまさに抜き出ていました。この手法で、私は最大ではプログラミング経験のない120人を超えるグループを扱うことができました。
At the beginning of class, it starts out more like a traditional class but after a while, we see them working individually with the transition happening as they learn how to use the notebooks. Since they'll be working individually, some people will naturally be faster than others. One interesting thing I realized was that after a training, I know exactly who I would want to hire. Some people would just be ahead of others. With this method, the largest group that I was able to handle was more than 120 people with no programming background.
