#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from views.utils import MCV
from models import User


class UserStatsView(MCV):
    _cls = User
    _urls = '/api/users_stats'
    access_level_default = 'admin'

    async def get(self):
        resp = {
            'all': await User.count_all(),
            'mentors': await User.count_by_field(
                mentor=True,
                organiser=False,
                admin=False
            ),
            'attendees': await User.count_by_field(
                mentor=False,
                organiser=False
            ),
            'organisers': await User.count_by_field(
                organiser=True,
                admin=False
            ),
            'admins': await User.count_by_field(admin=True),
            'attendee_accepted': await User.count_by_field(
                accepted=True,
                mentor=False)
            ,
            'attendee_confirmed': await User.count_by_field(
                confirmation='ack',
                mentor=False,
                accepted=True
            ),
            'attendee_noans_accepted': await User.count_by_field(
                confirmation='noans',
                mentor=False,
                accepted=True
            ),
            'attendee_rej_user': await User.count_by_field(
                confirmation='rej_user',
                mentor=False,
                accepted=True
            ),
            'attendee_rej_time': await User.count_by_field(
                confirmation='rej_time',
                mentor=False,
                accepted=True
            ),
        }
        return json(resp, sort_keys=True)
