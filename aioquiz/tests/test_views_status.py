from asynctest import MagicMock, patch

from sanic.response import HTTPResponse

from views.status import RegistrationActiveView


@patch("models.common.Config.get_registration")
async def test_sanic_db_find_by_id(patched_model):
    patched_model.return_value = True
    view = RegistrationActiveView()
    resp = await view.get(MagicMock)
    assert isinstance(resp, HTTPResponse)
    assert resp.body == b'{"registration":true}'
    patched_model.assert_awaited_once()
