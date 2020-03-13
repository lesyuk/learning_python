a = [int(i) for i in input().split()]
if len(a) % 2 == 0:
    e = len(a)
else:
    e = len(a) - 1
for i in range(e):
    if i % 2 == 0:
        v = a[i]
        a[i] = a[i + 1 - len(a)]
        a[i + 1 - len(a)] = v
[print(i, end=' ') for i in a]