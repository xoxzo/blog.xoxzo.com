Title: VueをDjangoと統合する方法
Date: 2020-08-05 09:00
Author: Fathur Rahman
Tags: django-vue; django-webpack; tutorial; vue;
Slug: vue-with-django-getting-started
Lang: ja
Summary: Vue と Django を統合する方法を解説します。

Ruby On RailsからDjangoに切り替えたとき、私は、まず、Webpackの公式統合がないということに気づきました。
Webpackは、フロントエンド アセットを、事実上、管理したりコンパイルしたりするためのツールです。
Webpackの公式統合がないので、私は、このチュートリアルはこれが足りない、こっちはこれが足りない、と、満足のいく結果が得られないまま、無数のチュートリアルを試すことになりました。

### 足りない、というのは

1. ほとんどのチュートリアルが、SPAベースのウェブアプリケーションを構築したい開発者を対象としているため、VueをDjangoから分離し、DjangoはRESTAPIプロバイダーとしてのみ機能させているのです。

2. jQueryを置き換えるために、Vueと組み合わせたDjangoに対応しているチュートリアルもありましたが、複雑なVueコンポーネントおよびVuex状態管理にはセットアップが適していませんでした。

### 本チュートリアルの到達目標

1. VueとDjangoを緊密に統合して、Djangoのルーティング パワーとテンプレート構文の機能を活用できるようにする

2. Vueシングルファイルコンポーネント（SFC）のパワーを利用してアプリケーションを構築する

ということで、このチュートリアルでは、この目標を達成するために、DjangoでVueを設定する方法について解説します。

### レシピ

1. アセットを管理するためのLaravelMix

2. アプリケーションのディレクトリにコンパイルされたアセットにLaravelMixを設定

3. Djangoテンプレートは、LaravelMixでコンパイルしたアセットを参照

これを読むと最初は、Djangoプロジェクトで、なぜ他のフレームワークのコンポーネントを使用する必要があるのか、と疑問に思いませんか。

名前とは異なり、Laravel Mixは、実はWebpackのフレームワークに依存しないラッパーであり、Webpackの統合を非常に簡単にしてくれるものなのです。

そのため、Laravel Mixを使用すると、使用するフレームワークに関係なく、フロントエンド アセットを簡単に管理できるのです。

## Laravel Mix をインストールする

- Djangoチュートリアルに基づいた、基本的なDjangoプロジェクトのセットアップがある、と仮定しましょう。

- Laravel MixをDjangoにインストールするには、[LaravelMixの 公式ドキュメンテーション](https://laravel-mix.com/docs/5.0/installation) に従ってみましょう。

- インストールページで、スタンドアロンプロジェクトのセクションまでスクロールダウンします。ここに記載されている手順に従います。

```
cd mysite
npm init -y
npm install laravel-mix --save-dev
cp node_modules/laravel-mix/setup/webpack.mix.js ./
```

- `webpack. mix .js` を開くと、JSとSASSがコンパイルされるデフォルトの構成が表示されます。この構成は、Djangoプロジェクトに一致するよう、後ほど更新することにします。

```
mix.js('src/app.js', 'dist/').sass('src/app.scss', 'dist/');
```

- デフォルトのディレクトリとファイルを設定します。

```
mkdir src && touch src/app.{js,scss}
```

![Default directory for JS and CSS]({filename}/images/vue-django/js-css-default-dir.png)

- LaravelMixを使用して、初コンパイルを実行しましょう。

```
node_modules/.bin/webpack --config=node_modules/laravel-mix/setup/webpack.config.js
```

![Success compiling assets]({filename}/images/vue-django/success-compiled.png)

- コンパイル後、コンパイルされたアセットは、ここで見つけられます。

```
dist/app.css
dist/app.js
dist/mix-manifest.json
```

![Compiled assets in dist directory]({filename}/images/vue-django/compiled-dist.png)

- `package.json` を 編集 してNPMスクリプトを追加します。

```
"scripts": {
    "dev": "npm run development",
    "development": "cross-env NODE_ENV=development node_modules/webpack/bin/webpack.js --progress --hide-modules --config=node_modules/laravel-mix/setup/webpack.config.js",
    "watch": "npm run development -- --watch",
    "hot": "cross-env NODE_ENV=development node_modules/webpack-dev-server/bin/webpack-dev-server.js --inline --hot --config=node_modules/laravel-mix/setup/webpack.config.js",
    "prod": "npm run production",
    "production": "cross-env NODE_ENV=production node_modules/webpack/bin/webpack.js --no-progress --hide-modules --config=node_modules/laravel-mix/setup/webpack.config.js"
}
```

- `cross-env` をインストールします。

```
npm install cross-env --save-dev
```

- これを実行すれば、アセットを簡単にコンパイルできるようになります。

```
npm run dev
```

- アセットの変化に常に耳を傾けるには

```
npm run watch
```

- NPMを使い始めたので、`node_modules` ディレクトリを無視しなくてはなりません。 

- プロジェクトのルート に 新しい `.gitignore` を作成します。

```
touch .gitignore
```

- `node_modules` を無視します。

```
# node modules
/node_modules
```

## Djangoアプリ用にLaravelMixを構成する

- Poll アプリ内に、 `resources`フォルダを 作成します。

```
cd polls
mkdir resources
mkdir resources/js
mkdir resources/sass
```

- Poll アプリ用に、空のjsファイルとscssファイルを作成します。

```
touch resources/js/poll.js
touch resources/sass/poll.scss
```

- フォルダーがまだない場合は、`static` フォルダーを作成し、その `static` フォルダー内に`build`フォルダーを 作成 しましょう。

```
mkdir -p static/build
```

- `webpack.mix.js` の構成を更新し ます。

```
let staticPath = "polls/static/build";
let resourcesPath = "polls/resources";

mix.setResourceRoot("/static/build"); // setResroucesRoots add prefix to url() in scss on example: from /images/close.svg to /static/images/close.svg
mix.setPublicPath("polls/static"); // Path where mix-manifest.json is created

// if you don't need browser-sync feature you can remove this lines
if (process.argv.includes("--browser-sync")) {
  mix.browserSync("localhost:8000");
}

// Now you can use full mix api
// Refer the file that was created in Step 2 to be compile
mix.js(`${resourcesPath}/js/poll.js`, `${staticPath}/`);
mix.sass(`${resourcesPath}/sass/poll.scss`, `${staticPath}/`);
```

- コマンドを実行してコンパイルします。

```
npm run dev
```

![Compile Poll assets in dist directory]({filename}/images/vue-django/compile-poll-assets.png)

- 正常にコンパイルされると、`static / build` フォルダー内にコンパイルされたアセットが表示されます。 

![Compiled Poll assets in build directory]({filename}/images/vue-django/poll-build-assets.png)

## Vue をインストールする

- Vueをインストールして、Djangoアプリ内で使い始めましょう。プロジェクトmysiteのルートに誘導し、このコマンドを実行してVueをインストールします。

```
npm i vue
```

- Vueをインストールしたら、JSファイル内でVueを使い始められます。`poll.js`を編集しましょう

```
import Vue from 'vue'

let vue = new Vue({
  //
}).$mount('#app')
```

- こちらを実行して、再度コンパイルします。

```
npm run dev
```

または、こちらを実行して自動的に再コンパイルしましょう。

```
npm run watch
```

## LaravelMixでコンパイルされたアセットを使うために、Django htmlを設定する

- html ページがまだないため、`templates / polls` ディレクトリ内に基本的なhtmlページを作成します。

```
mkdir templates/polls
```

- `base_layout.html` および `index.html` ファイルを新規作成します

```
touch templates/polls/base_layout.html
touch templates/polls/index.html
```

- `base_layout.html`を 編集します。`poll.js`で宣言されたVueインスタンスをマウントするため、id appでdivを使用していますので注意してください 。

```
{% load static %}
<html>

<head>

<!-- refer to CSS that was compiled by Laravel Mix -->

<link rel="stylesheet" type="text/css" href="{% static 'build/poll.css' %}">
</head>

<body>
<div id="app">
    {% block main_content %}

    {% endblock %}
</div>

<!-- refer to JS that was compiled by Laravel Mix -->
<script type="text/javascript" src="{% static 'build/poll.js' %}"></script>
</body>

</html>
```

- `index.html`を編集します。

```
{% extends 'polls/base_layout.html' %}

{% block main_content %}

<h1>Hello, world. You're at the polls index.</h1>

{% endblock %}
```

- `index.html`を使えるように `views.py`を更新しましょう。

```
def index(request):
    return render(request, 'polls/index.html')
```

- `http://127.0.0.1:8000/polls/`に誘導しましょう。

- Vueインスタンスが存在することを確認し、開発をラクにするには、次の拡張機能をインストールしましょう。

https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=en

- Vueインスタンスが機能している場合は、Vueパネルがアクティブになっていることがわかります。

![Vue panel activated]({filename}/images/vue-django/vue-panel-activated.png)

## Django htmlでVueシングルファイルコンポーネント(SFC)を使用する

- このプロジェクトでVueの使いはじめるので、シングルファイルコンポーネントを作成しましょう。`polls` ディレクトリ内で、こちらを実行します。

```
mkdir resources/js/components
```

- 新規Vueシングルファイルコンポーネントを作成しましょう。

```
touch resources/js/components/DemoComponent.vue
```

- `DemoComponent.vue`を編集します。

```
<template>
  <h1>{{ message }}</h1>
</template>

<script>
export default {
  data() {
    return {
      message: "Welcome to Vue!",
    };
  },
};
</script>
```

- `poll.js`内に新規コンポーネントを登録します。

```
import Vue from "vue";

// import components

Vue.component(
  "demo-component",
  require("./components/DemoComponent.vue").default
);

let vue = new Vue({
  //
}).$mount("#app");
```

- `polls/index.html`を編集します。

```
{% extends 'polls/base_layout.html' %}

{% block main_content %}

<h1>Hello, world. You're at the polls index.</h1>

<!-- load the Vue component -->

<demo-component></demo-component>

{% endblock %}
```

- 動作確認には、`http://127.0.0.1:8000/polls/`を更新しましょう。

- そのページにWelcome to Vueが表示されるはずです。Vueパネルでコンポーネントの検査が可能です。

![Inspect Vue component]({filename}/images/vue-django/inspect-vue-component.png)

## まとめ

ここまでくれば、VueとDjangoの統合に成功したと言えるでしょう。おめでとうございます。

次回は、DjangoからVueコンポーネントにデータを渡す方法を解説します。

引き続きご期待ください。
