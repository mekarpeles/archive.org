#-*- coding: utf-8 -*-

"""
    subapps.api.v1
    ~~~~~~~~~~~~~~
    
    Version 1 of the archive.org api

    :copyright: (c) 2013 by Archive.org
    :license: see LICENSE
"""

import waltz
from subapps.api.v1 import delegator as api_v1
from subapps.api.v2 import delegator as api_v2

urls = ("/v([0-9]+)/?$", "Docs",
        "/v1", api_v1.subapp,
        "/v2", api_v2.subapp,
        "/?", "Redir")

class Docs:
    def GET(self, v="1"):
        try:
            return getattr(waltz.render().api, 'v%s' % v)()
        except:
            return waltz.render().api.index()

class Redir:
    def GET(self):
        raise waltz.web.seeother('/v1/')


subapp = waltz.web.application(urls, globals())
