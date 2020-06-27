from bottle import template


def add_contact(message=False):
    return template('pages/add_contact.tpl', message=message)


def list_contacts(content):
    return template('pages/list_contacts', rows=content)
