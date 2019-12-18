Title: My favorite tools to resolve git merge conflicts
Lang: en
Date: 2019-03-29 09:00
Author: Arthur Sultanbekov
Tags: git; 2019; tip; tool; code;
Slug: my-favorite-tools-to-resolve-git-merge-conflicts
Summary: Overview of some tools to resolve git conflicts

## Creating merge conflict
For sake of the demo, I'll use remote git repo, and locally cloned repos on 2 different instances.
I'll make changes in python's simple server script. The base is

```
...
    #Handler for the GET requests
    def do_GET(self):
        if self.path=="/":
            self.path="/home.html"

        if self.path=="/command/":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("transfer +79000000000")
            return
...
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' , PORT_NUMBER)
```

And now I make changes on instance1:

```
-            self.wfile.write("transfer +79000000000")
+            self.wfile.write("transfer +81500000000")
...
-    print('Started httpserver on port ' , PORT_NUMBER)
+    print('Run httpserver on port ' , PORT_NUMBER)
```

Then I commit and push this changes to remote.

Similarly, I make changes on local repo on instance2:

```
-            # Send the html message
-            self.wfile.write("transfer +79000000000")
+            # transfer to Arthur's celluar phone
+            self.wfile.write("transfer +79111111111")
...
-    print('Started httpserver on port ' , PORT_NUMBER)
+    print('Started httpserver on port %s' % PORT_NUMBER)
```

Then I commit these changes, and try to push, and get expected error:

```
$ git push origin temp-branch-for-demo
To gitlab.com:arthur-s/helper_scripts.git
 ! [rejected]        temp-branch-for-demo -> temp-branch-for-demo (fetch first)
error: failed to push some refs to 'git@gitlab.com:arthur-s/helper_scripts.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

So, git says that I should pull changes from remote. I pull changes, and get conflict:

```
$ git pull origin temp-branch-for-demo
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From gitlab.com:arthur-s/helper_scripts
 * branch            temp-branch-for-demo -> FETCH_HEAD
   bf69429..10d3974  temp-branch-for-demo -> origin/temp-branch-for-demo
Auto-merging python2-simple-server.py
CONFLICT (content): Merge conflict in python2-simple-server.py
Automatic merge failed; fix conflicts and then commit the result.
```

## How to resolve this conflict?
Conflict is a part of code, where SCM (git) cannot univocally determine which changes to use in merging file. In my case, I made changes on same parts of code
I open `python2-simple-server.py` and see this for first conflicting part:

```
<<<<<<< HEAD
            # transfer to Arthur's celluar phone
            self.wfile.write("transfer +79111111111")
=======
            # Send the html message
            self.wfile.write("transfer +81500000000")
>>>>>>> 10d39749eac26d53652df5c190927479c2bc34ec
```

So, here in the code I have uncertainty, git don't know what to choose - simply saying, transfer to `+79111111111` or to `+81500000000`. 
And I need to choose myself, which part to use, or maybe totally override this section. I can manually remove `<<<<<<<` and `>>>>>>>`, and edit content between this brackets. There's a merge tools, and I want to tell about my favorite ones.


## GUI tools
[Sublime Merge](https://www.sublimemerge.com/) is a powerfull merge tool, intuitively understandable and with good UI. It has free and commercial versions. Free version comes with light theme only, paid version has light and dark themes.

![Sublime merge conflict preview](/images/arthur-media/Screenshot_6_sm_preview.png)

![Sublime merge conflict resolve](/images/arthur-media/Screenshot_7_sm_resolve.png)

[VScode](https://code.visualstudio.com/#built-in-git) has integrated merge tool, also powerfull and with good UI.

![Visual Studio Code conflict resolve](/images/arthur-media/Screenshot_8_vscode.png)


## Console tool
Recently I openned for myself `vimdiff`, and very liked it. To work with this tool need to know `vim` basics, especially how to navigate between splitted windows (`Ctrl` + `w` + one of navigation keys. Navigation keys are `h`, `j`, `k`, `l`).

##### Setup process
Make vimdiff as default git merge tool:

```
git config merge.tool vimdiff
git config merge.conflictstyle diff3
git config mergetool.prompt false
```

There's 2 options for conflictstyle - `merge`, which is default option,  and `diff3`. Diff3 adds common ancestor in the view, it will be described below.

Now I may run conflict resolver as `git mergetool`:

![vimdiff resolver](/images/arthur-media/Screenshot_11_vimdiff.png)

At first glance this may be look ugly. But you may install attractive color schemas, and `vim` will be very nice looking. Sublime merge and VSCode both splits window to 3 parts. Vimdiff splits it to 4 (with `diff3` configstyle), displaying common ancestor

On the screenshot, from left to right, there's file with LOCAL version, on center - BASE version (common ancestor), and 3rd is REMOTE version. Window on the bottom is file which will be MERGED.

##### Resolving process
Since vim is an editor, which designed to work with keyboard only, without mouse, you need to use this commands to choose which version to use in conflicting part of code. Move your cursor to the highlighted conflict area, and choose one of this versions:

```
:diffg RE  " get from REMOTE
:diffg BA  " get from BASE
:diffg LO  " get from LOCAL
```

e.g. run `:diffg LO` to use local changes.
