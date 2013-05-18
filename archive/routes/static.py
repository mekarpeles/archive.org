#-*-coding: utf-8 -*-

"""
    routes.static
    ~~~~~~~~~~~~~

    Serves static pages like terms, etc.
"""

from waltz import render, track

class Terms:
    @track
    def GET(self):
        return render().terms()
