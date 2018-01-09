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
        'all': 'Do Wszystkich',
        'accepted': 'Do Zakcpetowanych',
        'ack': 'Do Zakcpetowanych, ktorzy przyjeli',
        'noans': 'Do Zakcpetowanych, ktorzy jeszcze przyjeli - przypomnienie',
        'rejected': 'Do tych co odrzucili',
        'not_accepted': 'Do tych ktorzy nie zostali zaakceptowani - druga runda',
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
