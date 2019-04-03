Title: Djangoでのキャッシュバスティング
Date: 2018-08-22
Slug: cache-busting-in-django
Lang: ja
Tags: python; django; css; cache; 
Author: Hyejeong Park
Summary: ManifestStaticFilesStorage を使った Django でのキャッシュバスティング方法

## クエリ文字列を利用したCSSのキャッシュバスティング

あなたのサイトを訪れる人が使っているブラウザは、静的ファイルのコピーをローカルにキャッシュして保存します。
そのため、サイトを更新しても、変更点を見られない可能性があるのです。これではやっかいなので、
キャッシュをクリアしてブラウザに静的アセットの最新版をダウンロードするような、キャッシュバスティング戦略が必要となります。

クエリ文字列を利用すると、ブラウザにファイルの新しいバージョンがあることを通知できます。
私は以下のようにCSSファイルにバージョンを追加していました。

```html
<link href="{{ STATIC_URL }}css/base.css?v=1.4" rel="stylesheet" type="text/css">
```
しかし、この方法では、毎回クエリ文字列を手動で変更するのを忘れがちになります。
ですので、CSSのバージョン付けを自動化しようと、別の方法を探すことにしました。

## Djangoがやってくれます

クエリ文字列を追加する代わりに、ファイル名自体を変更してもキャッシュバスティングは機能します。
Djangoには [ManifestStaticFilesStorage](https://docs.djangoproject.com/ja/2.1/ref/contrib/staticfiles/#manifeststaticfilesstorage) 
があり、ファイルのコンテンツのMD5ハッシュ値をファイル名に付加できるのです。例えば、
`css/base.css` ファイルが `css/base.e352ca3230fc.css`という風にも保存されるのです。

ManifestStaticFilesStorage を有効にするには、以下の条件を満たしている必要があります。

- the `STATICFILES_STORAGE` の設定が `'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'`となっていること。
- `DEBUG` の設定が `False`であること。
- •	全ての静的ファイルが管理コマンドの `collectstatic` で集められていること。

```python
# settings.py
DEBUG = False
...
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
```
それから `static` というテンプレートタグを追加して、任意の相対パスのURLが、設定済みの  `STATICFILES_STORAGE`を利用して生成されるようにします。

```html
<!-- base.html -->
{% load static from staticfiles %}
...
<link href="{% static 'css/base.css' %}" rel="stylesheet" type="text/css">
```

このような変更を行うと `collectstatic`の実行時に静的なファイル名が自動的にハッシュ付きのものに置き換わります。

## django-storagesのManifestFilesMixinサポート

Xoxzo では `S3BotoStorage`を利用していますので `ManifestStaticFilesStorage`を利用するためには、特別なmixinが必要です。
[django-storages](https://github.com/jschneier/django-storages) は`ManifestFilesMixin`をサポートしているので、
ストレージのクラスへの追加が可能になります。

```python
# storage.py
from storages.backends.s3boto import S3BotoStorage as S3BotoStorageOrig
from django.contrib.staticfiles.storage import ManifestFilesMixin

class S3BotoStorage(S3BotoStorageOrig):
    ...

class StaticStorage(ManifestFilesMixin, S3BotoStorage):
    pass
```

```python
# settings.py
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storage.ManifestS3Storage'
```

おめでとうございます！

これでハッシュ化されたCSSファイルが使えるようになりました！

```html
<link href="../css/base.e352ca3230fc.css" rel="stylesheet" type="text/css">
```
