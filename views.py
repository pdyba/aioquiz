# !/usr/bin/python3.5
from json import loads as jloads
from sanic.response import json
from sanic.views import HTTPMethodView

from orm import DoesNoteExists
from models import Quiz
from models import Question
from models import Users
from models import LiveQuiz
from models import Lesson
import logging


_users = {}


async def format_dict_to_columns(adict):
    return [[a, adict[a]] for a in adict]


async def get_user_name(uid):
    if uid not in _users:
        user = await Users.get_by_id(uid)
        _users[uid] = '{} {}'.format(user.name, user.surname)
    return _users[uid]


# noinspection PyBroadException
class QuestionView(HTTPMethodView):
    _users = {}

    async def post(self, request):
        try:
            req = request.json
            user = await Users.get_first('email', req['creator'])
            req['creator'] = user.id
            question = Question(**req)
            await question.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err question.post')
            return json({})

    async def put(self, request, qid):
        try:
            req = request.json
            user = await Users.get_first('email', req['reviewer'])
            question = await Question.get_by_id(qid)
            question.reviewer = user.id
            question.active = req['accept']
            await question.update()
            return json({'success': True}, status=200)
        except:
            logging.exception('err question.update')
            return json({})

    async def get(self, request, qid=0):
        to_review = {
            'False': False,
            'false': False,
            'True': True,
            'true': True,
            None: None
        }[request.args.get('review', None)]
        
        if qid:
            question = await Question.get_by_id( qid)
            return json(await question.to_dict())
        elif to_review:
            questions = await Question.get_by_field_value(
                field='reviewer',
                value=0
            )
        elif not to_review:
            questions = await Question.get_by_field_value(
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


# noinspection PyBroadException
class UserView(HTTPMethodView):
    async def get(self, _, id_name=None):
        if isinstance(id_name, int):
            user = await Users.get_by_id(id_name)
            user = await user.to_dict()
        elif isinstance(id_name, str):
            user = await Users.get_first('email', id_name)
            user = await user.to_dict()
        else:
            users = await Users.get_all()
            user = []
            for u in users:
                user.append(await u.to_dict())
        return json(user)

    async def put(self, _, id_name=None):
        return json({'success': True}, status=200)

    async def post(self, request):
        try:
            req = request.json
            user = Users(**req)
            uid = await user.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err user.post')
            return json({})

    async def delete(self, _, uid):
        pass


# noinspection PyBroadException
class QuizManageView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            req['questions'] = [int(q) for q in req['questions']]
            user = await Users.get_first('email', req['creator'])
            req['creator'] = user.id
            quiz = Quiz(**req)
            await quiz.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err quiz_manage.post')
            return json({})


# noinspection PyBroadException
class QuizView(HTTPMethodView):
    _users = {}

    async def post(self, request):
        try:
            req = request.json
            user = await Users.get_by_id(req['uid'])
            quiz = await Quiz.get_by_id(req['quiz_id'])
            next_question = quiz.get_next_question(req['qid'])
        except:
            logging.exception('err quiz.post')
            return json({})

    async def get(self, _, qid=0):
        if qid:
            quiz = await Quiz.get_by_id(qid)
            quiz = await quiz.to_dict()
            quiz['questions'] = jloads(quiz['questions'])
            return json(quiz)
        else:
            quiz = await Quiz.get_all()
            resp = []
            for q in quiz:
                q = await q.to_dict()
                q['creator'] = await get_user_name(q['creator'])
                q['amount'] = len(jloads(q['questions']))
                resp.append(q)
            return json(resp)


# noinspection PyBroadException
class LiveQuizView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            req['questions'] = [int(q) for q in req['questions']]
            user = await Users.get_first('email', req['creator'])
            req['creator'] = user.id
            question = LiveQuiz(**req)
            await question.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err live_quiz.post')
            return json({})

    async def put(self, request, qid=0):
        try:
            req = request.json
            lg = await LiveQuiz.get_by_id(qid)
            if lg.answares:
                lg.answares = jloads(lg.answares)
            else:
                lg.answares = {}
            answare = req['answare']
            quest_id = str(req['question'])
            lg.answares.setdefault(quest_id, {})
            lg.answares[quest_id].setdefault(answare, 0)
            lg.answares[quest_id][answare] += 1
            await lg.update()
            return json({'success': True}, status=200)
        except:
            logging.exception('err live_quiz.post')
            return json({})

    async def get(self, _, qid=0):
        if qid:
            quiz = await LiveQuiz.get_by_id(qid)
            quiz = await quiz.to_dict()
            quiz['questions'] = jloads(quiz['questions'])
            if quiz['answares']:
                quiz['answares'] = jloads(quiz['answares'])
            else:
                quiz['answares'] = ''
            return json(quiz)
        else:
            quiz = await LiveQuiz.get_all()
            resp = []
            for q in quiz:
                q = await q.to_dict()
                q['creator'] = await get_user_name(q['creator'])
                q['amount'] = len(jloads(q['questions']))
                resp.append(q)
            return json(resp)


# noinspection PyBroadException
class LessonView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            user = await Users.get_first('email', req['creator'])
            req['creator'] = user.id
            lesson = Lesson(**req)
            await lesson.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err lesson.post')
            return json({'message': 'error creating'})

    async def get(self, _, lid=None):
        
        if lid:
            lesson = await Lesson.get_by_id(lid)
            return json(await lesson.to_dict())
        else:
            lessons = await Lesson.get_all()
            resp = []
            for l in lessons:
                resp.append(await l.to_dict())
            return json(resp)


# noinspection PyBroadException
class AuthenticateView(HTTPMethodView):
    user_error = {'success': False, 'msg': 'Wrong user name or password'}

    async def post(self, request):
        try:
            req = request.json
            user = await Users.get_first(
                'email',
                req.get('email', '')
            )
            if not user:
                print('n found')
                return json({'msg': 'User not found'}, status=404)
            if not user.active:
                print('n act')
                return json({'msg': 'User not active'}, status=404)
            if req.get('password', '') == user.password:
                return json(
                    {
                        'success': True,
                        'admin': user.admin,
                        'mentor': user.mentor,
                        'id': user.id
                    },
                    status=200
                )
            else:
                print(req.get('password', ''))
                print(user.password)
                return json(self.user_error, status=200)
        except DoesNoteExists:
            return json(self.user_error, status=200)
        except:
            logging.exception('err authentication.post')
        return json({'msg': 'internal error'}, status=500)
