Title: djangoのmigrationについて(2)
Date: 2017/05/08 14:00
Author: Akira Nonaka
Tags: django; python; migration
Slug: aboud-django-migration-2
Lang: ja
Summary: manage migrate を実行するとなにがおきるか

make migrationsを実行しても、migrationファイルが作成されるだけで、データベース実体には
なにも変化が発生しないことは、前回のBlogに書きました。

実際にデータベースのスキーマに変更を反映するには
```
python manage migrate

```
を実行します。このコマンドを実行すると次の２つの動作が実行されます。

1. mingrationに対応したsqlが、データベースに対して実行される。
2. mingrationを実行したという旨の記録がdjangoのテーブルに記録される。

実行記録がテーブルに記録されていますので、何度`python manage migrate`を実行しても、一つのmigrationがデータベースに
適用されるのは一回限りで、何回も実行されることはありません。





