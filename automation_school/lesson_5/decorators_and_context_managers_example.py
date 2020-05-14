# ---------------------------------------------------------------------------------------------------------------------
# Декоратор


def this_is_decorator(func_to_decorate):
    def wrapper():
        print('\nДекоратор начинает работу')
        print('Смотри, здесь возможна какая-то дополнительная логика, перед запуском функции')
        print('*' * 80)
        func_to_decorate()
        print('*' * 80)
        print('А здесь возможна какая-то дополнительная логика, после запуска функции')
        print('Декоратор заканчивает работу\n')
    return wrapper


def this_is_function():
    # some rocket science logic
    print(f'\nЯ функция. Здесь происходит какая-то логика\n')


this_is_function()

# # Не самый популярный вариант использования декоратора. Встречается редко
# this_is_decorated_function = this_is_decorator(this_is_function)
# this_is_decorated_function()


@this_is_decorator
def this_is_initially_decorated_function():
    # some rocket science logic
    print(f'\nЯ декорированная функция. Здесь происходит какая-то логика\n')


this_is_initially_decorated_function()


# ---------------------------------------------------------------------------------------------------------------------
# Декоратор. Несколько декораторов


# def deco_01(func):
#     def wrapper():
#         print('Deco 01. Start')
#         func()
#         print('Deco 01. End')
#     return wrapper
#
#
# def deco_02(func):
#     def wrapper():
#         print('Deco 02. Start')
#         func()
#         print('Deco 02. End')
#     return wrapper
#
#
# @deco_02
# @deco_01
# def decorate_me():
#     print('\nSome logic\n')
#
#
# decorate_me()


# ---------------------------------------------------------------------------------------------------------------------
# Декоратор. Атрибуты


# def deco(func):
#     def wrapper
#     :
#         print('Декоратор. Логика перед стартом')
#         func(*args, **kwargs)
#         print('Декоратор. Логика в конце')
#     return wrapper
#
#
# def deco(func):
#     def wrapper(a, b, c):
#         print('Декоратор. Логика перед стартом')
#         print(f'Я получил a={a}, b={b}, c={c}')
#         a, b, c = 5, 5, 5
#         print(f'И подменил их на a={a}, b={b}, c={c}')
#         func(a, b, c)
#         print('Декоратор. Логика в конце')
#     return wrapper
#
#
# @deco
# def some_func_with_parameters(a, b, c):
#     print(f'\n{a}+{b}+{c}={a+b+c}\n')
#
#
# some_func_with_parameters(1, 1, 1)


# ---------------------------------------------------------------------------------------------------------------------
# Декораторы для методов


# def method_deco(method_to_decorate):
#     def wrapper(self):
#         self.age += 3
#         return method_to_decorate(self)
#     return wrapper
#
#
# class Person:
#     def __init__(self, age):
#         self.age = age
#
#     @method_deco
#     def say(self):
#         print(f'Дайте винстон синий и ягуар. Мне уже {self.age} лет')
#
#
# p = Person(age=15)
# p.say()


# ---------------------------------------------------------------------------------------------------------------------
# Менджеры контекста


import random
from contextlib import contextmanager


# @contextmanager
# def random_func():
#     print('Логика до')
#     yield random.randint(0, 100)
#     print('Логика после')
#
#
# with random_func() as r:
#     print('\nВнутренняя логика', r, '\n')
#
# #
# @contextmanager
# def divide_securely(a, b):
#     try:
#         yield a / b
#     except ZeroDivisionError:
#         yield 'На ноль делить нельзя'
#
#
# with divide_securely(2, 0) as ds:
#     print(ds)
#
# with divide_securely(2, 2) as ds:
#     print(ds)


# ---------------------------------------------------------------------------------------------------------------------
# Менджеры контекста в природе


# with open('my_file.txt', 'w+') as file:
#     file.write('Hello world!')
#
# with open('my_file.txt', 'r') as file:
#     print(file.read())