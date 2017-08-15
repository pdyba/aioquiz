# !/usr/bin/python3.5
from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.exceptions import RequestTimeout
from sanic.exceptions import ServerError

from exception_handlers import handle_404s
from exception_handlers import handle_500s
from exception_handlers import handle_timeout
from views import ActivationView
from views import AuthenticateView
from views import EmailView
from views import ExercisesView
from views import LessonView
from views import LiveQuizManageView
from views import LiveQuizView
from views import MakeOrganiserView
from views import QuestionView
from views import QuizManageView
from views import QuizView
from views import ReviewAttendeesView
from views import UserView

app = Sanic()

app.static('/', './static/index.html')
app.static('/sum', './static/summary.html')
app.static('/js/vendor/', './static/js/vendor/')
app.static('/css/', './static/css')
app.static('/js', './static/js/')
app.static('/images', './static/images')
app.static('/partials', './static/partials')
app.static('/templates', './static/templates')
app.static('/lessons', './static/lessons')
app.static('/favicon.ico', './static/images/favicon.ico')

app.add_route(UserView.as_view(), '/api/user/')
app.add_route(UserView.as_view(), '/api/user/<id_name>')
app.add_route(AuthenticateView.as_view(), '/api/authenticate')

app.add_route(QuestionView.as_view(), '/api/question')
app.add_route(QuestionView.as_view(), '/api/question/<qid:int>')

app.add_route(LessonView.as_view(), '/api/lessons')
app.add_route(LessonView.as_view(), '/api/lessons/<qid:int>')

app.add_route(QuizView.as_view(), '/api/quiz')
app.add_route(QuizView.as_view(), '/api/quiz/<qid:int>')

app.add_route(QuizManageView.as_view(), '/api/quiz_manage')
app.add_route(QuizManageView.as_view(), '/api/quiz_manage/<qid:int>')

app.add_route(LiveQuizView.as_view(), '/api/live_quiz')
app.add_route(LiveQuizView.as_view(), '/api/live_quiz/<qid:int>')

app.add_route(LiveQuizManageView.as_view(), '/api/live_quiz_manage')
app.add_route(LiveQuizManageView.as_view(), '/api/live_quiz_manage/<qid:int>')

app.add_route(ReviewAttendeesView.as_view(), '/api/review_attendees')

app.add_route(EmailView.as_view(), '/api/email')

app.add_route(ActivationView.as_view(), '/api/activation/<uid:int>/<acode>')

app.add_route(MakeOrganiserView.as_view(), '/api/make_organiser')

app.add_route(ExercisesView.as_view(), '/api/exercise')
app.add_route(ExercisesView.as_view(), '/api/exercise/<lid:int>')

app.error_handler.add(ServerError, handle_500s)
app.error_handler.add(NotFound, handle_404s)
app.error_handler.add(RequestTimeout, handle_timeout)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
