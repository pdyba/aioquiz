# !/usr/bin/python3.5
from datetime import datetime

from orm import Boolean
from orm import Column
from orm import DateTime
from orm import DoesNotExist
from orm import Float
from orm import ForeignKey
from orm import Integer
from orm import String
from orm import Table

from utils import create_uuid
from utils import hash_string
from utils import safe_del_key


class Users(Table):
    _restricted_keys = ['session_uuid', 'password', 'magic_string', 'magic_string_date']
    _soft_restricted_keys = ['score', 'notes']
    _name = 'users'
    _schema = [
        Column('id', Integer(), primary_key=True),
        Column('email', String(255), unique=True),
        Column('name', String(255)),
        Column('surname', String(255)),
        Column('password', String(1000)),
        Column('magic_string', String(50), default='', required=False),
        Column('create_date', DateTime(), default=datetime.utcnow),
        Column('last_login', DateTime(), default=datetime.utcnow),
        Column('magic_string_date', DateTime(), default=datetime.utcnow),
        Column('mentor', Boolean(), default=False),
        Column('organiser', Boolean(), default=False),

        Column('admin', Boolean(), default=False),
        Column('session_uuid', String(255), required=False),

        Column('img', String(255), required=False, default=''),
        Column('linkedin', String(255), required=False),
        Column('twitter', String(255), required=False),
        Column('facebook', String(255), required=False),

        Column('city', String(255), required=False),
        Column('education', String(255), required=False),
        Column('university', String(255), required=False),
        Column('t_shirt', String(10), required=False),
        Column('lang', String(20), required=False, default='pl'),
        Column('age', Integer(), required=False, default=99),

        Column('python', Boolean(), default=False),
        Column('operating_system', String(10), required=False),
        Column('description', String(5000), required=False),
        Column('motivation', String(5000), required=False),
        Column('what_can_you_bring', String(5000), required=False),
        Column('experience', String(5000), required=False),
        Column('app_idea', String(5000), required=False),

        Column('pyfunction', String(255), required=False),

        Column('confirmation', String(10), default='noans'),
        Column('active', Boolean(), default=False),
        Column('accepted_rules', Boolean(), default=False),
        Column('accepted', Boolean(), default=False),
        Column('bring_power_cord', Boolean(), default=False),
        Column('attend_weekly', Boolean(), default=False),
        Column('i_needed_help', Integer(), default=0),

        Column('notes', String(5000), default=''),
        Column('score', Float(), default=0, required=False),
        Column('i_helped', Boolean(), default=False),
        Column('helped', String(5000), required=False),
        Column('gdpr', Boolean(), default=False),
    ]

    _banned_user_keys = [
        'i_needed_help', 'accepted_rules',
    ]
    _public_keys = _banned_user_keys + [
        'education', 'university', 't_shirt',
        'operating_system', 'motivation', 'experience',
        'app_idea', 'accepted', 'confirmation',
        'i_helped', 'helped',
    ]

    async def create(self):
        self.password = hash_string(self.password)
        return await super().create()

    @staticmethod
    async def validate_password(new_password):
        if len(new_password) < 8:
            return {"success": False, "msg": "Password needs to be at least 8 characters long"}
        if new_password == new_password.lower() or new_password == new_password.upper():
            return {
                "success": False,
                "msg": "Password needs to contain at least one small and one capital letter"
            }
        if not any([a for a in new_password if a.isnumeric()]):
            return {
                "success": False,
                "msg": "Password needs to contain at least one number"
            }
        if not any([a for a in new_password if not a.isalnum()]):
            return {
                "success": False,
                "msg": "Password needs to contain at least one small non alpha-numeric character like !, ? or *"
            }
        return {"success": True}

    async def set_password(self, password):
        self.password = hash_string(password)

    async def set_magic_string(self):
        self.magic_string = create_uuid()
        self.magic_string_date = datetime.utcnow()

    @classmethod
    async def get_user_by_session_uuid(cls, session_uuid):
        try:
            return await cls.get_first('session_uuid', session_uuid)
        except DoesNotExist:
            return None

    async def get_public_data(self):
        data = await self.to_dict()
        data = safe_del_key(data, self._public_keys)
        return data

    async def get_my_user_data(self):
        data = await self.to_dict()
        data = safe_del_key(data, self._banned_user_keys)
        return data

    async def update(self, **kwargs):
        if not self.magic_string_date:
            self.magic_string_date = datetime.utcnow()
        return await super().update(**kwargs)

    def is_only_attendee(self):
        return not (self.admin or self.mentor or self.organiser)

    async def set_session_uuid(self, session_uuid):
        await self.update_only_one_value('session_uuid', session_uuid)

    async def get_session_uuid(self):
        session_uuid =  create_uuid()
        await self.set_session_uuid(session_uuid)
        await self.update_only_one_value('last_login', datetime.utcnow())
        return session_uuid

class UserReview(Table):
    _name = 'user_review'
    _schema = [
        Column('users', ForeignKey('users')),
        Column('reviewer', ForeignKey('users')),
        Column('score', Integer()),
    ]
    _unique = ['users', 'reviewer']


class Seat(Table):
    _name = 'seat'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('row', String(255)),
        Column('number', Integer()),
        Column('users', ForeignKey('users'), unique=True),
        Column('i_need_help', Boolean(), default=False),
    ]


class Config(Table):
    _name = 'config'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('reg_active', Boolean(), default=True),
        Column('room_raws', Integer(), default=10),
        Column('room_columns', Integer(), default=10),
    ]

    @classmethod
    async def get_registration(cls):
        config = await cls.get_by_id(1)
        return config.reg_active
