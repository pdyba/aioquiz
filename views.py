# !/usr/bin/python3.5
from aiopg.sa import create_engine
from sanic.response import json
from sanic.views import HTTPMethodView

from models import Quiz
from models import Question
from models import Users
from models import LiveQuiz
from utils import logger

psql_cfg = {
    'user': 'aiopg',
    'database':  'postgres',
    'host': '127.0.0.1',
    'password': 'aiopg'
}


async def format_dict_to_columns(adict):
    return [[a, adict[a]] for a in adict]


class QuestionView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            question = Question(**req)
            async with create_engine(**psql_cfg) as engine:
                qid = await question.create(engine)
            return json({'id': qid}, status=302)
        except:
            logger.exception('err game.post')
            return json({})

    async def get(self, _, qid):
        async with create_engine(**psql_cfg) as engine:
            question = await Question.get_by_id(engine, qid)
            return json(await question.to_dict())


class UserView(HTTPMethodView):
    async def get(self, _, uid=0, name=''):
        async with create_engine(**psql_cfg) as engine:
            if uid:
                user = await Users.get_by_id(engine, uid)
            elif name:
                user = await Users.get_by_field_value(engine, 'name', name)
            else:
                user = await Users.get_all(engine)
        return json(await user.to_dict())

    async def post(self, request):
        try:
            async with create_engine(**psql_cfg) as engine:
                req = request.json
                user = Users(**req)
                uid = await user.create(engine)
                return json({'id': uid}, status=302)
        except:
            logger.exception('err game.post')
            return json({})

    async def put(self, _, uid):
        pass

    async def delete(self, _, uid):
        pass


class QuizView(HTTPMethodView):
    async def post(self, request):
        try:
            async with create_engine(**psql_cfg) as engine:
                req = request.json
                user = await Users.get_by_id(engine, req['uid'])
                quiz = await Quiz.get_by_id(engine, req['quiz_id'])
                next_question = quiz.get_next_question(req['qid'])
        except:
            logger.exception('err game.post')
            return json({})

    async def get(self, _, qid=0):
        async with create_engine(**psql_cfg) as engine:
            question = await Question.get_by_id(engine, qid)
        return json(await question.to_dict())


class LiveQuizView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            question = LiveQuiz(**req)
            async with create_engine(**psql_cfg) as engine:
                qid = await question.create(engine)
            return json({'id': qid}, status=302)
        except:
            logger.exception('err game.post')
            return json({})

    async def get(self, _, qid=0):
        async with create_engine(**psql_cfg) as engine:
            if qid:
                quiz = await LiveQuiz.get_by_id(engine, qid)
            else:
                quiz = await LiveQuiz.get_all(engine)
        return json(await quiz.to_dict())
