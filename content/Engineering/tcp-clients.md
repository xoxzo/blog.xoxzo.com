Title: TCP clients communication
Lang: en
Date: 2020-08-31 09:00
Author: Arthur Sultanbekov
Tags: tcp; tcpclient; http; websocket; keepalive; 2020;
Slug: tcp-clients-communication
Summary: Analysis of TCP clients

In general, I understand how clients and servers work - user sends some data, like , server replies with response. But it's too general, it's on high level. And yesterday I decided to learn their lower level, focusing on how they communicate. Thanksfully, there's tools like `Wireshark` and `tcpdump` allowing to see conversations. Since mainly I work with web technologies, I wanted to analyze TCP clients relatedto web. All next experiments were made on Ubuntu 20.04.

## Basic HTTP client and little theory

Let's start by very basic example. I'll use python's requests module to get html page:
```python
>>> import requests
>>> r = requests.get('http://example.com/')
```

If we check the dialog, we may notice that:

* `requests` appends `Connection: keep-alive` header by default
* We've received gzipped response

Basic HTTP client doesn't use keepalive, and for simplicity let's turn off gzipping, and continue:

```python
>>> r = requests.get('http://example.com/', headers={'Accept-Encoding': 'identity', 'Connection': 'Close'})
```

Now let's look to the output:

![http dialog]({filename}/images/tcp-clients-communication/2020-08-29_15-12.png)

Or schematic dialog would be:

![schematic http dialog]({filename}/images/tcp-clients-communication/2020-08-29_16-26.png)

First, we can see that every TCP request or reply has some flags like SYN, ACK, they are named Control bits, and used for congestion notification. There's 6 such flags:

* URG: Urgent Pointer field significant
* ACK: Acknowledgment field significant
* PSH: Push Function
* RST: Reset the connection
* SYN: Synchronize sequence numbers
* FIN: No more data from sender

4 flag are quite well-known, and they tell us about:
SYN - Initiates a connection
ACK - Acknowledges received data
FIN - Closes a connection
RST - Aborts a connection in response to an error
The other two flags, PSH (push) and URG (urgent), aren't as well-known. You may read about them [here](https://packetlife.net/blog/2011/mar/2/tcp-flags-psh-and-urg/).

Look to dialog between client (C) and server (S) above, and you can read it as:
* C wants to establish a connection with S (sends SYN)
* S replies with ACK - it allows us to connect
* C replies with ACK again - connection is established.
* Now C sends request to GET html page (PSH, ACK)
* S replies with ACK
* and then sends requested page.
* C replies, that it has received data, sends ACK
* C sends FIN, ACK - client doesn't have any more data to send to S
* S replies with FIN,ACK too
* since both sides doesn't have data to exchange, they can close connections. And they do. C sends ACK
* S closes the connection - sends ACK.

Note, that if we run the code above again (`requests.get('http://example.com/', headers={'Accept-Encoding': 'identity', 'Connection': 'Close'})`), then client would established connection again, with same dialog.

## HTTP client with keepalive

Let's check behaviour when we change `Connection` header value to `keepalive`.

In this case, we can see that dialog was same as in previous example, except client didn't get last ACK from server. So, server doesn't close the connection. To see benefits of keepalive, we need to run multiply requests from client to server. And in this case we may modify code to use session, and make multiply requests, but I decided to use browser, which is a TCP client itself. I looked for simple http website, and found one - [http://supervisord.org/](http://supervisord.org/). If you open it in browser, it will load the `/` page, and then js, css files, images, and so on. And here's the result of TCP dialogs for such case:

![http with keepalive dialog]({filename}/images/tcp-clients-communication/2020-08-29_18-50.png)

You may see, client opens a connection only once, and then gets data from server (http page, static and media files); then server closes connection after some timeout reaches (the value of timeout may be controlled by `Keep-Alive: timeout=X, max=Y` header). Of course, such approach minimizes CPU usage, and it's good for website performance.
You may read more about Keep-alive in HTTP in 1) https://www.imperva.com/learn/performance/http-keep-alive/ and 2) https://www.oreilly.com/library/view/http-the-definitive/1565925092/ch04s05.html


## Websocket

Let's check how websockets differ from http request. I decided to use simple WS server found at [simple-websocket-server](https://github.com/dpallot/simple-websocket-server).
I started echo WS server:

```python
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):
    def handleMessage(self):
        # echo message back to client
        self.sendMessage('resp: %s' % self.data)
    def handleConnected(self):
        print(self.address, 'connected')
    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('127.0.0.1', 8000, SimpleEcho)
server.serveforever()
```

I'll test WS using browser, by opening `websocket.html` file from that repo.

![websocket dialog]({filename}/images/tcp-clients-communication/2020-08-29_19-49.png)

![websocket dialog]({filename}/images/tcp-clients-communication/2020-08-29_19-48.png)

We can see here, that client and server establishes connecion, then both sides doesn't close the connection. C sends data with FIN flag set, and S replies with FIN too, then C sends ACK. Compared to HTTP with `Connection: keep-alive`, WS doesn't close the connection after timeout. If you are interrested in how websockets work, you may read [this article](https://lucumr.pocoo.org/2012/9/24/websockets-101/).


## HTTP2
For them, who interrested in understanding HTTP2 protocol, I may recommend next setup, based on [article](https://blog.lgohlke.de/docker/h2o/2016/03/01/dockerized-h2o-webserver.html):
1. I chose docker container, which allows unsecured connection:
```
> docker run -p "9090:8080" -d lkwg82/h2o-http2-server
```

2. I used [curl](https://curl.haxx.se/docs/http2.html) with http2 support:
```
> curl --version
curl 7.68.0 ...
Release-Date: 2020-01-08
Protocols: ...
Features: AsynchDNS brotli GSS-API HTTP2 HTTPS-proxy ...
# make request
> curl --head --http2 -H 'Accept-Encoding: identity' -v http://localhost:9090
# in response we get 404 Not Found, but it's ok
```

And here's the dialog flow:

![http2 dialog]({filename}/images/tcp-clients-communication/2020-08-30_11-23.png)

It's interrsting, that if we add `Connection: Close` header, protocol won't switch to HTTP2. In my example above I used `Accept-Encoding: identity` header, but it's meaningless to use in case of http2, since protocol uses data compression, and sends bytes instead of plain text.

## Conclusion
You've noticed, that I made unsecure http and ws requests, but not https and wss. If I made secure requests, I'd seen encrypted conversation, which is currently meaningles for me. Along with HTTP and WS requests, there's also interresting things that may be learned: AJAX requests, connection to MySQL/PostgreSQL databases, file uploading or downloading.
