lst = [int(i) for i in input().split()]
x = int(input())
s = []

for j in range(len(lst)):
    if x == lst[j]:
        s.append(j)

if len(s) != 0:
    print(*s)
else:
    print('Отсутствует')