Title: Software engineering is more than just coding
Date: 2017-04-27 10:42
Lang: en
Author: Kamal
Tags: software-engineering
Slug: software-engineering-discipline

It also about discipline and paying greater attention to detail.

Let say you're working in a branch named `feature-a`. You almost done with it and running the final tests. But then you have a couple of tests failed. You start investigating, put some debugging etc, and finally you discovered the issue that causing the tests to fail.

If you don't really care about process, the next step would be just to make a fix, commit it and call it a day. It just one line fix after all. But that might not what you want to do. For example, you have to verify whether the failure is a consequences of the changes you made for `feature-a`, or it's not.

So you also need to check on `master` to verify whether the same issue also happen there. It could mean the same test also failed on `master`. If yes, this mean the failure is not related at all to the changes you're working on for `feature-a`. And this mean you should commit the fix on `master`, and the merge it back to your working branch. This is important because if it broken on master and you do the fix on your branch, how do you propagate the changes to other branches as well ? If your branch is not ready yet to be merged to master, it mean other people has to cherrypick your changes into their branch. Worse, they could be making same changes in their branch, resulting in conflict when merging to master.

So you can see that in software engineering process, it's not just about adding some code. You have to practice self discipline and adhere to a standard workflow.
