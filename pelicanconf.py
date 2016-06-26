#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gatieme'
SITENAME = u'gatieme'
SITEURL = u'https://gatieme.github.io'
SITE_SOURCE = u"https://github.com/gatieme/gatieme.github.io"

FEED_DOMAIN = SITEURL
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

ARCHIVES_URL = "archives.html"

GITHUB_URL = u"https://github.com/gatieme/gatieme.github.io"
GITHUB_POSITION = "right"

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
#RELATIVE_URLS = True

THEME = './theme/pelican-bootstrap3'
#THEME = './theme/neat'

