Title: [Xoxzo]Changes for API endpoints
Date: 2017-11-24 
Slug: endpoint-nouns-change
Lang: en
Tags: endpoint, nouns
Author: Akira Nonaka
Summary: XOXZO has changed some endpoints in order to improve usability. 

In order to improve usablility, XOXZO has changed the API endpoints for
[Simple Playback API](http://docs.xoxzo.com/en/voice.html#simple-playback-api) and
[Checking Call Status API](http://docs.xoxzo.com/en/voice.html#checking-call-status)

*Simple Playback API*

* Old `POST /voice/simple/playback/`
* New `POST /voice/simple/playbacks/`

*Checking Call Status API*

* Old `GET /voice/simple/playback/<callid>`
* New `GET /voice/calls/<callid>/`

**Old endpoints will be available until Feb. 28 2018 and be removed afterwords.**
