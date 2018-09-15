#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from views.utils import MCV
from models import Users


class UserStatsView(MCV):
    _cls = Users
    _urls = '/api/users_stats'
    access_level_default = 'admin'

    async def get(self):
        resp = {
            'all': await Users.count_all(),
            'mentors': await Users.count_by_field(
                mentor=True,
                organiser=False,
                admin=False
            ),
            'attendees': await Users.count_by_field(
                mentor=False,
                organiser=False
            ),
            'organisers': await Users.count_by_field(
                organiser=True,
                admin=False
            ),
            'admins': await Users.count_by_field(admin=True),
            'attendee_accepted': await Users.count_by_field(
                accepted=True,
                mentor=False)
            ,
            'attendee_confirmed': await Users.count_by_field(
                confirmation='ack',
                mentor=False,
                accepted=True
            ),
            'attendee_noans_accepted': await Users.count_by_field(
                confirmation='noans',
                mentor=False,
                accepted=True
            ),
            'attendee_rej_user': await Users.count_by_field(
                confirmation='rej_user',
                mentor=False,
                accepted=True
            ),
            'attendee_rej_time': await Users.count_by_field(
                confirmation='rej_time',
                mentor=False,
                accepted=True
            ),
        }
        return json(resp, sort_keys=True)
