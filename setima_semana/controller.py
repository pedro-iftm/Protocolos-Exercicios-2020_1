from model import read_file, write_file
from view import access_denied, successfully_authenticated, login_page


def handle_request(request):
    if request.GET.button:
        if __is_authenticated(request):
            return successfully_authenticated(request.GET.user)

        write_file(request.GET.user)
        file_content = read_file()
        users = set(file_content)
        user_attempts = []

        for user in users:
            attemps = file_content.count(user)
            user_attempts.append((user, attemps))

        return access_denied(user_attempts)

    return login_page()


def __is_authenticated(request):
    user = request.GET.user
    password = request.GET.password

    if user == 'pedro' and password == '123':
        return True

    return False
