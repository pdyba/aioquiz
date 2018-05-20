#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView

from models import Question


# noinspection PyBroadException, PyProtectedMember
class CommonMentorTestBase(HTTPModelClassView):
    _cls = None
    _urls = []

    @user_required('mentor')
    async def get(self, _, current_user, tid=0):
        if tid:
            test = await self._cls.get_by_id(tid)
            resp = await test.to_dict()
            questions = await test.get_all_questions_to_grade(tid)
            resp['all_questions'] = questions
            return json(resp)
        else:
            tests = await self._cls.get_all()
            resp = []
            for test in tests:
                q = await test.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await test.get_question_amount()
                resp.append(q)
            return json(resp)


class CommonMentorQuestionGradeBase(HTTPModelClassView):
    _cls = None
    _urls = []

    @user_required('mentor')
    async def post(self, request, current_user, qid=0):
        try:
            req = request.json
            await self._cls.grade_answer_by_uid(
                uid=req['users'],
                qid=qid,
                score=req['score'],
                comment=req['comment']
            )
            return json({'success': True, 'msg': 'Answer Saved'})
        except:
            logging.exception('err CommonMentorTestBase.post')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required('mentor')
    async def put(self, request, current_user, qid=0):
        try:
            req = request.json
            await self._cls.grade_answer_by_uid(
                uid=req['users'],
                qid=qid,
                score=req['score'],
                comment=req['comment']
            )
            return json({'success': True, 'msg': 'Updated Saved'})
        except:
            logging.exception('err CommonMentorTestBase.put')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required('mentor')
    async def get(self, _, current_user, qid=0):
        if qid:
            question = await Question.get_by_id(qid)
            resp = await question.to_dict()
            resp['answers'] = await self._cls.get_by_anwares_to_grade_by_qid(qid)
            return json(resp)
        else:
            return json({'msg': 'no question id'})