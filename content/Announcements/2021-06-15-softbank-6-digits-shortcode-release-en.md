Title: Update in Sender Display for SB users (when jp_kp is used) and an additional SMS receiving option
Date: 2021-06-15
Slug: x4-jpkp-softbank-shortcode-update
Lang: en
Tags: xoxzo; release; 2021; jp-kp; update; senderid;
Author: Aiko Yokoyama
Summary: The Sender Display for Japanese SB users is updated when sending messages using K-premium service. Furthermore, an expanding function is added.

One of the most important element when sending SMS messages via API is how to set SenderID to be displayed on the receipients' devices.
Because this tells the recipients who sent them the message.

[K-premium service on Xoxzo](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service/) enables
the users to set the Sender display by attach the pre-registrered number as a parameter.

For KDDI/Docomo/Rakuten: pre-registered number<br>
For Softbank: a default shortcode


## An update on the shortcode

The shortcode being used as Sender to the Softbank recipients is updated from 5 digits to 6 digits.

Previous Shorcode: `22472`

New Shortcode: `249200`

## A new function: Get your own shortcode and catch the recipients' replies

We will organize your own 6-digits shortcode upon request.
In addition, what this new 6-digits code can do is that you can receive your message recipients' 
replies at a set webhook! 

Please contact help@xoxzo.com for further details.

## Any requests?

**KEIZOKU KAIZEN** is the key to the service of Xoxzo. We listens to our users' voice and apply improvements.
Please feel free to contact us about anything unfit or unsettled, we will be looking forward to hearing your voices.
