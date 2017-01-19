#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'chandan u'
SITENAME = u"Chandan 's Blog"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'Data science - Student'
SITEDESCRIPTION = '%s\'s Thoughts and Writings' % AUTHOR
SITELOGO = "https://s.gravatar.com/avatar/1ffef3b08b2d7091ed88bcd36cb2030f?s=80"

BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
ROBOTS = 'index, follow'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%B %d, %Y',
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
#
LINKS = (('portfolio', 'http://hit9.github.io/GhResume/?chandan-u'),)





# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/chandanu/'),
          ('github', 'https://github.com/chandan-u'),
          ('google', 'https://plus.google.com/u/0/112461392309064088729'))



# Menu items

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)



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
PLUGINS = ['ipynb.markup', 'sitemap', 'post_stats', 'better_code_samples', "deadlinks", "pelican_githubprojects", "neighbors", "tag_cloud", "share_post", "footer_insert"]



SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}


#THEME="iris"

THEME = "/Users/chandanuppuluri/pelican-themes/Flex/"

# STATIC FILES PATH : images, css ,js


# IGNORE FILES(Pelican ignores these globs while processing)

IGNORE_FILES= ['.ipynb_checkpoints']




DISQUS_SITENAME = "chandansblog"

STATIC_PATHS = ['images', 'extra', 'pdf']
USE_LESS = True


GITHUB_USER = 'chandan-u'
