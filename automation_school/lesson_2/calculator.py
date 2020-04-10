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
                print('Пожалуйста, введите число.')
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
                print('Пожалуйста, введите число.')
                continue
        else:
            exit()

    while True:
        operation = input('Введите знак операции: ')
        if operation != 'close':
            if operation not in ['+', '-', '*', '/']:
                print('Пожалуйста, введите знак операции из инструкции.')
                break
            if operation == '+':
                print(f'Сумма чисел {a} и {b} равна {a + b}')
                break
            elif operation == '-':
                print(f'Разница чисел {a} и {b} равна {a - b}')
                break
            elif operation == '*':
                print(f'Результат умножения чисел {a} и {b} равен {a * b}')
                break
            elif operation == '/':
                try:
                    print(f'Результат деления чисел {a} и {b} равен {a / b}')
                    break
                except ZeroDivisionError:
                    print('Делить на ноль нельзя!')
                    continue
        else:
            exit()
    continue
