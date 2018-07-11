Title: Running command on multiple servers with sup
Date: 2018-07-11 08:07
Author: Kamal Mustafa
Tags: golang, deploy
Slug: running-command-multiple-servers-sup
Lang: en
Summary: Quick look at tools named sup for executing command remotely on multiple servers

This is tool written in Golang (https://github.com/pressly/sup). It look similar to Fabric and also Ansible in certain aspect but I found it more flexible than Fabric and simpler than Ansible. Getting it is easy if you already have Golang environment on your computer. It just:-

```
go get -u github.com/pressly/sup/cmd/sup
```

Next is to define the Supfile. It can be like this:-

```
networks:
    web:
        hosts:
            - web-01.site.com:22
            - web-01.site.com:22
    db:
        hosts:
            - db-01.site.com:10022

commands:
    tailf:
        desc: Tailf local1
        run: tailf /var/log/local1
    bash:
        desc: Interactive commands on all hosts
        stdin: true
        run: bash
```

Then to run command for example tailf on web servers:-

```
sup web tailf
```

We can also run command interactively on all servers. In sup file above, I defined command bash that should be run in interactive mode.

```
sup web bash
```

For now there's no prompt but you can actually start typing and press Enter. For example you can run:-

grep ERROR /var/log/local1
You'll get output:-

```
grep ERROR /var/log/local1
kamal@web-01.site.com:22 | kamal@web-01:~$ Jan 12 21:21:06 web-01 messaging.Sender.send(): ERROR: Sending failed for xxx0 user1: -2 HTTPSConnectionPool(host='sender2.local', port=443): Max retries exceeded with url: /h/send (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.VerifiedHTTPSConnection object at 0x7ff769fe2c50>, 'Connection to sender2.local timed out. (connect timeout=10)'))
```

To quit, just type exit:-

```
exit
kamal@web-01:50022 | kamal@web-01:~$ exit
kamal@web-01:22 | kamal@web-01:~$ kamal@web-01:~$ exit
kamal@web-02:22 | kamal@web-02:~$ kamal@web-02:~$ exit
kamal@web-02:22 | Process exited with status 1
```

Command can also being pipe instead typing interactively:-

```
echo 'grep ERROR /var/log/local1' | sup x4 bash
```
