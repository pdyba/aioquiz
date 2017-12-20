#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from views.utils import HTTPModelClassView
from models import Config


# noinspection PyMethodMayBeStatic
class RegistrationActiveView(HTTPModelClassView):
    _urls = '/api/reg_active'

    async def get(self, _):
        return json({'registration': await Config.get_registration()})
