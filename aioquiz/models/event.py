# !/usr/bin/python3.5
from datetime import datetime

from models.db import db, EnchancedModel


class Event(EnchancedModel):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)

    country = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    geo_location_lang = db.Column(db.Float, nullable=False)
    geo_location_long = db.Column(db.Float, nullable=False)
    address = db.Column(db.String, nullable=False)
    address_picture = db.Column(db.String, nullable=False)
    address_desc = db.Column(db.String, nullable=False)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, default=datetime.utcnow)
    registration_start_date = db.Column(db.DateTime, default=datetime.utcnow)
    registration_end_date = db.Column(db.DateTime, default=datetime.utcnow)

    reg_active = db.Column(db.Boolean, default=True)
    event_active = db.Column(db.Boolean, default=True)


class EventMeeting(EnchancedModel):
    __tablename__ = 'event_meetings'

    order_number = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    lesson_active = db.Column(db.Boolean, default=False)


class EventUser(EnchancedModel):
    __tablename__ = 'event_users'    
    _soft_restricted_keys = ['score', 'notes']

    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    confirmation = db.Column(db.String, default='noans')
    accepted = db.Column(db.Boolean, default=False)
    bring_power_cord = db.Column(db.Boolean, default=False)
    attend_weekly = db.Column(db.Boolean, default=False)
    notes = db.Column(db.String, default='')
    score = db.Column(db.Float, default=0)
    i_helped = db.Column(db.Boolean)
    helped = db.Column(db.String)


class Sponsor(EnchancedModel):
    __tablename__ = 'sponsors'    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    logo = db.Column(db.String, default='')
    webpage = db.Column(db.String, default='')
    linkedin = db.Column(db.String)
    twitter = db.Column(db.String)
    facebook = db.Column(db.String)

    city = db.Column(db.String)
    country = db.Column(db.String)


class EventSponsors(EnchancedModel):
    __tablename__ = 'event_sponsors'    

    order_number = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsors.id'), nullable=False)
    rank = db.Column(db.String, nullable=False)
