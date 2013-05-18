#-*-coding: utf-8 -*-

"""
    routes.rest
    ~~~~~~~~~~~

    Serves static pages like terms, etc.
"""

import json
import requests
from waltz import web

class Ajax:
    def GET(self):
        web.header('Content-Type', 'application/json')
        i = web.input(id="")
        if i.id:
            r = requests.get('http://archive.org/details/%s?output=json' % i.id)
            return json.dumps(r.json())
        return ""

