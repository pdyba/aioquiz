#!/usr/bin/env python3.5
# encoding: utf-8
from views.organiser.common import CommonOrganiserTestView

from models import LiveQuiz
from models import Quiz
from models import Exam


class QuizOrgView(CommonOrganiserTestView):
    _cls = Quiz
    _urls = ['/api/organiser/quiz', '/api/organiser/quiz/<tid:int>']


class LiveQuizOrgView(CommonOrganiserTestView):
    _cls = LiveQuiz
    _urls = ['/api/organiser/live_quiz', '/api/organiser/live_quiz/<tid:int>']


class ExamOrgView(CommonOrganiserTestView):
    _cls = Exam
    _urls = ['/api/organiser/exam/', '/api/organiser/exam/<tid:int>']
