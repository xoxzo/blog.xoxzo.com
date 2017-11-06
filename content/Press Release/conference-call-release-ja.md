Title: 【Xoxzo】電話会議APIをリリースしました
Date: 2017-11-07 00:00
Author: Aiko Yokoyama
Tags: プレスリリース, 電話会議, 効率化, 電話会議, VOICE, ローカル発信者番号, API
Slug: conference-call-release
Lang: ja

いつも、[Xoxzo-クラウド・テレフォニー・プラットフォーム](https://www.xoxzo.com/ja/)をご利用いただき、有難うございます。

2017年11月1日、Xoxzoは[電話会議API](https://www.xoxzo.com/ja/about/voice-api/)をリリースしました。

複数での面会の設定をする際、参加者の予定のすり合わせに電話を何度も掛け直し、苦労した末に、「この電話、3人で同時に話せれば、どんなに効率がいいか…」と、切望したことはありませんか？

Xoxzoの電話会議APIを使えば、複数人数での通話が可能です。様々なチャットアプリではなく、電話番号に電話をかけるため、相手のスマホに同じアプリが入っていなくても、相手がそのアプリにアカウントがなくても大丈夫です。もちろん、固定電話にもかけることができます。

しかも、使い方は簡単。XoxzoはシンプルなウェブAPIで提供されていますので、１つのAPIを呼び出すだけで、ご利用いただけます。電話会議APIを開始するには、`POST`リクエストをこのエンドポイントに行ってください。

```https://api.xoxzo.com/voice/simple/conferences/```

電話の受信者に伝える「発信者番号」や「電話会議の参加者の電話番号」それに、受信者が電話会議にアクセスする際の音声ガイドの言語などが、併記するパラメーターにて設定できます。

詳細は、[Xoxzo APIのドキュメンテーション](http://docs.xoxzo.com/ja/voice.html#simple-conference-api)をご参照ください。

APIのご利用料金は、月額などの定額請求はございません。ご利用頂いた分のみの課金となります。
電話会議APIのご利用には、通常の[「音声発信」](https://www.xoxzo.com/ja/about/voice-api/)と同じ料金が発生します。

日本国内への発信の場合、携帯電話（090, 080, 070で始まる番号）への音声電話発信料金は、一分あたり16円、その他の電話番号への発信は一分あたり10円となります。(参考：[料金ページ](https://www.xoxzo.com/ja/about/pricing/#voice))

また、国内への発信の場合、専用のパラメーターを併記し、[発信者番号を特定の番号に表示できるオプション](https://help.xoxzo.com/ja/xoxzo-cloud-telephony-platform/articles/local-caller-id-for-dial-in-numbers/)がございます。（料金は、[料金ページ](https://www.xoxzo.com/ja/about/pricing/#voice)よりご確認ください。）

このオプションのご利用には、[ダイアルイン番号:音声電話着信APIサービス](https://www.xoxzo.com/ja/about/dial-in-api/)の購読が必要になります。ダイアルイン番号のわかりやすい使い方は、[こちらのチュートリアル](https://blog.xoxzo.com/ja/2017/07/01/dialinnumbers-tutorial/)にてご確認ください。

今後共、[Xoxzo-クラウド・テレフォニー・プラットフォーム](https://www.xoxzo.com/ja/)の新機能リリースにご期待下さい。



__■「Xoxzo」へのアクセス方法 __

「Xoxzo」サイトトップページ： [https://www.xoxzo.com/ja/](https://www.xoxzo.com/ja/)

「Xoxzo」ドキュメンテーション：[http://docs.xoxzo.com/ja/](http://docs.xoxzo.com/ja/)
 
 
__■「Xoxzo」最近のリリース __
[【Xoxzo】国内の電話番号を、発信者として設定できる新機能リリース](https://blog.xoxzo.com/ja/2017/08/23/jp-local-caller-id/)
[【Xoxzo】テキスト読み上げ機能（TTS）が ダイアルインナンバー（DIN）でもご利用頂けます](https://blog.xoxzo.com/ja/2017/05/24/text-to-speech-for-din/)
[【Xoxzo】テキスト読み上げ機能に英語サポートが追加されました。](https://blog.xoxzo.com/ja/2017/03/22/tts-en-release/)


【株式会社Xoxzoについて】

[![Xoxzoロゴ]({filename}/images/xoxzo-logo-02.png)](http://info.xoxzo.com/ja/)

Xoxzoは、2007年2月に設立以来SMS技術を中心に自社サービスを開発、運営をしています。「**継続改善**」をキーワードにしてお客様のニーズを満たすサービスを目指しています。
