#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gatieme'
SITENAME = u'gatieme'
SITEURL = u'http://localhost:8000'
#SITEURL = u'https://gatieme.github.io'
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
LINKS = (('LXR', 'http://lxr.free-electrons.com/'),
         ('牛客', 'http://www.nowcoder.com/contestRoom'),)

# Social widget
SOCIAL = (('github', 'https://github.com/gatieme'),
          ('stackoverflow', 'http://stackoverflow.com/users/4935308/gatieme'),
          ('csdn', 'http://blog.csdn.net/gatieme'),
          ('twitter', 'https://twitter.com/gatieme'),
          ('facebook', 'https://www.facebook.com/gatieme'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './theme/zurb-F5-basic'
#THEME = './theme/neat'

#  plugins configure
PLUGIN_PATH = u"pelican-plugins"
PLUGINS = ["sitemap"]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
