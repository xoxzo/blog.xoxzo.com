Title: How to integrate Vue with Django Part 2 - Passing data to Vue component
Date: 2021-01-07 09:00
Author: Fathur Rahman
Tags: django-vue; django-webpack; tutorial; vue;
Slug: vue-with-django-passing-data
Lang: en
Summary: Learn how to pass data from Django into Vue

In [previous tutorial](https://blog.xoxzo.com/2020/08/05/vue-with-django-getting-started/), we learn how to integrate Vue with Django. In this tutorial, we will learn how to pass data from Django into Vue component, and utilize it

### Updating Vue component

- Vue component can accept data via Props

- Lets update our `DemoComponent.vue` to add new props called `poll`

```
<template>
  <h1>{{ message }}</h1>
</template>

<script>
export default {

  props: {

    poll: {
      type: Object,
      required: true,
    },

  },

  data() {
    return {
      message: "Welcome to Vue!",
    };
  },
};
</script>
```

- Vue component can accept prop with type Object, Array, Boolean and String

- We want to use dict data from Django, so we will use Object type

- Lets refresh our page, and we should see this error since we havent pass the required `poll` props yet



### Passing dict from Django to Vue

- Lets update our `views.py` to pass simple dict to our html

```
def index(request):

    # declare a Poll dict. In real life, you should use a Model with Serializer

    poll = dict()

    poll["id"] = 1
    poll["title"] = "Software Engineering Poll"

    return render(request, 'polls/index.html', { "poll": poll })
```

- Since the data already passed into `polls/index.html`, lets update the file so we can pass the data to the Vue component

```
{% extends 'polls/base_layout.html' %}

{% block main_content %}

<h1>Hello, world. You're at the polls index.</h1>

<!-- load the Vue component -->

<demo-component :poll="{{ poll }}" ></demo-component>

{% endblock %}
```

- Lets refresh our page to check whether Vue component already received the required data

![Poll prop]({filename}/images/vue-django/vue-poll-prop.png)

### Utilizing the prop data with Vue

- Once the `poll` data is available to Vue component via props, we can start using the data inside the Vue component

- Lets update `DemoComponent.vue` html to show the `poll` title. Notice that we wrap under div container to prevent Vue error when using multiple HTML element

```
<template>
  <div>
    <h1>{{ message }}</h1>

    <h2>{{ poll.id }} - {{ poll.title }}</h2>
  </div>
</template>

<script>
export default {

  props: {

    poll: {
      type: Object,
      required: true,  
    },

  },

  data() {
    return {
      message: "Welcome to Vue!",
    };
  },
};
</script>
```

- Lets refresh our page to preview the changes

![Show Poll info]({filename}/images/vue-django/vue-show-poll.png)

- Congratulations! Next we will pass array of data to our Vue component and utilize it

### Update Vue component to receive array

- Lets edit `DemoComponent.vue` and add new props called `poll_questions`

```
<template>
  <div>
    <h1>{{ message }}</h1>

    <h2>{{ poll.id }} - {{ poll.title }}</h2>
  </div>
</template>

<script>
export default {

  props: {

    poll: {
      type: Object,
      required: true,  
    },

    poll_questions: {
      type: Array,
      required: true
    },

  },

  data() {
    return {
      message: "Welcome to Vue!",
    };
  },
};
</script>
```

### Passing array of dict from Django to Vue

- Lets edit `views.py` again

```
def index(request):

    # declare a Poll dict. In real life, you should use a Model with Serializer

    poll = dict()

    poll["id"] = 1
    poll["title"] = "Software Engineering Poll"

    # declare array of Poll Questions dict. In real life, you should use a Model with Serializer

    poll_questions = []

    poll_question1 = dict()

    poll_question1["id"] = 1
    poll_question1["title"] = "Your favourite Python framework?"

    poll_questions.append(poll_question1)

    poll_question2 = dict()
    
    poll_question2["id"] = 2
    poll_question2["title"] = "Your favourite Javascript framework?"

    poll_questions.append(poll_question2)

    return render(request, 'polls/index.html', { "poll": poll, "poll_questions": poll_questions })
```

- Now lets edit `polls/index.html` to pass the `poll_questions` data into Vue component

```
{% extends 'polls/base_layout.html' %}

{% block main_content %}

<h1>Hello, world. You're at the polls index.</h1>

<!-- load the Vue component -->

<demo-component :poll="{{ poll }}" :poll_questions="{{ poll_questions }}"></demo-component>

{% endblock %}
```

- Lets refresh our page to check whether Vue component already received the required data

![Poll Questions prop]({filename}/images/vue-django/vue-poll-questions-prop.png)

- Lets edit `DemoComponent.vue` to utilize the array of Poll Questions

```
<template>
  <div>
    <h1>{{ message }}</h1>

    <h2>{{ poll.id }} - {{ poll.title }}</h2>

    <!--  demo usage of poll_questions -->

    <p>List of questions:</p>

    <p v-for="question in poll_questions" :key="question.id">{{ question.id }} -  {{ question.title }}</p>

  </div>
</template>

<script>
export default {

  props: {

    poll: {
      type: Object,
      required: true,  
    },

    poll_questions: {
      type: Array,
      required: true
    },

  },

  data() {
    return {
      message: "Welcome to Vue!",
    };
  },
};
</script>
```
- Lets refresh our page to preview the changes

![Show Poll Questions info]({filename}/images/vue-django/vue-show-poll-questions.png)


## Additional Notes

- In real life, you should copy the Vue props into different property to prevent it from being overwrite if new props data coming in

- If you are using Serializer, you must convert Serializer data into JSON data before passing into the HTML for Vue to consume

```
def index(request):

    poll = Poll.objects.get(id=1)

    poll_serializer = PollSerializer(
        poll
    )

    poll_json_data = json.dumps(poll_serializer.data)

    return render(request, 'polls/index.html', { "poll": poll_json_data })
```

## Wrapping Up

- Congratulations! We have succesfully learned how to pass data from Django to Vue!

- In the next post, we will learn How to implement API with Django and Vue. Stay tune!