# !/usr/bin/python3.5
from datetime import datetime

from db_models import Table
from db_models import Column
from db_models import Integer
from db_models import String
from db_models import DateTime
from db_models import Boolean


class Question(Table):
    _name = 'question'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('question', String(1000)),
        Column('answares', String(1000), default=''),
        Column('qtype', String(50), default='plain'),
        Column('img', String(255), required=False, default=''),
        Column('creator', Integer(), default=1),
        Column('reviewer', Integer(), required=False, default=0),
        Column('lesson', Integer(), required=False, default=0),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('time_accepted', DateTime(), required=False, default=datetime(1900, 1, 1, 1, 1, 1, 1)),
        Column('active', Boolean(), default=False),
    ]


class Users(Table):
    _name = 'users'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('email', String(255), unique=True),
        Column('name', String(255)),
        Column('surname', String(255)),
        Column('password', String(1000)),
        Column('description', String(5000), required=False),
        Column('questions', String(10000), default=''),
        Column('live_quiz', String(5000), default=''),
        Column('moderator', Boolean(), default=False),
        Column('admin', Boolean(), default=False),
        Column('active', Boolean(), default=True)
    ]


class Quiz(Table):
    _name = 'quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('questions', String(10000)),
        Column('creator', Integer()),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('time_accepted', DateTime(), required=False),
    ]

    def get_next_question(self, qid):
        return self.questions[self.questions.index(qid) + 1]


class LiveQuiz(Table):
    _name = 'live_quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('questions', String(10000)),
        Column('creator', Integer()),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]


class Lesson(Table):
    _name = 'lesson'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('creator', Integer()),
        Column('file', String(255)),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]
