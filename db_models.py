# !/usr/bin/python3.5
from abc import abstractproperty
from datetime import datetime
import json

from psycopg2._psycopg import IntegrityError


class DoesNoteExists(Exception):
    @staticmethod
    async def to_dict():
        return {'msg': 'User Does not Exists'}


class Table:
    def __init__(self, **kwargs):
        for field in self._schema:
            name = field.name
            if name not in kwargs:
                if field.default is not None:
                    setattr(self, name, field.default)
                elif field.required and name != 'id':
                    raise Exception('No {} provided'.format(name))
            else:
                setattr(self, name, kwargs[field.name])

    def __str__(self):
        return '<' + self._name + ' ' + ' '.join([('{}={}'.format(prop.name, getattr(self, prop.name))) for prop in self._schema if not prop.name.startswith('time')]) + '>'

    def __repr__(self):
        return self.__str__()

    @classmethod
    def _gen_schema(cls):
        alist = []
        for field in cls._schema:
            alist.append(str(field))
        return ', '.join(alist)

    @classmethod
    def _in_schema(cls, name):
        for field in cls._schema:
            if name == field.name:
                return True
        return False

    @abstractproperty
    def _name(self):
        pass

    @abstractproperty
    def _schema(self):
        pass

    @classmethod
    async def _table_exists(cls, engine):
        async with engine.acquire() as conn:
            exists = await conn.execute("""SELECT EXISTS (
                        SELECT 1
                        FROM   information_schema.tables
                        WHERE  tables.table_name = '{}'
                    ); """.format(cls._name))
            exists = await exists.first()
            return str(exists) == '(False,)'

    @classmethod
    async def create_table(cls, engine):
        if await cls._table_exists(engine):
            async with engine.acquire() as conn:
                await conn.execute(
                    """CREATE TABLE {} ( {} );""".format(cls._name, cls._gen_schema())
                )
                print('{} Table Done'.format(cls._name))
        else:
            print('{} Table already exists'.format(cls._name))

    @classmethod
    async def get_by_id(cls, engine, uid):
        async with engine.acquire() as conn:
            resp = await conn.execute(
                """SELECT * FROM {} WHERE id = {}""".format(cls._name, uid)
            )
            resp = await resp.first()
            return cls(**resp)


    @classmethod
    async def get_all(cls, engine):
        async with engine.acquire() as conn:
            resp = await conn.execute("""SELECT * FROM {}""".format(cls._name))
            return [cls(**r) for r in await resp.fetchall()]

    @classmethod
    async def get_by_field_value(cls, engine, field, value):
        async with engine.acquire() as conn:
            resp = await conn.execute("""SELECT * FROM {} WHERE {}='{}'""".format(cls._name, field, value))
            return [cls(**r) for r in await resp.fetchall()]

    @classmethod
    async def get_first(cls, engine, field, value):
        data = await cls.get_by_field_value(engine, field, value)
        try:
            return data[0]
        except Exception as err:
            raise DoesNoteExists

    @classmethod
    def _format_create(cls, clsi):
        keys = []
        values = """"""
        for prop in cls._schema:
            if prop.name != 'id':
                keys.append(prop.name)
                if isinstance(prop.type, String):
                    try:
                        val = getattr(clsi, prop.name)
                    except AttributeError:
                        if not prop.required:
                            val = ''
                    ending = '"' if "'" in val else "'"
                    values += ending
                    values += prop.type.format(val)
                    values += ending
                elif isinstance(prop.type, DateTime):
                    val = getattr(clsi, prop.name)
                    values += "'"
                    values += str(val)
                    values += "'"
                else:
                    values += (str(getattr(clsi, prop.name)))
                values += ', '
        return ', '.join(keys), values[:-2]

    @classmethod
    async def _create(cls, engine, data):
        async with engine.acquire() as conn:
            resp = await conn.execute("""INSERT INTO {} ({}) VALUES
            ({})
            ;""".format(cls._name, *cls._format_create(data)))
            return resp

    async def create(self, engine):
        try:
            return await self._create(engine, self)
        except IntegrityError as e:
            er = e.pgerror
            msg = er[er.find('Key') + 4:er.find('already') - 1].replace('(', '').replace(')', '')
            return {
                'error': msg + 'already exists',
            }

    @classmethod
    def _format_update(cls, clsi):
        return ', '.join([("{}='{}'".format(prop.name, getattr(prop.type.format(clsi), prop.name))) for prop in cls._schema if not prop.name.startswith('time') and prop.name != 'id'])

    @classmethod
    async def _update(cls, engine, data):
        async with engine.acquire() as conn:
            resp =  await conn.execute(
                """UPDATE {} SET {}
                WHERE id = {}
                ;""".format(cls._name, cls._format_update(data), data.id))
            return resp

    async def update(self, engine):
        await self._update(engine, self)

    async def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self._schema}


class Column:
    def __init__(
            self,
            name,
            type,
            primary_key=False,
            required=True,
            default=None,
            unique=False
    ):
        self.name = name
        self.type = type
        self.primary_key = primary_key
        self.required = required
        self.unique = unique
        self.default = default() if callable(default) else default

    def __str__(self):
        if self.unique:
            return '{} {} UNIQUE NOT NULL'.format(self.name, str(self.type))
        elif not self.primary_key:
            return '{} {}'.format(self.name, str(self.type))
        return '{} serial primary key'.format(self.name)


class ColumnType:
    def __init__(self):
        pass

    @classmethod
    def __str__(cls):
        return cls._type

    @abstractproperty
    def _type(self):
        pass

    @abstractproperty
    def _py_type(self):
        pass

    @classmethod
    def validate(cls, data):
        return isinstance(data, cls._py_type)

    def format(self, data):
        return data


class Integer(ColumnType):
    _type = 'integer'
    _py_type = int


class String(ColumnType):
    _type = 'varchar({})'
    _py_type = str

    def __init__(self, length):
        super().__init__()
        self.length = length

    def __str__(self):
        return self._type.format(self.length)

    def validate(self, data):
        super().validate(data) and len(data) <= self.length

    def format(self, data):
        if isinstance(data, str):
            return data
        return json.dumps(data)


class Boolean(ColumnType):
    _type = 'boolean'
    _py_type = bool


class DateTime(ColumnType):
    _type = 'timestamp'
    _py_type = datetime

