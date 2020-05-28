# import pytest
#
#
# @pytest.fixture()
# def create_students_list():
#     # Можно рассматривать эту функцию как setup и teardown вместе
#     print('\nэта фикстура готовит список студентов')
#     # yield может возвращать значение, которым можно оперировать в тесте
#     yield ['Nastya', 'Masha', 'Lera', 'Lena', 'Max', 'Pasha', 'Kirill', 'Vadim']
#     print('\nи может делать что-то после')
#
#
# class TestToUpper:
#     # Тест-кейс с фикстурой, которая передает значение
#     def test_all_upper(self, create_students_list):
#         lst = create_students_list
#         for student in lst:
#             assert student.upper().isupper()
#
#     # Тест-кейс без фикстуры
#     def test_nothing(self):
#         pass
#
#     # Фикстура some_stuff выполнится только для того тест-кейса, в который была передана
#     def test_fail(self, some_stuff):
#         assert 0
