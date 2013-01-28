import waltz
from waltz import web, render, track

urls = ('/?', 'Home')
sessions = {"uid": None,
            "uname": "",
            "logged": False}
env = {"type": type}
app = waltz.setup.dancefloor(urls, globals(), sessions=sessions,
                             env=env, autoreload=False)

class Home:
    @track
    def GET(self):
        i = web.input(p=0)
        return render().index(page=int(i.p))

if __name__ == "__main__":
    app.run()
