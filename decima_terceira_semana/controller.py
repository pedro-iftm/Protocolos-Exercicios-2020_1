import re

from bottle import Bottle, static_file, request, redirect
from contact import Contact
from view import add_contact, edit_contact, list_contacts
from view import index as index_view


app = Bottle()


@app.route('/add-contact', method='GET')
def handle_add_contact():
    if request.GET.save_button:
        form_data = __get_form_data()
        Contact().add(**form_data)

        return redirect('/list-contacts')

    return add_contact()


@app.route('/edit-contact', method='GET')
def handle_edit_contact():
    id = request.query.get('id')

    if request.GET.save_button:
        form_data = __get_form_data()
        form_data['id'] = id
        Contact().edit(**form_data)

        return redirect('/list-contacts')

    contact = Contact().get(id)[0]
    initial_data = {'name': contact[0],
                    'id': contact[1],
                    'email': contact[2],
                    'phone': contact[3]}

    return edit_contact(**initial_data)


@app.route('/delete-contact', method='GET')
def handle_delete_contact():
    id = request.query.get('id')
    Contact().delete(id)
    return redirect('/list-contacts')


@app.route('/list-contacts', method='GET')
def handle_list_contacts():
    contacts = Contact().all()
    return list_contacts(contacts)


@app.route('/search-contacts', method='GET')
def handle_search_contacts():
    if request.GET.search_button:
        search = request.GET.search
        contacts = Contact().get(search)

        return list_contacts(contacts)


@app.route('/sort-contacts', method='GET')
def handle_sort_contacts():
    selected_sort = list(request.GET.values())

    if selected_sort:
        contacts = Contact().all(sort=selected_sort[0])
        return list_contacts(contacts)


@app.route('/<filename:path>')
def static_files(filename):
    return static_file(filename, root='pages/assets/')


@app.route('/')
def index():
    contacts = Contact().all()
    return list_contacts(contacts)


def __get_form_data():
    form_data = {'name': request.GET.name,
                 'id': request.GET.id,
                 'email': request.GET.email,
                 'phone': request.GET.phone}

    return form_data
