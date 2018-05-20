#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView


# noinspection PyBroadException, PyProtectedMember
class CommonTestBase(HTTPModelClassView):
    _cls = None
    _cls_answer = None
    _urls = []

    @user_required()
    async def post(self, request, current_user, qid=0):
        try:
            req = request.json
            uid = current_user.id
            qa = self._cls_answer(**{
                self._cls_answer._fk_col: qid,
                'question': req['question'],
                'answer': req['answer'],
                'users': uid,
            })
            await qa.create()
            quiz = await self._cls.get_by_id(qid)
            await quiz.update_status(uid)
            return json({'msg': 'Answer saved'})
        except:
            logging.exception('err live_quiz.post')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required()
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

    @user_required()
    async def patch(self, request, current_user, qid=0):
        try:
            uid = current_user.id
            quiz = await self._cls.get_by_id(qid)
            await quiz.update_status(uid, new_status='Submitted', add=0)
            return json({'msg': 'Submitted successfully'})
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
                if status.status == 'NotStarted' and not quiz.active and current_user.is_only_attendee():
                    continue
                resp.append(q)
            return json(resp)
