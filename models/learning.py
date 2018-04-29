# !/usr/bin/python3.5
from datetime import datetime

from config import DEFAULT_USER
from orm import Boolean
from orm import CodeString
from orm import Column
from orm import DateTime
from orm import ForeignKey
from orm import Integer
from orm import String
from orm import Table


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


class Quiz(Table):
    _name = 'quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]

    async def get_question(self, question_order=1):
        if question_order + 1 >= await self.get_question_amount():
            return {'last': True, 'msg': 'That was the last question of the quiz.'}
        qq = await QuizQuestions.get_first_by_many_field_value(
            quiz=self.id,
            question_order=question_order
        )
        return await Question.get_by_id(qq.question)

    async def get_question_amount(self):
        return len(await QuizQuestions.get_by_field_value('quiz', self.id))


class QuestionAnswer(Table):
    _name = 'question_answer'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('question', ForeignKey('question')),
        Column('answer', CodeString(5000)),
    ]
    _unique = ['users', 'question']


class QuizQuestions(Table):
    _name = 'quiz_questions'
    _schema = [
        Column('quiz', ForeignKey('quiz')),
        Column('question', ForeignKey('question')),
        Column('question_order', Integer(), default=0),
    ]


class LiveQuiz(Table):
    _name = 'live_quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]

    async def get_question(self, question_order=0):
        if question_order + 1 >= await self.get_question_amount():
            return {'last': True, 'msg': 'That was the last question of the quiz.'}
        lqq = await LiveQuizQuestion.get_first_by_many_field_value(
            live_quiz=self.id,
            question_order=question_order
        )
        return await Question.get_by_id(lqq.question)

    async def get_question_amount(self):
        return len(await LiveQuizQuestion.get_by_field_value('live_quiz', self.id))


class LiveQuizQuestion(Table):
    _name = 'live_quiz_questions'
    _schema = [
        Column('live_quiz', ForeignKey('live_quiz')),
        Column('question', ForeignKey('question')),
        Column('question_order', Integer(), default=0),
    ]
    _unique = ['live_quiz', 'question_order']


class LiveQuizAnswer(Table):
    _name = 'live_quiz_answer'
    _schema = [
        Column('live_quiz', ForeignKey('live_quiz')),
        Column('question', ForeignKey('question')),
        Column('answer', CodeString(5000)),
    ]
