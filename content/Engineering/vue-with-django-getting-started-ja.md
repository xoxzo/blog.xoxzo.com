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

- Now you can easily compile your assets by running

```
npm run dev
```

- To always listen to asset changes

```
npm run watch
```

- Since we started using NPM, we should ignore `node_modules` directory. 

- Create new `.gitignore` at the root of the project

```
touch .gitignore
```

- Ignore the `node_modules`

```
# node modules
/node_modules
```

## Configure Laravel Mix for Django apps

- We gonna create `resources` folder in our Poll app

```
cd polls
mkdir resources
mkdir resources/js
mkdir resources/sass
```

- Create empty js file and scss file for our Poll app

```
touch resources/js/poll.js
touch resources/sass/poll.scss
```

- If the folder hasn't existed, create a `static` folder, and inside the `static` folder, create a `build` folder

```
mkdir -p static/build
```

- We need to update `webpack.mix.js` configuration

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

- Run the command to compile

```
npm run dev
```

![Compile Poll assets in dist directory]({filename}/images/vue-django/compile-poll-assets.png)

- After successfully compiled, we can see the compiled assets inside the `static/build` folder

![Compiled Poll assets in build directory]({filename}/images/vue-django/poll-build-assets.png)

## Install Vue

- Let's install Vue and start using it inside our Django app. Navigate to the root of our project mysite and run this command to install Vue

```
npm i vue
```

- After installed Vue, we can start using Vue inside our JS file. Lets edit `poll.js`

```
import Vue from 'vue'

let vue = new Vue({
  //
}).$mount('#app')
```

- Compile again by running

```
npm run dev
```

or to automatically recompile by running

```
npm run watch
```

## Setup Django html to use compiled assets by Laravel Mix

- Since we don't have any html page yet, we will create a basic html page inside `templates/polls` directory

```
mkdir templates/polls
```

- Create new `base_layout.html` and `index.html` file

```
touch templates/polls/base_layout.html
touch templates/polls/index.html
```

- Edit `base_layout.html`. Notice that we use div with id app, to mount Vue instance that was declare in `poll.js`

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

- Edit `index.html`

```
{% extends 'polls/base_layout.html' %}

{% block main_content %}

<h1>Hello, world. You're at the polls index.</h1>

{% endblock %}
```

- Let's update our `views.py` to use the `index.html`

```
def index(request):
    return render(request, 'polls/index.html')
```

- Let's navigate to `http://127.0.0.1:8000/polls/`

- To verify Vue instance exist and make our development easier, we can install this extension:

https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd?hl=en

- If the Vue instance is working, we can see the Vue panel is activated

![Vue panel activated]({filename}/images/vue-django/vue-panel-activated.png)

## Use Vue Single File Component at Django html

- To start using Vue in our project, let's create a Single File component. Inside the `polls` directory, run this

```
mkdir resources/js/components
```

- Create a new Vue Single File Component

```
touch resources/js/components/DemoComponent.vue
```

- Edit `DemoComponent.vue`

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

- Register the new component inside `poll.js`

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

- Edit the `polls/index.html`

```
{% extends 'polls/base_layout.html' %}

{% block main_content %}

<h1>Hello, world. You're at the polls index.</h1>

<!-- load the Vue component -->

<demo-component></demo-component>

{% endblock %}
```

- To verify it is working, refresh `http://127.0.0.1:8000/polls/`

- We should see the Welcome to Vue at the page. We also can inspect the component at Vue panel

![Inspect Vue component]({filename}/images/vue-django/inspect-vue-component.png)

## Wrapping Up

If you have made this far, congratulations you have successfully integrate Vue with Django.

In the next post, we will learn How to pass data from Django into the Vue component.

Stay tuned and happy coding!
