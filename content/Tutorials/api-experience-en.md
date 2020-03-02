Title: User experience on Xoxzo API (Part 1)
Date: 2018-06-27 12:00
Author: Ai Sin Chan
Tags: sms; api user; api; tutorial; experience;
Slug: user-experience-on-xoxzo-api-part-1
Thumbnail: images/apiexp1.jpg
Lang: en
Summary: User experience on Xoxzo API

Today I tried my hands on using Xoxzo API to send SMS and make calls, including text-to-speech and conference call, and trying out the telephony utility function, ie: carrier lookup. 
First of all, I signed up for a trial [Xoxzo account](https://www.xoxzo.com/en/accounts/signup/), and was given 50 complimentary credits to try it out. 

![apiexp1](/images/apiexp1.jpg)
 
I created my [first API User](https://blog.xoxzo.com/2017/10/13/create-your-first-apiuser/), and obtained my “API SID” and “Authentication Token” which will be used in the commands that follow. 

![apiexp2](/images/apiexp2.jpg)
![apiexp3](/images/apiexp3.jpg)
  
Next, I downloaded [CURL](https://curl.haxx.se/dlwiz/?type=*) to my laptop. Since I am using an Intel processor with Windows OS, I chose the specific executable file that is compatible with my laptop specifications. Then I executed all the commands from the Windows Command Prompt in the directory (folder) where I store the CURL executable and library files. 

For anyone familiar with the Command Prompt, all you need is the CD command to navigate, and everything else is CURL function. For the reader who has never used Command Prompt before, you may consider spending an hour or so checking out a user manual and figuring out [how to use Command Prompt](https://www.lifewire.com/command-prompt-2625840). You really only need to practice using the few commands for CD (change directory).

I decided to start with [Voice API](https://www.xoxzo.com/en/about/voice-api/) – Audio File Playback API. I found an MP3 audio file playing harpsichord music with a [URL pointing to it](http://www.hubharp.com/web_sound/WalloonLilliShort.mp3), this is a pre-requisite to run the API. I modified the commands from the [Xoxzo tutorial](https://blog.xoxzo.com/2017/11/28/making-a-simple-playback-call/) to suit my situation. Here’s the command I issued, followed by the screenshot from my Command Prompt: 

```
curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "recording_url=http://www.hubharp.com/web_sound/WalloonLilliShort.mp3" https://api.xoxzo.com/voice/simple/playbacks/
```

![apiexp4](/images/apiexp4.jpg) 

A Call ID was displayed on Command Prompt. Then my phone started to ring. I answered and heard the harpsichord music playing through my phone. 

Immediately after the successful voice call, I checked the call status using the Check Call Status API, by specifying the Call ID displayed on Command Prompt. Here was the command I issued, followed by the screenshot:

```
curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/calls/41c181b6-1817-4f91-8a4f-5e0cf5105092/
```

![apiexp5](/images/apiexp5.jpg)

I checked my Xoxzo account, my credits were deducted by 16, and I was left with 34 credits, here is the screenshot:

![apiexp6](/images/apiexp6.jpg)
 
I no longer have enough credits to test out other Voice APIs, such as Text-to-Speech and Conference. The minimum required credits is 40. When I attempted to make a Text-to-Speech voice call, it failed.

![apiexp7](/images/apiexp7.jpg)
 
So, I tried [sending SMS](https://blog.xoxzo.com/2017/10/31/sending-your-first-sms/) next. This was the command I issued, followed by the screenshot of the Command Prompt: 

```
curl -u <API SID>:<Auth Token> --data-urlencode "sender=XoxzoBlog" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "message=Hello world, this is my first SMS sent over the Xoxzo." https://api.xoxzo.com/sms/messages/
```

![apiexp8](/images/apiexp8.jpg)
 
The Message ID was displayed after my command. Subsequently I issued this command to [check the SMS status](https://blog.xoxzo.com/2017/11/15/checking-your-sms-status/). 

curl -u <API SID>:<Auth Token> https://api.xoxzo.com/sms/messages/

![apiexp9](/images/apiexp9.jpg)
 
Meanwhile the SMS notification ringtone was audible on my mobile phone. I received the [SMS sent from the web](https://www.xoxzo.com/en/about/sms-api/):

![apiexp10](/images/apiexp10.jpg)
 
With less than 50 credits, I was still able to try out [Telephony Utilities API](https://www.xoxzo.com/en/about/utilities-api/) – Carrier Lookup API. I used a Japan mobile number and a Malaysia mobile number to try out this function. The commands I issued and the screenshot:

```
curl -u <API SID>:<Auth Token>  --data-urlencode "recipient=+81yyyyyyyy" https://api.xoxzo.com/utilities/carrierlookup/
```

![apiexp11](/images/apiexp11.jpg)
 
The Japan number I entered was subscribed from Asahi Net, an MVNO. The MVNO was not displayed, instead the actual infrastructure owner was displayed, in this case, NTT Docomo. The Malaysia number I entered had been ported to a different carrier (Celcom), in this case Maxis was displayed which was the carrier before porting. I am aware that the MNP (Mobile Number Portability) is supported on a best effort basis and is dependent on the end carrier, so in my case it is not reflected. 

When I entered a fixed line number, all the parameters returned were ‘null’. This function is only meant for mobile numbers. This function can be used to check validity of a mobile number, whether it is still in use. 

![apiexp12](/images/apiexp12.jpg)
 
Mobile numbers from any country is supported, I tried out a few more mobile numbers in various continents from my phone book, they all returned results. Screenshots are omitted for brevity, clarity, and confidentiality purposes. 

(to be continued)
