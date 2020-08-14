#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'raphael'
SITENAME = 'Standards & Deviations'
SITEURL = 'http://standardsanddeviations.net'

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
HOME_COVER = 'assets/images/geometry.jpg'
HEADER_COVERS_BY_TAG = {"abondance-et-liberte": "assets/images/abondance/cover.jpg"}
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["simple_footnotes", "pelican_youtube", "collate_content"]
PUBLICATIONS_SRC = 'content/pubs.bib'

# Social Widget
SOCIAL = (('twitter', 'https://twitter.com/stdanddev'),
	('Github', 'http://github.com/testingcan'))

# Bio

AUTHORS_BIO = {
	'raphael': {
		'name': 'Raphael',
		'website': 'standardsanddeviations.net',
		'bio': 'A small blog to organise my thoughts. Sometimes insightful, often rambling.',
		'cover': 'assets/images/geometry.jpg',
		'twitter': 'STDandDEV'
	}
}

