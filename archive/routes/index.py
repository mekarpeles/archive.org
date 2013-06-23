#-*-coding: utf-8 -*-

"""
    routes.index
    ~~~~~~~~~~~~

    Renders assets for the homepage
"""

import requests
from waltz import web, track, render
from api.v1.wayback import timeline
from utils import findurls

class Home:
    def GET(self):
        i = web.input(p='0', cat='', q='', rows=50, page=1)
        if i.q:
            return self.POST()
        return render().index(p=int(i.p))

    def POST(self):
        i = web.input(q='', cat='', p='0', rows=50, page=1)
        serp = "<p>No Results Found</p>"
        zeroclick = []
        if i.p == '0':
            if i.q:
                urls = findurls(i.q)
                if urls:
                    zeroclick += [(timeline(url), url) for url in urls]

        # Fallback to seach all mediatypes
        if i.q:
            r = requests.post('http://archive.org/advancedsearch.php',
                              data={'q': i.q.replace('http://', ''),
                                    'rows': i.rows,
                                    'page': i.page, 'output': 'json'})
            serp = r.json()
        return render().serp(query=i.q, p=i.p, serp=serp,
                             page=i.page, rows=i.rows,
                             zeroclick=zeroclick)

class Api:
    def GET(self):
        raise web.seeother('/api/v1/')
