Title: Fake domain setup for local development
Date: 2020-11-17
Slug: fake-domain-setup-for-local-development
Lang: en
Tags: https; local-development;
Author: Arthur Sultanbekov
Summary: Local web development server with https

In this article I'd like to show how to setup fake domain for local development.

## Warning! Following is not suitable for production!

# Fake domain setup

1.Add alias into `/etc/hosts` file. E.g. add line `127.0.0.1  mydomain.test`.

2.Don't use domain ending with `.dev`, if you don't have HTTPS certificates for that domain! Chrome and Firefox automatically redirects .dev domains to [secured HTTPS connection](https://ma.ttias.be/chrome-force-dev-domains-https-via-preloaded-hsts/)

3.Edit /etc/nsswitch.conf and make sure, that `hosts` param has `files` firs, e.g. `hosts:          files mdns4_minimal [NOTFOUND=return] dns`. It means, that domain names resolver will look at files (`/etc/hosts` file) first, and then tries other services (DB lookup, DNS lookup).

Now run your dev server and test connection, not by 127.0.0.1:<port>, but by mydomain.test:<port>

# Setup port 80

Now let's try access dev server on port 80. I'll use Nginx (`sudo apt install nginx`) for that, but Apache or Caddy also ok - any server with [reverse proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) support. Add `mydomain.conf` file into `/etc/nginx/conf.d` with following minimal content:
```
server {
    listen       80;
    server_name  www.mydomain.test mydomain.test;
    location / {
	    proxy_pass http://127.0.0.1:8000;  # reverse proxy to your dev server
	    proxy_set_header Host $host;
    }
}
```
Restart Nginx and you may acces dev server by http://mydomain.test. Congratulations!

# Setup HTTPS

Little bit of theory: HTTPS is a secure HTTP connection - data exchange between client and server is encrypted, not plain text, so no one who doesn't have encryption keys can understand what this data is. In most cases there's 3rd part in communication - Certificates Authority (CA), whom trust both client and server. CA provides public keys, known as Root Certificates, which is usually installed system-wide on Operation System. Valid root certificate allows establish a HTTPS connection.

When you get certificate for domain, you need to "prove" that it belongs to you. With localhost you cannot do same, since no one belong localhost, so you need to create a self signed certificate, to make your OS trust your CA.

Steps to setup HTTPS:

* generate self-signed root certificates
* create signed leaf certificates
* install root certificate on browser (or system-wide)

You can run openssl commands to generate certificates, like it described in this [article](https://letsencrypt.org/docs/certificates-for-localhost/):
```
openssl req -x509 -out localhost.crt -keyout localhost.key \
  -newkey rsa:2048 -nodes -sha256 \
  -subj '/CN=localhost' -extensions EXT -config <( \
   printf "[dn]\nCN=localhost\n[req]\ndistinguished_name = dn\n[EXT]\nsubjectAltName=DNS:localhost\nkeyUsage=digitalSignature\nextendedKeyUsage=serverAuth")
```
There's a easy-to-use tool named [miniCA](https://github.com/jsha/minica), which generates all necessary certificates:

```
minica --domains mydomain.test
```

And in my next article I'll show how to use another tool, Pebble to generate certificates.

### Setup Nginx to use that certificates

Certbot installed all keys/certificates into `/etc/letsencrypt/live/mydomain.test` directory. Now let's setup https:

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

