#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from models import Users
from models.event import Event
from models.event import Sponsor
from utils import hash_string

from views.utils import user_required
from views.utils import HTTPModelClassView


# noinspection PyBroadException, PyMethodMayBeStatic
class EventAttendenceConfirmation(HTTPModelClassView):
    _cls = Users
    _urls = ['/api/event/absence', '/api/event/absence/<uid>/<rhash>/<answer>']

    @user_required('no_user')
    async def get(self, _, current_user, uid, rhash, answer):
        try:
            user = await Users.get_by_id(int(uid))
            uhash = hash_string(user.name + str(user.id) + user.email)
            if not user.accepted:
                logging.error('{} was trying to hack us'.format(user.email))
                return json({'msg': 'Nice try! But nope.'})
            if user.confirmation != 'noans':
                return json({
                    'msg': 'Sorry, it is not possible to change your mind now'
                })
            if uhash == rhash:
                if answer == 'yes':
                    user.confirmation = 'ack'
                    await user.update()
                    return json({'msg': 'Widzimy się w Sobotę 23.09.2017!'})
                elif answer == 'no':
                    user.confirmation = 'rej_user'
                    await user.update()
                    return json({'msg': 'Szkoda, że się już nie zobaczymy'})
            else:
                return json({'msg': 'wrong hash'})
        except:
            logging.exception('AbsenceConfirmation')
            return json({'msg': 'wrong data'})

    @user_required()
    async def post(self, request, current_user):
        answer = request.json.get('answer')
        if not current_user.accepted:
            logging.error('{} was trying to hack us'.format(current_user.email))
            return json({'msg': 'Nice try but nope'})
        if current_user.confirmation != 'noans':
            return json({
                'msg': 'Sorry there is no option to change your mind now'
            })
        if answer == 'yes':
            current_user.confirmation = 'ack'
            await current_user.update()
            return json({
                'success': True,
                'msg': 'Widzmy się w Poniedzialek !'
            })
        elif answer == 'no':
            current_user.confirmation = 'rej_user'
            await current_user.update()
            return json({
                'success': True,
                'msg': 'Szkoda że się już nie zobaczymy'
            })
        else:
            return json({
                'success': False,
                'msg': 'Answer must be yes or no'
            })


class EventView(HTTPModelClassView):
    _cls = Event
    _urls = ['/api/event', '/api/event/<uid>']


class SponsorView(HTTPModelClassView):
    _cls = Sponsor
    _urls = ['/api/sponsor', '/api/sponsor/<uid>']
