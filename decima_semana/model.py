from os import path


def write_file(record):
    mode = 'a' if __has_file() else 'w'

    with open('students.txt', mode) as file:
        file.write(record + '\n')


def read_file():
    if not __has_file():
        return

    with open('students.txt', 'r') as file:
        content = []
        for line in file:
            formated_line = line.replace('\n', '').split(';')
            content.append(formated_line)

    return content


def __has_file():
    return path.exists('students.txt') and path.isfile('students.txt')
