# !/usr/bin/python3.5
from sanic.response import json

from config import MAINCONFIG
from views.utils import user_required
from views.utils import HTTPModelClassView
from models import Config


class ConfigView(HTTPModelClassView):
    _cls = Config
    _urls = '/api/admin/config'

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


class ReviewRulesView(HTTPModelClassView):
    _urls = '/api/admin/review_rules'

    @user_required('admin')
    async def get(self, _, current_user):
        rules = [x.strip() for x in MAINCONFIG.CIRITERIA.split('\n') if x]
        return json(rules)