Title: 【Xoxzo】ログダウンロード機能に、音声APIが加わりました
Date: 2020-08-18
Slug: logs-download-voice
Lang: ja
Tags: ログダウンロード; 新規リリース; 2020; 音声API;
Thumbnail: images/freepik/young-females-download-icon.jpg
Author: Aiko Yokoyama
Summary: ダッシュボードより、音声APIのご利用ログファイルもダウンロードできるようになりました！


Xoxzoのダッシュボードに、[音声API](https://www.xoxzo.com/ja/about/voice-api/)ご利用のログファイルダウンロード機能が追加されましたので、通知させていただきます。

この度、[音声プレイバックの配信状況を確認するAPI](https://docs.xoxzo.com/ja/voice.html#checking-call-status)を使わずとも、
アカウントにログインすれば、お好みの期間のご利用について、csv ファイルを直接ダウンロードできるようになりました。

[ダイヤル・イン・ナンバー](https://docs.xoxzo.com/ja/din.html)についても同様にダウンロードが可能です。

ダウンロードできる csv ファイル内の項目は、下記のとおりです。

<table>
  <tr>
    <th>音声API</th>
    <th>ダイヤル・イン・ナンバー</th>
  </tr>
  <tr>
    <td>call_type<br>
        caller<br>
        callid<br>
        cost<br>
        direction<br>
        start_time(UTC)<br>
        end_time(UTC)<br>
        duration(secs)<br>
        recipient<br>
        status<br>
        tags<br>
        url<br>
        apiuser</td>
    <td>caller<br>
        cost<br>
        direction<br>
        recipient<br>
        start_time(UTC)<br>
        end_time(UTC)<br>
        duration(secs)<br>
        status<br>
        apiuser<br>
        uuid<br>
        actionurl<br></td>
    </tr>
</table>


ダウンロードいただけるログは、 **過去42日まで、遡ることができます。**

## ダウンロードの方法

超シンプルです! 

ダッシュボードへログインし、左側のメニューより、_ご利用ログダウンロード_ をクリックしてください。

![Download dashboard](/images/logs-download-feature-screenshot-ja.png)

ダウンロードしたいログの日付を選択することも可能ですが、「過去7日間」「過去30日間」と言った、既定の選択肢もご用意しております。

ダウンロードのプロセスは、バックグランドで行われます。
ダウンロードファイルの生成にお時間が掛かりそうであれば、後ほどお戻りいただき、出来上がったファイルを確認していただくことができます。

下方の表にて「生成状況」が「生成完了」となりましたら、ログファイル名をクリックしてダウンロードしてください。

## ユーザーリクエストにお応えして生まれました

[Xoxzoのログダウンロード](https://blog.xoxzo.com/ja/2019/08/13/logs-download-feature-new-release/)は、ユーザー様のリクエストから生まれた機能です。
リリース時には、SMSのご利用ダウンロードのみが可能でした。

Thank you to rawpixel.com for the thumbnail:
[Background photo created by rawpixel.com - www.freepik.com](https://www.freepik.com/free-photos-vectors/background)
