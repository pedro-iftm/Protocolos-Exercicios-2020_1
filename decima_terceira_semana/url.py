import re

from bottle import Bottle, static_file
from contact import Contact
from controller import (handle_add_contact_request,
                        handle_delete_contact_request,
                        handle_edit_contact_request,
                        handle_list_contacts_request,
                        handle_search_contacts_request,
                        handle_sort_contacts_request)
from view import index as index_view

app = Bottle()


@app.route('/add-contact', method='GET')
def add_contact():
    return handle_add_contact_request()


@app.route('/edit-contact', method='GET')
def edit_contact():
    return handle_edit_contact_request()


@app.route('/delete-contact', method='GET')
def delete_contact():
    handle_delete_contact_request()


@app.route('/list-contacts', method='GET')
def list_contacts():
    return handle_list_contacts_request()


@app.route('/search-contacts', method='GET')
def search_contacts():
    return handle_search_contacts_request()


@app.route('/sort-contacts', method='GET')
def sort_contacts():
    return handle_sort_contacts_request()


@app.route('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='pages/assets/')


@app.route('/')
def index():
    return index_view()
