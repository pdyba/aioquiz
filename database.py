#!/usr/bin/env python3
# encoding: utf-8
import asyncio
from aiopg.sa import create_engine

from db_models import Question


tbl = Question

async def go():
    async with create_engine(
            user='aiopg',
            database='postgres',
            host='127.0.0.1',
            password='aiopg'
    ) as engine:
        await Question.create_table(engine)
        new_user = {
            'question': 'test_1',
            'answares': 'test_1',
            'img': 'test_1',
            'creator': 1,
            'reviewer': 1,
            'time_created': '2012-01-03 20:27:53',
            'time_accepted': '2012-01-03 20:27:53',
            'active': 't',
        }
        # await tbl.create_new_user(engine, new_user)
        x = await tbl.get_by_id(engine, 5)
        print(x)
        x.question = 'updated test'
        await  x.update(engine)
        print(await tbl.get_by_id(engine, 5))
        # print(await tbl.get_all(engine))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go())
