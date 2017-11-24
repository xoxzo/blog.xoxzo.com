Title: [Xoxzo]Kpremium service version 2 will cover all Japanese Carriers
Date: 2017-11-24
Slug: kpremium-v2-notice
Lang: en
Tags: api; k-premium; docomo; kddi; au; softbank; 
Thumbnail: images/
Author: Aiko Yokoyama
Summary: Our popular Kpremium service that supported the sendings to KDDI (au) phones will soon cover all Japanese carrier messages.

Thank you for using [Xoxzo, Cloud Telephony Platform](https://www.xoxzo.com/en/).

We are happily announcing that our Kpremium service will version up in the following month and below is the details of the change.

Originally, current [Kpremium service](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/) has
started in 2013, as an optional feature on SMS API for our [SMS Delivery Service, EZSMS](https://www.ezsms.biz/ja/).
Although it requires a registration and an approval before the use of this service, there are benefit such as that the senderID is fixed and 
the messsages are sent directly to the destination carriers, Kpremium service is our popular service since the release.

An upgrade is going to be released for this [Kpremium service](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)
and it covers all Japanese Carriers, not limited to KDDI any more.
The major upgrade are on:
* Sendings to ALL Japanese carriers are to be direct-send, not just to KDDI
* Sendings to Docomo/Softbank using Kpremium will set a fixed SenderID despite the set sender with `jp_kddi_sender`
* 13 credit will be deducted for an each Kpremium SMS sent.
* The display of delivery report
Also, please note that there is no change:
* The parameter to use Kpremium will not be changed. Please set the Kpremium flag of `jp_kp` as before, 
set your senderID with `jp_kddi_sender`

An assured raise in delivery factor is expected on the Japanese domestic SMS sending with this upgrade.
Please contact us to inquire any further information or assistance upon this change, as you may want to upgrade your system
to get the maximum benefit from it.
