Title: Setting up my first online voicemail
Date: 2020-10-23 10:00
Author: Iqbal Abdullah
Tags: covid19; remotework; 2020; wfh series; voicemail;
Slug: setting-up-my-first-online-voicemail
Thumbnail: images/Voicemail.png
Lang: en
Summary: I will go through the steps I took setting up my first online Xoxzo voicemail

With the COVID-19 pandemic, like many of us I started using a lot of online
shopping sites to get stuff delivered to the home without having to go out of
the house. A lot of these online stores required me to give them my phone
number.

The sad thing is that after a few weeks, my phone started receiving marketing calls and
SMS.

# Voicemail with Dial In Number (DIN)

Now with Xoxzo's latest [voicemail feature release]({filename}/Announcements/2020-10-20-voicemail-release-en.md)
I am able to quickly get a number and use it as a registration number for these
shopping sites. Up until now, Xoxzo could only transfer or respond to a call to
these DIN numbers using text-to-speech or an audio file, but with the voicemail
functionality, we can also now take messages.

Being able to take messages is important for me because there might be a real
reason the shops which I purchase from need to contact me. I needed a way to record
any messages they have for me and also notifications that tell me that I have
messages.

## Create an API User

After you've [registered for an account](https://www.xoxzo.com/en/accounts/signup/), you'll need
to create an API User to get the credentials needed to start subscribing to a number. This will be the
phone number which you'll give to the shops.

- After [loging in](https://www.xoxzo.com/en/accounts/login/), you'll be shown your "API Users" dashboard. Click on
  the "**Add API User**" button on the right side to start creating your API User.
- You'll be shown a screen to set the nickname of your API User. Set an easy to
  understand nickname like "Amazon" so you can easily remember what the API User is used for.
- You'll be shown back the dashboard. What you need now is the **API SID** and **Auth Token** of your newly
  created API User. Copy these two; We'll need these later.

## Setup action URL

You'll need to tell the Xoxzo platform what it should do when it receives a call
to your number. We need to set this up before getting a number for your
voicemail.

The Xoxzo platform makes a request to a particular URL which we call
`action_url`. This URL is setup by you, and you specify this URL when you
subscribe to a number. Because you need to setup a URL, it has to be hosted
somewhere.

You can of course host this URL on your own, but what your `action_url` will be
returning when the Xoxzo platforms makes it request is only a bunch of text. If
you can programatically change the text that you send back when Xoxzo makes its
request, it will be a powerful way for you to change how you handle the call that you
receive.

But for this exercise, we're only interested to store incoming voice calls to
our voicemail, so there is only a simple need to host this text somewhere
without any fancy logic.


## Subscribe to a number


### Remember to attach the `action_url` to your number


## Receiving voicemails to your new number


### Listening to your voicemails


And that's it! Perhaps the most difficult part is figuring out how to host your
`action_url` but once that's done, it's downhill all the way.

You can now use this number as a contact phone number for non-important stuff.
Anyone can still get in touch with you at this number, but you won't be sharing
your real personal or work number with everyone that you need to interact on the
internet.



