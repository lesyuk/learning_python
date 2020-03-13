steps_number = 0


# n — количество колец, start — начальный колышек, finish — колышек, на который нужно переместить все кольца
def move(n, start, finish):
    global steps_number
    steps_number += 1
    # у всех вызванных в стеке функций по мере вычета из n единицы n станет равно 1
    # как только у какой-то функции в стеке вызовов выполняется тело конструкции if, она прекращает выполнение
    if n == 1:
        print(n, 'from', start, 'to', finish)
    else:
        # 6 — сумма номеров колышков, buf — промежуточный колышек, номер которого нужно узнать
        buf = 6 - start - finish
        # 1 этап — переносим все диски n-1 со start на buf, finish — промежуточный колышек
        move(n - 1, start, buf)
        # 2 этап: переносим диск n со start на finish
        print(n, 'from', start, 'to', finish)
        # 3 этап: переносим все диски n-1 с buf на finish, start — промежуточный колышек
        move(n - 1, buf, finish)


n = int(input())
move(n, 1, 3)
print('Steps to transfer:', steps_number)
