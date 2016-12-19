Title: Understanding Python Import
Date: 2011-11-22 16:32
Author: Kamal Mustafa
Tags: python
Slug: understanding-python-import

There's a lot have been written on understanding Python import so I'm
not sure whether this one would help to clear the confusion or just add
more. I hope for the former. Having a new hire who is new to Python
bring up this issue again for us.

Python has few ways to import other modules and has been greatly covered
in effbot's article - [Importing Python
Modules](http://effbot.org/zone/import-confusion.htm). Module in Python
is any file that end with .py. You can import it if you can somehow make
that file available on Python import path (more on this later). An
immediate companion to module is package - you can think of it as
collection of modules but there's much simpler definition - any
directory containing (even blank) file named as `__init__.py`.

So the first form of import in python which is the `import` statement
can only import a module or package. Let say we have this example module
named `sugar`.

    $ touch sugar.py
    $ python
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56)
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sugar
    >>> sugar

That's quite clear I think. We have file named `sugar.py` and then we
can import it from python interpreter executed within the same
directory. If there's a function named `is_sweet()` in `sugar.py`, we
can reference it now as `sugar.is_sweet()`. Following this, you might be
attempting to do the following:-

    >>> import sugar.is_sweet
    Traceback (most recent call last):
    File "<console>", line 1, in <module>
    ImportError: No module named is_sweet

As the error message say, there's no module name is\_sweet. Remember, we
can only import module (or package) ? `is_sweet` on the other hand is a
function so I hope this is pretty clear at this moment. There could be
few reasons why you want to import only specific object rather than the
whole module and since python doesn't allow this, is this the end of the
world ? Luckily python provide another form of import that is
`from ... import` or I prefer to illustrate it as
`from module|package import object`. So, continuing from previous
example:-

    >>> from sugar import is_sweet
    >>> is_sweet
    <function is_sweet at 0xb731de9c>

Now we can import `is_sweet` function from module `sugar`. So we can
import specific object from a module using
`from module|package import object` form. Noticed that I used the term
object here because in python everything is an object - module is
object, package is object, function is object, class is object etc. Let
say we reorganize our sugar module into a package.

    $ mkdir sugar
    $ touch sugar/__init__.py
    $ touch sugar/white.py

Here we added new module named `white` to `sugar` package. To
specifically import white module we can:-

    >>> import sugar.white
    >>> sugar.white
    <module 'sugar.white' from 'sugar/white.pyc'>

or:-

    >>> from sugar import white
    >>> white
    <module 'sugar.white' from 'sugar/white.pyc'>

Try to say this phrase again in your head for a few times -
`from module|package import object` - (In English - from a module or
package, you can import an object). Again, everything is object in
Python.

Import path
-----------

Now we understand how import work (hopefully), another question come up.
How does python know where to look for all these modules ? When trying
to import module, Python look through a list of path. This list is
stored under `sys` module and can be referenced as `sys.path`.

    >>> import sys
    >>> sys.path
    ['',
    '/home/kamal/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg',
    '/home/kamal/lib/python2.6/site-packages/pip-1.0.1-py2.6.egg',
    '/home/kamal/lib/python2.6/site-packages/patu-0.1-py2.6.egg',
    '/home/kamal/lib/python2.6/site-packages/lxml-2.3-py2.6-linux-i686.egg',
    ......

Python provide a number of ways for you to modify this list of path so
that module that you intended can be found. One of it by specifying
environment variable named PYTHONPATH.

    PYTHONPATH=/home/kamal/my-python-lib

From now on, any `*.py` file under `/home/kamal/my-python-lib` can be
imported if you execute python from that environment. Another way is to
modify `sys.path` directly and more convenient since you can do this in
the initial bootstrap code of your application.
