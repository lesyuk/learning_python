# Статический метод — тип методов, который может быть вызван напрямую при помощи имени класса


class Car:

    @staticmethod
    def get_class_details():
        print("Это класс Car")


Car.get_class_details()