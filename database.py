#!/usr/bin/env python3
# encoding: utf-8
import asyncio
from aiopg.sa import create_engine

from db_models import Question, Users, LiveQuiz, Quiz




async def bootstrap_db():
    async with create_engine(
            user='aiopg',
            database='postgres',
            host='127.0.0.1',
            password='aiopg'
    ) as engine:
        await Question.create_table(engine)
        await Users.create_table(engine)
        await LiveQuiz.create_table(engine)
        await Quiz.create_table(engine)
        new_user = {
            'email': 'piotr@dyba.com.pl',
            'password': 'test_1',
            'img': 'test_1',
            'moderator': True,
            'admin': True,
        }
        tbl = Users(**new_user)
        await tbl.create(engine)
        await tbl.get_by_id(engine, 1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bootstrap_db())
