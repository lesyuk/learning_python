from automation_school.lesson_5.address_book import AddressBook
from pprint import pprint


class BookEntry(AddressBook):
    def add_entry(self, entry_id, name, last_name, email, phone, work_place):
        """Create a book entry"""
        self.book.update({entry_id: {'Имя': name,
                                     'Фамилия': last_name,
                                     'Email': email,
                                     'Телефон': phone,
                                     'Место работы': work_place}})

    def delete_entry(self, entry_id):
        """Delete a book entry by ID"""
        if len(self.book) != 0:
            del self.book[entry_id]
            print('Запись удалена.\n')
        else:
            print('Записей нет.\n')

    def show_entries(self):
        """Show all entries in the book"""
        if len(self.book) == 0:
            print('Записей нет.\n')
        else:
            pprint(self.book)
            print()

        # Old code
        # for entry_id, value in self.book.items():
        #     print(f'ID: {entry_id}')
        #     for k, v in value.items():
        #         print(f'{k}: {v}')
        #     print()


# AddressBook work example
if __name__ == '__main__':
    entry = BookEntry()
    entry.add_entry('1', 'Test', 'Testovich', 'test@test.com', '+79989999999', 'Roga i Kopita')
    entry.show_entries()
    entry.write()
    entry.delete_entry('1')
    print(entry.book == True)
