from bottle import template


def add_contact():
    return template('pages/add_contact')


def edit_contact(**kwargs):
    return template('pages/edit_contact', **kwargs)


def index():
    return template('pages/index')


def list_contacts(content):
    return template('pages/list_contacts', rows=content)
