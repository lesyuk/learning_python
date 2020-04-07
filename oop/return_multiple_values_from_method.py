# Методы класса могут возвращать множественные значения


class Square:

    @staticmethod
    def get_squares(a, b):
        return a * a, b * b


print(Square.get_squares(3, 5))