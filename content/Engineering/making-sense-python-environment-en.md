Title: Making sense of Python environment
Date: 2020-05-09 12:00
Slug: making-sense-python-environment
Lang: en
Tags: python; venv; virtualenv; pyenv; conda
Author: Kamal Mustafa
Thumbnail: /images/python-env.png
Summary: Let try to understand all the tools in setting up python development environment. Venv, pip, pyenv, we got it covered.

It has become a joke among Python newcomer on the plethora of tools needed to 
setup your python environment. You probably has heard about virtualenv, venv, 
pip, pyenv, conda and few others.

It is quite understandable why this is overwhelming to newcomer, although I 
personally think it's not as bad as in JS land ;)

Actually, if you just want to start coding in Python, you don't really need all 
these tools. Just the python interpreter is enough to get you started. But of 
course no programming language will be complete (or fun enough) with just the 
standard libraries. Sooner or later you'll need to get someone else code to 
avoid you from rebuilding the wheel.

While getting simple module or package can be done manually, as long as you 
understand PYTHONPATH (which I think something that every python programmer 
[should know](https://blog.xoxzo.com/2017/06/21/understanding-python-import-1/)), some automation is needed to get more third party packages.

In Python land, most third party packages live in PyPI (Python Package Index).  
The standard tools to find and install packages from PyPI is pip but other 
tools also exists. Depending on how you get python on your system, it could be already pre-installed. But in case your python doesn't has it, it can be installed the following way:-

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

Then installing packages from PyPI is as simple as:-

    pip install <packagename>

While look simple, newcomer already facing a lot of problem here. The thing is, `python` the command used to install pip above, must come from somewhere. Many tutorials assume `python` is there and in most cases it is. But even it is there, it not necessarily the "python" that you want.

On Linux system, when you type the command `python` (or any command for that matter), the shell that executing your command must look in somewhere. The place to look for the command is defined in environment variables called `PATH`. This basically a list of directories where the shell will look for the command to execute. Below is example of PATH values on my system:-

```
echo $PATH
/home/kamal/.poetry/bin:/home/kamal/.cargo/bin:/home/kamal/.local/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/home/kamal/.local/share/flatpak/exports/bin:/usr/lib/jvm/default/bin:/usr/bin/site_perl:/usr/bin/vendor_perl:/usr/bin/core_perl:/var/lib/snapd/snap/bin
```

Above mean the shell will start searching from `/home/kamal/.poetry/bin/` up until `/var/lib/snapd/snap/bin`. It will stop searching if it can find the command. If it still can't find the command until the last directory in the list, it will give you "command not found" error, or anything equivalent.

So where `python` will come from? That will vary among system. This is on my system for example:-

```
which python
/usr/bin/python
```

So my `python` program actually coming from `/usr/bin/python`. You can see that `/usr/bin` was in the list of directories in my `PATH` above. Because my `python` is in the `PATH`, that mean I can simply type `python` to execute it. But you can still execute any command even though it's not in the PATH. In this case you have to type the full path to the command, such as:-

    /opt/my-python-installed-manually/3.8/bin/python

But that would be crazy if you have to type that all the time, right? That's why everyone want to use the short version, i.e just `python`.

The problem with the shorter version is that most people doesn't realize how it works underneath and it easy for them to forget or mix up. They type "python" hoping that it would come from `/opt/my-python-installed-manually/3.8/bin` while in fact it was coming from `/usr/bin`.

So lesson no. 1 - know your `python` and where it come from. That will save you lot of trouble later on.

Let's get back to installing pip above. When you run `python get-pip.py`, the `python` used might come from `/usr/bin/python`. By default, python will place the packages in a directory that relative to the python interpreter itself, in this case it will be in `/usr/lib/python3.7/site-packages`. The version number in `python3.7` however will depend on the version of `python` that you use. The problem is, writing to `/usr/lib/` will require admin privileges. Some will quick to suggest that you run your command with `sudo`. That's a bad advice. The python packages that you're trying to install can execute any arbitrary code and unlike OS packages that will go through some vetting, no one vet for the packages uploaded on PyPI. Anyone can upload code, good or bad, malicious or not to PyPI.

In practice, you should never use `python` to run your python code. That `python` is [not for you](https://dev.to/k4ml/system-python-is-not-for-you-e4g). It is called system python and that because your OS system (I'm talking about Linux like Ubuntu here) also use python a lot to manage the system. They have lot of python program so they need `python` to run it.

## venv

In python3, a module called `venv` is included by default. This is actually coming from a module called `virtualenv` back in Python2 days. On Ubuntu you still need to install it with `sudo apt install python3-venv`. This allow you to create a separate python environment:-

    python3 -mvenv myenv

This basically create a new copy of python in `myenv` directory. You can see in the directory something like:-

```
ls myenv/
bin  include  lib  lib64  pyvenv.cfg  share
```

You can even create this [manually](https://dev.to/k4ml/python-diy-virtualenv-5e4j) if you want. You'll see there's another "python" in `myenv/bin/python`. This is the "python" that you should use. You can run it as "myenv/bin/python". You'll also notice pip also included by default, so you can run it as "myenv/bin/pip" to install new packages. Many tutorials related to venv will suggest that you run the following command next:-

```
source myenv/bin/activate
```
That basically allow you to just type "python" and it will use `myenv/bin/python`. I would advice against this, at least not in the beginning.

When you install some packages like `myenv/bin/pip install requests`, the packages will be "installed" to `myenv/lib/site-packages` directory. You can verify this from python console:-

```
myenv/bin/python
>>> import requests
>>> requests
<module 'requests' from '/home/ubuntu/myenv/lib/python3.6/site-packages/requests/__init__.py'>
```
Your actual path of course will look different than mine.

So that's the second lesson - always use venv to create a separate environment for your project. In practice, each project will have it's own venv.

There are 2 situations actually when you want to use venv:-

1. For your programming project. As mentioned above, always create separate vm for each project. As you're progressing, you might feel that having to manage all this manually is cumbersome. You're not wrong to feel that. These days, I'm using [poetry](https://python-poetry.org/) most of the time to manage my project's venv. Let's delve into poetry in the next article, hopefully. There's also pipenv in the same space.
2. For installing program/application written in python. In this situation, also always create venv before installing the program. For example, if you want to install youtube-dl, do:-

    python -mvenv venv
    venv/bin/pip install youtube-dl
    venv/bin/youtube-dl

Similar to using venv in project, having to create new venv everytime you want to install new program also will start becoming cumbersome. These days, I'm using pipx to handle this.

    pipx install youtube-dl

`pipx` will install it to `$HOME/.local` directory where the executable `youtube-dl` will be placed in `$HOME/.local/bin`. Just make sure that directory is in your `$PATH`.

Another alternative is to use `--user` flag to `pip` which will also install the package to `$HOME/.local` dir but with pipx I no longer use that.

## pyenv

So we have done  with venv, what about pyenv? Most of the time you don't really need this. You'll need pyenv in the following situation:-

1. Your system doesn't has python version that you want. For example, your system only has python3.4 but you want to use python3.7. In this case you can get python3.7 through pyenv. But as I'm on Ubuntu most of the time, I prefer to use deadsnake/ppa instead to get python version that I need.
2. You need to use multiple version of python. For example your project must be tested against python2.7, python3.4, python3.6, python3.7 and python3.8. In this situation, pyenv can be helpful.


In short, pyenv give you different version of python. But do you still need venv if you already use pyenv? In general yes. As we can see above, pyenv only give different version of python. Back to lesson #2 above, you should always use separate venv for your project. The different is that now the python that will be used to create the venv "probably" come from pyenv instead of the system python. I put "probably" in quote because you have to be very certain here. So go back to the first lesson. This is one area that trip many people off. They don't really know which python they're using, once they have started using pyenv.

## Summary
We have come to an end and hopefully you have better idea now how to setup your python environment. Let's recap what we have learned so far:-

1. Always make sure you know which python you're currently using. Check, re-check and double check again, always. Follow the path mentioned in the error message that should bring you to the actual python being used.
2. Always use separate venv for each of your project or application that you want to install.
3. You might want to use multiple versions of python. In this case you can use pyenv, or deadsnake ppa if you're on ubuntu.

Till we meet again, happy coding.

## Updates

I noticed that `get-pip.py` script now by default will install to your local dir. Yeay!

```
python get-pip.py
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Downloading pip-20.1-py2.py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 9.3 MB/s
Installing collected packages: pip
  WARNING: The scripts pip, pip2 and pip2.7 are installed in '/home/ubuntu/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
```
