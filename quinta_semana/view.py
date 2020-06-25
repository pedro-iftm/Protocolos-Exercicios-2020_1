from bottle import template

from model import read_file, write_file


def access_denied(attempts):
    return f'Acesso negado<br/>Outras tentativas: {attempts}'


def successfully_authenticated(user):
    return f'Bem-vindo {user}'


def login_page():
    return template('pages/index.tpl')
