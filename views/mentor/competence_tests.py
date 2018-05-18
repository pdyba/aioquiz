#!/usr/bin/env python3.5
# encoding: utf-8
from views.mentor.common import CommonMentorTestBase
from views.mentor.common import CommonMentorQuestionGradeBase

from models import Quiz
from models import Exam


class QuizMentor(CommonMentorTestBase):
    _cls = Quiz
    _urls = ['/api/mentor/quiz', '/api/mentor/quiz/<tid:int>']


class ExamMentor(CommonMentorTestBase):
    _cls = Exam
    _urls = ['/api/mentor/exam/', '/api/mentor/exam/<tid:int>']


class QuizMentorGrade(CommonMentorQuestionGradeBase):
    _cls = Quiz
    _urls = ['/api/mentor/grad/quiz', '/api/mentor/grade/quiz/<qid:int>']


class ExamMentorGrade(CommonMentorQuestionGradeBase):
    _cls = Exam
    _urls = ['/api/mentor/grade/exam/', '/api/mentor/grade/exam/<qid:int>']
