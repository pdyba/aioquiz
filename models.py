# !/usr/bin/python3.5
from datetime import datetime

from orm import Table
from orm import DoesNoteExists
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
        Column('answare', String(1000), default=''),
        Column('qtype', String(50), default='plain'),
        Column('img', String(255), required=False, default=''),
        Column('users', ForeignKey('users'), default=1),
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
        Column('i_needed_help', Integer(), default=0),
    ]

    @classmethod
    async def get_user_by_session_uuid(cls, session_uuid):
        try:
            return await cls.get_first('session_uuid', session_uuid)
        except DoesNoteExists:
            return None


class Lesson(Table):
    _name = 'lesson'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('users', ForeignKey('users'), default=1),
        Column('file', String(255)),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
        Column('quiz', ForeignKey('quiz'), required=False),
    ]


class Quiz(Table):
    _name = 'quiz'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('questions', String(10000)),
        Column('users', ForeignKey('users'), default=1),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]

    def get_next_question(self, qid):
        return self.questions[self.questions.index(qid) + 1]


class Exercise(Table):
    _name = 'exercise'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('users', ForeignKey('users'), default=1),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]


class LessonFeedback(Table):
    _name = 'lesson_feedback'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('lesson', ForeignKey('lesson')),
        Column('feedback', String(5000)),
    ]


class LessonExercise(Table):
    _name = 'lesson_exercise'
    _schema = [
        Column('lesson', ForeignKey('lesson')),
        Column('exercise', ForeignKey('exercise')),
        Column('feedback', String(5000)),
    ]


class LessonStatus(Table):
    _name = 'lesson_status'
    _schema = [
        Column('lesson', ForeignKey('lesson')),
        Column('users', ForeignKey('users')),
        Column('status', String(20)),
    ]


class QuestionAnsware(Table):
    _name = 'question_answare'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('question', ForeignKey('question')),
        Column('answare', String(5000)),
    ]


class ExerciseAnsware(Table):
    _name = 'lesson_status'
    _schema = [
        Column('exercise', ForeignKey('exercise')),
        Column('users', ForeignKey('users')),
        Column('answare', String(5000)),
        Column('status', String(20)),
    ]


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
        Column('users', ForeignKey('users'), default=1),
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


class Seat(Table):
    _name = 'seat'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('row', String(255)),
        Column('number', String(10000)),
        Column('users', ForeignKey('users')),
        Column('i_need_help', Boolean, default=False),
    ]


class Feedback(Table):
    _name = 'seat'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('row', String(255)),
        Column('number', String(10000)),
        Column('users', ForeignKey('users')),
    ]

