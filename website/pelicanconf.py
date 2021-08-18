#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Vladimir Haltakov"
SITENAME = "SUBOPTIMaL - Seriously Unnecessary Baffling Obscure Perplexing Terms In Machine Learning"
SITEURL = "https://suboptimal.wiki"
PATH = "content"
TIMEZONE = "Europe/Paris"
DEFAULT_LANG = "en"

# Set the theme to minimal
THEME = "themes/minimal/"

# Static pages of the website that will be generated
TEMPLATE_PAGES = {
    "pages/index.html": "index.html",
    "pages/404.html": "404.html",
    "pages/about.html": "about.html",
}

# Settings for the URLs of the blog and the articles
ARTICLE_URL = "explanation/{slug}/"
ARTICLE_SAVE_AS = "explanation/{slug}/index.html"
ARTICLE_ORDER_BY = "titleshort"
INDEX_SAVE_AS = "explanation.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Enable the jinja2content plugin
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["jinja2content"]