class AddressBook:
    entries_count = 0

    def __init__(self, name, last_name, email, phone, work_place):
        """Add new entry"""
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.work_place = work_place
        AddressBook.entries_count += 1
        print('Запись успешно добавлена')

    def delete_entry(self):
        """Delete obj."""
        AddressBook.entries_count -= 1
        del self
        print(f'Запись удалена. Оставшееся количество записей: {AddressBook.entries_count}')

    def show_entry(self):
        """Print current obj params"""
        print(f'Имя: {self.name}\n'
              f'Фамилия: {self.last_name}\n'
              f'Почтовый адрес: {self.email}\n'
              f'Телефон: {self.phone}\n'
              f'Место работы: {self.work_place}')

    @staticmethod
    def show_entries_count():
        """Print count of objects in the address book."""
        print(f'Количество записей в адресной книге: {AddressBook.entries_count}')


# entry1 = AddressBook('Павел', 'Лесюк', 'paul.lesyuk@gmail.com', '+79777097967', 'Циан')
# entry2 = AddressBook('Алексей', 'Гончаров', 'alexey.goncharov@gmail.com', '+79989999999', 'Тинькофф Банк')
# entry1.show_entry()
# entry2.show_entry()
# AddressBook.show_entries_count()
# entry1.delete_entry()
# entry2.delete_entry()
