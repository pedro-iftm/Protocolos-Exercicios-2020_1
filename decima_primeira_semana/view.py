from bottle import template


def add_contact():
    return template('static/add_contact')


def edit_contact(**kwargs):
    return template('static/edit_contact', **kwargs)


def index():
    return template('static/index')


def list_contacts(content):
    return template('static/list_contacts', rows=content)
