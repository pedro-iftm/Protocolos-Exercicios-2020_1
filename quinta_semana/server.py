from bottle import route, request, run

from controller import handle_request


@route('/', method='GET')
def login():
    return handle_request(request)


run()
