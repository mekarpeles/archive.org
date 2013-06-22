#-*- coding: utf-8 -*-

"""
    subapps.api.v1.resource
    ~~~~~~~~~~~~~~~~~~~~~~~
    
    REST API to retrieve resources and resource metadata

    :copyright: (c) 2013 by Archive.org
    :license: see LICENSE
"""

import json
import requests
import waltz

urls = ("/(.+)/meta/?", "Metadata",
        "/(.+)/?", "Resource",
        "/?", "Info")

def API(web):
    def decorator(f):
        def inner(*args, **kwargs):
            web.header('Content-Type', 'application/json')
            return json.dumps(f(*args, **kwargs))
        return inner
    return decorator

class Metadata:
    @API(waltz.web)
    def GET(self, id_):
        if id_:
            r = requests.get('http://archive.org/details/%s?output=json' % id_)
            return json.dumps(r.json())
        return ""

subapp = waltz.web.application(urls, globals())
