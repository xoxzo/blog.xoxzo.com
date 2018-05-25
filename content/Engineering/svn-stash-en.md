Title: Svn stash
Lang: en
Date: 2012-03-09 19:32
Author: Kamal Mustafa
Category: Engineering
Tags: git, svn, version control
Slug: svn-stash
Summary: regarding `stash` command.

Update 2012-05-02 - Add new use-case when merging from trunk.

------------------------------------------------------------------------

One thing I like in git is the `stash` command. Basically what it's
doing is  
to take out current changes that we have, store it in temporary place
and then  
revert our repo to it's previous pristine state. This has a number of
use cases.  
Let say you're working on some features and then got some bug report
that need  
to be fixed quickly. You may do new checkout in other location and do
the bug  
fixing work, commit it and then continue on your new features work. This
may not  
really prevalent if you work in branch since the bug might need to be
fixed in  
another branch. `git branch` does the job here since it allow you to
quickly  
switch branch.

Now back to us who still stuck with svn. Nothing wrong with svn, it does
the work  
and 99% of the time we're happy with it. There's another use case than I
mentioned  
just now. Supposed while working on the new features, you found a bug.
It may be  
just 1 line fix and you don't want the fix end up with features you're
working on  
currently. With svn, you have few options:-

-   Do new checkout in another directory, fix the bug and commit.
-   `svn diff > tmp.diff`, `svn revert -R .`, fix the bug and commit,
    `patch -p0 < tmp.diff`

Second option not really nice solution if you have lot of newly added
files and  
you want to have clean environment in order to test the bug fixes. You
have to  
manually copy all the files to some other place. So I search around for
'svn stash'  
and luckily there's few others who'd also thinking about 'svn stash'.
[There's one  
that look complete](http://www.blisted.org/blog/bin/svn/stash), from a
guy named scott (can't find any more details) so I  
give it a try. The script work quite well, it named as `svn`, just put
somewhere  
under your `$PATH`, make sure it come first before the usual path such
as `/usr/bin`  
or `/usr/local/bin`. The script basically a wrapper to actually svn
executable,  
it contains few additonal commands and if none match, it just forward
that to the real svn.

Scott's blog have enough explanation on how to use the script so I won't
repeat it  
here. Basically the flow are:-

-   `svn stash`
-   ... fix bug etc
-   `svn commit`
-   `svn stash list`
-   `svn stash pop` or `svn stash apply <stash-name>` - pop will remove
    the stash while `apply` will keep it.

Another useful use-case is when working on branch. While in the middle
of your work on the branch, you might want to merge latest changes from
trunk. It always good practice to merge into a clean working directory
rather than have the changes from merge mix your current uncommitted
work. You may not ready yet to commit your current changes. With `stash`
command you can 'stash' the current changes, merge latest changes from
trunk, commit, reapply the stash and continue to work:-

    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn status
    M       lib/py/mamoprivate/sms/__init__.py
    M       bin/sendsmsd
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn stash
    Reverted 'lib/py/mamoprivate/sms/__init__.py'
    Reverted 'bin/sendsmsd'
    Changes stashed as: "4d51a3eb-3a16-4e63-89e7-09e74cd30d91"
    Working copy reverted to 129
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn status
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn merge ../../trunk/
    --- Merging r129 through r132 into '.':
    U    lib/py/mamoprivate/d/projects/sms/settings.py
    M       lib/py/mamoprivate/d/projects/sms/settings.py
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn ci -m 'merge latest trunk, refs #381'
    Sending        381-reset-count
    Sending        381-reset-count/lib/py/mamoprivate/d/projects/sms/settings.py
    Transmitting file data .
    Committed revision 133.
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn stash list
    1637 2012-05-02 13:56 4d51a3eb-3a16-4e63-89e7-09e74cd30d91
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn stash pop 4d51a3eb-3a16-4e63-89e7-09e74cd30d91
    pop: 4d51a3eb-3a16-4e63-89e7-09e74cd30d91
    Unstaging stash "4d51a3eb-3a16-4e63-89e7-09e74cd30d91".
    M       lib/py/mamoprivate/sms/__init__.py
    M       bin/sendsmsd
    Stash "4d51a3eb-3a16-4e63-89e7-09e74cd30d91" removed.
    kamal@sms:~/marimore_sms/branches/381-reset-count
    $ svn status
    M       lib/py/mamoprivate/sms/__init__.py
    M       bin/sendsmsd

It also have some other goodies but I haven't try any of them. The
script also show  
a creative way to provide 'plugins' to a command that do not natively
support plugin.  
I might apply the same technique to other command. I have in mind to
override the  
svn commit command to provide some kind pre-commit hook that run the
code through  
static code checker before commiting. We're using Unfuddle so no chance
for us to use  
the native svn pre-commit hook. Lastly, thanks to
[scott](http://www.blisted.org/) for such useful script.
