#-*- coding: utf-8 -*-

"""
    subapps.api.v1 delegator
    ~~~~~~~~~~~~~~~~~~~~~~~~
    
    Delegates work to the right api v1 path

    :copyright: (c) 2013 by Archive.org
    :license: see LICENSE
"""

import waltz
from subapps.api.v1 import wayback, resource

urls = ("/.+", "Redirect")

class Redirect:
    def GET(self):
        raise waltz.web.seeother('/api/v2/')

subapp = waltz.web.application(urls, globals())
