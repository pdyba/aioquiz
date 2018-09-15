#!/usr/bin/env python3.5
# encoding: utf-8
import ssl
from sys import stdout

from models.db import db

try:
    from sanic.config import LOGGING
    version = '0.6'
except:
    from sanic.log import LOGGING_CONFIG_DEFAULTS as LOGGING
    version = '0.7'

from sanic import Sanic
from sanic_cors import CORS

from config import DB, SERVER
from exception_handlers import add_exception_handlers
from routes import add_urls
from routes import add_static
from utils import color_print


if not SERVER.DEBUG:
    if version == '0.6':
        LOGGING['loggers']['network']['level'] = 'WARNING'
        LOGGING['loggers']['sanic']['level'] = 'WARNING'
    elif version == '0.7':
        LOGGING['loggers']['sanic.error']['level'] = 'WARNING'
        LOGGING['loggers']['sanic.access']['level'] = 'WARNING'
        LOGGING['loggers']['root']['level'] = 'WARNING'
        LOGGING['loggers']['sanic.access']['handlers'] = ['error_console']
        LOGGING['handlers']['error_console']['stream'] = stdout
        LOGGING['formatters']['generic']['format'] = '%(asctime)s -  %(levelname).4s - %(name)11.11s : %(message)s'


app = Sanic(log_config=LOGGING)
# TODO change the orgins from * to config one (proper one)
CORS(app, automatic_options=True, esources={r"/api/*": {"origins": "*"}})


@app.middleware('response')
async def custom_banner(request, response):
    if request.path.startswith('/api'):
        response.headers["content-type"] = "application/json"
    return response

try:
    context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(SERVER.CERT, keyfile=SERVER.PRIVKEY)
    port = SERVER.PORT_HTTPS
except:
    port = SERVER.PORT_HTTP
    context = None

app = add_static(app)
app = add_urls(app)
app = add_exception_handlers(app)

app.config.DB_HOST = DB.HOST
app.config.DB_USER = DB.USER
app.config.DB_PASSWORD = DB.PASSWORD
app.config.DB_DATABASE = DB.DB

db.init_app(app)

if __name__ == "__main__":
    color_print('http://{}:{}'.format(SERVER.IP, port), color='green')
    app.run(
        host=SERVER.IP,
        port=port,
        debug=SERVER.DEBUG,
        ssl=context,
        workers=SERVER.WORKERS
    )
