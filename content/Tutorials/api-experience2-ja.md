Title: Xoxzo APIのユーザーエクスペリエンス（第2回）
Date: 2018-08-10
Author: Ai Sin Chan
Tags: sms; api ユーザー; api; tutorial; お試し; 2018
Slug: User-experience-on-Xoxzo-API-Part-2
Thumbnail: images/apiexp21.jpg
Lang: ja
Summary: Xoxzo API の体験レポート

Xoxzo APIを使った、[私のユーザーエクスペリエンス]
(https://blog.xoxzo.com/ja/2018/08/10/user-experience-on-xoxzo-api-part-1/)の第2回 です。

[オーディオファイルの再生](https://www.xoxzo.com/ja/about/voice-api/)、
[SMS配信](https://www.xoxzo.com/en/about/sms-api/)、および [キャリア検索 API](https://www.xoxzo.com/en/about/utilities-api/)
を試したあと、私は当初の50クレジットがほぼなくなっていました。
だから、私は、アカウントにクレジットを補って、他の機能を試し続けました。

まずは、[テキスト音声変換API](https://www.xoxzo.com/en/about/voice-api/)。このAPIはあなたが入力したテキストを読み上げることになっており、
通話上では音声として聞こえます。
サポート可能な言語は、英語と日本語です。
これは私が実行したコマンドであり、続いてWindows OSでのコマンドプロンプトのスクリーンショットが続きます。


curl -u <API SID>:<Auth Token> --data-urlencode "caller=+60xxxxxxx" --data-urlencode "recipient=+81yyyyyyyy" --data-urlencode "tts_lang=en" --data-urlencode "tts_message='Hello world, this is my first attempt at Xoxzo text-to-speech call. Testing, 1,, 2,,,3.'" https://api.xoxzo.com/voice/simple/playbacks/

![apiexp2](/images/apiexp21.jpg)

コマンドプロンプトにCallIDが表示されました。
テキスト音声変換/TTS（Text-to-Speech）を使った電話にでると、
[快活で滑らかな女性の声](https://blog.xoxzo.com/ja/2018/07/10/ivrflow/)に挨拶されました。
上記のコマンドで入力したテキストを読み上げたものです。
私は、[TTSチュートリアル](https://blog.xoxzo.com/ja/2018/03/09/making-a-voice-authentication-call-with-tts/)
で提案されていた通り、数字と数字の間に、カンマをいくつか入れて、
実験しました。数同士の間がほんの少し開いたことに気づきました。

その後、提供されたCallIDを使用して、自分のテキスト音声変換を使った通話の、ステータスを確認しました。以下が、私の使用したコマンドとスクリーンショットです。
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
