# !/usr/bin/python3.5
from abc import abstractproperty
from datetime import datetime


class Table:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if not hasattr(self, key) and self._in_schema(key):
                setattr(self, key, value)
            else:
                setattr(self, '{}__'.format(key), value)

    def __str__(self):
        return '<' + self._name + ' ' + ' '.join([('{}={}'.format(prop.name, getattr(self, prop.name))) for prop in self._schema if not prop.name.startswith('time')]) + '>'

    def __repr__(self):
        return self.__str__()

    @classmethod
    def _gen_schema(cls):
        ' ,'.join([str(field) for field in cls._schema])

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
                print('Question Table Done')

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
            resp = await conn.execute("""SELECT * FROM {} WHERE {} = {}}}""".format(cls._name, field, value))
            return [cls(**r) for r in await resp.fetchall()]

    @classmethod
    def _format_create(cls, clsi):
        keys = []
        values = ""
        for prop in cls._schema:
            if not prop.name.startswith('time') and prop.name != 'id':
                keys.append(prop.name)
                if isinstance(prop._py_type, str):
                    values += "'{}'".format(getattr(clsi, prop.name))
                else:
                    values += str(getattr(clsi, prop.name))
        return ', '.format(keys),


    @classmethod
    async def _create(cls, engine, data): # TODO: WIP
        async with engine.acquire() as conn:
            resp =  await conn.execute("""INSERT INTO question ({}) VALUES
            ({})
            ;""".format(*cls._format_create(data)))
            return resp

    async def create(self, engine):
        await self._create(engine, self)

    @classmethod
    def _format_update(cls, clsi):
        return ', '.join([("{}='{}'".format(prop.name, getattr(clsi, prop.name))) for prop in cls._schema if not prop.name.startswith('time') and prop.name != 'id'])


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

class Column:
    def __init__(self, name, type, primary_key=False):
        self.name = name
        self.type = type
        self.primary_key = primary_key

    def __str__(self):
        if not self.primary_key:
            return '{} {}'.format(self.name, self.type)
        elif self.primary_key and isinstance(self.type, Integer):
            return '{} serial primary key'.format(self.name)


class ColumnType:
    def __init__(self):
        pass

    @abstractproperty
    def _type(self):
        pass

    @abstractproperty
    def _py_type(self):
        pass

    @classmethod
    def __str__(cls):
        return cls._type

    @classmethod
    def validate(cls, data):
        return isinstance(data, cls._py_type)


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


class Boolean(ColumnType):
    _type = 'boolean'
    _py_type = bool


class DateTime(ColumnType):
    _type = 'timestamp'
    _py_type = datetime


class Question(Table):
    _name = 'question'
    _schema = [
        Column('id', Integer, primary_key=True),
        Column('question', String(1000)),
        Column('answares', String(1000)),
        Column('img', String(255)),
        Column('creator', Integer()),
        Column('reviewer', Integer()),
        Column('time_created', DateTime()),
        Column('time_accepted', DateTime()),
        Column('active', Boolean()),
    ]


class User(Table):
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(255))
    password = Column('password', String(1000))
    questions = Column('questions', String(10000))
    live_quiz = Column('live_quiz', String(500))
    moderator = Column('moderator', Boolean())
    admin = Column('admin', Boolean())
    active = Column('active', Boolean())


class Quiz(Table):
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(255))
    questions = Column('questions', String(10000))
    creator = Column('creator', Integer())
    time_created = Column('time_accepted', DateTime())


class LiveQuiz(Table):
    id = Column('id', Integer, primary_key=True)
    title = Column('title', String(255))
    questions = Column('questions', String(10000))
    creator = Column('creator', Integer())
    time_created = Column('time_created', DateTime())
    active = Column('active', Boolean())
