from bottle import redirect, request

from model import read_file, write_file
from view import add_contact, list_contacts, index


def handle_add_contacts_request():
    if request.GET.button:
        name = request.GET.name
        id = request.GET.id
        email = request.GET.email
        phone = request.GET.phone

        if name or id or email or phone:
            if name and id and email and phone:
                write_file(f'{name};{id};{email};{phone}')
            else:
                return add_contact('Preencha todos os dados')

        file = read_file()

        return (redirect('/list-contacts') if file
                else add_contact('O arquivo está vazio'))

    return add_contact()


def handle_list_contacts_request():
    return list_contacts(read_file())


def handle_index_request():
    return index()
