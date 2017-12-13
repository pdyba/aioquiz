# !/usr/bin/python3.5
import asyncio
from collections import defaultdict
from datetime import datetime
from functools import wraps
from json import dumps as jdumps
import logging

from asyncpg.exceptions import UniqueViolationError

from sanic.response import json
from sanic.response import redirect
from sanic.views import HTTPMethodView

from config import REGEMAIL
from config import MAINCONFIG
from config import ALL_EMAILS
from models import Absence
from models import AbsenceMeta
from models import Config
from models import Exercise
from models import Feedback
from models import Lesson
from models import LessonFeedback
from models import LiveQuiz
from models import LiveQuizAnsware
from models import LiveQuizQuestion
from models import Question
from models import QuestionAnsware
from models import Quiz
from models import QuizQuestions
from models import ExerciseAnsware
from models import UserReview
from models import Users
from models import Seat
from orm import DoesNotExist
from utils import get_args
from utils import hash_string
from utils import send_email
from utils import create_uuid

NOTAUTHRISED = json({'error': 'not allowed'}, status=401)

_users = {}
_users_names = {}


def user_required(access_level=None):
    def decorator(func):
        @wraps(func)
        async def func_wrapper(self, *args, **kwargs):
            global _users
            authorization = args[0].headers.get('authorization')
            if not authorization:
                return NOTAUTHRISED
            user = _users.get(authorization) or await Users.get_user_by_session_uuid(authorization)
            _users[authorization] = user
            if not user:
                return NOTAUTHRISED
            if access_level:
                if not getattr(user, access_level):
                    return NOTAUTHRISED
            args = list(args)
            args.append(user)
            args = tuple(args)
            return await func(self, *args, **kwargs)
        return func_wrapper
    return decorator


async def get_user_name(uid):
    if uid not in _users_names:
        user = await Users.get_by_id(uid)
        _users_names[uid] = '{} {}'.format(user.name, user.surname)
    return _users_names[uid]


# noinspection PyBroadException
class QuestionView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            if req['qtype'] == 'abcd':
                req['answares'] = jdumps(
                    [req['ans_a'], req['ans_b'], req['ans_c'], req['ans_d']]
                )
                del req['ans_a']
                del req['ans_b']
                del req['ans_c']
                del req['ans_d']
            question = Question(**req)
            await question.create()
            return json({'success': True})
        except:
            logging.exception('err question.post')
            return json({}, status=500)

    @user_required()
    async def put(self, request, qid, current_user):
        try:
            req = request.json
            user = await Users.get_first('email', req['reviewer'])
            question = await Question.get_by_id(qid)
            question.reviewer = user.id
            question.active = req['accept']
            await question.update()
            return json({'success': True})
        except:
            logging.exception('err question.update')
            return json({}, status=500)

    @user_required()
    async def get(self, request, current_user, qid=0):
        if qid:
            question = await Question.get_by_id(qid)
            return json(await question.to_dict())
        questions = await Question.get_all()
        resp = []
        for q in questions:
            data = await q.to_dict()
            data['creator'] = await get_user_name(data['users'])
            resp.append(data)
        return json(resp, sort_keys=True)


# noinspection PyBroadException
class UserView(HTTPMethodView):
    @user_required()
    async def get(self, request, current_user, id_name=None):
        if id_name:
            if id_name.isnumeric():
                user = await Users.get_by_id(int(id_name))
            elif id_name == 'undefined':
                return json({'msg': 'wrong username'}, 404)
            else:
                try:
                    user = await Users.get_first('email', id_name)
                except DoesNotExist:
                    logging.error('Wrong e-mail or smth: ' + id_name)
            if current_user.id == user.id:
                return json(await user.get_my_user_data())
            return json(await user.get_public_data())
        else:
            sort_by = 'id'
            if request.args:
                if 'sort_by' in request.args:
                    sort_by = request.args['sort_by'][0]
                    del request.args['sort_by']
                users = await Users.get_by_many_field_value(**get_args(request.args))
            else:
                users = await Users.get_all()
            user = []
            for u in users:
                if current_user.admin or current_user.organiser:
                    user.append(await u.to_dict())
                else:
                    user.append(await u.get_public_data())
            user.sort(key=lambda a: a[sort_by])
        return json(user, sort_keys=True)

    @user_required()
    async def put(self, request, current_user):
        try:
            req = request.json
            if 'admin' in req:
                del req['admin']
            await current_user.update_from_dict(req)
            return json({
                'success': True,
                'msg': 'Update successful'
            })
        except:
            logging.exception('err users.put')
            return json({}, status=500)

    async def post(self, request):
        """
        Registration handling.
        :param request:
        :return:
        """
        if not await Config.get_registration():
            return json(
                {'msg': 'Registartion is already closed'},
                status=401
            )
        try:
            req = request.json
            if 'admin' in req:
                del req['admin']
            user = Users(**req)
            user.session_uuid = create_uuid
            uid = await user.create()
            if not isinstance(uid, int):
                usr = Users.get_first('session_uuid', user.session_uuid)
                uid = usr.id
            if uid:
                text = REGEMAIL.TEXT_PL if user.lang == 'pl' else REGEMAIL.TEXT_EN
                text = text.format(
                        acode=user.session_uuid,
                        uid=uid,
                        name=user.name,
                        server=request.host
                )
                resp = await send_email(
                    recipients=[user.email],
                    text=text,
                    subject=REGEMAIL.SUBJECT_PL if user.lang == 'pl' else REGEMAIL.SUBJECT_EN,
                )
                if resp:
                    return json({
                        'success': True
                    })
                return json({'success': False, 'msg': 'error sending e-mail'})
        except DeprecationWarning:
            return json(
                {'msg': 'You probably used one of banned chars like ;'},
                status=500
            )
        except UniqueViolationError:
            return json(
                {'msg': 'You already registered, try loging in !'},
                status=400
            )
        except:
            logging.exception('err user.post')
        return json({}, status=500)

    @user_required()
    async def delete(self, _, current_user, id_name=None):
        if isinstance(id_name, str) and id_name.isnumeric():
            id_name = int(id_name)
        if not current_user.admin and current_user.id != id_name:
            return json({'success': False, 'msg': 'Unauthorised'})

        await UserReview.delete_by_many_fields(
            reviewer=id_name,
            users=id_name
        )
        await Lesson.delete_by_many_fields(author=id_name)
        
        for cls in [LessonFeedback, QuestionAnsware, ExerciseAnsware, Feedback, Absence, Seat]:
            await cls.delete_by_many_fields(users=id_name)

        await Users.detele_by_id(id_name)
        return json({'success': True})


# noinspection PyBroadException
class QuizManageView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            user = await Users.get_first('email', req['creator'])
            req['users'] = user.id
            questions = [int(q) for q in req['questions']]
            del req['questions']
            quiz = Quiz(**req)
            quiz_id = await quiz.create()
            for i, question in enumerate(questions):
                qq = QuizQuestions(quiz=quiz_id, question=question, question_order=i)
                await qq.create()
            return json({'success': True})
        except:
            logging.exception('err quiz_manage.post')
            return json({}, status=500)


# noinspection PyBroadException
class QuizView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user, qid=0):
        try:
            req = request.json
            qa = QuestionAnsware(
                users=req['user_id'],
                question=req['question'],
                answare=req['answare'],
            )
            await qa.update_or_create('users', 'question')
            quiz = await Quiz.get_by_id(qid)
            question = await quiz.get_question(req['current_question'] + 1)
            if isinstance(question, dict):
                return json(question)
            q = await question.to_dict()
            return json(q, sort_keys=True)
        except:
            logging.exception('err quiz.post')
            return json({}, status=500)

    @user_required()
    async def get(self, _, current_user, qid=0):
        if qid:
            quiz = await Quiz.get_by_id(qid)
            question = await quiz.get_question()
            q = await question.to_dict()
            q['quiz_title'] = quiz.title
            return json(q, sort_keys=True)
        else:
            quizes = await Quiz.get_all()
            resp = []
            for quiz in quizes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                resp.append(q)
            return json(resp, sort_keys=True)


# noinspection PyBroadException
class LiveQuizManageView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            user = await Users.get_first('email', req['creator'])
            req['users'] = user.id
            questions = [int(q) for q in req['questions']]
            del req['questions']
            quiz = LiveQuiz(**req)
            quiz_id = await quiz.create()
            for i, question in enumerate(questions):
                lqq = LiveQuizQuestion(
                    live_quiz=quiz_id,
                    question=question,
                    question_order=i
                )
                await lqq.create()
            return json({'success': True})
        except:
            logging.exception('err quiz_manage.post')
            return json({}, status=500)


# noinspection PyBroadException
class LiveQuizView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user, qid=0):
        try:
            req = request.json
            qa = LiveQuizAnsware(
                live_quiz=qid,
                question=req['question'],
                answare=req['answare'],
            )
            await qa.create()
            live_quiz = await LiveQuiz.get_by_id(qid)
            question = await live_quiz.get_question(req['current_question'] + 1)
            if isinstance(question, dict):
                return json(question)
            q = await question.to_dict()
            return json(q)
        except:
            logging.exception('err live_quiz.post')
            return json({}, status=500)

    @user_required()
    async def get(self, _, current_user, qid=0):
        if qid:
            quiz = await LiveQuiz.get_by_id(qid)
            question = await quiz.get_question()
            q = await question.to_dict()
            q['quiz_title'] = quiz.title
            return json(q)
        else:
            quizes = await LiveQuiz.get_all()
            resp = []
            for quiz in quizes:
                q = await quiz.to_dict()
                q['creator'] = await get_user_name(q['users'])
                q['amount'] = await quiz.get_question_amount()
                resp.append(q)
            return json(resp)


# noinspection PyBroadException
class LessonView(HTTPMethodView):
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
class AuthenticateView(HTTPMethodView):
    user_error = json(
        {'success': False, 'msg': 'Wrong user name or password'},
        status=404
    )

    async def post(self, request):
        global _users
        try:
            req = request.json
            user = await Users.get_first('email', req.get('email', ''))
            if not user:
                return json({'msg': 'User not found'}, status=404)
            if not user.active:
                return json({'msg': 'User not active'}, status=404)
            if hash_string(req.get('password', 'x')) == user.password:
                user.session_uuid = create_uuid()
                user.last_login = datetime.utcnow()
                await user.update()
                _users[user.session_uuid] = user
                return json({
                    'success': True,
                    'admin': user.admin,
                    'mentor': user.mentor,
                    'name': user.name,
                    'email': user.email,
                    'surname': user.surname,
                    'lang': user.lang,
                    'organiser': user.organiser,
                    'id': user.id,
                    'session_uuid': user.session_uuid,
                    'confirmation': user.confirmation
                })
            else:
                return self.user_error
        except DoesNotExist:
            return self.user_error
        except:
            logging.exception('err authentication.post')
        return json({'msg': 'internal error'}, status=500)


class MagicAuthenticateView(HTTPMethodView):
    user_error = json(
        {'success': False, 'msg': 'Wrong user name or password'},
        status=404
    )

    async def get(self, request, magic_string='xxx'):
        try:
            user = await Users.get_first_by_many_field_value(magic_string=magic_string)
        except DoesNotExist:
            return json(
                {'success': False, 'msg': 'Wrong Magic Link'},
                status=404
            )
        return json({
            'success': True,
            'admin': user.admin,
            'mentor': user.mentor,
            'name': user.name,
            'email': user.email,
            'surname': user.surname,
            'lang': user.lang,
            'organiser': user.organiser,
            'id': user.id,
            'session_uuid': user.session_uuid,
            'confirmation': user.confirmation
        })

    async def post(self, request):
        try:
            req = request.json
            try:
                user = await Users.get_first_by_many_field_value(email=req.get('email'))
            except DoesNotExist:
                return json({'msg': 'wrong email or user does not exists'})
            await user.set_magic_string()
            await user.update()
            magic_link = "Click on the link to login: http:\\\\{server}\{mlink}".format(
                    mlink=user.magic_string,
                    server=request.host
            )
            resp = await send_email(
                recipients=[user.email],
                text=magic_link,
                subject="Your PyLove Magic login link"
            )
            if resp:
                return json({
                    'success': True,
                    'msg': 'Check Your e-mail for the link'
                })
            return json({'success': False, 'msg': 'error sending e-mail'})
        except:
            logging.exception('err MagicAuthentication.post')
        return json({'msg': 'internal error'}, status=500)


class ForgotPasswordView(HTTPMethodView):
    async def post(self, request):
        try:
            req = request.json
            try:
                user = await Users.get_first_by_many_field_value(email=req.get('email'))
            except DoesNotExist:
                return json({'msg': 'wrong email or user does not exists'})
            password = create_uuid()
            await user.set_password(password)
            await user.update()
            resp = await send_email(
                recipients=[user.email],
                text=password,
                subject="Your new PyLove password"
            )
            if resp:
                return json({
                    'success': True,
                    'msg': 'Check Your e-mail for new password'
                })
            return json({'success': False, 'msg': 'error sending e-mail'})
        except:
            logging.exception('err user.post')
        return json({'msg': 'wrong email or user does not exists'}, status=404)


class AdminForgotPasswordView(HTTPMethodView):
    @user_required('admin')
    async def get(self, request, current_user, email):
        try:
            user = await Users.get_first_by_many_field_value(email=email)
        except DoesNotExist:
            logging.error(email)
            user = False
        if not user:
            return json({'msg': 'wrong email or user does not exists'})
        password = create_uuid()
        await user.set_password(password)
        await user.update()
        return json({"success": True, "new_pass": password})


# noinspection PyBroadException
class ChangePasswordView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            if hash_string(req.get('password', 'x')) == current_user.password:
                if req['new_password'] == req['new_password_2']:
                    await current_user.set_password(req['new_password'])
                    await current_user.update()
                    return json({"success": True, "msg": "You have Successfully changed password"})
                return json({"success": False, "msg": "You provided different new passwords"})
            return json({"success": False, "msg": "You provided wrong old password"})
        except:
            logging.exception('authentication.post')
        return json({'msg': 'internal error sorry please let us now', "success": False})


class LogOutView(HTTPMethodView):
    @user_required()
    async def post(self, request, current_user):
        if current_user:
            current_user.session_uuid = ''
            await current_user.update()
            return json({'success': True})
        return json({'success': False}, status=403)


class ReviewAttendeesView(HTTPMethodView):
    @user_required('organiser')
    async def get(self, request, current_user):
        allusers = await Users.get_by_many_field_value(
            admin=False,
            organiser=False
        )
        allreviews = await UserReview.get_all()
        reviews = defaultdict(dict)
        for rev in allreviews:
            reviews[rev.users][rev.reviewer] = {
                'score': rev.score,
                'name': await get_user_name(rev.reviewer)
            }
        users = []
        for u in allusers:
            ud = await u.to_dict(include_soft=True)
            ud.update({'reviews': reviews.get(u.id, {})})
            usr = reviews.get(u.id, {})
            review_amount = len(usr) or 1
            ud['score'] = sum([x.get('score', 0) for _, x in usr.items()]) / review_amount
            users.append(ud)
        users.sort(key=lambda a: a['score'], reverse=True)
        return json(users)

    @user_required('organiser')
    async def post(self, request, current_user):
        req = request.json
        req['reviewer'] = current_user.id
        ur = UserReview(**req)
        if not await ur.create():
            return json({'msg': 'already exists', 'error': True})
        all_ur = await UserReview.get_by_field_value('users', req['users'])
        user = await Users.get_by_id(req['users'])
        new_score = sum(u.score for u in all_ur) / (len(all_ur) or 1)
        user.score = new_score
        await user.update()
        return json({'success': True})

    @user_required('organiser')
    async def put(self, request, current_user):
        try:
            req = request.json
            user = await Users.get_by_id(req['users'])
            user.accepted = req['accept']
            await user.update()
            return json({'success': True})
        except:
            logging.exception('review_put')
            return json({'success': False}, status=500)


class EmailView(HTTPMethodView):
    recipients = {
        'all': 'Do Wszystkich',
        'accepted': 'Do Zakcpetowanych',
        'ack': 'Do Zakcpetowanych, ktorzy przyjeli',
        'noans': 'Do Zakcpetowanych, ktorzy jeszcze przyjeli - przypomnienie',
        'rejected': 'Do tych co odrzucili',
        'not_accpeted': 'Do tych ktorzy nie zostali zakceptowaniu - druga runda',
        'organiser': 'Do organizatorów',
        'mentor': 'Do mentorów',
    }

    @user_required('admin')
    async def get(self, request, current_user):
        resp = {
            'recipients': self.recipients,
            'possible_emails': ALL_EMAILS
        }
        return json(resp)

    @user_required('admin')
    async def post(self, request, current_user):
        req = request.json
        link = 'https://{}/api/workshopabsence/'.format(request.host)
        if req['email_type'] == 'EmailCustom':
            users = await Users.get_by_many_field_value(**req['recipients'])
            subject = req['subject']
            text = req['text'].format()
            await send_email(
                recipients=[u.email for u in users],
                text=text,
                subject=subject
            )
        elif req['email_type'] == 'EmailTooLate':
            users = await Users.get_by_many_field_value(**req['recipients'])
            for user in users:
                user.confirmation = 'rej_time'
                await user.update()
                email_data = {
                    "name": user.name
                }
                subject = req['subject']
                text = req['text'].format(**email_data)
                await send_email(
                    recipients=[user.email],
                    text=text,
                    subject=subject
                )
                await asyncio.sleep(0.05)
        elif req['email_type'] == "per_user":
            users = await Users.get_by_many_field_value(**req['recipients'])
            for user in users:
                uhash = hash_string(user.name + str(user.id) + user.email)
                email_data = {
                    "link_yes": link + str(user.id) + '/' + uhash + '/' + 'yes',
                    "link_no": link + str(user.id) + '/' + uhash + '/' + 'no',
                    "name": user.name,
                    "what_can_you_bring": user.what_can_you_bring
                }
                subject = req['subject']
                text = req['text'].format(email_data)
                await send_email(
                    recipients=user.email,
                    text=text,
                    subject=subject
                )
        else:
            users = await Users.get_by_many_field_value(**req['recipients'])
            recip = []
            for user in users:
                recip.append(user.email)
            subject = req['subject']
            text = req['text']
            await send_email(
                recipients=recip,
                text=text,
                subject=subject
            )
        return json({'success': True, 'count': len(users)})


class ActivationView(HTTPMethodView):
    async def get(self, request, uid, acode):
        user = await Users.get_by_id(uid)
        if user and user.session_uuid == acode:
            user.active = True
            await user.update()
            return redirect('/#/regconfirmed')
        return json({'success': False, 'reson': 'wrong token'})


class MakeOrganiserView(HTTPMethodView):
    @user_required('admin')
    async def post(self, request, current_user):
        req = request.json
        user = await Users.get_by_id(req['uid'])
        if user:
            user.organiser = req['organiser']
            await user.update()
            return json({'success': True})
        return json({'success': False, 'reson': 'wrong token'})


class ChangeMentorView(HTTPMethodView):
    @user_required('admin')
    async def post(self, request, current_user):
        req = request.json
        user = await Users.get_by_id(req['uid'])
        if user:
            user.mentor = req['mentor']
            await user.update()
            return json({'success': True})
        return json({'success': False, 'msg': 'wrong token'})


class ChangeActiveView(HTTPMethodView):
    @user_required('admin')
    async def post(self, request, current_user):
        req = request.json
        user = await Users.get_by_id(req['uid'])
        if user:
            user.active = req['active']
            await user.update()
            return json({'success': True})
        return json({'success': False, 'msg': 'wrong token'})


# noinspection PyBroadException
class ExercisesView(HTTPMethodView):
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


class UserStatsView(HTTPMethodView):
    @user_required('admin')
    async def get(self, _, current_user):
        resp = {
            'all': await Users.count_all(),
            'mentors': await Users.count_by_field(
                mentor=True,
                organiser=False,
                admin=False
            ),
            'atendees': await Users.count_by_field(
                mentor=False,
                organiser=False
            ),
            'organisers': await Users.count_by_field(
                organiser=True,
                admin=False
            ),
            'admins': await Users.count_by_field(admin=True),
            'attendee_accepted': await Users.count_by_field(
                accepted=True,
                mentor=False)
            ,
            'attendee_confirmed': await Users.count_by_field(
                confirmation='ack',
                mentor=False,
                accepted=True
            ),
            'attendee_noans_accepted': await Users.count_by_field(
                confirmation='noans',
                mentor=False,
                accepted=True
            ),
            'attendee_rej_user': await Users.count_by_field(
                confirmation='rej_user',
                mentor=False,
                accepted=True
            ),
            'attendee_rej_time': await Users.count_by_field(
                confirmation='rej_time',
                mentor=False,
                accepted=True
            ),
        }
        return json(resp, sort_keys=True)


class ReviewRulesView(HTTPMethodView):
    @user_required('organiser')
    async def get(self, _, current_user):
        rules = [x.strip() for x in MAINCONFIG.CIRITERIA.split('\n') if x]
        return json(rules)


class SeatView(HTTPMethodView):
    @user_required()
    async def get(self, _, current_user, uid=None):
        if uid:
            try:
                seats = await Seat.get_first('users', uid)
                resp = await seats.to_dict()
            except DoesNotExist:
                return json({})
        else:
            seats = await Seat.get_all()
            config = await Config.get_by_id(1)
            used_seats = defaultdict(dict)
            for seat in seats:
                full_user_name = await get_user_name(seat.users)
                used_seats[seat.row][seat.number] = {
                    'user_id': seat.users,
                    'user': full_user_name,
                    'name': full_user_name.split(' ')[0],
                    'i_need_help': seat.i_need_help
                }
            resp = defaultdict(dict)
            empty = {'user': False, 'i_need_help': False}
            empty_raw = {'user': False, 'i_need_help': False, 'empty_raw': True}
            for x in range(config.room_raws):
                raw = chr(65 + x)
                for y in range(config.room_columns):
                    if (y + 1) % 13 == 0:
                        resp[raw][y] = empty_raw
                    else:
                        resp[raw][y] = used_seats.get(raw, empty).get(y, empty)
        return json(resp, sort_keys=True)

    @user_required()
    async def post(self, request, _):
        req = request.json
        try:
            seat = Seat(**req)
            await seat.create()
            return json(
                {
                    'success': True,
                    'msg': 'Seat taken'
                },
                sort_keys=True
            )
        except UniqueViolationError:
            return json(
                {
                    'success': False,
                    'msg': 'You already have taken a seat'
                },
                sort_keys=True
            )

    @user_required()
    async def delete(self, _, current_user):
        seat = await Seat.get_first('users', current_user.id)
        await seat.delete()
        return json(
            {
                'success': True,
                'msg': 'Seat taken'
            },
            sort_keys=True
        )


class INeedHelpView(HTTPMethodView):
    @user_required()
    async def get(self, _, current_user):
        try:
            seats = await Seat.get_first('users', current_user.id)
            seats.i_need_help = True
            await seats.update()
            current_user.i_needed_help += 1
            await current_user.update()
            return json(
                {
                    'success': True,
                    'msg': 'Help is on the way'
                },
            )
        except DoesNotExist:
            return json(
                {
                    'success': False,
                    'msg': 'You need to pick a seat before asking for help'
                },
                sort_keys=True
            )

    @user_required()
    async def delete(self, _, current_user):
        try:
            seats = await Seat.get_first('users', current_user.id)
            seats.i_need_help = False
            await seats.update()
            return json(
                {
                    'success': True,
                    'msg': 'You are welcome'
                },
            )
        except DoesNotExist:
            return json(
                {
                    'success': False,
                    'msg': 'You need to pick a seat before asking for help'
                },
                sort_keys=True
            )


class ConfigView(HTTPMethodView):
    @user_required('admin')
    async def get(self, *_):
        config = await Config.get_by_id(1)
        resp = await config.to_dict()
        return json(resp, sort_keys=True)

    @user_required('admin')
    async def post(self, request, _):
        req = request.json
        try:
            config = await Config.get_by_id(1)
            await config.update_from_dict(req)
        except IndexError:
            config = Config(**req)
            await config.create()
        return json(
            {
                'success': True,
                'msg': 'Config updated'
            },
            sort_keys=True
        )


class AbsenceManagementView(HTTPMethodView):
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


class AbsenceView(HTTPMethodView):
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


# noinspection PyBroadException
class AbsenceConfirmation(HTTPMethodView):
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


class RegistrationActiveView(HTTPMethodView):
    async def get(self, _):
        return json({'registration': await Config.get_registration()})


class FeedbackView(HTTPMethodView):
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


class ExerciseOverview(HTTPMethodView):
    @user_required('mentor')
    async def get(self, _):
        exercises = await Exercise.get_all()
        resp = {}
        for ex in exercises:
            if not resp.get(ex.lesson):
                resp[ex.lesson] = {}
            resp[ex.lesson][ex.id] = await ex.to_dict()
            resp[ex.lesson][ex.id]['exercise_answare'] = await ExerciseAnsware.group_by_field('status', exercise=ex.id)
        return json(resp)
