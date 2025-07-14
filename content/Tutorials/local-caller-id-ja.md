Title: 【Voice API】ローカル発信者番号を設定しよう  
Date: 2025-07-14  
Author: Aiko Yokoyama  
Tags: voice; tutorial; dial-in; caller-id;  
Slug: voiceapi-local-caller-id  
Thumbnail: images/voiceapi-tutorial-thumbnail.png  
Lang: ja  
Summary: 音声通話APIでローカル発信者番号を使う方法を、ダイアルイン番号の取得から、APIでの利用方法までステップごとに解説します。

![header_image]({filename}/images/xoxzo-tutorial-head.png)

## ローカル発信者番号を設定しよう

Xoxzoの音声通話APIでは、ダイアルイン番号を取得することで、その番号を日本国内向け発信の**発信者番号**として利用することができます。  
このオプションを**「ローカル発信者番号」**と呼びます。

ここでは、実際にローカル発信者番号を設定するための手順を紹介します。

---

### ① ダイアルイン番号を検索します。  

まずは、APIまたはダッシュボードで利用可能な番号を検索します。  
APIでの検索方法：[ドキュメントはこちら](http://docs.xoxzo.com/ja/din.html#finding-a-dial-in-number-via-api)

![screen shot]({filename}/images/voiceapi-localcallerid-01-ja.png)

---

### ② ダイアルイン番号を取得します。  

取得したい番号を決定したら、APIで契約（subscribe）します。  
詳細手順：[ダイアルイン番号の取得](http://docs.xoxzo.com/ja/din.html#subscribing-to-a-dial-in-number-via-api)  
利用料金については、[音声電話着信料金](https://www.xoxzo.com/ja/about/pricing/voice/#din)をご参照ください。

![screen shot]({filename}/images/voiceapi-localcallerid-02-ja.png)

---

### ③ 音声APIで、ローカル発信者番号を指定して発信します。  

音声通話APIで日本国内向けの通話を発信する際、`caller` パラメーターに取得したダイアルイン番号を指定します。

日本国内向け特有のパラメーターを使用することで、ローカル発信者番号として動作します。  
詳しくは、[JP向けのオプション・パラメーター](http://docs.xoxzo.com/ja/voice.html#jp-specific-optional-parameters)をご参照ください。  
発信料金は以下ページにて確認できます：  
[音声電話発信料金（ローカル発信者番号）](https://www.xoxzo.com/ja/about/pricing/voice/#outbound-call)

![screen shot]({filename}/images/voiceapi-localcallerid-03-ja.png)

---

> 💡 **注意：**  
> 複数の番号を発信者番号として使いたい場合は、必要な数のダイアルイン番号を取得してください。

---

[設定方法がわかりにくい場合は、ヘルプページもご確認ください。](https://help.xoxzo.com/ja/xoxzo-voice-api/articles/local-caller-id-for-dial-in-numbers/)

![footer_image]({filename}/images/xoxzo-tutorial-line.png)

今回のチュートリアルはここまでです。  
ローカル発信者番号を使えば、日本国内向けの発信でも「実在する番号」からの着信通知が可能になります。  
ぜひご活用ください。

「ダイアルイン番号って何？」という方は、[ダイアルイン番号の使い方ガイド](https://blog.xoxzo.com/ja/2017/07/01/dialinnumbers-tutorial/)もご覧ください。
