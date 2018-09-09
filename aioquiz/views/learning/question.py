#!/usr/bin/env python3.5
# encoding: utf-8
import logging
from json import dumps as jdumps

from sanic.response import json

from views.utils import get_user_name
from views.utils import MCV

from models import Question
from models import Users

from utils import safe_del_key


# noinspection PyBroadException
class QuestionView(MCV):
    _cls = Question
    _urls = ['/api/question', '/api/question/<qid:int>']

    async def post(self):
        try:
            req = self.req.json
            if req['qtype'] == 'abcd':
                req['answers'] = jdumps(
                    [req['ans_a'], req['ans_b'], req['ans_c'], req['ans_d']]
                )
                req = safe_del_key(req, ['ans_a', 'ans_b', 'ans_c', 'ans_d'])
            question = Question(**req)
            await question.create()
            return json({'success': True})
        except:
            logging.exception('err question.post')
            return json({}, status=500)

    async def put(self, qid=0):
        try:
            req = self.req.json
            user = await Users.get_first('email', req['reviewer'])
            question = await Question.get_by_id(qid)
            question.reviewer = user.id
            question.active = req['accept']
            await question.update()
            return json({'success': True})
        except:
            logging.exception('err question.update')
            return json({}, status=500)

    async def get(self, qid=0):
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
