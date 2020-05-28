# """
# В файле conftest.py хранятся частоиспользуемые и универсальные фикстуры.
# Этот модуль не нужно импортировать, pytest сам его найдет.
# """
# import pytest
#
#
# @pytest.fixture(scope='session', autouse=True)
# def session_scope_func():
#     print('\nЗапуск тест-рана') # какая-то логика до тестов
#     yield # прогон тестов
#     print('\nТест-ран завершен') # какая-то логика после тестов
#
#
# @pytest.fixture()
# def some_stuff():
#     print('\nЗапуск тест-кейса')
#     yield
#     print('\nТест-кейс выполнен')