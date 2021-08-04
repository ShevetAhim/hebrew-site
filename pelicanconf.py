#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
import jinja2content

AUTHOR = 'Tom Gurion'
SITENAME = 'shevet-ahim'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = 'he'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme'
SLUGIFY_SOURCE = 'basename'

PLUGINS = [jinja2content]

DIRECT_TEMPLATES = ['index', 'activities']