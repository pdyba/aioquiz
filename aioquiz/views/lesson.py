#!/usr/bin/env python3.5
# encoding: utf-8
from datetime import datetime
from json import loads as jloads
import logging
from uuid import uuid4

from sanic.response import json

from orm import DoesNotExist
from models import Absence
from models import AbsenceMeta
from models import Exercise
from models import ExerciseAnswer
from models import Lesson
from models import LessonFeedbackAnswer
from models import LessonFeedbackMeta
from models import LessonFeedbackQuestion
from models import User

from views.utils import MCV

INVALID_ANSWER = json({'msg': 'Invalid answer provided for the given question type'}, 400)


# noinspection PyBroadException
class LessonView(MCV):
    _cls = Lesson
    _urls = ['/api/lessons', '/api/lessons/<lid:int>']

    
    async def post(self):
        try:
            req = self.req.json
            user = await User.get_first('email', req['creator'])
            req['creator'] = user.id
            lesson = Lesson(**req)
            await lesson.create()
            return json({'success': True})
        except:
            logging.exception('err lesson.post')
            return json({'msg': 'error creating'}, status=500)

    
    async def get(self, lid=None):
        if lid:
            lesson = await Lesson.get(lid)
            return json(await lesson.to_dict())
        else:
            lessons = await Lesson.get_all(suffix="ORDER BY lesson_no")
            resp = []
            for l in lessons:
                resp.append(await l.to_dict())
            resp.sort(key=lambda a: a['lesson_no'])
            return json(resp, sort_keys=True)


# noinspection PyBroadException
class ExercisesView(MCV):
    _cls = Exercise
    _urls = ['/api/exercise', '/api/exercise/<lid:int>']

    
    async def get(self, lid=0):
        if not lid:
            return json({}, 404)
        exercises = await Exercise.get_by_field_value('lesson', lid)
        resp = []
        for ex in exercises:
            q = await ex.to_dict()
            try:
                ans = await ExerciseAnswer.get_first_by_many_field_value(
                    users=self.current_user.id,
                    exercise=ex.id
                )
            except DoesNotExist:
                ans = None
            if ans:
                q['answered'] = True
                q['answer'] = ans.answer
            else:
                q['answered'] = False
            resp.append(q)
        resp.sort(key=lambda a: a['title'])
        return json(resp, sort_keys=True)

    
    async def post(self):
        req = self.req.json
        req['users'] = self.current_user.id
        ex = ExerciseAnswer(**req)
        try:
            await ex.create()
            return json({'success': True, 'msg': 'Exercise answer saved'})
        except:
            logging.exception("ExercisesView.post")
        return json({
            'success': False,
            'msg': 'ERROR: Exercise answer NOT saved'
        })

    
    async def put(self):
        req = self.req.json
        ex = await ExerciseAnswer.get_first_by_many_field_value(
            users=self.current_user.id,
            exercise=req['exercise']
        )
        if not ex.first_answer:
            ex.first_answer = ex.answer
        ex.answer = req['answer']
        try:
            await ex.update(users=self.current_user.id, exercise=req['exercise'])
            return json({'success': True, 'msg': 'Exercise answer saved'})
        except:
            logging.exception("ExercisesView.post")
        return json({
            'success': False,
            'msg': 'ERROR: Exercise answer NOT saved'
        })


class AbsenceManagementView(MCV):
    _cls = Absence
    _urls = ['/api/attendance', '/api/attendance/<lid:int>']
    access_level = {'get': 'admin', 'post': 'admin'}

    async def get(self, lid=None):
        try:
            abmeta = await AbsenceMeta.get_first('lesson', lid)
            resp = await abmeta.to_dict()
            resp['time_ended'] = str(resp['time_ended']).split('.')[0]
            return json(resp)
        except (DoesNotExist, TypeError):
            return await self.generate_code(self.current_user.id, lid)

    
    async def put(self):
        req = self.req.json
        code = req.get('code')
        if not code:
            return json(
                {
                    'success': False,
                    'msg': 'Missing code'
                },
            )
        try:
            abmeta = await AbsenceMeta.get_first('code', code)
        except DoesNotExist:
            return json({'msg': 'Code was wrong', 'success': False})
        if code != abmeta.code:
            return json(
                {
                    'success': False,
                    'msg': 'Wrong code'
                },
            )
        now = datetime.utcnow()
        if now > abmeta.time_ended:
            return json(
                {
                    'success': False,
                    'msg': 'You were too late'
                },
            )
        absence = Absence(lesson=abmeta.lesson, users=self.current_user.id, absent=True)
        await absence.update_or_create('lesson', 'users')
        return json(
            {
                'success': True,
                'msg': 'Attendance accepted'
            },
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

    async def post(self, lid=None):
        abmeta = await AbsenceMeta.get_first('lesson', lid)
        time_ended = datetime.now()
        time_ended = time_ended.replace(minute=time_ended.minute + 2)
        abmeta.time_ended = time_ended
        await abmeta.update()
        resp = await abmeta.to_dict()
        resp['time_ended'] = str(time_ended).split('.')[0]
        return json(resp)


class LessonFeedbackQuestionView(MCV):
    _cls = LessonFeedbackQuestion
    _urls = [
        '/api/feedback/questions',
        '/api/feedback/questions/<qid:int>'
    ]
    access_level_default = 'admin'

    async def get(self, qid=None):
        if qid:
            question = await LessonFeedbackQuestion.get(int(qid))
            return json(question)
        else:
            questions = await LessonFeedbackQuestion.get_all()
            return json(questions)

    async def post(self):
        required_fields = {'type', 'description', 'answers'}
        data = self.req.json
        if set(data.keys()) != required_fields:
            return json({'error': 'Missing required fields'}, 400)

        valid_types = {
            'open', 'abcd_single', 'abcd_multiple', 'int'
        }
        if data['type'] not in valid_types:
            return json({'error': 'Invalid question type'}, 400)

        if data['type'] in ['abcd_single', 'abcd_multiple'] and type(jloads(data['answers'])) != list:
            return json({'error': 'Invalid answers provided (should be a list)'}, 400)

        data.update({'author': self.current_user.id})

        question = LessonFeedbackQuestion(**data)
        await question.create()
        return json({'msg': 'Feedback question created'}, 200)

    async def put(self, qid):
        available_fields = {'type', 'description', 'answers'}
        data = self.req.json

        if set(data.keys()) - available_fields:
            return json({'error': 'I see what you did there. Not gonna happen.'}, 401)
        try:
            question = await LessonFeedbackQuestion.get_first("id", qid)

            if question.author != self.current_user.id:
                return json({'error': 'I see what you did there. Not gonna happen.'}, 401)

            # TODO: move valid_types to the LessonFeedbackQuestion class as a constant
            valid_types = {
                'open', 'abcd_single', 'abcd_multiple', 'int'
            }
            if data['type'] not in valid_types:
                return json({'error': 'Invalid question type'}, 400)

            if data['type'] in ['abcd_single', 'abcd_multiple'] and type(jloads(data['answers'])) != list:
                return json({'error': 'Invalid answers provided (should be a list)'}, 400)

            await question.update_from_dict(data)
            return json({'msg': 'Question updated successfully'}, 200)
        except DoesNotExist:
            return json({'error': 'There is no question with given id'}, 404)

    async def delete(self, _, current_user, qid):
        try:
            await LessonFeedbackQuestion.get_first("id", qid)
            await LessonFeedbackQuestion.detele_by_id(qid)

            return json({}, 204)
        except DoesNotExist:
            return json({'error': 'There is no question with given id'}, 404)


class LessonFeedbackMetaView(MCV):
    _urls = [
        '/api/feedback/questions/<qid:int>/meta/<lid:int>',
        '/api/feedback/questions_for_lesson/<lid:int>'  #TODO: questions_for_lesson rethink that in future
    ]
    access_level = {'get': 'any_user'}
    access_level_default = 'admin'
    
    async def get(self, lid):
        try:
            await Lesson.get_first("id", lid)
            questions = await LessonFeedbackQuestion.get_by_lesson_id(lid)

            return json(questions)
        except DoesNotExist:
            return json({'error': 'A lesson with given id does not exist'}, 404)

    async def post(self, qid, lid):
        try:
            await LessonFeedbackQuestion.get_first("id", qid)
        except DoesNotExist:
            return json({'error': 'A question with given id does not exist'}, 400)

        try:
            await Lesson.get_first("id", lid)
        except DoesNotExist:
            return json({'error': 'A lesson with given id does not exist'}, 400)

        meta = LessonFeedbackMeta(question=qid, lesson=lid)
        await meta.create()

        return json({'msg': 'Feedback association created successfully'}, 200)

    async def delete(self, qid, lid):
        try:
            # doing this twice since delete() could throw a weird out of bounds exc.
            await LessonFeedbackMeta.get_first_by_many_field_value(
                question=qid,
                lesson=lid
            )
            await LessonFeedbackMeta.delete_by_many_fields(
                question=qid,
                lesson=lid
            )
            return json({}, 204)
        except DoesNotExist:
            return json({'error': 'No association with given constraints exists in the database'}, 404)


class LessonFeedbackAnswerView(MCV):
    _urls = [
        '/api/feedback/answers_for_lesson/<lid:int>', # questions_for_lesson rethink that in future
        '/api/feedback/answers',
        '/api/feedback/answers/<aid:int>'
    ]

    @staticmethod
    async def _validate_answers(data):
        provided_answers = data['answers']
        question = None
        try:
            question = await LessonFeedbackQuestion.get_first("id", data['question'])
        except DoesNotExist:
            return json({'error': 'There is no question with given id'}, 400)

        if question.type == 'abcd_single':
            available_answers = jloads(question.answers)

            if jloads(provided_answers)[0] not in available_answers:
                return INVALID_ANSWER
        elif question.type == 'abcd_multiple':
            available_answers = jloads(question.answers)

            if set(jloads(provided_answers)) - set(available_answers):
                return INVALID_ANSWER
        elif question.type == 'int':
            try:
                int(provided_answers)
            except ValueError:
                return INVALID_ANSWER

    
    async def get(self, lid):
        try:
            await Lesson.get_first("id", lid)
        except DoesNotExist:
            return json({'error': 'There is no lesson with given id'}, 404)

        author = self.current_user.id
        answers = await LessonFeedbackAnswer.get_by_many_field_value(
            author=author,
            lesson=lid
        )

        return json(answers)

    
    async def post(self):
        required_fields = {'answers', 'question', 'lesson'}
        data = self.req.json
        if set(data.keys()) != required_fields:
            return json({'error': 'Missing required field(s)'}, 400)

        response = await LessonFeedbackAnswerView._validate_answers(data)

        if response:
            return response

        data.update({'author': self.current_user.id})

        answer = LessonFeedbackAnswer(**data)
        await answer.create()

        return json({'msg': 'Answer recorded'})

    
    async def put(self, aid):
        available_fields = {'answers', 'question', 'lesson'}
        data = self.req.json
        answer = None
        try:
            answer = await LessonFeedbackAnswer.get_first("id", aid)
            if answer.author != self.current_user.id:
                return json({'error': 'I see what you did there. Not gonna happen.'}, 401)
        except DoesNotExist:
            return json({'error': 'There is no answer with given id'}, 404)
        if set(data.keys()) - available_fields:
            return json({'error': 'Invalid field provided'}, 400)
        response = await LessonFeedbackAnswerView._validate_answers(data)
        if response:
            return response
        await answer.update_from_dict(data)
        return json({'msg': 'Answer updated'})
