# !/usr/bin/python3.5
from datetime import datetime

from orm import Table
from orm import DoesNoteExists
from orm import Column
from orm import Integer
from orm import String
from orm import CodeString
from orm import DateTime
from orm import Boolean
from orm import Float
from orm import ForeignKey


class Question(Table):
    _name = 'question'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('question', String(1000)),
        Column('answares', CodeString(2000), default=''),
        Column('possible_answare', String(1000), default=''),
        Column('qtype', String(50), default='plain'),
        Column('img', String(255), required=False, default=''),
        Column('users', ForeignKey('users'), default=1),
        Column('time_created', DateTime(), default=datetime.utcnow),
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
        Column('img', String(255), required=False, default=''),
        Column('motivation', String(5000), required=False),
        Column('what_can_you_bring', String(5000), required=False),
        Column('experience', String(5000), required=False),
        Column('app_idea', String(5000), required=False),
        Column('notes', String(5000), default=''),
        Column('mentor', Boolean(), default=False),
        Column('organiser', Boolean(), default=False),
        Column('admin', Boolean(), default=False),
        Column('active', Boolean(), default=False),
        Column('accepted_rules', Boolean(), default=False),
        Column('accepted', Boolean(), default=False),
        Column('create_date', DateTime(), default=datetime.utcnow),
        Column('last_login', DateTime(), default=datetime.utcnow),
        Column('session_uuid', String(255), required=False),
        Column('score', Float(), default=0, required=False),
        Column('i_needed_help', Integer(), default=0),
        Column('linkedin', String(255), required=False),
        Column('twitter', String(255), required=False),
        Column('facebook', String(255), required=False),
        Column('pyfunction', String(255), required=False),
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
        Column('users', ForeignKey('users'), default=1),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]

    async def get_question(self, question_order=0):
        if question_order + 1 >= await self.get_question_amount():
            return {'last': True, 'msg': 'That was last question in the quiz.'}
        qq = await QuizQuestions.get_first_by_many_field_value(
            quiz=self.id,
            question_order=question_order
        )
        return await Question.get_by_id(qq.question)

    async def get_question_amount(self):
        return len(await QuizQuestions.get_by_field_value(
            'quiz', self.id
        ))


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
        Column('answare', CodeString(5000)),
    ]


class ExerciseAnsware(Table):
    _name = 'lesson_status'
    _schema = [
        Column('exercise', ForeignKey('exercise')),
        Column('users', ForeignKey('users')),
        Column('answare', CodeString(5000)),
        Column('status', String(20)),
    ]


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
        Column('users', ForeignKey('users'), default=1),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
    ]

    async def get_question(self, question_order=0):
        if question_order + 1 >= await self.get_question_amount():
            return {'last': True, 'msg': 'That was last question in the quiz.'}
        lqq = await LiveQuizQuestion.get_first_by_many_field_value(
            live_quiz=self.id,
            question_order=question_order
        )
        return await Question.get_by_id(lqq.question)

    async def get_question_amount(self):
        return len(await LiveQuizQuestion.get_by_field_value(
            'live_quiz', self.id
        ))


class LiveQuizQuestion(Table):
    _name = 'live_quiz_questions'
    _schema = [
        Column('live_quiz', ForeignKey('live_quiz')),
        Column('question', ForeignKey('question')),
        Column('question_order', Integer(), default=0),
    ]


class LiveQuizAnsware(Table):
    _name = 'live_quiz_answare'
    _schema = [
        Column('live_quiz', ForeignKey('live_quiz')),
        Column('question', ForeignKey('question')),
        Column('answare', CodeString(5000)),
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

