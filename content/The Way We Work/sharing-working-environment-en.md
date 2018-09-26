Title: Sharing Our Working Environment
Date: 2018-08-02 14:00
Author: Zaki Akhmad
Tags: environment; work; tools; python; zsh; vscode; team-camp;
Slug: sharing-our-working-environment
Lang: en
Summary: Looking at others working environment during our team camp might improve productivity

On July 2018, we had another [team camp](https://blog.xoxzo.com/tag/team-camp/).
This time we had it in Kuala Lumpur. It is always an interesting and exciting
moment when you can meet and work in the same place with your colleague since
Xoxzo is a
[remote-working company](https://blog.xoxzo.com/2016/04/22/the-communication-costs-of-remote-work/).

![KL team camp 2018](/images/kl-team-camp-2018.jpg)

We have policy not to download the source code into our local computer. We are
never dictating everyone on how they should work, so everyone is free to work as
long it complies with the policy.

And people work differently. Some of us prefer just to use a plain text editor, and
some of us said, he could not live with terminal anymore.

On one of the session during the team camp, we shared on how we work. How is our
working environment look a like. How we setup our tools to improve productivity.

For example, I shared on how I use [vim-flake8](https://github.com/nvie/vim-flake8)
on my vim to automatically check the code for [PEP8](https://www.python.org/dev/peps/pep-0008/)
compliance. Everytime I save a Python file, flake8 will automatically check for:

* unused but imported modules
* unused variables
* syntax error
* spacing suggestion
* new line suggestion

For example I have this on my Python source code:
```
1 #!/usr/bin/python
2
3 from datetime import datetime
4
5 import django
6
7
8 now = datetime.now()
9 yesterday = timedelta(days=1)
10
11
```

And when I type :wq (save and quit on vim), vim will send a warning message:
```
1 example.py|5 col 1| F401 'django' imported but unused
2 example.py|9 col 13| F821 undefined name 'timedelta'
3 example.py|11 col 1| W391 blank line at end of file
```

This will definitely increase my productivity since I do not need to check
above error/warning manually by checking line-by-line.

Then my friend showed that there are lot of things we can do using Microsoft
Visual Studio Code: such as compare the diff, making commits, and also check
for syntax error. Even nowadays, VS Code is available in non-Windows
environment including [GNU/Linux](https://code.visualstudio.com/docs/setup/linux).

For shell, one of our team member was showing zsh. I was interested to switch to
zsh shell from the classic bash shell. zsh has one popular framework called
[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh).

It has a lot of plugins collection. One thing I notice that zsh can
do is that we can checkout to a branch without have to type the full branch
name. We can just type the keyworod and zsh will find it for us. For example:

```
$ git checkout -b PROJECT-123-update-readme
$ git checkout master

# Just type the keyword of the branch name and press tab
$ git checkout 123
# zsh will find it for you

$ git checkout PROJECT-123-update-readme
```

We also had the chance to see how our front end engineer work. This thing is a
completely different from what my day-to-day work. She showed the tools on
creating icon, wireframe, and then implement it via code. Things that I have
never done it, as a backend engineer.

I have been using a plain text editor and using bash for a quite long time until
now. Then I am thinking, why not to give it a try the IDE text editor and zsh.
_There should be always a room to try something new, right?_
