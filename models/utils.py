# !/usr/bin/python3.5
from datetime import datetime

from config import DEFAULT_USER

from orm import Boolean
from orm import Column
from orm import CodeString
from orm import DateTime
from orm import DoesNotExist
from orm import ForeignKey
from orm import Integer
from orm import String
from orm import Table

from utils import ClassProperty


class Question(Table):
    _name = 'question'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('question', String(1000)),
        Column('answers', CodeString(2000), default=''),
        Column('possible_answer', String(1000), default=''),
        Column('qtype', String(50), default='plain'),
        Column('img', String(255), required=False, default=''),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]


class CommonTestTemplate(Table):
    _name = ''
    _questions = None
    _status = None
    _answers = None
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]

    async def get_question(self, uid=0, as_json=True):
        return await self._questions.get_all_for_test(self.id, uid=uid, answer_cls=self._answers, as_json=as_json)

    async def get_status(self, uid):
        try:
            await self.update_status(uid, add=0)
            return await self._status.get_first_by_many_field_value(
                **{self._name: self.id, 'users': uid}
            )
        except DoesNotExist:
            status = self._status(**{self._name: self.id, 'users': uid})
            await status.create()
            return status

    async def get_question_amount(self):
        return await self._questions.count_by_field(**{self._name: self.id})

    async def update_status(self, uid, add=1, new_status=''):
        question_amount = await self.get_question_amount()
        cond = {self._name: self.id, 'users': uid}
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
            self._name: self.id,
            'question': question_id,
            'question_order': order
        })
        await test_question.create()

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

    async def delete_old_questions(self):
        old_questions = self._questions(**{self._name: 1, 'question': 1, 'question_order': 1})
        await old_questions.delete(**{self._name: self.id})


class CommonTestQuestion(Table):
    _name = ''
    _fk_col = ''

    @ClassProperty
    def _schema(cls):
        return [
            Column(cls._fk_col, ForeignKey(cls._fk_col)),
            Column('question', ForeignKey('question')),
            Column('question_order', Integer(), default=0),
        ]

    @ClassProperty
    def _unique(cls):
        return ['question_order', cls._fk_col]

    @classmethod
    async def get_all_for_test(cls, tid, uid=0, answer_cls=None, as_json=True):
        test_questions = await cls.get_by_many_field_value(
            **{cls._fk_col: tid}
        )
        resp = []
        for tq in test_questions:
            if as_json:
                qid = tq.question
                tq = await tq.to_dict()
                quest = await Question.get_by_id(qid)
                tq['question_details'] = await quest.to_dict()
                if uid and answer_cls:
                    answer = await answer_cls.get_answare_by_uid(quest.id, uid)
                    tq['question_details']['answer'] = answer.answer if answer else ''
            resp.append(tq)
        return resp


class CommonTestAnswer(Table):
    _name = ''
    _fk_col = ''

    @ClassProperty
    def _schema(cls):
        return [
            Column('users', ForeignKey('users')),
            Column(cls._fk_col, ForeignKey(cls._fk_col)),
            Column('question', ForeignKey('question')),
            Column('answer', CodeString(5000)),
            Column('comment', CodeString(1000), required=False, default=''),
            Column('score', Integer(), default=-1),
        ]

    @ClassProperty
    def _unique(cls):
        return ['users', 'question']

    @classmethod
    async def get_answare_by_uid(cls, qid, uid):
        try:
            return await cls.get_first_by_many_field_value(
                **{'question': qid, 'users': uid}
            )
        except DoesNotExist:
            return False


class CommonTestStatus(Table):
    _name = ''
    _fk_col = ''

    @ClassProperty
    def _schema(cls):
        return [
            Column('users', ForeignKey('users')),
            Column(cls._fk_col, ForeignKey(cls._fk_col)),
            Column('progress', Integer(), default=0),
            Column('score', Integer(), default=-1),
            Column('comment', CodeString(1000), required=False, default=''),
            Column('status', String(50), default='NotStarted'),
        ]

    @ClassProperty
    def _unique(cls):
        return ['users', cls._fk_col]
