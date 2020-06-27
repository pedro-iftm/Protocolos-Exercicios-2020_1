from bottle import redirect, request

from model import read_file, write_file
from view import add_contact, list_contacts


def handle_add_contacts_request():
    if request.GET.button:
        name = request.GET.name
        age = request.GET.age
        gender = request.GET.gender

        if name or age or gender:
            if name and age and gender:
                write_file(f'{name};{age};{gender}')
            else:
                return add_contact('Preencha todos os dados')

        file = read_file()

        return (redirect('/list-contacts') if file
                else add_contact('O arquivo está vazio'))

    return add_contact()


def handle_list_contacts_request():
    return list_contacts(read_file())
