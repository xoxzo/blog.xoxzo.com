Title: Some powerful features of Python
Date: 2019-10-29
Slug: powerful-features-python
Lang: en
Tags: python; programming; code;
Thumbnail: images/pythonlogo.jpg
Author: Surya Banerjee 
Summary: This article will talk about a few features which I personally find distinctive of the Python language.



Coding in Python for a year now has been quite a pleasurable experience and frankly I would trade it for no other language given that the simplicity of Python provides a much more friendly learning curve than anything else out there. For example, in Python, nothing obliges you to write classes and instantiate objects from them. If you don’t need complex structures in your project, you can just write functions. Even better, you can write a flat script for executing some simple and quick task without structuring the code at all.

 
Python’s philosophy is built on top of the idea of well thought out best practices. Python is a dynamic language and as such, already implements, or makes it easy to implement, a number of popular design patterns with a few lines of code. However, Python programs are easily scalable and the language is versatile enough to provide various degrees of control which as and when needed can be used to solve problems in a much efficient way. This article will talk about a few of those features which I personally find distinctive of the Python language.

  

## Understanding the double-underscore( __ ) of Python

Methods that begin and end with a double underscore are called dunder (a contraction of “double underscore”) or magic methods.

What’s the magic? Well, they are never called directly–instead, they are called via a mapping from a built-in function or operator, or, in the case of \__init__, it is called automagically when an object is created.

Let’s start with \__init__, since it’s the first one people typically learn:

    class Thing:
        def __init__(self):
            print('In __init__!')
        
    >>> t = Thing()
    In __init__!
    

So you see that \__init__ an initializer method is called when I created a new Thing object.

Suppose I want to add two Thing objects together–it doesn’t work, because my Thing type has not defined what it means to add two Things:

    >>> t1 = Thing()
    In __init__!
    
    >>> t2 = Thing()
    In __init__!
    
    >>> t1 + t2
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'Thing' and 'Thing'

Let’s fix that:

    >>> class Thing:
    ...	def __init__(self, moniker):
    ... 		self.moniker = moniker
    ...
    ... def __add__(self, other):
    ... 	print('In __add__!')
    ... 	return Thing(self.moniker + ' ' + other.moniker)
    ...
    >>> t1 = Thing('one')
    >>> t2 = Thing('two')
    >>> t3 = t1 + t2
    In __add__!
    
    >>> t3.moniker
    'one two'

So now we see that we can use the good old plus sign for addition, and when we do that, Python invokes the __add__ method for Thing objects.

We could invoke __add__ directly, even for integers, if we wanted:

    >>> int.__add__(2, 2)
    4

    

We could say that operators such as + invoke dunder methods under the hood.

But sometimes Python’s built-in functions invoke dunder methods. len() is a good example:

    >>>len('Python')
    6
    >>>'Python'.__len__()
    6
    

So when we call len() on an object, Python invokes __len__() for that object. Let’s try it on an int:

    >>> x = 4
    >>> len(x)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: object of type 'int' has no len()


The only reason it doesn’t work is because the int object has no __len__() method, not because integers are not iterable. Let’s create an int type which has a __len__() method:

    >>> class autolen(int):
    ... def __len__(self):
    ... return len(str(self))

    

The autolen object inherits from int and adds a __len__() method which returns the number of digits in the autolen:

    >>> x = autolen(12345678)
    >>> x ** 2
    152415765279684
    >>> len(x)
    8
    
So we can do int-y stuff with our autolen objects (since it inherits from int) and we can also call len() on them.

There is an exhaustive list of all such special functions, go check them out: https://docs.python.org/3/reference/datamodel.html#special-method-names  
  

  
## What is meta of classes?

A metaclass is the class of a class. A class defines how an instance of the class (i.e. an object) behaves while a metaclass defines how a class behaves. A class is an instance of a metaclass.

While in Python you can use arbitrary callables for metaclasses, the better approach is to make it an actual class itself. type is the usual metaclass in Python. type is itself a class, and it is its own type. You won't be able to recreate something like type purely in Python, but Python cheats a little. To create your own metaclass in Python you really just want to subclass type.

A metaclass is most commonly used as a class-factory. When you create an object by calling the class, Python creates a new class (when it executes the 'class' statement) by calling the metaclass. Combined with the normal \__init__ and \__new__ methods, metaclasses therefore allow you to do 'extra things' when creating a class, like registering the new class with some registry or replace the class with something else entirely.

When the class statement is executed, Python first executes the body of the class statement as a normal block of code. The resulting namespace (a dict) holds the attributes of the class-to-be. The metaclass is determined by looking at the baseclasses of the class-to-be (metaclasses are inherited), at the \__metaclass__ attribute of the class-to-be (if any) or the \__metaclass__ global variable. The metaclass is then called with the name, bases and attributes of the class to instantiate it.

However, metaclasses actually define the type of a class, not just a factory for it, so you can do much more with them. You can, for instance, define normal methods on the metaclass. These metaclass-methods are like classmethods in that they can be called on the class without an instance, but they are also not like classmethods in that they cannot be called on an instance of the class. type.\__subclasses__() is an example of a method on the type metaclass. You can also define the normal 'magic' methods, like \__add__, \__iter__ and \__getattr__, to implement or change how the class behaves.

Now let's simplify what all that jargon means. Let’s consider a situation where a company has 2 teams, one for writing the library for the system while the other team is responsible for more of the application/business logic. The application developers thus use the libraries created for them by the library team. Now, say the application developer wants to be sure that there is a particular method defined in a class from the library from which a derived class is created in the application code. The easiest way to check it would be something like this.  
  

    assert hasassert (BaseClass, MethodToCheck), “Its not there”  

  

So this is an example of a derived class enforcing some constraints on the base class. How about when the library developers want the base class to enforce some constraints on the derived class? Perfect excuse to use metaclasses!  
  

    class BaseMeta(type):
	    def __new__(cls, name, bases, body):
    
	    if not 'bar' in body:
		    raise TypeError('Derived class does not have bar defined')
    
	    return super().__new__(cls, name, bases, body)

    class Base(metaclass=BaseMeta):
	    def foo(self):
		return self.bar()  

Here we define the metaclass deriving from the class ‘type’ which checks for the bar method in the derived class and returns an error when it is unable to find it defined. This is the perfect example of one of the key use cases of metaclasses.
  
## A pinch of syntactic sugar called decorators

Let’s start with the basics: Everything in Python is an object. So functions are objects too. Now that means we could have functions as arguments passed on to another function. These functions are called higher-order functions. Thus, a higher-order function is a function that takes one or more functions as inputs and returns a function. I.e.  
  

    h(x) = f(g(x))  

  

where here f() is a higher-order function that takes a function of a single argument, g(x), and returns a function of a single argument, h(x). You can think of f() as modifying the behaviour of g().  
  
Decorators are syntactic sugar for applying in Python. They make an ugly statement look pretty, that's it.  
  
Here is the decorator syntax,

    @helloGalaxy
    @helloSolarSystem
    def hello(targetName=None):

  

is equivalent to,

    hello = helloGalaxy(helloSolarSystem(hello))

  

So, this is a illustrative description of a decorator. Read through the comments.  
  

    # A decorator is a function that expects ANOTHER function as parameter
    def my_shiny_new_decorator(a_function_to_decorate):
	    def the_wrapper_around_the_original_function():
		    print 'Before the function runs'
	        a_function_to_decorate()
	        print 'After the function runs'
	    
	    return the_wrapper_around_the_original_function
    
      
    
Now imagine you create a function you don’t want to ever touch again.

    def a_stand_alone_function():
    	    print 'I am a stand alone function, don’t you dare modify me'
        
        a_stand_alone_function()

__Output:__ `I am a stand alone function, don't you dare modify me`

Well, you can decorate it to extend its behavior. Just pass it to the decorator, it will wrap it dynamically in any code you want and return you a new function ready to be used:

  

    a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
    
    a_stand_alone_function_decorated()

 

And this is exactly equal to -  
  

    @my_shiny_new_decorator  
    a_stand _alone_function  

__Output:__

    Before the function runs
    I am a stand alone function, don't you dare modify me
    After the function runs

  
  

# Iterators and Generators, what are they?

In Python, an iterator is an object which implements the iterator protocol. The iterator protocol consists of two methods. The \__iter__() method, which must return the iterator object, and the next() method, which returns the next element from a sequence.

Iterators have several advantages:

-   Cleaner code
    
-   Iterators can work with infinite sequences
    
-   Iterators save resources
    

Python has several built-in objects, which implement the iterator protocol. For example lists, tuples, strings, dictionaries or files.

      
    
    # iterator.py
    str = "formidable"
    
    for e in str:
	    print(e, end=" ")
    
    print()
    
    it = iter(str)
    print(it.next())
    print(it.next())
    print(it.next())
    print(list(it))

  

In the code example, we show a built-in iterator on a string. In Python a string is an immutable sequence of characters. The iter() function returns an iterator on object. We can also use the list() or tuple() functions on iterators.

  

To understand this better, let’s pretend that we want to create an object that would let us iterate over a linear sequence of numbers(incremented by 1).  

class Linear_sequence:
    def __init__(self):
            self.initial = 0
            self.max = 20

    def __iter__(self):
            # Return the iterable object (self)
            return self

    def next(self):
            # When we need to stop the iteration we just need to raise
            # a StopIteration exception
            if self.initial > self.max:
                    raise StopIteration



            # save the value that has to be returned
            value_to_be_returned = self.initial + 1

            # calculate the next values of the sequence
            self.initial += 1

            return value_to_be_returned

    def __next__(self):
            # For compatibility with Python3
            return self.next()

if __name__ == '__main__':
    seq = Linear_sequence()
    for number in seq:
            print(number)

As you can see, all we’ve done is creating a class that implements the iteration protocol. This protocol is contained in two methods: the “iter” method that returns the object we would iterate over and the “next” method that is called automatically on each iteration and that returns the value for the current iteration.

  
Please note that the protocol in Python 3 is a little different and the “next()” method is called “\__next__()”  
  

**Now, lets move on to Generators.**


Generators in Python are just another way of creating iterable objects and are usually used when you need to create iterable object quickly, without the need of creating a class and adopting the iteration protocol. To create a generator you just need to define a function and then use the yield keyword instead of return.

So, the Linear sequence in a generator could be something like this:

    def linear_sequence(max):
    a = 0
    while a < max:
        a += 1
        yield a


Yes, so simple! Now, if you want to test it just use your new linear sequence generator function:

    if __name__ == '__main__':

    linear_generator = linear_sequence(20)
    # print out all the sequence        
    for number in linear_generator:
        print(number)

  
Every generator is an iterator, but not vice versa. A generator is built by calling a function that has one or more yield expressions (yield statements, in Python 2.5 and earlier), and is an object that meets the previous paragraph's definition of an iterator.

You may want to use a custom iterator, rather than a generator, when you need a class with somewhat complex state-maintaining behavior, or want to expose other methods besides next (and \__iter__ and \__init__). Most often, a generator (sometimes, for sufficiently simple needs, a generator expression) is sufficient, and it's simpler to code because state maintenance (within reasonable limits) is basically "done for you" by the frame getting suspended and resumed.

  
So the topics covered show a small glimpse of what power the Python programming language gives us, hence someone can start learning the basics and the rest is taken care of by Python. However, once someone gets better at it, they have more control and ability to take over much of the action that happens under the hood and build out to their desired results.
