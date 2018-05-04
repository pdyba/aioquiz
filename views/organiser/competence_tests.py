#!/usr/bin/env python3.5
# encoding: utf-8
from views.organiser.common import CommonOrganiserTestBase

from models import LiveQuiz
from models import Quiz
from models import Exam


class QuizOrgBase(CommonOrganiserTestBase):
    _cls = Quiz
    _urls = ['/api/organiser/quiz', '/api/organiser/quiz/<tid:int>']


class LiveQuizOrgBase(CommonOrganiserTestBase):
    _cls = LiveQuiz
    _urls = ['/api/organiser/live_quiz', '/api/organiser/live_quiz/<tid:int>']


class ExamOrgBase(CommonOrganiserTestBase):
    _cls = Exam
    _urls = ['/api/organiser/exam/', '/api/organiser/exam/<tid:int>']
