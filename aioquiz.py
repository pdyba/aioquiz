#!/usr/bin/env python3.5
# encoding: utf-8
import ssl

from sanic import Sanic
from sanic.config import LOGGING

from exception_handlers import add_exception_handlers
from routs import add_urls
from routs import add_static

from config import SERVER

if not SERVER.DEBUG:
    LOGGING['loggers']['network']['level'] = 'WARNING'
    LOGGING['loggers']['sanic']['level'] = 'WARNING'

app = Sanic()

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

if __name__ == "__main__":
    print('http://{}:{}'.format(SERVER.IP, port))  # TODO: should be in green
    app.run(
        host=SERVER.IP,
        port=port,
        debug=SERVER.DEBUG,
        ssl=context,
        log_config=LOGGING,
        workers=SERVER.WORKERS
    )
