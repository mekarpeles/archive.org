#-*- coding: utf-8 -*-

"""
    subapps.api.v1.wayback
    ~~~~~~~~~~~~~~~~~~~~~~
    
    REST API to retrieve wayback information

    :copyright: (c) 2013 by Archive.org
    :license: see LICENSE
"""

import json
import requests
import waltz
from utils import validurl
from api.v1 import wayback

urls = ("/(.+)/?", "Wayback",
        "/?", "Info")

class InvalidUrlError(Exception): pass

class Wayback:
    def GET(self, url=""):
        if validurl(url):
            src = wayback.timeline(url)
            waltz.web.header('Content-Type', 'image/png')
            return requests.get(src).content
        raise InvalidUrlError('%s is an invalid url' % url)

class Info:
    def GET(self):
        return "Wayback API"

subapp = waltz.web.application(urls, globals())
