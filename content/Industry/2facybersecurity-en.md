Title: The Role of SMS and Voice in Cybersecurity
Date: 2018-4-27 12:00
Author: Ai Sin Chan
Tags: api; sms; voice api; cyber security; 2fa; 2 factor authentication; two factor authentication; security token sms; 
Slug: 2fa-cyber-security
Lang: en
Thumbnail: images/2facybersecurity.jpg
Summary: Why two factor authentication is important to cyber security


We had discussed the many possible applications of SMS and Voice in businesses as well as public services in our previous entries. There is one more area we would like to zoom in to, where SMS and Voice could play a part, that is data protection and cybersecurity.

![2facybersecurity](/images/2facybersecurity.jpg)

## Types of Security Breach

The 5 common and distinct types of security breach are:

* Phishing and Social Engineering

* Password Attacks

* Malware

* Ransomware

* Denial-of-Service

## Notable Security Breach Cases

Corporate Case: Dubbed the biggest cybersecurity breach cases in history, Yahoo! reported two major data breach of user account data to hackers, affecting 1 billion user accounts in 2013 and 500 million in 2014 respectively.

Personal Case: Happening back in 2012, due to weaknesses in the Apple and Amazon authentication procedures, technology journalist Mat Honan lost his Google, Twitter, Amazon, and Apple accounts, as well as access to his MacBook and iPhone, including all data in his MacBook, to hackers who applied social engineering to gain access to his accounts. And the hackers were only after his three-character Twitter handle, that was a heavy price to pay for. Honan’s biggest regret was not backing up his data and not using 2FA for his accounts.

## What is Two Factor Authentication?

Two factor authentication (2FA) makes use of a combination of two of the following to authenticate user identity:

* something you know (login credentials: username, password)

* something you have (hardware: key fob, mobile phone)

* something you are (biometrics recognition: voice, thumbprint, iris)

There are a few ways to implement 2FA by applying “something you have”, usually by generating or sending one-time passwords (OTP) through:

* SMS or voice

* hardware (key fob)

* online app

* offline app

There is a weak point in cybersecurity in the account recovery process, the use of 2FA for logging in is bypassed. In designing the algorithm flow for account recovery such as in case of forgotten password, we highly recommend that a different set of 2FA is implemented before allowing passwords to be reset.

## SMS in 2FA

One of the most convenient solutions is to send a OTP to the user’s mobile phone over SMS, which the user must enter on the portal to gain access to her account. Implementing 2FA for your users’ accounts over SMS offers effective protection against phishing and password attacks, the apparent advantages are:

* Protect against weak passwords;

* No key fob required;

* No 3rd party app (whether online or offline) required.

It is also important to note that 2FA over SMS is not immune against:

* Social engineering: where the hacker has convinced your service provider to redirect your phone number to the hacker’s SIM;

* Malware attacks: where SMS sent to an Android phone infected with malware is intercepted and redirected to the hacker’s device instead.

However, we can deduce that the risk of facing such an attack is comparatively low, as opposed to not implementing 2FA at all.

## Voice in 2FA

As a variation to sending an OTP over SMS, voice can be used instead. Applying text-to-speech functionality to the standard 2FA process, the system dials a voice call and sends an OTP via voice audio. This is particularly useful for the visually impaired users.

Using OTP sent to a mobile device via an SMS or a voice clip is user-friendly for your users, relatively cheap and easy to implement, and achieves the purpose of 2FA.

As with any security measure, 2FA is not foolproof, but it adds an effective extra layer of a protective barrier against unauthorized access to any user accounts. There is no reason not to implement it into your system. Our SMS API and Voice API are the perfect tools for you to get started and get it done quickly.
