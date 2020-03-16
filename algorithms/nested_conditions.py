# Пример: хотим распечатать ДА, если число делится на два или делится на 3
x = int(input())

# Первый вариант:
if x % 2 == 0:
    print('ДА')
if x % 3 == 0:
    print('ДА')

# Будет напечатано два раза да, если число делится на 3 и на 2 (условия не исключают друг друга),
# поэтому этот пример не решает задачу

if x % 2 == 0:
    if x % 3 == 0:
        print('На 6')

# Запись эквивалентна записи ниже:
if x % 2 == 0 and x % 3 == 0:
    print('На 6')

# До тех пор, пока не появляется блок else
if x % 2 == 0:
    if x % 3 == 0:
        print('На 6')
else:
    print('Не делится на 6')

if x % 2 == 0 and x % 3 == 0:
    print('На 6')
else:
    print('Не делится на 6')

# В первом примере, если число не делится на 2 и 3, то ничего не будет выведено.
# Во втором примере всегда будет выводиться сообщение из блока else.
# Если переместить else из первого примера во вложенный if, то будет выполняться либо вложенный if, либо вложенный else.
