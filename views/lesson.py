#!/usr/bin/env python3.5
# encoding: utf-8
from datetime import datetime
import logging
from uuid import uuid4

from sanic.response import json

from orm import DoesNotExist
from models import Absence
from models import AbsenceMeta
from models import Exercise
from models import ExerciseAnsware
from models import Lesson
from models import Users
from utils import hash_string

from views.utils import user_required
from views.utils import HTTPModelClassView


# noinspection PyBroadException
class LessonView(HTTPModelClassView):
    _cls = Lesson
    _urls = ['/api/lessons', '/api/lessons/<qid:int>']

    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            user = await Users.get_first('email', req['creator'])
            req['creator'] = user.id
            lesson = Lesson(**req)
            await lesson.create()
            return json({'success': True})
        except:
            logging.exception('err lesson.post')
            return json({'msg': 'error creating'}, status=500)

    @user_required()
    async def get(self, _, current_user, lid=None):
        if lid:
            lesson = await Lesson.get_by_id(lid)
            return json(await lesson.to_dict())
        else:
            lessons = await Lesson.get_all()
            resp = []
            for l in lessons:
                resp.append(await l.to_dict())
            resp.sort(key=lambda a: a['id'])
            return json(resp, sort_keys=True)


# noinspection PyBroadException
class ExercisesView(HTTPModelClassView):
    _cls = Exercise
    _urls = ['/api/exercise', '/api/exercise/<lid:int>']

    @user_required()
    async def get(self, request, current_user, lid=0):
        if not lid:
            return json({}, 404)
        exercises = await Exercise.get_by_field_value('lesson', lid)
        resp = []
        for ex in exercises:
            q = await ex.to_dict()
            try:
                ans = await ExerciseAnsware.get_first_by_many_field_value(
                    users=current_user.id,
                    exercise=ex.id
                )
            except DoesNotExist:
                ans = None
            if ans:
                q['answared'] = True
                q['answare'] = ans.answare
            else:
                q['answared'] = False
            resp.append(q)
        resp.sort(key=lambda a: a['title'])
        return json(resp, sort_keys=True)

    @user_required()
    async def post(self, request, current_user):
        req = request.json
        req['users'] = current_user.id
        ex = ExerciseAnsware(**req)
        try:
            await ex.create()
            return json({'success': True, 'msg': 'Exercise answare saved'})
        except:
            logging.exception("ExercisesView.post")
        return json({
            'success': False,
            'msg': 'ERROR: Exercise answare NOT saved'
        })

    @user_required()
    async def put(self, request, current_user):
        req = request.json
        ex = await ExerciseAnsware.get_first_by_many_field_value(
            users=current_user.id,
            exercise=req['exercise']
        )
        if not ex.first_answare:
            ex.first_answare = ex.answare
        ex.answare = req['answare']
        try:
            await ex.update(users=current_user.id, exercise=req['exercise'])
            return json({'success': True, 'msg': 'Exercise answare saved'})
        except:
            logging.exception("ExercisesView.post")
        return json({
            'success': False,
            'msg': 'ERROR: Exercise answare NOT saved'
        })


class AbsenceManagementView(HTTPModelClassView):
    _cls = Absence
    _urls = ['/api/absence', '/api/absence/<lid:int>']

    @user_required('admin')
    async def get(self, _, current_user, lid=None):
        try:
            abmeta = await AbsenceMeta.get_first('lesson', lid)
            resp = await abmeta.to_dict()
            resp['time_ended'] = str(resp['time_ended']).split('.')[0]
            return json(resp)
        except (DoesNotExist, TypeError):
            return await self.generate_code(current_user.id, lid)

    @user_required()
    async def put(self, request, current_user):
        req = request.json
        code = req.get('code')
        if not code:
            return json(
                {
                    'success': False,
                    'msg': 'Missing code'
                },
                sort_keys=True
            )
        abmeta = await AbsenceMeta.get_first('code', code)
        if code != abmeta.code:
            return json(
                {
                    'success': False,
                    'msg': 'Wrong code'
                },
                sort_keys=True
            )
        now = datetime.utcnow()
        if now > abmeta.time_ended:
            return json(
                {
                    'success': False,
                    'msg': 'You were too late'
                },
                sort_keys=True
            )
        absence = Absence(lesson=abmeta.lesson, users=current_user.id, absent=True)
        await absence.update_or_create('lesson', 'users')
        return json(
            {
                'success': True,
                'msg': 'Attendance accepted'
            },
            sort_keys=True
        )

    @staticmethod
    async def generate_code(uid, lid):
        req = {'lesson': lid, 'users': uid}
        code = str(uuid4()).split('-')[0]
        time_ended = datetime.now()
        new_min = time_ended.minute + 2 if time_ended.minute < 58 else 2
        new_hour = time_ended.hour + 1 if time_ended.minute > 57 else time_ended.hour
        time_ended = time_ended.replace(minute=new_min, hour=new_hour)
        req['code'] = code
        req['time_ended'] = time_ended
        abmeta = AbsenceMeta(**req)
        await abmeta.create()
        return json(
            {
                'success': True,
                'msg': 'Created',
                'code': code,
                'time_ended': str(time_ended).split('.')[0]
            },
            sort_keys=True
        )

    @user_required('admin')
    async def post(self, _, current_user, lid=None):
        abmeta = await AbsenceMeta.get_first('lesson', lid)
        time_ended = datetime.now()
        time_ended = time_ended.replace(minute=time_ended.minute+2)
        abmeta.time_ended = time_ended
        await abmeta.update()
        resp = await abmeta.to_dict()
        resp['time_ended'] = str(time_ended).split('.')[0]
        return json(resp)


class AbsenceView(HTTPModelClassView):
    _cls = Absence
    _urls = ['/api/attendance', '/api/attendance/<lid:int>']

    @user_required()
    async def get(self, _, current_user, lid=None):
        if current_user.admin and lid:
            # TODO: Move to stats
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


# noinspection PyBroadException, PyMethodMayBeStatic
class AbsenceConfirmation(HTTPModelClassView):
    _cls = Users
    _urls = ['/api/workshopabsence', '/api/workshopabsence/<uid>/<rhash>/<answer>']

    async def get(self, _, uid, rhash, answer):
        try:
            user = await Users.get_by_id(int(uid))
            uhash = hash_string(user.name + str(user.id) + user.email)
            if not user.accepted:
                logging.error('{} was trying to hack us'.format(user.email))
                return json({'msg': 'Nice try! But nope.'})
            if user.confirmation != 'noans':
                return json({
                    'msg': 'Sorry, it is not possible to change your mind now'
                })
            if uhash == rhash:
                if answer == 'yes':
                    user.confirmation = 'ack'
                    await user.update()
                    return json({'msg': 'Widzimy się w Sobotę 23.09.2017!'})
                elif answer == 'no':
                    user.confirmation = 'rej_user'
                    await user.update()
                    return json({'msg': 'Szkoda, że się już nie zobaczymy'})
            else:
                return json({'msg': 'wrong hash'})
        except:
            logging.exception('AbsenceConfirmation')
            return json({'msg': 'wrong data'})

    @user_required()
    async def post(self, request, current_user):
        answer = request.json.get('answer')
        if not current_user.accepted:
            logging.error('{} was trying to hack us'.format(current_user.email))
            return json({'msg': 'Nice try but nope'})
        if current_user.confirmation != 'noans':
            return json({
                'msg': 'Sorry there is no option to change your mind now'
            })
        if answer == 'yes':
            current_user.confirmation = 'ack'
            await current_user.update()
            return json({
                'success': True,
                'msg': 'Widzmy się w Poniedzialek !'
            })
        elif answer == 'no':
            current_user.confirmation = 'rej_user'
            await current_user.update()
            return json({
                'success': True,
                'msg': 'Szkoda że się już nie zobaczymy'
            })
        else:
            return json({
                'success': False,
                'msg': 'Answer must be yes or no'
            })


class FeedbackView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/feedback'

    @user_required()
    async def get(self, _, current_user, lid=None):
        if lid:
            if lid.isnumeric():
                user = await Users.get_by_id(int(lid))
            elif lid == 'undefined':
                return json({'msg': 'wrong username'}, 404)
            else:
                try:
                    user = await Users.get_first('email', lid)
                except DoesNotExist:
                    logging.error('Wrong e-mail or smth: ' + lid)
            if current_user.id == user.id:
                return json(await user.get_my_user_data())
            return json(await user.get_public_data())
        # else: # TODO finish it
            feedbacks = await Feedback.get_all()
            # user = []
            # for u in users:
            #     if current_user.admin or current_user.organiser:
            #         user.append(await u.to_dict())
            #     else:
            #         user.append(await u.get_public_data())
            # user.sort(key=lambda a: a['id'])
        # return json(user, sort_keys=True)

    @user_required()
    async def post(self, _, current_user, lid=None):
        pass


