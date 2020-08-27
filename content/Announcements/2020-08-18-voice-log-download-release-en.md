Title: [Xoxzo] Voice & DIN API logs are downloadable!
Date: 2020-08-18
Slug: logs-download-voice
Lang: en
Tags: log-download; release; 2020; VoiceAPI;
Thumbnail: images/freepik/young-females-download-icon.jpg
Author: Aiko Yokoyama
Summary: Now Voice and Dial-In-Number logs are directly downloadable from your account page.


We are happy to announce that [Voice API](https://www.xoxzo.com/en/about/voice-api/)
logs are downloadable from the account page.

Using this direct Voice log download, you can check the usage log for your favorite duration of the data in csv format
without using the [Checking call status API](https://docs.xoxzo.com/en/voice.html#checking-call-status).

The logs for [Dial-In-Number](https://docs.xoxzo.com/en/din.html) also became downloadable now.


## What does the csv file data have?

The downloadable csv file contains the items as below.

<table style="width:100%" "border:1px">
  <tr style="padding:15px">
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

![Download dashboard](/images/voice-download-ss-en.jpg)

1. Please log in your account dashboard, choose _Download Usage Logs_ from the left side menu.

2. Although you can select the dates of the data period as you like, why don't you use the convenient preset selection of "Last 7 days" or "Last month" prepared for you? Please do not forget to select the API that you are going to get the log data.

3. Click on _Generate_ button. The process of the download file generation is to be done background. If you do not wish to wait, please come back to collect your file later.

4. Download can be done by clicking the _LOG FILE_ name in the table at the bottom.


## Did you know?

[Xoxzo's direct log download](https://blog.xoxzo.com/en/2019/08/13/logs-download-feature-new-release/) was develooped 
to respond to the users' request. The first release started with the SMS usage download.


Thank you to rawpixel.com for the thumbnail:
[Background photo created by rawpixel.com - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
