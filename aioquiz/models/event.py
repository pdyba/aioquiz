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


class Event(Table):
    _name = 'event'
    _schema = [
        Column('id', Integer(), primary_key=True),
        Column('title', String(500), unique=True),
        Column('description', String(1000)),

        Column('country', String(255)),
        Column('city', String(255)),
        Column('geo_location_lang', Float()),
        Column('geo_location_long', Float()),
        Column('address', String(500)),
        Column('address_picture', String(500)),
        Column('address_desc', String(500)),

        Column('create_date', DateTime(), default=datetime.utcnow),
        Column('start_date', DateTime(), default=datetime.utcnow),
        Column('end_date', DateTime(), default=datetime.utcnow),
        Column('registration_start_date', DateTime(), default=datetime.utcnow),
        Column('registration_end_date', DateTime(), default=datetime.utcnow),

        Column('reg_active', Boolean(), default=True),
        Column('event_active', Boolean(), default=True),
    ]


class EventMeetings(Table):
    _name = 'event_meetings'
    _schema = [
        Column('order_number', Integer()),
        Column('event', ForeignKey('event')),
        Column('lesson', ForeignKey('lesson')),
        Column('date', DateTime(), default=datetime.utcnow),
        Column('lesson_active', Boolean(), default=False),
    ]


class EventUsers(Table):
    _name = 'event_users'
    _soft_restricted_keys = ['score', 'notes']
    _schema = [
        Column('event', ForeignKey('event')),
        Column('users', ForeignKey('users')),

        Column('confirmation', String(10), default='noans'),
        Column('accepted', Boolean(), default=False),
        Column('bring_power_cord', Boolean(), default=False),
        Column('attend_weekly', Boolean(), default=False),
        Column('notes', String(5000), default=''),
        Column('score', Float(), default=0, required=False),
        Column('i_helped', Boolean(), default=False),
        Column('helped', String(5000), required=False),
    ]


class Sponsor(Table):
    _name = 'sponsor'
    _schema = [
        Column('id', Integer(), primary_key=True),
        Column('name', String(255)),
        Column('description', String(5000)),

        Column('logo', String(255), required=False, default=''),
        Column('webpage', String(255), required=False, default=''),
        Column('linkedin', String(255), required=False),
        Column('twitter', String(255), required=False),
        Column('facebook', String(255), required=False),

        Column('city', String(255), required=False),
        Column('country', String(255), required=False),
    ]


class EventSponsor(Table):
    _name = 'event_sponsor'
    _schema = [
        Column('order_number', Integer()),
        Column('event', ForeignKey('event')),
        Column('sponsor', ForeignKey('sponsor')),
        Column('rank', String(255)),
    ]
