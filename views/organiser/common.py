#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView


# noinspection PyBroadException, PyProtectedMember
class CommonOrganiserTestView(HTTPModelClassView):
    _cls = None
    _urls = []

    @user_required('organiser')
    async def post(self, request, current_user):
        try:
            req = request.json
            req['users'] = current_user.id
            questions = [int(q) for q in req['questions']]
            del req['questions']
            test = self._cls(**req)
            await test.create()
            for i, question in enumerate(questions):
                test.add_question(question['qid'], question['order'])
            return json({'success': True})
        except:
            logging.exception('err CommonOrganiserTestView.post')
            return json({}, status=500)


    @user_required('organiser')
    async def put(self, request, current_user, qid=0):
        try:
            req = request.json
            cond = {
                self._cls_answer._fk_col: qid,
                'question': req['question'],
                'users': current_user.id,
            }
            qa = await self._cls_answer.get_first_by_many_field_value(**cond)
            qa.answer = req['answer']
            await qa.update(**cond)
            return json({'msg': 'Answer Updated'})
        except:
            logging.exception('err live_quiz.post')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required('organiser')
    async def get(self, _, current_user, qid=0):
        if qid:
            quiz = await self._cls.get_by_id(qid)
            resp = await quiz.to_dict()
            questions = await quiz.get_question()
            resp['all_questions'] = questions
            return json(resp)
        else:
            quizzes = await self._cls.get_all()
            resp = []
            for quiz in quizzes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                resp.append(q)
            return json(resp)

#
# # noinspection PyBroadException
# class LiveQuizManageView(HTTPModelClassView):
#     _cls = None
#     _urls = []
#
#
#
#     @user_required()
#     async def quiz_post(self, request, current_user):
#         try:
#             req = request.json
#             user = await Users.get_first('email', req['creator'])
#             req['users'] = user.id
#             questions = [int(q) for q in req['questions']]
#             del req['questions']
#             quiz = Quiz(**req)
#             quiz_id = await quiz.create()
#             for i, question in enumerate(questions):
#                 qq = QuizQuestions(quiz=quiz_id, question=question, question_order=i)
#                 await qq.create()
#             return json({'success': True})
#         except:
#             logging.exception('err quiz_manage.post')
#             return json({}, status=500)