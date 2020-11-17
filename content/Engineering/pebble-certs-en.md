Title: Root certificates generation using ACME server Pebble
Date: 2020-11-18
Slug: root-certificates-generation-using-acme-server-pebble
Lang: en
Tags: pebble; ACME; certbot; letsencrypt;
Author: Arthur Sultanbekov
Summary: Root and leaf certificates for local development with https

[Pebble](https://github.com/letsencrypt/pebble) is a small ACME (Automatic Certificate Management Environment) test server not suited for use as a production CA.
One of benefits of ACME protocol is allowance to create certificates using wildcard, e.g. *.yourdoamin.com. It means, we may generate one certificate for all subdomains.

In my example I'll setup HTTPS connection for my development domain `mydomain.test` using Pebble and certbot. This domain is just an alias for host IP: just add `<HOST IP>    mydomain.test` into /etc/hosts. You may use 127.0.0.1 if you run pebble not from container.

Let's start. Clone Pebble repository, and then you may build `pebble` executable (it's written in Go language), or run docker containers like I did, using `docker-compose`:

```
> git clone https://github.com/letsencrypt/pebble.git
> cd pebble
> docker compose up
```

Now you have your own ACME server running.
If you run Pebble on docker containers, you need to tell ACME server where your fake domain is hosted. To do that run `curl --request POST --data '{"ip":"172.20.0.1"}' http://localhost:8055/set-default-ipv4` with your correct HOST IP address (and make sure, that Pebble can access that IP address.)

Next, install [certbot](https://certbot.eff.org/) and run this command to generate needed leaf certificates:

```
> certbot certonly --standalone -d mydomain.test --server https://localhost:14000/dir --email you@example.com --agree-tos --no-verify-ssl --http-01-port=5002
```

Used params:
* `certonly` - Obtain or renew a certificate, but do not install it
* `--standalone` means, that you don't need server like Apache or Nginx for domain verification. Certbot runs it's own local server. `--http-01-port=5002` tells to run this server on port 5002. When you start Peble, you can see in the logs record `challtestsrv_1  | pebble-challtestsrv - 2020/11/17 07:04:45 Creating HTTP-01 challenge server on :5002`, you need to use this port number for `--http-01-port`.
* `-d mydomain.test` domain
* `--server https://localhost:14000/dir` it is a path for ACME server directory. Pebble from docker-compose runs ACME server on port 14000 and exposes that port to host. Certbot makes request to that port.
* `--email you@example.com --agree-tos` - set your email ang agree terms of service, this is optional.
* `--no-verify-ssl` - since we make https request to server, we should use root certificate from test/certs/pebble.minica.pem, but I decided to skip ssl verification.

Congratulations, now you have signed certificates on `/etc/letsencrypt/live/mydomain.test/`!

# Root and Intermediate Certificates
Ok, now you have leaf certificates. But for https connection you also need public Root Certificate. You may know which certificate exactly you need:

```
> cd /etc/letsencrypt/live/mydomain.test/
> openssl x509 -in fullchain.pem -noout -issuer
issuer=CN = Pebble Intermediate CA 0342fc
```
We need an Intermediate certificate, which is taken from Pebble:
```
curl -s -o intermediate.crt https://localhost:15000/intermediates/0
```
Similarly, issuer for this certificate is `issuer=CN = Pebble Root CA 0e8b65`, which can be downloaded from `https://localhost:15000/roots/0`. This certificate is self-signed.

It's highly recommended by Pebble to not install this certificates system-wide, but only on clients, e.g. browsers.

# Nginx or Apache setup and certificates verification
You may use this config to serve local development server through Nginx by https:

```
server {
    listen       443 ssl;
    server_name  www.mydomain.test mydomain.test;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_certificate "/etc/letsencrypt/live/mydomain.test/fullchain.pem";
    ssl_certificate_key "/etc/letsencrypt/live/mydomain.test/privkey.pem";
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_prefer_server_ciphers on;
    ssl_ciphers HIGH:!aNULL:!MD5;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
    }
}
```

Analogically, SSL params for Apache's vhost may be setup as:

```
SSLEngine on
SSLCertificateFile /etc/letsencrypt/live/mydomain.test/cert.pem
SSLCertificateKeyFile /etc/letsencrypt/live/mydomain.test/privkey.pem
SSLCertificateChainFile /etc/letsencrypt/live/mydomain.test/chain.pem
```

You may verify certificates by next command:

```
> openssl verify -CAfile root.crt /etc/letsencrypt/live/mydomain.test/cert.pem 
/etc/letsencrypt/live/mydomain.test/cert.pem: OK
```

Now you may test HTTPS setup by `curl -iL https://mydomain.test`, using root and intermediate certificates. If all fine, and you see response from server, it means that you have successfully setup HTTPS for your http server.
If you've ignored Pebble warning and have installed certificates system-wide, then when you open url in browser, you'll see a message about untrusted CA. It's ok, browsers don't trust self signed certificates. It's enough to import only intermediate certificate to browser. E.g. for **Chrome** go to `Settings > Advanced Settings > Manage Certificates > Import`. For **Firefox** it is `Options > Encryption > View Certificates > Your Certificates > Open`.

