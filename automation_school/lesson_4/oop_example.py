# ---------------------------------------------------------------------------------------------------------------------
# Простейший класс


# class SomeClassTemplate:
#     ...
#
#
# print(SomeClassTemplate)
#
# instance = SomeClassTemplate()
# print(instance)
#
# print(type(SomeClassTemplate), type(instance))
#
# print(isinstance(instance, SomeClassTemplate))
#
# another_instance = SomeClassTemplate()
# another_another_instance = SomeClassTemplate()
#
# print(isinstance(another_instance, SomeClassTemplate))
# print(instance is another_instance)


# ---------------------------------------------------------------------------------------------------------------------
# Класс и его атрибуты


# class SomeClassTemplate:
#     SOME_CONST = 42
#
#     def create_internal_value(self, internal_value: int = 0):
#         self.internal_value = internal_value
#         self.SOME_CONST = 0
#
#     def show_internal_value(self):
#         print(self.internal_value)
#
#
# instance = SomeClassTemplate()
# print(instance.SOME_CONST)
#
# instance.create_internal_value(359)
# SomeClassTemplate.create_internal_value(instance, 359)
#
# instance.show_internal_value()
#
#
# """
# create_internal_value(value) и show_internal_value - методы класса
# SOME_CONST - поле класса. переменная класса
# self.internal_value - поле класса. переменная экземпляра класса
#
# все вместе они - атрибуты класса
# """


# ---------------------------------------------------------------------------------------------------------------------
# Класс с конструктором


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print(f'Привет,  меня зовут {self.name}')

# # niko = Person()  # TypeError: __init__() missing 1 required positional argument: 'name'
# niko = Person('Niko')
# niko.introduce()
# maxim = Person('Maxim')
# maxim.introduce()


# ---------------------------------------------------------------------------------------------------------------------
# Абстракция, Наследование, Полиморфизм, Инкапсуляция


# class Animal:
#     def __init__(self, sounds: str):
#         self.sounds = sounds
#
#     def vocalize(self):
#         print(f'{self.__class__.__name__} says {self.sounds}')
#
#
# class Dog(Animal):
#     ...
#
#
# class Cat(Animal):
#     ...
#
#
# class Tiger(Animal):
#     ...
#
#
# dog = Dog('bark!')
# cat = Cat('meow!')
# tiger = Tiger('roar!')
#
# dog.vocalize()
# cat.vocalize()
# tiger.vocalize()


# ---------------------------------------------------------------------------------------------------------------------
# Наследование

#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print(f'Привет,  меня зовут {self.name}')

#
# class Employee(Person):
#     ...


# niko = Employee()  # TypeError: __init__() missing 1 required positional argument: 'name'
# niko = Person('Niko')
# niko = Employee('Niko')
# niko.introduce()

#
# class Employee(Person):
#     def __init__(self, name, employer, position):
#         super().__init__(name)
#         self.employer = employer
#         self.position = position
#
#     def introduce(self):
#         super().introduce()
#         print(f'Я работаю в {self.employer} на должности {self.position}')
#
#
# niko = Person('Niko')
# niko.introduce()
#
# niko = Employee('Niko', 'ЦИАН', 'Инженер по автоматизации')
# niko.introduce()