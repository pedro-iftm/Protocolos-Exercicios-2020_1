from bottle import redirect, request

from model import read_file, write_file
from view import add_contact, list_contacts, index


def handle_add_contacts_request():
    if request.GET.button:
        name = request.GET.name
        age = request.GET.age
        contact = request.GET.contact

        if name or age or contact:
            if name and age and contact:
                write_file(f'{name};{age};{contact}')
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
