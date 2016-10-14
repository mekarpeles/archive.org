#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
archive.py
~~~~~~~~~~

:copyright: (c) 2016 by Anonymous.
:license: see LICENSE for more details.
"""

from flask import Flask
from flask.ext.routing import router
from flask.ext.cors import CORS
from views import endpoints
import views
from configs import options

urls = (
    #'/api',
    #'/terms/?'
    '/partials/<path:partial>', views.Partial,
    '/<path:uri>', views.Base,
    '/music', endpoints.Music,
    '/tv', endpoints.Tv,
    '/images', endpoints.Images,
    '/books', endpoints.Books,
    '/games', endpoints.Games,
    '/genealogy', endpoints.Genealogy,
    '/terms', endpoints.Terms,
    '/favicon.ico', endpoints.Fav,
    '/', endpoints.Web
)
app = router(Flask(__name__), urls)

if __name__ == "__main__":
    app.run(**options)
