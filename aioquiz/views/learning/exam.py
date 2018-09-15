#!/usr/bin/env python3.5
# encoding: utf-8
from models import Exam
from models import ExamAnswer

from views.learning.common import CommonTestBase


# noinspection PyBroadException
class ExamView(CommonTestBase):
    _cls = Exam
    _cls_answer = ExamAnswer
    _urls = ['/api/exam', '/api/exam/<qid:int>']
