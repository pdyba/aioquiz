# !/usr/bin/python3.5
from models.db import db, EnchancedModel
from models.utils import CommonTestAnswer
from models.utils import CommonTestQuestion
from models.utils import CommonTestStatus
from models.utils import CommonTestTemplate


# Quiz Section
class QuizAnswer(CommonTestAnswer, EnchancedModel):
    __tablename__ = 'quiz_answers'
    _fk_col = 'quiz'
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'), nullable=False)


class QuizQuestions(CommonTestQuestion, EnchancedModel):
    __tablename__ = 'quiz_questions'
    _fk_col = 'quiz'
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'), nullable=False)


class QuizStatus(CommonTestStatus, EnchancedModel):
    __tablename__ = 'quiz_statuses'
    _fk_col = 'quiz'
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'), nullable=False)


class Quiz(CommonTestTemplate, EnchancedModel):
    __tablename__ = 'quizes'
    _questions = QuizQuestions
    _status = QuizStatus
    _answers = QuizAnswer


# LiveQuiz Section
class LiveQuizQuestion(CommonTestQuestion, EnchancedModel):
    __tablename__ = 'live_quiz_questions'
    _fk_col = 'live_quiz'
    live_quiz_id = db.Column(db.Integer, db.ForeignKey('live_quizes.id'), nullable=False)


class LiveQuizAnswer(CommonTestAnswer, EnchancedModel):
    __tablename__ = 'live_quiz_answers'
    _fk_col = 'live_quiz'
    live_quiz_id = db.Column(db.Integer, db.ForeignKey('live_quizes.id'), nullable=False)


class LiveQuizStatus(CommonTestStatus, EnchancedModel):
    __tablename__ = 'live_quiz_statuses'
    _fk_col = 'live_quiz'
    live_quiz_id = db.Column(db.Integer, db.ForeignKey('live_quizes.id'), nullable=False)


class LiveQuiz(CommonTestTemplate, EnchancedModel):
    __tablename__ = 'live_quizes'
    _questions = LiveQuizQuestion
    _status = LiveQuizStatus
    _answers = LiveQuizAnswer


# Exam Section
class ExamQuestion(CommonTestQuestion, EnchancedModel):
    __tablename__ = 'exam_questions'
    _fk_col = 'exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)

    # TODO _unique = ['exam', 'question_order']


class ExamAnswer(CommonTestAnswer, EnchancedModel):
    __tablename__ = 'exam_answers'
    _fk_col = 'exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)


class ExamStatus(CommonTestStatus, EnchancedModel):
    __tablename__ = 'exam_statuses'
    _fk_col = 'exam'
    exam_id = db.Column(db.Integer, db.ForeignKey('exams.id'), nullable=False)


class Exam(CommonTestTemplate, EnchancedModel):
    __tablename__ = 'exams'
    _questions = ExamQuestion
    _status = ExamStatus
    _answers = ExamAnswer
