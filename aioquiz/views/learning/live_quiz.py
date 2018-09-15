#!/usr/bin/env python3.5
# encoding: utf-8
from views.learning.common import CommonTestBase

from models import LiveQuiz
from models import LiveQuizAnswer


# noinspection PyBroadException
class LiveQuizView(CommonTestBase):
    _cls = LiveQuiz
    _cls_answer = LiveQuizAnswer
    _urls = ['/api/live_quiz', '/api/live_quiz/<qid:int>']
