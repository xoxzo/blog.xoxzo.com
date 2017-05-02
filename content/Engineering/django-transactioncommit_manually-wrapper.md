Title: Django transaction.commit_manually wrapper
Date: 2012-08-27 09:02
Author: Kamal Mustafa
Tags: django
Slug: django-transactioncommit_manually-wrapper
Lang: en

I first [encountered this
problem](http://metaKamal%20Mustafa.blogspot.com/2011/05/django-transactioncommitmanually-mask.html)
1 year ago and it look's like the issue still not being fixed till now.
The [corresponding ticket](https://code.djangoproject.com/ticket/6623)
has been 5 years old already. When you used
`transaction.commit_manually` decorator around your function (usually
views function), you mark that function to be executed in single
transaction but you'll manage the transaction control, whether to commit
or rollback yourself. This in contrast to another related decorator
`transaction.commit_on_success` where django will handle the commit or
rollback depending on the function can be successfully executed or not.

Using `transaction.commit_manually`, there's usually a case when an
exception occurred in the function uncaught causing the commit or
rollback call not reached. When django detect this (because it see the
dirty bit in the transaction object), it raise
`TransactionManagementError` with the infamous message 'Transaction
managed block ended with pending COMMIT/ROLLBACK'. The original
exception however is buried inside the traceback and you have to dig it
out in the order to find out the real issue. It's really annoying
because sometime you have to disable the decorator in order to find out
the real error.

Until the issue get fixed and we manage to upgrade to latest version of
django (which unlikely to happen in the near future), I have decided to
create a wrapper around `transaction.commit_manually` and use it instead
of the original decorator.

I have also update the patch in the
[ticket](https://code.djangoproject.com/ticket/6623) to apply cleanly to
current django trunk but so far no feedback yet from django core
developers.
