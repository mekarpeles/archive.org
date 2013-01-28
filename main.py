import waltz
from waltz import render, track

urls = ('/?', 'Home')
sessions = {"uid": None,
            "uname": "",
            "logged": False}
app = waltz.setup.dancefloor(urls, globals(), sessions=sessions,
                             autoreload=False)

class Home:
    @track
    def GET(self):
        return render().index()

if __name__ == "__main__":
    app.run()
