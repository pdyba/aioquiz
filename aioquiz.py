# !/usr/bin/python3.5
from inspect import getmembers
from os.path import abspath
from os.path import dirname
from os.path import join

import ssl

from sanic import Sanic
from sanic.config import LOGGING
from sanic.exceptions import NotFound
from sanic.exceptions import RequestTimeout
from sanic.exceptions import ServerError


from exception_handlers import handle_404s
from exception_handlers import handle_500s
from exception_handlers import handle_timeout

import views
from views.utils import HTTPModelClassView

from config import SERVER

if not SERVER.DEBUG:
    LOGGING['loggers']['network']['level'] = 'WARNING'
    LOGGING['loggers']['sanic']['level'] = 'WARNING'

dir_name = dirname(abspath(__file__))
app = Sanic()

try:
    context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain("/opt/aioquiz/cert.pem", keyfile="/opt/aioquiz/privkey.pem")
    port = SERVER.PORT_HTTPS
except:
    port = SERVER.PORT_HTTP
    context = None

app.static('/', join(dir_name, 'static/index.html'))
app.static('/sum', join(dir_name, 'static/summary.html'))
app.static('/js/vendor/', join(dir_name, 'static/js/vendor/'))
app.static('/css/', join(dir_name, 'static/css'))
app.static('/js', join(dir_name, 'static/js/'))
app.static('/images', join(dir_name, 'static/images'))
app.static('/partials', join(dir_name, 'static/partials'))
app.static('/templates', join(dir_name, 'static/templates'))
app.static('/lessons', join(dir_name, 'static/lessons'))
app.static('/favicon.ico', join(dir_name, 'static/images/favicon.ico'))
app.static('/dist', join(dir_name, 'static/dist')) 

count_cls = 0
count_urls = 0

for member in getmembers(views):
    try:
        name, view = member
        if not issubclass(view, HTTPModelClassView) or view == HTTPModelClassView:
            if 'View' in name:
                print(name, 'skipping')  # TODO: should be yellow
            continue
    except:
        continue
    try:
        if isinstance(view._urls, list):
            count_cls += 1
            for url in view._urls:
                app.add_route(view.as_view(), url)
                count_urls += 1
        elif isinstance(view._urls, str):
            app.add_route(view.as_view(), view._urls)
            count_cls += 1
            count_urls += 1
        else:
            print("Something is missing: ", view._get_name(), view._urls)
    except AttributeError:
        print(view, 'no URLS provided')  # TODO: should be in red

print('Using {} classes with {} urls'.format(count_cls, count_urls))

app.error_handler.add(ServerError, handle_500s)
app.error_handler.add(NotFound, handle_404s)
app.error_handler.add(RequestTimeout, handle_timeout)

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
