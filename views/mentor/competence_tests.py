#!/usr/bin/env python3.5
# encoding: utf-8
from views.mentor.common import CommonMentorTestBase

from models import LiveQuiz
from models import Quiz
from models import Exam


class QuizOrgBase(CommonMentorTestBase):
    _cls = Quiz
    _urls = ['/api/mentor/quiz', '/api/mentor/quiz/<tid:int>']


class LiveQuizOrgBase(CommonMentorTestBase):
    _cls = LiveQuiz
    _urls = ['/api/mentor/live_quiz', '/api/mentor/live_quiz/<tid:int>']


class ExamOrgBase(CommonMentorTestBase):
    _cls = Exam
    _urls = ['/api/mentor/exam/', '/api/mentor/exam/<tid:int>']
