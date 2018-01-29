Title: Disruption of voice services on both Xoxzo and EZSMS
Date: 2018-01-29 12:00
Slug: 2018-01-27-server-issue
Lang: en
Tags: Xoxzo; EZSMS; Database-Issue; 
Author: Aiko Yokoyama
Summary: Disruption of Voice services for Xoxzo and EZSMS from 12:50 to 20:52 JST January 27, 2018.

Thank you for using [Xoxzo, Cloud Telephony Platform](https://www.xoxzo.com/en/)
and [SMS delivery service, EZSMS](https://www.ezsms.biz/ja/).

We had issues on one of our key servers which affected Xoxzo Voice APIs from 12:50 to 20:52
January 27, 2018. Due to this, it had affected the services below:

A portion of DIN numbers: <br>
**Xoxzo**
During the mentioned period, Dial in Numbers could not receive or make calls, and no credits
were charged during this period.

**EZSMS**
DialSMS did not receive any calls, no points were deducted during this period.

EZSMS CodeCall APIs / Simple Play back APIs accepted and charged for requests up to around 19:00 JST,
but was not charged, although any TTS usage during this time was charged.

All other services were not affected during this period.

We will contact customers who were affected by this issue within the next few
days.

We appologize for any inconvenience that was caused. We are on planning even better
improvements on our routine work and maintenance process.
