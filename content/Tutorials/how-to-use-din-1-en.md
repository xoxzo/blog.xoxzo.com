Title: Let's use the dial-in number
Date: 2017/07/01
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

! [Diagram of incoming call operation] ({filename} /images/Tutorial/din-get-call-en.jpeg)

The action instructs the XOXZO cloud system how to handle the incoming phone, and there are the following three types.

<Dl>
     <Dt> playback
     <Dd> Play specified MP3 file
     <Dt> transfer
     <Dd> Transfer to the specified phone number
     <Dt> say
     <Dd> Read out the specified text
</ Dl>

So let's explain how to build the DIN system in order.

## Search for a free phone number

The phone number available at DIN is XOXZO cloud system pooled and users can select their favorite phone number from this
You can choose. To obtain a list of available phone numbers, use the following API.

[DIN Search API] (http://docs.xoxzo.com/en/din.html#finding-a-dial-in-number-via-api)

In this API, `din_uid` (one unique identifier corresponding to DIN) corresponding to the telephone number one to one is returned.
In the API listed below, this `din_uid` is used as an important parameter, so let's keep it in mind.

## Contract the incoming phone number

When you decide the phone number you want to use, I will sign that number.
To make a contract

[DIN Contract API] (http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)

Use. Let's specify `din_uid` obtained by search API in the URL.

If the contract is successful

[DIN Contract Confirmation API] (http://docs.xoxzo.com/en/din.html#getting-the-list-of-subscribed-dial-in-numbers-via-api)

Let's check if you are contracting properly.

## Create an action server

The method of the HTTP request issued to the action server when receiving a call is `GET` and has two parameters.
Who did you call by using these parameters? What number did you call me? I understand.
By using these pieces of information, you can control finer actions.

<Dl>
    <Dt> caller
    <Dd> Phone caller ID
    <Dt> recipient
    <Dd> Phone number of incoming DIN
</ Dl>

The response action is returned in one line of plain text.
For details of the action, please see [here] (http://docs.xoxzo.com/en/din.html# available-actions)

[Here] (https://github.com/xoxzo/din-action-server-demo) was created using the Django framework
There is a sample of the action server.

## Setting action URL

Once the installation of the action server is completed, so that the XOXZO cloud system can call that server,
It is necessary to tell the action server URL to the XOXZO cloud.
We use the following API to set up this URL.

[Action URL Setting API] (http://docs.xoxzo.com/en/din.html#attach-an-action-to-the-dial-in-number-via-api)

# Cancel phone number

To cancel DIN, use the following API.

[DIN cancellation API] (http://docs.xoxzo.com/en/din.html#subscribing-to-a-dial-in-number-via-api)

## Libraries for each language

Convenient Python, Ruby, PHP libraries are available for using the XOXZO API. These are open source of MIT license, users can use freely.

- [Python] (https://github.com/xoxzo/xoxzo.cloudpy)
- [Ruby] (https://github.com/xoxzo/xoxzo-cloudruby)
- [PHP] (https://github.com/xoxzo/xoxzo.cloudphp)

## troubleshoot

When DIN does not work, let's check the following points

- Is the action URL set?
- Is the action URL correctly pointing to the action server?
- Is the action server accessible?
- Is the mp3 file of sound to be played accessible?
- Is there a mistake in the response text of the action? Is the spelling of the command, the number of arguments, and the contents of the argument correct?
- Is there enough credit?