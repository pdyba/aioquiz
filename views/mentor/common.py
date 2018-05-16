#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView


# noinspection PyBroadException, PyProtectedMember
class CommonMentorTestBase(HTTPModelClassView):
    _cls = None
    _urls = []

    @user_required('mentor')
    async def post(self, request, current_user):
        try:
            req = request.json
            req['users'] = current_user.id
        except:
            logging.exception('err CommonMentorTestBase.post')
            return json({}, status=500)

    @user_required('mentor')
    async def put(self, request, current_user, tid=0):
        try:
            req = request.json
            test = await self._cls.get_by_id(req['id'])
        except:
            logging.exception('err CommonMentorTestBase.put')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required('mentor')
    async def get(self, _, current_user, tid=0):
        if tid:
            quiz = await self._cls.get_by_id(tid)
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
