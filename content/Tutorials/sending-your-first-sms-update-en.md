Title: Send Your First SMS with Xoxzo API
Date: 2025-08-20 12:00
Author: Xoxzo Team
Tags: sms; api; tutorial
Slug: sending-your-first-sms-update
Thumbnail: images/xoxtan.png
Lang: en
Summary: Learn how to send your very first SMS using the command line and the Xoxzo API. Prepare your API credentials and try sending a message in just one command.
Series: Xoxzo API Tutorial
Series_index: 4

---

<img src="https://blog.xoxzo.com/images/xoxtan.png" width="200" height="200" style="margin: 0;">


## Introduction

In the previous tutorial, we created our first API user.  
Now it’s time to actually **send an SMS using the Xoxzo Web API**.  

SMS sending is the most basic function of the Xoxzo API. In this article, we will walk through the necessary setup and the exact command to send your first SMS.

---

## 1. What you need

- **Shell environment**  
  Use Command Prompt on Windows, or Terminal on Mac/Linux.  
  In this tutorial we will simply call it “the shell.”

- **API user credentials (SID and Auth Token)**  
  Log in to your account and check the *API User Management* section in the dashboard.  
  - You will need the pair of `API SID` and `Auth Token`.  
  - To copy the token, click the *Show Token* button.  

![SID and token](/images/Tutorial/send-sms/sidtoken-en.jpg)

- **Internet connection**

---

## 2. Format of API credentials

Combine your API SID and Auth Token with a colon (`:`) in between, all in one line:

APiSiD:AUthT0k3n

- Don’t forget the colon  
- Keep it on a single line without line breaks  

You will use this credential string for authentication in the request.

---

## 3. Let’s send an SMS

Prepare your mobile phone number in **E.164 format** (with country code).  
For Japan, that means starting with `+81` and dropping the leading zero.

Example: `+819012345678`

### cURL command example
Run the following command in your shell:

```
bash
curl -u YOUR_API_SID:YOUR_AUTH_TOKEN \
--data-urlencode 'sender=XoxzoTest (this will appear as the sender)' \
--data-urlencode 'recipient=+819012345678' \
--data-urlencode 'message=Hello from Xoxzo!' \
https://api.xoxzo.com/sms/messages/
```

You can also write it all in one single line without backslashes.

## 4. Check the result
If the request is successful, you will receive a response like this:
```
[{"msgid":"tHi5i5y0urMsGIdt3xT"}]
```

- If msgid is returned, the SMS was sent successfully.

- Within a few seconds, the SMS should arrive on your phone.

- Depending on the carrier, the sender name may be replaced.

After sending, check your account dashboard to confirm that credits have been deducted.

## 5. Summary
That’s it — your very first SMS with the Xoxzo API!
With a single command, you can send a message directly from your computer.

For more advanced use cases (voice calls, utility APIs, etc.), see the full documentation.

## Tip: Try SMS without coding — EZSMS
If you want to send SMS messages from your PC without writing code, try EZSMS.
No monthly fees or setup costs — pay only for what you send. All accessible directly from your browser.

- Send bulk SMS or customized messages to multiple recipients

- Upload CSV files for large-scale distribution

- Send to over 170 countries

**Revision history**

2025-08: Updated the entire tutorial with the latest instructions and UI details.

---
<div class="tutorial-footer"> <p><a href="/prev-url">← PREV_TITLE</a> · <a href="/tutorial-index-en.html">Tutorial Series</a> · <a href="/next-url">NEXT_TITLE →</a></p> <p><strong>Recommended:</strong> <a href="/send-your-first-sms">Send Your First SMS</a> ｜ <a href="/try-voice-api">Try the Voice API</a></p> </div> 
--- 