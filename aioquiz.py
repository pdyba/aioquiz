# !/usr/bin/python3.5
from sanic import Sanic

from views import AuthenticateView
from views import QuestionView
from views import UserView
from views import LessonView

app = Sanic()

app.static('/', './static/index.html')
app.static('/sum', './static/summary.html')
app.static('/js/vendor/', './static/js/vendor/')
app.static('/css/', './static/css')
app.static('/js', './static/js/')
app.static('/images', './static/images')
app.static('/partials', './static/partials')
app.static('/templates', './static/templates')
app.static('/favicon.ico', './static/images/favicon.ico')

app.add_route(UserView.as_view(), '/api/user/')
app.add_route(UserView.as_view(), '/api/user/<id_name>')
app.add_route(AuthenticateView.as_view(), '/api/authenticate')

app.add_route(QuestionView.as_view(), '/api/question/')
app.add_route(QuestionView.as_view(), '/api/question/<qid:int>')

app.add_route(LessonView.as_view(), '/api/lessons')
app.add_route(LessonView.as_view(), '/api/lessons/<qid:int>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
