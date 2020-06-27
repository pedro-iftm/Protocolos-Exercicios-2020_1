from bottle import Bottle, redirect, route, run, static_file

from controller import (handle_add_contacts_request,
                        handle_list_contacts_request)
from view import list_contacts as list_contacts_view

app = Bottle()


@route('/add-contact', method='GET')
def add_contact():
    return handle_add_contacts_request()


@route('/list-contacts', method='GET')
def list_contacts():
    return handle_list_contacts_request()


@route('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='pages/')


@route('/')
def index():
    return redirect('add-contact')


run()
