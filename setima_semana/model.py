from os import path


def write_file(user):
    mode = 'a' if __has_file() else 'w'

    with open('attempts.txt', mode) as file:
        file.write(user + '\n')


def read_file():
    if not __has_file():
        return

    with open('attempts.txt', 'r') as file:
        content = ''
        for line in file:
            content += line

    return content.split()


def __has_file():
    return path.exists('attempts.txt') and path.isfile('attempts.txt')
