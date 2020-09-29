Title: [Xoxzo]Change in K-premium parameter now effective
Date: 2020-10-01
Slug: x4-jpkp-parameter-update-2
Lang: en
Tags: xoxzo; release; 2020; jp-kp; update; parameter;
Author: Jocelyn ter Morsche
Summary: A parameter to set your pre-registered SenderID for the option service "K-premium" has been changed.

We would like to inform you that one of the parameters on Xoxzo's [K-premium service](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service/) has been changed and the old parameter is no longer in use. 
Please use the new parameter going forward:

Parameter (new): jp_kp_sender
Parameter (old): jp_kddi_sender

As you find in our [Documentation](https://docs.xoxzo.com/ja/sms.html#jp-specific-optional-parameters), please specify your pre-registered K-premium SenderID with this parameter together with one of the parameters below:

- `jp_kp` for [K-premium](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-service/) sending,

- `jp_kpl` for [K-premium Lite](https://help.xoxzo.com/en/xoxzo-cloud-telephony/articles/the-k-premium-lite/) sending.

The SenderID is important for recipients so they know who the message is from. The K-premium service on Xoxzo enables the users to set the pre-registered SenderIDs as fixed SenderIDs, and to be shown on the recipients devices by specifying them with parameters.

For any questions, please do not hesitate to contact our Helpdesk: help@xoxzo.com.

## Any requests?

**Keizoku Kaizen** is one of our service key at Xoxzo Inc. and the basic idea for these improvements are made to respond to our users requests. 
Please feel free to contact us about anything unfit or unsettled, we will be looking forward to hearing your voices.
