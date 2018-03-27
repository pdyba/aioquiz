#!/usr/bin/env python3.5
# encoding: utf-8
from random import shuffle

from sanic.response import json
from sanic.response import text
from views.utils import HTTPModelClassView


class ExercisesGeneratorView(HTTPModelClassView):
    _cls = None
    _urls = ['/exercise/<eid>']

    async def get(self, request, eid):
        if not eid:
            return json({}, 404)
        exer = getattr(self, 'exercise_{}'.format(eid))
        return await exer()


    @staticmethod
    async def exercise_1_19_1():
        resp = []
        occurences = 123
        for x in '; ! . : + - = | Luck I am Your Father'.split(' '):
            for _ in range(occurences):
                resp.append(x)
        shuffle(resp)
        return json(resp)


    @staticmethod
    async def exercise_1_19_2():
        pylove = 'pylove'
        occurence = 1000
        astring = ''

        for ix, i in enumerate('qwertyuiopasdfghjklzxcvbnm'):
            if i not in pylove:
                astring += i * (occurence - ix * 5)

        for i, let in enumerate(reversed(pylove)):
            astring += let * (occurence + (i + 1) * 50)
        astring = list(astring)
        shuffle(astring)
        return text(''.join(astring))
