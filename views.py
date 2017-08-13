# !/usr/bin/python3.5
from collections import defaultdict
from datetime import datetime
from json import dumps as jdumps
from functools import wraps
import logging
from uuid import uuid4

from sanic.response import json
from sanic.response import redirect
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
from models import UserReview

from utils import get_args
from utils import safe_del_key
from utils import hash_password
from utils import send_email

from config import REGEMAIL

_users = {}
_users_names = {}

NOTAUTHRISED = json({'error': 'not allowed'}, status=401)


def user_required(access_level=None):
    def decorator(func):
        @wraps(func)
        async def func_wrapper(self, *args, **kwargs):
            global _users
            authorization = args[0].headers.get('authorization')
            if not authorization:
                return NOTAUTHRISED
            user = _users.get(authorization) or await Users.get_user_by_session_uuid(authorization)
            _users[authorization] = user
            if not user:
                return NOTAUTHRISED
            if access_level:
                if not getattr(user, access_level):
                    return NOTAUTHRISED
            return await func(self, *args, **kwargs)
        return func_wrapper
    return decorator


async def get_user_name(uid):
    if uid not in _users_names:
        user = await Users.get_by_id(uid)
        _users_names[uid] = '{} {}'.format(user.name, user.surname)
    return _users_names[uid]

async def get_current_user(request):
    session_uid = request.headers.get('authorization')
    return _users.get(session_uid) or await Users.get_user_by_session_uuid(session_uid)


# noinspection PyBroadException
class QuestionView(HTTPMethodView):
    @user_required()
    async def post(self, request):
        try:
            req = request.json
            if req['qtype'] == 'abcd':
                req['answares'] = jdumps(
                    [req['ans_a'], req['ans_b'], req['ans_c'], req['ans_d']]
                )
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

    @user_required()
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

    @user_required()
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
    @user_required()
    async def get(self, request, id_name=None):
        if isinstance(id_name, int):
            user = await Users.get_by_id(id_name)
            user = await user.to_dict()
        elif isinstance(id_name, str):
            user = await Users.get_first('email', id_name)
            user = await user.to_dict()
        else:
            if request.args:
                users = await Users.get_by_many_field_value(**get_args(request.args))
            else:
                users = await Users.get_all()
            user = []
            for u in users:
                user.append(await u.to_dict())
        return json(user)

    @user_required()
    async def put(self, _, id_name=None):
        return json({'success': True}, status=200)

    async def post(self, request):
        try:
            req = request.json
            user = Users(**req)
            user.session_uuid = str(uuid4()).replace('-', '')
            uid = await user.create()
            await send_email(
                recipients=[user.email],
                text=REGEMAIL.TEXT.format(
                    acode=user.session_uuid,
                    uid=uid,
                    name=user.name,
                    server=request.host
                ),
                subject=REGEMAIL.SUBJECT,
            )
            return json({'success': True}, status=200)
        except:
            logging.exception('err user.post')
            return json({})

    @user_required('admin')
    async def delete(self, _, uid):
        pass


# noinspection PyBroadException
class QuizManageView(HTTPMethodView):
    @user_required()
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
    @user_required()
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

    @user_required()
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
    @user_required()
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
    @user_required()
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

    @user_required()
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
    @user_required()
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

    @user_required()
    async def get(self, _, lid=None):
        if lid:
            lesson = await Lesson.get_by_id(lid)
            return json(await lesson.to_dict())
        else:
            lessons = await Lesson.get_all()
            resp = []
            for l in lessons:
                resp.append(await l.to_dict())
            resp.sort(key=lambda a: a['id'])
            return json(resp)


# noinspection PyBroadException
class AuthenticateView(HTTPMethodView):
    user_error = json(
        {'success': False, 'msg': 'Wrong user name or password'},
        status=404
    )

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
            if hash_password(req.get('password', 'x')) == user.password:
                user.session_uuid = str(uuid4()).replace('-', '')
                user.last_login = datetime.utcnow()
                await user.update()
                return json(
                    {
                        'success': True,
                        'admin': user.admin,
                        'mentor': user.mentor,
                        'name': user.name,
                        'surname': user.surname,
                        'id': user.id,
                        'session_uuid': user.session_uuid
                    },
                    status=200
                )
            else:
                return self.user_error
        except DoesNoteExists:
            return self.user_error
        except:
            logging.exception('err authentication.post')
        return json({'msg': 'internal error'}, status=500)


class LogOutView(HTTPMethodView):
    @user_required()
    async def post(self, request):
        session_uid = request.headers.get('authorization')
        user = await Users.get_user_by_session_uuid(session_uid)
        if user:
            user.session_uuid = ''
            await user.update()
            return json({'success': True})
        return json({'success': False}, status=403)


class ReviewAttendeesView(HTTPMethodView):
    @user_required('organiser')
    async def get(self, request):
        allusers = await Users.get_by_many_field_value(
            admin=False,
            organiser=False
        )
        allreviews = await UserReview.get_all()
        reviews = defaultdict(dict)
        for rev in allreviews:
            reviews[rev.users][rev.reviewer] = {
                'score': rev.score,
                'name': await get_user_name(rev.reviewer)
            }
        users = []
        for u in allusers:
            ud = await u.to_dict(include_soft=True)
            ud.update({'reviews': reviews.get(u.id, {})})
            users.append(ud)
        return json(users)

    @user_required('organiser')
    async def post(self, request):
        current_user = await get_current_user(request)
        req = request.json
        req['reviewer'] = current_user.id
        ur = UserReview(**req)
        if not await ur.create():
            return json({'msg': 'already exists', 'error': True})
        all_ur = await UserReview.get_by_field_value('users', req['users'])
        user = await Users.get_by_id(req['users'])
        new_score = sum(u.score for u in all_ur) / (len(all_ur) or 1)
        user.score = new_score
        await user.update()
        return json({'success': True})

    @user_required('organiser')
    async def put(self, request):
        try:
            req = request.json
            user = await Users.get_by_id(req['users'])
            user.accepted = req['accept']
            await user.update()
            return json({'success': True})
        except:
            logging.exception('review_put')
            return json({'success': False})


class EmailView(HTTPMethodView):
    @user_required('organiser')
    async def get(self, request):
        recipients = []
        subject = '...'
        text = "..."
        resp = await send_email(
            recipients=recipients,
            text=text,
            subject=subject
        )
        return json({'success': resp})


class ActivationView(HTTPMethodView):
    async def get(self, request, uid, acode):
        user = await Users.get_by_id(uid)
        if user and user.session_uuid == acode:
            user.active = True
            await user.update()
            return redirect('/')
        return json({'success': False, 'reson': 'wrong token'})


class MakeOrganiserView(HTTPMethodView):
    @user_required('admin')
    async def post(self, request):
        req = request.json
        user = await Users.get_by_id(req['uid'])
        if user:
            user.organiser = req['organiser']
            await user.update()
            return json({'success': True})
        return json({'success': False, 'reson': 'wrong token'})