Title: Xoxzo のブログが新しくなりました！
Date: 2020-02-10
Slug: xoxzo-blog-has-a-new-look
Lang: ja
Tags: tip; new feature; 2020; 
Author: Hyejeong Park
Thumbnail: images/blog_redesign_00.png 
Summary: ブログの新デザインでは、何が、なぜかわったのでしょうか？

Xoxzoのアセットデザインの更新により、ブログを含めた、全面的な変更が行われました。
新しいデザインとファッションでは、何を、なぜ変更したかを共有させていただきたいと思います。

![blog_redesign_01]({filename}/images/blog_redesign_01.png)

## 記事リストへ、サムネイル画像を追加

以前の記事リストでは、レイアウトは視覚的に、読みたい記事へ案内するのが困難で、要素が重なってぼやけているように見えてしまっていました。
[カードレイアウト]（https://www.intercom.com/blog/why-cards-are-the-future-of-the-web/）は非常に直感的で、
記事を明確に区別して見せるため、この問題の改善に役立つことがわかりました。
判別しやすい方法で、リンクされたコンテンツをきれいに表示すると同時に、画像のサムネイルの追加も可能になりました。

サムネイルを簡単に生成するために、 `pelican-advthumbnailer`プラグインを使用しています。


##### 1. プラグインをインストールして `pelicanconf.py` をアップデートする
```
$ pip install pelican-advthumbnailer
```

```python
# pelicanconf.py
PLUGINS = [..., 'advthumbnailer']
```

##### 2. `Thumbnail` metadata を、自分のブログへ追加する
```html
<!-- new_blog_content.md -->
Title: Xoxzo blog has a new look!
Date: 2020-02-10 13:00 
Slug: xoxzo-blog-has-a-new-look
Lang: en
Author: Hyejeong Park
Thumbnail: images/blog_thumbnail.png
...
```

##### 3. `article.thumbnail` を `<img>` tag へ入れて、画像サイズを設定します。
デフォルトのサムネイル画像の追加をお忘れなく。
```html
<!-- index.html -->
<a href="{{ SITEURL }}/{{ article.url }}">
  {% if article.thumbnail %}
  <img src="{{ SITEURL }}/{{ article.thumbnail | thumbnail('350x_') }}">
  {% else %}
  <img src="{{ SITEURL }}/{{ THEME_STATIC_DIR }}/images/default_thumbnail.png">
  {% endif %}
</a>
```

`pelican-advthumbnailer` については [こちら](https://github.com/AlexJF/pelican-advthumbnailer) で、より詳しく説明しています。

「直感」という同じテーマに沿って、記事リストのタイポグラフィを変更、階層を明確に示すために色を加えて、
タイトルと要約部分のパディングを調整し、よりオーガニックな外観を作ることができました。

![blog_redesign_02]({filename}/images/blog_redesign_02.png)

## tag リストの除去
以前は、左側のサイドバーに長いタグリストがあり、ページの一番下までスクロールするのに時間がかかっていました。 
本来、ユーザーが記事を閲覧するのを助けるためのものなのですが、機能的にあまり役に立っていませんでした。 
ですので、タグリストは削除し、カテゴリーリストを残して、ページを見やすくすることにしました。

![blog_redesign_03]({filename}/images/blog_redesign_03.png)

## 記事ページテンプレートの更新
前バージョンの記事ページテンプレートでは、太字の記事タイトル以外の要素が、ほとんど同じサイズと色であったため、
要素を相互に区別するのが直観的とは言えませんでした。 
ブラウジング時にユーザーが感じるであろう摩擦を減らし、コンテンツに集中しやすくしたかったのです。

新しいデザインでは、コンテンツへの集中を支援するため、タイトルと本文のコンテンツに明確なコントラストを与え、
著者、日付、カテゴリなどの小さな要素に直感的な階層を加えました。

また、サイドバーも削除し、記事への焦点をより明確に合わせました。

![blog_redesign_04]({filename}/images/blog_redesign_04.png)

## エディターズピックエリアの追加
最高のコンテンツを活用してユーザーに紹介するため、ブログに「注目」エリアを作成することにしました。 
残念ながら、専用のPelicanプラグインを見つけることができなかったので動的に実行されていませんが、このセクションを定期的に更新します！

![blog_redesign_05]({filename}/images/blog_redesign_05.png)

## まとめ
ご紹介したすべての改善には、長い時間がかかりました。
再設計のおかげで、ついに今回のアップデートをお届けできる運びとなり、その日を楽しみにしています。 
こういった工夫で読者が楽しめるように、より直感的なユーザーエクスペリエンスを今後も作り続けたいと考えています。
