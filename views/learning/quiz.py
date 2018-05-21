#!/usr/bin/env python3.5
# encoding: utf-8
from models import Quiz
from models import QuizAnswer

from views.learning.common import CommonTestBase


# noinspection PyBroadException
class QuizView(CommonTestBase):
    _cls = Quiz
    _cls_answer = QuizAnswer
    _urls = ['/api/quiz', '/api/quiz/<qid:int>']
