import pickle
import time
dump_file = '/Users/paul/Documents/address_book.txt'


def work_time(func_to_decorate):
    """Calculates function run time"""
    def wrapper(*args):
        start_time = time.time()
        func_to_decorate(*args)
        print(f'Время выполнения операции: {time.time() - start_time}\n')
    return wrapper


class AddressBook:
    def __init__(self):
        self.entry = {}

    def add_entry(self, name, last_name, email, phone, work_place):
        """Create a book entry with a phone as ID"""
        self.entry.update({phone: {'Имя': name,
                                   'Фамилия': last_name,
                                   'Email': email,
                                   'Телефон': phone,
                                   'Место работы': work_place}})

    def delete_entry(self, phone):
        """Delete a book entry by phone"""
        del self.entry[phone]

    def show_entry(self):
        """Show all entries in the book"""
        if len(self.entry) == 0:
            print('Записей нет.\n')
        for self.value in self.entry.values():
            for k, v in self.value.items():
                print(f'{k}: {v}')
            print()

    @work_time
    def write(self):
        """Writing book data to a file"""
        f = open(dump_file, 'wb')
        pickle.dump(self.entry, f)
        f.close()

    @work_time
    def read(self):
        """Writing data to a book from a file"""
        f = open(dump_file, 'rb')
        self.entry.update(pickle.load(f))


address_book = AddressBook()
address_book.add_entry('Павел', 'Лесюк', 'paul.lesyuk@gmail.com', '+79777097967', 'Циан')
address_book.show_entry()
address_book.write()
address_book.delete_entry('+79777097967')
address_book.show_entry()
address_book.read()
address_book.show_entry()
