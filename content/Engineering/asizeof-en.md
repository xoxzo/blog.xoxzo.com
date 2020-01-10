Title: Asizeof module usage
Date: 2018-08-08 06:00
Author: Arthur Sultanbekov
Tags: tool; python; 2018;
Slug: asizeof-usage
Lang: en
Summary: Using asizeof module to investigate memory leaks

Sometimes your program starts to eating a lot of memory, and you try to find out
where is problem. There is variety of tools that can help you, and I wanted to
tell about simple tool named `asizeof` of
[Pympler](https://pythonhosted.org/Pympler/) lib.

Pympler has 2 trackers to measure, monitor and analyze the memory behavior of
Python objects. These trackers are `muppy` and `Class Tracker`.
They also can help you investigate memory leaks.

There is a built-in `sys.getsizeof()` method, which returns the size of pure
Python object only. Example:

```python
>>> import sys
>>> sys.getsizeof(None)
16
>>> sys.getsizeof([])
64
>>> sys.getsizeof('a')
50
>>> sys.getsizeof(['a'])
72
>>> sys.getsizeof(['avadakedavra'])
72
```

In contrast, `asizeof.asizeof()` recursively searches for inner values, and
counts whole size of object, including size of inner items:

```python
>>> from pympler import asizeof
>>> asizeof.asizeof(None)
16
>>> asizeof.asizeof([])
64
>>> asizeof.asizeof('a')
56
>>> asizeof.asizeof(['a'])
128
>>> asizeof.asizeof(['avadakedavra'])
136
```

You can find a bottleneck in your script using `asizeof` by checking the size of
values in your script. In complex and complicated scripts, probably we will need
another more convenient tools, but in small scripts `asizeof` will be handy.

Asizeof can be used when you intuitively guess which variable can be problematic,
and check its size, and to confirm the hunch. But if you totally do not know where
the issue may be, and if your problematic code consist of dozens or
hundreds of lines, then better to use memory profilers, because you cannot write
`print(asizeof())` on every variable.

Example:

```python
from pympler import asizeof

class Empty(object):
    pass

class Dummy(object):
    def __init__(self):
        self.a = ['apple', 'banana', ['foo', 'bar', ['tiger', 'leo']]]
        self.b = {'key1': 'val1', 'key2': 'val2'}
        self.c = bytearray(1024*1024*4)
        self.d = self


def investigated_function():
    sometuple = (4, 10, -2,)
    for i in range(1000):
        empty = Empty()
        dummy = Dummy()
        # do_something_with(dummy)
        
```

If we run `investigated_function()`, it will consume our memory, and we want
to investigate where is the problem. You just check values, e.g.:
```python
print( asizeof.asizeof(sometuple) )
print( asizeof.asizeof(empty) )
print( asizeof.asizeof(dummy) )
168
152
4195944
```

and you can see that problem is in `dummy` instance, which is 4,195,944 bytes,
which is around 4Mb. Also you can use `asizeof.asizesof` function
(plural, "A Sizes Of"):

```python
print( asizeof.asizesof(dummy.a, dummy.b, dummy.c, dummy.d) )
# returns sizes of individual values
(592, 512, 4194368, 472)
```

And from above command we can see, that `dummy.c` takes a lot of memory, which
is an attribute of Dummy class:

```python
self.c = bytearray(1024*1024*4)
```
