# !/usr/bin/python3.5
from datetime import datetime

from config import DEFAULT_USER
from orm import Boolean
from orm import CodeString
from orm import Column
from orm import DateTime
from orm import DoesNotExist
from orm import Float
from orm import ForeignKey
from orm import Integer
from orm import String
from orm import StringLiteral
from orm import Table
from utils import hash_string
from utils import safe_del_key


class Question(Table):
    _name = 'question'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('question', String(1000)),
        Column('answares', CodeString(2000), default=''),
        Column('possible_answare', String(1000), default=''),
        Column('qtype', String(50), default='plain'),
        Column('img', String(255), required=False, default=''),
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
        Column('time_created', DateTime(), default=datetime.utcnow),
    ]


class Users(Table):
    _restricted_keys = ['session_uuid', 'password']
    _soft_restricted_keys = ['score', 'notes']
    _name = 'users'
    _schema = [
        Column('id', Integer(), primary_key=True),
        Column('email', String(255), unique=True),
        Column('name', String(255)),
        Column('surname', String(255)),
        Column('password', String(1000)),
        Column('create_date', DateTime(), default=datetime.utcnow),
        Column('last_login', DateTime(), default=datetime.utcnow),
        Column('mentor', Boolean(), default=False),
        Column('organiser', Boolean(), default=False),

        Column('admin', Boolean(), default=False),
        Column('session_uuid', String(255), required=False),

        Column('img', String(255), required=False, default=''),
        Column('linkedin', String(255), required=False),
        Column('twitter', String(255), required=False),
        Column('facebook', String(255), required=False),

        Column('city', String(255), required=False),
        Column('education', String(255), required=False),
        Column('university', String(255), required=False),
        Column('t_shirt', String(10), required=False),
        Column('lang', String(20), required=False, default='pl'),
        Column('age', Integer(), required=False, default=99),

        Column('python', Boolean(), default=False),
        Column('operating_system', String(10), required=False),
        Column('description', String(5000), required=False),
        Column('motivation', String(5000), required=False),
        Column('what_can_you_bring', String(5000), required=False),
        Column('experience', String(5000), required=False),
        Column('app_idea', String(5000), required=False),

        Column('pyfunction', String(255), required=False),

        Column('confirmation', String(10), default='noans'),
        Column('active', Boolean(), default=False),
        Column('accepted_rules', Boolean(), default=False),
        Column('accepted', Boolean(), default=False),
        Column('bring_power_cord', Boolean(), default=False),
        Column('attend_weekly', Boolean(), default=False),
        Column('i_needed_help', Integer(), default=0),

        Column('notes', String(5000), default=''),
        Column('score', Float(), default=0, required=False),
        Column('i_helped', Boolean(), default=False),
        Column('helped', String(5000), required=False),
    ]

    _banned_user_keys = [
        'i_needed_help', 'accepted_rules',
    ]
    _public_keys = _banned_user_keys + [
        'education', 'university', 't_shirt',
        'operating_system', 'motivation', 'experience',
        'app_idea', 'accepted', 'confirmation',
        'i_helped', 'helped',
    ]

    async def create(self):
        self.password = hash_string(self.password)
        return await super().create()

    async def set_password(self, password):
        self.password = hash_string(password)

    @classmethod
    async def get_user_by_session_uuid(cls, session_uuid):
        try:
            return await cls.get_first('session_uuid', session_uuid)
        except DoesNotExist:
            return None

    async def get_public_data(self):
        data = await self.to_dict()
        data = safe_del_key(data, self._public_keys)
        return data

    async def get_my_user_data(self):
        data = await self.to_dict()
        data = safe_del_key(data, self._banned_user_keys)
        return data


class UserReview(Table):
    _name = 'user_review'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('reviewer', ForeignKey('users')),
        Column('score', Integer()),
    ]
    _unique = ['users', 'reviewer']


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
            return {'last': True, 'msg': 'That was the last question in the quiz.'}
        qq = await QuizQuestions.get_first_by_many_field_value(
            quiz=self.id,
            question_order=question_order
        )
        return await Question.get_by_id(qq.question)

    async def get_question_amount(self):
        return len(await QuizQuestions.get_by_field_value('quiz', self.id))


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
        Column('author', ForeignKey('users')),
        Column('answers', CodeString(10000)),
        Column('question', ForeignKey('lesson_feedback_question'))
    ]


class QuestionAnsware(Table):
    _name = 'question_answare'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('question', ForeignKey('question')),
        Column('answare', CodeString(5000)),
    ]
    _unique = ['users', 'question']


class ExerciseAnsware(Table):
    _name = 'exercise_answare'
    _schema = [
        Column('exercise', ForeignKey('exercise')),
        Column('users', ForeignKey('users')),
        Column('answare', CodeString(5000)),
        Column('first_answare', CodeString(5000), default=""),
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
        Column('users', ForeignKey('users'), default=DEFAULT_USER),
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
        return len(await LiveQuizQuestion.get_by_field_value('live_quiz', self.id))


class LiveQuizQuestion(Table):
    _name = 'live_quiz_questions'
    _schema = [
        Column('live_quiz', ForeignKey('live_quiz')),
        Column('question', ForeignKey('question')),
        Column('question_order', Integer(), default=0),
    ]
    _unique = ['live_quiz', 'question_order']


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
        Column('number', Integer()),
        Column('users', ForeignKey('users'), unique=True),
        Column('i_need_help', Boolean(), default=False),
    ]


class Feedback(Table):
    _name = 'feedback'
    _schema = [
        Column('lesson_review', String(10000)),
        Column('teacher_review', String(10000)),
        Column('material', Integer()),
        Column('teacher', ForeignKey('users')),
        Column('users', ForeignKey('users')),
        # O tym czy dobrze było zorganizowane
        # Czy polecilbys nasze warsztaty znajomym
        # Czy moglibyśmy lepiej się reklamować
        # Czy jakieś zagadnienia były za mało poruszone Albo za dużo
        # Czego brakowało
        # https://docs.google.com/forms/d/e/1FAIpQLSctlgSwoKQoB_3Hc5bfu3RYLbz0TNKQmg23jnc8MJ3wwRJn7g/viewform
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


class Config(Table):
    _name = 'config'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('reg_active', Boolean(), default=True),
        Column('room_raws', Integer(), default=10),
        Column('room_columns', Integer(), default=10),
    ]

    @classmethod
    async def get_registration(cls):
        config = await cls.get_by_id(1)
        return config.reg_active
