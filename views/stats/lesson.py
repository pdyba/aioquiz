#!/usr/bin/env python3.5
# encoding: utf-8
from sanic.response import json

from models import Exercise
from models import ExerciseAnsware

from views.utils import user_required
from views.utils import HTTPModelClassView


class ExerciseOverview(HTTPModelClassView):
    _cls = Exercise
    _urls = '/api/stats/exercises'

    @user_required('mentor')
    async def get(self, _):
        exercises = await Exercise.get_all()
        resp = {}
        for ex in exercises:
            if not resp.get(ex.lesson):
                resp[ex.lesson] = {}
            resp[ex.lesson][ex.id] = await ex.to_dict()
            resp[ex.lesson][ex.id]['exercise_answare'] = await ExerciseAnsware.group_by_field('status', exercise=ex.id)
        return json(resp)
