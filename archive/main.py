#-*-coding: utf-8 -*-

"""
    main.py
    ~~~~~~~
    
    Main application for archive.org
"""

import json
import requests
import waltz
import utils
from subapps.api.v1 import rest as api

urls = ('/api/v1', api.subapp,
        '/api/?', 'routes.index.Api',
        '/terms/?', 'routes.static.Terms',
        '/developers/?', 'routes.project.Projects',
        '/?', 'routes.index.Home')
        
sessions = {"uid": None,
            "uname": "",
            "karma": 0,
            "logged": False}

env = {'commify': waltz.web.commify,
       'json': json,
       'trunc': utils.truncate,
       'markdown': utils.markdown
       }

app = waltz.setup.dancefloor(urls, globals(), sessions=sessions,
                             env=env, autoreload=False)

if __name__ == "__main__":
    app.run()
