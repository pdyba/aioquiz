# !/usr/bin/python3.5
import re

from gino.ext.sanic import Gino

db = Gino()


class EnchancedModel(db.Model):
    @classmethod
    async def get_first(cls, field, value):
        return await cls.query.where(getattr(cls, field) == value).gino.first()

    @classmethod
    async def get_all(cls, suffix=""):
        return await cls.query.gino.all()


class CodeString(db.String):
    def validate(self, data):
        if isinstance(data, self._py_type):
            return re.match(
                "^[\s\(\)A-Za-z0-9\-_\.\+\*\\\/:=\'\{\},<\"\^\[\]]*",
                data
            )
        return False


db.CodeString = CodeString
