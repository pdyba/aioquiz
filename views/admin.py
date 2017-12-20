# !/usr/bin/python3.5
import asyncio
import logging

from sanic.response import json

from config import ALL_EMAILS
from config import MAINCONFIG
from utils import send_email
from utils import hash_string

from views.utils import user_required
from views.utils import HTTPModelClassView
from models import Users
from models import Config


class EmailView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/email'

    recipients = {
        'all': 'Do Wszystkich',
        'accepted': 'Do Zakcpetowanych',
        'ack': 'Do Zakcpetowanych, ktorzy przyjeli',
        'noans': 'Do Zakcpetowanych, ktorzy jeszcze przyjeli - przypomnienie',
        'rejected': 'Do tych co odrzucili',
        'not_accpeted': 'Do tych ktorzy nie zostali zakceptowaniu - druga runda',
        'organiser': 'Do organizatorów',
        'mentor': 'Do mentorów',
    }

    @user_required('admin')
    async def get(self, request, current_user):
        resp = {
            'recipients': self.recipients,
            'possible_emails': ALL_EMAILS
        }
        return json(resp)

    @user_required('admin')
    async def post(self, request, current_user):
        req = request.json
        link = 'https://{}/api/workshopabsence/'.format(request.host)
        if req['email_type'] == 'EmailCustom':
            users = await Users.get_by_many_field_value(**req['recipients'])
            subject = req['subject']
            text = req['text'].format()
            await send_email(
                recipients=[u.email for u in users],
                text=text,
                subject=subject
            )
        elif req['email_type'] == 'EmailTooLate':
            users = await Users.get_by_many_field_value(**req['recipients'])
            for user in users:
                user.confirmation = 'rej_time'
                await user.update()
                email_data = {
                    "name": user.name
                }
                subject = req['subject']
                text = req['text'].format(**email_data)
                await send_email(
                    recipients=[user.email],
                    text=text,
                    subject=subject
                )
                await asyncio.sleep(0.05)
        elif req['email_type'] == "per_user":
            users = await Users.get_by_many_field_value(**req['recipients'])
            for user in users:
                uhash = hash_string(user.name + str(user.id) + user.email)
                email_data = {
                    "link_yes": link + str(user.id) + '/' + uhash + '/' + 'yes',
                    "link_no": link + str(user.id) + '/' + uhash + '/' + 'no',
                    "name": user.name,
                    "what_can_you_bring": user.what_can_you_bring
                }
                subject = req['subject']
                text = req['text'].format(email_data)
                await send_email(
                    recipients=user.email,
                    text=text,
                    subject=subject
                )
        else:
            users = await Users.get_by_many_field_value(**req['recipients'])
            recip = []
            for user in users:
                recip.append(user.email)
            subject = req['subject']
            text = req['text']
            await send_email(
                recipients=recip,
                text=text,
                subject=subject
            )
        return json({'success': True, 'count': len(users)})


class UserStatsView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/users_stats'

    @user_required('admin')
    async def get(self, _, current_user):
        resp = {
            'all': await Users.count_all(),
            'mentors': await Users.count_by_field(
                mentor=True,
                organiser=False,
                admin=False
            ),
            'atendees': await Users.count_by_field(
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


class ReviewRulesView(HTTPModelClassView):
    _urls = '/api/review_rules'

    @user_required('organiser')
    async def get(self, _, current_user):
        rules = [x.strip() for x in MAINCONFIG.CIRITERIA.split('\n') if x]
        return json(rules)


class ConfigView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/i_need_help'

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


# noinspection PyMethodMayBeStatic
class RegistrationActiveView(HTTPModelClassView):
    _urls = '/api/reg_active'

    async def get(self, _):
        return json({'registration': await Config.get_registration()})

