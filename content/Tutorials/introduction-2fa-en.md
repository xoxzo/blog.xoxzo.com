Title: How to set up Two-Factor Authentication using SMS
Date: 2018-05-02 10:00
Author: Akira Nonaka
Tags: 2FA; Tutorial; SMS; API;
Slug: introduction-2fa-sms
Lang: en
Summary: Let's learn how to add Two-Factor Authentication on your Web-applications

There are many cases that user IDs and passwords are leaked by various Web services, 
accounts are compromised and illegally used.
As a means to prevent such troubles, it is becoming more common to confirm the mobile number of the user.
Even if ID and password are stolen, it is impossible to use the account alone, and it is the idea of two-factor authentication to try to confirm whether or not the user is really registered by some additional means.
This is the popular use-case within all what Xoxzo API users do with Xoxzo.

How will we introduce two-factor authentication using SMS in the web service then?
The flow will be roughly as follows.

1. Let the users to register with their mobile phone numbers at the first creation of their account.
1. A user tries to log in to a Web-service.
1. Generate a random 4 -6 digits PIN within the Web-service.
1. Send that PIN to the registered mobile phone number of the user via SMS.
1. User input that PIN to the Web-service.

Log-in will be accepted if the input PIN matches with the generated PIN, by the mean of confirming the log-in user surely posess the mobile phone.
Log-in will be rejected conversely, in case the input PIN doesn't match, which means the log-in user cannot be confirmed as the account holder.

Here is a sample code to send a PIN via SMS with Python[^1].

    import os
    import secrets
    from xoxzo.cloudpy import XoxzoClient
    
    # Sample code to execute two-factor-authentication by SMS
    
    # Generate 4 digit random PIN
    secret_key = secrets.randbelow(10000)
    message = "This is Xoxzo. Your PIN is %04d" % secret_key
    
    # Assume that the secret key to call API is saved as an environment variable
    # Please retrieve your SID and TOKEN from your signed in account on https://www.xoxzo.com/
    sid = os.getenv('XOXZO_API_SID')
    auth_token = os.getenv('XOXZO_API_AUTH_TOKEN')
    
    # Sending SMS
    xc = XoxzoClient(sid=sid, auth_token=auth_token)
    result = xc.send_sms(message=message, recipient="+818054695209", sender="XOXZO")

This code will send the message as below to the user's phone.

<br>
***
<br>
![SMS PIN](/images/introduction-2fa-sms/sms-2fa-en.jpg)
<br>
<br>

Please display the form to request the PIN input, the authentication will be successful if the input PIN matches with the *secret_key*.
 
#Summary

This is an introduction of simple Hot-to for two-factor authentication using SMS.
With implement of this method, you may avoid the multiple account creation by a user for each of their purpose.

[^1]: It is assumed to use Python 3.6 or later. There is no *secrets* package by default in Python before that ver., so you will need to use the appropriate random number generation library.
