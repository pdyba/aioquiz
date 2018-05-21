#!/usr/bin/env python3.5
# encoding: utf-8
from views.organiser.common import CommonOrganiserTestBase
from views.organiser.common import CommonActiveateTestBase

from models import LiveQuiz
from models import Quiz
from models import Exam


class QuizOrg(CommonOrganiserTestBase):
    _cls = Quiz
    _urls = ['/api/organiser/quizs', '/api/organiser/quizs/<tid:int>']


class QuizActive(CommonActiveateTestBase):
    _cls = Quiz
    _urls = ['/api/organiser/quiz/set_active']


class LiveQuizOrg(CommonOrganiserTestBase):
    _cls = LiveQuiz
    _urls = ['/api/organiser/live_quizs', '/api/organiser/live_quizs/<tid:int>']


class LiveQuizActive(CommonActiveateTestBase):
    _cls = LiveQuiz
    _urls = ['/api/organiser/live_quiz/set_active']


class ExamOrg(CommonOrganiserTestBase):
    _cls = Exam
    _urls = ['/api/organiser/exams/', '/api/organiser/exams/<tid:int>']


class ExamActive(CommonActiveateTestBase):
    _cls = Exam
    _urls = ['/api/organiser/exam/set_active']