Title: A python basic class in Tokyo Feb 6, 2016
Date: 2016-02-15 09:18
Author: Aiko Yokoyama
Tags: python
Slug: a-python-basic-class-in-tokyo-feb-6-2016

[![logo](https://xoxzoblog.files.wordpress.com/2016/02/logo.png?w=150)](https://djangogirls.org/)

I have attended an event of Django Girls Japan and Python ladies, a
Python basic.

<http://djangogirls-org.connpass.com/event/25660/>

**1. An introduction**  
We had 8 girls attended with 1 instructor and 3 mentors.  
6 students from within Tokyo and 1 from Nagoya and me from Kyoto.  
**2. Session**  
Using a text book of <http://www.amazon.co.jp/dp/4797371595>

We pre-read a half of the text before arrival, brought in some questions
about. As most of us were really beginners at Python, (0 - 2 years) none
of us really had good knowledge to even make questions.

The instructor thinks the basic level that he wanted us to have today is
to have an 'idea' of python.

He gave us some time to think about:  
- What is Data types, what will be problems if mis-treat the data
types.  
- What is Collection type data, and what are list, dictionary and taple,
their data rules and how to define.

Also,  
- What is Functions, what is Argument and what is returned value exactly
mean.  
&gt;&gt;  
I had some rough or general idea about them but as he explained as  
Function is like a factory  
Argument is like a reception that would take the orders/materials  
Return value is like a completed product made at the factory  
was very helpful.

Also then we students wondered what is modules then, so we challenged
onto some exercise to see what it is.

exercise 1  
a. Use 'For' and create a program that shows from 1 to 100  
b. Use 'if' to edit that program to show the numbers only over 30  
c. Edit that program to show only even numbers  
d. Edit that program to show only even numbers/over 50  
e. Edit that program to show only odd numbers

exercise 2  
Create a game program that we can play paper-scissors and rock.

When I compared my codes with the instructor's, I felt mine is like a
kinder-child made ...

     #-*- coding: utf-8

    ## まず、モジュールを読んでくる##
     import random

    ## randomモジュールにある、randint()という関数を使う##

    print ("じゃんけんをしましょう！
     1 = グー、2 = チョキ、3 = パー")

    ##　両者の手をみる ##
     cpu = random.randint(1,3)
     user = int(input())

\#\# 勝ち負けの判定 \#\#  
if user == 1:  
if cpu == 1:  
print ("あなたはグー、CPUもグー、「あいこ」です！")  
if cpu == 2:  
print ("あなたはグー、CPUはチョキ、あなたの勝ちです！")  
else:  
print ("あなたはグー、CPUはパー、あなたの負けです！")

if user == 2:  
if cpu == 1:  
print ("あなたはチョキ、CPUはグー、あなたの負けです！")  
if cpu == 2:  
print ("あなたはチョキ、CPUもチョキ、「あいこ」です！")  
else:  
print ("あなたはチョキ、CPUはパー、あなたの勝ちです！")

if user == 3:  
if cpu == 1:  
print ("あなたはパー、CPUはグー、あなたの勝ちです！")  
if cpu == 2:  
print ("あなたはパー、CPUはチョキ、あなたの負けです！")  
else:  
print ("あなたはパー、CPUもパー、「あいこ」です！")  
But, anyways, this is the start of learning. I am glad that I have made
a first step.
