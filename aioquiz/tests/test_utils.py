from asynctest import CoroutineMock

from utils import color_print
from utils import hash_string
from utils import safe_del_key
from utils import send_email
from utils import create_uuid
from utils import ClassProperty


class SmtpMock:
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, item):
        return CoroutineMock()


def test_hash_string():
    expected_hash = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    assert hash_string('test') == expected_hash


def test_color_print(capsys):
    resp = color_print('xxx')
    out, err = capsys.readouterr()
    assert resp == None
    assert out == '\x1b[1;31m xxx \x1b[0;0m\n'
    color_print('xxx', color='blue')
    out, err = capsys.readouterr()
    assert out == '\033[1;34m xxx \x1b[0;0m\n'


def test_safe_del_key():
    ex_dict = {'key_{}'.format(x): 'val_{}'.format(x) for x in range(10)}
    clean_dict_1 = safe_del_key(ex_dict, 'key_1')
    assert 'key_1' not in clean_dict_1
    assert len(clean_dict_1) == 9
    clean_dict_2 = safe_del_key(ex_dict, ['key_2', 'key_3', 'key_4'])
    assert 'key_2' not in clean_dict_2
    assert 'key_3' not in clean_dict_2
    assert 'key_4' not in clean_dict_2
    clean_dict_3 = safe_del_key(clean_dict_2, ['key_2', 'key_3', 'key_4'])
    assert clean_dict_3 == clean_dict_2
    assert len(clean_dict_3) == 6


def test_create_uuid():
    uid = create_uuid()
    assert len(uid) == 32
    assert uid.isalnum()


async def test_send_email(monkeypatch):
    monkeypatch.setattr("aiosmtplib.SMTP", SmtpMock)
    resp = await send_email(recipients='x@wp.pl', subject='xx', text='xx')
    assert resp == True


def test_class_property():
    class XT:
        @ClassProperty
        def name(cls):
            return cls.__name__

    xt = XT
    assert xt.name == 'XT'
