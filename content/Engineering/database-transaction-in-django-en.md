Title: Database Transaction in Django
Date: 2012-06-21 07:54
Author: Kamal Mustafa
Tags: django; python; 2012; tip;
Slug: database-transaction-in-django
Lang: en
Summary: Django tips, simple but important

Keep forgetting about this so this is to wrap my heads around it. First
I have  
the impression that Django by default execute database operations within
a  
transaction block, which is the source of my confusion. It's true only
to  
certain extent. The [first section in django documentation](https://docs.djangoproject.com/en/1.3/topics/db/transactions/)
already explained  
this (emphasized is mine):-

> Django’s default behavior is to run with an open transaction which it  
> commits automatically when any built-in, **data-altering model
> function  
> is called**. For example, if you call model.save() or
> model.delete(),the  
> change will be committed immediately.

Once you call any function that will alter the data such as `.save()`
method,  
Django will commit the transaction and start a new one. Take the
following code  
for example:-

    def step1():
    mms = MMSMessage()
    mms.save()
    step2()
    @transaction.commit_manually
    def step2():
    transaction.rollback()
    step1()

I thought no `MMSMessage` object will be saved since when `step2()`
function  
get called, the transaction was rollback. But the fact is, the
transaction  
already committed when `mms.save()` is called and by the time `step2()`  
executed it's already running in a new transaction, so the rollback does
not  
have any effect. To get what we want, both function must be made to run
in a  
single transaction.

    def step1():
    mms = MMSMessage()
    mms.save()
    step2()
    @transaction.commit_manually
    def step2():
    transaction.rollback()
    @transaction.commit_manually
    def main():
    step1()
    main()
