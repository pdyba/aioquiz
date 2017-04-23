# !/usr/bin/python3.5
from aiopg.sa import create_engine
from sanic.response import json
from sanic.views import HTTPMethodView

from db_models import UserDoesNoteExists
from models import Quiz
from models import Question
from models import Users
from models import LiveQuiz
from models import Lesson
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
    async def get(self, _, id_name=None):
        async with create_engine(**psql_cfg) as engine:
            if isinstance(id_name, int):
                user = await Users.get_by_id(engine, id_name)
                user = await user.to_dict()
            elif isinstance(id_name, str):
                user = await Users.get_first(engine, 'email', id_name)
                user = await user.to_dict()
            else:
                users = await Users.get_all(engine)
                user = []
                for u in users:
                    user.append(await u.to_dict())
        return json(user)

    async def post(self, request):
        try:
            async with create_engine(**psql_cfg) as engine:
                req = request.json
                user = Users(**req)
                uid = await user.create(engine)
                return json({'id': uid}, status=302)
        except:
            logger.exception('err user.post')
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
            logger.exception('err quiz.post')
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
            logger.exception('err live_quiz.post')
            return json({})

    async def get(self, _, qid=0):
        async with create_engine(**psql_cfg) as engine:
            if qid:
                quiz = await LiveQuiz.get_by_id(engine, qid)
            else:
                quiz = await LiveQuiz.get_all(engine)
        return json(await quiz.to_dict())


class LessonView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            lesson = Lesson(**req)
            async with create_engine(**psql_cfg) as engine:
                qid = await lesson.create(engine)
            return json({'id': qid}, status=302)
        except:
            logger.exception('err lesson.post')
            return json({})

    async def get(self, _, qid):
        async with create_engine(**psql_cfg) as engine:
            question = await Question.get_by_id(engine, qid)
            return json(await question.to_dict())


class AuthenticateView(HTTPMethodView):
    user_error = {'success': False, 'msg': 'Wrong user name or password'}
    async def post(self, request):
        try:
            req = request.json
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email', req.get('email', ''))
            if user and user.active and req.get('password', '') == user.password:
                return json({'success': True, 'admin': user.admin, 'moderator': user.moderator}, status=200)
            else:
                return json(self.user_error, status=200)
        except UserDoesNoteExists:
            return json(self.user_error, status=200)
        except:
            logger.exception('err authentication.post')
            return json({'msg': 'internal error'}, status=500)