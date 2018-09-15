# !/usr/bin/python3.5
from datetime import datetime

from models.db import db, EnchancedModel
from orm import DoesNotExist

from utils import create_uuid
from utils import hash_string
from utils import safe_del_key


class User(EnchancedModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    magic_string = db.Column(db.String, default='')
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)
    magic_string_date = db.Column(db.DateTime, default=datetime.utcnow)
    mentor = db.Column(db.Boolean, default=False)
    organiser = db.Column(db.Boolean, default=False)

    admin = db.Column(db.Boolean, default=False)
    session_uuid = db.Column(db.String)

    img = db.Column(db.String, default='')
    linkedin = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)

    city = db.Column(db.String)
    education = db.Column(db.String)
    university = db.Column(db.String)
    t_shirt = db.Column(db.String)
    lang = db.Column(db.String, default='pl')
    age = db.Column(db.Integer, default=99)

    python = db.Column(db.Boolean, default=False)
    operating_system = db.Column(db.String)
    description = db.Column(db.String)
    motivation = db.Column(db.String)
    what_can_you_bring = db.Column(db.String)
    experience = db.Column(db.String)
    app_idea = db.Column(db.String)

    pyfunction = db.Column(db.String)

    confirmation = db.Column(db.String, default='noans')
    active = db.Column(db.Boolean, default=False)
    accepted_rules = db.Column(db.Boolean, default=False)
    accepted = db.Column(db.Boolean, default=False)
    bring_power_cord = db.Column(db.Boolean, default=False)
    attend_weekly = db.Column(db.Boolean, default=False)
    i_needed_help = db.Column(db.Integer, default=0)

    notes = db.Column(db.String, default='')
    score = db.Column(db.Float, default=0)
    i_helped = db.Column(db.Boolean, default=False)
    helped = db.Column(db.String)
    gdpr = db.Column(db.Boolean, default=False)

    _restricted_keys = ['session_uuid', 'password', 'magic_string', 'magic_string_date']
    _soft_restricted_keys = ['score', 'notes']
    _banned_user_keys = [
        'i_needed_help', 'accepted_rules',
    ]
    _public_keys = _banned_user_keys + [
        'education', 'university', 't_shirt',
        'operating_system', 'motivation', 'experience',
        'app_idea', 'accepted', 'confirmation',
        'i_helped', 'helped',
    ]

    @classmethod
    async def create(cls, *args, **kwargs):
        if 'password' in kwargs:
            kwargs['password'] = hash_string(kwargs['password'])
        return await super().create(*args, **kwargs)

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

    # FIXME: This breaks updating for some reason
    # def update(self, *args, **kwargs):
    #     if not self.magic_string_date:
    #         kwargs['magic_string_date'] = datetime.utcnow()
    #     return super().update(*args, **kwargs)

    def is_only_attendee(self):
        return not (self.admin or self.mentor or self.organiser)

    async def set_session_uuid(self, session_uuid):
        await self.update(session_uuid=session_uuid).apply()

    async def get_session_uuid(self):
        session_uuid = create_uuid()
        await self.set_session_uuid(session_uuid)
        await self.update(last_login=datetime.utcnow()).apply()
        return session_uuid


class UserReview(EnchancedModel):
    __tablename__ = 'user_reviews'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    # TODO _unique = ['user_d', 'reviewer_id']


class Seat(EnchancedModel):
    __tablename__ = 'seats'

    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    i_need_help = db.Column(db.Boolean(), default=False)


class Config(EnchancedModel):
    __tablename__ = 'config'

    id = db.Column(db.Integer, primary_key=True)
    reg_active = db.Column(db.Boolean, default=True)
    room_raws = db.Column(db.Integer, default=10)
    room_columns = db.Column(db.Integer, default=10)

    @classmethod
    async def get_registration(cls):
        config = await cls.get(1)
        return config.reg_active
