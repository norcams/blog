#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import join as pjoin

#AUTHOR = u'First Last'
#AUTHOR_EMAIL = u'email@example.net'
SITENAME = u'norcams'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Oslo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

THEME = pjoin('themes', 'pure')
COVER_IMG_URL = 'http://i.imgur.com/sjoyqiP.jpg'
PROFILE_IMAGE_URL = 'http://i.imgur.com/sjoyqiP.jpg'
TAGLINE = 'culture automation measurement sharing'

SOCIAL = (
          ('google-plus', 'http://plus.norcams.org'),
          ('github', 'https://github.com/norcams/'),
          ('twitter-square', 'https://twitter.com/norcams'),
          ('rss', '/feeds/all.atom.xml'),
         )

DEFAULT_PAGINATION = False

PLUGIN_PATHS = [ 'pelican-plugins' ]
PLUGINS = [ 'gravatar' ]

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/hand.png']
EXTRA_PATH_METADATA = { 
    'extra/CNAME' : {'path' : 'CNAME'},
    'extra/hand.png' : { 'path' : 'favicon.ico' },
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
