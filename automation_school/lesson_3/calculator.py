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
      'Для выхода из программы введите команду "close" без кавычек.')

while True:
    while True:
        a = input('Введите первое число: ')
        if a != 'close':
            try:
                a = int(a)
                break
            except ValueError:
                print('Не похоже на число. Попробуйте еще раз.')
                continue
        else:
            exit()

    while True:
        b = input('Введите второе число: ')
        if b != 'close':
            try:
                b = int(b)
                break
            except ValueError:
                print('Не похоже на число. Попробуйте еще раз.')
                continue
        else:
            exit()

    while True:
        operation = input('Введите знак операции: ')
        if operation != 'close':
            if operation not in ['+', '-', '*', '/']:
                print('Неверный знак операции. Попробуйте еще раз.')
                continue
            if operation == '+':
                print(amount(a, b))
                break
            elif operation == '-':
                print(difference(a, b))
                break
            elif operation == '*':
                print(multiplication(a, b))
                break
            elif operation == '/':
                print(division(a, b))
                if division(a, b) == 'Делить на ноль нельзя!':
                    print('Чтобы начать ввод заново введите команду "new" без кавычек.\n'
                          'Для смены знака операции введите команду "retry" без кавычек.\n'
                          'Для выхода из программы введите команду "close" без кавычек.')
                    while True:
                        command = input()
                        if command == 'new':
                            break
                        elif command == 'retry':
                            break
                        elif command == 'close':
                            exit()
                        else:
                            print('Неверная команда. Попробуйте еще раз.')
                            continue
                    if command == 'retry':
                        continue
                    else:
                        break
        else:
            exit()
    continue
