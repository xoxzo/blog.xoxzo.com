Title: How to integrate Vue with Django Part 3 - Django Rest Framework API integration
Date: 2021-05-24 09:00
Author: Fathur Rahman
Tags: django-vue; django-webpack; tutorial; vue;
Slug: vue-with-django-rest-framework-api
Lang: en
Summary: Learn how to use Django Rest Framework API with Vue

API request is one of the important part in web development. Pair with Django Rest Framework, lets see how can we integrate Django Rest API with Vue.

## Install Axios

- Axios is the best API library for JS https://github.com/axios/axios

- We will utilize Axios to perform API request

- Lets install it via NPM

```
npm i axios
```

## Include `X-CSRFToken` in html page

- Django Rest Framework requires `X-CSRFToken` in for authentication

- We can use `{% csrf_token %}` provide by Django to get the `X-CSRFToken` value 

- Edit your base html, and include the csrf token tag inside the body

- Lets edit `base_layout.html` and add the `{% csrf_token %}`

```
{% load static %}
<html>

<head>

    <!-- refer to CSS that was compiled by Laravel Mix -->

    <link rel="stylesheet" type="text/css" href="{% static 'build/poll.css' %}">
</head>

<body>
    <div id="app">
      {% csrf_token %}
```

## Set the Axios global configuration

- Its better if we can seperate Axios configuration code from application code

- Lets create new file called `api.js`

```
touch src/api.js
```

- Add this code to `api.js`. What it does is auto set the header, and auto grab the token from the `csrf_token` for each Axios request

```
/**
 * We'll load the axios HTTP library which allows us to easily issue requests
 * to our Django back-end. This library automatically handles sending the
 * CSRF token as a header based on the value of the "XSRF" token cookie.
 */

window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

/**
 * Next we will register the CSRF Token as a common header with Axios so that
 * all outgoing HTTP requests automatically have it attached. This is just
 * a simple convenience so we don't have to attach every token manually.
 */

let token = document.getElementsByName("csrfmiddlewaretoken");

if (token) {
    window.axios.defaults.headers.common['X-CSRFToken'] = token[0].value;
} else {
    console.error('CSRF token not found: https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax');
}
```

- To start utilizing Axios in each global API request, include the newly created `api.js` into `app.js`

- Edit `app.js` and add this line into the top of the file

```
require('./api');
```

## Set the API base url

- We need to setup `base_url` so it can be use to build full url to the API endpoint

- Add `base_url` to the head section of `base_layout.html`

```
{% load static %}
<html>

<head>

    <!-- refer to CSS that was compiled by Laravel Mix -->

    <link rel="stylesheet" type="text/css" href="{% static 'build/poll.css' %}">

    <script>
      window.base_url = '{{ base_url }}';
    </script>
</head>
```

## Perform API request from Vue component

- Vue component now can perform API request using Axios, and global configuration already loaded via `api.js`

- Lets update our `DemoComponent.vue` to perform API request

```
<script>
export default {
  props: {
    poll: {
      type: Object,
      required: true,
    },

    poll_questions: {
      type: Array,
      required: true,
    },
  },

  data() {
    return {
      message: "Welcome to Vue!",
      polls: [],
    };
  },

  created() {
    // fetch list of polls after component created
    this.fetchPolls();
  },

  methods: {
    // get list of Poll

    fetchPolls() {
      const url = `${base_url}api/polls/`;

      let query_param = {};

      return axios
        .get(url, {
          params: query_param,
        })
        .then((response) => {
          let polls = response.data.results;

          this.polls = polls;

          return response.data;
        })
        .catch(function (error) {
          console.log("error res -->", error);

          throw error;
        });
    },

    // store new Poll

    storePoll(payload) {
      const url = `${base_url}api/polls/`;

      return axios
        .post(url, payload)
        .then((response) => {
          let poll = response.data;

          return poll;
        })
        .catch(function (error) {
          console.log("error res -->", error);

          throw error;
        });
    },

    // update existing Poll

    updatePoll(id, payload) {
      const url = `${base_url}api/polls/${id}/`;

      return axios
        .patch(url, payload)
        .then((response) => {
          let poll = response.data;

          return poll;
        })
        .catch(function (error) {
          console.log("error res -->", error);

          throw error;
        });
    },

    deletePoll(id) {
      const url = `${base_url}api/polls/${id}/`;

      return axios
        .delete(url)
        .then((response) => {
          return response;
        })
        .catch(function (error) {
          console.log("error res -->", error);

          throw error;
        });
    },
  },
};
</script>
```

- Please take note we only put dummy endpoint in the example and you should replace with your real endpoint

- Note that `base_url` usage if from the `base_url` that we set up earlier

- Also note that we dont need to pass the authentication token as it was already handled via `api.js` that we setup earlier

## Wrapping Up

- Congratulations! We have succesfully learned how to perform API request with Vue and Django Rest Framework!

- In the next post, we will learn How to use state management with Vue, Vuex and Django. Stay tuned!
