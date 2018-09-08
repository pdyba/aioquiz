from asynctest import MagicMock, patch

from sanic.response import HTTPResponse
from sanic.request import Request

mock_request = Request(b'/xxx/', {}, "", "", MagicMock)

from views.user import UserView
from views.user import INeedHelpView
from views.user import SeatView
from views.user import ForgotPasswordView
from views.user import ChangePasswordView
from views.user import SaveGDPR


@patch("models.common.Users.get_by_id")
async def test_user_view_get(patched_get_by_id):
    patched_get_by_id.return_value = True
    view = UserView()
    resp = await view.get(mock_request, MagicMock, 1)
    assert isinstance(resp, HTTPResponse)
    assert resp.body == b'{"msg":"NOT AUTHORISED"}'
    patched_get_by_id.assert_awaited_once()

