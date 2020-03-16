x = [int(i) for i in input().split()]
n = []

for i in range(len(x)):
    if len(n) < 2:
        if i != len(x) - 1:
            if x[i] > 0 and x[i + 1 - len(x)] > 0:
                n += x[i], x[i + 1 - len(x)]
            elif x[i] < 0 and x[i + 1 - len(x)] < 0:
                n += x[i], x[i + 1 - len(x)]
    else:
        break

[print(i, end=' ') for i in n]

# Решение разработчиков

a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i - 1] * a[i] > 0:
        print(a[i - 1], a[i])
        break
