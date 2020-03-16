# Пример: если хотя бы одно числоделится на 10, то flag = True

N = int(input())
flag = False
for i in range(N):
    x = int(input())
    flag = (x % 10 == 0) or flag
    print(flag)

"""
Последняя строчка заменяет выражение
if x % 10 == 0:
    flag == True
"""

# Обратный пример: если все из чисел делятся на 10, то flag = True, иначе = False

N = int(input())
flag = True
for i in range(N):
    x = int(input())
    flag = (flag and # можно брать строку в скобку и переносить на следующую, если она не умещается на текущей
            x % 10 == 0)
    print(flag)