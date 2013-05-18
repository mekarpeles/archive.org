#-*-coding: utf-8 -*-

"""
    main.py
    ~~~~~~~
    
    Main application for archive.org
"""

import waltz
from waltz import web
import requests
import markdown
import json

urls = ('/terms/?', 'routes.static.Terms',
        '/ajax/?', 'routes.rest.Ajax',
        '/projects/?', 'routes.project.Projects',
        '/?', 'routes.index.Home')
        
sessions = {"uid": None,
            "uname": "",
            "logged": False}

env = {'commify': web.commify,
       'json': json,
       'join': lambda x, y: y.join(x),
       'trunc': lambda x, l: '%s ...' % x[:l] if len(x) > l else x,
       'markdown': markdown.Markdown(safe_mode=True,
                                     html_replacement_text='').convert}

app = waltz.setup.dancefloor(urls, globals(), sessions=sessions,
                             env=env, autoreload=False)

if __name__ == "__main__":
    app.run()
