Title: Recognition of Python Import
Date: 2017/06/19 14:00
Author: Akira Nonaka
Tags: python; import; sys.path;
Slug: about-python-import
Lang: en
Summary: Let’s learn more about search path for Python import

It is a frequent problem for Python programmers that modules or packages that they want to `import`
are not found.

```
>>> import foo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'foo'
```
The first step to solving this problem is to recognize that the variable named `sys.path` is
where the Python interpreter goes to look to find the modules and packages that its supposed to import.
The format of this variable is a list.

For example, on `Ubuntu 14.04` that I have here it will be like this:
```
$ /usr/bin/python3
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', 
    '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages',
     '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
>>> print(len(sys.path))
7
```

The path `sys.path` is highly depended on the package called `site` which is loaded by default.
You can use an option `-S` when you launch Python interpreter not to load `site` package.
Here we can see the contents of `sys.path` when we manually `import` `site`.

```
$ /usr/bin/python3 -S
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python3.4/', '/usr/lib/python3.4/plat-x86_64-linux-gnu', 
    '/usr/lib/python3.4/lib-dynload']
>>> print(len(sys.path))
4
>>> import site
>>> print(len(sys.path))
7
```

There will be `sys.path[0]` which is the Python script's directory when launching the Python Interpreter
and is at the beginning of this list. This means that the directory of the script when executed launched
will also be searched by `import`

`sys.path[0]` will be empty when Python Interpreter was launched interactively: This basically points to
the current directory.

Be aware of the value of environmental variable `PYTHONPATH` that is inserted in `sys.path`
at the launch and it must be right after `sys.path[0]`

```
$ export PYTHONPATH="/foo/bar/baz"
$ /usr/bin/python3
>>> import sys
>>> print(sys.path)
['', '/foo/bar/baz', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', 
    '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', 
    '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
```

`sys.path` can also be modified as you like, for example, you can add your favorite directory in search
path of `import` from Python script as following.

```
>>> sys.path[0:0]=['/my/python/dir']
>>> print(sys.path)
['/my/python/dir', '', '/foo/bar/baz', '/usr/lib/python3.4', ...
```

[reference URL](https://docs.python.org/3/library/sys.html?highlight=sys.path#sys.path)
