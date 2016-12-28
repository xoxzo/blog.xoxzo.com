#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, '.'))

AUTHOR = 'Iqbal Abdullah'
SITENAME = 'Xoxzo Official Blog: Empowerment'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DEFAULT_DATE_FORMAT = "%Y-%m-%d"
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

#THEME           = 'themes/simple'
THEME           = 'themes/xoxzo'
PLUGIN_PATHS    = [os.path.join(PROJECT_ROOT, 'plugins'),]
PLUGINS         = ["i18n_subsites", ]

I18N_UNTRANSLATED_ARTICLES  = "keep"
I18N_UNTRANSLATED_PAGES     = "keep"

I18N_SUBSITES   = {
    'ja': {
        'SITENAME': 'Xoxzoの公式ブログ：「開花、発展、向上させる」',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
    },
    'ms': {
        'SITENAME': '',
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
    },
    'en': {
        'SITENAME': SITENAME,
        'STATIC_PATHS': STATIC_PATHS,
        'THEME': THEME,
    },
}

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT,
    'ja': DEFAULT_DATE_FORMAT,
    'ms': DEFAULT_DATE_FORMAT,
}

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

