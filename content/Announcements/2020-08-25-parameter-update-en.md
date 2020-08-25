Title: [Xoxzo]Change in K-premium parameter
Date: 2020-08-25
Slug: x4-jpkp-parameter-update
Lang: en
Tags: xoxzo; release; 2020; jp-kp; update; parameter;
Author: Aiko Yokoyama
Summary: A paramter to set your pre-registered SenderID for the option service "K-premium" is changed

The SenderID to be shown on the SMS recipients devices are important for the recipients to know
who sent the message, when the messages are sent via APIs.

[The K-premium service on Xoxzo](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service/) enable the users
to set the pre-registered SenderIDs as the fixed SenderID to be shown on the recipients devices by specifying them with parameter.

Please be informed that the parameter on Xoxzo's K-premium service has been changed.

- paramter (old): `jp_kddi_sender`

- paramter (new): `jp_kp_sender`

As you find in our [Documentation](https://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters),
please specify your pre-registered K-premium SenderID with this parameter together with another parameter below.

- `jp_kp` for [K-premium](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service/) sending,

- `jp_kpl` for [K-premium Lite](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-lite/) sending.

** Please note that the old paramter will not be available to use after 2020/10/1.

For any questions, please do not hesitate to contact our Help Desk on help@xoxzo.com.

## Any requests?

**Keizoku Kaizen** is one of our service key at Xoxzo Inc. and the basic idea for these improvements are made to respond to our users voice. 
Please feel free to contact us about anything unfit or unsettled, we will be looking forward to hearing your voices.
