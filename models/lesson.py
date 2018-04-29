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
from orm import StringLiteral
from orm import Table


class Lesson(Table):
    _name = 'lesson'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('lesson_no', Integer()),
        Column('title', String(255)),
        Column('description', String(10000)),
        Column('author', ForeignKey('users'), default=DEFAULT_USER),
        Column('file', String(255), required=False),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('active', Boolean(), default=False),
        Column('quiz', ForeignKey('quiz'), required=False),
        Column('live_quiz', ForeignKey('live_quiz'), required=False),
    ]


class Exercise(Table):
    _name = 'exercise'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('title', String(255)),
        Column('task', CodeString(10000)),
        Column('possible_answare', CodeString(1000), required=False),
        Column('author', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('lesson', ForeignKey('lesson')),
    ]
    _unique = ['title']


class ExerciseAnsware(Table):
    _name = 'exercise_answare'
    _schema = [
        Column('exercise', ForeignKey('exercise')),
        Column('users', ForeignKey('users')),
        Column('answare', CodeString(5000)),
        Column('first_answare', CodeString(5000), default=""),
        Column('status', String(20)),
    ]


class LessonFeedbackQuestion(Table):
    _name = 'lesson_feedback_question'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('author', ForeignKey('users'), default=DEFAULT_USER),
        Column('type', String(50)),
        Column('description', String(5000)),
        Column('answers', CodeString(10000))
    ]

    @classmethod
    async def get_by_lesson_id(cls, lid):
        return await cls.get_by_join(
            "lesson_feedback_meta",
            lesson=lid,
            id=StringLiteral("question")
        )


class LessonFeedbackMeta(Table):
    _name = 'lesson_feedback_meta'
    _schema = [
        Column('question', ForeignKey('lesson_feedback_question')),
        Column('lesson', ForeignKey('lesson'))
    ]


class LessonFeedbackAnswer(Table):
    _name = 'lesson_feedback_answer'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('author', ForeignKey('users')),
        Column('answers', CodeString(10000)),
        Column('question', ForeignKey('lesson_feedback_question')),
        Column('lesson', ForeignKey('lesson'))
    ]


class Feedback(Table):
    _name = 'feedback'
    _schema = [
        Column('lesson_review', String(10000)),
        Column('teacher_review', String(10000)),
        Column('material', Integer()),
        Column('teacher', ForeignKey('users')),
        Column('users', ForeignKey('users')),
    ]


class Absence(Table):
    _name = 'absence'
    _schema = [
        Column('lesson', ForeignKey('lesson')),
        Column('users', ForeignKey('users')),
        Column('absent', Boolean(), default=True),
    ]


class AbsenceMeta(Table):
    _name = 'absence_meta'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('lesson', ForeignKey('lesson')),
        Column('code', String(10)),
        Column('active', Boolean(), default=True),
        Column('users', ForeignKey('users')),
        Column('time_created', DateTime(), default=datetime.utcnow),
        Column('time_ended', DateTime()),
    ]
