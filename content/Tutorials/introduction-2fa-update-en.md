Title: Implementing Two-Factor Authentication (2FA) with the OTP API
Date: 2025-08-15 11:00
Author: Miko-chan
Tags: two-factor authentication; tutorial; sms; otp;
Slug: otp-api-2fa-tutorial
Lang: en
Thumbnail: /images/otp-api.jpg
Summary: Learn how to implement secure, simple, and cost-effective two-factor authentication using Xoxzo's new OTP API.

---

> **Important Notice**  
> This article explains how to implement two-factor authentication using Xoxzo's latest OTP API.  
> For the older implementation using our SMS API, see the [previous tutorial](https://blog.xoxzo.com/en/2021/11/22/introduction-2fa-sms/).

---

## 1. Introduction

Two-factor authentication (2FA) is a proven method for strengthening online account security.  
By requiring an additional verification step beyond just a password, it greatly reduces the risk of unauthorized access.

With Xoxzo’s **OTP API**, you can implement SMS-based one-time password verification more easily, securely, and cost-effectively than before.

---

## 2. Basic OTP API Flow

1. **Request an OTP** — Send a one-time password to the user’s phone number.
2. **User enters the OTP** — Your service receives it and verifies the code.
3. **Determine authentication success or failure**

---

## 3. Implementation Example (Python)

The example below uses the `requests` library to request and verify an OTP.

### Requesting an OTP
```python
import os
import requests

# Get API SID and token from environment variables
api_sid = os.getenv("XOXZO_API_SID")
api_token = os.getenv("XOXZO_API_AUTH_TOKEN")

# Request an OTP
resp = requests.post(
    "https://api.xoxzo.com/otp/request/",
    auth=(api_sid, api_token),
    json={
        "website": "https://example.com",  # Your website or app
        "phone_number": "+818012345678"    # User's phone number in E.164 format
    }
)

print(resp.json())
```

### Verifying an OTP
```
resp = requests.post(
    "https://api.xoxzo.com/otp/verify/",
    auth=(api_sid, api_token),
    json={
        "otp_id": "<OTP ID from the request step>",
        "code": "123456"  # Code entered by the user
    }
)

print(resp.json())
```
---

## 4. Benefits of Upgrading

Enhanced Security
Dedicated endpoints and server-side validation provide a more secure verification process.

Simplified Implementation
The new API reduces code complexity, making it easier to maintain.

Improved Cost Efficiency
The OTP API is more affordable than using standard SMS sending for 2FA.
For up-to-date pricing, please check our Pricing page.

Easier Management
View and manage OTP request and verification logs directly from the dashboard.

---

## 5. Conclusion

With the OTP API, you can implement two-factor authentication that is both secure and easy to deploy.
If you are using the older SMS sending API, switching to the OTP API requires minimal code changes while delivering security and cost benefits.

For full API specifications and additional features, see the OTP API documentation.

**Revision History**

2025-08: Published tutorial for implementing 2FA with the new OTP API.

