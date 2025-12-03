Title: When SMS Doesn’t Arrive: Voice Call Authentication as an Alternative
Slug: sms-vs-voice-auth
Lang: en
Date: 2025-11-21
Tags: SMS, Voice API, Authentication, Accessibility, Xoxzo
Author: Aiko Yokoyama
Thumbnail: images/smsvsvoice-en.jpg
Summary: When SMS delivery is unreliable, voice call text-to-speech authentication can be an effective alternative. It works even with landlines and improves accessibility for a wider range of users.

---

<img src="https://blog.xoxzo.com/images/smsvsvoice-en.jpg" width="200" height="200" style="margin: 0;">

## When SMS Doesn't Arrive: Voice Call Authentication as an Alternative

SMS is widely used for identity verification.  
However, situations where **“SMS doesn’t arrive”** or **“SMS can’t be found”** do occur:

- International SMS blocking settings  
- Carrier network delays  
- Messages being routed into apps like Plus Message  
- Users who rely on landline phones rather than mobile devices

In these cases, **voice call + text-to-speech authentication** is a practical and reliable alternative.

---

## How It Works

Voice call authentication places an automated call to the user’s phone number and  
reads out the verification code using TTS (text-to-speech):

“This is your verification service. Your code is 1 2 3 4.”


- The user simply answers the call  
- Works on both mobile phones and **landlines**  
- Stable in areas where SMS delivery may be unreliable  
- Easy to integrate alongside SMS verification

---

## When Voice Authentication Is Especially Useful

### ① Environments where SMS is unstable
International SMS restrictions, Plus Message routing, or other settings  
may cause SMS to be delayed or undelivered.

### ② Users with only a landline phone
Reception desks, elderly users, or certain business environments  
may not use mobile phones at all—but **voice calls always work**.

### ③ Users who have difficulty checking codes visually
Since the code is read aloud, voice authentication improves accessibility.

---

## Cost & Implementation

With Xoxzo’s **Voice API**, voice call authentication costs:

- **About 10 JPY per call** (japanese domestic, see [pricing page](https://www.xoxzo.com/en/about/pricing/voice/#outbound-call))  
- The similar price range as SMS verification  
- Easy to add to existing authentication flows

Documentation: https://docs.xoxzo.com/en/voice/

---

## Comparison: SMS vs Voice Call Authentication

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid #ccc; padding: 8px;">Item</th>
      <th style="border: 1px solid #ccc; padding: 8px;">SMS Authentication</th>
      <th style="border: 1px solid #ccc; padding: 8px;">Voice Call Authentication</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Delivery Method</td>
      <td style="border: 1px solid #ccc; padding: 8px;">SMS app</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Answer the call</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Landline Support</td>
      <td style="border: 1px solid #ccc; padding: 8px;">✕</td>
      <td style="border: 1px solid #ccc; padding: 8px;">◯</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Impact of International SMS Blocking</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Affected</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Not affected</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Carrier Network Delays</td>
      <td style="border: 1px solid #ccc; padding: 8px;">May occur</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Less likely</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Accessibility</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Requires reading the code</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Code is spoken aloud</td>
    </tr>
    <tr>
      <td style="border: 1px solid #ccc; padding: 8px;">Cost</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Approx. 10 JPY (Xoxzo OTP: from 3 JPY)</td>
      <td style="border: 1px solid #ccc; padding: 8px;">Approx. 10 JPY (<a href="https://www.xoxzo.com/en/about/pricing/voice/#outbound-call" target="_blank">Pricing page</a>)</td>
    </tr>
  </tbody>
</table>


---

## Implementation Ideas

- Show SMS **and** voice call authentication options on the login screen  
- Provide voice call as a fallback when SMS verification fails  
- Use voice-first authentication for users with landlines

This reduces verification failure and ultimately  
**helps prevent user drop-off during onboarding.**

---

## Summary

- SMS delivery can be unstable depending on device and carrier  
- Voice call authentication is a highly reliable alternative  
- Works with landlines and improves accessibility  
- Simple to implement with Xoxzo’s Voice API  

---

## Related Links

- [Xoxzo SMS API Documentation](https://docs.xoxzo.com/en/sms/)  
- [Xoxzo Voice API](https://docs.xoxzo.com/en/voice/)  
- [Xoxzo OTP API (3 JPY/SMS)](https://docs.xoxzo.com/en/otp/)  

## Related Articles
<a href="/Industry/sms-not-received-checkpoints-en.md">What to Do When an SMS Doesn't Arrive: 3 Things to Check</a><br>
<a href="/Industry/sms-vs-social-auth-en.md">SMS Authentication vs Social App Authentication: Which Is More Reliable?</a>
