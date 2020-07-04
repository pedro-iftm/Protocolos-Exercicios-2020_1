import re

from bottle import redirect, request

from contact import Contact
from view import add_contact, edit_contact, list_contacts
from view import index as index_view


def handle_add_contact_request():
    if request.GET.save_button:
        form_data = __get_form_data()
        Contact().add(**form_data)

        return redirect('/list-contacts')

    return add_contact()


def handle_edit_contact_request():
    id = request.query.get('id')

    if request.GET.save_button:
        form_data = __get_form_data()
        form_data['id'] = id
        Contact().edit(**form_data)

        return redirect('/list-contacts')

    contact = Contact().get(id)[0]
    formated_id = re.sub(r'[.-]*', '', contact[1])
    initial_data = {'name': contact[0],
                    'id': formated_id,
                    'email': contact[2],
                    'phone': contact[3]}

    return edit_contact(**initial_data)


def handle_list_contacts_request():
    contacts = Contact().all()
    return list_contacts(contacts)


def handle_delete_contact_request():
    id = request.query.get('id')
    Contact().delete(id)
    return redirect('/list-contacts')


def handle_search_contact_request():
    if request.GET.search_button:
        search = request.GET.search
        contacts = Contact().get(search)

        return list_contacts(contacts)


def __get_form_data():
    form_data = {'name': request.GET.name,
                 'id': request.GET.id,
                 'email': request.GET.email,
                 'phone': request.GET.phone}

    return form_data
