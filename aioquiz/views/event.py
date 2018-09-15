#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from models import Users
from models.event import Event
from models.event import EventUsers
from models.event import Sponsor
from utils import hash_string

from views.utils import MCV


# noinspection PyBroadException, PyMethodMayBeStatic
class EventAttendenceConfirmation(MCV):
    _cls = Users
    _urls = ['/api/event/absence', '/api/event/absence/<uid>/<rhash>/<answer>']

    async def get(self, uid, rhash, answer):
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

    async def post(self):
        answer = self.req.json.get('answer')
        if not self.current_user.accepted:
            logging.error('{} was trying to hack us'.format(self.current_user.email))
            return json({'msg': 'Nice try but nope'})
        if self.current_user.confirmation != 'noans':
            return json({
                'msg': 'Sorry there is no option to change your mind now'
            })
        if answer == 'yes':
            self.current_user.confirmation = 'ack'
            await self.current_user.update()
            return json({
                'success': True,
                'msg': 'Widzmy się w Poniedzialek !'
            })
        elif answer == 'no':
            self.current_user.confirmation = 'rej_user'
            await self.current_user.update()
            return json({
                'success': True,
                'msg': 'Szkoda że się już nie zobaczymy'
            })
        else:
            return json({
                'success': False,
                'msg': 'Answer must be yes or no'
            })


class EventsView(MCV):
    _cls = Event
    _urls = ['/api/events', '/api/events/<an_id>']

    async def get(self, an_id=None):
        events = await self._get(an_id)
        if not self.current_user:
            return json(events)
        user_events = await EventUsers.get_by_many_field_value(users=self.current_user.id)
        for uev in user_events:
            uev = await uev.to_dict()
            list(filter(lambda a: a.get('id') == uev.get('event'), events))[0].update({'user_data': uev})
        return json(events)


class EventView(MCV):
    _cls = Event
    _urls = ['/api/event', '/api/event/<an_id>']

    async def get(self, an_id=None):
        if not (self.current_user.admin or self.current_user.organiser):
            user_ev = await EventUsers.get_first_by_many_field_value(users=self.current_user.id)
            return json({'context': user_ev.event or 0})
        return await super().get(an_id=an_id)

    async def post(self):
        try:
            req = self.req.json
            model = EventUsers(**req)
            await model.create()
            return json({'success': True, 'msg': 'Signed up!'})
        except:
            logging.exception('err {}.post'.format(self._get_name()))
        return json({'msg': 'error creating'}, status=500)

    async def delete(self, an_id=None):
        try:
            await EventUsers.delete_by_many_fields(users=self.current_user.id, event=an_id)
            return json({'success': True, 'msg': 'Unsigned'})
        except:
            logging.exception('err {}.delete'.format(self._get_name()))
        return json({'msg': 'error deleting'}, status=500)


class SponsorView(MCV):
    _cls = Sponsor
    _urls = ['/api/sponsor', '/api/sponsor/<uid>']

    async def get(self, an_id=None):
        return json(await self._get(an_id=an_id))
