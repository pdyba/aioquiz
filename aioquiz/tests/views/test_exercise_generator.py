import asyncio
import unittest
from unittest.mock import patch, Mock

from aiohttp.test_utils import unittest_run_loop
from sanic.response import json, HTTPResponse

from views.exercise_generator import ExercisesGeneratorView


async def return_HTTPResponse(body):
    return json(body)


class ExercisesGeneratorViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_get(self):
        view = ExercisesGeneratorView()
        with patch.object(view, "exercise_1_19_1", Mock(return_value=return_HTTPResponse([]))):
            result = await view.get("1_19_1")
            self.assertTrue(isinstance(result, HTTPResponse))
            self.assertEqual(result.body, b'[]')
