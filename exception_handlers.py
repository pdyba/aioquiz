from sanic.response import json


def handle_500s(request, exception):
    return json(
        {"msg": "Nope not gonna work"},
        status=500
    )


def handle_404s(request, exception):
    return json(
        {'msg': "Yep, I totally found the page: {}".format(request.url)},
        status=404
    )


def handle_timeout(request, exception):
    return json(
        {'msg': "I have been waiting too long sorry"},
        status=408
    )
