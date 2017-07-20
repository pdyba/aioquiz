# !/usr/bin/python3.5
from datetime import datetime

from orm import Table
from orm import Column
from orm import Integer
from orm import String
from orm import DateTime
from orm import Boolean
from orm import Float
from orm import ForeignKey


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
        Column('city', String(255), required=False),
        Column('education', String(255), required=False),
        Column('university', String(255), required=False),
        Column('t_shirt', String(10), required=False),
        Column('operating_system', String(10), required=False),
        Column('confirmation', String(10), default='noans'),
        Column('description', String(5000), required=False),
        Column('motivation', String(5000), required=False),
        Column('what_can_you_bring', String(5000), required=False),
        Column('experience', String(5000), required=False),
        Column('app_idea', String(5000), required=False),
        Column('questions', String(10000), default=''),
        Column('live_quiz', String(5000), default=''),
        Column('notes', String(5000), default=''),
        Column('mentor', Boolean(), default=False),
        Column('admin', Boolean(), default=False),
        Column('active', Boolean(), default=False),
        Column('accepted_rules', Boolean(), default=False),
        Column('accepted', Boolean(), default=False),
        Column('create_date', DateTime(), default=datetime.utcnow),
        Column('last_login', DateTime(), default=datetime.utcnow),
        Column('session_uuid', String(255), required=False),
        Column('score', Float(), default=0, required=False),
    ]


class QuestionAnsware(Table):
    _name = 'question_answare'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('question', ForeignKey('question')),
        Column('answare', String(5000)),
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


class LessonStatus(Table):
    _name = 'lesson_status'
    _schema = [
        Column('lesson', ForeignKey('lesson')),
        Column('users', ForeignKey('users')),
        Column('status', String(20)),
    ]


class Quiz(Table):
    _name = 'quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('questions', String(10000)),
        Column('creator', Integer()),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]

    def get_next_question(self, qid):
        return self.questions[self.questions.index(qid) + 1]


class QuizQuestions(Table):
    _name = 'quiz_questions'
    _schema = [
        Column('quiz', ForeignKey('quiz')),
        Column('question', ForeignKey('question')),
    ]


class LiveQuiz(Table):
    _name = 'live_quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('creator', Integer()),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]


class LiveQuizQuestion(Table):
    _name = 'live_quiz_questions'
    _schema = [
        Column('lesson', ForeignKey('lesson')),
        Column('question', ForeignKey('question')),
    ]


class LiveQuizAnsware(Table):
    _name = 'live_quiz_answare'
    _schema = [
        Column('live_quiz', ForeignKey('live_quiz')),
        Column('question', ForeignKey('question')),
        Column('answare', String(5000)),
    ]