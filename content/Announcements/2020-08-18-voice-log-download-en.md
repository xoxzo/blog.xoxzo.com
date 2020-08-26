Title: [Xoxzo] Voice & DIN API logs are directly downloadable!
Date: 2020-08-18
Slug: logs-download-voice
Lang: en
Tags: log-download; release; 2020; VoiceAPI;
Thumbnail: images/freepik/young-females-download-icon.jpg
Author: Aiko Yokoyama
Summary: Now Voice and Dial-In-Number logs are directly downloadable from your account page.


We are happy to announce that[Voice API](https://www.xoxzo.com/ja/about/voice-api/)
logs are downloadable from the account page.

[Xoxzo's direct log download](https://blog.xoxzo.com/en/2019/08/13/logs-download-feature-new-release/) is develooped 
to respond to the users' request. The first release was only for the SMS usage download.

Using this direct Voice log download, you can check the usage log without 
using the [Checking call status API](https://docs.xoxzo.com/en/voice.html#checking-call-status)
for your favorite duration of the data in csv format.
This includes the logs for [Dial-In-Number](https://docs.xoxzo.com/en/din.html) usage.

The downloadable csv file contains the items as below.

<table>
  <tr>
    <th>Voice API</th>
    <th>Dial-In-Number</th>
  </tr>
  <tr>
    <td>call_type<br>
        caller<br>
        callid<br>
        cost<br>
        direction<br>
        start_time(UTC)<br>
        end_time(UTC)<br>
        duration(secs)<br>
        recipient<br>
        status<br>
        tags<br>
        url<br>
        apiuser</td>
    <td>caller<br>
        cost<br>
        direction<br>
        recipient<br>
        start_time(UTC)<br>
        end_time(UTC)<br>
        duration(secs)<br>
        status<br>
        apiuser<br>
        uuid<br>
        actionurl<br></td>
    </tr>
</table>

The downloadable data is up to **42 days before the current date**.

## How to download

It is super simple!

Please log in your account dashboard, choose _Download Usage Logs_ from the left side menu.

![Download dashboard](/images/logs-download-feature-screenshot-en.png)

Although you can select the dates of the data period as you like, 
why don't you use the convenient selection of "Last 7 days" or "Last month" prepared for you.

The process of the download file generation is done back ground.
If you do not wish to wait, please come back here later to collect your file later.

Download can be done by clicking the _LOG FILE_ name in the table at the bottom.


Thank you to rawpixel.com for the thumbnail:
[Background photo created by rawpixel.com - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
