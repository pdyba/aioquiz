#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from views.utils import get_user_name
from views.utils import MCV


# noinspection PyBroadException, PyProtectedMember
class CommonTestBase(MCV):
    _cls = None
    _cls_answer = None
    _urls = []
    quiz_finished = json({'msg': 'Quiz has finished or is no longer active', 'success': False})

    async def post(self, qid=0):
        try:
            quiz = await self._cls.get(qid)
            if not quiz.active and self.current_user.is_only_attendee():
                return self.quiz_finished
            req = self.req.json
            uid = self.current_user.id
            qa = self._cls_answer(**{
                self._cls_answer._fk_col: qid,
                'question': req['question'],
                'answer': req['answer'],
                'users': uid,
            })
            await qa.create()
            await quiz.update_status(uid)
            return json({'msg': 'Answer saved'})
        except:
            logging.exception('err live_quiz.post')
            return json({'msg': 'something went wrong'}, status=500)

    async def put(self, qid=0):
        try:
            quiz = await self._cls.get(qid)
            if not quiz.active and self.current_user.is_only_attendee():
                return self.quiz_finished
            req = self.req.json
            cond = {
                self._cls_answer._fk_col: qid,
                'question': req['question'],
                'users': self.current_user.id,
            }
            qa = await self._cls_answer.get_first_by_many_field_value(**cond)
            qa.answer = req['answer']
            await qa.update(**cond)
            return json({'msg': 'Answer Updated'})
        except:
            logging.exception('err live_quiz.post')
            return json({'msg': 'something went wrong'}, status=500)

    async def patch(self, qid=0):
        try:
            uid = self.current_user.id
            quiz = await self._cls.get(qid)
            await quiz.update_status(uid, new_status='Submitted', add=0)
            return json({'msg': 'Submitted successfully', 'success': True})
        except:
            logging.exception('err live_quiz.post')
            return json({'msg': 'something went wrong', 'success': False}, status=500)

    async def get(self, qid=0):
        if qid:
            quiz = await self._cls.get(qid)
            if not quiz.active and self.current_user.is_only_attendee():
                return self.quiz_finished
            resp = await quiz.to_dict()
            question = await quiz.get_question(uid=self.current_user.id)
            resp['all_questions'] = question
            status = await quiz.get_status(self.current_user.id)
            resp['status'] = status.status
            resp['progress'] = status.progress
            return json(resp)
        else:
            quizzes = await self._cls.get_all()
            resp = []
            for quiz in quizzes:
                status = await quiz.get_status(self.current_user.id)
                if not quiz.active and status.status != 'Graded' and self.current_user.is_only_attendee():
                    continue
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                q['status'] = status.status
                q['progress'] = status.progress
                q['score'] = status.score
                if status.status == 'NotStarted' and not quiz.active and self.current_user.is_only_attendee():
                    continue
                resp.append(q)
            return json(resp)
