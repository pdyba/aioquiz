# !/usr/bin/python3.5
import re

from gino.ext.sanic import Gino
from sqlalchemy import and_

from orm import DoesNotExist

db = Gino()


class EnchancedModel(db.Model):
    _restricted_keys = []
    _soft_restricted_keys = []

    @property
    def id_field(self):
        return self.__class__._fk_col + '_id'

    @classmethod
    async def get_first(cls, field, value):
        return await cls.query.where(getattr(cls, field) == value).gino.first()

    @classmethod
    async def get_all(cls, suffix=""):
        return await cls.query.gino.all()

    @classmethod
    async def get_by_many_field_value(cls, **kwargs):
        and_args = [getattr(cls, field) == value for field, value in kwargs.items()]
        return await cls.query.where(and_(*and_args)).gino.all()

    @classmethod
    async def get_first_by_many_field_value(cls, **kwargs):
        try:
            return (await cls.get_by_many_field_value(**kwargs))[0]
        except IndexError:
            raise DoesNotExist

    async def to_dict(self, include_soft=False):
        restricted_keys = self._restricted_keys if include_soft else self._restricted_keys + self._soft_restricted_keys
        return {field: value for field, value in self.__values__.items() if field not in restricted_keys}

    @classmethod
    async def get_by_field_value(cls, field, value):
        return await cls.query.where(getattr(cls, field) == value).gino.all()

    async def update_or_create(self, *args):
        kw = {arg: getattr(self, arg) for arg in args}
        try:
            inst = await self.get_first_by_many_field_value(**kw)
            await inst.update(**kw).apply()
            return inst, True
        except DoesNotExist:
            return (await self.create()), False

    @classmethod
    async def count_by_field(cls, append='', **kwargs):
        if append:
            raise ValueError('append is not supported anymore')
        return len(await cls.get_by_many_field_value(**kwargs))  # TODO find a way to count without fetching everything


class CodeString(db.String):
    def validate(self, data):
        if isinstance(data, self._py_type):
            return re.match(
                "^[\s\(\)A-Za-z0-9\-_\.\+\*\\\/:=\'\{\},<\"\^\[\]]*",
                data
            )
        return False


db.CodeString = CodeString
