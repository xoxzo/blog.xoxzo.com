Title: Binary operations
Date: 2018-11-22 12:00
Author: Arthur Sultanbekov
Tags: binary, operations;
Slug: binary-operations
Lang: en
Summary: Binary operations

# Ariphmetics
As we know, any number can be represnted by base 10 (decimal), 2 (binary), 16 (hexidimal). 1 bit can accept only two values - 0 or 1. Addition, Subsctraction, Multiplication and Division can be done on bin numbers like on regular decimal numbers.
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
```
In addition to ariphmetic operations, binary numbers also support boolean operations

# Boolean operations on bits
With some restrictions, boolean operations on bits came from Bool algebra. Bit can be considered as boolean True or False. Operations are:
* logical AND
* logical OR
* excluding OR (XOR)
* NOT

### AND
in python, `&` is for logical AND.
| A | 1 | 1 | 0 | 0 |
|---|---|---|---|---|
| B | 0 | 1 | 0 | 1 |
|A&B| 0 | 1 | 0 | 0 |

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
Operator for OR for binary operations - `|`.
| A | 1 | 1 | 0 | 0 |
|---|---|---|---|---|
| B | 0 | 1 | 0 | 1 |
|A\|B| 1 | 1 | 0 | 1 |
```python
>>> bin(0b1100 | 0b0101)
'0b1101'
```
### Excluding OR (XOR)
Operator for OR for binary operations - `^`. To get 1, only one of two bits can be 1
| A | 1 | 1 | 0 | 0 |
|---|---|---|---|---|
| B | 0 | 1 | 0 | 1 |
|A^B| 1 | 0 | 0 | 1 |

```python
>>> bin(0b1100 ^ 0b0101)
'0b1001'
```

### NOT
Reverse bits: 0 becomes 1, 1 becomes 0.
| A | 1 | 0 |
|---|---|---|
| ~A | 0 | 1 |

# Shifts
left shift:
```python
>>> bin(0b10110100 << 1)
'0b101101000'
>>> bin(0b10110100 << 2)
'0b1011010000'
>>> bin(0b10110100 << 3)
'0b10110100000'
```
right shift:
```python
>>> bin(0b10110100 >> 1)
'0b1011010'
>>> bin(0b10110100 >> 2)
'0b101101'
>>> bin(0b10110100 >> 3)
'0b10110'
```

# Where to use boolean operations on bits?
In real everyday programming we don't use bit operations.
1. Mainly boolean operations are used in cryptography.
2. If we have an IP-adress, e.g. 192.168.8.2 and we know mask of subnet, e.g. 255.255.248.0, we may determine bounds of ip adresses range for this subnet, and it's adress. To do this we must apply mask to this IP adress using logical AND:
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
and as a result we have 192.168.8.0, which is a subnet adress.

3. Left and right shifts may be used to quick multiplication or division to 2^N. In this case speed will be much faster, compared to using `*, /, **` operators
