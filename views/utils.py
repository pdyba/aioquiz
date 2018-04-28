#!/usr/bin/env python3.5
# encoding: utf-8
from functools import wraps
import logging
from abc import abstractproperty

from sanic.response import json
from sanic.views import HTTPMethodView

from models import Users

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
        async def func_wrapper(self, *args, **kwargs):
            if access_level != 'no_user':
                global _users
                resp = json({'msg': msg}, status=code)
                authorization = args[0].headers.get('authorization')
                if not authorization:
                    return resp
                user = _users.get(authorization) or await Users.get_user_by_session_uuid(authorization)
                _users[authorization] = user
                if not user:
                    return resp
                if access_level != 'any_user' and not getattr(user, access_level):
                    return resp
            else:
                user = None
            # below has to be that way as append does not return anything ;)
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


# noinspection PyMethodMayBeStatic,PyUnusedLocal
class HTTPModelClassView(HTTPMethodView):
    _cls = None

    @abstractproperty
    def _urls(self):
        pass

    @classmethod
    def _get_name(cls):
        return cls.__name__

    @user_required(access_level='no_user')
    async def get(self, request, current_user, an_id=None):
        if an_id:
            an_model = await self._cls.get_by_id(an_id)
            q = await an_model.to_dict()
            return json(q)
        else:
            an_model = await self._cls.get_all()
            models = []
            for quiz in an_model:
                models.append(await quiz.to_dict())
            return json(models)

    @user_required(access_level='no_user')
    async def post(self, request, current_user):
        try:
            req = request.json
            model = self._cls(**req)
            await model.create()
            return json({'success': True})
        except:
            logging.exception('err {}.post'.format(self._get_name()))
        return json({'msg': 'error creating'}, status=500)

    @user_required(access_level='no_user')
    async def delete(self, request, current_user, an_id=None):
        model = await self._cls.get_by_id(an_id)
        await model.delete()
        return json({
            'success': True,
            'msg': 'Deleted successfully'
        })

    @user_required(access_level='no_user')
    async def put(self, request, current_user, an_id=None):
        req = request.json
        model = await self._cls.get_by_id(an_id)
        await model.update_from_dict(req)
        return json({
            'success': True,
            'msg': 'Deleted successfully'
        })
