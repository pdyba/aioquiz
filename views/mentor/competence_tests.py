#!/usr/bin/env python3.5
# encoding: utf-8
from views.mentor.common import CommonMentorTestBase

from models import Quiz
from models import Exam


class QuizMentorBase(CommonMentorTestBase):
    _cls = Quiz
    _urls = ['/api/mentor/quiz', '/api/mentor/quiz/<tid:int>']


class ExamMentorBase(CommonMentorTestBase):
    _cls = Exam
    _urls = ['/api/mentor/exam/', '/api/mentor/exam/<tid:int>']
