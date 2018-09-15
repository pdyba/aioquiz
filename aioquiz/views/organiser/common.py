#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import get_user_name
from views.utils import OrganiserMCV


# noinspection PyBroadException, PyProtectedMember
class CommonOrganiserTestBase(OrganiserMCV):
    _cls = None
    _urls = []

    async def post(self):
        try:
            req = self.req.json
            req['users'] = self.current_user.id
            questions = [q for q in req['all_questions']]
            del req['all_questions']
            test = self._cls(**req)
            await test.create()
            for i, question in enumerate(questions):
                await test.add_question(question['question_details']['id'], question.get('question_order', i + 1))
            return json({'success': True, 'msg': '{} created'.format(self._cls._name)})
        except:
            logging.exception('err CommonOrganiserTestView.post')
            return json({}, status=500)

    async def put(self, tid=0):
        try:
            req = self.req.json
            test = await self._cls.get(req['id'])
            new_questions = [q for q in req['all_questions']]
            if req['active'] in ('None', None):
                req['active'] = False
            del req['all_questions']
            await test.update_from_dict(req)
            await test.delete_old_questions()
            for i, question in enumerate(new_questions):
                await test.add_question(question['question_details']['id'], question.get('question_order', i + 1))
            return json({'success': True, 'msg': '{} updated'.format(self._cls._name.capitalize())})
        except:
            logging.exception('err CommonOrganiserTestBase.put')
            return json({'msg': 'something went wrong'}, status=500)

    async def get(self, tid=0):
        if tid:
            try:
                quiz = await self._cls.get(tid)
                resp = await quiz.to_dict()
                questions = await quiz.get_question()
                resp['all_questions'] = questions
            except IndexError:
                if tid == 1:
                    resp = {}
                else:
                    raise
            unused_questions = await self._cls.get_all_available_questions()
            resp['unused_questions'] = unused_questions
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


class CommonActiveateTestBase(OrganiserMCV):
    _cls = None
    _urls = []
    access_level_default = 'organiser'
    
    async def post(self):
        req = self.req.json
        test = await self._cls.get(req['id'])
        if test:
            test.active = req['active']
            await test.update()
            return json({
                'success': True,
                'msg': '{} is {} mentor'.format(test.id, 'now active' if req['active'] else 'NOT')
            })
        return json({'success': False, 'msg': 'wrong test id'})