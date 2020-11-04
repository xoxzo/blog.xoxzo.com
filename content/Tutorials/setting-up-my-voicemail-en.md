Title: Setting up my first online voicemail
Date: 2020-10-23 10:00
Author: Iqbal Abdullah, Josef Monje
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

Some of us at Xoxzo use Github Gists for this. Signing up
for an account at github.com is free and it's a quick way to put text files online
for an `action_url`. At a later step, you'll configure the `action_url` with some text.
That text will be the content of the gist. You can save the gist and view it as plain text
by clicking the **raw** button. You can find it on the right side while viewing your gist.
While viewing the raw gist, take not of its URL. This will be the URL of your `action_url`.

## Subscribe to a number

First thing you need to do is to subscribe to a DIN. To find numbers, send a
request to the Xoxzo API with your user's API SID and Auth Token. If you have the
`curl` program installed, the request looks like this:

```
curl -u <SID>:<AUTH_TOKEN> https://api.xoxzo.com/voice/dins/
```

You can use any program or even programming language to make the request but we'll use
`curl` in the examples since it's a common way to make requests in the command-line.

This request returns a list of available DINs you can choose from.
Once you've selected a DIN, take note of its `din_uid` because you need this to subscribe,
which is what we'll do next. You'll also need this later when we attach the `action_url` to the DIN.

To subscribe to a DIN, send a `POST` request to the API:

```
curl -u <SID>:<AUTH_TOKEN> -d'din_uid=<din_uid>' https://api.xoxzo.com/voice/dins/subscriptions/
```

When this request succeeds, your subscription starts immediately and your credits will be charged.
You can read more about this process in our [documentation](https://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api).

### Remember to attach the `action_url` to your number

At this point, the DIN doesn't do anything yet so the next step is to attach an `action_url`.
The voicemail system can be configured to use either **text-to-speech** or a **mp3** file hosted
somewhere for the voicemail greeting. In this example, tts is used since it's very easy to do.

For a text-to-speech greeting, put `voicemail say` in your `action_url` followed by
the [language code](https://docs.xoxzo.com/en/utilsapi.html#tts-lang-label) and your message enclosed in quotes:

```
voicemail say en "Hello, you have reached my voicemail. I cannot answer the phone right now, but I will return your call as soon as I can..."
```

This is the content of the the `action_url`. If you have't created a github gist mentioned earlier,
create one now with your preferred greeting. Get the URL of the **raw** gist and that will be the URL.
Once you have that URL, you can attach it to the DIN:

```
curl -u <SID>:<AUTH_TOKEN> -d'action_url=<url>' https://api.xoxzo.com/voice/dins/subscriptions/<din_uid>/
```
 
Once this is done, you're ready to receive voicemail messages.

## Receiving voicemails to your new number

It works just like any voicemail. When someone calls your DIN, they hear a greeting and they
can leave a message. The message gets recorded and all the recordings will be available for your use later.

### Listening to your voicemails

To listen to your voicemail messages, login to the your Xoxzo account and you'll find a link to your 
`Voicemail Records` on the left. There you'll see a list of your recordings with information such as when and who called.
You can download or delete recordings and if you start getting a lot of messages, you can filter by date, caller, DIN, or API user.

# Your voicemail is setup

And that's it! Perhaps the most difficult part is figuring out how to host your
`action_url` but once that's done, it's downhill all the way.

You can now use this number as a contact phone number for non-important stuff.
Anyone can still get in touch with you at this number, but you won't be sharing
your real personal or work number with everyone that you need to interact on the
internet.
