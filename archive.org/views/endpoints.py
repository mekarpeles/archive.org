#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
endpoints.py
~~~~~~~~~~~~

:copyright: (c) 2016 by Anonymous.
:license: see LICENSE for more details.
"""

import requests
import markdown
from flask import render_template, request, Response
from flask.views import MethodView
from api.wayback import timeline
from utils import findurls, commify, truncate, join

md = markdown.Markdown(output_format='html4')

class Images(MethodView):
    def get(self, uri=None):
        i = dict(request.args)
        return render_template(
            'base.html', template='/partials/index.html',
            service="images"
        )

    def post(self):
        return "images"

class Fav(MethodView):
    def get(self):
        return Response("")
    
class Music(MethodView):
    def get(self, uri=None):
        return render_template(
            'base.html', template='/partials/music.html',
        )

class Genealogy(MethodView):
    def get(self, uri=None):
        return render_template(
            'base.html', template='/partials/genealogy.html',
        )

class Books(MethodView):
    def get(self, uri=None):
        return render_template(
            'base.html', template='/partials/books.html',
        )

class Games(MethodView):
    def get(self, uri=None):
        return render_template(
            'base.html', template='/partials/games.html',
        )

class Tv(MethodView):
    def get(self, uri=None):
        return render_template(
            'base.html', template='/partials/tv.html',
        )    

class Terms(MethodView):
    def get(self, uri=None):
        return render_template(
            'base.html', template='/partials/terms.html',
        )


class Web(MethodView):
    def get(self, uri=None):
        i = dict(request.args)
        return render_template('base.html', template='/partials/web.html')

    def post(self):
        page = request.form.get('page', 0)
        rows = request.form.get('rows', 50)
        query = request.form.get('q', '')
        zeroclick = []

        if query:
            urls = findurls(query)
            if urls:
                zeroclick += [(timeline(url), url) for url in urls]

            # Fallback to seach all mediatypes
            r = requests.post('http://archive.org/advancedsearch.php',
                              data={'q': query.replace('http://', ''),
                                    'rows': rows,
                                    'page': page,
                                    'output': 'json'
                              })
            serp = r.json()
            lambdas = {
                'markdown': lambda s: md.convert(s),
                'join': join,
                'trunc': truncate
            }
            results = {
                "count": serp['response']['numFound'],
                "time": commify(serp['responseHeader']['QTime'] / 1000.0),
                "items": serp['response']['docs']
            }

            return render_template(
                'base.html', template='/partials/serp.html',
                query=query, results=results, zeroclick=zeroclick,
                utils=lambdas, service=""
            )

urls = ()
