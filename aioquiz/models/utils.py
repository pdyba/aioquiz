# !/usr/bin/python3.5
from datetime import datetime
import logging

from config import DEFAULT_USER
from models.db import db, EnchancedModel
from orm import DoesNotExist


class Question(EnchancedModel):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answers = db.Column(db.CodeString, default='')
    possible_answer = db.Column(db.String, default='')
    qtype = db.Column(db.String, default='plain')
    img = db.Column(db.String, default='')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=DEFAULT_USER)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)


class CommonTestTemplate:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=DEFAULT_USER)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=False)

    _questions = None
    _status = None
    _answers = None

    async def get_question(self, uid=0, as_json=True):
        return await self._questions.get_all_for_test(self.id, uid=uid, answer_cls=self._answers, as_json=as_json)

    async def get_status(self, uid):
        try:
            await self.update_status(uid, add=0)
            return await self._status.get_first_by_many_field_value(
                **{self.id_field: self.id, 'user_id': uid}
            )
        except DoesNotExist:
            status = self._status(**{self.id_field: self.id, 'user_id': uid})
            await status.create()
            return status

    async def get_question_amount(self):
        return await self._questions.count_by_field(**{self.id_field: self.id})

    async def update_status(self, uid, add=1, new_status=''):
        question_amount = await self.get_question_amount()
        cond = {self.id_field: self.id, 'user_id': uid}
        status = await self._status.get_first_by_many_field_value(**cond)
        status.progress += add
        if status.progress < question_amount:
            status.status = 'inProgress'
            if not add:
                return
        elif new_status:
            status.status = new_status
        elif status.progress > question_amount:
            status.progress = question_amount
        elif status.progress == question_amount and status.status != 'Submitted':
            status.status = 'Done'
        await status.update(**cond)

    async def add_question(self, question_id, order):
        test_question = self._questions(**{
            self.id_field: self.id,
            'question': question_id,
            'question_order': order
        })
        return await test_question.create()

    @classmethod
    async def get_all_available_questions(cls, as_json=True):
        available_questions = []
        all_questions = await Question.get_all()
        used_questions = await cls._questions.get_all()
        used_questions = [q.question for q in used_questions]
        for question in all_questions:
            if question.id not in used_questions:
                if as_json:
                    available_questions.append({'question_details': await question.to_dict()})
                else:
                    available_questions.append(question)
        return available_questions

    @classmethod
    async def get_all_questions_to_grade(cls, tid, as_json=True):
        resp = []
        questions = await cls._questions.get_all_for_test(tid)
        for quest in questions:
            try:
                quest['graded'] = await cls._answers.get_graded_count(quest['question'])
                quest['to_grade'] = await cls._answers.get_answer_count(quest['question']) - quest['graded']
            except:
                raise
            resp.append(quest)
        return resp

    async def delete_old_questions(self):
        old_questions = self._questions(**{self.id_field: 1, 'question': 1, 'question_order': 1})
        await old_questions.delete(**{self.id_field: self.id})

    @classmethod
    async def get_by_anwers_to_grade_by_qid(cls, qid):
        answers = []
        for ans in await cls._answers.get_answers_by_qid(qid):
            answers.append(await ans.to_dict())
        return answers

    @classmethod
    async def grade_answer_by_uid(cls, qid, uid, score, comment=''):
        try:
            answer = await cls._answers.get_answer_by_uid(qid, uid)
            answer.score = score
            answer.comment = comment
            await answer.update(**{'question': qid, 'user_id': uid})
            return True
        except Exception:
            logging.exception('error grading')
            return False

    async def close_test(self):
        resp = {}
        all_statuses = await self._status.get_by_many_field_value(**{self.id_field: self.id})
        for status in all_statuses:
            status.score = await self._answers.sum_by_uid_tid(uid=status.user_id, tid=self.id)
        resp['max'] = max([status.score for status in all_statuses])
        resp['count'] = len(all_statuses)
        resp['mean'] = resp['max'] / resp['count']
        for status in all_statuses:
            status.score = int(status.score / resp['max'] * 100)
            status.status = 'Graded'
            await status.update(**{"user_id": status.user_id, self.id_field: self.id})
        return resp


class CommonTestQuestion:
    _fk_col = ''

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question_order = db.Column(db.Integer, default=0)
    # TODO unique = ['question_order', cls._fk_col]

    @classmethod
    async def get_all_for_test(cls, tid, uid=0, answer_cls=None, as_json=True):
        test_questions = await cls.get_by_many_field_value(
            **{cls._fk_col + '_id': tid}
        )
        resp = []
        for tq in test_questions:
            if as_json:
                qid = tq.question_id
                tq = await tq.to_dict()
                quest = await Question.get(qid)
                tq['question_details'] = await quest.to_dict()
                if uid and answer_cls:
                    answer = await answer_cls.get_answer_by_uid(quest.id, uid)
                    tq['question_details']['answer'] = answer.answer if answer else ''
            resp.append(tq)
        return resp


class CommonTestAnswer:
    _fk_col = ''

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    answer = db.Column(db.CodeString, nullable=False)
    comment = db.Column(db.CodeString, default='')
    score = db.Column(db.Integer, default=-1)

    # TODO unique = ['users', 'question']

    @classmethod
    async def get_answer_by_uid(cls, qid, uid):
        try:
            return await cls.get_first_by_many_field_value(
                **{'question_id': qid, 'user_id': uid}
            )
        except DoesNotExist:
            return False

    @classmethod
    async def get_answers_by_qid(cls, qid):
        try:
            return await cls.get_by_many_field_value(
                **{'question_id': qid}
            )
        except DoesNotExist:
            return False

    @classmethod
    async def get_answer_count(cls, qid):
        try:
            return await cls.count_by_field(
                **{'question_id': qid}
            )
        except DoesNotExist:
            return False

    @classmethod
    async def get_graded_count(cls, qid):
        try:
            return await cls.count_by_field(
                append=' AND score <> -1',
                **{'question_id': qid}
            )
        except DoesNotExist:
            return False

    @classmethod
    async def sum_by_uid_tid(cls, uid, tid):
        return await cls.sum('score',  **{cls._fk_col + '_id': tid, "user_id": uid}) or 0


class CommonTestStatus:
    _fk_col = ''

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    progress = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=-1)
    comment = db.Column(db.CodeString, default='')
    status = db.Column(db.String, default='NotStarted')

    # TODO unique = ['users', cls._fk_col]
