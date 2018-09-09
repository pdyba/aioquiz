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


from views.user import UserView
from views.user import INeedHelpView
from views.user import SeatView
from views.user import ForgotPasswordView
from views.user import ChangePasswordView
from views.user import SaveGDPR




@patch("models.common.Users.get_by_id")
async def test_user_view_get_by_id_unauth(patched_get_by_id):
    patched_get_by_id.return_value = True
    view = UserView()
    resp = await view.get(mock_request, MagicMock, 1)
    assert isinstance(resp, HTTPResponse)
    assert resp.body == b'{"msg":"NOT AUTHORISED"}'




@patch("models.common.Users.get_by_id")
async def test_user_view_get_by_id(patched_get_by_id):
    patched_get_by_id.return_value = True
    view = UserView()
    resp = await view.get(mock_request, MagicMock, 1)
    assert isinstance(resp, HTTPResponse)
    # patched_get_by_id.assert_awaited_once()
    assert resp.body == b'{"msg":"..."}'


# @patch("models.common.Users.get_first")
# async def test_user_view_get_first(patched_get_first):
#     patched_get_first.return_value = True
#     view = UserView()
#     resp = await view.get(mock_request, MagicMock, 1)
#     assert isinstance(resp, HTTPResponse)
#     assert resp.body == b'{"msg":"NOT AUTHORISED"}'
#     patched_get_first.assert_awaited_once()
#
#
# @patch("models.common.Users.get_by_many_field_value")
# async def test_user_view_get_by_may_fields(patched_get_by_many_field_value):
#     patched_get_by_many_field_value.return_value = True
#     view = UserView()
#     resp = await view.get(mock_request, MagicMock)
#     assert isinstance(resp, HTTPResponse)
#     assert resp.body == b'{"msg":"NOT AUTHORISED"}'
#     patched_get_by_many_field_value.assert_awaited_once()
#
# @patch("models.common.Users.get_all")
# async def test_user_view_get_get_all(patched_get_all):
#     patched_get_all.return_value = True
#     view = UserView()
#     resp = await view.get(mock_request, MagicMock)
#     assert isinstance(resp, HTTPResponse)
#     assert resp.body == b'{"msg":"NOT AUTHORISED"}'
#     patched_get_all.assert_awaited_once()

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
