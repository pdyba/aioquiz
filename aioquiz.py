# !/usr/bin/python3.5
from uuid import uuid4

from sanic import Sanic
from sanic.response import json
from sanic.views import HTTPMethodView

from models import Quiz
from utils import logger

current_sessions = {}
answares = {}

main_quiz = Quiz()


class QuestionView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            logger.warn(req)
            session_id = req.get('session_id')
            qid = req.get('qid') + 1
            quiz = await main_quiz.get(qid)
            answares.setdefault(qid, []).append(req.get('answare'))
            resp = {
                'session_id': session_id,
                'question': quiz.question,
                'qtype': quiz.qtype,
                'answares': quiz.answares,
                'qid': qid
            }
            return json(resp)
        except:
            logger.exception('err game.post')
            return json({})

    async def get(self, _):
        try:
            session_id = str(uuid4())
            resp = {
                'session_id': session_id,
                'question': 'Whats Your name',
                'qtype': 'plain',
                'answares': [],
                'qid': 0
            }
            return json(resp)
        except:
            logger.exception('err game.get')
            return json({})


class Summary(HTTPMethodView):
    def get(self, request):
        pass

    def post(self, request):
        pass


app = Sanic()

app.static('/', './static/index.html')
app.static('/js/vendor/', './static/js/vendor/')
app.static('/css/', './static/css')
app.static('/js', './static/js/')
app.static('/images', './static/images')

app.add_route(QuestionView.as_view(), '/api/quiz')
app.add_route(Summary.as_view(), '/api/summary')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
