# !/usr/bin/python3.5
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import HTTPModelClassView

from models import LiveQuiz
from models import LiveQuizQuestion
from models import Quiz
from models import QuizQuestions
from models import Users

# noinspection PyBroadException
class QuizManageView(HTTPModelClassView):
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
class LiveQuizManageView(HTTPModelClassView):
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