from model import read_file, write_file, rewrite_file


class Contact:
    def add(self, name, id, email, phone):
        write_file(f'{name};{id};{email};{phone}')

    def edit(self, name, id, email, phone):
        self.__remove_row_from_file(id)
        write_file(f'{name};{id};{email};{phone}')

    def delete(self, id):
        self.__remove_row_from_file(id)

    def all(self, filter=None):
        return read_file()

    def get(self, value):
        file = read_file()
        file = [row for row in file if value in str(row)]
        return file

    def __remove_row_from_file(self, value):
        file = read_file()
        record = [row for row in file if value in row]
        file.remove(record[0])

        file = [';'.join(row) for row in file]
        rewrite_file(file)
