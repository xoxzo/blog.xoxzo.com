Title: Github: Managing fork and making pull request
Date: 2015-09-10 09:08
Author: Kamal Mustafa
Category: Engineering
Tags: git, github, version control
Slug: github-managing-fork-and-making-pull-request
Lang: en

It's common when you're using a third party library, there's come a
point when you need to make some changes to accomodate your project
requirements. On Github, it easy to fork the repository into your own
repo and start making all the changes you need.

One thing to consider when creating a fork is that you always want your
changes to be merged back with the upstream repo. This will lift out lot
of burden in maintaining your changes and syncing it out with the
changes in the upstream. To facilitate this, you have to do a number of
things that will help this 'merging' process easier both on your part
and also original developer(s).

Always create a specific branch for the specific changes you want to
made. This will help in sending a pull request back as it would allow
the original developer(s) to review the changes atomically.

Because of the first rule above, it mean changes you did would span into
more than 1 branch, so how would you use that in your project ? So you
need to create another branch, called it develop or something and merge
all the changes in other branches into this branch. So you would
probably have list of branches such as:-

    * develop
    master
    remotes/origin/HEAD -> origin/master
    remotes/origin/develop
    remotes/origin/master
    remotes/origin/signup-form-mixin
    remotes/origin/update-email-verify

Any changes that specific to your project need and never intended to be
merged with upstream repo should be in `develop` branch. Never make any
changes to the `master` branch. That branch should only be the place
where you pull changes from upstream.
