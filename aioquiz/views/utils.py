#!/usr/bin/env python3.5
# encoding: utf-8
from functools import wraps
import logging

from sanic.response import json
from sanic.views import HTTPMethodView

from models import User

_users = {}
_users_names = {}


def user_required(access_level='any_user', msg='NOT AUTHORISED', code=401):
    """
    no_user - anonymus
    any_user - loged user
    mentor
    organiser
    admin
    :param code: int
    :param msg: str
    :param access_level:
    :return: wrapped_function
    """
    def decorator(func):
        @wraps(func)
        async def func_wrapper(cls, *args, **kwargs):
            global _users
            resp = json({'msg': msg}, status=code)
            try:
                req = args[0]
            except IndexError:
                print(cls)
            authorization = req.headers.get('authorization')
            al = cls.access_level.get(req.method.lower(), cls.access_level_default) or access_level
            if al == 'no_user' and not authorization:
                user = None
            elif not authorization:
                return resp
            else:
                user = _users.get(authorization) or await User.get_user_by_session_uuid(authorization)
                _users[authorization] = user
                if not user and al != 'no_user':
                    return resp
                if al not in ['any_user', 'no_user'] and not getattr(user, al):
                    return resp
            cls.current_user = user
            return await func(cls, *args, **kwargs)
        return func_wrapper
    return decorator


async def get_user_name(uid):
    if uid not in _users_names:
        user = await User.get(uid)
        _users_names[uid] = '{} {}'.format(user.name, user.surname)
    return _users_names[uid]


# noinspection PyMethodMayBeStatic,PyUnusedLocal
class MCV(HTTPMethodView):
    """
    MCV - ModelClassView
    """
    _cls = None
    req = None
    current_user = None
    access_level = {}
    access_level_default = 'any_user'

    @property
    def _urls(self):
        pass

    @classmethod
    def _get_name(cls):
        return cls.__name__

    @user_required()
    def dispatch_request(self, request, *args, **kwargs):
        self.req = request
        handler = getattr(self, request.method.lower(), None)
        return handler(*args, **kwargs)

    async def _get(self, an_id=None):
        if an_id:
            an_model = await self._cls.get(an_id)
            q = await an_model.to_dict()
            return q
        an_model = await self._cls.get_all()
        models = []
        for mod in an_model:
            models.append(await mod.to_dict())
        return models

    async def get(self, an_id=None):
        return json(await self._get(an_id))

    async def _post(self, an_id=None):
        model = self._cls(**self.req.json)
        await model.create()

    async def post(self):
        try:
            await self._post()
            return json({'success': True})
        except:
            logging.exception('err {}.post'.format(self._get_name()))
        return json({'msg': 'error creating'}, status=500)

    async def _delete(self, an_id=None):
        model = await self._cls.get(an_id)
        await model.delete()

    async def delete(self, an_id=None):
        await self._delete(an_id)
        return json({
            'success': True,
            'msg': 'Deleted successfully'
        })

    async def _put(self, an_id=None):
        model = await self._cls.get(an_id)
        await model.update_from_dict(self.req.json)

    async def put(self, an_id=None):
        await self._put(an_id)
        return json({
            'success': True,
            'msg': 'Updated successfully'
        })


class AdminMCV(MCV):
    access_level_default = 'admin'


class OrganiserMCV(MCV):
    access_level_default = 'organiser'


class MentorMCV(MCV):
    access_level_default = 'mentor'
