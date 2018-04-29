# !/usr/bin/python3.5
from datetime import datetime

from config import DEFAULT_USER
from orm import Boolean
from orm import Column
from orm import CodeString
from orm import DateTime
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
        Column('answer', CodeString(2000), default=''),
        Column('possible_answer', String(1000), default=''),
        Column('qtype', String(50), default='plain'),
        Column('img', String(255), required=False, default=''),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]


class CommonTestTemplate(Table):
    _name = ''
    _questions = None
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]

    async def get_question(self):
        return await self._questions.get_by_many_field_value(
            **{self._name: self.id}
        )

    async def get_question_amount(self):
        return await self._questions.count_by_field(**{self._name: self.id})


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
        ]

    @ClassProperty
    def _unique(cls):
        return ['users', cls._fk_col]
