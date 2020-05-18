from automation_school.lesson_5.work_time_decorator import work_time
import json

dump_file = '/Users/paul/Documents/address_book.txt'


class AddressBook:
    def __init__(self):
        self.book = {}

    @work_time
    def write(self):
        """Writing book data to a file"""
        f = open(dump_file, 'w')
        json.dump(self.book, f)
        f.close()
        print('Данные адресной книги сохранены.')

    @work_time
    def read(self):
        """Writing data to a book from a file"""
        f = open(dump_file, 'r')
        self.book.update(json.load(f))
        print('Данные адресной книги загружены.')
