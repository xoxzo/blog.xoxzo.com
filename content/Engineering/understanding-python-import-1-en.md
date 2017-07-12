Title: Understanding Python Import
Date: 2017/06/21 09:52
Author: Kamal Mustafa
Tags: python; import; sys.path;
Slug: understanding-python-import-1
Lang: en
Summary: Let’s learn more about search path for Python import

Failing to import module/packages in python is no #1 problem faced by any python programmers. It is so common that I think it's not too much if I say, 80% of what they need to know to become python expert already covered if they manage to understand this part of python.

The import mechanism in python actually very simple (it's not actually because some [black magic][lucumr] involved). But let's just pretend for now the black magic didn't exists. There are only 2 things that can affect import in python.

```
PYTHONPATH
sys.path
```

The later is build upon the former. So whenever you can't import some modules or packages (you know what the difference between module and package, right ?), this is the 2 places you want to check. Or if you want to alter the behavior of the import, this also 2 things you want to poke around.

By the default, `sys.path` is filled in with a number of entries. For example, on ubuntu 14.04:-

```
>>> import sys
>>> sys.path
['', '/home/kamal/.local/lib/python3.4/site-packages/Baker-1.3-py3.4.egg', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/home/kamal/.local/lib/python3.4/site-packages', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages', '/usr/lib/python3.4/dist-packages']
>>> len(sys.path)
9
```

What path get added to sys.path heavily influenced by `site` module which automatically imported when you launch python. We can suppress this by using `python -S`. This is what I got after using that flag:-

```
>>> import sys
>>> sys.path
['', '/usr/lib/python3.4/', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload']
```

You can see that it lot less that the first one. This default entries in sys.path usually the location of the standard library. This what make `import os`, `import json` actually work. Ok, I'm wrong. The path to standard lib seem to be hardcoded in the binaries, maybe using combination of sys.prefix + 'lib' + sys.version.

So again, this is the place to check if you can't import certain module (or packages). Using [buildout], it goes one step further. Buildout rebuild sys.path and add all the paths to the eggs directories so you can exactly know if the packages you want to import is not there, then obviously you can't import it.

Hopefully after reading this, you won't have any issue with importing module (or packages) in python. Or if you still have, at least you know where to look for.

[reference URL](https://docs.python.org/3/library/sys.html?highlight=sys.path#sys.path)
[lucumr]:http://lucumr.pocoo.org/2011/9/21/python-import-blackbox/
[buildout]:http://www.buildout.org/
