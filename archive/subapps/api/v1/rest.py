#-*- coding: utf-8 -*-

"""
    subapps.api.v1
    ~~~~~~~~~~~~~~
    
    Version 1 of the archive.org api

    :copyright: (c) 2013 by Archive.org
    :license: see LICENSE
"""

import json
import waltz
from api.v1 import wayback
from subapps.api.v1 import resource, wayback

urls = ("/wayback", wayback.subapp,
        "/resource", resource.subapp,
        "/?", "Docs",
        "/*", "Docs",
        "", "Docs")

class Docs:
    def GET(self):
        return waltz.render().api()

subapp = waltz.web.application(urls, globals())
