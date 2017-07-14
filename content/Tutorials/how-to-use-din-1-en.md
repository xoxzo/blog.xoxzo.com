Title: Let's use the dial-in number
Date: 2017/07/13
Author: Akira Nonaka
Tags: din; did; tuborial;
Slug: dialinnumbers-tutorial
Lang: en
Summary: I will outline the dial-in number API that controls incoming calls

## Overview

### What is dial in number?

The dial-in number (Dial in number, hereinafter referred to as DIN)
It is a function to control incoming calls using XOXZO's Telephony API.
The user subscribe the telephone number,
if there is an incoming call on the phone, you can transfer the call or playback the message using the XOXZO DIN API.

The rough flow until use is as follows.

1. Search for a free unsubscribe number
1. Choose the desired phone number from among them and sign up
1. Create an action server
1. Set the action server URL

### Behavior of the action server when receiving an incoming call
 
When an incoming call arrives at the contracted phone number, 
the XOXZO cloud system issues an HTTP request to the action URL of the web server (hereinafter referred to as action server) specified by the API.
Users using DIN must install an action server to respond to HTTP requests from the XOXZO cloud.

![Diagram of incoming call operation]({filename}/images/Tutorial/din-get-call-en.jpeg)

The action instructs the XOXZO cloud system how to handle the incoming phone, and there are the following three types.

<Dl>
     <Dt> playback
     <Dd> Play specified MP3 file
     <Dt> transfer
     <Dd> Transfer to the specified phone number
     <Dt> say
     <Dd> Read out the specified text
</Dl>

So let's explain how to build the DIN system in order.

## Search for a free phone number

The phone numbers available for DIN are pooled in XOXZO cloud system and users can select their favorite phone number. 
To obtain a list of available phone numbers, use the following API.

[DIN Search API](http://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api)

The returned list include `din_uid`, a unique identifier of DIN.
This `din_uid` is used as an important parameter in the following API, so let's keep that in mind.

## Subscribe the incoming phone number

When you decide the phone number you want to use, you can subscribe that DIN with the
following API.

[DIN subscribing API](http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)

Please specify the `din_uid` in the URL.

If the subscription is successful, use the following API

[DIN list subscription API](http://docs.xoxzo.com/en/din.html#getting-the-list-of-subscribed-dial-in-numbers-via-api)

to check if your subscription is all right.

## Create an action server

#TODO

When DIN get a call, XOXZO cloud will send HTTP GET request with two parameters.
By using these parameters, you can know which DIN get called and who called this DIN.
Thus, you can control action according to these parameters.

<Dl>
    <Dt> caller
    <Dd> Phone caller ID
    <Dt> recipient
    <Dd> Phone number of incoming DIN
</Dl>

The action server should return action in one line plain text.
For details of the action, please see [here](http://docs.xoxzo.com/en/din.html#available-actions)

You can find a sample action server created with Django web framework [here.](https://github.com/xoxzo/din-action-server-demo)


## Setting action URL

Once the installation of the action server is completed,
it is necessary to tell the action server URL to the XOXZO cloud so that it can your action server.
We use the following API to set up this URL.

[Action URL Setting API](http://docs.xoxzo.com/en/din.html#attach-an-action-to-the-dial-in-number-via-api)

# Cancel phone number

To cancel DIN, use the following API.

[DIN cancellation API](http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)

## Libraries for each language

Fou your convenience, Python, Ruby, PHP libraries are available for using the XOXZO API.
These are open source of MIT license. You can use these freely.

- [Python](https://github.com/xoxzo/xoxzo.cloudpy)
- [Ruby](https://github.com/xoxzo/xoxzo-cloudruby)
- [PHP](https://github.com/xoxzo/xoxzo.cloudphp)

## Troubleshoot

When DIN does not work, let's check the following points

- Is the action URL set?
- Is the action URL correctly pointing to the action server?
- Is the action server accessible from XOXZO cloud?
- Is the mp3 sound file accessible from XOXZO cloud?
- Is there no mistake in the response action text? Is the spelling of the command, the number of arguments, and the contents of the argument correct?
- Is there enough credit?