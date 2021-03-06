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


address_book = AddressBook()
address_book.add_entry('Павел', 'Лесюк', 'paul.lesyuk@gmail.com', '+79777097967', 'Циан')
address_book.show_entry()
address_book.delete_entry('+79777097967')
address_book.show_entry()
