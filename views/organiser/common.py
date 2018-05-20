#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView


# noinspection PyBroadException, PyProtectedMember
class CommonOrganiserTestBase(HTTPModelClassView):
    _cls = None
    _urls = []

    @user_required('organiser')
    async def post(self, request, current_user):
        try:
            req = request.json
            req['users'] = current_user.id
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

    @user_required('organiser')
    async def put(self, request, current_user, tid=0):
        try:
            req = request.json
            test = await self._cls.get_by_id(req['id'])
            new_questions = [q for q in req['all_questions']]
            if req['active'] in ('None', None):
                req['active'] = False
            del req['all_questions']
            await test.update_from_dict(req)
            await test.delete_old_questions()
            print(len(new_questions))
            for i, question in enumerate(new_questions):
                await test.add_question(question['question_details']['id'], question.get('question_order', i + 1))
            return json({'success': True, 'msg': '{} updated'.format(self._cls._name.capitalize())})
        except:
            logging.exception('err CommonOrganiserTestBase.put')
            return json({'msg': 'something went wrong'}, status=500)

    @user_required('organiser')
    async def get(self, _, current_user, tid=0):
        if tid:
            try:
                quiz = await self._cls.get_by_id(tid)
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


class CommonActiveateTestBase(HTTPModelClassView):
    _cls = None
    _urls = []

    @user_required('organiser')
    async def post(self, request, current_user):
        req = request.json
        test = await self._cls.get_by_id(req['id'])
        if test:
            test.active = req['active']
            await test.update()
            return json({
                'success': True,
                'msg': '{} is {} mentor'.format(test.id, 'now active' if req['active'] else 'NOT')
            })
        return json({'success': False, 'msg': 'wrong test id'})