Title: 【EZSMS】ログ・ファイルの読み方
Date: 2022-06-27
Author: Aiko Yokoyama
Tags: sms; tutorial; log; ezsms;
Slug: ezsms-how-to-read-log
Thumbnail: images/ezsms-tutorial-thumbnail.png
Lang: ja
Summary: EZSMSで行った送信や、ダイヤルSMSへの着信が記録されているログ・ファイル。アカウントページからダウンロードして開いたら、たくさんの項目が並んでいます。ログ・ファイルの内容をどのように確認していくのか、解説します。

![header_image]({filename}/images/ezsms-tutorial-head.png)

[前回のチュートリアル](https://blog.xoxzo.com/ja/2022/06/24/ezsms-log-download/)では、ログ・ファイルのダウンロードについてご案内しました。実際にダウンロードしたファイルを開いてみましたか？<br>

たった一通のSMS送信の記録にしては、項目がずらりと並んでいて、驚かれたかもしれないですね。シンプルなようでいて、SMS送信には、様々な要素があることがおわかりいただけたかと思います。<br>

今回は、ダウンロードできるファイルの種類とファイル内の項目について、ご説明いたします。

## ログ・ファイルのファイル形式
パソコンで扱うファイルには、それぞれファイル名の最後にピリオド（ドット）で区切られた英数字 1〜4字で構成される _拡張子_ がついています。
例えば、画像ファイルには「jpg」や「png」、表計算ファイルには「xlsx」や、圧縮ファイルは「zip」などで、これによって、ファイルの種類が識別されています。


EZSMSのアカウントページからダウンロードできるログ・ファイルは「CSV」という拡張子がついた [.csv形式のファイル](https://ja.wikipedia.org/wiki/Comma-Separated_Values) です。
このファイルは、テキストファイルなので、そのまま開くと、項目が「,」（コンマ）で区切られた形で表示されますが、エクセルなどの表計算ソフトで開くと、簡単に見やすい罫線引きの表として表示できます。

**例）** <br>
.csvファイルを[テキストファイル](https://ja.wikipedia.org/wiki/Comma-Separated_Values)として開く<br>
> 国名,首都,国土面積,人口,通貨
> 日本,東京,"377,973,89km2", 	1億2614万6099人,円
> アメリカ合衆国,コロンビア特別区,"9,834,000km2",3億3100万3000人,USD

.csvファイルを[表計算ファイル](https://ja.wikipedia.org/wiki/%E8%A1%A8%E8%A8%88%E7%AE%97%E3%82%BD%E3%83%95%E3%83%88)として開く<br>
<div class="table-responsive">
  <table>
<tr>
  <th>国名</th>
  <th>首都</th>
  <th>国土面積</th>
  <th>人口</th>
  <th>通貨</th>
 </tr>
<tr>
  <td>日本</td>
  <td>東京</td>
  <td>377,973,89km2</td>
  <td>1億2614万6099人</td>
  <td>円</td>
</tr>
<tr>
  <td>アメリカ合衆国</td>
  <td>コロンビア特別区</td>
  <td>9,834,000km2</td>
  <td>3億3100万3000人</td>
  <td>USD</td>
 </tr>
</table>
</div>

表計算ソフトで開くと、人間の目にとって見やすく、その後分析に使うように、データの並べ替えや分類を行ったり、計算式を入れて計算するのに便利ですね。<br>

## ログ・ファイルを読もう
さて、開き方がわかったところで、EZSMSでダウンロードできる、SMS送信のログ・ファイルの読み方をご紹介します。
<br><br>
ファイル内にあるデータは、横位置業に一件の送信についての詳細が、項目ごとに記されています。
その項目は、下記のとおりです。
<div class="table-responsive">
  <table border="1" cellpadding="1" cellspacing="1">
    <tbody>
      <tr>
        <th style="text-align: center;"></th>
        <th style="text-align: center;">項目</th>
        <th style="text-align: center;">日本語</th>
        <th style="text-align: center;">説明</th>
      </tr>
      <tr>
        <td>1</td>
        <td>SEND TIME<br>
        (LOCALTIME)</td>
        <td>送信日時</td>
        <td>EZSMS側でメッセージの送信リクエストを受け付けた時刻。</td>
      </tr>
      <tr>
        <td>2</td>
        <td>LATEST STATUS UPDATED TIME<br>
        (LOCAL TIME)</td>
        <td>送信ステータス<br>最新更新日時</td>
        <td>SMS送信ステータスを更新した時刻。</td>
      </tr>
      <tr>
        <td>3</td>
        <td>DELIVERY END TIME<br>
        (LOCALTIME)</td>
        <td>送信終了日時</td>
        <td>送信完了時刻。メッセージが不達の場合でも送信完了といいます。</td>
      </tr>
      <tr>
        <td>4</td>
        <td>MESSAGE ID</td>
        <td>メッセージID</td>
        <td>各メッセージに特定するためユニークなID。固有の送信について、問い合わせをいただく際に必要です。</td>
      </tr>
      <tr>
        <td>5</td>
        <td>RECIPIENT</td>
        <td>受信者の電話番号</td>
        <td>送信の宛先</td>
      </tr>
      <tr>
        <td>6</td>
        <td>SENDER ID</td>
        <td>送信元ID</td>
        <td>送信時に送信元として設定されたID</td>
      </tr>
      <tr>
        <td>7</td>
        <td>MESSAGE</td>
        <td>メッセージ本文</td>
        <td>設定されたメッセージ</td>
      </tr>
      <tr>
        <td>8</td>
        <td>MESSAGE STATUS</td>
        <td>送信ステータス</td>
        <td>メッセージの送信状況です。以下のステータスのどれかになります。<br>
        &nbsp;&nbsp;<strong>MESSAGE_DELIVERY_COMPLETE</strong><br>
        &nbsp;&nbsp;正常に配信完了しました。<br>
        &nbsp;&nbsp;<strong>MESSAGE_PASSED_TO_CARRIER_FOR_DELIVERY</strong><br>
        &nbsp;&nbsp;メッセージはキャリアに渡っています。配信完了までしばらくお待ちください。<br>
        &nbsp;&nbsp;<strong>MESSAGE_EXPIRED</strong><br>
        &nbsp;&nbsp;メッセージはキャリアまで渡っていますが、キャリアが決めたリトライ回数に達しても宛先の携帯電話まで着信できなかったため配信できませんでした。<br>
        &nbsp;&nbsp;<strong>MESSAGE_DELIVERY_FAILED</strong><br>
        &nbsp;&nbsp;配信に失敗しました。考えられる理由として [こちら](https://help.xoxzo.com/ja/ezsms-sms-delivery-service/articles/what-would-cause-the-sending-failure/) をご覧ください。</td>
      </tr>
      <tr>
        <td>9</td>
        <td>USED_POINTS</td>
        <td>消費ポイント数</td>
        <td>このメッセージの送信が消費したポイント数 参照： [料金ページ](https://www.ezsms.biz/ja/faq/price/) </td>
      </tr>
      <tr>
        <td>10</td>
        <td>SHORTLINK STATUS</td>
        <td>ショートリンクの<br>ステータス</td>
        <td>リンクトラッキングを使った送信時に、リンク（URL）がアクセスされたかどうかを示します。<br>
        &nbsp;&nbsp;<strong>0 の場合</strong> リンクはアクセスされていません<br>
        &nbsp;&nbsp;<strong>1 の場合</strong>　リンクはアクセスされています</td>
      </tr>
      <tr>
        <td>11</td>
        <td>SHORTLINK URL</td>
        <td>ショートリンクURL</td>
        <td>リンクトラッキングに使われた、ショートURL<br>（有効期限は生成後90日です）</td>
      </tr>
    </tbody>
  </table>
</div>




![end of tutorial]({filename}/images/ezsms-tutorial-line.png)

今回のチュートリアルは、ここまでです。<br>
ログ・ファイル内に並ぶ、たくさんの項目の読み方がおわかりいただけましたか？<br>
次回は、ログ・ファイルの保存についてです。<br>
お楽しみに。

