#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from views.utils import AdminMCV
from models import Config


class ConfigView(AdminMCV):
    _cls = Config
    _urls = '/api/admin/config'

    async def get(self):
        config = await Config.get_by_id(1)
        resp = await config.to_dict()
        return json(resp, sort_keys=True , default=str)

    async def post(self):
        req = self.req.json
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
