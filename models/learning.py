# !/usr/bin/python3.5
from models.utils import CommonTestAnswer
from models.utils import CommonTestQuestion
from models.utils import CommonTestStatus
from models.utils import CommonTestTemplate


class QuestionAnswer(CommonTestAnswer):
    _name = 'question_answer'
    _fk_col = 'quiz'


class QuizQuestions(CommonTestQuestion):
    _name = 'quiz_questions'
    _fk_col = 'quiz'


class QuizStatus(CommonTestStatus):
    _name = 'quiz_status'
    _fk_col = 'quiz'


class Quiz(CommonTestTemplate):
    _name = 'quiz'
    _questions = QuizQuestions
    _status = QuizStatus


class LiveQuizQuestion(CommonTestQuestion):
    _name = 'live_quiz_questions'
    _fk_col = 'live_quiz'


class LiveQuizAnswer(CommonTestAnswer):
    _name = 'live_quiz_answer'
    _fk_col = 'live_quiz'


class LiveQuizStatus(CommonTestStatus):
    _name = 'live_quiz_status'
    _fk_col = 'live_quiz'


class LiveQuiz(CommonTestTemplate):
    _name = 'live_quiz'
    _questions = LiveQuizQuestion
    _status = LiveQuizStatus


class ExamQuestion(CommonTestQuestion):
    _name = 'exam_question'
    _fk_col = 'exam'
    _unique = ['exam', 'question_order']


class ExamAnswer(CommonTestAnswer):
    _name = 'exam_answer'
    _fk_col = 'exam'


class ExamStatus(CommonTestStatus):
    _name = 'exam_status'
    _fk_col = 'exam'


class Exam(CommonTestTemplate):
    _name = 'exam'
    _questions = ExamAnswer
