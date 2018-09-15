#!/usr/bin/env python3.5
# encoding: utf-8
from datetime import datetime
import logging

from sanic.response import json

import config
from orm import DoesNotExist
from views.utils import MCV
from models import Users

from utils import hash_string
from utils import send_email
from utils import create_uuid

_users = {}


# noinspection PyBroadException PyMethodMayBeStatic
class AuthenticateView(MCV):
    _cls = Users
    _urls = '/api/auth/login'
    access_level_default = 'no_user'

    user_error = json(
        {'success': False, 'msg': 'Wrong user name or password'},
        status=404
    )

    async def post(self):
        global _users
        try:
            req = self.req.json
            user = await Users.get_first('email', req.get('email', ''))
            if not user:
                return json({'msg': 'User not found'}, status=404)
            if not user.active:
                return json({'msg': 'User not active'}, status=404)
            if hash_string(req.get('password', 'x')) == user.password:
                session_uuid = await user.get_session_uuid()
                _users[session_uuid] = user
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
                    'session_uuid': session_uuid,
                    'confirmation': user.confirmation,
                    'gdpr': user.gdpr,
                })
            else:
                return self.user_error
        except DoesNotExist:
            return self.user_error
        except:
            logging.exception('err authentication.post')
        return json({'msg': 'internal error'}, status=500)


# noinspection PyMethodMayBeStatic
class MagicAuthenticateView(MCV):
    _cls = Users
    _urls = [
        '/api/auth/magic_link',
        '/api/auth/magic_link/<magic_string>'
    ]
    access_level_default = 'no_user'
    
    user_error = json(
        {'success': False, 'msg': 'Wrong user name or password'},
    )

    async def get(self, magic_string=''):
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

    async def post(self):
        try:
            req = self.req.json
            http_s = config.SERVER.SCHEME or self.req.scheme
            try:
                user = await Users.get_first_by_many_field_value(email=req.get('email'))
            except DoesNotExist:
                return json({'msg': 'wrong email or user does not exist'})
            await user.set_magic_string()
            await user.update()
            magic_link = """
            Click on the link to login:

            {http_s}://{server}/#/magic_link?ml={mlink}
            """.format(
                http_s=http_s,
                mlink=user.magic_string,
                server=config.SERVER.NAME or self.req.host
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
class LogOutView(MCV):
    _cls = Users
    _urls = '/api/auth/logout'
    access_level_default = 'no_user'
    
    async def get(self):
        if self.current_user:
            await self.current_user.set_session_uuid('')
            return json({'success': True})
        return json({'success': False}, status=403)
