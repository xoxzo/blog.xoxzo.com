Title: Wifi Security Concern for Remote Developer
Lang: en
Date: 2017-05-20 10:44
Author: Kamal Mustafa
Tags: cyber security; 2017; developer;
Slug: wifi-security-concern-remote-dev
Thumbnail: images/matnet.jpg
Summary: Few key things and risks for developer to be aware when working in public wifi network.

I managed to join a session on [Malaysia Open Source Conference 2017 (MOSCMY)][moscmy] by [matnet], 
which talked about the topic of ["Exploiting 802.11 with OSS tools"][1]. It turned out to a very interesting
session. As remote developer, I think this is very crucial topic as it is very common for us to work
using a public wifi network, either at our favourite cafe or co-working space.

While I'm aware of the potential security risks in using public wifi, I haven't thought
that launching an exploit is easy with a plethora of tools at your disposal. This is an eye opener
and will definitely will force me to always use an ssh tunnel when working through wifi, or to
better seriously consider implementing VPN for our work.

![matnet]({filename}/images/matnet.jpg)

matnet begin the talk by explaining the basic frame types in 802.11 protocol. Basically it consists
of 3 main components:-

* Control Frame
* Data Frame
* Management Frame

The focus of exploit will be on the Management Frame, which is used to maintain communication between
a device and the Access Point (AP). Management Frame is unencrypted.

There are few attacks that can be done on this data frame:-

* Deauth attack - the attacker sends bogus deauthentication signals, either for specific client or
all the clients connecting to a particular IP. This is simply a denial of service (DOS) attack where
client will see that they are unable to connect to the AP. But this can also be
a basis for further attacks.
* Beacons injection - the attacker sends fake beacon signals that publish/advertise as AP(s). Those looking
for a wifi access point will see a lot of available APs, although all those are fake. This is in way can
also being used as a way to advertise product or services through wifi signals ;)
* Based on these 2 types of attack, there are a number of complete tools to facilitate an attack on a
wifi network, like MANA that can be used to setup an evil twin of a legitimate AP. The attacker will
send deauth signal to disconnect client from legitimate AP and then convince the client that it is the
legitimate AP. Once client connected, it effectively become man in the middle (MITM) between client
and the client's target destination.

matnet and his partner [jep] demonstrated two tools that being used to capture user's credentials like
the wifi's password or their other credentials like facebook or other internet services. The tools,
wifiphisher and fluxion provide a number of attack scenario that we can choose to orchestrate the exploits.
All those are automated and running it is as simply as executing a number of commands. 

Knowing what the bad guys capable of doing out there, I think it's important for us to start taking
defensive mechanism when working over public wifi. In fact this also applies when at home as wifi is so
ubiquitous these days and our home is no different than Starbucks or the public library. The risks are the same.

The first thing we can start right away is to always use ssh tunnel. This however is still far from being
perfect. Our DNS requests for example, can still being sniffed and worse, the attacker can provide fake response.
Tools like [sshuttle] provide a way to tunnel DNS request as well. The ultimate solution is to have a VPN connection.

[matnet]:http://lanyrd.com/profile/matnet-2668/
[jep]:http://lanyrd.com/profile/jep/
[sshuttle]:https://github.com/apenwarr/sshuttle
[moscmy]:http://lanyrd.com/2017/moscmy/
[1]:http://lanyrd.com/2017/moscmy/sfqmcx/
