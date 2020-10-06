Title: python / isprintable() & 2-byte-space problem
Date: 2020-09-25
Author: Akira Nonaka
Tags: python, isprintable
Slug: about-is-printable
Lang: en
Summary: An alert on specification of python isprintable() 

I happened to meet an issue of an application crash, by the incorrec input of ASCII `ESC(0x1b)` within the character string parameter
that needs to be UTF-8 encoding.
The cause of the crash was that the parameter with the character string including ISO-2022-JP character set was given.


It is not acceptable for the application to be crashed even the wrong data is input.
I was to add an extra check for the input data. The application is written with python3.

I discovered a convenient python function `isprintable()` while I was wondering how
to check if the input string includes any `ESC`.

[specification of isprintqable()](https://docs.python.org/3.7/library/stdtypes.html#str.isprintable)


My trial of this function showed that `ESC` can be found in the string.
How great, this is happily ever after! 
I wrote a test code and created pull request to be reviewed.

Then I proceeded onto the next testing to check if the correct data to be recognized
as wrong while the wrong data gets hit, this can be happened when a new validation is added.
I gathered the history data left in the production database to test it.

Unfortunately, there were bunch of data flagged as wrong input despite they were correct data.
The cause of this was 2-byte-space `\u3000` . `isprintable()` returns False to the input of this character.
The ASCII space character `0x20` can be returned as `printable (True)` of course.
Although it is an eye-opening behavior that 2-byte-space is not printable, 
this is the correct reaction according to the specification.
I changed my code to check the existance of `ESC` directly to resubmit my pull request. 

Finding this behavior before the production release was great.
It is scary to even just imagine to release this without knowing!

### A lesson learned by this: It is essential to test with the real data!
