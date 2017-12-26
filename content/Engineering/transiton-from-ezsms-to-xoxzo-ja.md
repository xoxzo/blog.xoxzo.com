Title: Kプレミアムサービスの、EZSMSからXOXZOへの移行のお勧め
Date: 2017/12/26
Author: Akira Nonaka
Tags: ezsms; xoxzo; KPremium;
Slug: transition-from-ezsms-to-xoxzo
Lang: ja
Summary: EZSMS APIからXOXZO APIへの移行について解説します

EZSMSおよびXOXZOでは従来より、キャリア様への直接接続を提供するKプレミアムサービスを提供してきました。これまでのサポートはKDDI様のみでしたが、この度XOXZOではKプレミアムV2へとサービスをアップグレードし、従来のKDDI様のみならず、Softbank様、DOCOMO様への直接接続のサービスを開始致しました。この直収サービスにより

- 送信IDの固定化
- さらなる到達率の向上

が実現されました。

今後、このような機能の強化はXOXZOサービスを、中心に行う計画ですので、お客さま於かれましては、なるべく早い時期にEZSMS APIからXOXZO APIへの移行を検討されることをお勧めします。なおEZSMSのKプレミアムサービスは現行まま継続されKDDI様のみのサポートとなります。

#### EZSMS APIからXOXZO APIへの移行のための手順

1. [XOXZOのアカウントにサインアップする](https://www.xoxzo.com/ja/accounts/signup/)
1. [XOXZOのAPI SID、Auth Tokenを生成する](https://www.xoxzo.com/ja/you/profile/)
1. EZSMS APIコールを XOXZO APIに書き換える

XOXZO APIの詳細に関しては[ドキュメント](http://docs.xoxzo.com/ja/)をご参照ください

もしEZSMSからXoxzoへの移行に関するご質問やご相談などがございましたら、ご気軽に *help@xoxzo.com* までご連絡ください。

[API比較表のダウンロードはこちらから]({filename}/images/pdf/EZSMS−XOXZO−API比較表.pdf)