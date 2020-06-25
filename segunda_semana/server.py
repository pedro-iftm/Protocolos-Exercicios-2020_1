from bottle import route, request, template, run


@route('/', method='GET')
def login():
    if request.GET.button:
        user = request.GET.user
        password = request.GET.password

        if user == 'pedro' and password == '123':
            return f'Bem-vindo {user}'

        return f'{user} seu usuário ou senha são inválidos!'

    return template('pages/index.tpl')


run()
