Title: [Xoxzo] K-Premium service V2 will cover all Japanese operators
Date: 2017-11-24
Slug: kpremium-v2-notice
Lang: en
Tags: api; k-premium; docomo; kddi; au; softbank; 
Thumbnail: images/xoxzo-logo-02.png
Author: Aiko Yokoyama
Summary: Our popular K-Premium service that supported only KDDI (au) will now cover all Japanese carrier messages.

Thank you for using [Xoxzo, Cloud Telephony Platform](https://www.xoxzo.com/en/).

We are excited to announce that our K-Premium service will be upgraded on **5th Dec 2017**. 

Originally, the current [K-Premium service](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/) was released in 2013, as an optional feature for our sister
SMS API service [SMS Delivery Service, EZSMS](https://www.ezsms.biz/ja/).

Although requiring registration and an approval before use,
K-Premium has been a popular optional service because it allows you to set the
sender id and uses a direct route for KDDI recipients.

The upgrade to be released for [K-Premium service](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/) will allow direct connections to all Japanese operators,
and not only limited to KDDI.

The major points of this upgrade are:

- Sendings to **ALL Japanese operators** are to be direct, **not just to KDDI**
- Sendings to Docomo/Softbank using K-Premium will set **a fixed SenderID** despite the set sender with `jp_kddi_sender`
- **13 credits** will be deducted for an each K-Premium SMS sent.
- The text display of delivery report

Please also note:

- The parameter to use K-Premium will not be changed. Please continues using the K-Premium flag 
`jp_kp` and set your sender id with `jp_kddi_sender`. `jp_kddi_sender` will
still be used when sending to KDDI.

We expect increased delivery rates to Japanese numbers with this upgrade.

Please feel free to contact us at (help@xoxzo.com) to inquire any further information or
assistance concerning this upgrade.
