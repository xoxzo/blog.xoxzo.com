Title: Security in Software Development Life Cycle (SDLC) - Guest Lecture at University of Indonesia
Date: 2017-04-20 06:30
Author: Zaki Akhmad
Tags: security, sdlc, university of indonesia, computer science
Lang: en
Slug: security-in-sdlc
Summary: The Security Aspect in the Software Development Life Cycle (SDLC)

Last Thursday, I was giving a guest lecture at University of Indonesia about
Security in SDLC (Software Development Life Cycle). It is nice to be back in
campus and meet students. I arrived a bit early to prepare everything and just
to make sure my presentation went smooth.

I used to be a penetration tester and breaking stuff, but now I am building the
application. Having a security in mind while developing application is not easy.
Why I should care about security while the main functionalities is not working
yet?

At first, I explained the theory of security in SDLC. Where the penetration test
position in SDLC and told them that even a penetration test cannot ensure that
our application is secure.

Some people said a penetration test is like testing your car security with
front-impact crash only, while you do not care about the side-impact or the
back-impact or event the top-impact crash.

But in real life, I said people still asking for penetration test. Why? Because
penetration test is the easiest way to have a security snapshot from your
application. Reviewing code or audit all the components will take too much time
and costly. The correct way based on text-book, you should include security
aspect on every aspects of the SDLC.

Now, the programmers should have security in mind while developing application.
They should write test code! Yes, writing test code is hard. But once you start
developing with TDD (Test Driven Development) your application will be more
robust and you can do development better and faster. If the programmers write
the code securely the chance of having a security vulnerability will be lesser.

Write test code not only the expected case, but also the alternate case. What if
the username contains single quote, dash, or any other special characters. Try
to think out of the box. What if someone attempts to login 1000 times with
wrong password? What should our application do?

Of course, within 2 hours is impossible to explain all the details. The objective
of this lecture is to build security awareness for students that is important
to write a secure code and have enough test while building the application. We do
not want to build an application which leaks our customer personal information
right? And when we build an application which includes financial transactions,
security is a must.

As usual, I gave small present to students who were asking questions. There is
one good question which I do not have an answer yet. I shared my experience while
doing network forensic to investigate a SQL injection attack. Then this student
asked me, is it possible for us to know in real time that we have a SQL
injection vulnerability or our database might already have injected? A WAF
(Web Application Firewall) might be helpful to inspect the traffic coming to
our application, but I do not know for sure yet.

At the end of session, I quickly asked students what programming language they
use for developing application. Surprisingly PHP still popular! While only few
students use Python.

![the students]({filename}/images/security-in-sdlc-2017.jpg)
