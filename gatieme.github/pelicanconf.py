#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'gatieme'
AUTHOR_EMAIL = u'gatieme@163.com'

TAGLINE = 'Whatever is worth doing is worth doing well.'

SITENAME = u'gatieme'
#SITEURL = u'http://localhost:8000'
SITEURL = u'https://gatieme.github.io'
SITE_SOURCE = u"https://github.com/gatieme/gatieme.github.io"
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')



TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'

ARCHIVES_URL = "archives.html"

DISPLAY_CATEGORIES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = False

GITHUB_URL = u"https://github.com/gatieme/gatieme.github.io"
GITHUB_POSITION = "right"
TWITTER_URL = u'https://twitter.com/gatieme'
FACEBOOK_URL = u'https://www.facebook.com/gatieme'


# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Content path
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files', 'charity']
EXTRA_PATH_METADATA = {
    'files/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    'charity/404.html': {'path': '404.html'},
}


# URL settings
PPAGINATION_PATTERNS = ((1, '{base_name}/', '{base_name}/index.html'),
                       (2, '{base_name}/page/', '{base_name}/page/{number}.html'),)
AARTICLE_URL = ('articles/{slug}.html')
AARTICLE_SAVE_AS = ('articles/{slug}.html')
PPAGE_LANG_SAVE_AS = False


# Blogroll
LINKS = (('LXR', 'http://lxr.free-electrons.com/'),
         ('Pelican', 'http://docs.getpelican.com/en/3.6.3'),
         ('NowCoder', 'http://www.nowcoder.com/contestRoom'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/gatieme'),
          ('StackOverFlow', 'http://stackoverflow.com/users/4935308/gatieme'),
          ('CSDN', 'http://blog.csdn.net/gatieme'),
          ('Twitter', 'https://twitter.com/gatieme'),
          ('FaceBook', 'https://www.facebook.com/gatieme'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = './pelican-themes/zurb-F5-basic'
#THEME = './pelican-themes/tuxlite_tbs'
#COVER_BG_COLOR = '#375152'
DEFAULT_PAGINATION = 10

MD_EXTENSIONS = (['codehilite(css_class=highlight)', 'extra',
                      'fenced_code', 'tables', 'sane_lists'])

# Plugins configure
PLUGIN_PATHS = ["pelican-plugins",]
PLUGINS = ["sitemap", ]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 1,
        "indexes": 0.9,
        "pages": 0.7,
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


# Can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False
