import waltz
from waltz import web, render, track
from urlparse import urlparse
import requests

urls = ('/?', 'Home')
sessions = {"uid": None,
            "uname": "",
            "logged": False}
env = {'commify': web.commify}
app = waltz.setup.dancefloor(urls, globals(), sessions=sessions,
                             env=env, autoreload=False)

class Home:
    @track
    def GET(self):
        i = web.input(p='0')
        return render().index(p=int(i.p))

    def POST(self):
        i = web.input(q="", p='0', rows=50, page=1)
        serp = "<p>No Results Found</p>"
        zeroclick=""
        if i.p == '0' and 'http://' in i.q:
            zeroclick = '<img style="height: 50px;" src="http://archive.org/images/wayback.gif"/><span style="position: relative; top: -14px; margin-left: 10px;">Go Wayback in time! <a style="margin-left: 10px;" href="http://web.archive.org/web/*/%s">View older versions of %s</a><span>' % (i.q, i.q)
            #raise web.seeother('http://web.archive.org/web/*/%s' % i.q)

        # Fallback to seach all mediatypes
        if i.q:
            r = requests.post('http://archive.org/advancedsearch.php',
                              data={'q': i.q.replace('http://', ''),
                                    'rows': i.rows,
                                    'page': i.page, 'output': 'json'})
            serp = r.json
        return render().serp(query=i.q, p=i.p, serp=serp,
                             page=i.page, rows=i.rows,
                             zeroclick=zeroclick)

if __name__ == "__main__":
    app.run()
