Title: 【EZSMS】 Phone Number Formatter tool release! 
Date: 2022-03-15
Slug: number-formatter-release
Lang: en
Tags: ezsms; new release; 2022; number formatter;
Thumbnail: images/formatter2.png
Author: Jocelyn ter Morsche
Summary: EZSMS allows you to send SMS messages from your PC, it's easy to use even if you are not a technical person. We have released a new tool that can modify any phone number to comply with the international number notation E.164 before sending.

Thank you for using [EZSMS](https://www.ezsms.biz/).

EZSMS allows you to send SMS messages from your PC, it's easy to use even if you are not a technical person.

We strive to keep improving our product. Last time we released the tool  [_link tracking_](https://blog.xoxzo.com/en/2021/01/28/ez-link-tracking-release/), which is an optional service that you can use to obtain more information about the people who clicked your link and so have a better idea of how you can improve your marketing efforts.

This time, we're pleased to announce our latest release: the _phone number formatter_

### Issues when sending SMS from the web

The world of the internet and the web is globally oriented. Therefore, SMS sent from the web must have **world standard phone number notation**.
This phone number display format is called [E.164](https://help.xoxzo.com/ezsms-sms-delivery-service/articles/E164-format/)
There are unusual rules, such as adding the unnecessary __country code__ and the leading symbol **+ (plus)** when writing this as a "phone number" in Japan.
It's a hassle to remember, but you can't send your messages unless the phone number is written in this notation.

Of course, it is possible to remember the rules of the E.164 format and revise the phone number list that you have manually, but it takes a lot of time to go through each phone number and modify it to the standard notation. (Besides, not everyone is good with using spreadsheets!)

Most of the content which we sent by SMS, such as marketing messages and emergency broadcasts are of high importance and urgency. You want to send them as fast as possible so that the recipient can also read them as fast as possible.

### EZSMS supports non-engineers

EZSMS has a sister service, [Xoxzo](https://www.xoxzo.com/). Xoxzo offers a telephony API, which is useful for engineers developing web services and apps.

However, EZSMS is a service that even non-engineers who do not know coding or programming can easily use from a web browser. Simply registeer and you can start sending immediately. So, we developed a tool that can automatically revise any number in your phone number list to the E.164 format. Even if you don't understand the rules of E.164, or if you can't revise the list using spreadsheets, there is no problem! Please leave it to EZSMS.

### How to use the Phone Number Formatter

[How to use the automatic number correction tool](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/how-to-use-number-formatter/) it's very easy! <br>
If the recipient field contains an invalid phone number that needs to be corrected, the _Send from the web_ will still show up when you try to send the message. For details, see the next section.

The Phone Number Formatter displays a correction sample of the entered number. Numbers in an invalid format that couldn't be modified are excluded from the list. The result of automatic correction will be displayed for all numbers, so that you can look through the revisions before you agree to send your message.
*Please not that CSV sending is currently not supported. 

For more information please visit the [help center](https://help.xoxzo.com/en/ezsms-sms-delivery-service/articles/how-to-use-number-formatter)。


### Functions of the Phone Number Formatter

How does the Phone Number Formatter correct the entered number? <br>
It is mainly modified based on the following rules.

|||
|--------------------|--------------------|
|**Phone numbers that won't be formatted: **|E.164 compliant mobile phone numbers|
||Original (domestic) format mobile phone number | corrected to the E.164 number before sending|
|**The Phone Number Formatter is displayed**||
|||
|**Numbers that will be formatted: ** | Mobile numbers that do not comply with E.164|
||080-0000-0000（domestic standard notation）|
||08000000000 (Domestic notation without hyphens)|
||80-0000-0000(If there is no leading 0)|
||818000000000(E.164 notation without leading + (plus))|
|**Numbers that will be excluded: ** | Numbers that do not exist in the mobile number library|
||Free dial (0120/0800)|
||IP service（050）|
||Fixed-line phone|

* Please note that this tool can't determine whether the contract of a mobile phone number, whether the power is on, whether the radio wave is within reach, or if the model can receive SMS messages at that time.

### Price

The Phone Number Formatter is free to use.

### The reason for developing this tool

The Phone Number Formatter was developed in response to a high number of requests from Xoxzo and EZSMS users.
We always strive to improve the experience of our customers. 

Stay tuned for the next release!

** If you have any questions, please send us a message at（help@xoxzo.com）**

