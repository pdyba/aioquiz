#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import get_user_name
from views.utils import MentorMCV

from models import Question


# noinspection PyBroadException, PyProtectedMember
class CommonMentorTestBase(MentorMCV):
    _cls = None
    _urls = []

    async def get(self, tid=0):
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

    async def post(self, tid=0):
        if tid:
            test = await self._cls.get_by_id(tid)
            status = await test.close_test()
            status.update({
                'success': True,
                'msg': 'Max: {max} count: {count} mean: {mean}'.format(**status)
            })
            return json(status)
        else:
            return json({'msg': 'no test id'})


class CommonMentorQuestionGradeBase(MentorMCV):
    _cls = None
    _urls = []

    async def post(self, qid=0):
        try:
            req = self.req.json
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

    async def put(self, qid=0):
        try:
            req = self.req.json
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

    async def get(self, qid=0):
        if qid:
            question = await Question.get_by_id(qid)
            resp = await question.to_dict()
            resp['answers'] = await self._cls.get_by_anwers_to_grade_by_qid(qid)
            return json(resp)
        else:
            return json({'msg': 'no question id'})


class CommonMentorQuestionAutoGradeBase(MentorMCV):
    _cls = None
    _urls = []

    async def get(self, qid=0):
        if qid:
            question = await Question.get_by_id(qid)
            if question.qtype not in ('abcd', 'bool'):
                return json({
                    'msg': 'You cannot autograde questions types other than abcd and bool',
                    'success': False
                })
            answers = await self._cls.get_by_anwers_to_grade_by_qid(qid)
            positive = 0
            for ans in answers:
                score = 1 if ans['answer'].strip() == question.possible_answer.strip() else 0
                await self._cls.grade_answer_by_uid(
                    uid=ans['users'],
                    qid=qid,
                    score=score,
                    comment='autograded'
                )
                positive += score
            return json({
                'msg': 'Graded {} questions {} good {} wrong'.format(len(answers), positive, len(answers) - positive),
                'success': True
            })
        else:
            return json({'msg': 'no question id', 'success': False})
