Title: [Xoxzo] SMS Character Limit Expanded to 660!
Date: 2025-06-03
Slug: long-sms
Lang: en
Tags: Long SMS; 660 characters; 2025;
Thumbnail: /images/longsms-en.png
Author: Aiko Yokoyama
Summary: According to the GSM specification, a single SMS in Japanese is limited to 70 characters. But what if you need to send more? With Xoxzo’s SMS API, you can now send messages up to 660 characters long — all from a mobile number, and at a lower cost than traditional direct mail.

---

Thank you for using [Xoxzo – The Cloud Telephony Platform](https://www.xoxzo.com/).  
We're excited to announce that our SMS API now supports messages of up to **660 characters** in Japanese!

---

### 💬 Common Use Cases for SMS

Generally, SMS messages fall into three main categories:
- **Authentication**
- **Urgent Notifications**
- **Marketing**

**Authentication:**  
Simple and effective:
```This is Xoxzo. Your verification code is 3030.```

**Urgent Notifications:**  
Keep it short and actionable:
```Alert Level 3: "Evacuation for the elderly." Please begin evacuation for elderly residents.```


But sometimes, additional context is needed — like a link to your service page or a map for evacuation. SMS can help, especially as smartphone usage increases and links can direct users smoothly from SMS to browser.

However, links can be long, even with URL shorteners, and within the 140-character limit, every word counts.

---

### 📢 Marketing Messages Need More Room

Marketing messages often require more than 140 characters — you may need a greeting, campaign details, and opt-out instructions. That’s why we now support **long-form SMS up to 660 characters**.

Compared to direct mail, SMS offers instant delivery at a fraction of the cost — and now, with much more room to communicate.

You can check our documentation for [character limits](https://help.xoxzo.com/en/xoxzo-cloud-telephony/sms-api/articles/how-many-characters-would-fit-within-1-x-sms/) and [API usage](https://docs.xoxzo.com/en/sms#send-sms-messages-api).

---

### ✉️ Mail2SMS Also Supports Long Messages

With [Mail2SMS](https://www.xoxzo.com/en/about/mail2sms-api/), you can send SMS from your mail client — no development required. Learn more [here](https://help.xoxzo.com/en/xoxzo-cloud-telephony/sms-api/articles/how-to-send-via-mail2sms/).

---

### ⚠️ Please Note:
Due to GSM specifications, Japanese SMS messages are limited to 140 characters per segment. While our API accepts up to 660 characters, it will be divided into multiple parts, and **each segment is billed separately**.

Longer messages don’t always mean better results. For best performance, keep messages concise and to the point:

- **Up to 70 characters**: Notifications, one-line campaigns, or links  
  `Your reservation is confirmed for tomorrow. Details: https://xxx.jp`

- **150–200 characters**: Brief info with a call to action  
  `Limited-time sale today! Up to 50% off popular items. Check it out: https://xxx.jp/sale`

- **Up to 660 characters**: Only for detailed explanations when absolutely necessary  
  `Your health check results are in. Blood pressure is slightly high. Please review the enclosed notes and contact us if needed. Next appointment: https://xxx.jp`

---

📰 Also read: [Long SMS? It's Basically Email](https://blog.xoxzo.com/en/2021/12/07/long-sms-is-not-sms/)

For questions or assistance, feel free to contact our [Help Desk](mailto:help@xoxzo.com).

Thank you again for choosing [Xoxzo](https://www.xoxzo.com/).
