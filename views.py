# !/usr/bin/python3.5
from json import loads as jloads

from aiopg.sa import create_engine
from sanic.response import json
from sanic.views import HTTPMethodView
from psycopg2 import OperationalError

from db_models import DoesNoteExists
from models import Quiz
from models import Question
from models import Users
from models import LiveQuiz
from models import Lesson
from utils import logger

psql_cfg = {
    'user': 'aiopg',
    'database': 'postgres',
    'host': '127.0.0.1',
    'password': 'aiopg'
}

_users = {}


async def format_dict_to_columns(adict):
    return [[a, adict[a]] for a in adict]


async def get_user_name(uid):
    if uid not in _users:
        async with create_engine(**psql_cfg) as engine:
            user = await Users.get_by_id(engine, uid)
            _users[uid] = '{} {}'.format(user.name, user.surname)
    return _users[uid]


class QuestionView(HTTPMethodView):
    _users = {}

    async def post(self, request):
        try:
            req = request.json
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email', req['creator'])
                req['creator'] = user.id
                question = Question(**req)
                await question.create(engine)
            return json({'success': True}, status=200)
        except:
            logger.exception('err question.post')
            return json({})

    async def put(self, request, qid):
        try:
            req = request.json
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email', req['reviewer'])
                question = await Question.get_by_id(engine, qid)
                question.reviewer = user.id
                question.active = req['accept']
                await question.update(engine)
            return json({'success': True}, status=200)
        except:
            logger.exception('err question.update')
            return json({})

    async def get(self, request, qid=0):
        to_review = {
            'False': False,
            'false': False,
            'True': True,
            'true': True,
            None: None
        }[request.args.get('review', None)]
        async with create_engine(**psql_cfg) as engine:
            if qid:
                question = await Question.get_by_id(engine, qid)
                return json(await question.to_dict())
            elif to_review:
                questions = await Question.get_by_field_value(
                    engine,
                    field='reviewer',
                    value=0
                )
            elif not to_review:
                questions = await Question.get_by_field_value(
                    engine,
                    field='active',
                    value=True
                )
            resp = []
            for q in questions:
                data = await q.to_dict()
                if to_review:
                    data['creator'] = await get_user_name(data['creator'])
                resp.append(data)
            return json(resp)


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
                return json({'success': True}, status=200)
        except:
            logger.exception('err user.post')
            return json({})

    async def put(self, _, uid):
        pass

    async def delete(self, _, uid):
        pass


class QuizManageView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            req['questions'] = [int(q) for q in req['questions']]
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email', req['creator'])
                req['creator'] = user.id
                quiz = Quiz(**req)
                await quiz.create(engine)
            return json({'success': True}, status=200)
        except:
            logger.exception('err quiz_manage.post')
            return json({})


class QuizView(HTTPMethodView):
    _users = {}

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
            if qid:
                quiz = await Quiz.get_by_id(engine, qid)
                return json(await quiz.to_dict())
            else:
                quiz = await Quiz.get_all(engine)
                resp = []
                for q in quiz:
                    q = await q.to_dict()
                    q['creator'] = await get_user_name(q['creator'])
                    q['amount'] = len(jloads(q['questions']))
                    resp.append(q)
                return json(resp)


class LiveQuizView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            req['questions'] = [int(q) for q in req['questions']]
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email', req['creator'])
                req['creator'] = user.id
                question = LiveQuiz(**req)
                await question.create(engine)
            return json({'success': True}, status=200)
        except:
            logger.exception('err live_quiz.post')
            return json({})

    async def put(self, request, qid=0):
        try:
            req = request.json
            async with create_engine(**psql_cfg) as engine:
                lg = await LiveQuiz.get_by_id(engine, qid)
                if lg.answares:
                    lg.answares = jloads(lg.answares)
                else:
                    lg.answares = {}
                answare = req['answare']
                quest_id = str(req['question'])
                lg.answares.setdefault(quest_id, {})
                lg.answares[quest_id].setdefault(answare, 0)
                lg.answares[quest_id][answare] += 1
                await lg.update(engine)
            return json({'success': True}, status=200)
        except:
            logger.exception('err live_quiz.post')
            return json({})

    async def get(self, _, qid=0):
        async with create_engine(**psql_cfg) as engine:
            if qid:
                quiz = await LiveQuiz.get_by_id(engine, qid)
                quiz = await quiz.to_dict()
                quiz['questions'] = jloads(quiz['questions'])
                if quiz['answares']:
                    quiz['answares'] = jloads(quiz['answares'])
                else:
                    quiz['answares'] = ''
                return json(quiz)
            else:
                quiz = await LiveQuiz.get_all(engine)
                resp = []
                for q in quiz:
                    q = await q.to_dict()
                    q['creator'] = await get_user_name(q['creator'])
                    q['amount'] = len(jloads(q['questions']))
                    resp.append(q)
                return json(resp)


class LessonView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email', req['creator'])
                req['creator'] = user.id
                lesson = Lesson(**req)
                await lesson.create(engine)
            return json({'success': True}, status=200)
        except:
            logger.exception('err lesson.post')
            return json({'message': 'error creating'})

    async def get(self, _, lid=None):
        async with create_engine(**psql_cfg) as engine:
            if lid:
                lesson = await Lesson.get_by_id(engine, lid)
                return json(await lesson.to_dict())
            else:
                lessons = await Lesson.get_all(engine)
                resp = []
                for l in lessons:
                    resp.append(await l.to_dict())
                return json(resp)


class AuthenticateView(HTTPMethodView):
    user_error = {'success': False, 'msg': 'Wrong user name or password'}

    async def post(self, request):
        try:
            req = request.json
            async with create_engine(**psql_cfg) as engine:
                user = await Users.get_first(engine, 'email',
                                             req.get('email', ''))
            if user and user.active and req.get('password',
                                                '') == user.password:
                return json(
                    {
                        'success': True,
                        'admin': user.admin,
                        'moderator': user.moderator,
                        'id': user.id
                    },
                    status=200
                )
            else:
                return json(self.user_error, status=200)
        except DoesNoteExists:
            return json(self.user_error, status=200)
        except OperationalError:
            logger.error('Could not connect to DB')
        except:
            logger.exception('err authentication.post')
        return json({'msg': 'internal error'}, status=500)
