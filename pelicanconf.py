#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'testingcan'
SITENAME = 'Standards & Deviations'
SITEURL = ''

THEME = "../attila/"
STATIC_PATHS = ['assets']

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DEFAULT_METADATA = {
    'status': 'draft',
}


# Theme
HOME_COVER = 'assets/images/blog_cover.jpg'
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["simple_footnotes"]