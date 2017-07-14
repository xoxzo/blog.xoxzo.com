Title: djangoのmigrationについて(3)
Date: 2017/05/25 14:00
Author: Akira Nonaka
Tags: django; python; migration; learning python series;
Slug: about-django-migration-3
Lang: ja
Summary: migrationのクリーンアップ方法について

開発の段階では、しばしばDBのスキーマ変更に試行錯誤が発生します。
このため、最終的には余分なmigrationsが出来あがってしまうことがあります。
例えば、自分がある機能セットAの開発を担当する場合を考えてみましょう。
最初の開発段階で以下のようなモデルを書いたとします。

    class SampleModel1(models.Model):
        name = models.CharField(max_length=200)
        address = models.CharField(max_length=500, null=True)
    
この段階でいちどmigrationをつくります。

    $ python manage.py makemigrations
    Migrations for 'app1':
      app1/migrations/0001_initial.py:
        - Create model SampleModel1
        
このように `0001_initial.py` というmigrationができあがりました。内容はこのようになっています。

    class Migration(migrations.Migration):
    
        initial = True
    
        dependencies = [
        ]
    
        operations = [
            migrations.CreateModel(
                name='SampleModel1',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('name', models.CharField(max_length=200)),
                    ('address', models.CharField(max_length=500, null=True)),
                ],
            ),
        ]
    
さて、開発を進めていくに従って、最初は気が付かなかったカラム`age`が必要であることがわかりました。
そこで`age`という属性をモデルに追加します。

    class SampleModel1(models.Model):
        name = models.CharField(max_length=200)
        address = models.CharField(max_length=500, null=True)
        age = models.IntegerField()

再び、migrationを作成します。

    $ python manage.py makemigrations
    Migrations for 'app1':
      app1/migrations/0002_samplemodel1_age.py:
        - Add field age to samplemodel1
        
２番めのmigrationである`0002_samplemodel1_age`ができあがりました。内容をみてみましょう。
        
    class Migration(migrations.Migration):
    
        dependencies = [
            ('app1', '0001_initial'),
        ]
    
        operations = [
            migrations.AddField(
                model_name='samplemodel1',
                name='age',
                field=models.IntegerField(null=True),
            ),
        ]

*余談ですが `dependencies` という属性に注意してください。このmigrationは `0001_initial` という
migrationに依存していることがわかります。
このようにして、djangoはデータベースのスキーマを変更する場合、migrationを適用する順番を知るわけです。*

さて開発が完了し、コードレビューを行う段階になりました。
ここまでくると、いよいよmigrationをリポジトリにコミットする必要があります。
いまmigrationは２つ出来ていますが、これは開発の途中経過を含んでいます。
レビューは最終的な成果物さえ見てもらえばよいので、途中経過のmigrationは整理したほうがスッキリします。
我々の開発チームではプルリクエストを出す前には「migrationのクリーンアップ」と呼ばれる作業をするのが
習慣となっています。

これを行うには、

1. 自分が開発段階で作成したmigrationを全て削除する
2. 再度` python manage.py makemigrations` を実行する

という手順を踏みます。

ですから今回の場合は
    
    rm 0001_initial.py 0002_samplemodel1_age.py

を実行し`makemigrations`を実行します。

    $ python manage.py makemigrations
    Migrations for 'app1':
      app1/migrations/0001_initial.py:
        - Create model SampleModel1
        
できあがったmigrationを見てみましょう。

    class Migration(migrations.Migration):
    
        initial = True
    
        dependencies = [
        ]
    
        operations = [
            migrations.CreateModel(
                name='SampleModel1',
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('name', models.CharField(max_length=200)),
                    ('address', models.CharField(max_length=500, null=True)),
                    ('age', models.IntegerField(null=True)),
                ],
            ),
        ]

このように、以前は２つに別れていたmigrationが１つにまとまり、最終的なモデルの記述をのみを反映したもの
になりました。これだとレビュアーも、途中経過を全て辿らなくてすみ、本質的なレビューに専念できるのではないでしょうか。

makemigratinの動作は、現在出来上がっている全てのmigrationを適用した結果の仮想的モデル構造と、現在の
モデル記述(models.py)の間の差分をとり、差分があれば、その部分を反映したmigrationをファイルに書き出すという
動作をおこなうので、このような手順が可能になっています。

