Title: Django vs Flask, which one is better?
Date: 2019-04-3 12:01
Author: Surya Banerjee
Tags: django; webframework; flask; python; development;
Slug: django-vs-flask
Lang: en
Thumbnail: images/djangoflask/so_questions.png
Summary: Flask vs Django, the battle of frameworks can be a bit confusing to people who start off. This is a guide for making an informed decision about the right web framework to work with.

I would like to congratulate you for deciding to develop web apps using python. Python is currently one of the most popular programming languages around, favored for its clean, readable code, and flexibility. It is also in high demand because of its wide range of web frameworks that can take your project from idea to reality, in the fastest time possible. Let's first address the most fundamental question.

# What are web frameworks?
A web framework is a code library that makes web development faster and easier by providing common patterns for building reliable, scalable and maintainable web applications. What that means is that a web framework takes away all the boring and repetitive tasks from you and lets you concentrate on building what you want to build. Pretty cool stuff!  
Frameworks provide functionality in their code or through extensions to perform common operations required to run web applications. These common operations include:

* URL routing
* Input form handling and validation
* HTML, XML, JSON, and other output formats with a templating engine
* Database connection configuration and persistent data manipulation through an object-relational mapper (ORM)
* Web security against Cross-site request forgery (CSRF), SQL Injection, Cross-site Scripting (XSS) and other common   malicious attacks
* Session storage and retrieval

Now not all frameworks have all the functionalities listed above. Some frameworks take the "batteries-included" approach where everything possible comes bundled with the framework while others have a minimal core package that can be extended later. Here is where the approach of ‘Flask’ and ‘Django’ differ.

# What are 'Flask' and 'Django' exactly?
##### Flask: 
As they describe themselves (From PyPi) - Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
Now what that basically means is that Flask implements a bare-minimum and leaves the bells and whistles to add-ons or to the developer. 
##### Django:
For Django, they describe themselves (From PyPi) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. It is a web application framework with a "batteries-included" philosophy. The principle behind batteries-included is that the common functionality for building web applications should come with the framework instead of as separate libraries. Thus the common functionalities listed above are all available in Django to be quickly implemented.

Now you might be thinking why use Flask when Django already provides all the features out of the box. The answer lies in what you are trying to build. Flask provides simplicity, flexibility and fine-grained control. It is unopinionated (it lets you decide how you want to implement things). Thus if you are building a very simple web app or you need to customize all aspects of the app, Flask is a better option. However, the batteries included in Django makes it easier for Django developers to accomplish common web development tasks like user authentication, URL routing and database schema migration. Also, Django accelerates custom web application development by providing built-in template engine, ORM system, and bootstrapping tool. Sounds confusing? Let's dig into this further and let you make your own choice.

# How do they match up in terms of performance with each other? 
##### Performance Benchmarks:
![benchmarks](/images/djangoflask/benchmarks.png)<a class="caption" href="http://klen.github.io/py-frameworks-bench/">Credit</a>

As we can see from the benchmark, Flask is significantly faster than Django due to the lightweight nature of the framework. However as I mentioned earlier, Django provides a lot of functionalities which are unavailable in Flask for rapid development and prototyping.

# How popular are both the frameworks?
Another key factor for choosing a framework to work with is the way the community embraces it. Let’s look at some popular websites using Flask and Django.

##### Websites using Flask:
* Pinterest
* Reddit
* Twilio

##### Websites using Django:
* Instagram
* Disqus
* Dropbox

Also Django beats Flask in two counts. Django is so popular that it has a large community of django developers who come together once, or maybe twice a year for **DjangoCon** which is their own conference. Unfortunately Flask doesn’t have any equivalent conference.Also, Flask does not have any corporate sponsors in the same league as the ones with Django like

* Microsoft
* Eventbrite
* Mozilla
* Caktus Group
* 791 Tech

Django has been around for longer — it was first released in 2005, while Flask debuted in 2010 — and is more popular — in January 2017, there were 2631 StackOverflow questions about Django and 575 for Flask. Both frameworks are growing steadily in popularity, as can be seen by the number of StackOverflow questions about each in the image below.
![so_questions](/images/djangoflask/so_questions.png)
Thus we can see that overall Django has more community engagement than Flask.

# Learning curve - Django vs Flask:
This is one aspect that Flask beats Django by quite a distance. Flask being a lightweight and barebone framework is easier to grasp than Django. However the learning curve for Django can be rewarding as it makes your job easier later. Let’s try to build a ‘Hello World’ app in both these frameworks and you can be the judge.
 
##### “Hello Flask”
A good practise is to isolate your python environment before installing any packages. This be done using virtual environments. My favourite tool to get this done is ‘virtualenv’. Assuming you are using a debian based distro like Ubuntu, you can do this to install the package -

```
sudo apt-get install virtualenv
```

Now that we have virtualenv installed, let's create a virtual environment and activate it.
```
virtualenv -p python3 venv/
source venv/bin/activate
```
(To deactivate, just type ‘deactivate’)

The first thing we need to do in order to use Flask is to install it. This can easily be done by using pip.
```
pip install flask
```
Once you've done that, create a Python file called flaskhello.py and insert the following code:
```
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
 return "Hello, World!"  
if __name__ == "__main__":
 app.run()
```
##### Let's understand what this code does:
* Line 1 imports Flask
* Line 3 initializes an app variable, using the __name__ attribute
* Line 5 is where the @app.route python decorator takes the function directly below it and modifies it. We use this to route traffic from a specific URL to the function directly below. Using different @app.route calls, we can 'trigger' different parts of the code when the user visits different parts of our application. Here, we only have a single route /, which is the default "root" of our application.
* In Line 6 the function name hello is not important. In stead of calling this function from somewhere else in our code, it will be called automatically. It's still a good practice to give it a relevant name though.
* Line 7 returns the string to our user. Usually we would render a template or return HTML here so that users will see a nicely formatted page, but returning a Python string works fine too.
* Line 9 is normal Python boilerplate to make sure we don't run anything automatically if our code is imported by another Python script.
* Line 10 calls the run() method of the app we initialized in Line 3. This starts the development server for Flask and allows us to visit our web application from our local machine by visiting localhost.

##### ‘Hello Django’
Django can also be installed through pip. Run the following command:
```
pip install django
```
When you installed Django, it also set up the django-admin command, which we'll use now. Run the following:
```
django-admin startproject hellodjango
```
Here we create a Django "project", and it will create a hellodjango directory. If we look in the hellodjango directory, we'll see that it created a manage.py file and a subdirectory which is also called hellodjango. Inside the subdirectory there are three Python scripts. We'll only need to worry about urls.py for our "Hello World" project.

The next step is to use Django to create an App, which is an organizational structure below that of a Django Project (one Project can contain many apps). We will use the manage.py file that the previous command created in order to create the application. From the outer hellodjango directory, we run the following command:
```
python manage.py startapp helloworld
```
This creates the helloworld app and makes it part of our hellodjango project. Now we need to configure the URL routing (like we did with @app.route in Flask). Because Django projects have more default structure than Flask apps, we'll have a few extra steps. The previous command created a helloworld directory within the outer hellodjango directory. Open the automatically created helloworld/views.py file and add the following code:
```
from django.http import HttpResponse
def index(request):
  return HttpResponse("Hello, World!")
```

* Line 1 imports the HttpResponse function, which we can use to send a string over HTTP to the user of our web app. As with Flask, we wouldn't usually use this, as we'd want to do more complicated things with rendering HTML templates. However, for our Hello World app this is all we need.
* In line 3, we're defining an index function. Here, unlike with Flask, we don't use a decorator that says this function should be called when the user visits our application. Instead, we'll set this up via two urls.py files — one for the project, which was automatically created, and one for the application, which we'll need to create.
* Line 4 returns the "Hello, World!" string wrapped in an HttpResponse so that it can be displayed in our user's web browser.

Now we need to create a urls.py file for our application. Create helloworld/urls.py and add the following code:
```
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
* Line 1 imports the url function so that we can link specific URLs to functions in our views.py file.
* Line 3 imports the views.py file that we added our "Hello, World" index() view to.
* Lines 5-7 sets up a list of urlpatterns — this is equivalent to the @app.route decorators that we used in Flask. We match specific URLs using regular expressions, and link these to functions in our views.py script. In this case, we set up a single pattern, which matches an empty URL (like "/" in Flask — in other words, the default page of our application) and links it to the views.index function that we wrote earlier.

That's the URL configuration for our app (helloworld). We also need a URL configuration for our project (hellodjango). Edit the hellodjango/hellodjango/urls.py file, which was automatically created (it might be a bit confusing that there are two urls.py files, but it should make sense if you think of one belonging to the entire project, routing URLs to different apps, and the other belonging to the helloworld app alone). Add the following code:
```
from django.conf.urls import include, url  
urlpatterns = [ 
    url(r'^hello/', include('helloworld.urls')), 
]
```
This is similar to the previous file. However, instead of routing URLs of a specific pattern to a specific view, we are routing them to a specific application. In this case, any URL that has /hello after it will be sent along to our helloworld application and will look in helloworld.urls to work out which view to call.
Now go back to the outer /hellodjango directory (the one which contains the manage.py file) and run the following command:
```
python manage.py runserver
```

This runs the Django development server, which lets us visit our application on localhost, as we did with Flask. You should see output that is similar to the following:
```
Performing system checks…
System check identified no issues (0 silenced).
You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 03, 2017 - 16:14:20
Django version 1.10.5, using settings 'hellodjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
You can ignore the warning about the migrations — this is related to the database for the web application, which we are not using. We can visit http://127.0.0.1:8000/hello to view our "Hello, World!" greeting (don't forget the /hello at the end, which tells Django which app to visit).

# So finally you now know enough to make your choice
So we have gone through a comparative analysis of the python web frameworks - Flask and Django. Now I think you are armed with enough knowledge to make an informed decision for yourself and your project. So go on, try it yourself!

**Disclaimer:**
*We at [Xoxzo](https://www.xoxzo.com/en/) are a telephony API company and proactive supporters of the python developer community. If you want to do cool stuff like sending SMS texts and invoke calls with your code, do check us out [here](https://www.xoxzo.com/en/) where you get some free credits to start tinkering with our awesome API!*
