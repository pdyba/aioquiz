#!/usr/bin/env python3.5
# encoding: utf-8
from collections import defaultdict
import logging

from asyncpg import UniqueViolationError
from sanic.response import json
from sanic.response import redirect

from config import REGEMAIL
from config import SERVER
from orm import DoesNotExist
from models import Users
from models import Config
from utils import get_args, hash_string
from utils import create_uuid
from utils import send_email

from views.utils import user_required
from views.utils import get_user_name
from views.utils import HTTPModelClassView

from models import Absence
from models import ExerciseAnswer
from models import Feedback
from models import Lesson
from models import LessonFeedbackAnswer
from models import QuestionAnswer
from models import Seat
from models import UserReview


# noinspection PyBroadException
class UserView(HTTPModelClassView):
    _cls = Users
    _urls = ['/api/users/', '/api/users/<id_name>']

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
            return json({'msg': 'Update Failed'}, status=500)

    async def post(self, request):
        """
        Registration handling.
        :param request:
        :return:
        """
        if not await Config.get_registration():
            return json(
                {'msg': 'Registration is already closed'},
                status=401
            )
        try:
            req = request.json
            if 'admin' in req:
                del req['admin']
            user = Users(**req)
            user.session_uuid = create_uuid()
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
                    server=SERVER.NAME or request.host
                )
                resp = await send_email(
                    recipients=[user.email],
                    text=text,
                    subject=REGEMAIL.SUBJECT_PL if user.lang == 'pl' else REGEMAIL.SUBJECT_EN,
                )
                if resp:
                    return json({
                        'success': True,
                        'msg': 'Check Your e-mail for activation link!'
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
        for cls in [Lesson, LessonFeedbackAnswer]:
            await cls.delete_by_many_fields(author=id_name)

        # TODO: for question authors, set author=DEFAULT_USER and don't remove them
        for cls in [QuestionAnswer, ExerciseAnswer, Feedback, Absence, Seat]:
            await cls.delete_by_many_fields(users=id_name)

        await Users.detele_by_id(id_name)
        return json({'success': True})


class ActivationView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/user/activation/<uid:int>/<acode>'

    async def get(self, request, uid, acode):
        user = await Users.get_by_id(uid)
        if user and user.session_uuid == acode:
            user.active = True
            await user.update()
            return redirect('/#/regconfirmed')
        return json({'success': False, 'msg': 'wrong token'})


class INeedHelpView(HTTPModelClassView):
    _cls = Users
    _urls = ['/api/user/i_need_help']

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


class SeatView(HTTPModelClassView):
    _cls = None
    _urls = ['/api/seats', '/api/seats/<uid:int>']

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
            empty_row = {'user': False, 'i_need_help': False, 'empty_row': True}
            # TODO: Move to config (empty rows)
            for x in range(config.room_raws):
                raw = chr(65 + x)
                for y in range(config.room_columns):
                    if (y + 1) % 13 == 0:
                        resp[raw][y] = empty_row
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


# noinspection PyMethodMayBeStatic
class ForgotPasswordView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/user/password_forgot'

    # noinspection PyUnusedLocal
    async def post(self, request):
        # noinspection PyBroadException
        try:
            req = request.json
            try:
                user = await Users.get_first_by_many_field_value(email=req.get('email'))
            except DoesNotExist:
                return json({'msg': 'wrong email or user does not exist'})
            password = create_uuid()
            await user.set_password(password)
            await user.update()
            resp = await send_email(
                recipients=[user.email],
                text="Your new PyLove password:\n" + password,
                subject="Your new PyLove password"
            )
            if resp:
                return json({
                    'success': True,
                    'msg': 'Check Your e-mail for new password'
                })
            return json({'success': False, 'msg': 'Error sending e-mail'})
        except:
            logging.exception('err user.post')
        return json({'msg': 'Wrong email or user does not exist'}, status=404)


# noinspection PyBroadException PyMethodMayBeStatic
class ChangePasswordView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/user/password_change'

    # noinspection PyMethodOverriding
    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            validation_outcome = await current_user.validate_password(req['new_password'])
            if not validation_outcome['success']:
                return json(validation_outcome)
            if hash_string(req.get('password', 'x')) == current_user.password:
                if req['new_password'] == req['new_password_2']:
                    await current_user.set_password(req['new_password'])
                    await current_user.update()
                    return json({"success": True, "msg": "You have successfully changed your password"})
                return json({"success": False, "msg": "You provided different new password"})
            return json({"success": False, "msg": "You provided wrong old password"})
        except:
            logging.exception('authentication.post')
        return json({'msg': 'Sorry, internal error. Please let us now!', "success": False})


# noinspection PyMethodMayBeStatic
class SaveGDPR(HTTPModelClassView):
    """
    Saves GDPR/RODO FFS...
    """
    _cls = Users
    _urls = '/api/user/gdpr'

    @user_required()
    async def get(self, request, current_user):
        # noinspection PyBroadException
        try:
            current_user.gdpr = True
            await current_user.update()
            return json({
                'success': True,
                'msg': 'You confirmed reading and agreeing with our Privacy Policy'
            })
        except:
            logging.exception('err user.post')
        return json({
            'success': False,
            'msg': 'You Failed to comply with our Privacy Policy You will be automaticly logout, failing to comply by 25.05 will lead to account removal'
        })