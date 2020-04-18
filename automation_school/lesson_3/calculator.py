def number_input():
    number = input('Введите число: ')
    if type(number_validation(number)) == float:
        return number_validation(number)


def number_validation(number):
    if number != 'close':
        try:
            return float(number)
        except ValueError:
            print('Не похоже на число. Попробуйте еще раз.')
            number_input()
    else:
        exit()


def operation_sign_input_and_validation():
    sign = input('Введите знак операции: ')
    if sign != 'close':
        if sign in ['+', '-', '*', '/']:
            return sign
        else:
            print('Неверный знак операции. Попробуйте еще раз.')
            return operation_sign_input_and_validation()
    else:
        exit()


def amount(a, b):
    return f'Сумма чисел {a} и {b} равна {a + b}'


def difference(a, b):
    return f'Разница чисел {a} и {b} равна {a - b}'


def multiplication(a ,b):
    return f'Результат умножения чисел {a} и {b} равен {a * b}'


def division(a, b):
    try:
        return f'Результат деления чисел {a} и {b} равен {a / b}'
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'


print('Добро пожаловать в калькулятор. Доступные операции: \n'
      '+\n'
      '-\n'
      '*\n'
      '/\n'
      'На вход программе подается два числа и знак операции.\n'
      'Для выхода из программы введите команду "close" без кавычек.')

while True:
    a = number_input()
    b = number_input()
    operation_sign = operation_sign_input_and_validation()
    if operation_sign == '+':
        print(amount(a, b))
        continue
    elif operation_sign == '-':
        print(difference(a, b))
        continue
    elif operation_sign == '*':
        print(multiplication(a, b))
        continue
    elif operation_sign == '/':
        print(division(a, b))
        continue
