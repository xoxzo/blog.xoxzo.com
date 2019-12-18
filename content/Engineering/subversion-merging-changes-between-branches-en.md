Title: Subversion merging changes between branches
Lang: en
Date: 2011-09-24 08:04
Author: Kamal Mustafa
Tags: 2011; tip; developer; code;
Slug: subversion-merging-changes-between-branches
Summary: let's talk about svn branching strategy

For svn branching strategy, we used the [feature
branch](http://stackoverflow.com/questions/597707/best-branching-strategy-when-doing-continuous-integration)
approach. This mean we keep trunk stable at all time and for any new
features to work on, we start a new branch. While working on the branch,
we'll keep it in sync with trunk by merging any latest changes happened
on the trunk. Once the feature is ready, we merge that branch back into
trunk. Subversion &gt; 1.5 `--reintegrate` option really helpfull here.

There's a case however we end up with multiple branches active at a
time. Supposed there are 3 new features that need to be implemented.
Logically I would start 3 separate branches to work on each features
since all of it are not related to each other. Let assume I start 3
branches named as branch-A, branch-B and branch-C. I keep working on
these 3 branches over the time. As the time passed by, branch-A is
finished and ready to get into trunk. As usual after making sure
branch-A has all the latest changes in trunk, I merged it back into
trunk:-

    $ cd branches/branch-A
    $ svn merge ../../trunk
    $ svn ci -m 'merge latest changes from trunk into branch-A'
    $ cd ../../trunk
    $ svn merge --reintegrate ../branches/branch-A

Everything work flawlessly and as expected here. Before continuing
working on other branches, I'll make sure all those branches in sync
with trunk by merging all latest changes in the trunk. This would
include the new features implemented in branch-A.

    $ cd branches/branch-B
    $ svn merge ../../trunk
    $ svn ci -m 'merge latest trunk into branch-B'
    $ cd branches/branch-C
    $ svn merge ../../trunk
    $ svn ci -m 'merge latest trunk into branch-C'

I'd then continue working on branch-B and branch-C. Later on I'd
realized that changes that I made in branch-C actually also needed in
branch-B. Let assume I added new function in branch-C and then found out
that the code in branch-B also need the same function. Now it's not
possible to merge branch-C into trunk yet so that it changes can be
propagated to branch-B. Ideally I should be able to merge changes
between branch-B and branch-C before merging back both branches into
trunk but subversion is not that clever in tracking merge between
branches like this. So I decided that all development now should be done
in branch-B. This mean I need to merge all changes that been done in
branch-C into branch-B.

When trying to do this - merge branch-C into branch-B, I ended up with
lot of conflict. Remember the changes we have done in the branch-A
earlier ? In branch-A, among the changes that we have done involved
adding some new files. Now the changes (adding new files) exists in both
branch-B and branch-C because we take it from trunk. When merging
branch-C into branch-B subversion will try to add the new files again
and we have conflict. It said something like - "local add, incoming add
upon merge". Searching around, I found the solution in this [SO
question](http://stackoverflow.com/questions/738367/why-am-i-getting-tree-conflicts-in-subversion):-

    $ svn resolve -R --accept working

It mean for any conflict, keep the current working copy and discard the
incoming changes. This is fine if you know exactly the changes that you
need contained in different files than the conflicted one. Otherwise you
have to manually inspect the file and fix the conflicting line. I'm not
sure yet whether this can be merged cleanly back to the trunk. Will
update this post later.
