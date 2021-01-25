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

from views.utils import get_user_name
from views.utils import MCV

from models import Absence
from models import ExerciseAnswer
from models import Feedback
from models import Lesson
from models import LessonFeedbackAnswer
from models import QuizAnswer
from models import Seat
from models import UserReview


# noinspection PyBroadException
class UserView(MCV):
    _cls = Users
    _urls = ['/api/users/', '/api/users/<id_name>']
    access_level = {'post': 'no_user'}
    access_level_default = 'any_user'

    async def get(self, id_name=None):
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
            if self.current_user.id == user.id:
                return json(await user.get_my_user_data())
            return json(await user.get_public_data())
        else:
            sort_by = 'id'
            if self.req.args:
                if 'sort_by' in self.req.args:
                    sort_by = self.req.args['sort_by'][0]
                    del self.req.args['sort_by']
                users = await Users.get_by_many_field_value(**get_args(self.req.args))
            else:
                users = await Users.get_all()
            user = []
            for u in users:
                if self.current_user.admin or self.current_user.organiser:
                    user.append(await u.to_dict())
                else:
                    user.append(await u.get_public_data())
            user.sort(key=lambda a: a[sort_by])
        return json(user, sort_keys=True)

    async def put(self):
        try:
            req = self.req.json
            if 'admin' in req:
                del req['admin']
            await self.current_user.update_from_dict(req)
            return json({
                'success': True,
                'msg': 'Update successful'
            })
        except:
            logging.exception('err users.put')
            return json({'msg': 'Update Failed'}, status=500)

    async def post(self):
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
            req = self.req.json
            if 'admin' in req:
                del req['admin']
            user = Users(**req)
            user.session_uuid = create_uuid()
            user.active = True
            uid = await user.create()
            if not isinstance(uid, int):
                usr = Users.get_first('session_uuid', user.session_uuid)
            return json({
                'success': True,
                'msg': 'Check Your e-mail for activation link!'
            })
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

    async def delete(self, id_name=None):
        if isinstance(id_name, str) and id_name.isnumeric():
            id_name = int(id_name)
        if not self.current_user.admin and self.current_user.id != id_name:
            return json({'success': False, 'msg': 'Unauthorised'})
        user = await Users.get_by_id(id_name)
        user.name = 'deleted'
        user.img = 'deleted'
        user.linkedin = 'deleted'
        user.twitter = 'deleted'
        user.facebook = 'deleted'
        user.surname = 'deleted'
        user.email = 'deleted@{}'.format(user.id)
        user.active = False
        await user.update()
        return json({'success': True})


class ActivationView(MCV):
    _cls = Users
    _urls = '/api/user/activation/<uid:int>/<acode>'
    access_level_default = 'no_user'

    async def get(self, uid, acode):
        user = await Users.get_by_id(uid)
        if user and user.session_uuid == acode:
            user.active = True
            await user.update()
            return redirect('/#/regconfirmed')
        return json({'success': False, 'msg': 'wrong token'})


class INeedHelpView(MCV):
    _cls = Users
    _urls = ['/api/user/i_need_help']

    async def get(self):
        try:
            seats = await Seat.get_first('users', self.current_user.id)
            seats.i_need_help = True
            await seats.update()
            self.current_user.i_needed_help += 1
            await self.current_user.update()
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
 
    async def delete(self):
        try:
            seats = await Seat.get_first('users', self.current_user.id)
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


class SeatView(MCV):
    _cls = None
    _urls = ['/api/seats', '/api/seats/<uid:int>']

    async def get(self, uid=None):
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

    async def post(self):
        req = self.req.json
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

    async def delete(self):
        seat = await Seat.get_first('users', self.current_user.id)
        await seat.delete()
        return json(
            {
                'success': True,
                'msg': 'Seat taken'
            },
            sort_keys=True
        )


# noinspection PyMethodMayBeStatic
class ForgotPasswordView(MCV):
    _cls = Users
    _urls = '/api/user/password_forgot'
    access_level_default = 'no_user'

    # noinspection PyUnusedLocal
    async def post(self):
        # noinspection PyBroadException
        try:
            req = self.req.json
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
class ChangePasswordView(MCV):
    _cls = Users
    _urls = '/api/user/password_change'

    # noinspection PyMethodOverriding
    async def post(self):
        try:
            req = self.req.json
            validation_outcome = await self.current_user.validate_password(req['new_password'])
            if not validation_outcome['success']:
                return json(validation_outcome)
            if hash_string(req.get('password', 'x')) == self.current_user.password:
                if req['new_password'] == req['new_password_2']:
                    await self.current_user.set_password(req['new_password'])
                    await self.current_user.update()
                    return json({"success": True, "msg": "You have successfully changed your password"})
                return json({"success": False, "msg": "You provided different new password"})
            return json({"success": False, "msg": "You provided wrong old password"})
        except:
            logging.exception('authentication.post')
        return json({'msg': 'Sorry, internal error. Please let us now!', "success": False})


# noinspection PyMethodMayBeStatic
class SaveGDPR(MCV):
    """
    Saves GDPR/RODO FFS...
    """
    _cls = Users
    _urls = '/api/user/gdpr'
    failed_msg = """You have failed to comply with our Privacy Policy. 
        You will be automatically logged out. 
        Failing to comply by 25.05.2018 will lead to account removal."""

    async def get(self, request, current_user):
        # noinspection PyBroadException
        try:
            self.current_user.gdpr = True
            await self.current_user.update()
            return json({
                'success': True,
                'msg': 'You confirmed reading and agreed with our Privacy Policy'
            })
        except:
            logging.exception('err user.post')
        return json({
            'success': False,
            'msg': self.failed_msg
        })