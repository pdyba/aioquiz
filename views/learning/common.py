#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView


# noinspection PyBroadException
class CommonTestBase(HTTPModelClassView):
    _cls = None
    _cls_answer = None
    _urls = []

    @user_required()
    async def post(self, request, current_user, qid=0):
        try:
            req = request.json
            qa = self._cls_answer(**{
                self._cls_answer._name: qid,
                'question': req['question'],
                'answer': req['answer'],
            })
            await qa.create()
            return json({'msg': 'Answer saved'})
        except:
            logging.exception('err live_quiz.post')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required()
    async def get(self, _, current_user, qid=0):
        if qid:
            quiz = await self._cls.get_by_id(qid)
            resp = await quiz.to_dict()
            question = await quiz.get_question(uid=current_user.id)
            resp['all_questions'] = question
            status = await quiz.get_status(current_user.id)
            resp['status'] = status.status
            resp['progress'] = status.progress
            return json(resp)
        else:
            quizzes = await self._cls.get_all()
            resp = []
            for quiz in quizzes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                status = await quiz.get_status(current_user.id)
                q['status'] = status.status
                q['progress'] = status.progress
                resp.append(q)
            return json(resp)
