Title: Cache busting in Django
Date: 2018-08-22
Slug: cache-busting-in-django
Lang: en
Tags: python; django; css; cache; 
Author: Hyejeong Park
Summary: How to cache bust in Django using ManifestStaticFilesStorage.

## Cache busting CSS with query strings

Because visitors' browsers locally store a cached copy of the static files, they are may unable to see the changes when you update your site. This can be troublesome, so we need a cache busting strategy to clear cache and to make the browser download a fresh copy of the static assets.

By using a query string, we can tell the browser that there is a new version of the file. I used to add the version to CSS file like this:

```html
<link href="{{ STATIC_URL }}css/base.css?v=1.4" rel="stylesheet" type="text/css">
```
However, it is easy to forget to change the query string manually every time. So I started to find the other way to automate CSS versioning.

## Django does it for us

Instead of adding a query string, changing the file name itself is also working for cache busting. There is [ManifestStaticFilesStorage](https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/#manifeststaticfilesstorage) in Django that appends the MD5 hash of the file’s content to the filename. For example, the `css/base.css` file would also be saved as `css/base.e352ca3230fc.css`.

To enable the ManifestStaticFilesStorage, you have to meet the following requirements:

- the `STATICFILES_STORAGE` setting is set to `'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'`.
- the `DEBUG` setting is set to `False`.
- you’ve collected all your static files by using the `collectstatic` management command.

```python
# settings.py
DEBUG = False
...
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
```
And add the `static` template tag to build the URL for the given relative path using the configured `STATICFILES_STORAGE`.

```html
<!-- base.html -->
{% load static from staticfiles %}
...
<link href="{% static 'css/base.css' %}" rel="stylesheet" type="text/css">
```

With this changes, the static filename will be replaced automatically with hashed name one when run `collectstatic`.

## ManifestFilesMixin support in django-storages

Because Xoxzo is using `S3BotoStorage`, we need a special mixin to use `ManifestStaticFilesStorage`.
[django-storages](https://github.com/jschneier/django-storages) supports `ManifestFilesMixin`, and you can add it to your storage class.

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

Congratulations! Now you can get the hashed CSS file!
```html
<link href="../css/base.e352ca3230fc.css" rel="stylesheet" type="text/css">
```