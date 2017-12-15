# !/usr/bin/python3.5
import logging
from json import dumps as jdumps

from sanic.response import json
from sanic.views import HTTPMethodView

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClass

from models import LiveQuiz
from models import LiveQuizAnsware
from models import LiveQuizQuestion
from models import Question
from models import Quiz
from models import QuizQuestions
from models import QuestionAnsware
from models import Users


# noinspection PyBroadException
class QuestionView(HTTPMethodView):
    _cls = Users
    _urls = ['/api/question', '/api/question/<qid:int>']

    @user_required()
    async def post(self, request, current_user):
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
            return json({'success': True})
        except:
            logging.exception('err question.post')
            return json({}, status=500)

    @user_required()
    async def put(self, request, qid, current_user):
        try:
            req = request.json
            user = await Users.get_first('email', req['reviewer'])
            question = await Question.get_by_id(qid)
            question.reviewer = user.id
            question.active = req['accept']
            await question.update()
            return json({'success': True})
        except:
            logging.exception('err question.update')
            return json({}, status=500)

    @user_required()
    async def get(self, request, current_user, qid=0):
        if qid:
            question = await Question.get_by_id(qid)
            return json(await question.to_dict())
        questions = await Question.get_all()
        resp = []
        for q in questions:
            data = await q.to_dict()
            data['creator'] = await get_user_name(data['users'])
            resp.append(data)
        return json(resp, sort_keys=True)


# noinspection PyBroadException
class QuizManageView(HTTPMethodView):
    _cls = Users
    _urls = ['/api/quiz_manage', '/api/quiz_manage/<qid:int>']

    @user_required()
    async def post(self, request, current_user):
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
            return json({'success': True})
        except:
            logging.exception('err quiz_manage.post')
            return json({}, status=500)


# noinspection PyBroadException
class QuizView(HTTPMethodView):
    _cls = Users
    _urls = ['/api/quiz', '/api/quiz/<qid:int>']

    @user_required()
    async def post(self, request, current_user, qid=0):
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
            return json(q, sort_keys=True)
        except:
            logging.exception('err quiz.post')
            return json({}, status=500)

    @user_required()
    async def get(self, _, current_user, qid=0):
        if qid:
            quiz = await Quiz.get_by_id(qid)
            question = await quiz.get_question()
            q = await question.to_dict()
            q['quiz_title'] = quiz.title
            return json(q, sort_keys=True)
        else:
            quizes = await Quiz.get_all()
            resp = []
            for quiz in quizes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                resp.append(q)
            return json(resp, sort_keys=True)


# noinspection PyBroadException
class LiveQuizManageView(HTTPMethodView):
    _cls = Users
    _urls = ['/api/live_quiz_manage', '/api/live_quiz_manage/<qid:int>']

    @user_required()
    async def post(self, request, current_user):
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
            return json({'success': True})
        except:
            logging.exception('err quiz_manage.post')
            return json({}, status=500)


# noinspection PyBroadException
class LiveQuizView(HTTPMethodView):
    _cls = Users
    _urls = ['/api/live_quiz', '/api/live_quiz/<qid:int>']

    @user_required()
    async def post(self, request, current_user, qid=0):
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
            return json({}, status=500)

    @user_required()
    async def get(self, _, current_user, qid=0):
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
