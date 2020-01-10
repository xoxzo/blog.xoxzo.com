Title: Code Review is not only LGTM!
Lang: en
Date: 2018-11-09
Author: Zaki Akhmad
Tags: code; 2018; tip; 
Slug: code-review-is-not-only-lgtm
Summary: Doing code review is not as simple as it seems.

LGTM! (Looks Good To Me!)

On daily tasks, other than writing code I am also doing code review.
And doing code review is not only about leaving LGTM comment. I am not that
expert yet on doing code review. Yes, I still need to learn a lot.

Once I found a good material about code review, but I can not recall what is the
keyword to search this material.

The first thing I do when doing code review is asking for PEP8 compliance. I
know this is not a substantial thing to do. I mean, PEP8 will not check for the
code logic. PEP8 will only check for the code syntax: is there any modules
imported but it is not being used, unused variables, too many blank spaces, etc.
But somehow I consider comply with PEP8 is an important thing to do because the
code will also being read by someone else not only by the code author. Imagine
when you need to read other people code and the code is being written without
following the standard.

There are many automated tools out there to ensure that the code you write is
comply with PEP8. Since most of the time I use vim, I use vim-flake8 plugin.
You may check this steps that I wrote on [enabling flake8 on
vim](https://gist.github.com/za/983db825aee2dc352d5341da357cbfb4).

After that, then I would review the core logic of the PR. For Django case, I
would review the views.py I will do the manual test that if it is a new
functionality, this new functionality is working as expected. If the manual
test is OK, then I would like to have the test code is exist to do this test.

If everything is OK, I will proceed to alternate use case. What I mean by
alternate use case here is not the main use case but for example what if other
user who does not have the privilege trying to do the action in the new
functionality. Since I come from security background this concept is not too
difficult for me to understand. For a simple example, a logged in user B should
not be able to reset user A password.

I still need to learn to do a better code review. So far I found a quite
interesting angle on doing [code review by Ana
Balica](https://ana-balica.github.io/2017/05/28/humanizing-among-coders/). So
please also have a look and I will update this blog post as well once I found
the code review material that I can not recall for now.
