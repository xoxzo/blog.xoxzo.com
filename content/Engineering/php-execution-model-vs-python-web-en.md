Title: PHP execution model vs Python web
Date: 2012-05-02 16:48
Lang: en
Author: Kamal Mustafa
Tags: python; 2012; tip; django;
Slug: php-execution-model-vs-python-web
Thumbnail: images/5e422-6a0153916e707f970b0168eaaad5df970c-pi.png
Summary: A comparison on how php and python executes it's web applications

We're still looking for a better way to explain the difference between
PHP execution model vs Python for web application to new developers
joining us. This is to help them understand the key differences when
developing web application in Python. One source of confusion among them
was when they realized the state-full nature of Python web application
compared to state-less nature of PHP. The following diagram is my
attempt to show them these key difference.

PHP
---

![Php]({filename}/images/5e422-6a0153916e707f970b0168eaaad5df970c-pi.png)

PHP execution model is quite simple actually and follow a cgi-like
model. It simply take the php file as it's input, parse and interpret it
and then return what ever output the script produced, pass it back to
apache as response that will return back to requesting user (browser).
Unlike cgi, mod\_php already preloaded with the PHP interpreter so the
process of parsing and executing the script is fast since it does not
need to invoke PHP interpreter for each requests.

This diagram also tell us that `mod_php` is simply a fast PHP
interpreter and it does not know anything about our application. This
make PHP a state-less environment.

Python
------

![Python]({filename}/images/7c5e7-6a0153916e707f970b016765b4178f970b-pi.png)

In Python/Django execution model, our app always running as part of the
server process (although probably as separate user) and only the views
function/callable that will be executed on each request. This mean some
part of our code will only been executed once when we start/restart the
web server and only the code in the views function/callable are
guaranteed to run in each requests. This mean it's possible to store
data that would persist between requests. For example:-

    from django.http import HttpResponse
    counter = []
    def home(request):
    counter.append(1)
    return HttpResponse("Counter: %d" % len(counter))

This is simple django views and if you access this through browser
you'll see the counter value will be incremented every time you refresh
the browser. If you're just coming from PHP this new fact should be more
a warning than a cool new thing you want to try doing since most of the
time you want to avoid storing state like this and make sure you always
start with a fresh data on each requests. If you really need to store
data that persist between requests such remembering user already login,
there's better way such as django session object.

Another important consequences from this new fact about python execution
model is that it mean when we change our code, we have to restart the
server so that it will have the latest copy of our code. PHP programmers
might found this daunting at first but if you already work in
application server model like Java you'll know that this is rather
typical because when the server is start, it already load our code into
memory, waiting to call some function when request came in. PHP due to
it's CGI-like manner is different because the whole code only executed
as part of the request.

Executing whole application code on each requests work best with PHP
because it's already been designed from the ground up as web language.
The standard library functions in PHP also been written in C so it's
already fast and executing that on each requests doesn't matter much.
Python however has most of it's standard library written in Python
itself which mean executing that on each request would be too slow.
You'll also facing the same problem in PHP once your code base grow to
certain level where you need to look for solution that cache the opcode
such as APC or eAccelerator.

Definitely there are more to discuss on the differences between PHP and
Python execution model for web application but I hope this post can
start giving you an idea why developing in Python a bit different than
what you already accustomed to in PHP. I'll try to expand this topic
more in upcoming posts and also welcome any suggestion to help PHP
developers to keep up fast in Python web development. Related reading
that help me a lot in understanding the difference between PHP and
Python web execution model is a blog post by Ian Bicking few years ago -
[What PHP Deployment Gets
Right](http://blog.ianbicking.org/2008/01/12/what-php-deployment-gets-right/).
