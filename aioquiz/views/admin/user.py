#!/usr/bin/env python3.5
# encoding: utf-8
from collections import defaultdict
import logging

from sanic.response import json

from models import User
from models import UserReview

from orm import DoesNotExist

from utils import create_uuid

from views.utils import get_user_name
from views.utils import AdminMCV
from views.utils import OrganiserMCV


class SetOrganiserView(AdminMCV):
    _cls = User
    _urls = '/api/admin/user/set_organiser'

    async def post(self):
        req = self.req.json
        user = await User.get(req['uid'])
        if user:
            user.organiser = req['organiser']
            await user.update()
            return json({'success': True})
        return json({'success': False, 'reson': 'wrong token'})


class SetMentorView(AdminMCV):
    _cls = User
    _urls = '/api/admin/user/set_mentor'

    async def post(self):
        req = self.req.json
        user = await User.get(req['uid'])
        if user:
            user.mentor = req['mentor']
            await user.update()
            return json({
                'success': True,
                'msg': '{} is {} mentor'.format(user.name, 'now a' if req['mentor'] else 'NOT')
            })
        return json({'success': False, 'msg': 'wrong token'})


class ChangeActiveView(AdminMCV):
    _cls = User
    _urls = '/api/admin/user/set_active'

    async def post(self):
        req = self.req.json
        user = await User.get(req['uid'])
        if user:
            user.active = req['active']
            await user.update()
            return json({'success': True})
        return json({'success': False, 'msg': 'wrong token'})


class ReviewAttendeesView(OrganiserMCV):
    _cls = User
    _urls = ['/api/admin/user/review']

    async def get(self):
        allusers = await User.get_by_many_field_value(
            admin=False,
            organiser=False
        )
        allreviews = await UserReview.get_all()
        reviews = defaultdict(dict)
        for rev in allreviews:
            reviews[rev.users][rev.reviewer] = {
                'score': rev.score,
                'name': await get_user_name(rev.reviewer)
            }
        users = []
        for u in allusers:
            ud = await u.to_dict(include_soft=True)
            ud.update({'reviews': reviews.get(u.id, {})})
            usr = reviews.get(u.id, {})
            review_amount = len(usr) or 1
            ud['score'] = sum([x.get('score', 0) for _, x in usr.items()]) / review_amount
            users.append(ud)
        users.sort(key=lambda a: a['score'], reverse=True)
        return json(users)

    async def post(self):
        req = self.req.json
        req['reviewer'] = self.current_user.id
        ur = UserReview(**req)
        if not await ur.create():
            return json({'msg': 'already exists', 'error': True})
        all_ur = await UserReview.get_by_field_value('user_id', req['users'])
        user = await User.get(req['users'])
        new_score = sum(u.score for u in all_ur) / (len(all_ur) or 1)
        user.score = new_score
        await user.update()
        return json({'success': True})

    async def put(self):
        try:
            req = self.req.json
            user = await User.get(req['users'])
            user.accepted = req['accept']
            await user.update()
            return json({'success': True})
        except:
            logging.exception('review_put')
            return json({'success': False}, status=500)


# noinspection PyMethodMayBeStatic
class AdminForgotPasswordView(AdminMCV):
    _cls = User
    _urls = '/api/admin/users/new_password/<email>'

    # noinspection PyUnusedLocal

    async def get(self, email):
        try:
            user = await User.get_first_by_many_field_value(email=email)
        except DoesNotExist:
            logging.error(email)
            user = False
        if not user:
            return json({'msg': 'wrong email or user does not exist'})
        password = create_uuid()
        await user.set_password(password)
        await user.update()
        return json({"success": True, "msg": password})
