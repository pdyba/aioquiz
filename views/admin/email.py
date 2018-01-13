#!/usr/bin/env python3.5
# encoding: utf-8
import asyncio

from sanic.response import json

from config import ALL_EMAILS
from utils import send_email
from utils import hash_string

from views.utils import user_required
from views.utils import HTTPModelClassView
from models import Users


class EmailView(HTTPModelClassView):
    _cls = Users
    _urls = '/api/admin/email'

    recipients = {
        'all' : {
            'type': 'all',
            'name': 'Do Wszystkich',
            'conditions': {}
        },
        'accepted': {
            'type': 'accepted',
            'name': 'Do Zaakceptowanych',
            'conditions': {
                'accepted': True, 'organiser': False, 'mentor': False, 'admin': False
            }
         },
        'accepted_noans': {
            'type': 'accepted_noans',
            'name': 'Do zaakceptowanych, którzy jeszcze nie potwierdzili - przypomnienie',
            'conditions': {
                'accepted': True,
                'confirmation': 'noans',
                'organiser': False,
                'mentor': False,
                'admin': False
            }
        },
        'confirmed': {
            'type': 'confirmed',
            'name': 'Do zaakceptowanych, którzy potwierdzili swój udział',
            'conditions': {
                'accepted': True,
                'confirmation': 'ack',
                'organiser': False,
                'mentor': False,
                'admin': False
            }
        },
        'rejected': {
            'type': 'rejected',
            'name': 'Do tych, co odrzucili',
            'conditions': {
                'accepted': False,
                'organiser': False,
                'mentor': False,
                'admin': False
            }
        },
        'not_accepted': {
            'type': 'not_accepted',
            'name': 'Do tych którzy nie zostali zaakceptowani',
            'conditions': {'accepted': False, 'organiser': False, 'mentor': False, 'admin': False},

        },
        'admin': {
            'type': 'admin',
            'name': 'Do Adminów',
            'conditions': {'admin': True},
        },
        'organiser': {
            'type': 'organiser',
            'name': 'Do organizatorów',
            'conditions': {'organiser': True},
        },
        'mentor': {
            'type': 'mentor',
            'name': 'Do mentorów',
            'conditions': {'mentor': True},
        },
    }

    @user_required('admin')
    async def get(self, request, current_user, **kwargs):
        resp = {
            'recipients': self.recipients,
            'possible_emails': ALL_EMAILS
        }
        return json(resp)

    @user_required('admin')
    async def post(self, request, current_user):
        data = request.json
        mail_data = data['mail']
        users = await Users.get_by_many_field_value(**data['recipients']['conditions'])
        if mail_data['per_user']:
            for user in users:
                if mail_data['email_type'] == 'EmailTooLate':
                    user.confirmation = 'rej_time'
                    await user.update()
                    email_data = {
                        "name": user.name
                    }
                else:
                    link = 'https://{}/api/event/absence/{}/{}/'.format(
                        request.host,
                        str(user.id),
                        hash_string(user.name + str(user.id) + user.email)
                    )
                    email_data = {
                        "link_yes": link + 'yes',
                        "link_no": link + 'no',
                        "name": user.name,
                        "what_can_you_bring": user.what_can_you_bring
                    }
                subject = mail_data['subject']
                text = mail_data['text'].format(**email_data)
                await send_email(
                    recipients=[user.email],
                    text=text,
                    subject=subject
                )
                await asyncio.sleep(0.03)
        else:
            subject = mail_data['subject']
            text = mail_data['text']
            await send_email(
                recipients=[u.email for u in users],
                text=text,
                subject=subject
            )
        return json({
            'success': True,
            'msg': "Send: {} e-mail to {}".format(len(users), data['recipients']['name'])
        })
