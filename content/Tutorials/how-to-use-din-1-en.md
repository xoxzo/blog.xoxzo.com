Title: Let's use the dial-in number
Date: 2017/07/13
Author: Akira Nonaka
Tags: din; did; tutorial;
Slug: dialinnumbers-tutorial
Lang: en
Summary: I will outline the dial-in number API that controls incoming calls

## Overview

### What is dial in number?

The Dial in number (hereinafter referred to as DIN) is a function to control
incoming calls using XOXZO's Telephony API. The user subscribes a telephone number,
and if there is an incoming call to that number, you can transfer the call or playback
a message using the XOXZO DIN API.

Roughly the flow are as follows.

1. Search for an available DIN.
1. Choose the phone number you like and subscribe to it.
1. Create an action server.
1. Set the action server URL.

### Behavior of the action server when receiving an incoming call
 
When an incoming call arrives at the subscribed phone number, 
XOXZO cloud system issues an HTTP request to the action URL of the web server
(hereinafter referred to as action server) specified by the API.
Users using DIN must install an action server to respond to HTTP requests from the XOXZO cloud.

![Diagram of incoming call operation]({filename}/images/Tutorial/din-get-call-en.jpeg)

The action instructs the XOXZO cloud system how to handle the incoming phone, and there are
three types of action you can specify:

<Dl>
     <Dt> playback
     <Dd> Play specified MP3 file
     <Dt> transfer
     <Dd> Transfer to the specified phone number
     <Dt> say
     <Dd> Read out a specified text
</Dl>

So let me explain how to build the DIN system in order.

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

# TODO

When a DIN receives a call, XOXZO cloud will send a HTTP GET request to a callback URL you specify
with two parameters. By using these parameters, you can know which DIN was called and what number
called the DIN. You can then dynamically control your action action according to these parameters.

<Dl>
    <Dt> caller
    <Dd> Phone caller ID
    <Dt> recipient
    <Dd> Phone number of incoming DIN
</Dl>

The action server should return action in one line plain text.
For details of the action, please see [here](http://docs.xoxzo.com/en/din.html#available-actions)

You can find a sample action server created with Django web framework
[here.](https://github.com/xoxzo/din-action-server-demo)

## Setting action URL

Once the installation of the action server is completed, it is necessary to tell the action
server URL to XOXZO cloud so that it knows where to send the callback GET request above. 

We use the following API to do this:

[Action URL Setting API](http://docs.xoxzo.com/en/din.html#attach-an-action-to-the-dial-in-number-via-api)

# Cancel phone number

Once you're finished with a particular DIN, you can cancel the subscribtion with the following API.

[DIN cancellation API](http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)

## Libraries for each language

Fou your convenience, Python, Ruby, PHP libraries are available for using the XOXZO API.
These are open source of MIT license. You can use these freely.

- [Python](https://github.com/xoxzo/xoxzo.cloudpy)
- [Ruby](https://github.com/xoxzo/xoxzo-cloudruby)
- [PHP](https://github.com/xoxzo/xoxzo.cloudphp)

## Troubleshoot

When things don't work as expected, check the following points:

- Is the action URL set?
- Is the action URL correctly pointing to the action server?
- Is the action server accessible from XOXZO cloud?
- Is the mp3 sound file accessible from XOXZO cloud?
- Are there no mistakes in the response action text?
  Is the spelling of the command, the number of arguments, and the contents of the argument correct?
- Are there enough credit?
