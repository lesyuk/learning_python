import pytest
from automation_school.lesson_5.address_book_entry import BookEntry


@pytest.fixture
def entry():
    entry = BookEntry()
    yield entry


@pytest.fixture()
def data():
    yield '1', 'Test', 'Testovich', 'test@test.com', '+79989999999', 'Roga i Kopita'


class TestAddressBook:
    def test_add_entry(self, entry, data):
        entry.add_entry(*data)
        for k, v in entry.book.items():
            assert v is not None

    def test_delete_entry(self, entry, data):
        entry.add_entry(*data)
        entry.delete_entry(data[0])
        assert len(entry.book) == 0



