# !/usr/bin/python3.5
from datetime import datetime
import logging

from sanic.response import json

from orm import DoesNotExist
from views.utils import user_required
from views.utils import HTTPModelClassView
from models import Users

from utils import hash_string
from utils import send_email
from utils import create_uuid

_users = {}


# noinspection PyBroadException PyMethodMayBeStatic
class AuthenticateView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/authenticate'

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


# noinspection PyMethodMayBeStatic
class MagicAuthenticateView(HTTPModelClassView):
    _cls = Users
    _urls = [
        '/api/magic_link',
        '/api/magic_link/<magic_string>'
    ]

    user_error = json(
        {'success': False, 'msg': 'Wrong user name or password'},
    )

    async def get(self, request, magic_string=''):
        if not magic_string or len(magic_string) < 32:
            return json(
                {'success': False, 'msg': 'Invalid Magic Link'},
            )
        try:
            user = await Users.get_first('magic_string', magic_string)
        except DoesNotExist:
            return json(
                {'success': False, 'msg': 'Wrong Magic Link'},
            )
        if (datetime.utcnow() - user.magic_string_date).total_seconds() > 300:
            return json(
                {'success': False, 'msg': 'Link is only active for 5 minutes.'},
            )
        user.magic_string = " "
        user.session_uuid = create_uuid()
        user.last_login = datetime.utcnow()
        await user.update()
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
            http_s = request.scheme
            try:
                user = await Users.get_first_by_many_field_value(email=req.get('email'))
            except DoesNotExist:
                return json({'msg': 'wrong email or user does not exists'})
            await user.set_magic_string()
            await user.update()
            magic_link = """
            Click on the link to login:

            {http_s}://{server}/#/magic_link?ml={mlink}
            """.format(
                http_s=http_s,
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


# noinspection PyMethodMayBeStatic
class ForgotPasswordView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/forgot_password'

    # noinspection PyUnusedLocal
    async def post(self, request):
        # noinspection PyBroadException
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


# noinspection PyMethodMayBeStatic
class AdminForgotPasswordView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/admin_forgot_password/<email>'

    # noinspection PyUnusedLocal
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


# noinspection PyBroadException PyMethodMayBeStatic
class ChangePasswordView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/change_password'

    # noinspection PyMethodOverriding
    @user_required()
    async def post(self, request, current_user):
        try:
            req = request.json
            if hash_string(req.get('password', 'x')) == current_user.password:
                if req['new_password'] == req['new_password_2']:
                    await current_user.set_password(req['new_password'])
                    await current_user.update()
                    return json({"success": True, "msg": "You have successfully changed password"})
                return json({"success": False, "msg": "You provided different new passwords"})
            return json({"success": False, "msg": "You provided wrong old password"})
        except:
            logging.exception('authentication.post')
        return json({'msg': 'Sorry, internal error. Please let us now!', "success": False})


# noinspection PyMethodMayBeStatic
class LogOutView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/logout'

    # noinspection PyUnusedLocal, PyMethodOverriding
    @user_required()
    async def post(self, request, current_user):
        if current_user:
            current_user.session_uuid = ''
            await current_user.update()
            return json({'success': True})
        return json({'success': False}, status=403)
