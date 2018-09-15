#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from views.utils import MCV
from models import Config


# noinspection PyMethodMayBeStatic
class RegistrationActiveView(MCV):
    _urls = '/api/status/config/registration'

    async def _get(self, an_id=None):
        return {'registration': await Config.get_registration()}
