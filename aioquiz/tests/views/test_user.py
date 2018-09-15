import asyncio
import unittest
from aiohttp.test_utils import unittest_run_loop
from unittest.mock import patch as synpatch
synpatch("views.utils.user_required", lambda x: x).start()

from asynctest import MagicMock, patch

from sanic.response import HTTPResponse
from sanic.request import Request

mock_request = Request(b'/xxx/', {'authorization': 'asdadas'}, "", "", MagicMock)

# def user_required_hacked(access_level='any_user', msg='NOT AUTHORISED', code=401):
#     def decorator(func):
#         @wraps(func)
#         async def func_wrapper(self, *args, **kwargs):
#             return await func(self, *args, **kwargs)
#         return func_wrapper
#     return decorator



# @pytest.fixture(autouse=True)
# def nouser(monkeypatch):
#     monkeypatch.setattr("views.utils.user_required", user_required_hacked)


from views.user import UserView, ActivationView
from views.user import INeedHelpView
from views.user import SeatView
from views.user import ForgotPasswordView
from views.user import ChangePasswordView
from views.user import SaveGDPR


class UserViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_get(self):
        view = UserView()
        resp = await view.get("undefined")
        self.assertTrue(isinstance(resp, HTTPResponse))
        self.assertEqual(resp.body, b'{"msg":"wrong username"}')

    @unittest_run_loop
    async def test_put(self):
        view = UserView()

    @unittest_run_loop
    async def test_post(self):
        view = UserView()

    @unittest_run_loop
    async def test_delete(self):
        view = UserView()


class ActivationViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()
    @unittest_run_loop
    async def test_get(self):
        view = ActivationView()


class INeedHelpViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_get(self):
        view = INeedHelpView()

    @unittest_run_loop
    async def test_delete(self):
        view = INeedHelpView()


class SeatViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_get(self):
        view = SeatView()

    @unittest_run_loop
    async def test_post(self):
        view = SeatView()

    @unittest_run_loop
    async def test_delete(self):
        view = SeatView()


class ForgotPasswordViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_post(self):
        view = ForgotPasswordView()


class ChangePasswordViewTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_post(self):
        view = ChangePasswordView()


class SaveGDPRTest(unittest.TestCase):
    loop = asyncio.get_event_loop()

    @unittest_run_loop
    async def test_get(self):
        view = SaveGDPR()


x = ['assert_any_await',
     'assert_any_call',
     'assert_awaited',
     'assert_awaited_once',
     'assert_awaited_once_with',
     'assert_awaited_with',
     'assert_called',
     'assert_called_once',
     'assert_called_once_with',
     'assert_called_with',
     'assert_has_awaits',
     'assert_has_calls',
     'assert_not_awaited',
     'assert_not_called',
     'attach_mock',
     'await_args',
     'await_args_list',
     'await_count',
     'awaited',
     'call_args',
     'call_args_list',
     'call_count',
     'called',
     'configure_mock',
     'method_calls',
     'mock_add_spec',
     'mock_calls',
     'reset_mock',
     'return_value',
     'side_effect']
