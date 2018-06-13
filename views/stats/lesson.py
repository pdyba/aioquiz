#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from models import Absence
from models import AbsenceMeta
from models import ExamStatus
from models import Exercise
from models import ExerciseAnswer
from models import ExamAnswer
from models import Lesson
from models import Users

from orm import DoesNotExist

from views.utils import user_required
from views.utils import HTTPModelClassView

FINAL_EXAM = 6
INTERN_EXAM = 3

class ExerciseOverview(HTTPModelClassView):
    _cls = Exercise
    _urls = '/api/stats/exercises'

    @user_required('mentor')
    async def get(self, _):
        exercises = await Exercise.get_all()
        resp = {}
        for ex in exercises:
            if not resp.get(ex.lesson):
                resp[ex.lesson] = {}
            resp[ex.lesson][ex.id] = await ex.to_dict()
            resp[ex.lesson][ex.id]['exercise_answer'] = await ExerciseAnswer.group_by_field('status', exercise=ex.id)
        return json(resp)

    @user_required('organiser')
    async def post(self, request, current_user):
        req = request.json
        max_exercises = await Exercise.count_all()
        resp = {'exercises': {}, 'max_exercises': max_exercises}
        for uid in req:
            ec = await ExerciseAnswer.count_by_field(users=uid)
            ec += 30 # zgubione zadania przy stracie bazy danych
            ec = ec if ec < max_exercises else max_exercises
            resp['exercises'][uid] = ec
        return json(resp)


class ExamOverview(HTTPModelClassView):
    _cls = Exercise
    _urls = '/api/stats/exam'

    @user_required('organiser')
    async def post(self, request, current_user):
        req = request.json
        resp = {'exams': {}, 'intern': {}}
        for uid in req:
            try:
                exam = await ExamStatus.get_first_by_many_field_value(users=uid, exam=FINAL_EXAM)  # TODO: change it in future
                resp['exams'][uid] = exam.score
            except DoesNotExist:
                resp['exams'][uid] = -1
            try:
                intern_ans = await ExamAnswer.get_by_many_field_value(users=uid, exam=INTERN_EXAM)  # TODO: change it in future
                intern_resp = {}  # so hackish so sad
                for intern in intern_ans:
                    if intern.question == 9:
                        intern_resp['intern'] = intern.answer
                    if intern.question == 10:
                        intern_resp['why'] = intern.answer
                    if intern.question == 11:
                        intern_resp['1'] = intern.answer
                    if intern.question == 12:
                        intern_resp['2'] = intern.answer
                    if intern.question == 13:
                        intern_resp['3'] = intern.answer
                    if intern.question == 14:
                        intern_resp['details'] = intern.answer
                resp['intern'][uid] = intern_resp
            except DoesNotExist:
                pass
        return json(resp)


class AbsenceStatsView(HTTPModelClassView):
    _cls = Absence
    _urls = ['/api/stats/attendance', '/api/stats/attendance/<lid:int>']

    @user_required()
    async def get(self, _, current_user, lid=None):
        if current_user.admin and lid:
            absences = await Absence.get_by_field_value('lesson', lid)
            lesson = await Lesson.get_by_id(lid)
            lesson = lesson.title
            max_absences = 200
            current_attendence = len(absences)
        else:
            absences = await AbsenceMeta.get_all()
            user_absence = await Absence.get_by_field_value('users', current_user.id)
            lesson = ""
            max_absences = len(absences)
            current_attendence = len(user_absence)
        attendance = []

        for absence in absences:
            if not lid:
                lesson = await Lesson.get_by_id(absence.lesson)
                data = {'lesson': lesson.title}
                uabs = list(filter(
                    lambda b: b.lesson == absence.lesson,
                    user_absence
                ))
                data['absent'] = True if uabs else False
            else:
                data = await absence.to_dict()
                user = await Users.get_by_id(data['users'])
                data['users'] = user.surname
            attendance.append(data)

        return json({
            'max': max_absences,
            'amount': current_attendence,
            'data': attendance,
            'lesson': lesson,
            'perc': "{}%".format(round(current_attendence/max_absences*100, 2))
        })

    @user_required('organiser')
    async def post(self, request, current_user):
        req = request.json
        max_absences = await AbsenceMeta.count_all()
        resp = {'absences': {}, 'max_absences': max_absences}
        for uid in req:
            resp['absences'][uid] = await Absence.count_by_field(users=uid)
        return json(resp)
