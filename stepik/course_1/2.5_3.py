'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения,
которые повторяются в нём более одного раза.
'''

a = [int(i) for i in input().split()]
l = len(a)
a.sort()
m = []

if l > 1:
    for i in range(l):
        if a[i] == a[i + 1 - l]:
            if a[i] not in m:
                m.append(a[i])

    for i in range(len(m)):
        print(m[i], end=' ')