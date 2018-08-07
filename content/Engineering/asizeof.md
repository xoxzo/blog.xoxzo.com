Title: Asizeof module usage
Date: 2018-08-07 06:00
Author: Arthur Sultanbekov
Tags: asizeof; memory; tools; python; pympler;
Slug: asizeof-usage
Lang: en
Summary: Asizeof can be used to investigate memory leaks

Sometimes your programm starts eating a lot of memory, and you try to find out where is problem. There's variety of tools that can help you, and I wanted to tell about simple tool named `asizeof` of  [Pympler](https://pythonhosted.org/Pympler/) lib.

Pympler has 2 trackers to measure, monitor and analyze the memory behavior of Python objects. This trackers are `muppy` and `Class Tracker`, they also can help you investigate memory leaks.

There's built-in `sys.getsizeof()` method, which returns size of pure python object only. Let's see an example:
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
>>>
```

In contrast, `asizeof.asizeof()` recursively searchs for inner values, and counts whole size of object, including size of inner items:
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
>>> 
```

Checking size of values in your script, using `asizeof`, you can find a bottleneck in your script. In complex and complicated scripts another more convinient tools can be used, but in small scripts `asizeof` can be used. Also `asizeof` can be used in `for` loops, or when you want to get exact size of some value (it's harder to do with another heavier tools).

Let's see an example:

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

If we run `investigated_function()`, it will eat our memory, and we want to investigate where's the problem. You just check values, e.g.:
```python
print( asizeof.asizeof(sometuple) )
print( asizeof.asizeof(empty) )
print( asizeof.asizeof(dummy) )
168
152
4195944
```

and you see that problem is in `dummy` instance, which is 4,195,944 bytes, which is around 4Mb. Also you can use `asizeof.asizesof` function (plural, "A Sizes Of"):
```python
print( asizeof.asizesof(dummy.a, dummy.b, dummy.c, dummy.d) )
# returns sizes of individual values
(592, 512, 4194368, 472)
```

And from command above we can see, that `dummy.c` takes a lot of memory, which is an attribute of Dummy class:
```python
self.c = bytearray(1024*1024*4)
```
