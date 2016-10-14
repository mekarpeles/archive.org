#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__init__.py
~~~~~~~~~~~

:copyright: (c) 2016 by Anonymous.
:license: see LICENSE for more details.
"""

from flask import render_template
from flask.views import MethodView

class Base(MethodView):
    def get(self, uri=None):
        return render_template('base.html')

class Partial(MethodView):
    def get(self, partial):
        return render_template('partials/%s.html' % partial)