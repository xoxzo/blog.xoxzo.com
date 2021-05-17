Title: VueをDjangoと統合する方法
Date: 2020-08-05 09:00
Author: Fathur Rahman
Tags: django-vue; django-webpack; tutorial; vue;
Slug: vue-with-django-getting-started
Lang: ja
Summary: Vue と Django を統合する方法を解説します。
私がRuby On RailsからDjangoに切り替えたとき、最初に気付いたのはWebpackの公式統合がないということでした。

Webpack is the defacto tool to manage and compile your front end assets.

Due to lacking official integration of Webpack, I try countless tutorials with no satisfying result due to several shortcomings

### Some of the shortcomings are

1. Most tutorials cater for developers who wants to build SPA based web application, so they separate Vue from Django and Django only served as REST API provider

2. Some tutorials cater for Django coupled with Vue to replace jQuery, however the setup is not suitable for complex Vue component and Vuex state management.

### What we want to achieve in this tutorial

1. We want to tightly couple Vue with Django, so we can utilize the power of Django routing and template syntax

2. We want to utilize the power of Vue Single File Component (SFC) to build our application

So in this tutorial, I will share on how to setup Vue with Django to achieve our objectives

### Recipes

1. Laravel Mix to manage assets

2. Configure Laravel Mix to compiled assets into our application directory

3. Django template refer to the assets that were compiled by Laravel Mix

So when you first read about Laravel Mix, you must be wondering why should we use other framework components in Django project?

Contrary to the naming, Laravel Mix is actually a framework-agnostic wrapper for Webpack, which makes the webpack integration becomes really easy.

So we can use Laravel Mix to easily manage our front end assets no matter what framework that we use

## Install Laravel Mix

- Let assume we have basic Django project setup based on Django tutorial

- To install Laravel Mix into Django, let's follow [the official documentation for Laravel Mix](https://laravel-mix.com/docs/5.0/installation)

- At the installation page, scroll down to the section of Stand-Alone Project. We will follow the steps provided here

```
cd mysite
npm init -y
npm install laravel-mix --save-dev
cp node_modules/laravel-mix/setup/webpack.mix.js ./
```

- Open `webpack.mix.js` and we can see the default configuration where our JS and SASS will be compiled. We will update this configuration later to match our Django project

```
mix.js('src/app.js', 'dist/').sass('src/app.scss', 'dist/');
```

- Setup default directory and file

```
mkdir src && touch src/app.{js,scss}
```

![Default directory for JS and CSS]({filename}/images/vue-django/js-css-default-dir.png)

- Let's run our first compile using Laravel Mix

```
node_modules/.bin/webpack --config=node_modules/laravel-mix/setup/webpack.config.js
```

![Success compiling assets]({filename}/images/vue-django/success-compiled.png)

- After compile, we can find the compiled assets here

```
dist/app.css
dist/app.js
dist/mix-manifest.json
```

![Compiled assets in dist directory]({filename}/images/vue-django/compiled-dist.png)

- Edit `package.json` and add NPM scripts

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

- Install `cross-env`

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
