Title: [Xoxzo] Changes for K-Premium parameters
Date: 2017-07-31 14:00
Slug: k-premium-parameter-change
Lang: en
Tags: k-premium; 2017;
Author: Aiko Yokoyama
Summary: Changes to our K-Premium services API parameter.

The parameter name for our
[K-Premium services](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/)
has been updated to reduce the exceptions and have more consistency with all our other API parameters.

The parameter name for our [K-Premium services](https://help.xoxzo.com/en/xoxzo-cloud-telephony-platform/articles/the-k-premium-service/) is now:

```
jp_kp
jp_kddi_sender
```
(Using underscores)

Instead of:
```
jp-kp
jp-kddi-sender
```
(Using dashes)

__Dash types are still acceptable until August 14 2017.__ We request
that customers update their code using underscores instead.

Please refer to [our documentation](http://docs.xoxzo.com/en/sms.html#jp-specific-optional-parameters) 
for the latest version of the API.

For any comments or questions, please inquire at: help@xoxzo.com

Thank you for using [Xoxzo, Cloud Telephony Platform](https://www.xoxzo.com/en/).
