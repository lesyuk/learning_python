a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a in [c + 1, c, c - 1] and b in [d + 1, d, d - 1]:
    print([c + 1, c, c - 1])
    print('YES')
else:
    print('NO')