from model import read_file, write_file
from view import access_denied, successfully_authenticated, login_page


def handle_request(request):
    if request.GET.button:
        if __is_authenticated(request):
            return successfully_authenticated(request.GET.user)

        write_file(request.GET.user)
        attempts = ', '.join(read_file())

        return access_denied(attempts)

    return login_page()


def __is_authenticated(request):
    user = request.GET.user
    password = request.GET.password

    if user == 'pedro' and password == '123':
        return True

    return False
