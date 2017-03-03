Title: Making Sense of Python App
Date: 2017-02-16 18:23
Lang: en
Author: Kamal
Tags: python
Slug: making-sense-python-app
Status: draft

1\. Those who new python, especially coming from PHP background, may look at Python as complex beast of stuff. Too many thing that look overly complex compared to what they used to in PHP.

2\. Computer program basically fall into 2 types - program that can execute itself, and program that depend on another program to execute it. Python fall into the second type.

3\. The typical way to run python application basically like this:-

    python yourapp.py

4\. We have learnt in no. 2 above that python program fall into program that need other program to execute it. So that's it. You can see above we 2 things:-

    - python
    - yourapp.py

5\. You might found python program that look like it can execute itself. Well, it just cheating, nothing magic about that. But let's talk about that in another topic.

6\. Let's get back to example in no. 3 and 4 above. Let's repeat again - python program fall into program that need other program to execute it. So as you can see in no. 4, we have 2 program there. The first program is called `python`. Depend on your Operating System (OS), there are a number of way to get it on your system - some people call it 'installation'. The second program - `yourapp.py`, is well ... your app. It's your application that you wrote in Python programming language. The code written in Python programming language, need a program called `python` to run it. That's the reason we have to run:-

    python yourapp.py

7\. Doesn't matter how big or small python program that you need to run, in whatever framework or using whatever libraries, the above concept remain the same. I repeat - remain the same. There's nothing magic going on. You might find the application that you want to run may hide the above fact in some funky command line wrapper, like they saying, just type this to run our magic funcky app:-

    funkyapp

8\. There's nothing magic. Ever.

9\. One thing that I usually observe is that, since the `funkyapp` above look like a magic, people just run it hoping for magic to happen and when something goes wrong, the app didn't want to start - they're lost. They don't know where to begin for troubleshooting.

10\. Another worst scenario is that, not enough giving magic to the `funkyapp`, the step to get to run `funkyapp` also being obscured in another script usually called 'installation script' or 'deployment script'. It make it worst because user don't really know what happen. They don't even know `funkyapp` exists because the script promise that when it finish, everything will run good and proper. The script lie.

11\. So how to troubleshoot when `funkyapp` don't want to start, or not running as expected ? Back to basic. You have to find those 2 program that we talked about in no. 3, 4 and 5 above. Find where's your PYTHON, and where is your APP ? It must be somewhere on the disk of your computer and when you found it, try to execute it directly:-

    python funkyapp.py
