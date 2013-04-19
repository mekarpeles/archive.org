import waltz
from waltz import web, render, track
from urlparse import urlparse
import requests
import markdown
import json

urls = ('/terms/?', 'Terms',
        '/ajax/?', 'Ajax',
        '/?', 'Home')
        
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

class Home:
    @track
    def GET(self):
        i = web.input(p='0', q='', rows=50, page=1)
        if i.q:
            return self.POST()
        return render().index(p=int(i.p))

    def POST(self):
        i = web.input(q="", p='0', rows=50, page=1)
        serp = "<p>No Results Found</p>"
        zeroclick=""
        if i.p == '0' and 'http://' in i.q:
            zeroclick = '<img style="height: 50px;" src="http://archive.org/images/wayback.gif"/><span style="position: relative; top: -14px; margin-left: 10px;"><a style="margin-left: 10px;" href="http://web.archive.org/web/*/%s">View older versions o1f %s</a><span>' % (i.q, i.q)
            raise web.seeother('http://web.archive.org/web/*/%s' % i.q)

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

class Ajax:
    def GET(self):
        web.header('Content-Type', 'application/json')
        i = web.input(id="")
        if i.id:
            r = requests.get('http://archive.org/details/%s?output=json' % i.id)
            return json.dumps(r.json())
        return ""

class Terms:
    @track
    def GET(self):
        return render().terms()

if __name__ == "__main__":
    app.run()
