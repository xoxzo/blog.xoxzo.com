Title: Use git pre-commit hook to Maintain Code Quality
Lang: en
Date: 2019-02-22 09:00
Author: Zaki Akhmad
Tags: code, quality, git, pre-commit, hook 
Slug: use-git-pre-commit-hook-to-maintain-code-quality
Summary: Automate checking code before committing it
Lang: en

Let say your company has coding standard. It is written somewhere in the
company documentation. As new onboard, you read this document thoroughly. Then
you start create your first pull request. Then you still left a trailing 
whitespace on some lines.

BTW, it is a good start that a company has coding standard. If a company
does not have or does not follow any existing coding standard, things will be
mess. As code is read much more often than it is written, we should have
convention on how we write code.

To enforce this coding standard, we can use git pre-commit hook. Let start from
the simplest one where we forbid a code to have a trailing whitespace. The first
thing you need to do is activate git pre-commit hook.

```
# Read the instruction in the file
$ vim .git/hooks/pre-commit.sample

# To enable this hook, rename this file to "pre-commit".
$ mv .git/hooks/pre-commit.sample .git/hooks/pre-commit
```

Try to make a commit with a trailing whitespace:

```
za@kwazii:02:49:04 {pep8-compliance} ~/dev/github/za/sandbox$ git diff HEAD

diff --git a/plant.py b/plant.py
new file mode 100644
index 0000000..b8904ac
--- /dev/null
+++ b/plant.py
@@ -0,0 +1,4 @@
+#!/usr/bin/python
+
+def sum(a, b):
+    return None  

```

Try to commit it:

```
za@kwazii:02:49:59 {pep8-compliance} ~/dev/github/za/sandbox$ git commit -v
plant.py:4: trailing whitespace.
+    return None  
```

So you cannot commit the code unless you have removed the trailing whitespace.
What if we want to enforce PEP8 compliance on each code? How we enforce this
using git pre-commit hook?

So, we will use existing git pre-commit hook file for PEP8 compliance. We will
use this [cbrueffer github repo](https://github.com/cbrueffer/pep8-git-hook):

```
# Download the pre-commit file
$ wget https://raw.githubusercontent.com/cbrueffer/pep8-git-hook/master/pre-commit

# Move it to .git/hooks folder
$ mv pre-commit .git/hooks/

# Set it as executable
$ chmod u+x .git/hooks/pre-commit
```

And now we need to setup virtualenv to install 
```
$ virtualenv -p `which python3` .venv
$ source .venv/bin/activate
(.venv)$ pip install pycodestyle
```

Try to commit a file which is breaking PEP8. Create the file.

```
#!/usr/bin/python


from datetime import *
def sum(a, b):
    return None

def div(a, b):
  return a/b  
```

Try to commit it.

```
(.venv)$ git add plant.py
(.venv)$ git commit -v

PEP8 style violations have been detected.  Please fix them
or force the commit with "git commit --no-verify".

./plant.py:5:1: E302 expected 2 blank lines, found 0
./plant.py:8:1: E302 expected 2 blank lines, found 1
./plant.py:9:3: E111 indentation is not a multiple of four
./plant.py:9:11: E226 missing whitespace around arithmetic operator
./plant.py:9:13: W291 trailing whitespace
```

Rather than doing it manually, we need to have this .git/hooks/pre-commit file
to automate the process of PEP8 code checking.
