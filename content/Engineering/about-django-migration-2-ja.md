Title: djangoのmigrationについて(2)
Date: 2017/05/08 14:00
Author: Akira Nonaka
Tags: django; python; migration
Slug: aboud-django-migration-2
Lang: ja
Summary: manage migrate を実行するとなにがおきるか

`makemigrations`を実行しても、migrationファイルが作成されるだけで、データベース自体にはなにも変化が発生しないことは、前回のBlogに書きました。

実際に変更をデータベースのスキーマに反映するには
```
$ python manage migrate

```
を実行します。このコマンドを実行すると次の２つの動作が行われます。

1. migrationに対応したsqlが、データベースに対して実行される。[^注1]
2. migrationを実行したという旨の記録が`django_migrations`というテーブルに記録される。

実行履歴がテーブルに記録されていますので、何度`python manage migrate`を実行しても、
一つのmigrationがデータベースに適用されるのは一回限りで、何回も実行されることはありません。

テーブル`django_migrations`の内容はこのようになっており、アプリケーション名、migration名、適用日時などが記録されています。

![テーブルサンプル]({filename}/images/dinajgo_migrations.png)

実際にmigrationを作り、`migrate`の実行前後でこのテーブルの中にどのようにレコードが書き込まれるか、
観察してみると動作の理解が深まるでしょう。

また未適用のmigrationがある状態で`python manage.py runserver`を実行すると
```
$ python manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.
```
といったように「まだ未適用のmigrationがあるので正しく動作しない可能性があります」といった警告が表示されます。

Webアプリケーション開発、運用中のデータベース改版履歴管理には、みなさん苦労されていることと思います。
djangoフレームワークの中で、migrationの機能は大変強力ですので、是非チェックすることをお勧めします。

[^注1]:実行されるsqlを確認したい時は`$python manage.py sqlmigrate`を使うことができます。
