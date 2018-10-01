Title: User experience on Xoxzo API (Part 2)
Date: 2018-07-03 12:00
Author: Ai Sin Chan
Tags: sms; api user; api; tutorial; experience; 2018
Slug: user-experience-on-xoxzo-api-part-2
Thumbnail: images/apiexp21.jpg
Lang: en
Summary: User experience on Xoxzo API

This is continued from [Part 1](https://blog.xoxzo.com/2018/06/27/user-experience-on-xoxzo-api-part-1/) on my user experience in using Xoxzo API.

After trying out the [Audio File Playback](https://www.xoxzo.com/en/about/voice-api/), [SMS](https://www.xoxzo.com/en/about/sms-api/), and [Carrier Lookup](https://www.xoxzo.com/en/about/utilities-api/) APIs, I was running low on the initial 50 credits. So, I topped up my account and continued trying out other functions. 

I moved on to the [Text-to-Speech API](https://www.xoxzo.com/en/about/voice-api/). This API is supposed to read out the text that you type, and it is heard in the call as voice. Languages supported are English and Japanese. This was the command I issued, followed by the screenshot of my Command Prompt on Windows OS.

curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "tts_lang=en" --data-urlencode "tts_message='Hello world, this is my first attempt at Xoxzo text-to-speech call. Testing, 1,, 2,,,3.'" https://api.xoxzo.com/voice/simple/playbacks/

![apiexp2](/images/apiexp21.jpg)

A Call ID was displayed on Command Prompt. When I answered the Text-to-Speech call ringing on my phone, I was greeted with a brisk and smooth [female voice](https://blog.xoxzo.com/2018/05/23/ivrflow/) reading out the text that I entered in the command above. I experimented with a few commas in between the numbers as suggested in the [TTS tutorial](https://blog.xoxzo.com/2018/03/09/making-a-voice-authentication-call-with-tts/), and noticed that the pause between the numbers increased by a fraction of a second. 

Subsequently, I used the Call ID provided to check the status of my Text-to-Speech call. Following is the command I used, and the screenshot.

curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/calls/7142d264-a945-41ed-8dcb-c28dc7a8c339/

![apiexp2](/images/apiexp22.jpg)

After being satisfied with Text-to-Speech, I tried out the [Conference API](https://www.xoxzo.com/en/about/voice-api/), which will initiate calls originating from the web to 2 numbers. When both recipients answer, the call will be bridged, and they can talk to one another. Following is the command I issued, and the screenshot. 

curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "participants=+81yyyyyyyy,+81zzzzzzzz" https://api.xoxzo.com/voice/simple/conferences/

![apiexp2](/images/apiexp23.jpg)
 
The command upon successfully entered, returned 1 Conference ID, and 2 Call IDs, ie: one Call ID per recipient for each leg of the conference call. In the meantime, my phone rang, I answered it and was able to talk to the other recipient like any normal phone call. Neither of us dialed to the other party, we both received a ringing call and answered the call. 

Next, I entered the Conference ID to check the status of the conference call. This was the command I issued, followed by the screenshot. 

curl -u <API SID>:<Auth Token> https://api.xoxzo.com/voice/simple/conferences/b600722b-d1e0-4eaf-a4a9-ba33bfcc2560/

![apiexp2](/images/apiexp24.jpg)

When you sign up for a [free trial account](https://www.xoxzo.com/en/accounts/signup/), the complimentary 50 credits you receive will only be sufficient for 1 voice call, a few SMS, and a few carrier lookup attempts. So, take your pick on the voice call, whether you would like to try: audio file playback, text-to-speech call, or conference call. And you should do it while your credits are above 40, which is the minimum requirement for voice calls, although [call per minute](https://www.xoxzo.com/en/about/pricing/) costs much less than 40 credits. This is probably enforced to ensure you can have at least a few minutes on the call before running out of credits. Of course, you can always top up your credits to use more functions and make more calls. 

My verdict? The [Xoxzo APIs](https://www.xoxzo.com/) are really easy to use. It is my first experience using web telephony, making a variety of voice calls and sending SMS from a computer with internet connection. You don’t have to be a developer to try out the APIs; basic computer literacy, in particular, basic command line interface (CLI) skills will suffice. 
