# !/usr/bin/python3.5
from datetime import datetime
from json import dump
from uuid import uuid4

from sanic import Sanic
from sanic.response import json
from sanic.views import HTTPMethodView

from models import Quiz
from utils import logger

current_sessions = {}
answares = {}
main_quiz = Quiz()


async def format_dict_to_columns(adict):
    return [[a, adict[a]] for a in adict]


class QuestionView(HTTPMethodView):
    async def get_question(self, qid, session_id):
        quiz = await main_quiz.get(qid)
        return {
            'session_id': session_id,
            'question': quiz.question,
            'qtype': quiz.qtype,
            'answares': quiz.answares,
            'qid': qid,
            'img': quiz.img,
        }

    async def post(self, request):
        try:
            req = request.json
            session_id = req.get('session_id')
            qid = req.get('qid')
            answare = req.get('answare')
            answares.setdefault(qid, {}).setdefault(answare, 0)
            answares[qid][answare] += 1
            return json(await self.get_question(qid + 1, session_id))
        except:
            logger.exception('err game.post')
            return json({})

    async def get(self, _):
        try:
            session_id = str(uuid4())
            return json(await self.get_question(0, session_id))
        except:
            logger.exception('err game.get')
            return json({})


class Stats(HTTPMethodView):
    async def get(self, _, qid):
        return json({
            'max': sum(answares.get(0, {0: 0}).values()),
            'done': sum(answares.get(qid, {0: 0}).values()),
        })


class Summary(HTTPMethodView):
    async def get_question_and_answares(self, qid, session_id):
        quiz = await main_quiz.get(qid)
        columns = await format_dict_to_columns(answares.get(qid, {}))
        if quiz.qtype == 'end':
            await self.save()
        return {
            'session_id': session_id,
            'question': quiz.question,
            'qtype': quiz.qtype,
            'columns': columns,
            'qid': qid,
            'img': quiz.img,
        }

    @staticmethod
    async def save():
        filename = str(datetime.utcnow())
        with open(filename, 'w') as file:
            dump(answares, file, indent=4)

    async def post(self, request):
        try:
            req = request.json
            session_id = req.get('session_id')
            qid = req.get('qid')
            return json(await self.get_question_and_answares(qid, session_id))
        except:
            logger.exception('err game.post')
            return json({})

    async def get(self, _):
        try:
            session_id = str(uuid4())
            qid = 0
            return json(await self.get_question_and_answares(qid, session_id))
        except:
            logger.exception('err game.post')
            return json({})


app = Sanic()

app.static('/', './static/index.html')
app.static('/sum', './static/summary.html')
app.static('/js/vendor/', './static/js/vendor/')
app.static('/css/', './static/css')
app.static('/js', './static/js/')
app.static('/images', './static/images')

app.add_route(QuestionView.as_view(), '/api/quiz')
app.add_route(Summary.as_view(), '/api/summary')
app.add_route(Stats.as_view(), '/api/stats/<qid:int>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
