# !/usr/bin/python3.5
from json import dumps as jdumps
import logging
from uuid import uuid4

from sanic.response import json
from sanic.views import HTTPMethodView

from orm import DoesNoteExists
from models import Quiz
from models import Question
from models import Users
from models import LiveQuiz
from models import Lesson
from models import QuizQuestions
from models import LiveQuizQuestion
from models import LiveQuizAnsware
from models import QuestionAnsware
from models import LessonStatus
from models import LessonStatus



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
    async def post(self, request):
        try:
            req = request.json
            if req['qtype'] == 'abcd':
                req['answares'] = jdumps([req['ans_a'], req['ans_b'], req['ans_c'], req['ans_d']])
                del req['ans_a']
                del req['ans_b']
                del req['ans_c']
                del req['ans_d']
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
        if qid:
            question = await Question.get_by_id( qid)
            return json(await question.to_dict())
        questions = await Question.get_all()
        resp = []
        for q in questions:
            data = await q.to_dict()
            data['creator'] = await get_user_name(data['users'])
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
            user = await Users.get_first('email', req['creator'])
            req['users'] = user.id
            questions = [int(q) for q in req['questions']]
            del req['questions']
            quiz = Quiz(**req)
            quiz_id = await quiz.create()
            for i, question in enumerate(questions):
                qq = QuizQuestions(quiz=quiz_id, question=question, question_order=i)
                await qq.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err quiz_manage.post')
            return json({})


# noinspection PyBroadException
class QuizView(HTTPMethodView):
    async def post(self, request, qid=0):
        try:
            req = request.json
            qa = QuestionAnsware(
                users=req['user_id'],
                question=req['question'],
                answare=req['answare'],
            )
            await qa.update_or_create('users', 'question')
            quiz = await Quiz.get_by_id(qid)
            question = await quiz.get_question(req['current_question'] + 1)
            if isinstance(question, dict):
                return json(question)
            q = await question.to_dict()
            return json(q)
        except:
            logging.exception('err quiz.post')
            return json({})

    async def get(self, _, qid=0):
        if qid:
            quiz = await Quiz.get_by_id(qid)
            question = await quiz.get_question()
            q = await question.to_dict()
            q['quiz_title'] = quiz.title
            return json(q)
        else:
            quizes = await Quiz.get_all()
            resp = []
            for quiz in quizes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                resp.append(q)
            return json(resp)


# noinspection PyBroadException
class LiveQuizManageView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            user = await Users.get_first('email', req['creator'])
            req['users'] = user.id
            questions = [int(q) for q in req['questions']]
            del req['questions']
            quiz = LiveQuiz(**req)
            quiz_id = await quiz.create()
            for i, question in enumerate(questions):
                lqq = LiveQuizQuestion(
                    live_quiz=quiz_id,
                    question=question,
                    question_order=i
                )
                await lqq.create()
            return json({'success': True}, status=200)
        except:
            logging.exception('err quiz_manage.post')
            return json({})


# noinspection PyBroadException
class LiveQuizView(HTTPMethodView):
    async def post(self, request, qid=0):
        try:
            req = request.json
            qa = LiveQuizAnsware(
                live_quiz=qid,
                question=req['question'],
                answare=req['answare'],
            )
            await qa.create()
            live_quiz = await LiveQuiz.get_by_id(qid)
            question = await live_quiz.get_question(req['current_question'] + 1)
            if isinstance(question, dict):
                return json(question)
            q = await question.to_dict()
            return json(q)
        except:
            logging.exception('err live_quiz.post')
            return json({})

    async def get(self, _, qid=0):
        if qid:
            quiz = await LiveQuiz.get_by_id(qid)
            question = await quiz.get_question()
            q = await question.to_dict()
            q['quiz_title'] = quiz.title
            return json(q)
        else:
            quizes = await LiveQuiz.get_all()
            resp = []
            for quiz in quizes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
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
                return json({'msg': 'User not found'}, status=404)
            if not user.active:
                return json({'msg': 'User not active'}, status=404)
            if req.get('password', '') == user.password:
                user.session_uuid = str(uuid4()).replace('-', '')
                await user.update()
                return json(
                    {
                        'success': True,
                        'admin': user.admin,
                        'mentor': user.mentor,
                        'id': user.id,
                        'session_uuid': user.session_uuid
                    },
                    status=200
                )
            else:
                return json(self.user_error, status=200)
        except DoesNoteExists:
            return json(self.user_error, status=200)
        except:
            logging.exception('err authentication.post')
        return json({'msg': 'internal error'}, status=500)


class LogOutView(HTTPMethodView):
    async def post(self, request):
        req = request.json
        user = await Users.get_user_by_session_uuid(req.session_uid)
        if user:
            user.session_uuid = ''
            await user.update()
            return json({'success': True})
        return json({'success': False}, status=403)
