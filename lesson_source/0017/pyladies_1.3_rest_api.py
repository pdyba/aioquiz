import json
import hashlib
import os
from os.path import isfile
from os.path import abspath
from os.path import dirname
from os.path import join
from random import randint

from sanic import Sanic
from sanic import response

app = Sanic(__name__)

health = "ok"

g_status = 'I am fine'

g_user_status = {}


def hash_string(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route("/health", methods=['GET'])
def status(request):
    """
    /health
    GET
    proper response:
        200: {'health': "OK"}
    :param request:
    :return:
    """
    return response.json({'health': health})


@app.route("/status/set", methods=['POST'])
def status_set(request):
    """
    /status/set
    POST
    requires:
        "status": string
    proper response:
        200: {'success': True}
    :param request:
    :return:
    """
    req = request.json
    if 'status' not in req:
        return response.json(
            {
                'success': False,
                'reason': 'You need to provide new status'
            },
            status=400
        )
    global g_status
    g_status = req['status']
    print('New status: {}'.format(g_status))
    return response.json({'success': True}, status=200)


@app.route("/status", methods=['GET'])
def get_status(request):
    """
    /status
    GET
    proper response:
        200: {'status': string}
    :param request:
    :return:
    """
    return response.json({'status': g_status})


@app.route("/register", methods=['POST'])
def register(request):
    """
    /register
    POST
    requires:
        "name": string
        "password": string
    proper response:
        200: {'success': True}
    :param request:
    :return:
    """
    req = request.json
    if 'name' not in req or 'password' not in req:
        return response.json(
            {
                'success': False,
                'reason': 'You need to provide name amd password to create a user'
            },
            status=400
        )
    h_name = hash_string(req['name'])
    path = 'users/{}'.format(h_name)
    if isfile(path):
        return response.json(
            {
                'success': False,
                'reason': 'User already exists'
            },
            status=401
        )
    req['api_key'] = h_name
    with open(path, 'w') as file:
        json.dump(req, file)
    print("{} just registered".format(req['name']))
    return response.json({'success': True}, status=200)


@app.route("/auth", methods=['POST'])
def login(request):
    """
    /auth
    POST
    requires:
        "name": string
        "password": string
    proper response:
        {'api_key': string, 'name': string}
    :param request:
    :return:
    """
    req = request.json
    if 'name' not in req or 'password' not in req:
        return response.json(
            {
                'success': False,
                'reason': 'You need to provide name amd password to login'
            },
            status=400
        )
    h_name = hash_string(req['name'])
    if not isfile('users/{}'.format(h_name)):
        return response.json(
            {
                'success': False,
                'reason': 'Unauthorised'
            },
            status=401
        )
    print('{} just logged'.format(req['name']))
    return response.json({'api_key': h_name, 'name': req['name']}, status=200)


@app.route("/user_status/set", methods=['POST'])
def set_user_status(request):
    """
    /user_status/set
    POST
    requires:
        "api_key": string
        "status": string
    proper response:
        {'success': True}
    :param request:
    :return:
    """
    req = request.json
    if not req.get('api_key') or not isfile('users/{}'.format(req.get('api_key'))):
        return response.json(
            {
                'success': False,
                'reason': 'Unauthorised'
            },
            status=401
        )
    if not req.get('status'):
        return response.json(
            {
                'success': False,
                'reason': 'no status provided'
            },
            status=400
        )
    with open('users/{}'.format(req.get('api_key'))) as file:
        user = json.load(file)
    global g_user_status
    g_user_status[user['name']] = req['status']
    print("{} just set new status {}".format(user['name'], req['status']))
    return response.json({'success': True}, status=200)


@app.route("/user_status", methods=['GET'])
def user_status(request):
    """
    /user_status
    GET
    proper response:
        200: {string: string}
    :param request:
    :return:
    """
    return response.json(g_user_status)


@app.route("/cat", methods=['GET'])
async def test_file(request):
    """
    /cat
    GET
    proper response:
        200: data
    :param request:
    :return:
    """
    return await response.file(
        os.path.abspath("cats/cat_{}.jpg".format(randint(1, 9)))
    )


@app.route("/query_string")
def query_string(request):
    """
    /query_string
    GET
    proper response:
        200: {
        "parsed": bool,
        "args": dict,
        "url": dict,
        "query_string": dict
    }
    :param request:
    :return:
    """
    return response.json({
        "parsed": True,
        "args": request.args,
        "url": request.url,
        "query_string": request.query_string
    })


@app.route("/requests", methods=['GET'])
async def get_requests(request):
    """
    /requests
    GET
    proper response:
        200: data
    :param request:
    :return:
    """
    return await response.file(os.path.abspath("files/requests-2.18.4-py2.py3-none-any.whl"))


@app.route("/requests_tar", methods=['GET'])
async def get_requests_tar(request):
    """
    /requests_tar
    GET
    proper response:
        200: data
    :param request:
    :return:
    """
    return await response.file(os.path.abspath("files/requests-2.18.4.tar.gz"))

dir_name = dirname(abspath(__file__))
app.static('/', join(dir_name, 'static/index.html'))
app.static('/css/', join(dir_name, 'static/css'))
app.static('/images', join(dir_name, 'static/images'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10080, workers=3)
