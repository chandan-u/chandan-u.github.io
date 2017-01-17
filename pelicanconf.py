#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'chandan u'
SITENAME = u'Text-Mining Tutorial'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
         ('Python.org', 'http://python.org/'),
         )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Blog index recreated at :
INDEX_SAVE_AS = 'index.html'


# Saving pages in main directory instead of sub:
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

#THEME="iris"

THEME = "/Users/chandanuppuluri/pelican-themes/Flex/"

# STATIC FILES PATH : images, css ,js


# IGNORE FILES(Pelican ignores these globs while processing)

IGNORE_FILES= ['.ipynb_checkpoints']


