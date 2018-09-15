# !/usr/bin/python3.5
from datetime import datetime

from config import DEFAULT_USER
from models.db import db, EnchancedModel
from orm import StringLiteral


class Lesson(EnchancedModel):
    __tablename__ = 'lessons'

    id = db.Column(db.Integer, primary_key=True)
    lesson_no = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=DEFAULT_USER)
    file = db.Column(db.String)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    active = db.Column(db.Boolean, default=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'))
    live_quiz_id = db.Column(db.Integer, db.ForeignKey('live_quizes.id'))


class Exercise(EnchancedModel):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    task = db.Column(db.CodeString, nullable=False)
    possible_answer = db.Column(db.CodeString)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=DEFAULT_USER)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))


class ExerciseAnswer(EnchancedModel):
    __tablename__ = 'exercise_answers'

    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    answer = db.Column(db.CodeString, nullable=False)
    first_answer = db.Column(db.CodeString, default='')
    status = db.Column(db.String, nullable=False)


class LessonFeedbackQuestion(EnchancedModel):
    __tablename__ = 'lesson_feedback_questions'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=DEFAULT_USER)
    type = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    answers = db.Column(db.CodeString, nullable=False)

    @classmethod
    async def get_by_lesson_id(cls, lid):
        return await cls.get_by_join(
            "lesson_feedback_meta",
            lesson=lid,
            id=StringLiteral("question")
        )


class LessonFeedbackMeta(EnchancedModel):
    __tablename__ = 'lesson_feetback_meta'

    question_id = db.Column(db.Integer, db.ForeignKey('lesson_feedback_questions.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)


class LessonFeedbackAnswer(EnchancedModel):
    __tablename__ = 'lesson_feedback_answers'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    answers = db.Column(db.CodeString, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('lesson_feedback_questions.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)


class Feedback(EnchancedModel):
    __tablename__ = 'feedback'

    lesson_review = db.Column(db.String, nullable=False)
    teacher_review = db.Column(db.String, nullable=False)
    material = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class Absence(EnchancedModel):
    __tablename__ = 'absence'

    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    absent = db.Column(db.Boolean, default=True)


class AbsenceMeta(EnchancedModel):
    __tablename__ = 'absence_meta'

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    code = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_created = db.Column(db.DateTime, default=datetime.utcnow)
    time_ended = db.Column(db.DateTime)
