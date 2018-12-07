Title: Binary operations
Date: 2018-11-22 12:00
Author: Arthur Sultanbekov
Tags: binary, operations;
Slug: binary-operations
Lang: en
Summary: Binary operations

# General
I'd like to write about bits, and how I understand them. We want from computer something, and write a program for it, in languages like Python, C, PHP or another, which is understandable for humans. But a computer doesn't understand such written code, and first, compilator translates this code into binary data. Binary data is a data, formatted specially for a computer. E.g. we want to do a simple operation like addition, 5+3. Or print something in the console. Or run the game, no matter, in every case compiler prepares binary data. To be true, compilator prepares byte-code, but by meaning it is a binary data.
Binary data, in simple words, is a consequence of 2 values - 0 and 1. 
1 byte consisting of 8 bits. As I remember from school, 1 byte has 8 bits, because such a number of bits is needed to store 1 symbol. 1 char is 1 byte. But it is not true, using python language I can show that 1 letter takes much more bytes:
```python
import sys
>>> sys.getsizeof('a')
50
```
So, 1 char in python takes 50 bytes, or 50x8=400 bits.
Interesting note, historically in different platforms there was bytes with 6,7,32,36 bits.

But my article will be about bits as mathematical numbers.

# Arithmetic
As we know, any number can be represented by base 10 (decimal), 2 (binary), 16 (hexadecimal), and any other. 1 bit can accept only two values - 0 or 1. Number, of course, can consist of any number of bits. Addition, Subtraction, Multiplication, and Division can be done on bin numbers like on regular decimal numbers.
In python bin numbers starts with prefix `0b`.
```python
>>> 0b0
0
>>> 0b1
1
>>> 0b10
2
>>> 0b11
3
>>> 0b11010
26
>>> 0b1+0b10
3
>>> bin(3)
'0b11'
>>> type(bin(3))
<type 'str'>
>>> int('11', base=2)
3
>>> int('0b11', base=2)
3
# we can prepend zeros on binary, it won't change it's value:
>>> int('01') ==  int('001') ==  int('000001') == 1
True 
1
```
In addition to ariphmetic operations, binary numbers also support boolean operations

# Boolean operations on bits
With some restrictions, boolean operations on bits came from Bool algebra. You may consider 1 as True, and 0 as False. Operations are:
* binary AND
* binary OR
* excluding binary OR (XOR)
* binary NOT

See tables below to understand rules of this operations.

### AND
Operator for OR for binary operations in python - `&`. If one of bits is 0, then resulted bit will be 0.
| A | B | A & B |
|---|---|---|
| 1 | 0 | 0 |
| 1 | 1 | 1 |
| 0 | 0 | 0 |
| 0 | 1 | 0 |

In practice this operation can be used for quick determination wheather number odd or not, by `x & 1` (if result is 0, then number is even, otherwise number is odd)
```python
>>> bin(0b1100 & 0b0101)
'0b100'
>>> bin(4)
'0b100'
>>> int(bin(4), base=2) & 1
0  # 4 is odd
>>> int(bin(5), base=2) & 1
1 # 5 is even
```

### OR
Operator for OR for binary operations in python - `|`. In simple words, this operation returns 1 (True) when at least one of bits is 1 (True).
| A | B | A \| B |
|---|---|---|
| 1 | 0 | 1 |
| 1 | 1 | 1 |
| 0 | 0 | 0 |
| 0 | 1 | 1 |

```python
>>> bin(0b1100 | 0b0101)
'0b1101'
```

### Excluding OR (XOR)
Operator for OR for binary operations in python - `^`. Similar to OR, but when two bits are 1, resulted bit will be 0.

| A | B | A \| B |
|---|---|---|
| 1 | 0 | 1 |
| 1 | 1 | 0 |
| 0 | 0 | 0 |
| 0 | 1 | 1 |


```python
>>> bin(0b1100 ^ 0b0101)
'0b1001'
```

### NOT
Reverse bits: 0 becomes 1, 1 becomes 0.
| A | 1 | 0 |
|---|---|---|
| ~A | 0 | 1 |

```python
>>> bin(~0b01)
'-0b10'
>>> -0b10
-2
```
Need to say, that when we use bitwise NOT on a number, it changes its sign to the opposite.

# Shifts
There's also _shift_ operations: In these operations, the digits are moved, or shifted, to the left or right by N indexes.

### Left shift
In this case, to the right end zeros added:
```python
>>> bin(0b10110100 << 1)
'0b101101000'
>>> bin(0b10110100 << 2)
'0b1011010000'
>>> bin(0b10110100 << 3)
'0b10110100000'
```

### Right shift
Bits shift to the right, from right side certain number of bits being dropped:
```python
>>> bin(0b10110100 >> 1)
'0b1011010'
>>> bin(0b10110100 >> 2)
'0b101101'
>>> bin(0b10110100 >> 3)
'0b10110'
```

# Where to use boolean operations on bits?
Mainly in programming bitwise operations are not commonly used.
1. Bitwise operations are used in cryptography.
2. If we have an IP-address, e.g. 192.168.8.2 and we know mask of a subnet, e.g. 255.255.248.0, we may determine bounds of IP addresses range for this subnet, and its address. To do this we must apply the mask to this IP address using logical AND:
```python
>>> bin(192)
'0b11000000'
>>> bin(255)
'0b11111111'
>>> 192 & 255
192
>>> 168 & 255
168
>>> 11 & 248
8
>>> 2 & 0
0
>>>
```
and as a result, we have 192.168.8.0, which is a subnet address.

3. Left and right shifts may be used to quick multiplication or division to 2^N. In this case speed will be faster, compared to using `*, /, **` operators.
```python
>>> 0b1
1
>>> 0b10
2
>>> 0b100
4
>>> 0b1000
8

>>> 50 >> 1
25
>>> 25 >> 1
12
```
Of course, there's another use cases of bitwise operations.
