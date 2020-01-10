Title: Supporting HTML5 features in browsers using polyfill
Date: 2012-04-23 11:23
Author: Muhammad Juwaini
Tags: 2012;
Slug: polyfilling-the-future
Lang: en
Thumbnail: images/860d2-6a0153916e707f970b0168ea921382970c-pi.jpg
Summary: Explaining Polyfill

What is polyfill?
#####################################################

A polyfill or polyfiller is code designed to provide technology that is
not native to a web browser. For example, earlier versions of Internet
Explorer do not support all the features of HTML5 which may necessitate
the use of polyfills to display features of HTML5 which are not
supported by the web browser.

What does it mean?
#####################################################


If you use &lt;audio&gt; tag for certain filetypes (for example, an mp3
file), there are some browser that do not supports it.[^1]
What does it needs to be done if we want to play an mp3 file on Firefox
3.6? Well, we can use a flash audio player for instance or we could
provide other compatible files. The latter is not preferable for it
requires a lot of space and processing power. We'd have to convert every
single file that are not supported by browsers to a format it supports.
Polyfills provide a fallback for this type of
situations.[^2]

How Do We Check A Feature Is In A Browser?
#####################################################

Check out <http://html5readiness.com/> to view the readiness of a
browser to a specific HTML5 feature. 

[![Capture4-23-2012-6.41.10
AM]({filename}/images/860d2-6a0153916e707f970b0168ea921382970c-pi.jpg "Capture4-23-2012-6.41.10 AM")


But How Do We Check It In Code?
-----------------------------------------------------

To check it in code, we could use Modernizr to detect if a specific
feature is in the browser. <http://modernizr.com/docs/#features-css>

For example,


    if (Modernizr.audio.mp3 == '' and '' == false)
    {
    // Use the flash audio player
    }


Where Do We Get These Polyfills?
#####################################################

Most of them are listed at <http://html5please.com>

That's it.
#####################################################

The "polyfill" or "regressive enhancement" technique just means that you
go ahead and use HTML5 features then use other libraries to emulate
native behavior in older browsers. So instead of worrying about support
in some browsers, use these polyfills to enhance the browsers to provide
the user with proper experience to your web sites and applications.

[^1]: <http://html5doctor.com/native-audio-in-the-browser/>

[^2]: <http://html5please.com/#audio>

